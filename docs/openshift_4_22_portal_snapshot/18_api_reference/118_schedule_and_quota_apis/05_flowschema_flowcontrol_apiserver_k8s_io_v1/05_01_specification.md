# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  `metadata` is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  FlowSchemaSpec describes how the FlowSchema’s specification looks like.   
`status` |  `object` |  FlowSchemaStatus represents the current state of a FlowSchema.   
Show more

## 5.1.1. .spec

Description
     FlowSchemaSpec describes how the FlowSchema’s specification looks like. 
Type
     `object`
Required
    

  * `priorityLevelConfiguration`



Property| Type| Description  
---|---|---  
`distinguisherMethod` |  `object` |  FlowDistinguisherMethod specifies the method of a flow distinguisher.   
`matchingPrecedence` |  `integer` |  `matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence. Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default.   
`priorityLevelConfiguration` |  `object` |  PriorityLevelConfigurationReference contains information that points to the "request-priority" being used.   
`rules` |  `array` |  `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema.   
`rules[]` |  `object` |  PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request.   
Show more

## 5.1.2. .spec.distinguisherMethod

Description
     FlowDistinguisherMethod specifies the method of a flow distinguisher. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`type` |  `string` |  `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required.   
Show more

## 5.1.3. .spec.priorityLevelConfiguration

Description
     PriorityLevelConfigurationReference contains information that points to the "request-priority" being used. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  `name` is the name of the priority level configuration being referenced Required.   
Show more

## 5.1.4. .spec.rules

Description
     `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. 
Type
     `array`

## 5.1.5. .spec.rules[]

Description
     PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request. 
Type
     `object`
Required
    

  * `subjects`



Property| Type| Description  
---|---|---  
`nonResourceRules` |  `array` |  `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.   
`nonResourceRules[]` |  `object` |  NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request.   
`resourceRules` |  `array` |  `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.   
`resourceRules[]` |  `object` |  ResourcePolicyRule is a predicate that matches some resource requests, testing the request’s verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request’s namespace.   
`subjects` |  `array` |  subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required.   
`subjects[]` |  `object` |  Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.   
Show more

## 5.1.6. .spec.rules[].nonResourceRules

Description
     `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL. 
Type
     `array`

## 5.1.7. .spec.rules[].nonResourceRules[]

Description
     NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request. 
Type
     `object`
Required
    

  * `verbs`
  * `nonResourceURLs`



Property| Type| Description  
---|---|---  
`nonResourceURLs` |  `array (string)` |  `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example: - "/healthz" is legal - "/hea*" is illegal - "/hea" is legal but matches nothing - "/hea/**" also matches nothing - "/healthz/** " matches all per-component health checks. "*" matches all non-resource urls. if it is present, it must be the only entry. Required.   
`verbs` |  `array (string)` |  `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required.   
Show more

## 5.1.8. .spec.rules[].resourceRules

Description
     `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty. 
Type
     `array`

## 5.1.9. .spec.rules[].resourceRules[]

Description
     ResourcePolicyRule is a predicate that matches some resource requests, testing the request’s verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request’s namespace. 
Type
     `object`
Required
    

  * `verbs`
  * `apiGroups`
  * `resources`



Property| Type| Description  
---|---|---  
`apiGroups` |  `array (string)` |  `apiGroups` is a list of matching API groups and may not be empty. "*" matches all API groups and, if present, must be the only entry. Required.   
`clusterScope` |  `boolean` |  `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.   
`namespaces` |  `array (string)` |  `namespaces` is a list of target namespaces that restricts matches. A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "**". Note that "** " matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.   
`resources` |  `array (string)` |  `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource. For example, [ "services", "nodes/status" ]. This list may not be empty. "*" matches all resources and, if present, must be the only entry. Required.   
`verbs` |  `array (string)` |  `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs and, if present, must be the only entry. Required.   
Show more

## 5.1.10. .spec.rules[].subjects

Description
     subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required. 
Type
     `array`

## 5.1.11. .spec.rules[].subjects[]

Description
     Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account. 
Type
     `object`
Required
    

  * `kind`



Property| Type| Description  
---|---|---  
`group` |  `object` |  GroupSubject holds detailed information for group-kind subject.   
`kind` |  `string` |  `kind` indicates which one of the other fields is non-empty. Required   
`serviceAccount` |  `object` |  ServiceAccountSubject holds detailed information for service-account-kind subject.   
`user` |  `object` |  UserSubject holds detailed information for user-kind subject.   
Show more

## 5.1.12. .spec.rules[].subjects[].group

Description
     GroupSubject holds detailed information for group-kind subject. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the user group that matches, or "*" to match all user groups. See <https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go> for some well-known group names. Required.   
Show more

## 5.1.13. .spec.rules[].subjects[].serviceAccount

Description
     ServiceAccountSubject holds detailed information for service-account-kind subject. 
Type
     `object`
Required
    

  * `namespace`
  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  `name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required.   
`namespace` |  `string` |  `namespace` is the namespace of matching ServiceAccount objects. Required.   
Show more

## 5.1.14. .spec.rules[].subjects[].user

Description
     UserSubject holds detailed information for user-kind subject. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  `name` is the username that matches, or "*" to match all usernames. Required.   
Show more

## 5.1.15. .status

Description
     FlowSchemaStatus represents the current state of a FlowSchema. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  `conditions` is a list of the current states of FlowSchema.   
`conditions[]` |  `object` |  FlowSchemaCondition describes conditions for a FlowSchema.   
Show more

## 5.1.16. .status.conditions

Description
     `conditions` is a list of the current states of FlowSchema. 
Type
     `array`

## 5.1.17. .status.conditions[]

Description
     FlowSchemaCondition describes conditions for a FlowSchema. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  `lastTransitionTime` is the last time the condition transitioned from one status to another.   
`message` |  `string` |  `message` is a human-readable message indicating details about last transition.   
`reason` |  `string` |  `reason` is a unique, one-word, CamelCase reason for the condition’s last transition.   
`status` |  `string` |  `status` is the status of the condition. Can be True, False, Unknown. Required.   
`type` |  `string` |  `type` is the type of the condition. Required.   
Show more
