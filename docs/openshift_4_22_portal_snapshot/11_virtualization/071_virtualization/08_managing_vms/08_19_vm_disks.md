# 8.19. VM disks

## 8.19.1. Hot-plug virtual disks to running VMs

You can hot-plug or hot-unplug virtual disks from running VMs to dynamically adjust storage without downtime. 

Only data volumes and persistent volume claims (PVCs) can be hot plugged and hot-unplugged. You cannot hot plug or hot-unplug container disks. 

A hot plugged disk remains attached to the VM even after reboot. You must unplug the disk to remove it from the VM. 

Note

Each VM has a `virtio-scsi` controller so that hot plugged disks can use the SCSI bus. The `virtio-scsi` controller overcomes the limitations of VirtIO while retaining its performance advantages. It is highly scalable and supports hot plugging over 4 million disks. 

When you hot plug disks to the VirtIO (`virtio-blk`) bus, each disk uses a PCI Express (PCIe) slot in the VM. The number of PCIe slots is limited and pre-set automatically at the VM creation as specified in the "Available VirtIO Ports" table. Therefore, you can use `virtio-blk` for a small number of disks that does not exceed the number of available slots. 

### 8.19.1.1. Hot plug and unplug disks by using the web console

You can hot plug a disk by attaching it to a virtual machine (VM) while the VM is running by using the OpenShift Container Platform web console. 

The hot plugged disk remains attached to the VM until you unplug it. 

**Prerequisites**

  * You must have a data volume or persistent volume claim (PVC) available for hot plugging. 



**Procedure**

  1. Navigate to **Virtualization** **VirtualMachines** in the web console. 
  2. Select a running VM to view its details. 
  3. On the **VirtualMachine details** page, click **Configuration** **Storage**. 
  4. Add a hot plugged disk: 

     1. Click **Add**. 
     2. In the **Add disk (hot plugged)** window, select the disk from the **Source** list and click **Save**. 

  5. Optional: Select the type of the interface bus. The options are **VirtIO** and **SCSI**. The default bus type is **VirtIO**. 
  6. Optional: Change the type of the interface bus of an existing hot plugged disk: 

     1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) beside the disk and select the **Edit** option. 
     2. In the **Interface** field, select the desired option. 

  7. Optional: Unplug a hot plugged disk: 

     1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) beside the disk and select **Detach**. 
     2. Click **Detach**. 




### 8.19.1.2. Hot plug and hot unplug a disk by using the CLI

You can hot plug and hot unplug a disk while a virtual machine (VM) is running by using the command line. 

The hot plugged disk remains attached to the VM until you unplug it. 

**Prerequisites**

  * You must have at least one data volume or persistent volume claim (PVC) available for hot plugging. 



**Procedure**

  * Hot plug a disk by running the following command: 

```shell-session
$ virtctl addvolume <virtual-machine|virtual-machine-instance> \
  --volume-name=<datavolume|PVC> \
  [--bus <bus_type>] [--persist] [--serial=<label_name>]
```


where: 

`--bus <bus_type>`
     Optional: Specifies the bus type of the added disk. Supported values are `virtio` and `scsi`. The default bus type is `virtio`. 
`--persist`
     Optional: Specifies that the virtual disk is permanently mounted on a virtual machine. This flag does not apply to virtual machine instances. 
`--serial=<label_name>`
     Optional: Specifies an alphanumeric string label of your choice to identify the hot plugged disk in a guest virtual machine. If you do not specify this option, the label defaults to the name of the hot plugged data volume or PVC. 

  * Hot unplug a disk by running the following command: 

```shell-session
$ virtctl removevolume <virtual-machine|virtual-machine-instance> \
  --volume-name=<datavolume|PVC>
```


### 8.19.1.3. Additional resources

  * [Available VirtIO Ports](https://kubevirt.io/user-guide/storage/hotplug_volumes/#available-virtio-ports)



## 8.19.2. Expand virtual machine disks

Expand the persistent volume claim (PVC) of your virtual machine disk to accommodate growing data requirements. If your storage provider does not support volume expansion, you can expand the available virtual storage of a VM by adding blank data volumes. 

You cannot reduce the size of a VM disk. 

### 8.19.2.1. Expand a VM disk PVC by using the web console

You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk. To specify the increased PVC volume, you can use the **VirtualMachines** page in the web console, with the VM running. 

Note

If the PVC uses the file system volume mode, the disk image file expands to the available size while reserving some space for file system overhead. 

**Procedure**

  1. In the **Administrator** or **Virtualization** perspective, open the **VirtualMachines** page. 
  2. Select the running VM to open its **Details** page. 
  3. Select the **Configuration** tab and click **Storage**. 
  4. Click the options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the disk you want to expand. Select the **Edit** option. 

The **Edit disk** dialog opens. 

  5. In the **PersistentVolumeClaim size** field, enter the desired size. 

Note

You can enter any value greater than the current one. However, if the new value exceeds the available size, an error is displayed. 

  6. Click **Save**. 



### 8.19.2.2. Expand a VM disk PVC by using the CLI

You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk. To specify the increased PVC volume, you can edit the `PersistentVolumeClaim` manifest by using the OpenShift CLI (`oc`). 

Note

If the PVC uses the file system volume mode, the disk image file expands to the available size while reserving some space for file system overhead. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Edit the `PersistentVolumeClaim` manifest of the VM disk that you want to expand: 

```shell-session
$ oc edit pvc <pvc_name>
```


  2. Update the disk size: 

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
   name: vm-disk-expand
spec:
  accessModes:
     - ReadWriteMany
  resources:
    requests:
       storage: 3Gi
# ...
```


     * `spec.resources.requests.storage` specifies the new disk size. 




### 8.19.2.3. Expand VM storage by adding blank data volumes

You can expand the available storage of a virtual machine (VM) by adding blank data volumes. 

**Prerequisites**

  * You must have at least one persistent volume. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `DataVolume` manifest as shown in the following example: 

```yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: blank-image-datavolume
spec:
  source:
    blank: {}
  storage:
    resources:
      requests:
        storage: <2Gi>
  storageClassName: "<storage_class>"
```


     * `spec.storage.resources.requests.storage` specifies the amount of available space requested for the data volume. 
     * `spec.storageClassName` is an optional field that specifies a storage class. If you do not specify a storage class, the default storage class is used. 

  2. Create the data volume by running the following command: 

```shell-session
$ oc create -f <blank-image-datavolume>.yaml
```


### 8.19.2.4. Additional resources

  * [Extending a basic volume in Windows](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/extend-a-basic-volume)
  * [Extending an existing file system partition without destroying data in Red Hat Enterprise Linux](https://access.redhat.com/solutions/29095)
  * [Extending a logical volume and its file system online in Red Hat Enterprise Linux](https://access.redhat.com/solutions/24770)
  * [Configuring preallocation mode for data volumes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/storage#virt-using-preallocation-for-datavolumes "10.10. Using preallocation for data volumes")
  * [Managing data volume annotations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/storage#virt-managing-data-volume-annotations "10.11. Managing data volume annotations")



## 8.19.3. Configure shared volumes for virtual machines

Enable high-availability scenarios like Windows Failover Clustering by configuring shared disks to allow multiple virtual machines to access the same storage volume. A shared disk’s volume must be block mode. 

You configure disk sharing by exposing the storage as either of these types: 

  * An ordinary VM disk 
  * A logical unit number (LUN) disk with an SCSI connection and raw device mapping, as required for Windows Failover Clustering for shared volumes 



In addition to configuring disk sharing, you can also set an error policy for each ordinary VM disk or LUN disk. The error policy controls how the hypervisor behaves when an input/output error occurs on a disk Read or Write. 

### 8.19.3.1. Share a block disk between multiple VMs

You can configure block volumes so that multiple virtual machines (VMs) can share storage. 

The application running on the guest operating system determines the storage option you must configure for the VM. A disk of type `disk` exposes the volume as an ordinary disk to the VM. 

You can set an error policy for each disk. The error policy controls how the hypervisor behaves when an input/output error occurs while a disk is being written to or read. The default behavior stops the VM and generates a Kubernetes event. 

You can accept the default behavior, or you can set the error policy to one of the following options: 

  * `report`, which reports the error in the guest. 
  * `ignore`, which ignores the error. The Read or Write failure is undetected. 
  * `enospace`, which produces an error indicating that there is not enough disk space. 



**Prerequisites**

  * The volume access mode must be `ReadWriteMany` (RWX) if the VMs that are sharing disks are running on different nodes. 

If the VMs that are sharing disks are running on the same node, `ReadWriteOnce` (RWO) volume access mode is sufficient. 

Note

Not all filesystem and format combinations support RWX mode. For example, XFS format does not support RWX mode. When multiple VMs write to an XFS-formatted volume, data corruption occurs and only the writing VM can access the data. 

  * The storage provider must support the required Container Storage Interface (CSI) driver. 



**Procedure**

  1. Create the `VirtualMachine` manifest for your VM to set the required values, as shown in the following example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: <vm_name>
spec:
  template:
# ...
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
            errorPolicy: report
          - disk:
              bus: virtio
            name: cluster
            shareable: true
          interfaces:
          - masquerade: {}
            name: default
```


     * `spec.template.spec.domain.devices.disks.errorPolicy` defines how the hypervisor should behave when an IO error occurs. 
     * `spec.template.spec.domain.devices.disks.shareable` defines whether multiple virtual machines (VMs) can use the same underlying disk. 

  2. Save the `VirtualMachine` manifest file to apply your changes. 



### 8.19.3.2. Share a LUN-backed disk between multiple VMs

To secure data on your VM from outside access, you can enable SCSI persistent reservation and configure a LUN-backed virtual machine disk to be shared among multiple virtual machines. 

By enabling the shared option, you can use advanced SCSI commands, such as those required for a Windows failover clustering implementation, for managing the underlying storage. 

When a storage volume is configured as the `LUN` disk type, a VM can use the volume as a logical unit number (LUN) device. As a result, the VM can deploy and manage the disk by using SCSI commands. 

You reserve a LUN through the SCSI persistent reserve options. To enable the reservation: 

  1. Configure the feature gate option 
  2. Activate the feature gate option on the LUN disk to issue SCSI device-specific input and output controls (IOCTLs) that the VM requires. 



You can set an error policy for each LUN disk. The error policy controls how the hypervisor behaves when an input/output error occurs on a disk Read or Write. The default behavior stops the guest and generates a Kubernetes event. 

For a LUN disk with an SCSi connection and a persistent reservation, as required for Windows Failover Clustering for shared volumes, you set the error policy to `report`. 

**Prerequisites**

  * You must have cluster administrator privileges to configure the feature gate option. 
  * The volume access mode must be `ReadWriteMany` (RWX) if the VMs that are sharing disks are running on different nodes. 

If the VMs that are sharing disks are running on the same node, `ReadWriteOnce` (RWO) volume access mode is sufficient. 

  * The storage provider must support a Container Storage Interface (CSI) driver that uses Fibre Channel (FC), Fibre Channel over Ethernet (FCoE), or iSCSI storage protocols. 
  * If you are a cluster administrator and intend to configure disk sharing by using LUN, you must enable the cluster’s feature gate on the `HyperConverged` custom resource (CR). 
  * Disks that you want to share must be in block mode. 



**Procedure**

  1. Edit or create the `VirtualMachine` manifest for your VM to set the required values, as shown in the following example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-0
spec:
  template:
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: sata
            name: rootdisk
          - errorPolicy: report
            lun:
              bus: scsi
              reservation: true
            name: na-shared
            serial: shared1234
      volumes:
      - dataVolume:
          name: vm-0
        name: rootdisk
      - name: na-shared
        persistentVolumeClaim:
          claimName: pvc-na-share
```


     * `spec.template.spec.domain.devices.disks.errorPolicy` defines how the hypervisor should behave when an IO error occurs. 
     * `spec.template.spec.domain.devices.disks.lun` defines a volume exposed as a LUN device. 
     * `spec.template.spec.domain.devices.disks.lun.reservation` defines whether the persistent reservation is enabled. 
     * `spec.template.spec.domain.devices.disks.serial` specifies an alphanumeric serial number for the disk. The serial number is visible to the guest operating system and can be used to identify the disk inside the VM. 

  2. Save the `VirtualMachine` manifest file to apply your changes. 



#### 8.19.3.2.1. Share a LUN-backed disk by using the web console

You can use the OpenShift Container Platform web console to configure disk sharing by using LUN. 

**Prerequisites**

  * The cluster administrator must enable the `persistentreservation` feature gate setting. 



**Procedure**

  1. Click **Virtualization** **VirtualMachines** in the web console. 
  2. Select a VM to open the **VirtualMachine details** page. 
  3. Expand **Storage**. 
  4. On the **Disks** tab, click **Add disk**. 
  5. Specify the **Name** , **Source** , **Size** , **Interface** , and **Storage Class**. 
  6. Select **LUN** as the **Type**. 
  7. Select **Shared access (RWX)** as the **Access Mode**. 
  8. Select **Block** as the **Volume Mode**. 
  9. Expand **Advanced Settings** , and select both checkboxes. 
  10. Click **Save**. 



#### 8.19.3.2.2. Share a LUN-backed disk by using the CLI

You can use the command line to configure disk sharing by using LUN. 

**Procedure**

  1. Edit or create the `VirtualMachine` manifest for your VM to set the required values, as shown in the following example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-0
spec:
  template:
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: sata
            name: rootdisk
          - errorPolicy: report
            lun:
              bus: scsi
              reservation: true
            name: na-shared
            serial: shared1234
      volumes:
      - dataVolume:
          name: vm-0
        name: rootdisk
      - name: na-shared
        persistentVolumeClaim:
          claimName: pvc-na-share
```


     * `spec.template.spec.domain.devices.disks.errorPolicy` defines how the hypervisor should behave when an IO error occurs. 
     * `spec.template.spec.domain.devices.disks.lun` defines a volume exposed as a LUN device. 
     * `spec.template.spec.domain.devices.disks.lun.reservation` defines whether the persistent reservation is enabled. 
     * `spec.template.spec.domain.devices.disks.serial` specifies an alphanumeric serial number for the disk. The serial number is visible to the guest operating system and can be used to identify the disk inside the VM. 

  2. Save the `VirtualMachine` manifest file to apply your changes. 



### 8.19.3.3. SCSI persistent reservation for shared LUN disks

You can enable the SCSI `persistentReservation` feature gate and allow a LUN-backed block mode virtual machine (VM) disk to be shared among multiple virtual machines. 

The `persistentReservation` feature gate is disabled by default. You can enable the `persistentReservation` feature gate by using the web console or the command line. 

#### 8.19.3.3.1. Prerequisites

  * Cluster administrator privileges are required. 
  * The volume access mode `ReadWriteMany` (RWX) is required if the VMs that are sharing disks are running on different nodes. If the VMs that are sharing disks are running on the same node, the `ReadWriteOnce` (RWO) volume access mode is sufficient. 
  * The storage provider must support a Container Storage Interface (CSI) driver that uses Fibre Channel (FC), Fibre Channel over Ethernet (FCoE), or iSCSI storage protocols. 



#### 8.19.3.3.2. Enable SCSI persistent reservation by using the web console

You must enable the PersistentReservation feature gate to allow a LUN-backed block mode virtual machine (VM) disk to be shared among multiple virtual machines. Enabling the feature gate requires cluster administrator privileges. 

**Procedure**

  1. Click **Virtualization** **Settings** in the web console. 
  2. Select **Cluster**. 
  3. Expand **SCSI persistent reservation** and set **Enable persistent reservation** to on. 



#### 8.19.3.3.3. Enabling the PersistentReservation feature gate by using the CLI

You can enable the `persistentReservation` feature gate by using the command line. Enabling the feature gate requires cluster administrator privileges. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Enable the `persistentReservation` feature gate by running the following command: 

```shell-session
$ oc patch hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv --type json -p \
'[{"op":"replace","path":"/spec/featureGates/persistentReservation", "value": true}]'
```


### 8.19.3.4. Additional resources

  * [Persistent reservation helper protocol](https://www.qemu.org/docs/master/interop/pr-helper.html)
  * [Failover Clustering in Windows Server and Azure Stack HCI](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview)



## 8.19.4. Migrate a VM disk to a different storage class

You can migrate one or more virtual disks to a different storage class to optimize storage performance or reduce costs without stopping your virtual machine (VM) or virtual machine instance (VMI). 

### 8.19.4.1. Storage class migration

A persistent volume claim (PVC) requests storage with specific attributes, such as size and performance, defined by its storage class. You cannot change a PVC’s storage class after you create it. 

The storage backend that provisioned the original PVC holds the VM’s data. The target storage class might use a different backend, which does not have that data until you migrate it there. 

To move a VM disk to a new storage class, you create a migration plan. The migration plan creates a new PVC in the target storage class and copies the data from the original PVC to the new PVC. 

### 8.19.4.2. Assign storage migration permissions

Cluster administrators must grant users permission to perform storage migrations. Permissions to perform storage migrations are not part of the administrative or editing roles in the cluster by default. 

**Prerequisites**

  * You have cluster administrator privileges. 



**Procedure**

  1. (Optional) To assign the user single namespace storage migration permissions, run the following command: 

```shell-session
$ kubectl create rolebinding <role_binding_name> \
    --clusterrole=migrations.kubevirt.io:storagemigrate \
    --user=<user_name> -n <namespace>
```


where: 

<role_binding_name>
     The name to assign to this role binding instance. 
<user_name>
     The user to assign the storage migration permission. 
<namespace>
     The applicable namespace for this role binding instance. 

  2. (Optional) To assign the user multiple namespace storage migration permissions, run the following command: 

```shell-session
$ kubectl create clusterrolebinding <role_binding_name> \
    --clusterrole=migrations.kubevirt.io:storagemigrate-multins \
    --user=<user_name>
```


where: 

<role_binding_name>
     The name to assign to this role binding instance. 
<user_name>
     The user to assign the storage migration permission. 




### 8.19.4.3. Migrate VM disks to another storage class in the web console

You can migrate one or more disks attached to a virtual machine (VM) to a different storage class by using the OpenShift Container Platform web console. When performing this action on a running VM, the operation of the VM is not interrupted and the data on the migrated disks remains accessible. 

**Prerequisites**

  * You must have a data volume or a persistent volume claim (PVC) available for storage class migration. 
  * The cluster must have a node available for live migration. As part of the storage class migration, the VM is live migrated to a different node. 
  * The VM must be running. 



**Procedure**

  1. Navigate to **Virtualization** **VirtualMachines** in the web console. 
  2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) beside the virtual machine and select **Migration** **Storage**. 

You can also access this option from the **VirtualMachine details** page by selecting **Actions** **Migration** **Storage**. 

Alternatively, right-click the VM in the tree view and select **Migration** from the menu. 

  3. On the **Migration details** page, choose whether to migrate the entire VM storage or selected volumes only. If you click **Selected volumes** , select any disks that you intend to migrate. Click **Next** to proceed. 
  4. From the list of available options on the **Destination StorageClass** page, select the storage class to migrate to. Click **Next** to proceed. 
  5. On the **Review** page, review the list of affected disks and the target storage class. To start the migration, click **Migrate VirtualMachine storage**. 
  6. Stay on the **Migrate VirtualMachine storage** page to watch the progress and wait for the confirmation that the migration completed successfully. 



**Verification**

  1. From the **VirtualMachine details** page, navigate to **Configuration** **Storage**. 
  2. Verify that all disks have the expected storage class listed in the **Storage class** column. 



## 8.19.5. Insert a CD-ROM ISO image into a live virtual machine

To attach a storage device to a virtual machine (VM) without rebooting the VM, you can configure a VM to use a virtual CD-ROM drive, and insert an ISO image in the drive. 

This also makes it possible to install an operating system from a CD-ROM in the VM. 

### 8.19.5.1. Insert a CD-ROM in a running VM by using the CLI

To make data on a CD-ROM storage device available to a running virtual machine (VM), create a virtual CD-ROM drive in the VM and insert the CD-ROM into the drive as an ISO image. 

Setting up a virtual CD-ROM drive requires rebooting the VM, but afterwards, you can insert and eject ISO images in the drive while the VM is running. 

**Prerequisites**

  * The `DeclarativeHotplugVolumes` feature gate is enabled. To ensure this, the `HyperConverged` CR must contain the `declarativeHotplugVolumes: true` line in the `spec.featureGates` configuration section: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
    featureGates:
      declarativeHotplugVolumes: true
```


Note

The `DeclarativeHotplugVolumes` feature gate does not support hot plugging ephemeral volumes. 

  * You have an ISO image of a CD-ROM available in the cluster. 



**Procedure**

  1. Run the following command to edit the configuration of the VM in which you want to insert the CD-ROM: 

```shell-session
$ oc edit vm <vm-name> -n <namespace>
```


where: 

     * `<vm-name>` is the name of the VM 
     * `<namespace>` is the name of the project name space that contains the VM 

  2. Add a `cdrom` disk to the `spec.template.spec.domains.devices.disks` section of the VM configuration. For example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  runStrategy: Always
  template:
    spec:
      domain:
        devices:
          disks:
          - cdrom:
              bus: sata
              name: cdrom
```


  3. If the VM is running, shut it down. 
  4. Insert a CD-ROM volume in the `spec.template.spec.volumes` section of the VM configuration. For example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  template:
    spec:
      volumes:
      - dataVolume:
          name: cdrom-example
          hotpluggable: true
        name: cdrom
```


You can insert a CD-ROM this way while the VM is running, but the dataVolume must have the `hotpluggable: true` parameter set. 

  5. Optional: In the guest operating system, verify that the CD-ROM has been detected. 
  6. Optional: Eject the CD-ROM volume. To do so, remove the `cdrom` volume from the `spec.template.spec.volumes` section of the VM configuration. You can do this while the VM is running. 



### 8.19.5.2. Insert a CD-ROM into a running VM from the web console

To make data on a CD-ROM storage device available to a running virtual machine (VM), create a virtual CD-ROM drive in the VM and insert the CD-ROM into the drive as an ISO image. 

Setting up a virtual CD-ROM drive requires rebooting the VM, but you can insert and eject ISO images in the drive while the VM is running. 

**Prerequisites**

  * The `DeclarativeHotplugVolumes` feature gate is enabled. To ensure this, the `HyperConverged` CR must contain the `declarativeHotplugVolumes: true` line in the `spec.featureGates` configuration section: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
    featureGates:
      declarativeHotplugVolumes: true
```


Note

The `DeclarativeHotplugVolumes` feature gate does not support hot plugging ephemeral volumes. 




**Procedure**

  1. In the OpenShift Container Platform web console, go to **Virtualization** **VirtualMachines**. 
  2. Click the name of the VM in which you want to insert the CD-ROM. 
  3. On the VM details page, click the **Configuration** tab. 
  4. Open the **Storage** pane. 
  5. Click **Add**. 

A drop-down menu opens. 

  6. Click **CD-ROM**. 
  7. In the **Name** field, add a name for the CD-ROM drive device. 
  8. Select the ISO image to add to the drive as a CD-ROM volume. To do so, click the drop-down button, and select from the volumes available in the cluster. 

Alternatively, you can upload a new ISO file and insert it into the CD-ROM drive after it is created. To do so: 

     1. Ensure that the **Upload a new ISO file to the cluster** line is checked. 
     2. Drag and drop an ISO file in the **Upload ISO** field, or click **Upload** and select the ISO image that you want to upload. 
     3. In the **Upload mode** field, select **Mount uploaded ISO as DataVolume**. 

  9. Click **Add**. 

The CD-ROM drive is added to the **Storage** list. 

  10. If the VM is running, shut it down or restart it. 
  11. To insert the ISO file attached to the CD-ROM drive as a CD-ROM volume into the VM, click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the CD-ROM drive, and click **Inject**. You can do this while the VM is running. 
  12. Optional: In the guest operating system, verify that the CD-ROM has been detected. 
  13. Optional: To eject the CD-ROM from the VM, click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the CD-ROM device in the web console, and select **Eject**. You can do this while the VM is running.
