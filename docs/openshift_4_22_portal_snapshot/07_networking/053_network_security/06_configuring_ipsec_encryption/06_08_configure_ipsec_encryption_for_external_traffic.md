# 6.8. Configure IPsec encryption for external traffic

To configure IPsec encryption for traffic between OpenShift Container Platform and external hosts, you can create Butane machine configs with PKCS#12 certificates and apply them to cluster nodes. 

Note

After you apply the machine config, the Machine Config Operator (MCO) reboots affected nodes in your cluster to rollout the new machine config. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * You have installed the `butane` tool on your local computer. For more information, see "Installing Butane". 
  * You have installed the NMState Operator on the cluster. 
  * You logged in to the cluster as a user with `cluster-admin` privileges. 
  * You have an existing PKCS#12 certificate for the IPsec endpoint and a CA cert in Privacy Enhanced Mail (PEM) format. 
  * You enabled IPsec in either `Full` or `External` mode on your cluster. 
  * You must set the `routingViaHost` parameter to `true` in the `ovnKubernetesConfig.gatewayConfig` specification of the OVN-Kubernetes network plugin. 



**Procedure**

  1. Create an IPsec configuration with an NMState Operator node network configuration policy. For more information, see [Configuring an IPsec based VPN connection by using nmstatectl](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/setting-up-an-ipsec-vpn_configuring-and-managing-networking#configuring-an-ipsec-based-vpn-connection-by-using-nmstatectl_setting-up-an-ipsec-vpn). 

     1. To identify the IP address of the cluster node that is the IPsec endpoint, enter the following command: 

```plaintext
$ oc get nodes
```


     2. Create a file named `ipsec-config.yaml` that has a node network configuration policy for the NMState Operator, such as in the following examples. For an overview about `NodeNetworkConfigurationPolicy` objects, see [The Kubernetes NMState project](https://nmstate.io/kubernetes-nmstate/). 

**Example NMState IPsec transport configuration**

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: ipsec-config
spec:
  nodeSelector:
    kubernetes.io/hostname: "<hostname>"
  desiredState:
    interfaces:
    - name: <interface_name>
      type: ipsec
      libreswan:
        left: <cluster_node>
        leftid: '%fromcert'
        leftrsasigkey: '%cert'
        leftcert: left_server
        leftmodecfgclient: false
        right: <external_host>
        rightid: '%fromcert'
        rightrsasigkey: '%cert'
        rightsubnet: <external_address>/32
        ikev2: insist
        type: transport
```


where: 

`kubernetes.io/hostname`
     Specifies the hostname to apply the policy to. This host serves as the left side host in the IPsec configuration. 
`name`
     Specifies the name of the interface to create on the host. 
`left`
     Specifies the hostname of the cluster node that terminates the IPsec tunnel on the cluster side. The name must match the SAN `[Subject Alternate Name]` from your supplied PKCS#12 certificates. 
`right`
     Specifies the external hostname, such as `host.example.com`. The name should match the SAN `[Subject Alternate Name]` from your supplied PKCS#12 certificates. 
`rightsubnet`
    

Specifies the IP address of the external host, such as `10.1.2.3/32`. 

**Example NMState IPsec tunnel configuration**

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: ipsec-config
spec:
  nodeSelector:
    kubernetes.io/hostname: "<hostname>"
  desiredState:
    interfaces:
    - name: <interface_name>
      type: ipsec
      libreswan:
        left: <cluster_node>
        leftid: '%fromcert'
        leftmodecfgclient: false
        leftrsasigkey: '%cert'
        leftcert: left_server
        right: <external_host>
        rightid: '%fromcert'
        rightrsasigkey: '%cert'
        rightsubnet: <external_address>/32
        ikev2: insist
        type: tunnel
```


     3. To configure the IPsec interface, enter the following command: 

```shell-session
$ oc create -f ipsec-config.yaml
```


  2. Give the following certificate files to add to the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in the next steps. 

     * `left_server.p12`: The certificate bundle for the IPsec endpoints 
     * `ca.pem`: The certificate authority that you signed your certificates with 

  3. Create a machine config to add your certificates to the cluster. 
  4. Read the password from a mounted secret file: 

```shell-session
$ password=$(cat run/secrets/<left_server_password>)
```


     * `left_server_password`:: The name of the file that contains the password. This file exists in the mounted secret. 

  5. Use the `pk12util` tool, which comes prepackaged with Red Hat Enterprise Linux (RHEL), to specify a password that protects `PKCS#12` files by entering the following command. Ensure that you replace the `<password>` value with your password. 

```shell-session
$ pk12util -W "<password>" -i /etc/pki/certs/left_server.p12 -d /var/lib/ipsec/nss/
```


  6. To create Butane config files for the control plane and compute nodes, enter the following command: 

Note

The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane. 

```shell-session
$ for role in master worker; do
  cat >> "99-ipsec-${role}-endpoint-config.bu" <<-EOF
  variant: openshift
  version: 4.22.0
  metadata:
    name: 99-${role}-import-certs
    labels:
      machineconfiguration.openshift.io/role: $role
  systemd:
    units:
    - name: ipsec-import.service
      enabled: true
      contents: |
        [Unit]
        Description=Import external certs into ipsec NSS
        Before=ipsec.service

        [Service]
        Type=oneshot
        ExecStart=/usr/local/bin/ipsec-addcert.sh
        RemainAfterExit=false
        StandardOutput=journal

        [Install]
        WantedBy=multi-user.target
  storage:
    files:
    - path: /etc/pki/certs/ca.pem
      mode: 0400
      overwrite: true
      contents:
        local: ca.pem
    - path: /etc/pki/certs/left_server.p12
      mode: 0400
      overwrite: true
      contents:
        local: left_server.p12
    - path: /usr/local/bin/ipsec-addcert.sh
      mode: 0740
      overwrite: true
      contents:
        inline: |
          #!/bin/bash -e
          echo "importing cert to NSS"
          certutil -A -n "CA" -t "CT,C,C" -d /var/lib/ipsec/nss/ -i /etc/pki/certs/ca.pem
          pk12util -W "" -i /etc/pki/certs/left_server.p12 -d /var/lib/ipsec/nss/
          certutil -M -n "left_server" -t "u,u,u" -d /var/lib/ipsec/nss/
EOF
done
```


  7. To transform the Butane files that you created in the earlier step into machine configs, enter the following command: 

```shell-session
$ for role in master worker; do
  butane -d . 99-ipsec-${role}-endpoint-config.bu -o ./99-ipsec-$role-endpoint-config.yaml
done
```


  8. To apply the machine configs to your cluster, enter the following command: 

```shell-session
$ for role in master worker; do
  oc apply -f 99-ipsec-${role}-endpoint-config.yaml
done
```


Important

As the Machine Config Operator (MCO) updates machines in each machine config pool, it reboots each node one by one. You must wait for all the nodes to update before external IPsec connectivity is available. 




**Verification**

  1. Check the machine config pool status by entering the following command: 

```shell-session
$ oc get mcp
```


A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`. 

Note

By default, the MCO updates one machine per pool at a time, causing the total time the migration takes to increase with the size of the cluster. 

  2. To confirm that IPsec machine configs rolled out successfully, enter the following commands: 

     1. Confirm the creation of the IPsec machine configs: 

```shell-session
$ oc get mc | grep ipsec
```


**Example output**

```plaintext
80-ipsec-master-extensions        3.2.0        6d15h
80-ipsec-worker-extensions        3.2.0        6d15h
```


     2. Confirm you have applied the IPsec extension to control plane nodes: 

```shell-session
$ oc get mcp master -o yaml | grep 80-ipsec-master-extensions -c
```


     3. Confirm the application of the IPsec extension to compute nodes. Example output would show `2`. 

```shell-session
$ oc get mcp worker -o yaml | grep 80-ipsec-worker-extensions -c
```
