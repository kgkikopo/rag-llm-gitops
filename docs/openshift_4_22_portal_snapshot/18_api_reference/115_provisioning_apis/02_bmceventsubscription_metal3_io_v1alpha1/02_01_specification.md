# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |   
`status` |  `object` |   
Show more

## 2.1.1. .spec

Description
    
Type
     `object`

Property| Type| Description  
---|---|---  
`context` |  `string` |  Arbitrary user-provided context for the event   
`destination` |  `string` |  A webhook URL to send events to   
`hostName` |  `string` |  A reference to a BareMetalHost   
`httpHeadersRef` |  `object` |  A secret containing HTTP headers which should be passed along to the Destination when making a request   
Show more

## 2.1.2. .spec.httpHeadersRef

Description
     A secret containing HTTP headers which should be passed along to the Destination when making a request 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is unique within a namespace to reference a secret resource.   
`namespace` |  `string` |  namespace defines the space within which the secret name must be unique.   
Show more

## 2.1.3. .status

Description
    
Type
     `object`

Property| Type| Description  
---|---|---  
`error` |  `string` |   
`subscriptionID` |  `string` |   
Show more
