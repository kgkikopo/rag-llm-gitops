# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of permitted ImageStreams   
`status` |  ``  |  Status of the TestExtensionAdmission   
Show more

## 5.1.1. .spec

Description
     Specification of permitted ImageStreams 
Type
     `object`
Required
    

  * `permit`



Property| Type| Description  
---|---|---  
`permit` |  `array (string)` |  List of permitted ImageStream patterns in format "namespace/imagestream". Each segment must be either "**" (wildcard) or a valid name (no embedded wildcards). Examples - "openshift/** ", "**/** ", "namespace/stream"   
Show more
