# 30.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Spec defines the desired state of ReferenceGrant.   
Show more

## 30.1.1. .spec

Description
     Spec defines the desired state of ReferenceGrant. 
Type
     `object`
Required
    

  * `from`
  * `to`



Property| Type| Description  
---|---|---  
`from` |  `array` |  From describes the trusted namespaces and kinds that can reference the resources described in "To". Each entry in this list MUST be considered to be an additional place that references can be valid from, or to put this another way, entries MUST be combined using OR.  Support: Core   
`from[]` |  `object` |  ReferenceGrantFrom describes trusted namespaces and kinds.   
`to` |  `array` |  To describes the resources that may be referenced by the resources described in "From". Each entry in this list MUST be considered to be an additional place that references can be valid to, or to put this another way, entries MUST be combined using OR.  Support: Core   
`to[]` |  `object` |  ReferenceGrantTo describes what Kinds are allowed as targets of the references.   
Show more

## 30.1.2. .spec.from

Description
    

From describes the trusted namespaces and kinds that can reference the resources described in "To". Each entry in this list MUST be considered to be an additional place that references can be valid from, or to put this another way, entries MUST be combined using OR. 

Support: Core 

Type
     `array`

## 30.1.3. .spec.from[]

Description
     ReferenceGrantFrom describes trusted namespaces and kinds. 
Type
     `object`
Required
    

  * `group`
  * `kind`
  * `namespace`



Property| Type| Description  
---|---|---  
`group` |  `string` |  Group is the group of the referent. When empty, the Kubernetes core API group is inferred.  Support: Core   
`kind` |  `string` |  Kind is the kind of the referent. Although implementations may support additional resources, the following types are part of the "Core" support level for this field.  When used to permit a SecretObjectReference:  * Gateway  When used to permit a BackendObjectReference:  * GRPCRoute * HTTPRoute * TCPRoute * TLSRoute * UDPRoute   
`namespace` |  `string` |  Namespace is the namespace of the referent.  Support: Core   
Show more

## 30.1.4. .spec.to

Description
    

To describes the resources that may be referenced by the resources described in "From". Each entry in this list MUST be considered to be an additional place that references can be valid to, or to put this another way, entries MUST be combined using OR. 

Support: Core 

Type
     `array`

## 30.1.5. .spec.to[]

Description
     ReferenceGrantTo describes what Kinds are allowed as targets of the references. 
Type
     `object`
Required
    

  * `group`
  * `kind`



Property| Type| Description  
---|---|---  
`group` |  `string` |  Group is the group of the referent. When empty, the Kubernetes core API group is inferred.  Support: Core   
`kind` |  `string` |  Kind is the kind of the referent. Although implementations may support additional resources, the following types are part of the "Core" support level for this field:  * Secret when used to permit a SecretObjectReference * Service when used to permit a BackendObjectReference   
`name` |  `string` |  Name is the name of the referent. When unspecified, this policy refers to all resources of the specified Group and Kind in the local namespace.   
Show more
