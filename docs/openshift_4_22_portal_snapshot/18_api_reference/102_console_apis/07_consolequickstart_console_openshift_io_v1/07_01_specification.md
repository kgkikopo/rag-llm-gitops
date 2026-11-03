# 7.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ConsoleQuickStartSpec is the desired quick start configuration.   
Show more

## 7.1.1. .spec

Description
     ConsoleQuickStartSpec is the desired quick start configuration. 
Type
     `object`
Required
    

  * `description`
  * `displayName`
  * `durationMinutes`
  * `introduction`
  * `tasks`



Property| Type| Description  
---|---|---  
`accessReviewResources` |  `array` |  accessReviewResources contains a list of resources that the user’s access will be reviewed against in order for the user to complete the Quick Start. The Quick Start will be hidden if any of the access reviews fail.   
`accessReviewResources[]` |  `object` |  ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface   
`conclusion` |  `string` |  conclusion sums up the Quick Start and suggests the possible next steps. (includes markdown)   
`description` |  `string` |  description is the description of the Quick Start. (includes markdown)   
`displayName` |  `string` |  displayName is the display name of the Quick Start.   
`durationMinutes` |  `integer` |  durationMinutes describes approximately how many minutes it will take to complete the Quick Start.   
`icon` |  `string` |  icon is a base64 encoded image that will be displayed beside the Quick Start display name. The icon should be an vector image for easy scaling. The size of the icon should be 40x40.   
`introduction` |  `string` |  introduction describes the purpose of the Quick Start. (includes markdown)   
`nextQuickStart` |  `array (string)` |  nextQuickStart is a list of the following Quick Starts, suggested for the user to try.   
`prerequisites` |  `array (string)` |  prerequisites contains all prerequisites that need to be met before taking a Quick Start. (includes markdown)   
`tags` |  `array (string)` |  tags is a list of strings that describe the Quick Start.   
`tasks` |  `array` |  tasks is the list of steps the user has to perform to complete the Quick Start.   
`tasks[]` |  `object` |  ConsoleQuickStartTask is a single step in a Quick Start.   
Show more

## 7.1.2. .spec.accessReviewResources

Description
     accessReviewResources contains a list of resources that the user’s access will be reviewed against in order for the user to complete the Quick Start. The Quick Start will be hidden if any of the access reviews fail. 
Type
     `array`

## 7.1.3. .spec.accessReviewResources[]

Description
     ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface 
Type
     `object`

Property| Type| Description  
---|---|---  
`fieldSelector` |  `object` |  fieldSelector describes the limitation on access based on field. It can only limit access, not broaden it.   
`group` |  `string` |  Group is the API Group of the Resource. "*" means all.   
`labelSelector` |  `object` |  labelSelector describes the limitation on access based on labels. It can only limit access, not broaden it.   
`name` |  `string` |  Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.   
`namespace` |  `string` |  Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview   
`resource` |  `string` |  Resource is one of the existing resource types. "*" means all.   
`subresource` |  `string` |  Subresource is one of the existing resource types. "" means none.   
`verb` |  `string` |  Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "*" means all.   
`version` |  `string` |  Version is the API Version of the Resource. "*" means all.   
Show more

## 7.1.4. .spec.accessReviewResources[].fieldSelector

Description
     fieldSelector describes the limitation on access based on field. It can only limit access, not broaden it. 
Type
     `object`

Property| Type| Description  
---|---|---  
`rawSelector` |  `string` |  rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.   
`requirements` |  `array` |  requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.   
`requirements[]` |  `object` |  FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values.   
Show more

## 7.1.5. .spec.accessReviewResources[].fieldSelector.requirements

Description
     requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. 
Type
     `array`

## 7.1.6. .spec.accessReviewResources[].fieldSelector.requirements[]

Description
     FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the field selector key that the requirement applies to.   
`operator` |  `string` |  operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future.   
`values` |  `array (string)` |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty.   
Show more

## 7.1.7. .spec.accessReviewResources[].labelSelector

Description
     labelSelector describes the limitation on access based on labels. It can only limit access, not broaden it. 
Type
     `object`

Property| Type| Description  
---|---|---  
`rawSelector` |  `string` |  rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.   
`requirements` |  `array` |  requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.   
`requirements[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
Show more

## 7.1.8. .spec.accessReviewResources[].labelSelector.requirements

Description
     requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. 
Type
     `array`

## 7.1.9. .spec.accessReviewResources[].labelSelector.requirements[]

Description
     A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the label key that the selector applies to.   
`operator` |  `string` |  operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`values` |  `array (string)` |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
Show more

## 7.1.10. .spec.tasks

Description
     tasks is the list of steps the user has to perform to complete the Quick Start. 
Type
     `array`

## 7.1.11. .spec.tasks[]

Description
     ConsoleQuickStartTask is a single step in a Quick Start. 
Type
     `object`
Required
    

  * `description`
  * `title`



Property| Type| Description  
---|---|---  
`description` |  `string` |  description describes the steps needed to complete the task. (includes markdown)   
`review` |  `object` |  review contains instructions to validate the task is complete. The user will select 'Yes' or 'No'. using a radio button, which indicates whether the step was completed successfully.   
`summary` |  `object` |  summary contains information about the passed step.   
`title` |  `string` |  title describes the task and is displayed as a step heading.   
Show more

## 7.1.12. .spec.tasks[].review

Description
     review contains instructions to validate the task is complete. The user will select 'Yes' or 'No'. using a radio button, which indicates whether the step was completed successfully. 
Type
     `object`
Required
    

  * `failedTaskHelp`
  * `instructions`



Property| Type| Description  
---|---|---  
`failedTaskHelp` |  `string` |  failedTaskHelp contains suggestions for a failed task review and is shown at the end of task. (includes markdown)   
`instructions` |  `string` |  instructions contains steps that user needs to take in order to validate his work after going through a task. (includes markdown)   
Show more

## 7.1.13. .spec.tasks[].summary

Description
     summary contains information about the passed step. 
Type
     `object`
Required
    

  * `failed`
  * `success`



Property| Type| Description  
---|---|---  
`failed` |  `string` |  failed briefly describes the unsuccessfully passed task. (includes markdown)   
`success` |  `string` |  success describes the succesfully passed task.   
Show more
