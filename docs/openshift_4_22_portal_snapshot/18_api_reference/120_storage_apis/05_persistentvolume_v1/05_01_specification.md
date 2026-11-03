# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  PersistentVolumeSpec is the specification of a persistent volume.   
`status` |  `object` |  PersistentVolumeStatus is the current status of a persistent volume.   
Show more

## 5.1.1. .spec

Description
     PersistentVolumeSpec is the specification of a persistent volume. 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessModes` |  `array (string)` |  accessModes contains all ways the volume can be mounted. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes>  
`awsElasticBlockStore` |  `object` |  Represents a Persistent Disk resource in AWS.  An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.   
`azureDisk` |  `object` |  AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.   
`azureFile` |  `object` |  AzureFile represents an Azure File Service mount on the host and bind mount to the pod.   
`capacity` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  capacity is the description of the persistent volume’s resources and capacity. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity>  
`cephfs` |  `object` |  Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.   
`cinder` |  `object` |  Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.   
`claimRef` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
`csi` |  `object` |  Represents storage that is managed by an external CSI volume driver   
`fc` |  `object` |  Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.   
`flexVolume` |  `object` |  FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.   
`flocker` |  `object` |  Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.   
`gcePersistentDisk` |  `object` |  Represents a Persistent Disk resource in Google Compute Engine.  A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.   
`glusterfs` |  `object` |  Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.   
`hostPath` |  `object` |  Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.   
`iscsi` |  `object` |  ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.   
`local` |  `object` |  Local represents directly-attached storage with node affinity   
`mountOptions` |  `array (string)` |  mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options>  
`nfs` |  `object` |  Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.   
`nodeAffinity` |  `object` |  VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.   
`persistentVolumeReclaimPolicy` |  `string` |  persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming> Possible enum values: - `"Delete"` means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion. - `"Recycle"` means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling. - `"Retain"` means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain.   
`photonPersistentDisk` |  `object` |  Represents a Photon Controller persistent disk resource.   
`portworxVolume` |  `object` |  PortworxVolumeSource represents a Portworx volume resource.   
`quobyte` |  `object` |  Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.   
`rbd` |  `object` |  Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.   
`scaleIO` |  `object` |  ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume   
`storageClassName` |  `string` |  storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.   
`storageos` |  `object` |  Represents a StorageOS persistent volume resource.   
`volumeAttributesClassName` |  `string` |  Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process.   
`volumeMode` |  `string` |  volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.  Possible enum values: - `"Block"` means the volume will not be formatted with a filesystem and will remain a raw block device. - `"Filesystem"` means the volume will be or is formatted with a filesystem.   
`vsphereVolume` |  `object` |  Represents a vSphere volume resource.   
Show more

## 5.1.2. .spec.awsElasticBlockStore

Description
    

Represents a Persistent Disk resource in AWS. 

An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling. 

Type
     `object`
Required
    

  * `volumeID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>  
`partition` |  `integer` |  partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).   
`readOnly` |  `boolean` |  readOnly value true will force the readOnly setting in VolumeMounts. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>  
`volumeID` |  `string` |  volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>  
Show more

## 5.1.3. .spec.azureDisk

Description
     AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. 
Type
     `object`
Required
    

  * `diskName`
  * `diskURI`



Property| Type| Description  
---|---|---  
`cachingMode` |  `string` |  cachingMode is the Host Caching mode: None, Read Only, Read Write.  Possible enum values: - `"None"` \- `"ReadOnly"` \- `"ReadWrite"`  
`diskName` |  `string` |  diskName is the Name of the data disk in the blob storage   
`diskURI` |  `string` |  diskURI is the URI of data disk in the blob storage   
`fsType` |  `string` |  fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`kind` |  `string` |  kind expected values are Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared  Possible enum values: - `"Dedicated"` \- `"Managed"` \- `"Shared"`  
`readOnly` |  `boolean` |  readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
Show more

## 5.1.4. .spec.azureFile

Description
     AzureFile represents an Azure File Service mount on the host and bind mount to the pod. 
Type
     `object`
Required
    

  * `secretName`
  * `shareName`



Property| Type| Description  
---|---|---  
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretName` |  `string` |  secretName is the name of secret that contains Azure Storage Account Name and Key   
`secretNamespace` |  `string` |  secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod   
`shareName` |  `string` |  shareName is the azure Share Name   
Show more

## 5.1.5. .spec.cephfs

Description
     Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling. 
Type
     `object`
Required
    

  * `monitors`



Property| Type| Description  
---|---|---  
`monitors` |  `array (string)` |  monitors is Required: Monitors is a collection of Ceph monitors More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
`path` |  `string` |  path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /   
`readOnly` |  `boolean` |  readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
`secretFile` |  `string` |  secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
`secretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`user` |  `string` |  user is Optional: User is the rados user name, default is admin More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
Show more

## 5.1.6. .spec.cephfs.secretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.7. .spec.cinder

Description
     Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling. 
Type
     `object`
Required
    

  * `volumeID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>  
`readOnly` |  `boolean` |  readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>  
`secretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`volumeID` |  `string` |  volumeID used to identify the volume in cinder. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>  
Show more

## 5.1.8. .spec.cinder.secretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.9. .spec.claimRef

Description
     ObjectReference contains enough information to let you inspect or modify the referred object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 5.1.10. .spec.csi

Description
     Represents storage that is managed by an external CSI volume driver 
Type
     `object`
Required
    

  * `driver`
  * `volumeHandle`



Property| Type| Description  
---|---|---  
`controllerExpandSecretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`controllerPublishSecretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`driver` |  `string` |  driver is the name of the driver to use for this volume. Required.   
`fsType` |  `string` |  fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".   
`nodeExpandSecretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`nodePublishSecretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`nodeStageSecretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`readOnly` |  `boolean` |  readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).   
`volumeAttributes` |  `object (string)` |  volumeAttributes of the volume to publish.   
`volumeHandle` |  `string` |  volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.   
Show more

## 5.1.11. .spec.csi.controllerExpandSecretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.12. .spec.csi.controllerPublishSecretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.13. .spec.csi.nodeExpandSecretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.14. .spec.csi.nodePublishSecretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.15. .spec.csi.nodeStageSecretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.16. .spec.fc

Description
     Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling. 
Type
     `object`

Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`lun` |  `integer` |  lun is Optional: FC target lun number   
`readOnly` |  `boolean` |  readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`targetWWNs` |  `array (string)` |  targetWWNs is Optional: FC target worldwide names (WWNs)   
`wwids` |  `array (string)` |  wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.   
Show more

## 5.1.17. .spec.flexVolume

Description
     FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin. 
Type
     `object`
Required
    

  * `driver`



Property| Type| Description  
---|---|---  
`driver` |  `string` |  driver is the name of the driver to use for this volume.   
`fsType` |  `string` |  fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.   
`options` |  `object (string)` |  options is Optional: this field holds extra command options if any.   
`readOnly` |  `boolean` |  readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
Show more

## 5.1.18. .spec.flexVolume.secretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.19. .spec.flocker

Description
     Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling. 
Type
     `object`

Property| Type| Description  
---|---|---  
`datasetName` |  `string` |  datasetName is Name of the dataset stored as metadata  name on the dataset for Flocker should be considered as deprecated   
`datasetUUID` |  `string` |  datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset   
Show more

## 5.1.20. .spec.gcePersistentDisk

Description
    

Represents a Persistent Disk resource in Google Compute Engine. 

A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling. 

Type
     `object`
Required
    

  * `pdName`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
`partition` |  `integer` |  partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
`pdName` |  `string` |  pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
`readOnly` |  `boolean` |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
Show more

## 5.1.21. .spec.glusterfs

Description
     Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling. 
Type
     `object`
Required
    

  * `endpoints`
  * `path`



Property| Type| Description  
---|---|---  
`endpoints` |  `string` |  endpoints is the endpoint name that details Glusterfs topology. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod>  
`endpointsNamespace` |  `string` |  endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod>  
`path` |  `string` |  path is the Glusterfs volume path. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod>  
`readOnly` |  `boolean` |  readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod>  
Show more

## 5.1.22. .spec.hostPath

Description
     Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling. 
Type
     `object`
Required
    

  * `path`



Property| Type| Description  
---|---|---  
`path` |  `string` |  path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>  
`type` |  `string` |  type for HostPath Volume Defaults to "" More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath> Possible enum values: - `""` For backwards compatible, leave it empty if unset - `"BlockDevice"` A block device must exist at the given path - `"CharDevice"` A character device must exist at the given path - `"Directory"` A directory must exist at the given path - `"DirectoryOrCreate"` If nothing exists at the given path, an empty directory will be created there as needed with file mode 0755, having the same group and ownership with Kubelet. - `"File"` A file must exist at the given path - `"FileOrCreate"` If nothing exists at the given path, an empty file will be created there as needed with file mode 0644, having the same group and ownership with Kubelet. - `"Socket"` A UNIX socket must exist at the given path   
Show more

## 5.1.23. .spec.iscsi

Description
     ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling. 
Type
     `object`
Required
    

  * `targetPortal`
  * `iqn`
  * `lun`



Property| Type| Description  
---|---|---  
`chapAuthDiscovery` |  `boolean` |  chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication   
`chapAuthSession` |  `boolean` |  chapAuthSession defines whether support iSCSI Session CHAP authentication   
`fsType` |  `string` |  fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#iscsi>  
`initiatorName` |  `string` |  initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.   
`iqn` |  `string` |  iqn is Target iSCSI Qualified Name.   
`iscsiInterface` |  `string` |  iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).   
`lun` |  `integer` |  lun is iSCSI Target Lun number.   
`portals` |  `array (string)` |  portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).   
`readOnly` |  `boolean` |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.   
`secretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`targetPortal` |  `string` |  targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).   
Show more

## 5.1.24. .spec.iscsi.secretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.25. .spec.local

Description
     Local represents directly-attached storage with node affinity 
Type
     `object`
Required
    

  * `path`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified.   
`path` |  `string` |  path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, …​).   
Show more

## 5.1.26. .spec.nfs

Description
     Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling. 
Type
     `object`
Required
    

  * `server`
  * `path`



Property| Type| Description  
---|---|---  
`path` |  `string` |  path that is exported by the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>  
`readOnly` |  `boolean` |  readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>  
`server` |  `string` |  server is the hostname or IP address of the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>  
Show more

## 5.1.27. .spec.nodeAffinity

Description
     VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from. 
Type
     `object`

Property| Type| Description  
---|---|---  
`required` |  `object` |  A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.   
Show more

## 5.1.28. .spec.nodeAffinity.required

Description
     A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms. 
Type
     `object`
Required
    

  * `nodeSelectorTerms`



Property| Type| Description  
---|---|---  
`nodeSelectorTerms` |  `array` |  Required. A list of node selector terms. The terms are ORed.   
`nodeSelectorTerms[]` |  `object` |  A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.   
Show more

## 5.1.29. .spec.nodeAffinity.required.nodeSelectorTerms

Description
     Required. A list of node selector terms. The terms are ORed. 
Type
     `array`

## 5.1.30. .spec.nodeAffinity.required.nodeSelectorTerms[]

Description
     A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  A list of node selector requirements by node’s labels.   
`matchExpressions[]` |  `object` |  A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchFields` |  `array` |  A list of node selector requirements by node’s fields.   
`matchFields[]` |  `object` |  A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
Show more

## 5.1.31. .spec.nodeAffinity.required.nodeSelectorTerms[].matchExpressions

Description
     A list of node selector requirements by node’s labels. 
Type
     `array`

## 5.1.32. .spec.nodeAffinity.required.nodeSelectorTerms[].matchExpressions[]

Description
     A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The label key that the selector applies to.   
`operator` |  `string` |  Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.  Possible enum values: - `"DoesNotExist"` \- `"Exists"` \- `"Gt"` \- `"In"` \- `"Lt"` \- `"NotIn"`  
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.   
Show more

## 5.1.33. .spec.nodeAffinity.required.nodeSelectorTerms[].matchFields

Description
     A list of node selector requirements by node’s fields. 
Type
     `array`

## 5.1.34. .spec.nodeAffinity.required.nodeSelectorTerms[].matchFields[]

Description
     A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The label key that the selector applies to.   
`operator` |  `string` |  Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.  Possible enum values: - `"DoesNotExist"` \- `"Exists"` \- `"Gt"` \- `"In"` \- `"Lt"` \- `"NotIn"`  
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.   
Show more

## 5.1.35. .spec.photonPersistentDisk

Description
     Represents a Photon Controller persistent disk resource. 
Type
     `object`
Required
    

  * `pdID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`pdID` |  `string` |  pdID is the ID that identifies Photon Controller persistent disk   
Show more

## 5.1.36. .spec.portworxVolume

Description
     PortworxVolumeSource represents a Portworx volume resource. 
Type
     `object`
Required
    

  * `volumeID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.   
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`volumeID` |  `string` |  volumeID uniquely identifies a Portworx volume   
Show more

## 5.1.37. .spec.quobyte

Description
     Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling. 
Type
     `object`
Required
    

  * `registry`
  * `volume`



Property| Type| Description  
---|---|---  
`group` |  `string` |  group to map volume access to Default is no group   
`readOnly` |  `boolean` |  readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.   
`registry` |  `string` |  registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes   
`tenant` |  `string` |  tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin   
`user` |  `string` |  user to map volume access to Defaults to serivceaccount user   
`volume` |  `string` |  volume is a string that references an already created Quobyte volume by name.   
Show more

## 5.1.38. .spec.rbd

Description
     Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling. 
Type
     `object`
Required
    

  * `monitors`
  * `image`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#rbd>  
`image` |  `string` |  image is the rados image name. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`keyring` |  `string` |  keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`monitors` |  `array (string)` |  monitors is a collection of Ceph monitors. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`pool` |  `string` |  pool is the rados pool name. Default is rbd. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`readOnly` |  `boolean` |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`secretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`user` |  `string` |  user is the rados user name. Default is admin. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
Show more

## 5.1.39. .spec.rbd.secretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.40. .spec.scaleIO

Description
     ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume 
Type
     `object`
Required
    

  * `gateway`
  * `system`
  * `secretRef`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"   
`gateway` |  `string` |  gateway is the host address of the ScaleIO API Gateway.   
`protectionDomain` |  `string` |  protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.   
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretRef` |  `object` |  SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace   
`sslEnabled` |  `boolean` |  sslEnabled is the flag to enable/disable SSL communication with Gateway, default false   
`storageMode` |  `string` |  storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.   
`storagePool` |  `string` |  storagePool is the ScaleIO Storage Pool associated with the protection domain.   
`system` |  `string` |  system is the name of the storage system as configured in ScaleIO.   
`volumeName` |  `string` |  volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.   
Show more

## 5.1.41. .spec.scaleIO.secretRef

Description
     SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 5.1.42. .spec.storageos

Description
     Represents a StorageOS persistent volume resource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretRef` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
`volumeName` |  `string` |  volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace.   
`volumeNamespace` |  `string` |  volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod’s namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.   
Show more

## 5.1.43. .spec.storageos.secretRef

Description
     ObjectReference contains enough information to let you inspect or modify the referred object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 5.1.44. .spec.vsphereVolume

Description
     Represents a vSphere volume resource. 
Type
     `object`
Required
    

  * `volumePath`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`storagePolicyID` |  `string` |  storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.   
`storagePolicyName` |  `string` |  storagePolicyName is the storage Policy Based Management (SPBM) profile name.   
`volumePath` |  `string` |  volumePath is the path that identifies vSphere volume vmdk   
Show more

## 5.1.45. .status

Description
     PersistentVolumeStatus is the current status of a persistent volume. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastPhaseTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions.   
`message` |  `string` |  message is a human-readable message indicating details about why the volume is in this state.   
`phase` |  `string` |  phase indicates if a volume is available, bound to a claim, or released by a claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase> Possible enum values: - `"Available"` used for PersistentVolumes that are not yet bound Available volumes are held by the binder and matched to PersistentVolumeClaims - `"Bound"` used for PersistentVolumes that are bound - `"Failed"` used for PersistentVolumes that failed to be correctly recycled or deleted after being released from a claim - `"Pending"` used for PersistentVolumes that are not available - `"Released"` used for PersistentVolumes where the bound PersistentVolumeClaim was deleted released volumes must be recycled before becoming available again this phase is used by the persistent volume claim binder to signal to another process to reclaim the resource   
`reason` |  `string` |  reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.   
Show more
