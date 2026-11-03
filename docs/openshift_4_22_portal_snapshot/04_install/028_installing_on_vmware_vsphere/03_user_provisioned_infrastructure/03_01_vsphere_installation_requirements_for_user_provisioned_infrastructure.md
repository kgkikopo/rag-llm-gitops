# 3.1. vSphere installation requirements for user-provisioned infrastructure

Before you begin an installation on infrastructure that you provision, be sure that your vSphere environment meets the following installation requirements. 

## 3.1.1. VMware vSphere infrastructure requirements

You must install an OpenShift Container Platform cluster on one of the following versions of a VMware vSphere instance that meets the requirements for the components that you use: 

  * Version 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later 
  * VMware vSphere Foundation 9 or later, or VMware Cloud Foundation 9 or later 



Both of these releases support Container Storage Interface (CSI) migration, which is enabled by default on OpenShift Container Platform 4.22. 

Note

Red Hat follows Broadcom’s End of Support dates for VMware products that OpenShift Container Platform runs on. After a VMware product version reaches End of Support, that version is no longer supported for use with OpenShift Container Platform. 

You can host the VMware vSphere infrastructure on-premise or on a [VMware Cloud Verified provider](https://cloud.vmware.com/providers) that meets the requirements outlined in the following tables: 

Table 3.1. Version requirements for vSphere virtual environmentsVirtual environment product| Required version  
---|---  
VMware virtual hardware  |  15 or later   
vSphere ESXi hosts  |  8.0 Update 1 or later, or VMware vSphere Foundation 9 or later; VMware Cloud Foundation 5.0 or later, or VMware Cloud Foundation 9 or later   
vCenter host  |  8.0 Update 1 or later, or VMware vSphere Foundation 9 or later; VMware Cloud Foundation 5.0 or later, or VMware Cloud Foundation 9 or later   
Show more

Important

You must ensure that the time on your ESXi hosts is synchronized before you install OpenShift Container Platform. See [Editing the Time Configuration Settings of Your ESXi Host (Broadcom documentation)](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/host-configuration-host-management/synchronizing-clocks-on-the-vsphere-network-host-management/editing-time-configuration-for-a-host-host-management.html). 

Table 3.2. Minimum supported vSphere version for VMware componentsComponent| Minimum supported versions| Description  
---|---|---  
Hypervisor  |  vSphere 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later with virtual hardware version 15; VMware vSphere Foundation 9 or later, or VMware Cloud Foundation 9 or later  |  This hypervisor version is the minimum version that Red Hat Enterprise Linux CoreOS (RHCOS) supports. For more information about supported hardware on the latest version of Red Hat Enterprise Linux (RHEL) that is compatible with RHCOS, see [Hardware](https://catalog.redhat.com/hardware/search) on the Red Hat Customer Portal.   
Networking (NSX)  |  vSphere 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later; VMware vSphere Foundation 9 or later, or VMware Cloud Foundation 9 or later  |  Red Hat uses the Partner Certification process to verify NSX compatibility.   
CPU micro-architecture  |  x86-64-v2 or higher  |  OpenShift Container Platform version 4.13 and later are based on the RHEL 9.2 host operating system, which raised the microarchitecture requirements to x86-64-v2. See [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures) in the RHEL documentation.   
Show more

Important

To ensure the best performance conditions for your cluster workloads that operate on Oracle® Cloud Infrastructure (OCI) and on the Oracle® Cloud VMware Solution (OCVS) service, ensure volume performance units (VPUs) for your block volume are sized for your workloads. 

The following list provides some guidance in selecting the VPUs needed for specific performance needs: 

  * Test or proof of concept environment: 100 GB, and 20 to 30 VPUs. 
  * Base-production environment: 500 GB, and 60 VPUs. 
  * Heavy-use production environment: More than 500 GB, and 100 or more VPUs. 



Consider allocating additional VPUs to give enough capacity for updates and scaling activities. See [Block Volume Performance Levels (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm). 

Note

The following additional VMware vSphere Foundation and VMware Cloud Foundation components are outside the scope of Red Hat support: 

  * Management: VCF Operations, VCF Automation, VCF Fleet Management, and VCF Identity Broker. 
  * Networking: VMware NSX Container Plugin (NCP). 
  * Migration: VMware HCX. 



## 3.1.2. VMware vSphere CSI Driver Operator requirements

To successfully install and operate the vSphere CSI Driver Operator, verify that your environment meets the minimum VMware vSphere, vCenter, and virtual machine version requirements. 

To install the vSphere Container Storage Interface (CSI) Driver Operator, the following requirements must be met: 

  * VMware vSphere version 8.0 Update 1 or later; or VMware vSphere Foundation (VVF) 9; or VMware Cloud Foundation (VCF) 5 or later 
  * vCenter version 8.0 Update 1 or later; or VVF 9; or VCF 5 or later 
  * Virtual machines of hardware version 15 or later 
  * No third-party vSphere CSI driver already installed in the cluster 



If a third-party vSphere CSI driver is present in the cluster, OpenShift Container Platform does not overwrite it. The presence of a third-party vSphere CSI driver prevents OpenShift Container Platform from updating to OpenShift Container Platform 4.13 or later. 

Note

The VMware vSphere CSI Driver Operator is supported only on clusters deployed with `platform: vsphere` in the installation manifest. 

You can create a custom role for the Container Storage Interface (CSI) driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator. The custom role can include privilege sets that assign a minimum set of permissions to each vSphere object. This means that the CSI driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator can establish a basic interaction with these objects. 

Important

Installing an OpenShift Container Platform cluster in a vCenter is tested against a full list of privileges as described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected and unsupported behaviors that might occur when creating a custom role with a set of restricted privileges. 

To remove a third-party CSI driver, see "Removing a third-party vSphere CSI Driver". 

**Additional resources**

  * [Removing a third-party vSphere CSI Driver](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-vsphere-install-issues_persistent-storage-csi-vsphere)
  * [Updating hardware on nodes running in vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-hardware-on-nodes-running-on-vsphere)
  * [Minimum permissions for the storage components](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_vmware_vsphere/user-provisioned-infrastructure#installation-vsphere-minimum-permissions-storage_upi-vsphere-installation-reqs "Table 3.7. Minimum permissions for the storage components")



## 3.1.3. Requirements for a cluster with user-provisioned infrastructure

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines. 

### 3.1.3.1. vCenter requirements

Before you install an OpenShift Container Platform cluster on your vCenter that uses infrastructure that you provided, you must prepare your environment. 

#### 3.1.3.1.1. Required vCenter account privileges

To install an OpenShift Container Platform cluster in a vCenter, your vSphere account must include privileges for reading and creating the required resources. Using an account that has global administrative privileges is the simplest way to access all of the necessary permissions. 

Note

The following tables do not explicitly list the ESXi host object. In the vSphere hierarchy, ESXi hosts are child objects of the cluster. If you apply your custom role to the vSphere vCenter Cluster object with the "Propagate to children" setting enabled, the required privileges automatically propagate down to the ESXi hosts. You do not need to apply permissions directly to individual ESXi host objects. 

Table 3.3. Roles and privileges required for installation in vSphere APIvSphere object for role| When required| Required privileges in vSphere API  
---|---|---  
vSphere vCenter  |  Always  | 

  * `Cns.Searchable`
  * `InventoryService.Tagging.AttachTag`
  * `InventoryService.Tagging.CreateCategory`
  * `InventoryService.Tagging.CreateTag`
  * `InventoryService.Tagging.DeleteCategory`
  * `InventoryService.Tagging.DeleteTag`
  * `InventoryService.Tagging.EditCategory`
  * `InventoryService.Tagging.EditTag`
  * `Sessions.ValidateSession`
  * `StorageProfile.Update`
  * `StorageProfile.View`

  
vSphere vCenter Cluster  |  Always  | 

  * `Host.Config.Storage`
  * `Resource.AssignVMToPool`
  * `VApp.AssignResourcePool`
  * `VApp.Import`
  * `VirtualMachine.Config.AddNewDisk`

  
vSphere vCenter Resource Pool  |  For a provided existing resource pool  | 

  * `Resource.AssignVMToPool`
  * `VApp.AssignResourcePool`
  * `VApp.Import`
  * `VirtualMachine.Config.AddNewDisk`

  
vSphere Datastore  |  Always  | 

  * `Datastore.AllocateSpace`
  * `Datastore.Browse`
  * `Datastore.FileManagement`
  * `InventoryService.Tagging.ObjectAttachable`

  
vSphere Port Group  |  Always  |  `Network.Assign`  
Virtual Machine Folder  |  Always  | 

  * `InventoryService.Tagging.ObjectAttachable`
  * `Resource.AssignVMToPool`
  * `VApp.Import`
  * `VirtualMachine.Config.AddExistingDisk`
  * `VirtualMachine.Config.AddNewDisk`
  * `VirtualMachine.Config.AddRemoveDevice`
  * `VirtualMachine.Config.AdvancedConfig`
  * `VirtualMachine.Config.Annotation`
  * `VirtualMachine.Config.CPUCount`
  * `VirtualMachine.Config.DiskExtend`
  * `VirtualMachine.Config.DiskLease`
  * `VirtualMachine.Config.EditDevice`
  * `VirtualMachine.Config.Memory`
  * `VirtualMachine.Config.RemoveDisk`
  * `VirtualMachine.Config.Rename`
  * `Host.Config.Storage`
  * `VirtualMachine.Config.ResetGuestInfo`
  * `VirtualMachine.Config.Resource`
  * `VirtualMachine.Config.Settings`
  * `VirtualMachine.Config.UpgradeVirtualHardware`
  * `VirtualMachine.Interact.GuestControl`
  * `VirtualMachine.Interact.PowerOff`
  * `VirtualMachine.Interact.PowerOn`
  * `VirtualMachine.Interact.Reset`
  * `VirtualMachine.Inventory.Create`
  * `VirtualMachine.Inventory.CreateFromExisting`
  * `VirtualMachine.Inventory.Delete`
  * `VirtualMachine.Provisioning.Clone`
  * `VirtualMachine.Provisioning.MarkAsTemplate`
  * `VirtualMachine.Provisioning.DeployTemplate`

  
vSphere vCenter data center  |  `VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API. See the "Minimum permissions for the Machine API" table.  | 

  * `InventoryService.Tagging.ObjectAttachable`
  * `Resource.AssignVMToPool`
  * `VirtualMachine.Config.AddExistingDisk`
  * `VirtualMachine.Config.AddNewDisk`
  * `VirtualMachine.Config.AddRemoveDevice`
  * `VirtualMachine.Config.AdvancedConfig`
  * `VirtualMachine.Config.Annotation`
  * `VirtualMachine.Config.CPUCount`
  * `VirtualMachine.Config.DiskExtend`
  * `VirtualMachine.Config.DiskLease`
  * `VirtualMachine.Config.EditDevice`
  * `VirtualMachine.Config.Memory`
  * `VirtualMachine.Config.RemoveDisk`
  * `VirtualMachine.Config.Rename`
  * `VirtualMachine.Config.ResetGuestInfo`
  * `VirtualMachine.Config.Resource`
  * `VirtualMachine.Config.Settings`
  * `VirtualMachine.Config.UpgradeVirtualHardware`
  * `VirtualMachine.Interact.GuestControl`
  * `VirtualMachine.Interact.PowerOff`
  * `VirtualMachine.Interact.PowerOn`
  * `VirtualMachine.Interact.Reset`
  * `VirtualMachine.Inventory.Create`
  * `VirtualMachine.Inventory.CreateFromExisting`
  * `VirtualMachine.Inventory.Delete`
  * `VirtualMachine.Provisioning.Clone`
  * `VirtualMachine.Provisioning.DeployTemplate`
  * `VirtualMachine.Provisioning.MarkAsTemplate`
  * `Folder.Create`
  * `Folder.Delete`

  
Show more

Table 3.4. Roles and privileges required for installation in vCenter graphical user interface (GUI)vSphere object for role| When required| Required privileges in vCenter GUI  
---|---|---  
vSphere vCenter  |  Always  | 

  * `Cns.Searchable`
  * `"vSphere Tagging"."Assign or Unassign vSphere Tag"`
  * `"vSphere Tagging"."Create vSphere Tag Category"`
  * `"vSphere Tagging"."Create vSphere Tag"`
  * `vSphere Tagging"."Delete vSphere Tag Category"`
  * `"vSphere Tagging"."Delete vSphere Tag"`
  * `"vSphere Tagging"."Edit vSphere Tag Category"`
  * `"vSphere Tagging"."Edit vSphere Tag"`
  * `Sessions."Validate session"`
  * `"VM storage policies"."Update VM storage policies"`
  * `"VM storage policies"."View VM storage policies"`

  
vSphere vCenter Cluster  |  Always  | 

  * `Host.Configuration."Storage partition configuration"`
  * `Resource."Assign virtual machine to resource pool"`
  * `VApp."Assign resource pool"`
  * `VApp.Import`
  * `"Virtual machine"."Change Configuration"."Add new disk"`

  
vSphere vCenter Resource Pool  |  If providing an existing resource pool  | 

  * `Host.Configuration."Storage partition configuration"`
  * `Resource."Assign virtual machine to resource pool"`
  * `VApp."Assign resource pool"`
  * `VApp.Import`
  * `"Virtual machine"."Change Configuration"."Add new disk"`

  
vSphere Datastore  |  Always  | 

  * `Datastore."Allocate space"`
  * `Datastore."Browse datastore"`
  * `Datastore."Low level file operations"`
  * `"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"`

  
vSphere Port Group  |  Always  |  `Network."Assign network"`  
Virtual Machine Folder  |  Always  | 

  * `"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"`
  * `Resource."Assign virtual machine to resource pool"`
  * `VApp.Import`
  * `"Virtual machine"."Change Configuration"."Add existing disk"`
  * `"Virtual machine"."Change Configuration"."Add new disk"`
  * `"Virtual machine"."Change Configuration"."Add or remove device"`
  * `"Virtual machine"."Change Configuration"."Advanced configuration"`
  * `"Virtual machine"."Change Configuration"."Set annotation"`
  * `"Virtual machine"."Change Configuration"."Change CPU count"`
  * `"Virtual machine"."Change Configuration"."Extend virtual disk"`
  * `"Virtual machine"."Change Configuration"."Acquire disk lease"`
  * `"Virtual machine"."Change Configuration"."Modify device settings"`
  * `"Virtual machine"."Change Configuration"."Change Memory"`
  * `"Virtual machine"."Change Configuration"."Remove disk"`
  * `"Virtual machine"."Change Configuration".Rename`
  * `"Virtual machine"."Change Configuration"."Reset guest information"`
  * `"Virtual machine"."Change Configuration"."Change resource"`
  * `"Virtual machine"."Change Configuration"."Change Settings"`
  * `"Virtual machine"."Change Configuration"."Upgrade virtual machine compatibility"`
  * `"Virtual machine".Interaction."Guest operating system management by VIX API"`
  * `"Virtual machine".Interaction."Power off"`
  * `"Virtual machine".Interaction."Power on"`
  * `"Virtual machine".Interaction.Reset`
  * `"Virtual machine"."Edit Inventory"."Create new"`
  * `"Virtual machine"."Edit Inventory"."Create from existing"`
  * `"Virtual machine"."Edit Inventory"."Remove"`
  * `"Virtual machine".Provisioning."Clone virtual machine"`
  * `"Virtual machine".Provisioning."Mark as template"`
  * `"Virtual machine".Provisioning."Deploy template"`

  
vSphere vCenter data center  |  `VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API.  | 

  * `"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"`
  * `Resource."Assign virtual machine to resource pool"`
  * `VApp.Import`
  * `"Virtual machine"."Change Configuration"."Add existing disk"`
  * `"Virtual machine"."Change Configuration"."Add new disk"`
  * `"Virtual machine"."Change Configuration"."Add or remove device"`
  * `"Virtual machine"."Change Configuration"."Advanced configuration"`
  * `"Virtual machine"."Change Configuration"."Set annotation"`
  * `"Virtual machine"."Change Configuration"."Change CPU count"`
  * `"Virtual machine"."Change Configuration"."Extend virtual disk"`
  * `"Virtual machine"."Change Configuration"."Acquire disk lease"`
  * `"Virtual machine"."Change Configuration"."Modify device settings"`
  * `"Virtual machine"."Change Configuration"."Change Memory"`
  * `"Virtual machine"."Change Configuration"."Remove disk"`
  * `"Virtual machine"."Change Configuration".Rename`
  * `"Virtual machine"."Change Configuration"."Reset guest information"`
  * `"Virtual machine"."Change Configuration"."Change resource"`
  * `"Virtual machine"."Change Configuration"."Change Settings"`
  * `"Virtual machine"."Change Configuration"."Upgrade virtual machine compatibility"`
  * `"Virtual machine".Interaction."Guest operating system management by VIX API"`
  * `"Virtual machine".Interaction."Power off"`
  * `"Virtual machine".Interaction."Power on"`
  * `"Virtual machine".Interaction.Reset`
  * `"Virtual machine"."Edit Inventory"."Create new"`
  * `"Virtual machine"."Edit Inventory"."Create from existing"`
  * `"Virtual machine"."Edit Inventory"."Remove"`
  * `"Virtual machine".Provisioning."Clone virtual machine"`
  * `"Virtual machine".Provisioning."Deploy template"`
  * `"Virtual machine".Provisioning."Mark as template"`
  * `Folder."Create folder"`
  * `Folder."Delete folder"`

  
Show more

Additionally, the user requires some `ReadOnly` permissions, and some of the roles require permission to propagate the permissions to child objects. These settings vary depending on whether or not you install the cluster into an existing folder. 

Table 3.5. Required permissions and propagation settingsvSphere object| When required| Propagate to children| Permissions required  
---|---|---|---  
vSphere vCenter  |  Always  |  False  |  Listed required privileges   
vSphere vCenter data center  |  Existing folder  |  False  |  `ReadOnly` permission   
vSphere vCenter Cluster  |  Always  |  True  |  Listed required privileges   
vSphere vCenter Datastore  |  Always  |  False  |  Listed required privileges   
vSphere Switch  |  Always  |  False  |  `ReadOnly` permission   
vSphere Port Group  |  Always  |  False  |  Listed required privileges   
vSphere vCenter Virtual Machine Folder  |  Existing folder  |  True  |  Listed required privileges   
vSphere vCenter Resource Pool  |  Existing resource pool  |  True  |  Listed required privileges   
Show more

For more information about creating an account with only the required privileges, see [vSphere Permissions and User Management Tasks](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-5372F580-5C23-4E9C-8A4E-EF1B4DD9033E.html) in the vSphere documentation. 

#### 3.1.3.1.2. Minimum required vCenter account privileges

After you create a custom role and assign privileges to the role, you can create permissions by selecting specific vSphere objects. You can then assign the custom role to a user or group for each object. 

Before you create permissions or request for the creation of permissions for a vSphere object, decide what minimum permissions apply to the vSphere object. By doing this task, you can ensure a basic interaction exists between a vSphere object and OpenShift Container Platform architecture. 

Important

If you create a custom role and you do not assign privileges to it, the vSphere Server by default assigns a `Read Only` role to the custom role. Note that for the cloud provider API, the custom role only needs to inherit the privileges of the `Read Only` role. 

Consider creating a custom role when an account with global administrative privileges does not meet your needs. 

Important

Red Hat does not support configuring an account without including the required privileges. Red Hat tests OpenShift Container Platform cluster installations in vCenter against the full list of privileges described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected behaviors that might occur when creating a custom role with a restricted set of privileges. You must retain the full set of privileges from the "Required vCenter account privileges" section after cluster installation. Reducing the account to only the permissions listed in the minimum permission tables in the "Minimum required vCenter account privileges" section after installation is not supported and can cause unexpected cluster behavior. The minimum permission tables are for reference only; they show which privileges apply to which OpenShift Container Platform components (such as storage or the Machine API) when you design or audit custom roles. The supported configuration is to assign the full set of privileges from the "Required vCenter account privileges" section at all times, both during and after installation. 

The following tables specify how the required vCenter account privileges provided earlier in this document are relevant to different aspects of OpenShift Container Platform architecture. 

Table 3.6. Minimum permissions for postinstallation management of componentsvSphere object for role| When required| Required privileges  
---|---|---  
vSphere vCenter  |  Always  | 

  * `Cns.Searchable`
  * `InventoryService.Tagging.AttachTag`
  * `InventoryService.Tagging.CreateCategory`
  * `InventoryService.Tagging.CreateTag`
  * `InventoryService.Tagging.DeleteCategory`
  * `InventoryService.Tagging.DeleteTag`
  * `InventoryService.Tagging.EditCategory`
  * `InventoryService.Tagging.EditTag`
  * `Sessions.ValidateSession`
  * `StorageProfile.Update`
  * `StorageProfile.View`

  
vSphere vCenter Cluster  |  If you intend to create VMs in the cluster root  | 

  * `Host.Config.Storage`
  * `Resource.AssignVMToPool`

  
vSphere vCenter Resource Pool  |  If you included an existing resource pool in the `install-config.yaml` file  |  `Host.Config.Storage`  
vSphere Datastore  |  Always  | 

  * `Datastore.AllocateSpace`
  * `Datastore.Browse`
  * `Datastore.FileManagement`
  * `InventoryService.Tagging.ObjectAttachable`

  
vSphere Port Group  |  Always  |  `Network.Assign`  
Virtual Machine Folder  |  Always  | 

  * `VirtualMachine.Config.AddExistingDisk`
  * `VirtualMachine.Config.AddRemoveDevice`
  * `VirtualMachine.Config.AdvancedConfig`
  * `VirtualMachine.Config.Annotation`
  * `VirtualMachine.Config.CPUCount`
  * `VirtualMachine.Config.DiskExtend`
  * `VirtualMachine.Config.Memory`
  * `VirtualMachine.Config.Settings`
  * `VirtualMachine.Interact.PowerOff`
  * `VirtualMachine.Interact.PowerOn`
  * `VirtualMachine.Inventory.CreateFromExisting`
  * `VirtualMachine.Inventory.Delete`
  * `VirtualMachine.Provisioning.Clone`
  * `VirtualMachine.Provisioning.DeployTemplate`

  
vSphere vCenter data center  |  `VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.  | 

  * `Resource.AssignVMToPool`
  * `VirtualMachine.Config.AddExistingDisk`
  * `VirtualMachine.Config.AddRemoveDevice`
  * `VirtualMachine.Interact.PowerOff`
  * `VirtualMachine.Interact.PowerOn`
  * `VirtualMachine.Provisioning.DeployTemplate`

  
Show more

Table 3.7. Minimum permissions for the storage componentsvSphere object for role| When required| Required privileges  
---|---|---  
vSphere vCenter  |  Always  | 

  * `Cns.Searchable`
  * `InventoryService.Tagging.CreateCategory`
  * `InventoryService.Tagging.CreateTag`
  * `InventoryService.Tagging.EditCategory`
  * `InventoryService.Tagging.EditTag`
  * `StorageProfile.Update`
  * `StorageProfile.View`

  
vSphere vCenter Cluster  |  If you intend to create VMs in the cluster root  |  `Host.Config.Storage`  
vSphere vCenter Resource Pool  |  If you included an existing resource pool in the `install-config.yaml` file  |  `Host.Config.Storage`  
vSphere Datastore  |  Always  | 

  * `Datastore.Browse`
  * `Datastore.FileManagement`
  * `InventoryService.Tagging.ObjectAttachable`

  
vSphere Port Group  |  Always  |  `Read Only`  
Virtual Machine Folder  |  Always  | 

  * `VirtualMachine.Config.AddExistingDisk`
  * `VirtualMachine.Config.AddRemoveDevice`

  
vSphere vCenter data center  |  `VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.  | 

  * `VirtualMachine.Config.AddExistingDisk`
  * `VirtualMachine.Config.AddRemoveDevice`

  
Show more

Table 3.8. Minimum permissions for the Machine APIvSphere object for role| When required| Required privileges  
---|---|---  
vSphere vCenter  |  Always  | 

  * `InventoryService.Tagging.AttachTag`
  * `InventoryService.Tagging.CreateCategory`
  * `InventoryService.Tagging.CreateTag`
  * `InventoryService.Tagging.DeleteCategory`
  * `InventoryService.Tagging.DeleteTag`
  * `InventoryService.Tagging.EditCategory`
  * `InventoryService.Tagging.EditTag`
  * `Sessions.ValidateSession`
  * `StorageProfile.Update`
  * `StorageProfile.View`

  
vSphere vCenter Cluster  |  If you intend to create VMs in the cluster root  |  `Resource.AssignVMToPool`  
vSphere vCenter Resource Pool  |  If you included an existing resource pool in the `install-config.yaml` file  |  `Read Only`  
vSphere Datastore  |  Always  | 

  * `Datastore.AllocateSpace`
  * `Datastore.Browse`

  
vSphere Port Group  |  Always  |  `Network.Assign`  
Virtual Machine Folder  |  Always  | 

  * `VirtualMachine.Config.AddRemoveDevice`
  * `VirtualMachine.Config.AdvancedConfig`
  * `VirtualMachine.Config.Annotation`
  * `VirtualMachine.Config.CPUCount`
  * `VirtualMachine.Config.DiskExtend`
  * `VirtualMachine.Config.Memory`
  * `VirtualMachine.Config.Settings`
  * `VirtualMachine.Interact.PowerOff`
  * `VirtualMachine.Interact.PowerOn`
  * `VirtualMachine.Inventory.CreateFromExisting`
  * `VirtualMachine.Inventory.Delete`
  * `VirtualMachine.Provisioning.Clone`
  * `VirtualMachine.Provisioning.DeployTemplate`

  
vSphere vCenter data center  |  `VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API.  | 

  * `Resource.AssignVMToPool`
  * `VirtualMachine.Interact.PowerOff`
  * `VirtualMachine.Interact.PowerOn`
  * `VirtualMachine.Provisioning.DeployTemplate`

  
Show more

#### 3.1.3.1.3. Using OpenShift Container Platform with vMotion

If you intend on using vMotion in your vSphere environment, consider the following before installing an OpenShift Container Platform cluster. 

  * Using Storage vMotion can cause issues and is not supported. 
  * Using VMware compute vMotion to migrate the workloads for both OpenShift Container Platform compute machines and control plane machines is generally supported, where _generally_ implies that you meet all VMware best practices for vMotion. 

To help ensure the uptime of your compute and control plane nodes, ensure that you follow the VMware best practices for vMotion, and use VMware anti-affinity rules to improve the availability of OpenShift Container Platform during maintenance or hardware issues. 

For more information about vMotion and anti-affinity rules, see the VMware vSphere documentation for [vMotion networking requirements](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-3B41119A-1276-404B-8BFB-A32409052449.html) and [VM anti-affinity rules](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-FBE46165-065C-48C2-B775-7ADA87FF9A20.html). 

  * If you are using VMware vSphere volumes in your pods, migrating a VM across datastores, either manually or through Storage vMotion, causes invalid references within OpenShift Container Platform persistent volume (PV) objects that can result in data loss. 
  * OpenShift Container Platform does not support selective migration of virtual machine disks (VMDKs) across datastores, using datastore clusters for VM provisioning or for dynamic or static provisioning of PVs, or using a datastore that is part of a datastore cluster for dynamic or static provisioning of PVs. 

Important

You can specify the path of any datastore that exists in a datastore cluster. By default, Storage Distributed Resource Scheduler (SDRS), which uses Storage vMotion, is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable SDRS to avoid data loss issues for your OpenShift Container Platform cluster. If you must specify VMs across many datastores, use a `datastore` object to specify a failure domain in your cluster’s `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement". 




#### 3.1.3.1.4. Cluster resources

When you deploy an OpenShift Container Platform cluster that uses infrastructure that you provided, you must create the following resources in your vCenter instance: 

  * 1 Folder 
  * 1 Tag category 
  * 1 Tag 
  * Virtual machines: 

    * 1 template 
    * 1 temporary bootstrap node 
    * 3 control plane nodes 
    * 3 compute machines 




Although these resources use 856 GB of storage, the bootstrap node gets deleted during the cluster installation process. At a minimum, a standard cluster requires 800 GB of storage. 

If you deploy more compute machines, the OpenShift Container Platform cluster will use more storage. 

#### 3.1.3.1.5. Cluster limits

Available resources vary between clusters. A limit exists for the number of possible clusters within vCenter, primarily by available storage space and any limitations on the number of required resources. Be sure to consider both limitations to the vCenter resources that the cluster creates and the resources that you require to deploy a cluster, such as IP addresses and networks. 

#### 3.1.3.1.6. Networking requirements

You can use Dynamic Host Configuration Protocol (DHCP) for the network and configure the DHCP server to set persistent IP addresses to machines in your cluster. In the DHCP lease, you must configure the DHCP to use the default gateway. 

Note

You do not need to use the DHCP for the network if you want to provision nodes with static IP addresses. 

If you specify nodes or groups of nodes on different VLANs for a cluster that you want to install on user-provisioned infrastructure, you must ensure that machines in your cluster meet the requirements outlined in the "Network connectivity requirements" section of the _Networking requirements for user-provisioned infrastructure_ document. 

If you are installing to a restricted environment, the VM in your restricted network must have access to vCenter so that it can provision and manage nodes, persistent volume claims (PVCs), and other resources. 

Note

Ensure that each OpenShift Container Platform node in the cluster has access to a Network Time Protocol (NTP) server that is discoverable by DHCP. Installation is possible without an NTP server. However, asynchronous server clocks can cause errors, which the NTP server prevents. 

Additionally, you must create the following networking resources before you install the OpenShift Container Platform cluster: 

#### 3.1.3.1.7. DNS records

You must create DNS records for two static IP addresses in the appropriate DNS server for the vCenter instance that hosts your OpenShift Container Platform cluster. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`. 

Table 3.9. Required DNS recordsComponent| Record| Description  
---|---|---  
API VIP  |  `api.<cluster_name>.<base_domain>.` |  This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the control plane machines. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
Ingress VIP  |  `*.apps.<cluster_name>.<base_domain>.` |  A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the worker nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
Show more

**Additional resources**

  * [Creating a compute machine set on vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#creating-machineset-vsphere_creating-machineset-vsphere)



### 3.1.3.2. Required machines for cluster installation

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails. 

The smallest OpenShift Container Platform clusters require the following hosts: 

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines. 

Table 3.10. Minimum required hostsHosts| Description  
---|---  
One temporary bootstrap machine  |  The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster.   
Three control plane machines  |  The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane.   
At least two compute machines, which are also known as worker machines.  |  The workloads requested by OpenShift Container Platform users run on the compute machines.   
Show more

Important

To maintain high availability of your cluster, use separate physical hosts for these cluster machines. 

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can use Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later. 

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits). 

### 3.1.3.3. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 3.11. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
---|---|---|---|---|---  
Bootstrap  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Control plane  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Compute  |  RHCOS  |  2  |  8 GB  |  100 GB  |  300   
Show more

  * OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance. 
  * As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines. 



Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA): 

  * x86-64 architecture requires x86-64-v2 ISA 
  * ARM64 architecture requires ARMv8.0-A ISA 
  * ppc64le architecture requires IBM® Power9 ISA 
  * s390x architecture requires IBM® z14 ISA 



For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation. 

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform. 

Important

Do not use memory ballooning in OpenShift Container Platform clusters. Memory ballooning can cause cluster-wide instabilities, service degradation, or other undefined behaviors. 

  * Control plane machines must have committed memory equal to or greater than the published minimum resource requirements for a cluster installation. 
  * Compute machines must have a minimum reservation equal to or greater than the published minimum resource requirements for a cluster installation. 



These minimum CPU and memory requirements do not account for resources required by user workloads. 

For more information, see the Red Hat Knowledgebase article [Memory Ballooning and OpenShift](https://access.redhat.com/articles/7074533). 

**Additional resources**

  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)



### 3.1.3.4. Requirements for encrypting virtual machines

You can encrypt your virtual machines prior to installing OpenShift Container Platform 4.22 by meeting the following requirements. 

  * You have configured a Standard key provider in vSphere. For more information, see [Adding a KMS to vCenter Server](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-AC06B3C3-901F-402E-B25F-1EE7809D1264.html). 

Important

The Native key provider in vCenter is not supported. For more information, see [vSphere Native Key Provider Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-54B9FBA2-FDB1-400B-A6AE-81BF3AC9DF97.html). 

  * You have enabled host encryption mode on all of the ESXi hosts that are hosting the cluster. For more information, see [Enabling host encryption mode](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-A9E1F016-51B3-472F-B8DE-803F6BDB70BC.html). 
  * You have a vSphere account which has all cryptographic privileges enabled. For more information, see [Cryptographic Operations Privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-660CCB35-847F-46B3-81CA-10DDDB9D7AA9.html). 



When you deploy the OVF template in the section titled "Installing RHCOS and starting the OpenShift Container Platform bootstrap process", select the option to "Encrypt this virtual machine" when you are selecting storage for the OVF template. After completing cluster installation, create a storage class that uses the encryption storage policy you used to encrypt the virtual machines. 

**Additional resources**

  * [Creating an encrypted storage class](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#vsphere-pv-encryption)



### 3.1.3.5. Certificate signing requests management

On user-provisioned infrastructure, you must implement a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management. 

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that kubelet credentials request because it cannot confirm that the correct machine issued the request. You must find and implement a method of verifying the validity of the kubelet serving certificate requests and approving them. 

### 3.1.3.6. Networking requirements for user-provisioned infrastructure

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files. 

Important

Ensure you enable the `disk.EnableUUID` parameter on all virtual machines in your cluster. 

During the initial boot, the machines require an IP address configuration that is set either through a DHCP server or statically by providing the required boot options. After a network connection is established, the machines download their Ignition config files from an HTTP or HTTPS server. The Ignition config files are then used to set the exact state of each machine. The Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation. 

Note

  * Consider using a DHCP server for long-term management of the cluster machines. Ensure that the DHCP server is configured to provide persistent IP addresses, DNS server information, and hostnames to the cluster machines. 
  * If a DHCP service is not available for your user-provisioned infrastructure, you can instead provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the _Installing RHCOS and starting the OpenShift Container Platform bootstrap process_ section for more information about static IP provisioning and advanced networking options. 



The Kubernetes API server must be able to resolve the node names of the cluster machines. If the API servers and worker nodes are in different zones, you can configure a default DNS search zone to allow the API server to resolve the node names. Another supported approach is to always refer to hosts by their fully-qualified domain names in both the node objects and all DNS requests. 

#### 3.1.3.6.1. Setting the cluster node hostnames through DHCP

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start before this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node. 

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation. 

#### 3.1.3.6.2. Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster. 

This section provides details about the ports that are required. 

Important

In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat. 

Table 3.12. Ports used for all-machine to all-machine communicationsProtocol| Port| Description  
---|---|---  
ICMP  |  N/A  |  Network reachability tests   
TCP  |  `1936` |  Metrics   
`9000`-`9999` |  Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`.   
`10250`-`10259` |  The default ports that Kubernetes reserves   
`22623` |  The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines.   
UDP  |  `6081` |  Geneve   
`9000`-`9999` |  Host level services, including the node exporter on ports `9100`-`9101`.   
`500` |  IPsec IKE packets   
`4500` |  IPsec NAT-T packets   
`123` |  Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`.   
TCP/UDP  |  `30000`-`32767` |  Kubernetes node port   
ESP  |  N/A  |  IPsec Encapsulating Security Payload (ESP)   
Show more

Table 3.13. Ports used for all-machine to control plane communicationsProtocol| Port| Description  
---|---|---  
TCP  |  `6443` |  Kubernetes API   
Show more

Table 3.14. Ports used for control plane machine to control plane machine communicationsProtocol| Port| Description  
---|---|---  
TCP  |  `2379`-`2380` |  etcd server and peer ports   
Show more

#### 3.1.3.6.3. NTP configuration for user-provisioned infrastructure

OpenShift Container Platform clusters are configured to use a public Network Time Protocol (NTP) server by default. If you want to use a local enterprise NTP server, or if your cluster is being deployed in a disconnected network, you can configure the cluster to use a specific time server. For more information, see the documentation for _Configuring chrony time service_. 

If a DHCP server provides NTP server information, the chrony time service on the Red Hat Enterprise Linux CoreOS (RHCOS) machines read the information and can sync the clock with the NTP servers. 

**Additional resources**

  * [Configuring chrony time service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#installation-special-config-chrony_installing-customizing)



### 3.1.3.7. User-provisioned DNS requirements

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes. 

The following is a list of required cluster components: 

  * The Kubernetes API 
  * The OpenShift Container Platform application wildcard 
  * The bootstrap and control plane machines 
  * The compute machines 



Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines. 

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate. 

Note

It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the _DHCP recommendations for user-provisioned infrastructure_ section for more information. 

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`. 

Table 3.15. Required DNS recordsComponent| Record| Description  
---|---|---  
Kubernetes API  |  `api.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
`api-int.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.  Important The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods.   
Routes  |  `*.apps.<cluster_name>.<base_domain>.` |  A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console.   
Bootstrap machine  |  `bootstrap.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap machine. These records must be resolvable by the nodes within the cluster.   
Control plane machines  |  `<control_plane><n>.<cluster_name>.<base_domain>.` |  DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster.   
Compute machines  |  `<compute><n>.<cluster_name>.<base_domain>.` |  DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster.   
Show more

Note

In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration. 

Tip

You can use the `dig` command to verify name and reverse name resolution. See the section on _Validating DNS resolution for user-provisioned infrastructure_ for detailed validation steps. 

#### 3.1.3.7.1. Example DNS configuration for user-provisioned clusters

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure. 

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another. 

In the examples, the cluster name is `ocp4` and the base domain is `example.com`. 

The following example is a BIND zone file that shows sample DNS A records for name resolution in a user-provisioned cluster. 

Note

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

```plaintext
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
	IN	MX 10	smtp.example.com.
;
;
ns1.example.com.		IN	A	192.168.1.5
smtp.example.com.		IN	A	192.168.1.5
;
helper.example.com.		IN	A	192.168.1.5
helper.ocp4.example.com.	IN	A	192.168.1.5
;
api.ocp4.example.com.		IN	A	192.168.1.5
api-int.ocp4.example.com.	IN	A	192.168.1.5
;
*.apps.ocp4.example.com.	IN	A	192.168.1.5
;
bootstrap.ocp4.example.com.	IN	A	192.168.1.96
;
control-plane0.ocp4.example.com.	IN	A	192.168.1.97
control-plane1.ocp4.example.com.	IN	A	192.168.1.98
;
control-plane2.ocp4.example.com.	IN	A	192.168.1.99
;
compute0.ocp4.example.com.	IN	A	192.168.1.11
compute1.ocp4.example.com.	IN	A	192.168.1.7
;
;EOF
```


where: 

`api.ocp4.example.com.`
     Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer. 
`api-int.ocp4.example.com.`
     Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications. 
`*.apps.ocp4.example.com.`
     Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. 
`bootstrap.ocp4.example.com`
     Provides name resolution for the bootstrap machine. 
`control-plane0.ocp4.example.com`
     Provides name resolution for the control plane machines. 
`compute0.ocp4.example.com.`
     Provides name resolution for the compute machines. 

The following example BIND zone file shows sample PTR records for reverse name resolution in a user-provisioned cluster: 

```plaintext
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
;
5.1.168.192.in-addr.arpa.	IN	PTR	api.ocp4.example.com.
5.1.168.192.in-addr.arpa.	IN	PTR	api-int.ocp4.example.com.
;
96.1.168.192.in-addr.arpa.	IN	PTR	bootstrap.ocp4.example.com.
;
97.1.168.192.in-addr.arpa.	IN	PTR	control-plane0.ocp4.example.com.
98.1.168.192.in-addr.arpa.	IN	PTR	control-plane1.ocp4.example.com.
;
99.1.168.192.in-addr.arpa.	IN	PTR	control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	compute1.ocp4.example.com.
;
;EOF
```


where: 

`api.ocp4.example.com.`
     Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer. 
`api-int.ocp4.example.com.`
     Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications. 
`bootstrap.ocp4.example.com.`
     Provides reverse DNS resolution for the bootstrap machine. 
`control-plane0.ocp4.example.com.`
     Provides reverse DNS resolution for the control plane machines. 
`compute0.ocp4.example.com.`
     Provides reverse DNS resolution for the compute machines. 

Note

A PTR record is not required for the OpenShift Container Platform application wildcard. 

### 3.1.3.8. Load balancing requirements for user-provisioned infrastructure

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

Note

If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately. 

The load balancing infrastructure must meet the following requirements: 

  * API load balancer: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions: 

    * Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode. 
    * A stateless load balancing algorithm. The options vary based on the load balancer implementation. 




Important

Do not configure session persistence for an API load balancer. Configuring session persistence for a Kubernetes API server might cause performance issues from excess application traffic for your OpenShift Container Platform cluster and the Kubernetes API that runs inside the cluster. 

Configure the following ports on both the front and back of the API load balancers: 

Port| Back-end machines (pool members)| Internal| External| Description  
---|---|---|---|---  
`6443` |  Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. You must configure the `/readyz` endpoint for the API server health check probe.  |  X  |  X  |  Kubernetes API server   
`22623` |  Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane.  |  X  |  |  Machine config server   
Show more

Note

The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values. 

  * Application Ingress load balancer: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. Configure the following conditions: 

    * Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode. 
    * A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform. 




Tip

If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption. 

Configure the following ports on both the front and back of the load balancers: 

Table 3.16. Application Ingress load balancerPort| Back-end machines (pool members)| Internal| External| Description  
---|---|---|---|---  
`443` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTPS traffic   
`80` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTP traffic   
Show more

Note

If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. 

#### 3.1.3.8.1. Example load balancer configuration for user-provisioned clusters

Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters. 

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another. 

Tip

If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node. 

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

Note

If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`. 

**Sample API and application Ingress load balancer configuration**

```plaintext
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
```


where: 

`listen api-server-6443`
     Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic. 
`server bootstrap bootstrap.ocp4.example.com`
     The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete. 
`listen machine-config-server`
     Port `22623` handles the machine config server traffic and points to the control plane machines. 
`listen ingress-router-443`
     Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. 
`listen ingress-router-80`
    

Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. 

Note

If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
