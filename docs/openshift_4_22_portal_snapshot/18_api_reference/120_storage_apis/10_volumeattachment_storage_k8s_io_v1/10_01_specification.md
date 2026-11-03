# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  VolumeAttachmentSpec is the specification of a VolumeAttachment request.   
`status` |  `object` |  VolumeAttachmentStatus is the status of a VolumeAttachment request.   
Show more

## 10.1.1. .spec

Description
     VolumeAttachmentSpec is the specification of a VolumeAttachment request. 
Type
     `object`
Required
    

  * `attacher`
  * `source`
  * `nodeName`



Property| Type| Description  
---|---|---  
`attacher` |  `string` |  attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().   
`nodeName` |  `string` |  nodeName represents the node that the volume should be attached to.   
`source` |  `object` |  VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set.   
Show more

## 10.1.2. .spec.source

Description
     VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`inlineVolumeSpec` |  [`PersistentVolumeSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PersistentVolumeSpec) |  inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod’s inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod’s inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature.   
`persistentVolumeName` |  `string` |  persistentVolumeName represents the name of the persistent volume to attach.   
Show more

## 10.1.3. .status

Description
     VolumeAttachmentStatus is the status of a VolumeAttachment request. 
Type
     `object`
Required
    

  * `attached`



Property| Type| Description  
---|---|---  
`attachError` |  `object` |  VolumeError captures an error encountered during a volume operation.   
`attached` |  `boolean` |  attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.   
`attachmentMetadata` |  `object (string)` |  attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.   
`detachError` |  `object` |  VolumeError captures an error encountered during a volume operation.   
Show more

## 10.1.4. .status.attachError

Description
     VolumeError captures an error encountered during a volume operation. 
Type
     `object`

Property| Type| Description  
---|---|---  
`errorCode` |  `integer` |  errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.  This is an optional, beta field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set.   
`message` |  `string` |  message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.   
`time` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  time represents the time the error was encountered.   
Show more

## 10.1.5. .status.detachError

Description
     VolumeError captures an error encountered during a volume operation. 
Type
     `object`

Property| Type| Description  
---|---|---  
`errorCode` |  `integer` |  errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.  This is an optional, beta field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set.   
`message` |  `string` |  message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.   
`time` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  time represents the time the error was encountered.   
Show more
