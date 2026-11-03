# 1.102. io.k8s.api.core.v1.TypedLocalObjectReference schema

Description
     TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace. 
Type
     `object`
Required
    

  * `kind`
  * `name`



## 1.102.1. Schema

Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
Show more
