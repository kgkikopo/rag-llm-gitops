# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of constraints of a scalable resource   
`status` |  `object` |  Most recently observed status of a scalable resource   
Show more

## 3.1.1. .spec

Description
     Specification of constraints of a scalable resource 
Type
     `object`
Required
    

  * `maxReplicas`
  * `minReplicas`
  * `scaleTargetRef`



Property| Type| Description  
---|---|---  
`maxReplicas` |  `integer` |  MaxReplicas constrains the maximal number of replicas of a scalable resource   
`minReplicas` |  `integer` |  MinReplicas constrains the minimal number of replicas of a scalable resource   
`scaleTargetRef` |  `object` |  ScaleTargetRef holds reference to a scalable resource   
Show more

## 3.1.2. .spec.scaleTargetRef

Description
     ScaleTargetRef holds reference to a scalable resource 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name specifies a name of an object, e.g. worker-us-east-1a. Scalable resources are expected to exist under a single namespace.   
Show more

## 3.1.3. .status

Description
     Most recently observed status of a scalable resource 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastTargetRef` |  `object` |  LastTargetRef holds reference to the recently observed scalable resource   
Show more

## 3.1.4. .status.lastTargetRef

Description
     LastTargetRef holds reference to the recently observed scalable resource 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name specifies a name of an object, e.g. worker-us-east-1a. Scalable resources are expected to exist under a single namespace.   
Show more
