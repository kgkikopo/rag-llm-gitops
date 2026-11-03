# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`conditions` |  `array` |  List of component conditions observed   
`conditions[]` |  `object` |  Information about the condition of a component.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
Show more

## 4.1.1. .conditions

Description
     List of component conditions observed 
Type
     `array`

## 4.1.2. .conditions[]

Description
     Information about the condition of a component. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`error` |  `string` |  Condition error code for a component. For example, a health check error code.   
`message` |  `string` |  Message about the condition for a component. For example, information about a health check.   
`status` |  `string` |  Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown".   
`type` |  `string` |  Type of condition for a component. Valid value: "Healthy"   
Show more
