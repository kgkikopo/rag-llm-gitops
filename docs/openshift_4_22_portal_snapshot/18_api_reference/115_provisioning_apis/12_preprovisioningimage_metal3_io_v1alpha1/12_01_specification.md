# 12.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  PreprovisioningImageSpec defines the desired state of PreprovisioningImage.   
`status` |  `object` |  PreprovisioningImageStatus defines the observed state of PreprovisioningImage.   
Show more

## 12.1.1. .spec

Description
     PreprovisioningImageSpec defines the desired state of PreprovisioningImage. 
Type
     `object`

Property| Type| Description  
---|---|---  
`acceptFormats` |  `array (string)` |  acceptFormats is a list of acceptable image formats.   
`architecture` |  `string` |  architecture is the processor architecture for which to build the image.   
`networkDataName` |  `string` |  networkDataName is the name of a Secret in the local namespace that contains network data to build in to the image.   
Show more

## 12.1.2. .status

Description
     PreprovisioningImageStatus defines the observed state of PreprovisioningImage. 
Type
     `object`

Property| Type| Description  
---|---|---  
`architecture` |  `string` |  architecture is the processor architecture for which the image is built   
`conditions` |  `array` |  conditions describe the state of the built image   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`extraKernelParams` |  `string` |  extraKernelParams is a string with extra parameters to pass to the kernel when booting the image over network. Only makes sense for initrd images.   
`format` |  `string` |  format is the type of image that is available at the download url: either iso or initrd.   
`imageUrl` |  `string` |  imageUrl is the URL from which the built image can be downloaded.   
`kernelUrl` |  `string` |  kernelUrl is the URL from which the kernel of the image can be downloaded. Only makes sense for initrd images.   
`networkData` |  `object` |  networkData is a reference to the version of the Secret containing the network data used to build the image.   
Show more

## 12.1.3. .status.conditions

Description
     conditions describe the state of the built image 
Type
     `array`

## 12.1.4. .status.conditions[]

Description
     Condition contains details for one aspect of the current state of this API Resource. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `message`
  * `reason`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This may be an empty string.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more

## 12.1.5. .status.networkData

Description
     networkData is a reference to the version of the Secret containing the network data used to build the image. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |   
`version` |  `string` |   
Show more
