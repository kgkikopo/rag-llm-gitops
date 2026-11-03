# 17.13. Reducing NIC queues using the Node Tuning Operator

The Node Tuning Operator facilitates reducing NIC queues for enhanced performance. Adjustments are made using the performance profile, allowing customization of queues for different network devices. 

## 17.13.1. Adjust the NIC queues with the performance profile

You can use a performance profile to adjust the queue count for each network device. By using the Node Tuning Operator, you can reduce NIC queues for enhanced performance. 

Supported network devices: 

  * Non-virtual network devices 
  * Network devices that support multiple queues (channels) 



Unsupported network devices: 

  * Pure software network interfaces 
  * Block devices 
  * Intel DPDK virtual functions 



**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * Install the OpenShift CLI (`oc`). 



**Procedure**

  1. Log in to the OpenShift Container Platform cluster running the Node Tuning Operator as a user with `cluster-admin` privileges. 
  2. Create and apply a performance profile appropriate for your hardware and topology. For guidance on creating a profile, see the "Creating a performance profile" section. 
  3. Edit this created performance profile: 

```shell-session
$ oc edit -f <your_profile_name>.yaml
```


  4. Populate the `spec` field with the `net` object. The object list can contain two fields: 

     * `userLevelNetworking` is a required field specified as a boolean flag. If `userLevelNetworking` is `true`, the queue count is set to the reserved CPU count for all supported devices. The default is `false`. 
     * `devices` is an optional field specifying a list of devices that will have the queues set to the reserved CPU count. If the device list is empty, the configuration applies to all network devices. The configuration is as follows: 

       * `interfaceName`: This field specifies the interface name, and it supports shell-style wildcards, which can be positive or negative. 

         * Example wildcard syntax is as follows: `<string> .*`
         * Negative rules are prefixed with an exclamation mark. To apply the net queue changes to all devices other than the excluded list, use `!<device>`, for example, `!eno1`. 

       * `vendorID`: The network device vendor ID represented as a 16-bit hexadecimal number with a `0x` prefix. 
       * `deviceID`: The network device ID (model) represented as a 16-bit hexadecimal number with a `0x` prefix. 

Note

When a `deviceID` is specified, the `vendorID` must also be defined. A device that matches all of the device identifiers specified in a device entry `interfaceName`, `vendorID`, or a pair of `vendorID` plus `deviceID` qualifies as a network device. This network device then has its net queues count set to the reserved CPU count. 

When two or more devices are specified, the net queues count is set to any net device that matches one of them. 

  5. Set the queue count to the reserved CPU count for all devices by using this example performance profile: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: manual
spec:
  cpu:
    isolated: 3-51,55-103
    reserved: 0-2,52-54
  net:
    userLevelNetworking: true
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
# ...
```


  6. Set the queue count to the reserved CPU count for all devices matching any of the defined device identifiers by using this example performance profile: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: manual
spec:
  cpu:
    isolated: 3-51,55-103
    reserved: 0-2,52-54
  net:
    userLevelNetworking: true
    devices:
    - interfaceName: "eth0"
    - interfaceName: "eth1"
    - vendorID: "0x1af4"
      deviceID: "0x1000"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
# ...
```


  7. Set the queue count to the reserved CPU count for all devices starting with the interface name `eth` by using this example performance profile: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: manual
spec:
  cpu:
    isolated: 3-51,55-103
    reserved: 0-2,52-54
  net:
    userLevelNetworking: true
    devices:
    - interfaceName: "eth*"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
# ...
```


  8. Set the queue count to the reserved CPU count for all devices with an interface named anything other than `eno1` by using this example performance profile: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: manual
spec:
  cpu:
    isolated: 3-51,55-103
    reserved: 0-2,52-54
  net:
    userLevelNetworking: true
    devices:
    - interfaceName: "!eno1"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
# ...
```


  9. Set the queue count to the reserved CPU count for all devices that have an interface name `eth0`, `vendorID` of `0x1af4`, and `deviceID` of `0x1000` by using this example performance profile: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: manual
spec:
  cpu:
    isolated: 3-51,55-103
    reserved: 0-2,52-54
  net:
    userLevelNetworking: true
    devices:
    - interfaceName: "eth0"
    - vendorID: "0x1af4"
      deviceID: "0x1000"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
# ...
```


  10. Apply the updated performance profile: 

```shell-session
$ oc apply -f <your_profile_name>.yaml
```


## 17.13.2. Verifying the queue status

To ensure that your performance profile changes are active, verify the queue status. 

By reviewing the provided examples, you can confirm that specific tuning configurations are successfully applied to your environment. 

In this section, several examples illustrate different performance profiles and how to verify the changes are applied. 

Example 1
    

Example 1 demonstrates that the net queue count that is set to the reserved CPU count (2) for _all_ supported devices. 

The relevant section from the performance profile is: 

```yaml
apiVersion: performance.openshift.io/v2
metadata:
  name: performance
spec:
  kind: PerformanceProfile
  spec:
    cpu:
      reserved: 0-1  #total = 2
      isolated: 2-8
    net:
      userLevelNetworking: true
# ...
```


The following command displays the status of the queues associated with a device: 

Note

Run this command on the node where the performance profile was applied. 

```shell-session
$ ethtool -l <device>
```


The following command verifies the queue status before the profile is applied: 

```shell-session
$ ethtool -l ens4
```


**Example output**

```shell-session
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   4
```


The following command verifies the queue status after the profile is applied: 

```shell-session
$ ethtool -l ens4
```


**Example output**

```shell-session
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   2
```


  * `Combined`: Specifies the combined channel that shows the total count of reserved CPUs for _all_ supported devices is 2. This matches what is configured in the performance profile. 



Example 2
    

Example 2 demonstrates that the net queue count is set to the reserved CPU count (2) for _all_ supported network devices with a specific `vendorID`. 

The relevant section from the performance profile is: 

```yaml
apiVersion: performance.openshift.io/v2
metadata:
  name: performance
spec:
  kind: PerformanceProfile
  spec:
    cpu:
      reserved: 0-1
      isolated: 2-8
    net:
      userLevelNetworking: true
      devices:
      - vendorID = 0x1af4
# ...
```


The following command displays the status of the queues associated with a device: 

Note

Run this command on the node where the performance profile was applied. 

```shell-session
$ ethtool -l <device>
```


The following command verifies the queue status after the profile is applied: 

```shell-session
$ ethtool -l ens4
```


**Example output**

```shell-session
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   2
```


  * `Combined`: Specifies that the total count of reserved CPUs for all supported devices with `vendorID=0x1af4` is 2. For example, if there is another network device `ens2` with `vendorID=0x1af4` it will also have total net queues of 2. This matches what is configured in the performance profile. 



Example 3
    

Example 3 shows that the net queue count is set to the reserved CPU count (2) for _all_ supported network devices that match any of the defined device identifiers. The command `udevadm info` provides a detailed report on a device. In this example the devices are: 

```shell-session
# udevadm info -p /sys/class/net/ens4
...
E: ID_MODEL_ID=0x1000
E: ID_VENDOR_ID=0x1af4
E: INTERFACE=ens4
...
```


```shell-session
# udevadm info -p /sys/class/net/eth0
...
E: ID_MODEL_ID=0x1002
E: ID_VENDOR_ID=0x1001
E: INTERFACE=eth0
...
```


Set the net queues to 2 for a device with `interfaceName` equal to `eth0` and any devices that have a `vendorID=0x1af4` with the following performance profile: 

```shell-session
apiVersion: performance.openshift.io/v2
metadata:
  name: performance
spec:
  kind: PerformanceProfile
    spec:
      cpu:
        reserved: 0-1  #total = 2
        isolated: 2-8
      net:
        userLevelNetworking: true
        devices:
        - interfaceName = eth0
        - vendorID = 0x1af4
# ...
```


The following command verifies the queue status after the profile is applied: 

```shell-session
$ ethtool -l ens4
```


**Example output**

```shell-session
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   2
```


  * `Combined`: Specifies that the total count of reserved CPUs for all supported devices with `vendorID=0x1af4` is set to 2. 

For example, if there is another network device `ens2` with `vendorID=0x1af4`, it will also have the total net queues set to 2. Similarly, a device with `interfaceName` equal to `eth0` will have total net queues set to 2. 




## 17.13.3. Logging associated with adjusting NIC queues

To verify NIC queue adjustments, review the Tuned daemon logs. These log messages detail the assigned devices that are recorded in the respective Tuned daemon logs. 

The following messages might be recorded to the `/var/log/tuned/tuned.log` file: 

  * An `INFO` message is recorded detailing the successfully assigned devices: 

```shell-session
INFO tuned.plugins.base: instance net_test (net): assigning devices ens1, ens2, ens3
```


  * A `WARNING` message is recorded if none of the devices can be assigned: 

```shell-session
WARNING  tuned.plugins.base: instance net_test: no matching devices available
```
