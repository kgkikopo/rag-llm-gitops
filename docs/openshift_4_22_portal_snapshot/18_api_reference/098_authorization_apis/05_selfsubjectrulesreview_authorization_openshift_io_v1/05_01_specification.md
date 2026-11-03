# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  SelfSubjectRulesReviewSpec adds information about how to conduct the check   
`status` |  `object` |  SubjectRulesReviewStatus is contains the result of a rules check   
Show more

## 5.1.1. .spec

Description
     SelfSubjectRulesReviewSpec adds information about how to conduct the check 
Type
     `object`
Required
    

  * `scopes`



Property| Type| Description  
---|---|---  
`scopes` |  `array (string)` |  scopes to use for the evaluation. Empty means "use the unscoped (full) permissions of the user/groups". Nil means "use the scopes on this request".   
Show more

## 5.1.2. .status

Description
     SubjectRulesReviewStatus is contains the result of a rules check 
Type
     `object`

Property| Type| Description  
---|---|---  
`evaluationError` |  `string` |  evaluationError can appear in combination with Rules. It means some error happened during evaluation that may have prevented additional rules from being populated.   
`rules` |  `array` |  rules is the list of rules (no particular sort) that are allowed for the subject   
`rules[]` |  `object` |  PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.   
Show more

## 5.1.3. .status.rules

Description
     rules is the list of rules (no particular sort) that are allowed for the subject 
Type
     `array`

## 5.1.4. .status.rules[]

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
