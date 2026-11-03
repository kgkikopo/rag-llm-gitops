# 21.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  IPAddressSpec describe the attributes in an IP Address.   
Show more

## 21.1.1. .spec

Description
     IPAddressSpec describe the attributes in an IP Address. 
Type
     `object`
Required
    

  * `parentRef`



Property| Type| Description  
---|---|---  
`parentRef` |  `object` |  ParentReference describes a reference to a parent object.   
Show more

## 21.1.2. .spec.parentRef

Description
     ParentReference describes a reference to a parent object. 
Type
     `object`
Required
    

  * `resource`
  * `name`



Property| Type| Description  
---|---|---  
`group` |  `string` |  Group is the group of the object being referenced.   
`name` |  `string` |  Name is the name of the object being referenced.   
`namespace` |  `string` |  Namespace is the namespace of the object being referenced.   
`resource` |  `string` |  Resource is the resource of the object being referenced.   
Show more
