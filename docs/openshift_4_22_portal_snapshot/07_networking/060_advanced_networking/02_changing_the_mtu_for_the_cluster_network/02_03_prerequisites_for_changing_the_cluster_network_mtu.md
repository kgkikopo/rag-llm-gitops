# 2.3. Prerequisites for changing the cluster network MTU

Before you change the cluster network maximum transmission unit (MTU), verify that you have the required access, tools, and network infrastructure to support the new MTU value. 

Ensure that the following conditions are met before you begin: 

  * You have installed the OpenShift CLI (`oc`). 
  * You have access to the cluster using an account with `cluster-admin` permissions. 
  * You have identified the target MTU for your cluster. The MTU for the OVN-Kubernetes network plugin must be set to `100` less than the lowest hardware MTU value in your cluster. 
  * If your nodes are physical machines, ensure that the cluster network and the connected network switches support jumbo frames. 
  * If your nodes are virtual machines (VMs), ensure that the hypervisor and the connected network switches support jumbo frames. 



## 2.3.1. Check the current cluster MTU value

To ensure network stability and performance in a hybrid environment where part of your cluster is in the cloud and part is an on-premise environment, you can obtain the current maximum transmission unit (MTU) for the cluster network. 

**Procedure**

  * To obtain the current MTU for the cluster network, enter the following command: 

```shell-session
$ oc describe network.config cluster
```


**Example output**

```plaintext
...
Status:
  Cluster Network:
    Cidr:               10.217.0.0/22
    Host Prefix:        23
  Cluster Network MTU:  1400
  Network Type:         OVNKubernetes
  Service Network:
    10.217.4.0/23
...
```


## 2.3.2. Prepare your hardware MTU configuration

You must prepare the MTU configuration for your underlying hardware by using a method such as DHCP, PXE, or NetworkManager before you apply the changes to the cluster network. 

**Procedure**

  * Prepare your configuration for the hardware MTU: 

    * If your hardware MTU is specified with DHCP, update your DHCP configuration such as with the following dnsmasq configuration: 

```plaintext
dhcp-option-force=26,<mtu>
```


where: 

`<mtu>`
     Specifies the hardware MTU for the DHCP server to advertise. 

    * If your hardware MTU is specified with a kernel command line with PXE, update that configuration accordingly. 
    * If your hardware MTU is specified in a NetworkManager connection configuration, complete the following steps. This approach is the default for OpenShift Container Platform if you do not explicitly specify your network configuration with DHCP, a kernel command line, or some other method. Your cluster nodes must all use the same underlying network configuration for the following procedure to work unmodified. 

Find the primary network interface by entering the following command: 

```shell-session
$ oc debug node/<node_name> -- chroot /host nmcli -g connection.interface-name c show ovs-if-phys0
```


where: 

`<node_name>`
     Specifies the name of a node in your cluster. 

Create the following `NetworkManager` configuration in the `<interface>-mtu.conf` file: 

```plaintext
[connection-<interface>-mtu]
match-device=interface-name:<interface>
ethernet.mtu=<mtu>
```


where: 

`<interface>`
    

Specifies the primary network interface name or the bond if using bonding. 

Important

Observe the following constraints when specifying the interface: 

      * Do not specify subordinate interfaces of a bond, such as `eth0` or `eth1`. Subordinate interfaces automatically inherit the MTU value set on the parent bond. 
      * The MTU of the VLAN interface cannot exceed the MTU of its parent physical or bonded interface. A parent interface with a larger MTU, such as `9000` for jumbo frames, can host VLANs with smaller MTUs, such as `1500`. However, raising the MTU of a VLAN interface beyond the MTU parent interface current limit requires updating the parent interface first. 

`<mtu>`
     Specifies the new hardware MTU value. 

If you used Kubernetes NMState to configure the `br-ex` bridge, use the Kubernetes NMState Operator to update the MTU for the `br-ex` bridge. Changing the MTU for this bridge in a `.nmconnection` file could lead to persistence issues as the Machine Config Operator (MCO) might overwrite the file. 




## 2.3.3. Create MachineConfig objects

To prepare your nodes for a hardware MTU change, you must create `MachineConfig` objects for both control plane and compute nodes. Creating these objects ensures that the updated network interface settings are ready for deployment without causing immediate cluster instability. 

**Procedure**

  1. Create two `MachineConfig` objects, one for the control plane nodes and another for the worker nodes in your cluster: 

     1. Create the following Butane config in the `control-plane-interface.bu` file: 

Note

The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane. 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 01-control-plane-interface
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  files:
    - path: /etc/NetworkManager/conf.d/99-<interface>-mtu.conf
      contents:
        local: <interface>-mtu.conf
      mode: 0600
```


where: 

`storage.files.path`
     Specifies the `NetworkManager` connection name for the primary network interface. 
`storage.files.local`
     Specifies the local filename for the updated `NetworkManager` configuration file from an earlier step. 

     2. Create the following Butane config in the `worker-interface.bu` file: 

Note

The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane. 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 01-worker-interface
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  files:
    - path: /etc/NetworkManager/conf.d/99-<interface>-mtu.conf
      contents:
        local: <interface>-mtu.conf
      mode: 0600
```


where: 

`storage.files.path`
     Specifies the `NetworkManager` connection name for the primary network interface. 
`storage.files.local`
     Specifies the local filename for the updated `NetworkManager` configuration file from an earlier step. 

  2. Create `MachineConfig` objects from the Butane configs by running the following command: 

```shell-session
$ for manifest in control-plane-interface worker-interface; do
    butane --files-dir . $manifest.bu > $manifest.yaml
  done
```


Warning

Do not apply these machine configs until explicitly instructed later in this procedure. Applying these machine configs now causes a loss of stability for the cluster. 




## 2.3.4. Begin the MTU migration

Start the maximum transmission unit (MTU) migration by specifying the migration configuration for the cluster network and machine interfaces. The Machine Config Operator performs a rolling reboot of the nodes to prepare the cluster for the MTU change. 

**Procedure**

  1. To begin the MTU migration, specify the migration configuration by entering the following command. The Machine Config Operator performs a rolling reboot of the nodes in the cluster in preparation for the MTU change. 

```shell-session
$ oc patch Network.operator.openshift.io cluster --type=merge --patch \
  '{"spec": { "migration": { "mtu": { "network": { "from": <overlay_from>, "to": <overlay_to> } , "machine": { "to" : <machine_to> } } } } }'
```


where: 

`<overlay_from>`
     Specifies the current cluster network MTU value. 
`<overlay_to>`
     Specifies the target MTU for the cluster network. This value is set relative to the value of `<machine_to>`. For OVN-Kubernetes, this value must be `100` less than the value of `<machine_to>`. 
`<machine_to>`
     Specifies the MTU for the primary network interface on the underlying host network. 

```shell-session
$ oc patch Network.operator.openshift.io cluster --type=merge --patch \
  '{"spec": { "migration": { "mtu": { "network": { "from": 1400, "to": 9000 } , "machine": { "to" : 9100} } } } }'
```


  2. As the Machine Config Operator updates machines in each machine config pool, the Operator reboots each node one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command: 

```shell-session
$ oc get machineconfigpools
```


A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`. 

Note

By default, the Machine Config Operator updates one machine per pool at a time, causing the total time the migration takes to increase with the size of the cluster. 




## 2.3.5. Verify the machine configuration

Verify the machine configuration on your hosts to confirm that the maximum transmission unit (MTU) migration applied successfully. Checking the configuration state and system settings help ensures that the nodes use the correct migration script. 

**Procedure**

  * Confirm the status of the new machine configuration on the hosts: 

    1. To list the machine configuration state and the name of the applied machine configuration, enter the following command: 

```shell-session
$ oc describe node | egrep "hostname|machineconfig"
```


**Example output**

```plaintext
kubernetes.io/hostname=master-0
machineconfiguration.openshift.io/currentConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
machineconfiguration.openshift.io/desiredConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
machineconfiguration.openshift.io/reason:
machineconfiguration.openshift.io/state: Done
```


    2. Verify that the following statements are true: 

       * The value of `machineconfiguration.openshift.io/state` field is `Done`. 
       * The value of the `machineconfiguration.openshift.io/currentConfig` field is equal to the value of the `machineconfiguration.openshift.io/desiredConfig` field. 

    3. To confirm that the machine config is correct, enter the following command: 

```shell-session
$ oc get machineconfig <config_name> -o yaml | grep ExecStart
```


where: 

`<config_name>`
     Specifies the name of the machine config from the `machineconfiguration.openshift.io/currentConfig` field. 

The machine config must include the following update to the systemd configuration: 

```plaintext
ExecStart=/usr/local/bin/mtu-migration.sh
```


## 2.3.6. Apply the new hardware MTU value

You must apply the new hardware maximum transmission unit (MTU) value to your nodes by updating the underlying network interfaces and verifying that the Machine Config Operator successfully reboots each node. 

**Procedure**

  1. Update the underlying network interface MTU value: 

     * If you are specifying the new MTU with a NetworkManager connection configuration, enter the following command. The MachineConfig Operator automatically performs a rolling reboot of the nodes in your cluster. 

```shell-session
$ for manifest in control-plane-interface worker-interface; do
    oc create -f $manifest.yaml
  done
```


     * If you are specifying the new MTU with a DHCP server option or a kernel command line and PXE, make the necessary changes for your infrastructure. 

  2. As the Machine Config Operator updates machines in each machine config pool, the Operator reboots each node one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command: 

```shell-session
$ oc get machineconfigpools
```


A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`. 

Note

By default, the Machine Config Operator updates one machine per pool at a time, causing the total time the migration takes to increase with the size of the cluster. 

  3. Confirm the status of the new machine configuration on the hosts: 

     1. To list the machine configuration state and the name of the applied machine configuration, enter the following command: 

```shell-session
$ oc describe node | egrep "hostname|machineconfig"
```


**Example output**

```plaintext
kubernetes.io/hostname=master-0
machineconfiguration.openshift.io/currentConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
machineconfiguration.openshift.io/desiredConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
machineconfiguration.openshift.io/reason:
machineconfiguration.openshift.io/state: Done
```


Verify that the following statements are true: 

        * The value of `machineconfiguration.openshift.io/state` field is `Done`. 
        * The value of the `machineconfiguration.openshift.io/currentConfig` field is equal to the value of the `machineconfiguration.openshift.io/desiredConfig` field. 

     2. To confirm that the machine config is correct, enter the following command: 

```shell-session
$ oc get machineconfig <config_name> -o yaml | grep path:
```


where: 

`<config_name>`
     Specifies the name of the machine config from the `machineconfiguration.openshift.io/currentConfig` field. 

If the machine config is successfully deployed, the previous output contains the `/etc/NetworkManager/conf.d/99-<interface>-mtu.conf` file path and the `ExecStart=/usr/local/bin/mtu-migration.sh` line. 




## 2.3.7. Finalize the MTU migration

Finalize the MTU migration to apply the new maximum transmission unit (MTU) settings to the OVN-Kubernetes network plugin. This updates the cluster configuration and triggers a rolling reboot of the nodes to complete the process. 

**Procedure**

  1. To finalize the MTU migration, enter the following command for the OVN-Kubernetes network plugin: 

```shell-session
$ oc patch Network.operator.openshift.io cluster --type=merge --patch \
  '{"spec": { "migration": null, "defaultNetwork":{ "ovnKubernetesConfig": { "mtu": <mtu> }}}}'
```


where: 

`<mtu>`
     Specifies the new cluster network MTU that you specified with `<overlay_to>`. 

  2. After finalizing the MTU migration, each machine config pool node is rebooted one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command: 

```shell-session
$ oc get machineconfigpools
```


A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`. 




**Verification**

  1. To get the current MTU for the cluster network, enter the following command: 

```shell-session
$ oc describe network.config cluster
```


  2. Get the current MTU for the primary network interface of a node: 

     1. To list the nodes in your cluster, enter the following command: 

```shell-session
$ oc get nodes
```


     2. To obtain the current MTU setting for the primary network interface on a node, enter the following command: 

```shell-session
$ oc adm node-logs <node> -u ovs-configuration | grep configure-ovs.sh | grep mtu | grep <interface> | head -1
```


where: 

`<node>`
     Specifies a node from the output from the previous step. 
`<interface>`
     Specifies the primary network interface name for the node. 

**Example output**

```plaintext
ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8051
```
