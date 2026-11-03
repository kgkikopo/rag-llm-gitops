# 1.92. io.k8s.api.core.v1.ResourceQuotaSpec schema

Description
     ResourceQuotaSpec defines the desired hard limits to enforce for Quota. 
Type
     `object`

## 1.92.1. Schema

Property| Type| Description  
---|---|---  
`hard` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") |  hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/>  
`scopeSelector` |  `ScopeSelector` |  scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.   
`scopes` |  `array (string)` |  A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.   
Show more
