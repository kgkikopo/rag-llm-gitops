# 12.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  SelfSubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set   
`status` |  `object` |  SubjectAccessReviewStatus   
Show more

## 12.1.1. .spec

Description
     SelfSubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set 
Type
     `object`

Property| Type| Description  
---|---|---  
`nonResourceAttributes` |  `object` |  NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface   
`resourceAttributes` |  `object` |  ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface   
Show more

## 12.1.2. .spec.nonResourceAttributes

Description
     NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface 
Type
     `object`

Property| Type| Description  
---|---|---  
`path` |  `string` |  Path is the URL path of the request   
`verb` |  `string` |  Verb is the standard HTTP verb   
Show more

## 12.1.3. .spec.resourceAttributes

Description
     ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface 
Type
     `object`

Property| Type| Description  
---|---|---  
`fieldSelector` |  `object` |  FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to * ensure rawSelector and requirements are not both set * consider the requirements field if set * not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the *SubjectAccessReview endpoints of the kube-apiserver: * If rawSelector is empty and requirements are empty, the request is not limited. * If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. * If rawSelector is empty and requirements are present, the requirements should be honored * If rawSelector is present and requirements are present, the request is invalid.   
`group` |  `string` |  Group is the API Group of the Resource. "*" means all.   
`labelSelector` |  `object` |  LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to * ensure rawSelector and requirements are not both set * consider the requirements field if set * not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the *SubjectAccessReview endpoints of the kube-apiserver: * If rawSelector is empty and requirements are empty, the request is not limited. * If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. * If rawSelector is empty and requirements are present, the requirements should be honored * If rawSelector is present and requirements are present, the request is invalid.   
`name` |  `string` |  Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.   
`namespace` |  `string` |  Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview   
`resource` |  `string` |  Resource is one of the existing resource types. "*" means all.   
`subresource` |  `string` |  Subresource is one of the existing resource types. "" means none.   
`verb` |  `string` |  Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "*" means all.   
`version` |  `string` |  Version is the API Version of the Resource. "*" means all.   
Show more

## 12.1.4. .spec.resourceAttributes.fieldSelector

Description
     FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to * ensure rawSelector and requirements are not both set * consider the requirements field if set * not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the *SubjectAccessReview endpoints of the kube-apiserver: * If rawSelector is empty and requirements are empty, the request is not limited. * If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. * If rawSelector is empty and requirements are present, the requirements should be honored * If rawSelector is present and requirements are present, the request is invalid. 
Type
     `object`

Property| Type| Description  
---|---|---  
`rawSelector` |  `string` |  rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.   
`requirements` |  [`array (FieldSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-FieldSelectorRequirement) |  requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.   
Show more

## 12.1.5. .spec.resourceAttributes.labelSelector

Description
     LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to * ensure rawSelector and requirements are not both set * consider the requirements field if set * not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the *SubjectAccessReview endpoints of the kube-apiserver: * If rawSelector is empty and requirements are empty, the request is not limited. * If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. * If rawSelector is empty and requirements are present, the requirements should be honored * If rawSelector is present and requirements are present, the request is invalid. 
Type
     `object`

Property| Type| Description  
---|---|---  
`rawSelector` |  `string` |  rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.   
`requirements` |  [`array (LabelSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement) |  requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.   
Show more

## 12.1.6. .status

Description
     SubjectAccessReviewStatus 
Type
     `object`
Required
    

  * `allowed`



Property| Type| Description  
---|---|---  
`allowed` |  `boolean` |  Allowed is required. True if the action would be allowed, false otherwise.   
`denied` |  `boolean` |  Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.   
`evaluationError` |  `string` |  EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.   
`reason` |  `string` |  Reason is optional. It indicates why a request was allowed or denied.   
Show more
