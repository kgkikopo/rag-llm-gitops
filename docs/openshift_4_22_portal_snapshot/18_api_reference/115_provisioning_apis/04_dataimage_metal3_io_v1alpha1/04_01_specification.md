# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  DataImageSpec defines the desired state of DataImage.   
`status` |  `object` |  DataImageStatus defines the observed state of DataImage.   
Show more

## 4.1.1. .spec

Description
     DataImageSpec defines the desired state of DataImage. 
Type
     `object`
Required
    

  * `url`



Property| Type| Description  
---|---|---  
`url` |  `string` |  Url is the address of the dataImage that we want to attach to a BareMetalHost   
Show more

## 4.1.2. .status

Description
     DataImageStatus defines the observed state of DataImage. 
Type
     `object`

Property| Type| Description  
---|---|---  
`attachedImage` |  `object` |  Currently attached DataImage   
`error` |  `object` |  Error count and message when attaching/detaching   
`lastReconciled` |  `string` |  Time of last reconciliation   
Show more

## 4.1.3. .status.attachedImage

Description
     Currently attached DataImage 
Type
     `object`
Required
    

  * `url`



Property| Type| Description  
---|---|---  
`url` |  `string` |   
Show more

## 4.1.4. .status.error

Description
     Error count and message when attaching/detaching 
Type
     `object`
Required
    

  * `count`
  * `message`



Property| Type| Description  
---|---|---  
`count` |  `integer` |   
`message` |  `string` |   
Show more
