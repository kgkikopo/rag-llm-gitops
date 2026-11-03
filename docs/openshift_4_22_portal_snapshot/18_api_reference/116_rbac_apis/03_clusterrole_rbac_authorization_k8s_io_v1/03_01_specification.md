# 3.1. Specification

Property| Type| Description  
---|---|---  
`aggregationRule` |  `object` |  AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole   
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata.   
`rules` |  `array` |  Rules holds all the PolicyRules for this ClusterRole   
`rules[]` |  `object` |  PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.   
Show more

## 3.1.1. .aggregationRule

Description
     AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole 
Type
     `object`

Property| Type| Description  
---|---|---  
`clusterRoleSelectors` |  [`array (LabelSelector)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole’s permissions will be added   
Show more

## 3.1.2. .rules

Description
     Rules holds all the PolicyRules for this ClusterRole 
Type
     `array`

## 3.1.3. .rules[]

Description
     PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. 
Type
     `object`
Required
    

  * `verbs`



Property| Type| Description  
---|---|---  
`apiGroups` |  `array (string)` |  APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups.   
`nonResourceURLs` |  `array (string)` |  NonResourceURLs is a set of partial urls that a user should have access to. *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both.   
`resourceNames` |  `array (string)` |  ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed.   
`resources` |  `array (string)` |  Resources is a list of resources this rule applies to. '*' represents all resources.   
`verbs` |  `array (string)` |  Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '*' represents all verbs.   
Show more
