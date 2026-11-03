# 4.5. Creating additional manifest files

As an optional task, you can create additional manifests to further configure your cluster beyond the configurations available in the `install-config.yaml` and `agent-config.yaml` files. 

Important

Customizations to the cluster made by additional manifests are not validated, are not guaranteed to work, and might result in a nonfunctional cluster. 

## 4.5.1. Creating a directory to contain additional manifests

If you create additional manifests to configure your Agent-based installation beyond the `install-config.yaml` and `agent-config.yaml` files, you must create an `openshift` subdirectory within your installation directory. 

All of your additional machine configurations must be located within this subdirectory. 

Note

The most common type of additional manifest you can add is a `MachineConfig` object. For examples of `MachineConfig` objects you can add during the Agent-based installation, see "Using MachineConfig objects to configure nodes" in the "Additional resources" section. 

**Procedure**

  * On your installation host, create an `openshift` subdirectory within the installation directory by running the following command: 

```shell-session
$ mkdir <installation_directory>/openshift
```


**Additional resources**

  * [Using MachineConfig objects to configure nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-configs-configure)



## 4.5.2. Creating a manifest object that includes a customized br-ex bridge

By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, use the Agent-based Installer to create a `MachineConfig` object that includes an NMState configuration file. 

Important

Customizations to the cluster made by additional manifests are not validated and not guaranteed to work. These manifests might result in a nonfunctional cluster. 

For more information about an additional manifest file, see "Creating a directory to contain additional manifests". 

Note

You can use Butane to create machine configs. For more information, see "Creating a MachineConfig object by using Butane". 

Consider using the customized `br-ex` bridge configuration for any of the following tasks: 

  * You need to modify the `br-ex` bridge after you installed the cluster. 
  * You need to modify the maximum transmission unit (MTU) for your cluster. 
  * You need to update DNS values. 
  * You need to modify attributes for a different bond interface. Examples include MIImon (Media Independent Interface Monitor), bonding mode or Quality of Service (QoS). 
  * You need to enable Link Layer Discovery Protocol (LLDP) to discover and troubleshoot switch connectivity. 



Note

Use the default OVS `br-ex` bridge for standard environments. 

Use the default OVS `br-ex` bridge mechanism for single network interface controller (NIC) environments with default network settings. 

After you install Red Hat Enterprise Linux CoreOS (RHCOS) and the system reboots, the Machine Config Operator injects Ignition configuration files into each node. This operation ensures that each node receives the `br-ex` bridge network configuration. To prevent configuration conflicts, the default OVS `br-ex` bridge mechanism is disabled. 

Warning

The following list of interface names are reserved and you cannot use the names with NMstate configurations: 

  * `br-ext`
  * `br-int`
  * `br-local`
  * `br-nexthop`
  * `br0`
  * `ext-vxlan`
  * `ext`
  * `genev_sys_*`
  * `int`
  * `k8s-*`
  * `ovn-k8s-*`
  * `patch-br-*`
  * `tun0`
  * `vxlan_sys_*`



**Prerequisites**

  * Optional: You have installed the [`nmstatectl`](https://nmstate.io/user/quick_guide.html) CLI tool to validate your NMState configuration. 
  * You checked that an `openshift` subdirectory exists in your installation directory. If the subdirectory does not exist, create the subdirectory. 



**Procedure**

  1. Create an NMState configuration file and define a customized `br-ex` bridge network configuration in the file: 

**Example of an NMState configuration for a customized`br-ex` bridge network**

```yaml
interfaces:
- name: enp2s0
  type: ethernet
  state: up
  mtu: 9000
  ipv4:
    enabled: false
  ipv6:
    enabled: false
- name: br-ex
  type: ovs-bridge
  state: up
  ipv4:
    enabled: false
    dhcp: false
  ipv6:
    enabled: false
    dhcp: false
  bridge:
    options:
      mcast-snooping-enable: true
    port:
    - name: enp2s0
    - name: br-ex
- name: br-ex
  type: ovs-interface
  state: up
  copy-mac-from: enp2s0
  mtu: 9000
  ipv4:
    enabled: true
    dhcp: true
    auto-route-metric: 48
  ipv6:
    enabled: true
    dhcp: true
    auto-route-metric: 48
# ...
```


where: 

`interfaces.name`
     Specifies the name of the interface. 
`interfaces.type`
     Specifies the type of ethernet. 
`interfaces.state`
     Specifies the requested state for the interface after creation. 
`mtu`
     To ensure network stability and performance, you must explicitly declare the MTU in the manifest for every interface. Do not rely on automatic MTU configuration. The MTU configured on a bridge port or VLAN-tagged interface must not exceed the maximum frame size supported by the attached physical medium. A mismatch causes packet fragmentation or connectivity loss. 
`ipv4.enabled`
     Disables IPv4 and IPv6 in this example. 
`port.name`
     Specifies the node NIC to which the bridge attaches. 
`auto-route-metric`
     Sets the parameter to `48` to ensure the `br-ex` default route always has the highest precedence (lowest metric). This configuration prevents routing conflicts with any other interfaces that are automatically configured by the `NetworkManager` service. 

  2. Use the `cat` command to base64-encode the contents of the NMState configuration: 

```shell-session
$ cat <nmstate_configuration>.yml | base64
```


where: 

`<nmstate_configuration>`
     Replace `<nmstate_configuration>` with the name of your NMState resource YAML file. 

  3. Create a `MachineConfig` file as an additional manifest file. Define a customized `br-ex` bridge network configuration analogous to the following example in the file. The Agent-based Installer automatically applies the updates from the `MachineConfig` object to your cluster. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 10-br-ex-worker
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/worker-0.yml
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/worker-1.yml
# ...
```


where: 

`metadata.name`
     Specifies the name of the policy. 
`contents.source`
     Writes the encoded base64 information to the specified path. 
`path`
    

For each node in your cluster, specify the hostname path to your node and the base-64 encoded Ignition configuration file data for the machine type. The `worker` role is the default role for nodes in your cluster. You must use the `.yml` extension for configuration files. For example, use `$(hostname -s).yml` when specifying the short hostname path for each node or all nodes in the `MachineConfig` manifest file. 

You can apply a single global configuration to all nodes in your cluster by using the `/etc/nmstate/openshift/cluster.yml` configuration file. In this case, you do not need to specify the short hostname path for each node, such as `/etc/nmstate/openshift/<node_hostname>.yml`. For example: 

**Example /etc/nmstate/openshift/cluster.yml configuration file**

```yaml
# ...
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/cluster.yml
# ...
```


  4. Save the additional manifest file in the `openshift` subdirectory of your installation directory. 

On completing other configuration inputs for your installation, such as encrypting the disk, you create the ISO image. After booting this image, the customized `br-ex` bridge configuration applies to each node in your cluster. 




**Additional resources**

  * [Creating a MachineConfig object by using Butane](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#installation-special-config-butane-create_installing-customizing)



## 4.5.3. Creating disk partitions

In general, you must use the default disk partitioning that is created during the RHCOS installation. However, there are cases where you might want to create a separate partition for a directory that you expect to grow. 

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` directory or a subdirectory of `/var`. For example: 

  * `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system. 
  * `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage. 
  * `/var`: Holds data that you might want to keep separate for purposes such as auditing. 

Important

For disk sizes larger than 100GB, and especially larger than 1TB, create a separate `/var` partition. 




Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date to keep that data intact. This method eliminates the need to re-pull containers or copy large log files during system updates. 

The use of a separate partition for the `/var` directory or a subdirectory of `/var` also prevents data growth in the partitioned directory from filling up the root file system. 

The following procedure sets up a separate `/var` partition by adding a machine config manifest that is wrapped into the Ignition config file for a node type during the preparation phase of an installation. 

**Prerequisites**

  * You have created an `openshift` subdirectory within your installation directory. 



**Procedure**

  1. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 98-var-partition
storage:
  disks:
  - device: /dev/disk/by-id/<device_name>
    partitions:
    - label: var
      start_mib: <partition_start_offset>
      size_mib: <partition_size>
      number: 5
  filesystems:
    - device: /dev/disk/by-partlabel/var
      path: /var
      format: xfs
      mount_options: [defaults, prjquota]
      with_mount_unit: true
```


where: 

`<device_name>`
     Specifies the storage device name of the disk that you want to partition. 
`<partition_start_offset>`
     Specifies the minimum offset value for the boot disk. For best performance, specify a minimum offset value of 25000 mebibytes. The root file system is automatically resized to fill all available space up to the specified offset. If no offset value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition. 
`<partition_size>`
     Specifies the size of the data partition in mebibytes. 
`mount_options`
    

The `prjquota` mount option must be enabled for filesystems used for container storage. 

Note

When creating a separate `/var` partition, you cannot use different instance types for compute nodes, if the different instance types do not have the same device name. 

  2. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command: 

```shell-session
$ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
```


## 4.5.4. Use ZTP manifests

As an optional task, you can use GitOps Zero Touch Provisioning (ZTP) manifests to configure your installation beyond the options available through the `install-config.yaml` and `agent-config.yaml` files. 

See "Challenges of the network far edge" to learn more about GitOps Zero Touch Provisioning (ZTP). 

Important

Zero Touch Provisioning (ZTP) is not supported for two-node clusters with fencing (TNF). Although you can use Red Hat Advanced Cluster Management (RHACM) for installations, the additional infrastructure components required for ZTP are not validated for this topology. 

Note

GitOps ZTP manifests can be generated with or without configuring the `install-config.yaml` and `agent-config.yaml` files beforehand. If you chose to configure the `install-config.yaml` and `agent-config.yaml` files, the configurations will be imported to the ZTP cluster manifests when they are generated. 

**Prerequisites**

  * You have placed the `openshift-install` binary in a directory that is on your `PATH`. 
  * Optional: You have created and configured the `install-config.yaml` and `agent-config.yaml` files. 



**Procedure**

  1. Generate ZTP cluster manifests by running the following command: 

```shell-session
$ openshift-install agent create cluster-manifests --dir <installation_directory>
```


Important

If you have created the `install-config.yaml` and `agent-config.yaml` files, those files are deleted and replaced by the cluster manifests generated through this command. 

Any configurations made to the `install-config.yaml` and `agent-config.yaml` files are imported to the ZTP cluster manifests when you run the `openshift-install agent create cluster-manifests` command. 

  2. Navigate to the `cluster-manifests` directory by running the following command: 

```shell-session
$ cd <installation_directory>/cluster-manifests
```


  3. Configure the manifest files in the `cluster-manifests` directory. For sample files, see the "Sample GitOps ZTP custom resources" section. 
  4. Disconnected clusters: If you did not define mirror configuration in the `install-config.yaml` file before generating the ZTP manifests, perform the following steps: 

     1. Navigate to the `mirror` directory by running the following command: 

```shell-session
$ cd ../mirror
```


     2. Configure the manifest files in the `mirror` directory. 




**Additional resources**

  * [Sample GitOps ZTP custom resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/installing-with-agent-based-installer#sample-ztp-custom-resources_installing-with-agent-based-installer "4.10. Sample GitOps ZTP custom resources")
  * [Challenges of the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-deploying-far-edge-clusters-at-scale)



## 4.5.5. Encrypting the disk

As an optional task, you can encrypt your disk or partition while installing OpenShift Container Platform with the Agent-based Installer. 

Important

If there are leftover TPM encryption keys from a previous operating system on the bare-metal host, the cluster deployment can get stuck. To avoid this situation, it is highly recommended to reset the TPM chip in the BIOS before booting the ISO. 

**Prerequisites**

  * You have created and configured the `install-config.yaml` and `agent-config.yaml` files, unless you are using ZTP manifests. 
  * You have placed the `openshift-install` binary in a directory that is on your `PATH`. 



**Procedure**

  1. Generate ZTP cluster manifests by running the following command: 

```shell-session
$ openshift-install agent create cluster-manifests --dir <installation_directory>
```


Important

If you have created the `install-config.yaml` and `agent-config.yaml` files, those files are deleted and replaced by the cluster manifests generated through this command. 

Any configurations made to the `install-config.yaml` and `agent-config.yaml` files are imported to the ZTP cluster manifests when you run the `openshift-install agent create cluster-manifests` command. 

Note

If you have already generated ZTP manifests, skip this step. 

  2. Navigate to the `cluster-manifests` directory by running the following command: 

```shell-session
$ cd <installation_directory>/cluster-manifests
```


  3. Add the following section to the `agent-cluster-install.yaml` file: 

```yaml
diskEncryption:
    enableOn: all
    mode: tang
    tangServers: "server1": "http://tang-server-1.example.com:7500"
```


where: 

`diskEncryption.enableOn`
     Specifies which nodes to enable disk encryption on. Valid values are `none`, `all`, `masters`, and `workers`. 
`diskEncryption.mode`
     Specifies which disk encryption mode to use. Valid values are `tpmv2` and `tang`. 
`diskEncryption.tangServers`
     Specifies the Tang servers if you are using Tang. This value is optional. 




**Additional resources**

  * [About disk encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#installation-special-config-storage_installing-customizing)



## 4.5.6. Configuring cluster network MTU at installation time

You can explicitly set the cluster network maximum transmission unit (MTU) during installation by placing a `Network` custom resource (CR) as an additional manifest in the `openshift` directory of your Agent-based Installer configuration. 

Setting the cluster network MTU with additional headroom during deployment prevents the need for a Day 2 MTU update that requires at least two rolling reboots of all cluster nodes. 

During installation, the Cluster Network Operator (CNO) automatically calculates the cluster network MTU based on the primary network interface MTU. When you enable IPsec at installation time, the calculation includes both the OVN-Kubernetes overhead of 100 bytes and the IPsec overhead. If you plan to enable IPsec or another encapsulation technology as a Day 2 operation, the calculated MTU includes only the OVN-Kubernetes overhead and might be insufficient. 

By explicitly setting the cluster network MTU at installation time, you can include additional headroom for those future needs and avoid a disruptive MTU migration. 

Important

The cluster network MTU value must be lower than the machine network MTU by at least 100 bytes to account for OVN-Kubernetes overlay overhead. If you plan to enable IPsec as a Day 2 operation, allow an additional 46 bytes for IPsec headroom. For example, with a machine network MTU of `9100` bytes, set the cluster network MTU to `8900` bytes, which accounts for the following offset: 

  * OVN-Kubernetes overhead: 100 bytes 
  * IPsec headroom: 46 bytes 
  * Extra headroom: 54 bytes 
  * Total offset: 200 bytes 



To avoid selecting an MTU value that a node cannot support, verify the maximum MTU (`maxmtu`) that the network interface accepts by running the `ip -d link` command. 

**Prerequisites**

  * You have created the `install-config.yaml` and `agent-config.yaml` files for your installation. 
  * You have created the `openshift` subdirectory within your installation directory as described in "Creating a directory to contain additional manifests". 



**Procedure**

  1. In your `agent-config.yaml` file, set the machine network MTU on the network interface for each host by using NMState configuration. 

The following example configures an Ethernet interface with MTU `9100`: 

```yaml
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
    networkConfig:
      interfaces:
        - name: eno1
          type: ethernet
          state: up
          mtu: 9100
          ipv4:
            enabled: true
            dhcp: false
            address:
              - ip: "192.168.111.80"
                prefix-length: 24
```


  2. Create a `Network` CR manifest file named `set-cluster-mtu.yaml` that sets the cluster network MTU: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      mtu: 8900
```


where: 

`mtu`
     Specifies the cluster network MTU value. This value must be at least 100 bytes less than the machine network MTU. In this example, the value is 200 bytes less than the machine network MTU of 9100 to allow headroom for IPsec and other future requirements. 

  3. Place the `set-cluster-mtu.yaml` manifest file in the `openshift` subdirectory of your installation directory: 

```plaintext
<installation_directory>/
├── install-config.yaml
├── agent-config.yaml
└── openshift/
    └── set-cluster-mtu.yaml
```


Note

Manifests in the `openshift` directory cannot override default cluster manifests. This restriction does not affect the `Network` CR for cluster network MTU because MTU configuration is not part of the default manifest set. 

  4. Create the agent image and boot your servers as described in "Creating and booting the agent image". 

During cluster installation, the installation program applies the `Network` CR as an additional manifest, and the CNO uses the specified MTU value instead of auto-calculating it. 




**Verification**

  * After the cluster installation is complete, verify the cluster network MTU by running the following command: 

```shell-session
$ oc get networks.operator.openshift.io cluster -o yaml
```


**Example output**

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
# ...
spec:
  # ...
  defaultNetwork:
    ovnKubernetesConfig:
      # ...
      mtu: 8900
```
