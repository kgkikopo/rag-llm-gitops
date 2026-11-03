# 6.3. Create the preferred configuration inputs

Create the preferred configuration inputs used to create the PXE files. 

Note

Configuring the `install-config.yaml` and `agent-config.yaml` files is the preferred method for using the Agent-based Installer. Using GitOps ZTP manifests is optional. 

**Procedure**

  1. Install the `nmstate` dependency by running the following command: 

```shell-session
$ sudo dnf install /usr/bin/nmstatectl -y
```


  2. Place the `openshift-install` binary in a directory that is on your PATH. 
  3. Create a directory to store the install configuration by running the following command: 

```shell-session
$ mkdir ~/<directory_name>
```


  4. Create the `install-config.yaml` file by running the following command: 

```shell-session
$ cat << EOF > ./<directory_name>/install-config.yaml
apiVersion: v1
baseDomain: test.example.com
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  replicas: 0
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  replicas: 1
metadata:
  name: sno-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
pullSecret: '<pull_secret>'
sshKey: '<ssh_pub_key>'
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
EOF
```


where: 

`compute.architecture`
    

Specifies the system architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`. 

If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command. For more information, see "Verifying the supported architecture for installing an Agent-based Installer cluster". 

`metadata.name`
     Specifies your cluster name. This value is required. 
`networking.networkingType`
     Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value. 
`platform`
    

Specifies your platform. If you set the platform to `vSphere`, `baremetal`, or `none`, you can configure IP address endpoints for cluster nodes in three ways: IPv4, IPv6, or IPv4 and IPv6 in parallel (dual-stack). 

**Example of dual-stack networking**

```yaml
networking:
  clusterNetwork:
    - cidr: 172.21.0.0/16
      hostPrefix: 23
    - cidr: fd02::/48
      hostPrefix: 64
  machineNetwork:
    - cidr: 192.168.11.0/16
    - cidr: 2001:DB8::/32
  serviceNetwork:
    - 172.22.0.0/16
    - fd03::/112
  networkType: OVNKubernetes
platform:
  baremetal:
    apiVIPs:
    - 192.168.11.3
    - 2001:DB8::4
    ingressVIPs:
    - 192.168.11.4
    - 2001:DB8::5
```


Note

For bare-metal platforms, host settings made in the platform section of the `install-config.yaml` file are used by default, unless they are overridden by configurations made in the `agent-config.yaml` file. 

`pullSecret`
     Specifies your pull secret. 
`sshKey`
     Specifies your SSH public key. 
`additionalTrustBundle`
     Specifies the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry. You must specify this parameter if you are using a disconnected mirror registry. 
`imageContentSources`
    

Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository. You must specify this parameter if you are using a disconnected mirror registry. 

Important

     * When using the `oc adm release mirror` command, use the output from the `imageContentSources` section. 
     * When using the `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command. 
     * The `ImageContentSourcePolicy` resource is deprecated. 

  5. Create the `agent-config.yaml` file by running the following command: 

```shell-session
$ cat > agent-config.yaml << EOF
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: sno-cluster
rendezvousIP: 192.168.111.80
hosts:
  - hostname: master-0
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a5
    rootDeviceHints:
      deviceName: /dev/sdb
    networkConfig:
      interfaces:
        - name: eno1
          type: ethernet
          state: up
          mac-address: 00:ef:44:21:e6:a5
          ipv4:
            enabled: true
            address:
              - ip: 192.168.111.80
                prefix-length: 23
            dhcp: false
      dns-resolver:
        config:
          server:
            - 192.168.111.1
      routes:
        config:
          - destination: 0.0.0.0/0
            next-hop-address: 192.168.111.2
            next-hop-interface: eno1
            table-id: 254
EOF
```


where: 

`rendezvousIP`
     Specifies the IP address used to determine which node performs the bootstrapping process as well as running the `assisted-service` component. You must provide the rendezvous IP address when you do not specify at least one host’s IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided hosts' `networkConfig`. 
`hosts`
     Specifies host configuration. The number of hosts defined must not exceed the total number of hosts defined in the `install-config.yaml` file, which is the sum of the values of the `compute.replicas` and `controlPlane.replicas` parameters. This configuration is optional. 
`hosts.hostname`
     Specifies a value that overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods. This configuration is optional. 
`hosts.rootDeviceHints`
    

Specifies a configuration that enables provisioning of the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value. 

Note

This parameter is mandatory for FCP multipath configurations on IBM Z. 

`hosts.networkConfig`
     Specifies the network interface configuration of a host in NMState format. This configuration is optional. 

  6. Optional: To create an iPXE script, add the `bootArtifactsBaseURL` to the `agent-config.yaml` file: 

```yaml
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: sno-cluster
rendezvousIP: 192.168.111.80
bootArtifactsBaseURL: <asset_server_URL>
```


Where `<asset_server_URL>` is the URL of the server you will upload the PXE assets to. 




**Additional resources**

  * [Deploying with dual-stack networking](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#modifying-install-config-for-dual-stack-network_ipi-install-installation-workflow)
  * [Configuring the install-config yaml file](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#configuring-the-install-config-file_ipi-install-installation-workflow)
  * [Configuring a three-node cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installation-three-node-cluster_installing-restricted-networks-bare-metal)
  * [About root device hints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/preparing-to-install-with-agent-based-installer#root-device-hints_preparing-to-install-with-agent-based-installer "1.4.2. About root device hints")
  * [NMState state examples (NMState documentation)](https://nmstate.io/examples.html)
  * [Creating additional manifest files](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/installing-with-agent-based-installer#installing-ocp-agent-opt-manifests_installing-with-agent-based-installer "4.5. Creating additional manifest files")
