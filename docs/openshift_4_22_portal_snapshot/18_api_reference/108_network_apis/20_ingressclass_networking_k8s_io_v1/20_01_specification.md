# 20.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  IngressClassSpec provides information about the class of an Ingress.   
Show more

## 20.1.1. .spec

Description
     IngressClassSpec provides information about the class of an Ingress. 
Type
     `object`

Property| Type| Description  
---|---|---  
`controller` |  `string` |  controller refers to the name of the controller that should handle this class. This allows for different "flavors" that are controlled by the same controller. For example, you may have different parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. "acme.io/ingress-controller". This field is immutable.   
`parameters` |  `object` |  IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource.   
Show more

## 20.1.2. .spec.parameters

Description
     IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  kind is the type of resource being referenced.   
`name` |  `string` |  name is the name of resource being referenced.   
`namespace` |  `string` |  namespace is the namespace of the resource being referenced. This field is required when scope is set to "Namespace" and must be unset when scope is set to "Cluster".   
`scope` |  `string` |  scope represents if this refers to a cluster or namespace scoped resource. This may be set to "Cluster" (default) or "Namespace".   
Show more
