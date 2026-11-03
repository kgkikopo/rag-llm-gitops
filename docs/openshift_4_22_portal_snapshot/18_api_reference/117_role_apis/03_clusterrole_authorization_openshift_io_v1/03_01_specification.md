# 3.1. Specification

Property| Type| Description  
---|---|---  
`aggregationRule` |  [`AggregationRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-AggregationRule) |  aggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.   
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`rules` |  `array` |  rules holds all the PolicyRules for this ClusterRole   
`rules[]` |  `object` |  PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.   
Show more

## 3.1.1. .rules

Description
     rules holds all the PolicyRules for this ClusterRole 
Type
     `array`

## 3.1.2. .rules[]

Description
     PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. 
Type
     `object`
Required
    

  * `verbs`
  * `resources`



Property| Type| Description  
---|---|---  
`apiGroups` |  `array (string)` |  apiGroups is the name of the APIGroup that contains the resources. If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed   
`attributeRestrictions` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  attributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error.   
`nonResourceURLs` |  `array (string)` |  NonResourceURLsSlice is a set of partial urls that a user should have access to. *s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different.   
`resourceNames` |  `array (string)` |  resourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed.   
`resources` |  `array (string)` |  resources is a list of resources this rule applies to. ResourceAll represents all resources.   
`verbs` |  `array (string)` |  verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule. VerbAll represents all kinds.   
Show more
