# 1.4. Host configuration

You can make additional configurations for each host on the cluster in the `agent-config.yaml` file, such as network configurations and root device hints. 

Important

For each host you configure, you must specify which host you are configuring by providing the MAC address of an interface on the host. 

## 1.4.1. Host roles

Each host in the cluster is assigned a role of either `master` or `worker`. You can define the role for each host in the `agent-config.yaml` file by using the `role` parameter. If you do not assign a role to the hosts, the roles will be assigned at random during installation. 

It is recommended to explicitly define roles for your hosts. 

The `rendezvousIP` must be assigned to a host with the `master` role. This can be done manually or by allowing the Agent-based Installer to assign the role. 

Important

You do not need to explicitly define the `master` role for the rendezvous host, however you cannot create configurations that conflict with this assignment. 

For example, if you have 4 hosts with 3 of the hosts explicitly defined to have the `master` role, the last host that is automatically assigned the `worker` role during installation cannot be configured as the rendezvous host. 

**Sample agent-config.yaml file**

```yaml
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: example-cluster
rendezvousIP: 192.168.111.80
hosts:
  - hostname: master-1
    role: master
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a5
  - hostname: master-2
    role: master
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a6
  - hostname: master-3
    role: master
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a7
  - hostname: worker-1
    role: worker
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a8
```


## 1.4.2. About root device hints

The `rootDeviceHints` parameter enables the installation program to provision the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. 

The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. The installation program uses the first discovered device that matches the hint value. The configuration can combine multiple hints, but a device must match all hints for the installation program to select it. 

Table 1.3. SubfieldsSubfield| Description  
---|---  
`deviceName` |  A string containing a Linux device name such as `/dev/vda` or `/dev/disk/by-path/`.  Note It is recommended to use the `/dev/disk/by-path/<device_path>` link to the storage location.  The hint must match the actual value exactly.   
`hctl` |  A string containing a SCSI bus address like `0:0:0:0`. The hint must match the actual value exactly.   
`model` |  A string containing a vendor-specific device identifier. The hint can be a substring of the actual value.   
`vendor` |  A string containing the name of the vendor or manufacturer of the device. The hint can be a sub-string of the actual value.   
`serialNumber` |  A string containing the device serial number. The hint must match the actual value exactly.   
`minSizeGigabytes` |  An integer representing the minimum size of the device in gigabytes.   
`wwn` |  A string containing the unique storage identifier. The hint must match the actual value exactly. If you use the `udevadm` command to retrieve the `wwn` value, and the command outputs a value for `ID_WWN_WITH_EXTENSION`, then you must use this value to specify the `wwn` subfield.   
`rotational` |  A boolean indicating whether the device should be a rotating disk (true) or not (false).   
Show more

**Example usage**

```yaml
     - name: master-0
       role: master
       rootDeviceHints:
         deviceName: "/dev/sda"
```
