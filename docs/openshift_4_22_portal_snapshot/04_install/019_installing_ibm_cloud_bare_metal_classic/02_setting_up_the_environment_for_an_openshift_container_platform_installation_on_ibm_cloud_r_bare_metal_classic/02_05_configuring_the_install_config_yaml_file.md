# 2.5. Configuring the install-config.yaml file

To configure OpenShift Container Platform for IBM Cloud® Bare Metal (Classic) infrastructure, you can edit the `install-config.yaml` file to set the required IPMI privilege level and hardware parameters for your bare-metal nodes. 

The `install-config.yaml` file requires some additional details. Most of the information is teaching the installation program and the resulting cluster enough about the available IBM Cloud® Bare Metal (Classic) hardware so that it is able to fully manage it. The material difference between installing on bare metal and installing on IBM Cloud® Bare Metal (Classic) is that you must explicitly set the privilege level for IPMI in the BMC section of the `install-config.yaml` file. 

**Procedure**

  1. Configure `install-config.yaml`. Change the appropriate variables to match the environment, including `pullSecret` and `sshKey`. 

```yaml
apiVersion: v1
baseDomain: <domain>
metadata:
  name: <cluster_name>
networking:
  machineNetwork:
  - cidr: <public-cidr>
  networkType: OVNKubernetes
compute:
- name: worker
  replicas: 2
controlPlane:
  name: master
  replicas: 3
  platform:
    baremetal: {}
platform:
  baremetal:
    apiVIP: <api_ip>
    ingressVIP: <wildcard_ip>
    provisioningNetworkInterface: <NIC1>
    provisioningNetworkCIDR: <CIDR>
    hosts:
      - name: openshift-master-0
        role: master
        bmc:
          address: ipmi://10.196.130.145?privilegelevel=OPERATOR
          username: root
          password: <password>
        bootMACAddress: 00:e0:ed:6a:ca:b4
        rootDeviceHints:
          deviceName: "/dev/sda"
      - name: openshift-worker-0
        role: worker
        bmc:
          address: ipmi://<out-of-band-ip>?privilegelevel=OPERATOR
          username: <user>
          password: <password>
        bootMACAddress: <NIC1_mac_address>
        rootDeviceHints:
          deviceName: "/dev/sda"
pullSecret: '<pull_secret>'
sshKey: '<ssh_pub_key>'
```


where: 

`bmc.address`
     Specifies the IPMI address with `privilegelevel=OPERATOR`. IBM Cloud® Bare Metal (Classic) infrastructure requires this privilege level. 
`bootMACAddress`
    

Specifies the MAC address of the private `provisioning` network NIC for the corresponding node. 

Note

You can use the `ibmcloud` command-line utility to retrieve the password. 

```shell-session
$ ibmcloud sl hardware detail <id> --output JSON | \
  jq '"(.networkManagementIpAddress) (.remoteManagementAccounts[0].password)"'
```


Replace `<id>` with the ID of the node. 

  2. Create a directory to store the cluster configuration: 

```shell-session
$ mkdir ~/clusterconfigs
```


  3. Copy the `install-config.yaml` file into the directory: 

```shell-session
$ cp install-config.yaml ~/clusterconfigs
```


  4. Power off all bare-metal nodes before installing the OpenShift Container Platform cluster: 

```shell-session
$ ipmitool -I lanplus -U <user> -P <password> -H <management_server_ip> power off
```


  5. Remove old bootstrap resources if any remain from an earlier deployment try: 

```bash
for i in $(sudo virsh list | tail -n +3 | grep bootstrap | awk {'print $2'});
do
  sudo virsh destroy $i;
  sudo virsh undefine $i;
  sudo virsh vol-delete $i --pool $i;
  sudo virsh vol-delete $i.ign --pool $i;
  sudo virsh pool-destroy $i;
  sudo virsh pool-undefine $i;
done
```
