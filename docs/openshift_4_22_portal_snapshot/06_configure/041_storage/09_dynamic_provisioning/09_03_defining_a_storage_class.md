# 9.3. Defining a storage class

`StorageClass` objects apply cluster-wide and are available to all namespaces. Only users with cluster-admin or storage-admin privileges can create or modify them. 

This centralized control ensures consistent storage policies across your cluster while requiring application teams to coordinate with administrators for custom storage configurations. 

Important

The Cluster Storage Operator might install a default storage class depending on the platform in use. This storage class is owned and controlled by the Operator. It cannot be deleted or modified beyond defining annotations and labels. If different behavior is required, you must define a custom storage class. 

The following sections describe the basic definition for a `StorageClass` object and specific examples for each of the supported plugin types. 

## 9.3.1. Basic StorageClass object definition

A `StorageClass` object defines the metadata, provisioner type, and plugin-specific parameters that determine how persistent volumes (PVs) are dynamically created in your cluster. 

Each storage provisioner type requires different parameters, and annotations control cluster-wide defaults, making this structure the foundation for all dynamic storage provisioning. 

**Example`StorageClass` definition**

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
  annotations:
    storageclass.kubernetes.io/is-default-class: 'true'
    ...
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
...
```


  * `kind`: API object type. 
  * `apiversion`: The current apiVersion. 
  * `metadata.name`: The name of the storage class. 
  * Optional: `metadata.annotations`: Annotations for the storage class. 
  * `provisioner`: The type of provisioner associated with this storage class. 
  * Optional: `parameters`: The parameters required for the specific provisioner. This is different for each plugin. 



## 9.3.2. RHOSP Cinder StorageObject object definition

This RHOSP Cinder storage class example demonstrates how to configure volume types for performance optimization, control availability zone placement for high availability, and specify filesystem types for your persistent volumes. 

**Example Cinder storage class YAML file**

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
provisioner: kubernetes.io/cinder
parameters:
  type: fast
  availability: nova
  fsType: ext4
```


  * `metadata.name`: Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes. 
  * `parameter.type`: Volume type created in Cinder. Default is empty. 
  * `parameters.availability`: Availability Zone. If not specified, volumes are generally round-robined across all active zones where theOpenShift Container Platform cluster has a node. 
  * `parameters.fsType`: File system that is created on dynamically provisioned volumes. This value is copied to the `fsType` field of dynamically provisioned persistent volumes, and the file system is created when the volume is mounted for the first time. The default value is `ext4`. The following is a RHOSP Cinder example storage class object definition. 



## 9.3.3. RHOSP Manila Container Storage Interface (CSI) object definition

The OpenStack Manila CSI Driver Operator automatically creates storage classes for all available Manila share types immediately after installation, eliminating manual configuration. 

This automation ensures you can start provisioning persistent volumes right away without needing to understand Manila share type details or write custom `StorageClass` definitions. 

## 9.3.4. AWS Elastic Block Store (EBS) StorageObject object definition

This AWS EBS storage class example shows how to configure volume type, IOPS performance, encryption settings, and filesystem type for dynamically provisioned persistent volumes. 

**Example AWS EBS storage class YAML file**

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
provisioner: ebs.csi.aws.com
parameters:
  type: io1
  iopsPerGB: "10"
  encrypted: "true"
  kmsKeyId: keyvalue
  fsType: ext4
```


  * `metadata.name`: Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes. 
  * `parameters.type`: Select from `io1`, `gp3`, `sc1`, `st1`. The default is `gp3`. For valid Amazon Resource Name (ARN) values, see the AWS documentation, _Identify AWS resources with Amazon Resource Names (ARNs)_. 
  * Optional: `parameters.iopsPerGB`. Only for **io1** volumes. I/O operations per second per GiB. 

The AWS volume plugin multiplies this with the size of the requested volume to compute IOPS of the volume. The maximum value is 20,000 IOPS, which is the maximum supported by AWS. 

For more information, see the AWS documentation, _Identify AWS resources with Amazon Resource Names (ARNs)_. 

  * Optional: `parameters.encrypted`. Indicates whether to encrypt the EBS volume. Valid values are `true` or `false`. 
  * Optional: `parameters.kmsKeyId`. The full ARN of the key to use when encrypting the volume. If none is supplied, but `encypted` is set to `true`, then AWS generates a key. 

For valid ARN values, see the AWS documentation, _Identify AWS resources with Amazon Resource Names (ARNs)_. 

  * Optional: `parameters.fsType`. File system that is created on dynamically provisioned volumes. This value is copied to the `fsType` field of dynamically provisioned persistent volumes, and the file system is created when the volume is mounted for the first time. The default value is `ext4`. 



**Additional resources**

  * [AWS documentation](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)



## 9.3.5. Azure Disk StorageClass object definition

This Azure Disk storage class example demonstrates how to configure managed disks with delayed volume binding for optimal zone placement, volume expansion, and performance tiers. 

Key parameters ensure compatibility with OpenShift nodes, which require managed disks rather than shared or dedicated storage accounts. 

**Example Azure Disk storage class YAML file**

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class-name>
provisioner: kubernetes.io/azure-disk
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  kind: Managed
  storageaccounttype: Premium_LRS
reclaimPolicy: Delete
```


  * `metadata.name`: Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes. 
  * `volumeBindingMode`: Using `WaitForFirstConsumer` is strongly recommended. This provisions the volume while allowing enough storage to schedule the pod on a free worker node from an available zone. 
  * `parameters.kind`: Possible values are `Shared` (default), `Managed`, and `Dedicated`. 

Important

Red Hat only supports the use of `Managed`. 

With `Shared` and `Dedicated`, Azure creates unmanaged disks, while OpenShift Container Platform creates a managed disk for machine operating system (root) disks. But because Azure Disk does not allow the use of both managed and unmanaged disks on a node, unmanaged disks created with `Shared` or `Dedicated` cannot be attached to OpenShift Container Platform nodes. 

  * `parameters.storageaccounttype`: Azure storage account SKU tier. Default is empty. Note that Premium VMs can attach both `Standard_LRS` and `Premium_LRS` disks. Standard VMs can only attach `Standard_LRS` disks. Managed VMs can only attach managed disks. Unmanaged VMs can only attach unmanaged disks. 

    * `Shared`: Azure creates all unmanaged disks in a few shared storage accounts in the same resource group as the cluster. 
    * `Managed`: Azure creates new managed disks. 
    * `Dedicated`, and a `storageAccount` is not specified: Azure creates a new dedicated storage account for the new unmanaged disk in the same resource group as the cluster. 
    * `Dedicated`, and a `storageAccount` is specified: Azure uses the specified storage account for the new unmanaged disk in the same resource group as the cluster. For this to work, the specified storage account must be in the same region, and Azure Cloud Provider must have write access to the storage account. 




## 9.3.6. Azure File object definition

To enable Azure File storage classes to dynamically provision file shares, grant the persistent volume binder permissions to create and manage secrets containing Azure storage credentials. 

This allows the provisioner to securely store and access the Azure storage account name and key required for file share creation. 

**Procedure**

  1. Define a `ClusterRole` object that allows access to create and view secrets as in the following example file: 

**Cluster role example YAML file**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: <persistent_volume_binder_role>
rules:
- apiGroups: ['']
  resources: ['secrets']
  verbs:     ['get','create']
```


     * `Metadata.name`: The name of the cluster role to view and create secrets. 

  2. Add the cluster role to the service account by running the following command: 

```shell-session
$ oc adm policy add-cluster-role-to-user <persistent-volume-binder-role> system:serviceaccount:kube-system:persistent-volume-binder
```


Where `<persistent-volume-binder-role>` is the name of the cluster role you provided in the preceding step. 

  3. Create the Azure File `StorageClass` object as in the following example file: 

**Example Azure File storage class YAML file**

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <azure-file>
provisioner: kubernetes.io/azure-file
parameters:
  location: eastus
  skuName: Standard_LRS
  storageAccount: <storage-account>
reclaimPolicy: Delete
volumeBindingMode: Immediate
```


     * `metadata.name`: Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes. 
     * `parameters.location`: Location of the Azure storage account, such as `eastus`. The default is empty, meaning that a new Azure storage account is created in the OpenShift Container Platform cluster’s location. 
     * `parameters.skuName`: SKU tier of the Azure storage account, such as `Standard_LRS`. The default is empty, meaning that a new Azure storage account is created with the `Standard_LRS` SKU. 
     * `parameters.storageAccount`: Name of the Azure storage account. If a storage account is provided, then `skuName` and `location` are ignored. If no storage account is provided, the storage class searches for storage accounts associated with the resource group for accounts that match the defined `skuName` and `location`. 




### 9.3.6.1. Considerations when using Azure File

Azure File storage has inherent file system limitations, including lack of support for symlinks, hard links, and sparse files by default, plus ownership mismatches between mounted directories and container processes. 

Understanding these constraints and using mount options such as uid, gid, and mfsymlinks helps you configure Azure File storage classes that work correctly with your containerized applications. 

The following features are not supported: 

  * Symlinks 
  * Hard links 
  * Extended attributes 
  * Sparse files 
  * Named pipes 



Additionally, the owner user identifier (UID) of the Azure File mounted directory is different from the process UID of the container. You can specify the `uid` mount option in the `StorageClass` object to define a specific user identifier to use for the mounted directory. 

The following `StorageClass` object demonstrates modifying the `uid` and group identifier (`gid`), along with enabling symlinks for the mounted directory. 

**Example Azure File storage class YAML file with modified`uid` and `gid`**

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: azure-file
mountOptions:
  - uid=1500
  - gid=1500
  - mfsymlinks
provisioner: kubernetes.io/azure-file
parameters:
  location: eastus
  skuName: Standard_LRS
reclaimPolicy: Delete
volumeBindingMode: Immediate
```


  * `mountOptions.uid`: Specifies the user identifier to use for the mounted directory. 
  * `mountOptions.gid`: Specifies the group identifier to use for the mounted directory. 
  * `mountOptions.mfsymlinks`: Enables symlinks. 



## 9.3.7. GCE PersistentDisk (gcePD) object definition

This Google Compute Engine Persistent Disk (GCE PD) storage class example shows how to configure disk performance tiers (SSD, standard, or hyperdisk-balanced), enable volume expansion, and use delayed binding to optimize zone placement for your workloads. 

**Example GCE PD storage class YAML file**

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class-name>
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
  replication-type: none
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Delete
```


  * `metadata.name`: The name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes. 
  * `parameters.type`: Select `pd-ssd`, `pd-standard`, or `hyperdisk-balanced`. The default is `pd-ssd`. 



## 9.3.8. VMware vSphere object definition

This VMware vSphere storage class example demonstrates the basic structure and Container Storage Interface (CSI) provisioner configuration required to enable dynamic storage provisioning on vSphere infrastructure. 

This minimal definition provides the foundation for vSphere storage integration, which you can extend with storage policies, datastore preferences, and other vSphere-specific parameters. 

**Example vSphere storage class YAML file**

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
provisioner: csi.vsphere.vmware.com
```


  * `metadata.name`: Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes. 
  * `provisioner`: The name of the provisioner for the storage class. For vSphere, this is `csi.vsphere.vmware.com`.
