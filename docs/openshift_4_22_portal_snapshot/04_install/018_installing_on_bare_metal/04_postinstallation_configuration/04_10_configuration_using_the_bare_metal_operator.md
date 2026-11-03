# 4.10. Configuration using the Bare Metal Operator

When deploying OpenShift Container Platform on bare-metal hosts, there are times when you need to make changes to the host either before or after provisioning. 

This can include inspecting the host’s hardware, firmware, and firmware details. It can also include formatting disks or changing modifiable firmware settings. 

You can use the Bare Metal Operator (BMO) to provision, manage, and inspect bare-metal hosts in your cluster. The BMO can complete the following operations: 

  * Provision bare-metal hosts to the cluster with a specific image. 
  * Turn a host on or off. 
  * Inspect hardware details of the host and report them to the bare-metal host. 
  * Upgrade or downgrade a host’s firmware to a specific version. 
  * Inspect firmware and configure BIOS settings. 
  * Clean disk contents for the host before or after provisioning the host. 



The BMO uses the following resources to complete these tasks: 

  * `BareMetalHost`
  * `HostFirmwareSettings`
  * `FirmwareSchema`
  * `HostFirmwareComponents`
  * `HostUpdatePolicy`



The BMO maintains an inventory of the physical hosts in the cluster by mapping each bare-metal host to an instance of the `BareMetalHost` custom resource definition. Each `BareMetalHost` resource features hardware, software, and firmware details. The BMO continually inspects the bare-metal hosts in the cluster to ensure each `BareMetalHost` resource accurately details the components of the corresponding host. 

The BMO also uses the `HostFirmwareSettings` resource, the `FirmwareSchema` resource, and the `HostFirmwareComponents` resource to detail firmware specifications and upgrade or downgrade firmware for the bare-metal host. 

The BMO interfaces with bare-metal hosts in the cluster by using the Ironic API service. The Ironic service uses the Baseboard Management Controller (BMC) on the host to interface with the machine. 

The BMO `HostUpdatePolicy` can enable or disable live updates to the firmware settings, BMC settings, or BIOS settings of a bare-metal host after provisioning the host. By default, the BMO disables live updates. 

## 4.10.1. Bare Metal Operator architecture

The Bare Metal Operator uses multiple resources to provision, manage, and inspect bare-metal hosts, including the `BareMetalHost`, `HostFirmwareSettings`, `FirmwareSchema`, `HostFirmwareComponents`, and `HostUpdatePolicy` resources. 

![BMO architecture overview](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_bare_metal-en-US/images/65afda87892888af3a7e6e6829ac50eb/715_OpenShift_Bare_Metal_Operator_updates_0624.png) ![BMO architecture overview](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_bare_metal-en-US/images/65afda87892888af3a7e6e6829ac50eb/715_OpenShift_Bare_Metal_Operator_updates_0624.png)

BareMetalHost
     The `BareMetalHost` resource defines a physical host and its properties. When you provision a bare-metal host to the cluster, you must define a `BareMetalHost` resource for that host. For ongoing management of the host, you can inspect the information in the `BareMetalHost` resource or update this information. 

The `BareMetalHost` resource features provisioning information such as the following: 

  * Deployment specifications such as the operating system boot image or the custom RAM disk 
  * Provisioning state 
  * Baseboard Management Controller (BMC) address 
  * Desired power state 



The `BareMetalHost` resource features hardware information such as the following: 

  * Number of CPUs 
  * MAC address of a NIC 
  * Size of the host’s storage device 
  * Current power state 

HostFirmwareSettings
     You can use the `HostFirmwareSettings` resource to retrieve and manage the firmware settings for a host. When a host moves to the `Available` state, the Ironic service reads the host’s firmware settings and creates the `HostFirmwareSettings` resource. There is a one-to-one mapping between the `BareMetalHost` resource and the `HostFirmwareSettings` resource. 




You can use the `HostFirmwareSettings` resource to inspect the firmware specifications for a host or to update a host’s firmware specifications. 

Note

You must adhere to the schema specific to the vendor firmware when you edit the `spec` field of the `HostFirmwareSettings` resource. This schema is defined in the read-only `FirmwareSchema` resource. 

FirmwareSchema
     Firmware settings vary among hardware vendors and host models. A `FirmwareSchema` resource is a read-only resource that contains the types and limits for each firmware setting on each host model. The data comes directly from the BMC by using the Ironic service. You can use the `FirmwareSchema` resource to identify valid values that you can specify in the `spec` field of the `HostFirmwareSettings` resource. 

A `FirmwareSchema` resource can apply to many `BareMetalHost` resources if the schema is the same. 

HostFirmwareComponents
     Metal3 provides the `HostFirmwareComponents` resource, which describes BIOS and baseboard management controller (BMC) firmware versions. You can upgrade or downgrade the host’s firmware to a specific version by editing the `spec` field of the `HostFirmwareComponents` resource. This is useful when deploying with validated patterns that have been tested against specific firmware versions. 
HostUpdatePolicy
     The `HostUpdatePolicy` resource can enable or disable live updates to the firmware settings, BMC settings, or BIOS settings of bare-metal hosts. By default, the `HostUpdatePolicy` resource for each bare-metal host restricts updates to hosts during provisioning. You must modify the `HostUpdatePolicy` resource for a host when you want to update the firmware settings, BMC settings, or BIOS settings after provisioning the host. 

**Additional resources**

  * [Metal3 API service for provisioning bare-metal hosts](https://metal3.io/)
  * [Ironic API service for managing bare-metal infrastructure](https://ironicbaremetal.org/)



## 4.10.2. About the BareMetalHost resource

You can use the `BareMetalHost` resource to define physical hosts and their properties, including deployment specifications, hardware information, and provisioning state. 

The `BareMetalHost` resource contains two sections: 

  1. The `BareMetalHost` spec 
  2. The `BareMetalHost` status 



Hardware data is available in the `status.hardware` section of the `BareMetalHost` object and in the `HardwareData` object. You can access the `HardwareData` object by running the following command: 

```shell-session
$ oc get hardwaredata <machine_name> -n openshift-machine-api
```


where: 

`<machine_name>`
     Specifies the name of a bare-metal host. 

### 4.10.2.1. The BareMetalHost spec

The `spec` section of the `BareMetalHost` resource defines the desired state of the host. 

Table 4.1. BareMetalHost specParameters| Description  
---|---  
`architecture` |  Specifies the CPU architecture of the underlying machine. Supported values are `aarch64` and `x86_64`. If this value is not specified, it will default to the architecture of the control plane. You can add `aarch64` machines to a cluster with `x86_64` control plane machines, but you cannot add `x86_64` machines to a cluster with `aarch64` control plane machines.   
`automatedCleaningMode` |  An interface to enable or disable automated cleaning during provisioning and de-provisioning. When set to `disabled`, it skips automated cleaning. When set to `metadata`, automated cleaning is enabled. The default setting is `metadata`.   
`bmc: address: credentialsName: disableCertificateVerification:` |  The `bmc` configuration setting contains the connection information for the baseboard management controller (BMC) on the host. The fields are: 

  * `address`: The URL for communicating with the host’s BMC controller. 
  * `credentialsName`: A reference to a secret containing the username and password for the BMC. 
  * `disableCertificateVerification`: A boolean to skip certificate validation when set to `true`. 

  
`bootMACAddress` |  The MAC address of the network interface controller (NIC) used for provisioning the host.   
`bootMode` |  The boot mode of the host. It defaults to `UEFI`, but it can also be set to `legacy` for BIOS boot, or `UEFISecureBoot`.   
`consumerRef` |  A reference to another resource that is using the host. It could be empty if another resource is not currently using the host. For example, a `Machine` resource might use the host when the `machine-api` is using the host.   
`description` |  A human-provided string to help identify the host.   
`externallyProvisioned` |  A boolean indicating whether the host provisioning and deprovisioning are managed externally. When set: 

  * Power status can still be managed using the online field. 
  * Hardware inventory will be monitored, but no provisioning or deprovisioning operations are performed on the host. 

  
`firmware` |  Contains information about the BIOS configuration of bare-metal hosts. Currently, `firmware` is only supported by iRMC, iDRAC, iLO4 and iLO5 BMCs. The sub fields are: 

  * `simultaneousMultithreadingEnabled`: Allows a single physical processor core to appear as several logical processors. Valid settings are `true` or `false`. 
  * `sriovEnabled`: SR-IOV support enables a hypervisor to create virtual instances of a PCI-express device, potentially increasing performance. Valid settings are `true` or `false`. 
  * `virtualizationEnabled`: Supports the virtualization of platform hardware. Valid settings are `true` or `false`. 

  
`image: url: checksum: checksumType: format:` |  The `image` configuration setting holds the details for the image to be deployed on the host. Ironic requires the image fields. However, when the `externallyProvisioned` configuration setting is set to `true` and the external management does not require power control, the fields can be empty. The setting supports the following fields: 

  * `url`: The URL of an image to deploy to the host. 
  * `checksum`: The actual checksum or a URL to a file containing the checksum for the image at `image.url`. 
  * `checksumType`: You can specify checksum algorithms. Currently `image.checksumType` only supports `md5`, `sha256`, and `sha512`. The default checksum type is `md5`. 
  * `format`: This is the disk format of the image. It can be one of `raw`, `qcow2`, `vdi`, `vmdk`, `live-iso` or be left unset. Setting it to `raw` enables raw image streaming in the Ironic agent for that image. Setting it to `live-iso` enables ISO images to live boot without deploying to disk, and it ignores the `checksum` fields. 

  
`networkData` |  A reference to the secret containing the network configuration data and its namespace, so that it can be attached to the host before the host boots to set up the network.   
`online` |  A boolean indicating whether the host should be powered on (`true`) or off (`false`). Changing this value will trigger a change in the power state of the physical host.   
`raid: hardwareRAIDVolumes: softwareRAIDVolumes:` |  (Optional) Contains the information about the RAID configuration for bare-metal hosts. If not specified, it retains the current configuration.  Note OpenShift Container Platform 4.22 supports hardware RAID on the installation drive for BMCs, including: 

  * Fujitsu iRMC with support for RAID levels 0, 1, 5, 6, and 10 
  * Dell iDRAC using the Redfish API with firmware version 6.10.30.20 or later and RAID levels 0, 1, and 5 

OpenShift Container Platform 4.22 does not support software RAID on the installation drive.  See the following configuration settings: 

  * `hardwareRAIDVolumes`: Contains the list of logical drives for hardware RAID, and defines the desired volume configuration in the hardware RAID. If you do not specify `rootDeviceHints`, the first volume is the root volume. The sub-fields are: 
    * `level`: The RAID level for the logical drive. The following levels are supported: `0`,`1`,`2`,`5`,`6`,`1+0`,`5+0`,`6+0`. 
    * `name`: The name of the volume as a string. It should be unique within the server. If not specified, the volume name will be autogenerated. 
    * `numberOfPhysicalDisks`: The number of physical drives as an integer to use for the logical drove. Defaults to the minimum number of disk drives required for the particular RAID level. 
    * `physicalDisks`: The list of names of physical disk drives as a string. This is an optional field. If specified, the controller field must be specified too. 
    * `controller`: (Optional) The name of the RAID controller as a string to use in the hardware RAID volume. 
    * `rotational`: If set to `true`, it will only select rotational disk drives. If set to `false`, it will only select solid-state and NVMe drives. If not set, it selects any drive types, which is the default behavior. 
    * `sizeGibibytes`: The size of the logical drive as an integer to create in GiB. If unspecified or set to `0`, it will use the maximum capacity of physical drive for the logical drive. 
  * `softwareRAIDVolumes`: OpenShift Container Platform 4.22 does not support software RAID on the installation drive. This configuration contains the list of logical disks for software RAID. If you do not specify `rootDeviceHints`, the first volume is the root volume. If you set `HardwareRAIDVolumes`, this item will be invalid. Software RAIDs will always be deleted. The number of created software RAID devices must be `1` or `2`. If there is only one software RAID device, it must be `RAID-1`. If there are two RAID devices, the first device must be `RAID-1`, while the RAID level for the second device can be `0`, `1`, or `1+0`. The first RAID device will be the deployment device, which cannot be a software RAID volume. Enforcing `RAID-1` reduces the risk of a non-booting node in case of a device failure. The `softwareRAIDVolume` field defines the desired configuration of the volume in the software RAID. The sub-fields are: 
    * `level`: The RAID level for the logical drive. The following levels are supported: `0`,`1`,`1+0`. 
    * `physicalDisks`: A list of device hints. The number of items should be greater than or equal to `2`. 
    * `sizeGibibytes`: The size of the logical disk drive as an integer to be created in GiB. If unspecified or set to `0`, it will use the maximum capacity of physical drive for logical drive. 

You can set the `hardwareRAIDVolume` as an empty slice to clear the hardware RAID configuration. For example:  `spec: raid: hardwareRAIDVolume: []` If you receive an error message indicating that the driver does not support RAID, set the `raid`, `hardwareRAIDVolumes` or `softwareRAIDVolumes` to nil. You might need to ensure the host has a RAID controller.   
`rootDeviceHints: deviceName: hctl: model: vendor: serialNumber: minSizeGigabytes: wwn: wwnWithExtension: wwnVendorExtension: rotational:` |  The `rootDeviceHints` parameter enables provisioning of the RHCOS image to a particular device. It examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value. The configuration can combine multiple hints, but a device must match all hints to get selected. The fields are: 

  * `deviceName`: A string containing a Linux device name like `/dev/vda`. The hint must match the actual value exactly. 
  * `hctl`: A string containing a SCSI bus address like `0:0:0:0`. The hint must match the actual value exactly. 
  * `model`: A string containing a vendor-specific device identifier. The hint can be a substring of the actual value. 
  * `vendor`: A string containing the name of the vendor or manufacturer of the device. The hint can be a sub-string of the actual value. 
  * `serialNumber`: A string containing the device serial number. The hint must match the actual value exactly. 
  * `minSizeGigabytes`: An integer representing the minimum size of the device in gigabytes. 
  * `wwn`: A string containing the unique storage identifier. The hint must match the actual value exactly. 
  * `wwnWithExtension`: A string containing the unique storage identifier with the vendor extension appended. The hint must match the actual value exactly. 
  * `wwnVendorExtension`: A string containing the unique vendor storage identifier. The hint must match the actual value exactly. 
  * `rotational`: A boolean indicating whether the device should be a rotating disk (true) or not (false). 

  
Show more

### 4.10.2.2. The BareMetalHost status

The `BareMetalHost` status represents the host’s current state, and includes tested credentials, current hardware details, and other information. 

Table 4.2. BareMetalHost statusParameters| Description  
---|---  
`goodCredentials` |  A reference to the secret and its namespace holding the last set of baseboard management controller (BMC) credentials the system was able to validate as working.   
`errorMessage` |  Details of the last error reported by the provisioning backend, if any.   
`errorType` |  Indicates the class of problem that has caused the host to enter an error state. The error types are: 

  * `provisioned registration error`: Occurs when the controller is unable to reregister an already provisioned host. 
  * `registration error`: Occurs when the controller is unable to connect to the host’s baseboard management controller. 
  * `inspection error`: Occurs when an attempt to obtain hardware details from the host fails. 
  * `preparation error`: Occurs when cleaning fails. 
  * `provisioning error`: Occurs when the controller fails to provision or deprovision the host. 
  * `power management error`: Occurs when the controller is unable to modify the power state of the host. 
  * `detach error`: Occurs when the controller is unable to detach the host from the provisioner. 

  
`hardware: cpu arch: model: clockMegahertz: flags: count:` |  The `hardware.cpu` field details of the CPU(s) in the system. The fields include: 

  * `arch`: The architecture of the CPU. 
  * `model`: The CPU model as a string. 
  * `clockMegahertz`: The speed in MHz of the CPU. 
  * `flags`: The list of CPU flags. For example, `'mmx','sse','sse2','vmx'` etc. 
  * `count`: The number of CPUs available in the system. 

  
`hardware: firmware:` |  Contains BIOS firmware information. For example, the hardware vendor and version.   
`hardware: nics: - ip: name: mac: speedGbps: vlans: vlanId: pciAddress: pxe:` |  The `hardware.nics` field contains a list of network interfaces for the host. The fields include: 

  * `ip`: The IP address of the network interface controller (NIC), if one was assigned when the discovery agent ran. 
  * `name`: A string identifying the network device. For example, `nic-1`. 
  * `mac`: The MAC address of the NIC. 
  * `speedGbps`: The speed of the device in Gbps. 
  * `vlans`: A list holding all the VLANs available for this NIC. 
  * `vlanId`: The untagged VLAN ID. 
  * `pciAddress`: The PCI address of the NIC. For example, `0000:00:03.0`. 
  * `pxe`: Whether the NIC is able to boot using PXE. 

  
`hardware: ramMebibytes:` |  The host’s amount of memory in Mebibytes (MiB).   
`hardware: storage: - name: rotational: sizeBytes: serialNumber:` |  The `hardware.storage` field contains a list of storage devices available to the host. The fields include: 

  * `name`: A string identifying the storage device. For example, `disk 1 (boot)`. 
  * `rotational`: Indicates whether the disk is rotational, and returns either `true` or `false`. 
  * `sizeBytes`: The size of the storage device. 
  * `serialNumber`: The device’s serial number. 

  
`hardware: systemVendor: manufacturer: productName: serialNumber:` |  Contains information about the host’s `manufacturer`, the `productName`, and the `serialNumber`.   
`lastUpdated` |  The timestamp of the last time the status of the host was updated.   
`operationalStatus` |  The status of the server. The status is one of the following: 

  * `OK`: Indicates all the details for the host are known, correctly configured, working, and manageable. 
  * `discovered`: Implies some of the host’s details are either not working correctly or missing. For example, the BMC address is known but the login credentials are not. 
  * `error`: Indicates the system found some sort of unrecoverable error. Refer to the `errorMessage` field in the status section for more details. 
  * `delayed`: Indicates that provisioning is delayed to limit simultaneous provisioning of multiple hosts. 
  * `detached`: Indicates the host is marked `unmanaged`. 

  
`poweredOn` |  Boolean indicating whether the host is powered on.   
`provisioning: state: id: image: raid: firmware: rootDeviceHints:` |  The `provisioning` field contains values related to deploying an image to the host. The sub-fields include: 

  * `state`: The current state of any ongoing provisioning operation. The states include: 
    * `<empty string>`: There is no provisioning happening at the moment. 
    * `unmanaged`: There is insufficient information available to register the host. 
    * `registering`: The agent is checking the host’s BMC details. 
    * `match profile`: The agent is comparing the discovered hardware details on the host against known profiles. 
    * `available`: The host is available for provisioning. This state was previously known as `ready`. 
    * `preparing`: The existing configuration will be removed, and the new configuration will be set on the host. 
    * `provisioning`: The provisioner is writing an image to the host’s storage. 
    * `provisioned`: The provisioner wrote an image to the host’s storage. 
    * `externally provisioned`: Metal3 does not manage the image on the host. 
    * `deprovisioning`: The provisioner is wiping the image from the host’s storage. 
    * `inspecting`: The agent is collecting hardware details for the host. 
    * `deleting`: The agent is deleting the from the cluster. 
  * `id`: The unique identifier for the service in the underlying provisioning tool. 
  * `image`: The image most recently provisioned to the host. 
  * `raid`: The list of hardware or software RAID volumes recently set. 
  * `firmware`: The BIOS configuration for the bare-metal server. 
  * `rootDeviceHints`: The root device selection instructions used for the most recent provisioning operation. 

  
`triedCredentials` |  A reference to the secret and its namespace holding the last set of BMC credentials that were sent to the provisioning backend.   
Show more

**Additional resources**

  * [NICs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#spec-hardware-nics-2)



## 4.10.3. Getting the BareMetalHost resource

You can retrieve the `BareMetalHost` resource to review hardware details, provisioning state, BMC configuration, and power status for a physical host. 

**Procedure**

  1. Get the list of `BareMetalHost` resources: 

```shell-session
$ oc get bmh -n openshift-machine-api -o yaml
```


Note

You can use `baremetalhost` as the long form of `bmh` with `oc get` command. 

  2. Get the list of hosts: 

```shell-session
$ oc get bmh -n openshift-machine-api
```


  3. Get the `BareMetalHost` resource for a specific host: 

```shell-session
$ oc get bmh <host_name> -n openshift-machine-api -o yaml
```


Where `<host_name>` is the name of the host. 

**Example**

```yaml
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  creationTimestamp: "2022-06-16T10:48:33Z"
  finalizers:
  - baremetalhost.metal3.io
  generation: 2
  name: openshift-worker-0
  namespace: openshift-machine-api
  resourceVersion: "30099"
  uid: 1513ae9b-e092-409d-be1b-ad08edeb1271
spec:
  automatedCleaningMode: metadata
  bmc:
    address: redfish://10.46.61.19:443/redfish/v1/Systems/1
    credentialsName: openshift-worker-0-bmc-secret
    disableCertificateVerification: true
  bootMACAddress: 48:df:37:c7:f7:b0
  bootMode: UEFI
  consumerRef:
    apiVersion: machine.openshift.io/v1beta1
    kind: Machine
    name: ocp-edge-958fk-worker-0-nrfcg
    namespace: openshift-machine-api
  customDeploy:
    method: install_coreos
  online: true
  rootDeviceHints:
    deviceName: /dev/disk/by-id/scsi-<serial_number>
  userData:
    name: worker-user-data-managed
    namespace: openshift-machine-api
status:
  errorCount: 0
  errorMessage: ""
  goodCredentials:
    credentials:
      name: openshift-worker-0-bmc-secret
      namespace: openshift-machine-api
    credentialsVersion: "16120"
  hardware:
    cpu:
      arch: x86_64
      clockMegahertz: 2300
      count: 64
      flags:
      - 3dnowprefetch
      - abm
      - acpi
      - adx
      - aes
      model: Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz
    firmware:
      bios:
        date: 10/26/2020
        vendor: HPE
        version: U30
    hostname: openshift-worker-0
    nics:
    - mac: 48:df:37:c7:f7:b3
      model: 0x8086 0x1572
      name: ens1f3
    ramMebibytes: 262144
    storage:
    - hctl: "0:0:0:0"
      model: VK000960GWTTB
      name: /dev/disk/by-id/scsi-<serial_number>
      sizeBytes: 960197124096
      type: SSD
      vendor: ATA
    systemVendor:
      manufacturer: HPE
      productName: ProLiant DL380 Gen10 (868703-B21)
      serialNumber: CZ200606M3
  lastUpdated: "2022-06-16T11:41:42Z"
  operationalStatus: OK
  poweredOn: true
  provisioning:
    ID: 217baa14-cfcf-4196-b764-744e184a3413
    bootMode: UEFI
    customDeploy:
      method: install_coreos
    image:
      url: ""
    raid:
      hardwareRAIDVolumes: null
      softwareRAIDVolumes: []
    rootDeviceHints:
      deviceName: /dev/disk/by-id/scsi-<serial_number>
    state: provisioned
  triedCredentials:
    credentials:
      name: openshift-worker-0-bmc-secret
      namespace: openshift-machine-api
    credentialsVersion: "16120"
```


## 4.10.4. Editing a BareMetalHost resource

You can edit a node’s `BareMetalHost` resource to update BMC information, move nodes between clusters, or modify provisioning configuration. 

Consider the following examples: 

  * You deploy a cluster with the Assisted Installer and need to add or edit the baseboard management controller (BMC) host name or IP address. 
  * You want to move a node from one cluster to another without deprovisioning it. 



**Prerequisites**

  * Ensure the node is in the `Provisioned`, `ExternallyProvisioned`, or `Available` state. 



**Procedure**

  1. Get the list of nodes: 

```shell-session
$ oc get bmh -n openshift-machine-api
```


  2. Before editing the node’s `BareMetalHost` resource, detach the node from Ironic by running the following command: 

```shell-session
$ oc annotate baremetalhost <node_name> -n openshift-machine-api 'baremetalhost.metal3.io/detached=true'
```


Replace `<node_name>` with the name of the node. 

  3. Edit the `BareMetalHost` resource by running the following command: 

```shell-session
$ oc edit bmh <node_name> -n openshift-machine-api
```


  4. Reattach the node to Ironic by running the following command: 

```shell-session
$ oc annotate baremetalhost <node_name> -n openshift-machine-api 'baremetalhost.metal3.io/detached'-
```


## 4.10.5. Troubleshooting latency when deleting a BareMetalHost resource

You can disable the cleaning process to resolve latency when deleting a `BareMetalHost` resource if Ironic’s cleanup retries cause the provisioning status to remain in the deleting state. 

When the Bare Metal Operator (BMO) deletes a `BareMetalHost` resource, Ironic deprovisions the bare-metal host with a process called cleaning. When cleaning fails, Ironic retries the cleaning process three times, which is the source of the latency. The cleaning process might not succeed, causing the provisioning status of the bare-metal host to remain in the **deleting** state indefinitely. When this occurs, use the following procedure to disable the cleaning process. 

Warning

Do not remove finalizers from the `BareMetalHost` resource. 

**Procedure**

  1. If the cleaning process fails and restarts, wait for it to finish. This might take about 5 minutes. 
  2. If the provisioning status remains in the **deleting** state, disable the cleaning process by modifying the `BareMetalHost` resource and setting the `automatedCleaningMode` field to `disabled`. See "Editing a `BareMetalHost` resource" for additional details. 



## 4.10.6. Attaching a non-bootable ISO to a bare-metal node

You can attach a generic, non-bootable ISO virtual media image to a provisioned node by using the `DataImage` resource. After you apply the resource, the ISO image becomes accessible to the operating system after it has booted. 

This is useful for configuring a node after provisioning the operating system and before the node boots for the first time. 

**Prerequisites**

  * The node must use Redfish or drivers derived from it to support this feature. 
  * The node must be in the `Provisioned` or `ExternallyProvisioned` state. 
  * The `name` must be the same as the name of the node defined in its `BareMetalHost` resource. 
  * You have a valid `url` to the ISO image. 



**Procedure**

  1. Create a `DataImage` resource: 

```yaml
apiVersion: metal3.io/v1alpha1
kind: DataImage
metadata:
  name: <node_name>
spec:
  url: "http://dataimage.example.com/non-bootable.iso"
```


where: 

`<node_name>`
     Specifies the name of the node as defined in its `BareMetalHost` resource. 
`spec.url`
     Specifies the URL and path to the ISO image. 

  2. Save the `DataImage` resource to a file by running the following command: 

```shell-session
$ vim <node_name>-dataimage.yaml
```


  3. Apply the `DataImage` resource by running the following command: 

```shell-session
$ oc apply -f <node_name>-dataimage.yaml -n <node_namespace>
```


Replace `<node_namespace>` so that the namespace matches the namespace for the `BareMetalHost` resource. For example, `openshift-machine-api`. 

  4. Reboot the node. 

Note

To reboot the node, attach the `reboot.metal3.io` annotation, or reset set the `online` status in the `BareMetalHost` resource. A forced reboot of the bare-metal node will change the state of the node to `NotReady` for awhile. For example, 5 minutes or more. 

  5. View the `DataImage` resource by running the following command: 

```shell-session
$ oc get dataimage <node_name> -n openshift-machine-api -o yaml
```


**Example output**

```yaml
apiVersion: v1
items:
- apiVersion: metal3.io/v1alpha1
  kind: DataImage
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"metal3.io/v1alpha1","kind":"DataImage","metadata":{"annotations":{},"name":"bmh-node-1","namespace":"openshift-machine-api"},"spec":{"url":"http://dataimage.example.com/non-bootable.iso"}}
    creationTimestamp: "2024-06-10T12:00:00Z"
    finalizers:
    - dataimage.metal3.io
    generation: 1
    name: bmh-node-1
    namespace: openshift-machine-api
    ownerReferences:
    - apiVersion: metal3.io/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: BareMetalHost
      name: bmh-node-1
      uid: 046cdf8e-0e97-485a-8866-e62d20e0f0b3
    resourceVersion: "21695581"
    uid: c5718f50-44b6-4a22-a6b7-71197e4b7b69
  spec:
    url: http://dataimage.example.com/non-bootable.iso
  status:
    attachedImage:
      url: http://dataimage.example.com/non-bootable.iso
    error:
      count: 0
      message: ""
    lastReconciled: "2024-06-10T12:05:00Z"
```


## 4.10.7. Configuring NC-SI and DisablePowerOff for shared NICs

The Network Controller Sideband Interface (NC-SI) enables the Baseboard Management Controller (BMC) to share a system network interface card (NIC) with the host for management traffic, using protocols like Redfish, IPMI, or vendor-specific interfaces. 

The `DisablePowerOff` feature prevents hard power-offs, ensuring soft reboots to maintain BMC connectivity. 

**Prerequisites**

  * NC-SI-capable hardware and NICs. 
  * BMC configured with an IP address and network connection. 
  * Administrative access to the BMC. 
  * Access to the OpenShift cluster with `cluster-admin` privileges. 



**Procedure**

  1. Configure the BMC to enable NC-SI for a shared NIC. 
  2. Verify BMC connectivity using Redfish or IPMI by running one of the following commands: 

```shell-session
$ curl -k https://<bmc_ip>/redfish/v1/Systems/1
```


```shell-session
$ ipmitool -I lanplus -H <bmc_ip> -U <user> -P <pass> power status
```


  3. Enable the `DisablePowerOff` feature by editing the `BareMetalHost` resource in the `openshift-machine-api` namespace: 

```yaml
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: example-host
  namespace: openshift-machine-api
spec:
  online: true
  bmc:
    address: <protocol>://<bmc_ip>/<bmc_address_format>
    credentialsName: bmc-secret
  disablePowerOff: true
```


See the "BMC addressing" sections for details on supported protocols and BMC address formats. 

  4. Apply the changes by running the following command: 

```shell-session
$ oc apply -f <filename>.yaml
```


**Verification**

  * Check the `BareMetalHost` status by running the following command: 

```shell-session
$ oc get baremetalhost example-host -n openshift-machine-api -o yaml
```


Confirm that `disablePowerOff: true` is in the `spec` section. 

  * Test a reboot by restarting a node pod and verify that BMC connectivity remains active. 
  * Attempt to set `BareMetalHost.spec.online=false`. It should fail with an error indicating power-off is disabled. 



## 4.10.8. About the HostFirmwareSettings resource

You can use the `HostFirmwareSettings` resource to retrieve and manage BIOS settings for a host, providing vendor-specific configuration beyond the basic firmware fields in the `BareMetalHost` resource. 

When a host moves to the `Available` state, Ironic reads the host’s BIOS settings and creates the `HostFirmwareSettings` resource. The resource contains the complete BIOS configuration returned from the baseboard management controller (BMC). Whereas, the `firmware` field in the `BareMetalHost` resource returns three vendor-independent fields, the `HostFirmwareSettings` resource typically comprises many BIOS settings of vendor-specific fields per host. 

The `HostFirmwareSettings` resource contains two sections: 

  1. The `HostFirmwareSettings` spec. 
  2. The `HostFirmwareSettings` status. 



Note

Reading and modifying firmware settings is only supported for drivers based on the vendor-independent Redfish protocol, Fujitsu iRMC or HP iLO. 

### 4.10.8.1. The HostFirmwareSettings spec

The `spec` section of the `HostFirmwareSettings` resource defines the desired state of the host’s BIOS, and it is empty by default. Ironic uses the settings in the `spec.settings` section to update the baseboard management controller (BMC) when the host is in the `Preparing` state. Use the `FirmwareSchema` resource to ensure that you do not send invalid name/value pairs to hosts. See "About the `FirmwareSchema` resource" for additional details. 

**Example**

```shell-session
spec:
  settings:
    ProcTurboMode: Disabled
```


where: 

`spec.settings.ProcTurboMode: Disabled`
     Specifies a name/value pair that sets the `ProcTurboMode` BIOS setting to `Disabled`. 

Note

Integer parameters listed in the `status` section appear as strings. For example, `"1"`. When setting integers in the `spec.settings` section, the values should be set as integers without quotes. For example, `1`. 

### 4.10.8.2. The HostFirmwareSettings status

The `status` represents the current state of the host’s BIOS. 

Table 4.3. HostFirmwareSettingsParameters| Description  
---|---  
`status: conditions: - lastTransitionTime: message: observedGeneration: reason: status: type:` |  The `conditions` field contains a list of state changes. The sub-fields include: 

  * `lastTransitionTime`: The last time the state changed. 
  * `message`: A description of the state change. 
  * `observedGeneration`: The current generation of the `status`. If `metadata.generation` and this field are not the same, the `status.conditions` might be out of date. 
  * `reason`: The reason for the state change. 
  * `status`: The status of the state change. The status can be `True`, `False` or `Unknown`. 
  * `type`: The type of state change. The types are `Valid` and `ChangeDetected`. 

  
`status: schema: name: namespace: lastUpdated:` |  The `FirmwareSchema` for the firmware settings. The fields include: 

  * `name`: The name or unique identifier referencing the schema. 
  * `namespace`: The namespace where the schema is stored. 
  * `lastUpdated`: The last time the resource was updated. 

  
`status: settings:` |  The `settings` field contains a list of name/value pairs of a host’s current BIOS settings.   
Show more

## 4.10.9. Getting the HostFirmwareSettings resource

The `HostFirmwareSettings` resource contains the vendor-specific BIOS properties of a physical host. You must get the `HostFirmwareSettings` resource for a physical host to review its BIOS properties. 

**Procedure**

  1. Get the detailed list of `HostFirmwareSettings` resources by running the following command: 

```shell-session
$ oc get hfs -n openshift-machine-api -o yaml
```


Note

You can use `hostfirmwaresettings` as the long form of `hfs` with the `oc get` command. 

  2. Get the list of `HostFirmwareSettings` resources by running the following command: 

```shell-session
$ oc get hfs -n openshift-machine-api
```


  3. Get the `HostFirmwareSettings` resource for a particular host by running the following command: 

```shell-session
$ oc get hfs <host_name> -n openshift-machine-api -o yaml
```


Where `<host_name>` is the name of the host. 




## 4.10.10. Editing the HostFirmwareSettings resource of a provisioned host

You can modify BIOS settings on a provisioned host by editing the `HostFirmwareSettings` resource, then scaling the machine set down and up to apply the changes. 

Important

You can only edit hosts when they are in the `provisioned` state, excluding read-only values. You cannot edit hosts in the `externally provisioned` state. 

**Procedure**

  1. Get the list of `HostFirmwareSettings` resources by running the following command: 

```shell-session
$ oc get hfs -n openshift-machine-api
```


  2. Edit the host `HostFirmwareSettings` resource by running the following command: 

```shell-session
$ oc edit hfs <hostname> -n openshift-machine-api
```


Where `<hostname>` is the name of a provisioned host. The `HostFirmwareSettings` resource will open in the default editor for your terminal. 

  3. Add name and value pairs to the `spec.settings` section by running the following command: 

**Example**

```shell-session
spec:
  settings:
    name: value
```


where: 

`spec.settings.name`
     Specifies the firmware setting name and value. Use the `FirmwareSchema` resource to identify the available settings for the host. You cannot set values that are read-only. 

  4. Save the changes and exit the editor. 
  5. Get the host machine name by running the following command: 

```shell-session
 $ oc get bmh <hostname> -n openshift-machine name
```


Where `<hostname>` is the name of the host. The terminal displays the machine name under the `CONSUMER` field. 

  6. Annotate the machine to delete it from the machine set by running the following command: 

```shell-session
$ oc annotate machine <machine_name> machine.openshift.io/delete-machine=true -n openshift-machine-api
```


Where `<machine_name>` is the name of the machine to delete. 

  7. Get a list of nodes and count the number of worker nodes by running the following command: 

```shell-session
$ oc get nodes
```


  8. Get the machine set by running the following command: 

```shell-session
$ oc get machinesets -n openshift-machine-api
```


  9. Scale the machine set by running the following command: 

```shell-session
$ oc scale machineset <machineset_name> -n openshift-machine-api --replicas=<n-1>
```


Where `<machineset_name>` is the name of the machine set and `<n-1>` is the decremented number of worker nodes. 

  10. When the host enters the `Available` state, scale up the machine set to make the `HostFirmwareSettings` resource changes take effect by running the following command: 

```shell-session
$ oc scale machineset <machineset_name> -n openshift-machine-api --replicas=<n>
```


Where `<machineset_name>` is the name of the machine set and `<n>` is the number of worker nodes. 




## 4.10.11. Performing a live update to the HostFirmwareSettings resource

You can perform a live update to the `HostFirmwareSettings` resource after it has begun running workloads. Live updates do not trigger deprovisioning and reprovisioning the host. 

Warning

Performing a live update to the `HostFirmwareSettings` resource can be a destructive and destabilizing action. Perform these updates only after careful consideration. 

Before you apply a live update in a production cluster, validate the update in a development or test cluster. Ensure that these updates comply with your organization’s test policies before you apply them to a production cluster. 

If a cluster has fewer than three compute nodes, use caution. Firmware updates in such clusters can result in the cluster entering a degraded state. 

Do not interrupt firmware updates. If the update stops responding, engage the support of your hardware vendor. 

**Prerequisites**

  * The `HostUpdatePolicy` resource must have the `firmwareSettings` parameter set to `onReboot`. 



**Procedure**

  1. Update the `HostFirmwareSettings` resource by running the following command: 

```shell-session
$ oc patch hostfirmwaresettings <hostname> --type merge -p \
    '{"spec": {"settings": {"<name>": "<value>"}}}'
```


where: 

`<hostname>`
     Specifies the name of the host. 
`<name>`
     Specifies the name of the setting. 
`<value>`
     Specifies the value of the setting. You can set multiple name-value pairs. 

Note

Get the `FirmwareSchema` resource to determine which settings the hardware supports and what settings and values you can update. You cannot update read-only values and you cannot update the `FirmwareSchema` resource. You can also use the `oc edit <hostname> hostfirmwaresettings -n openshift-machine-api` command to update the `HostFirmwareSettings` resource. 

  2. Cordon and drain the node by running the following command: 

```shell-session
$ oc drain <node_name> --force
```


For `<node_name>`, specify the name of the node. 

  3. Power off the host for a period of 5 minutes by running the following command: 

```shell-session
$ oc patch bmh <hostname> --type merge -p '{"spec": {"online": false}}'
```


This step ensures that daemonsets or controllers can mark any infrastructure pods that might be running on the host as offline, while the remaining hosts handle incoming requests. 

  4. After 5 minutes, power on the host by running the following command: 

```shell-session
$ oc patch bmh <hostname> --type merge -p '{"spec": {"online": true}}'
```


The servicing operation commences and the Bare Metal Operator (BMO) sets the `operationalStatus` parameter of the `BareMetalHost` to `servicing`. The BMO updates the `operationalStatus` parameter to `OK` after updating the resource. If an error occurs, the BMO updates the `operationalStatus` parameter to `error` and retries the operation. 

  5. Once Ironic completes the update and the host powers up, uncordon the node by running the following command: 

```shell-session
$ oc uncordon <node_name>
```


## 4.10.12. Verifying the HostFirmware Settings resource is valid

You can verify that changes to the `HostFirmwareSettings` resource are valid by checking the status conditions, ensuring that BIOS setting values comply with the `FirmwareSchema` constraints. 

**Procedure**

  1. Get a list of `HostFirmwareSetting` resources: 

```shell-session
$ oc get hfs -n openshift-machine-api
```


  2. Verify that the `HostFirmwareSettings` resource for a particular host is valid: 

```shell-session
$ oc describe hfs <host_name> -n openshift-machine-api
```


Where `<host_name>` is the name of the host. 

**Example output:**

```shell-session
Events:
  Type    Reason            Age    From                                    Message
  ----    ------            ----   ----                                    -------
  Normal  ValidationFailed  2m49s  metal3-hostfirmwaresettings-controller  Invalid BIOS setting: Setting ProcTurboMode is invalid, unknown enumeration value - Foo
```


Important

If the response returns `ValidationFailed`, there is an error in the resource configuration and you must update the values to conform to the `FirmwareSchema` resource. 




## 4.10.13. About the FirmwareSchema resource

The `FirmwareSchema` resource contains valid types and limits for BIOS settings on each host model, enabling you to identify valid values when configuring the `HostFirmwareSettings` resource. 

Table 4.4. FirmwareSchema specificationParameters| Description  
---|---  
`<BIOS_setting_name> attribute_type: allowable_values: lower_bound: upper_bound: min_length: max_length: read_only: unique:` |  The `spec` is a simple map consisting of the BIOS setting name and the limits of the setting. The fields include: 

  * `attribute_type`: The type of setting. The supported types are: 
    * `Enumeration`
    * `Integer`
    * `String`
    * `Boolean`
  * `allowable_values`: A list of allowable values when the `attribute_type` is `Enumeration`. 
  * `lower_bound`: The lowest allowed value when `attribute_type` is `Integer`. 
  * `upper_bound`: The highest allowed value when `attribute_type` is `Integer`. 
  * `min_length`: The shortest string length that the value can have when `attribute_type` is `String`. 
  * `max_length`: The longest string length that the value can have when `attribute_type` is `String`. 
  * `read_only`: The setting is read only and cannot be modified. 
  * `unique`: The setting is specific to this host. 

  
Show more

## 4.10.14. Getting the FirmwareSchema resource

Each host model from each vendor has different BIOS settings. When editing the `HostFirmwareSettings` resource’s `spec` section, the name/value pairs you set must conform to that host’s firmware schema. To ensure you are setting valid name/value pairs, get the `FirmwareSchema` for the host and review it. 

**Procedure**

  1. Get the list of `FirmwareSchema` resource instances by running the following command: 

```shell-session
$ oc get firmwareschema -n openshift-machine-api
```


  2. Get a particular `FirmwareSchema` instance by running the following command: 

```shell-session
$ oc get firmwareschema <instance_name> -n openshift-machine-api -o yaml
```


Where `<instance_name>` is the name of the schema instance stated in the `HostFirmwareSettings` resource (see Table 3). 




## 4.10.15. About the HostFirmwareComponents resource

You can use the `HostFirmwareComponents` resource to view and update Basic Input/Output System (BIOS), baseboard management controller (BMC), and network interface controller (NIC) firmware versions for bare-metal hosts. 

To update NIC host firmware components, the server must support Redfish and must permit you to use Redfish to update NIC firmware. You can use Metal3 to update NIC host firmware components for the Intel Ethernet 800 Series (`ice` driver) and the NVIDIA Mellanox ConnectX-6 (CX6) and ConnectX-7 (CX7) (`mlx_5` driver). The updates are validated on Dell hardware. The following list outlines important considerations before you update the NICs: 

  * If you have more than one network adapter with the same type of NIC, for example, Intel Ethernet 800 Series, when you update one NIC the update might be applied to multiple NICs. Redfish identifies all components that can benefit from the update and then applies the image to all these components. 
  * You cannot necessarily update a listed network adapter. A machine might use Redfish to display their NIC and firmware information, but prevent you from updating the adapter through Redfish. For more information about checking if you can update a network adapter, see "Identifying the NICs `HostFirmwareComponents` resources you can update". 



The `HostFirmwareComponents` resource contains two sections: 

  1. The `HostFirmwareComponents` spec 
  2. The `HostFirmwareComponents` status 



### 4.10.15.1. HostFirmwareComponents spec

The `spec` section of the `HostFirmwareComponents` resource defines the desired state of the BIOS and BMC versions of the host, and the NIC firmware components of the host if the information is available by using Redfish. 

Table 4.5. HostFirmwareComponents specParameters| Description  
---|---  
`updates: component: url:` |  The `updates` configuration setting contains the components to update. The fields are: 

  * `component`: The name of the component. The valid settings are `bios`, `bmc`, or `nic:<ID>`. 
  * `url`: The URL to the component’s firmware specification and version. 

  
Show more

### 4.10.15.2. HostFirmwareComponents status

The `status` section of the `HostFirmwareComponents` resource returns the current status of the BIOS and BMC versions of the host, and the NIC firmware components of the host if the information is available by using Redfish. 

Table 4.6. HostFirmwareComponents statusParameters| Description  
---|---  
`components: component: initialVersion: currentVersion: lastVersionFlashed: updatedAt:` |  The `components` section contains the status of the components. The fields are: 

  * `component`: The name of the firmware component. It returns `bios`, `bmc`, `nic:<ID1>`, or `nic:<ID2>`. 
  * `initialVersion`: The initial firmware version of the component. Ironic retrieves this information when creating the `BareMetalHost` resource. You cannot change it. 
  * `currentVersion`: The current firmware version of the component. Initially, the value matches the `initialVersion` value until Ironic updates the firmware on the bare-metal host. 
  * `lastVersionFlashed`: The last firmware version of the component flashed on the bare-metal host. This field returns `null` until Ironic updates the firmware. 
  * `updatedAt`: The timestamp when Ironic updated the bare-metal host’s firmware. 

  
`updates: component: url:` |  The `updates` configuration setting contains the updated components. The fields are: 

  * `component`: The name of the component. 
  * `url`: The URL to the component’s firmware specification and version. 

  
Show more

## 4.10.16. Getting the HostFirmwareComponents resource

The `HostFirmwareComponents` resource contains the specific firmware version of the BIOS and baseboard management controller (BMC) of a physical host. You must get the `HostFirmwareComponents` resource for a physical host to review the firmware version and status. 

**Procedure**

  1. Get the detailed list of `HostFirmwareComponents` resources by running the following command: 

```shell-session
$ oc get hostfirmwarecomponents -n openshift-machine-api -o yaml
```


  2. Get the list of `HostFirmwareComponents` resources by running the following command: 

```shell-session
$ oc get hostfirmwarecomponents -n openshift-machine-api
```


  3. Get the `HostFirmwareComponents` resource for a particular host by running the following command: 

```shell-session
$ oc get hostfirmwarecomponents <host_name> -n openshift-machine-api -o yaml
```


Where `<host_name>` is the name of the host. 

**Example**

```yaml
---
apiVersion: metal3.io/v1alpha1
kind: HostFirmwareComponents
metadata:
  creationTimestamp: 2024-04-25T20:32:06Z"
  generation: 1
  name: ostest-master-2
  namespace: openshift-machine-api
  ownerReferences:
  - apiVersion: metal3.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: BareMetalHost
    name: ostest-master-2
    uid: 16022566-7850-4dc8-9e7d-f216211d4195
  resourceVersion: "2437"
  uid: 2038d63f-afc0-4413-8ffe-2f8e098d1f6c
spec:
  updates: []
status:
  components:
  - component: bios
    currentVersion: 1.0.0
    initialVersion: 1.0.0
  - component: bmc
    currentVersion: "1.00"
    initialVersion: "1.00"
  - component: nic:<ID1>
    currentVersion: 0.10.0
    initialVersion: 0.10.0
  - component: nic:<ID2>
    currentVersion: 1.8.1
    initialVersion: 1.8.1
  conditions:
  - lastTransitionTime: "2024-04-25T20:32:06Z"
    message: ""
    observedGeneration: 1
    reason: OK
    status: "True"
    type: Valid
  - lastTransitionTime: "2024-04-25T20:32:06Z"
    message: ""
    observedGeneration: 1
    reason: OK
    status: "False"
    type: ChangeDetected
  lastUpdated: "2024-04-25T20:32:06Z"
  updates: []
```


## 4.10.17. Editing the HostFirmwareComponents resource of a provisioned host

You can edit the `HostFirmwareComponents` resource to upgrade or downgrade BIOS and BMC firmware versions on a provisioned host without deprovisioning it. 

**Procedure**

  1. Get the detailed list of `HostFirmwareComponents` resources by running the following command: 

```shell-session
$ oc get hostfirmwarecomponents -n openshift-machine-api -o yaml
```


  2. Edit the `HostFirmwareComponents` resource by running the following command: 

```shell-session
$ oc edit <hostname> hostfirmwarecomponents -n openshift-machine-api
```


Where `<hostname>` is the name of the host. The `HostFirmwareComponents` resource will open in the default editor for your terminal. 

  3. Make the appropriate edits. 

**Example output**

```yaml
---
apiVersion: metal3.io/v1alpha1
kind: HostFirmwareComponents
metadata:
  creationTimestamp: 2024-04-25T20:32:06Z"
  generation: 1
  name: ostest-master-2
  namespace: openshift-machine-api
  ownerReferences:
  - apiVersion: metal3.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: BareMetalHost
    name: ostest-master-2
    uid: 16022566-7850-4dc8-9e7d-f216211d4195
  resourceVersion: "2437"
  uid: 2038d63f-afc0-4413-8ffe-2f8e098d1f6c
spec:
  updates:
    - name: bios
      url: https://myurl.with.firmware.for.bios
    - name: bmc
      url: https://myurl.with.firmware.for.bmc
status:
  components:
  - component: bios
    currentVersion: 1.0.0
    initialVersion: 1.0.0
  - component: bmc
    currentVersion: "1.00"
    initialVersion: "1.00"
  conditions:
  - lastTransitionTime: "2024-04-25T20:32:06Z"
    message: ""
    observedGeneration: 1
    reason: OK
    status: "True"
    type: Valid
  - lastTransitionTime: "2024-04-25T20:32:06Z"
    message: ""
    observedGeneration: 1
    reason: OK
    status: "False"
    type: ChangeDetected
  lastUpdated: "2024-04-25T20:32:06Z"
```


where: 

`spec.updates.- name`
     Specifies the firmware component to update. Set to `bios` to update the BIOS version or `bmc` to update the BMC version. 
`spec.updates.- name.url`
     Specifies the URL for the firmware version. 

  4. Save the changes and exit the editor. 
  5. Get the host machine name by running the following command: 

```shell-session
$ oc get bmh <host_name> -n openshift-machine name
```


Where `<host_name>` is the name of the host. The terminal displays the machine name under the `CONSUMER` field. 

  6. Annotate the machine to delete it from the machine set by running the following command: 

```shell-session
$ oc annotate machine <machine_name> machine.openshift.io/delete-machine=true -n openshift-machine-api
```


Where `<machine_name>` is the name of the machine to delete. 

  7. Get a list of nodes and count the number of worker nodes by running the following command: 

```shell-session
$ oc get nodes
```


  8. Get the machine set by running the following command: 

```shell-session
$ oc get machinesets -n openshift-machine-api
```


  9. Scale down the machine set by running the following command: 

```shell-session
$ oc scale machineset <machineset_name> -n openshift-machine-api --replicas=<n-1>
```


Where `<machineset_name>` is the name of the machine set and `<n-1>` is the decremented number of worker nodes. 

  10. When the host enters the `Available` state, scale up the machine set to make the `HostFirmwareComponents` resource changes take effect by running the following command: 

```shell-session
$ oc scale machineset <machineset_name> -n openshift-machine-api --replicas=<n>
```


Where `<machineset_name>` is the name of the machine set and `<n>` is the number of worker nodes. 




## 4.10.18. Performing a live update to the HostFirmwareComponents resource

You can perform a live update to the `HostFirmwareComponents` resource on an already provisioned host. Live updates do not trigger deprovisioning and reprovisioning the host. 

Warning

Performing a live update to the `HostFirmwareComponents` resource can be a destructive and destabilizing action. Perform these updates only after careful consideration. 

Before you apply a live update in a production cluster, validate the update in a development or test cluster. Ensure that these updates comply with your organization’s test policies before you apply them to a production cluster. 

If a cluster has fewer than three compute nodes, use caution. Firmware updates in such clusters can result in the cluster entering a degraded state. 

Do not interrupt firmware updates. If the update stops responding, engage the support of your hardware vendor. 

**Prerequisites**

  * The `HostUpdatePolicy` resource must have the `firmwareUpdates` parameter set to `onReboot`. 



**Procedure**

  1. Update the `HostFirmwareComponents` resource by running the following command: 

```shell-session
$ oc patch hostfirmwarecomponents <hostname> --type merge -p \
    '{"spec": {"updates": [{"component": "<type>", \
                        "url": "<url>"}]}}'
```


where: 

`<hostname>`
     Specifies the name of the host. 
`<type>`
     Specifies the type of component, either `bios` or `bmc`. 
`<url>`
     Specifies the URL for the component. 

Note

You can also use the `oc edit <hostname> hostfirmwarecomponents -n openshift-machine-api` command to update the resource. 

  2. Cordon and drain the node by running the following command: 

```shell-session
$ oc drain <node_name> --force
```


For `<node_name>`, specify the name of the node. 

  3. Power off the host for a period of 5 minutes by running the following command: 

```shell-session
$ oc patch bmh <hostname> --type merge -p '{"spec": {"online": false}}'
```


This step ensures that daemonsets or controllers mark any infrastructure pods that might be running on the node as offline, while the remaining nodes handle incoming requests. 

  4. After 5 minutes, power on the host by running the following command: 

```shell-session
$ oc patch bmh <hostname> --type merge -p '{"spec": {"online": true}}'
```


The servicing operation commences and the Bare Metal Operator (BMO) sets the `operationalStatus` parameter of the `BareMetalHost` to `servicing`. The BMO updates the `operationalStatus` parameter to `OK` after updating the resource. If an error occurs, the BMO updates the `operationalStatus` parameter to `error` and retries the operation. 

  5. Uncordon the node by running the following command: 

```shell-session
$ oc uncordon <node_name>
```


## 4.10.19. Identifying the NICs HostFirmwareComponents resources you can update

You can use the Redfish `NetworkAdapters` resource to identify network interface controllers (NICs) that were added to the `HostFirmwareComponents` custom resource (CR). The NIC is displayed in the CR with the prefix `nic:` followed by the network adapter ID of the resource. For example, `nic:AD007`. 

**Procedure**

  1. Get the detailed list of `HostFirmwareComponents` NIC resources by running the following command: 

```shell-session
$ curl -ksu “$USER:$PASS” https://<BMC>/redfish/v1/Chassis/<SystemID>/NetworkAdapters | jq .
```


The `<SystemID>` is based on the value that you set for `bmh` in the `spec.bmc.address`. 

**Example output**

```yaml
{
  "@odata.context": "/redfish/v1/$metadata#NetworkAdapterCollection.NetworkAdapterCollection",
  "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters",
  "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
  "Description": "Collection Of Network Adapter",
  "Members": [
    {
      "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1"
    },
    {
      "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Slot.3"
    }
  ],
  "Members@odata.count":2,
  "Name": "Network Adapter Collection"
}
```


  2. Identify the corresponding network adapter in the firmware inventory resource, as the network adapter does not indicate if you can update firmware with Redfish, by running the following command: 

```shell-session
$ curl -ksu “$USER:$PASS” https://<BMC>/redfish/v1/UpdateService/FirmwareInventory | jq .
```


**Example output**

```yaml
{
  "@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
  "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory",
  "@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
  "Description": "Collection of Firmware Inventory",
  "Members": [
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-102303-22.0.9__NIC.Integrated.1-2-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-102303-22.0.9__NIC.Integrated.1-3-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-102303-22.0.9__NIC.Integrated.1-4-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-102378-22.0.9__NIC.Integrated.1-1-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-104480-14.31.22.50__NIC.Slot.3-1-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-104480-14.31.22.50__NIC.Slot.3-2-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-102303-22.0.9__NIC.Integrated.1-2-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-102303-22.0.9__NIC.Integrated.1-3-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-102303-22.0.9__NIC.Integrated.1-4-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-102378-22.0.9__NIC.Integrated.1-1-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-104480-14.31.22.50__NIC.Slot.3-1-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-104480-14.31.22.50__NIC.Slot.3-2-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Previous-102303-20.0.17__NIC.Integrated.1-2-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Previous-102303-20.0.17__NIC.Integrated.1-3-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Previous-102303-20.0.17__NIC.Integrated.1-4-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Previous-102378-20.0.17__NIC.Integrated.1-1-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Previous-104480-14.24.80.00__NIC.Slot.3-1-1"
    },
    {
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Previous-104480-14.24.80.00__NIC.Slot.3-2-1"
    }
  ],
  "Members@odata.count": 18,
  "Name": "Firmware Inventory Collection"
}
```


  3. Check if the parameter is set to `true` by running the following command: 

```shell-session
$ curl -ksu "$USER:$PASS" https://<BMC>/redfish/v1/UpdateService/FirmwareInventory/Current-102303-22.0.9__NIC.Integrated.1-2-1 | jq .
```


**Example output**

```yaml
{
  "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
  "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-102303-22.0.9__NIC.Integrated.1-2-1",
  "@odata.type": "#SoftwareInventory.v1_9_0.SoftwareInventory",
  "Description": "Represents Firmware Inventory",
  "Id": "Current-102303-22.0.9__NIC.Integrated.1-2-1",
  "Name": "Intel(R) Ethernet 10G X710 rNDC - E4:43:4B:4B:60:B1",
  "Oem": {
    "Dell": {
      "@odata.type": "#DellOem.v1_3_0.DellOemResources",
      "DellSoftwareInventory": {
        "@odata.context": "/redfish/v1/$metadata#DellSoftwareInventory.DellSoftwareInventory",
        "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-102303-22.0.9__NIC.Integrated.1-2-1/Oem/Dell/DellSoftwareInventory/DCIM:CURRENT_0x23_701__NIC.Integrated.1-2-1",
        "@odata.type": "#DellSoftwareInventory.v1_2_0.DellSoftwareInventory",
        "BuildNumber": 0,
        "Classifications": [
          "Firmware"
        ],
        "Classifications@odata.count": 1,
        "ComponentID": "102303",
        "ComponentType": "FRMW",
        "Description": "The DellSoftwareInventory resource is a representation of an available device firmware in the managed system.",
        "DeviceID": "1572",
        "ElementName": "Intel(R) Ethernet 10G X710 rNDC - E4:43:4B:4B:60:B1",
        "HashValue": "1158cfbfdf6cb387bc0806999b28b83892cfaf1307b466abd6546ff8e5ea1459",
        "Id": "DCIM:CURRENT_0x23_701__NIC.Integrated.1-2-1",
        "IdentityInfoType": [
          "OrgID:ComponentType:VendorID:DeviceID:SubVendorID:SubDeviceID"
        ],
        "IdentityInfoType@odata.count": 1,
        "IdentityInfoValue": [
          "DCIM:firmware:8086:1572:1028:0000"
        ],
        "IdentityInfoValue@odata.count": 1,
        "InstallationDate": "NA",
        "IsEntity": true,
        "MajorVersion": 22,
        "MinorVersion": 0,
        "Name": "DellSoftwareInventory",
        "PLDMCapabilitiesDuringUpdate": "0x00000000",
        "PLDMFDPCapabilitiesDuringUpdate": "0x00000000",
        "RevisionNumber": 9,
        "RevisionString": null,
        "SidebandUpdateCapable": false,
        "Status": "AvailableForInstallation",
        "SubDeviceID": "0000",
        "SubVendorID": "1028",
        "VendorID": "8086",
        "impactsTPMmeasurements": true
      }
    }
  },
  "ReleaseDate": "2023-03-03T00:00:00Z",
  "SoftwareId": "102303",
  "Status": {
    "Health": "OK",
    "State": "Enabled"
  },
  "Updateable": true,
  "Version": "22.0.9"
}
```


     * `Updateable`: Indicates the value the parameter is set to. 

  4. Where the `Updateable` parameter is set to `true`, you can use Redfish to update the network adapter. 



## 4.10.20. About the HostUpdatePolicy resource

You can use the `HostUpdatePolicy` resource to enable or disable applying live updates to the firmware settings, BMC settings, or firmware settings of each bare-metal host. By default, the Operator disables live updates to already provisioned bare-metal hosts by default. 

The `HostUpdatePolicy` spec
     The `spec` section of the `HostUpdatePolicy` resource provides two settings: 
`firmwareSettings`
     This setting corresponds to the `HostFirmwareSettings` resource. 
`firmwareUpdates`
     This setting corresponds to the `HostFirmwareComponents` resource. 

When you set the value to `onPreparing`, you can only update the host during provisioning, which is the default setting. When you set the value to `onReboot`, you can update a provisioned host by applying the resource and rebooting the bare-metal host. Then, follow the procedure for editing the `HostFirmwareSettings` or `HostFirmwareComponents` resource. 

**Example`HostUpdatePolicy` resource**

```yaml
apiVersion: metal3.io/v1alpha1
kind: HostUpdatePolicy
metadata:
  name: <hostname>
  namespace: openshift-machine-api
spec:
  firmwareSettings: <setting>
  firmwareUpdates: <setting>
```


where: 

`<hostname>`
     Specifies the name of the bare-metal host. 
`spec.firmwareSettings`
     Specifies the update policy setting. Specify `onPreparing` to disable live updates. Specify `onReboot` to enable live updates. 

## 4.10.21. Setting the HostUpdatePolicy resource

By default, the `HostUpdatePolicy` disables live updates. To enable live updates, create the `HostUpdatePolicy` resource. 

Warning

Performing a live update to the `HostUpdatePolicy` resource can be a destructive and destabilizing action. Perform these updates only after careful consideration. 

Before you apply a live update in a production cluster, validate the update in a development or test cluster. Ensure that these updates comply with your organization’s test policies before you apply them to a production cluster. 

If a cluster has fewer than three compute nodes, use caution. Firmware updates in such clusters can result in the cluster entering a degraded state. 

Do not interrupt firmware updates. If the update stops responding, engage the support of your hardware vendor. 

**Procedure**

  1. Create the `HostUpdatePolicy` resource by running the following command: 

```shell-session
$ vim hup.yaml
```


You can use any text editor you prefer. 

**Example`HostUpdatePolicy` resource:**

```yaml
apiVersion: metal3.io/v1alpha1
kind: HostUpdatePolicy
metadata:
  name: <hostname>
  namespace: openshift-machine-api
spec:
  firmwareSettings: onReboot
  firmwareUpdates: onReboot
```


Replace `<hostname>` with the name of the host. 

  2. Save the changes to the `hup.yaml` file. 
  3. Apply the policy by running the following command: 

```shell-session
$ oc apply -f hup.yaml
```
