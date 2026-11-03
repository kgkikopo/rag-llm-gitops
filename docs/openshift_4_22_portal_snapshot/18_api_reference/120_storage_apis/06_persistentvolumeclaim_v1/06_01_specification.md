# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes   
`status` |  `object` |  PersistentVolumeClaimStatus is the current status of a persistent volume claim.   
Show more

## 6.1.1. .spec

Description
     PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessModes` |  `array (string)` |  accessModes contains the desired access modes the volume should have. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1>  
`dataSource` |  `object` |  TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.   
`dataSourceRef` |  `object` |  TypedObjectReference contains enough information to let you locate the typed referenced object   
`resources` |  `object` |  VolumeResourceRequirements describes the storage resource requirements for a volume.   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is a label query over volumes to consider for binding.   
`storageClassName` |  `string` |  storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1>  
`volumeAttributesClassName` |  `string` |  volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string or nil value indicates that no VolumeAttributesClass will be applied to the claim. If the claim enters an Infeasible error state, this field can be reset to its previous value (including nil) to cancel the modification. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/>  
`volumeMode` |  `string` |  volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  Possible enum values: - `"Block"` means the volume will not be formatted with a filesystem and will remain a raw block device. - `"Filesystem"` means the volume will be or is formatted with a filesystem.   
`volumeName` |  `string` |  volumeName is the binding reference to the PersistentVolume backing this claim.   
Show more

## 6.1.2. .spec.dataSource

Description
     TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
Show more

## 6.1.3. .spec.dataSourceRef

Description
     TypedObjectReference contains enough information to let you locate the typed referenced object 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
`namespace` |  `string` |  Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
Show more

## 6.1.4. .spec.resources

Description
     VolumeResourceRequirements describes the storage resource requirements for a volume. 
Type
     `object`

Property| Type| Description  
---|---|---  
`limits` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more

## 6.1.5. .status

Description
     PersistentVolumeClaimStatus is the current status of a persistent volume claim. 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessModes` |  `array (string)` |  accessModes contains the actual access modes the volume backing the PVC has. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1>  
`allocatedResourceStatuses` |  `object (string)` |  allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states: - ControllerResizeInProgress: State set when resize controller starts resizing the volume in control-plane. - ControllerResizeFailed: State set when resize has failed in resize controller with a terminal error. - NodeResizePending: State set when resize controller has finished resizing the volume but further resizing of volume is needed on the node. - NodeResizeInProgress: State set when kubelet starts resizing the volume. - NodeResizeFailed: State set when resizing has failed in kubelet with a terminal error. Transient errors don’t set NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.   
`allocatedResources` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.   
`capacity` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  capacity represents the actual resources of the underlying volume.   
`conditions` |  `array` |  conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.   
`conditions[]` |  `object` |  PersistentVolumeClaimCondition contains details about state of pvc   
`currentVolumeAttributesClassName` |  `string` |  currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim   
`modifyVolumeStatus` |  `object` |  ModifyVolumeStatus represents the status object of ControllerModifyVolume operation   
`phase` |  `string` |  phase represents the current phase of PersistentVolumeClaim.  Possible enum values: - `"Bound"` used for PersistentVolumeClaims that are bound - `"Lost"` used for PersistentVolumeClaims that lost their underlying PersistentVolume. The claim was bound to a PersistentVolume and this volume does not exist any longer and all data on it was lost. - `"Pending"` used for PersistentVolumeClaims that are not yet bound   
Show more

## 6.1.6. .status.conditions

Description
     conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'. 
Type
     `array`

## 6.1.7. .status.conditions[]

Description
     PersistentVolumeClaimCondition contains details about state of pvc 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastProbeTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastProbeTime is the time we probed the condition.   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastTransitionTime is the time the condition transitioned from one status to another.   
`message` |  `string` |  message is the human-readable message indicating details about last transition.   
`reason` |  `string` |  reason is a unique, this should be a short, machine understandable string that gives the reason for condition’s last transition. If it reports "Resizing" that means the underlying persistent volume is being resized.   
`status` |  `string` |  Status is the status of the condition. Can be True, False, Unknown. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=state%20of%20pvc-,conditions.status,-(string)%2C%20required>  
`type` |  `string` |  Type is the type of the condition. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=set%20to%20%27ResizeStarted%27.-,PersistentVolumeClaimCondition,-contains%20details%20about>  
Show more

## 6.1.8. .status.modifyVolumeStatus

Description
     ModifyVolumeStatus represents the status object of ControllerModifyVolume operation 
Type
     `object`
Required
    

  * `status`



Property| Type| Description  
---|---|---  
`status` |  `string` |  status is the status of the ControllerModifyVolume operation. It can be in any of following states: - Pending Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing. - InProgress InProgress indicates that the volume is being modified. - Infeasible Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.  Possible enum values: - `"InProgress"` InProgress indicates that the volume is being modified - `"Infeasible"` Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified - `"Pending"` Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing   
`targetVolumeAttributesClassName` |  `string` |  targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled   
Show more
