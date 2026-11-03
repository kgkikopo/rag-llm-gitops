# 1.77. io.k8s.api.core.v1.LocalObjectReference schema

Description
     LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. 
Type
     `object`

## 1.77.1. Schema

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more
