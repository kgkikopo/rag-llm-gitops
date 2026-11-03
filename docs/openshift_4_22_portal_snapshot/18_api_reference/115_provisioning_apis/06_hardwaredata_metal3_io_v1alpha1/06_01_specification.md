# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  HardwareDataSpec defines the desired state of HardwareData.   
Show more

## 6.1.1. .spec

Description
     HardwareDataSpec defines the desired state of HardwareData. 
Type
     `object`

Property| Type| Description  
---|---|---  
`hardware` |  `object` |  The hardware discovered on the host during its inspection.   
Show more

## 6.1.2. .spec.hardware

Description
     The hardware discovered on the host during its inspection. 
Type
     `object`

Property| Type| Description  
---|---|---  
`cpu` |  `object` |  Details of the CPU(s) in the system.   
`firmware` |  `object` |  System firmware information.   
`hostname` |  `string` |  Name of the host at the inspection time.   
`nics` |  `array` |  List of network interfaces for the host.   
`nics[]` |  `object` |  NIC describes one network interface on the host.   
`ramMebibytes` |  `integer` |  The host’s amount of memory in Mebibytes.   
`storage` |  `array` |  List of storage (disk, SSD, etc.) available to the host.   
`storage[]` |  `object` |  Storage describes one storage device (disk, SSD, etc.) on the host.   
`systemVendor` |  `object` |  System vendor information.   
Show more

## 6.1.3. .spec.hardware.cpu

Description
     Details of the CPU(s) in the system. 
Type
     `object`

Property| Type| Description  
---|---|---  
`arch` |  `string` |   
`clockMegahertz` |  `number` |  ClockSpeed is a clock speed in MHz   
`count` |  `integer` |   
`flags` |  `array (string)` |   
`model` |  `string` |   
Show more

## 6.1.4. .spec.hardware.firmware

Description
     System firmware information. 
Type
     `object`

Property| Type| Description  
---|---|---  
`bios` |  `object` |  The BIOS for this firmware   
Show more

## 6.1.5. .spec.hardware.firmware.bios

Description
     The BIOS for this firmware 
Type
     `object`

Property| Type| Description  
---|---|---  
`date` |  `string` |  The release/build date for this BIOS   
`vendor` |  `string` |  The vendor name for this BIOS   
`version` |  `string` |  The version of the BIOS   
Show more

## 6.1.6. .spec.hardware.nics

Description
     List of network interfaces for the host. 
Type
     `array`

## 6.1.7. .spec.hardware.nics[]

Description
     NIC describes one network interface on the host. 
Type
     `object`

Property| Type| Description  
---|---|---  
`ip` |  `string` |  The IP address of the interface. This will be an IPv4 or IPv6 address if one is present. If both IPv4 and IPv6 addresses are present in a dual-stack environment, two nics will be output, one with each IP.   
`lldp` |  `object` |  LLDP data for this interface   
`mac` |  `string` |  The device MAC address   
`model` |  `string` |  The vendor and product IDs of the NIC, e.g. "0x8086 0x1572"   
`name` |  `string` |  The name of the network interface, e.g. "en0"   
`pciAddress` |  `string` |  The NIC PCI address   
`pxe` |  `boolean` |  Whether the NIC is PXE Bootable   
`speedGbps` |  `integer` |  The speed of the device in Gigabits per second   
`vlanId` |  `integer` |  The untagged VLAN ID   
`vlans` |  `array` |  The VLANs available   
`vlans[]` |  `object` |  VLAN represents the name and ID of a VLAN.   
Show more

## 6.1.8. .spec.hardware.nics[].lldp

Description
     LLDP data for this interface 
Type
     `object`

Property| Type| Description  
---|---|---  
`portID` |  `string` |  The switch port ID from LLDP   
`switchID` |  `string` |  The switch chassis ID from LLDP   
`switchSystemName` |  `string` |  The switch system name from LLDP   
Show more

## 6.1.9. .spec.hardware.nics[].vlans

Description
     The VLANs available 
Type
     `array`

## 6.1.10. .spec.hardware.nics[].vlans[]

Description
     VLAN represents the name and ID of a VLAN. 
Type
     `object`

Property| Type| Description  
---|---|---  
`id` |  `integer` |  VLANID is a 12-bit 802.1Q VLAN identifier   
`name` |  `string` |   
Show more

## 6.1.11. .spec.hardware.storage

Description
     List of storage (disk, SSD, etc.) available to the host. 
Type
     `array`

## 6.1.12. .spec.hardware.storage[]

Description
     Storage describes one storage device (disk, SSD, etc.) on the host. 
Type
     `object`

Property| Type| Description  
---|---|---  
`alternateNames` |  `array (string)` |  A list of alternate Linux device names of the disk, e.g. "/dev/sda". Note that this list is not exhaustive, and names may not be stable across reboots.   
`hctl` |  `string` |  The SCSI location of the device   
`model` |  `string` |  Hardware model   
`name` |  `string` |  A Linux device name of the disk, e.g. "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0". This will be a name that is stable across reboots if one is available.   
`rotational` |  `boolean` |  Whether this disk represents rotational storage. This field is not recommended for usage, please prefer using 'Type' field instead, this field will be deprecated eventually.   
`serialNumber` |  `string` |  The serial number of the device   
`sizeBytes` |  `integer` |  The size of the disk in Bytes   
`type` |  `string` |  Device type, one of: HDD, SSD, NVME.   
`vendor` |  `string` |  The name of the vendor of the device   
`wwn` |  `string` |  The WWN of the device   
`wwnVendorExtension` |  `string` |  The WWN Vendor extension of the device   
`wwnWithExtension` |  `string` |  The WWN with the extension   
Show more

## 6.1.13. .spec.hardware.systemVendor

Description
     System vendor information. 
Type
     `object`

Property| Type| Description  
---|---|---  
`manufacturer` |  `string` |   
`productName` |  `string` |   
`serialNumber` |  `string` |   
Show more
