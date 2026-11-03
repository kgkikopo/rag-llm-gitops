# 13.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview.   
`status` |  `object` |  SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it’s safe to assume the subject has that permission, even if that list is incomplete.   
Show more

## 13.1.1. .spec

Description
     SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview. 
Type
     `object`

Property| Type| Description  
---|---|---  
`namespace` |  `string` |  Namespace to evaluate rules for. Required.   
Show more

## 13.1.2. .status

Description
     SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it’s safe to assume the subject has that permission, even if that list is incomplete. 
Type
     `object`
Required
    

  * `resourceRules`
  * `nonResourceRules`
  * `incomplete`



Property| Type| Description  
---|---|---  
`evaluationError` |  `string` |  EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn’t support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.   
`incomplete` |  `boolean` |  Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn’t support rules evaluation.   
`nonResourceRules` |  `array` |  NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete.   
`nonResourceRules[]` |  `object` |  NonResourceRule holds information that describes a rule for the non-resource   
`resourceRules` |  `array` |  ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete.   
`resourceRules[]` |  `object` |  ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete.   
Show more

## 13.1.3. .status.nonResourceRules

Description
     NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete. 
Type
     `array`

## 13.1.4. .status.nonResourceRules[]

Description
     NonResourceRule holds information that describes a rule for the non-resource 
Type
     `object`
Required
    

  * `verbs`



Property| Type| Description  
---|---|---  
`nonResourceURLs` |  `array (string)` |  NonResourceURLs is a set of partial urls that a user should have access to. **s are allowed, but only as the full, final step in the path. "** " means all.   
`verbs` |  `array (string)` |  Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options. "*" means all.   
Show more

## 13.1.5. .status.resourceRules

Description
     ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete. 
Type
     `array`

## 13.1.6. .status.resourceRules[]

Description
     ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete. 
Type
     `object`
Required
    

  * `verbs`



Property| Type| Description  
---|---|---  
`apiGroups` |  `array (string)` |  APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "*" means all.   
`resourceNames` |  `array (string)` |  ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. "*" means all.   
`resources` |  `array (string)` |  Resources is a list of resources this rule applies to. "**" means all in the specified apiGroups. "** /foo" represents the subresource 'foo' for all resources in the specified apiGroups.   
`verbs` |  `array (string)` |  Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy. "*" means all.   
Show more
