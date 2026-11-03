# 9.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ResourceQuotaSpec defines the desired hard limits to enforce for Quota.   
`status` |  `object` |  ResourceQuotaStatus defines the enforced hard limits and observed use.   
Show more

## 9.1.1. .spec

Description
     ResourceQuotaSpec defines the desired hard limits to enforce for Quota. 
Type
     `object`

Property| Type| Description  
---|---|---  
`hard` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/>  
`scopeSelector` |  `object` |  A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.   
`scopes` |  `array (string)` |  A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.   
Show more

## 9.1.2. .spec.scopeSelector

Description
     A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  A list of scope selector requirements by scope of the resources.   
`matchExpressions[]` |  `object` |  A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.   
Show more

## 9.1.3. .spec.scopeSelector.matchExpressions

Description
     A list of scope selector requirements by scope of the resources. 
Type
     `array`

## 9.1.4. .spec.scopeSelector.matchExpressions[]

Description
     A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values. 
Type
     `object`
Required
    

  * `scopeName`
  * `operator`



Property| Type| Description  
---|---|---  
`operator` |  `string` |  Represents a scope’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.  Possible enum values: - `"DoesNotExist"` \- `"Exists"` \- `"In"` \- `"NotIn"`  
`scopeName` |  `string` |  The name of the scope that the selector applies to.  Possible enum values: - `"BestEffort"` Match all pod objects that have best effort quality of service - `"CrossNamespacePodAffinity"` Match all pod objects that have cross-namespace pod (anti)affinity mentioned. - `"NotBestEffort"` Match all pod objects that do not have best effort quality of service - `"NotTerminating"` Match all pod objects where spec.activeDeadlineSeconds is nil - `"PriorityClass"` Match all pod objects that have priority class mentioned - `"Terminating"` Match all pod objects where spec.activeDeadlineSeconds >=0 - `"VolumeAttributesClass"` Match all pvc objects that have volume attributes class mentioned.   
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
Show more

## 9.1.5. .status

Description
     ResourceQuotaStatus defines the enforced hard limits and observed use. 
Type
     `object`

Property| Type| Description  
---|---|---  
`hard` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/>  
`used` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Used is the current observed total usage of the resource in the namespace.   
Show more
