# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec defines the desired quota   
`status` |  `object` |  status defines the actual enforced quota and its current usage   
Show more

## 3.1.1. .spec

Description
     spec defines the desired quota 
Type
     `object`
Required
    

  * `quota`
  * `selector`



Property| Type| Description  
---|---|---  
`quota` |  `object` |  quota defines the desired quota   
`selector` |  `object` |  selector is the selector used to match projects. It should only select active projects on the scale of dozens (though it can select many more less active projects). These projects will contend on object creation through this resource.   
Show more

## 3.1.2. .spec.quota

Description
     quota defines the desired quota 
Type
     `object`

Property| Type| Description  
---|---|---  
`hard` |  `integer-or-string` |  hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/>  
`scopeSelector` |  `object` |  scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.   
`scopes` |  `array (string)` |  A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.   
Show more

## 3.1.3. .spec.quota.scopeSelector

Description
     scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  A list of scope selector requirements by scope of the resources.   
`matchExpressions[]` |  `object` |  A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.   
Show more

## 3.1.4. .spec.quota.scopeSelector.matchExpressions

Description
     A list of scope selector requirements by scope of the resources. 
Type
     `array`

## 3.1.5. .spec.quota.scopeSelector.matchExpressions[]

Description
     A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values. 
Type
     `object`
Required
    

  * `operator`
  * `scopeName`



Property| Type| Description  
---|---|---  
`operator` |  `string` |  Represents a scope’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.   
`scopeName` |  `string` |  The name of the scope that the selector applies to.   
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
Show more

## 3.1.6. .spec.selector

Description
     selector is the selector used to match projects. It should only select active projects on the scale of dozens (though it can select many more less active projects). These projects will contend on object creation through this resource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`annotations` |  `undefined (string)` |  AnnotationSelector is used to select projects by annotation.   
`labels` |  ``  |  LabelSelector is used to select projects by label.   
Show more

## 3.1.7. .status

Description
     status defines the actual enforced quota and its current usage 
Type
     `object`
Required
    

  * `total`



Property| Type| Description  
---|---|---  
`namespaces` |  ``  |  namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project.   
`total` |  `object` |  total defines the actual enforced quota and its current usage across all projects   
Show more

## 3.1.8. .status.total

Description
     total defines the actual enforced quota and its current usage across all projects 
Type
     `object`

Property| Type| Description  
---|---|---  
`hard` |  `integer-or-string` |  Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/>  
`used` |  `integer-or-string` |  Used is the current observed total usage of the resource in the namespace.   
Show more
