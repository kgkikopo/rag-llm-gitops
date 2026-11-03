# 11.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  OperatorGroupSpec is the spec for an OperatorGroup resource.   
`status` |  `object` |  OperatorGroupStatus is the status for an OperatorGroupResource.   
Show more

## 11.1.1. .spec

Description
     OperatorGroupSpec is the spec for an OperatorGroup resource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`selector` |  `object` |  Selector selects the OperatorGroup’s target namespaces.   
`serviceAccountName` |  `string` |  ServiceAccountName is the admin specified service account which will be used to deploy operator(s) in this operator group.   
`staticProvidedAPIs` |  `boolean` |  Static tells OLM not to update the OperatorGroup’s providedAPIs annotation   
`targetNamespaces` |  `array (string)` |  TargetNamespaces is an explicit set of namespaces to target. If it is set, Selector is ignored.   
`upgradeStrategy` |  `string` |  UpgradeStrategy defines the upgrade strategy for operators in the namespace. There are currently two supported upgrade strategies:  Default: OLM will only allow clusterServiceVersions to move to the replacing phase from the succeeded phase. This effectively means that OLM will not allow operators to move to the next version if an installation or upgrade has failed.  TechPreviewUnsafeFailForward: OLM will allow clusterServiceVersions to move to the replacing phase from the succeeded phase or from the failed phase. Additionally, OLM will generate new installPlans when a subscription references a failed installPlan and the catalog has been updated with a new upgrade for the existing set of operators.  WARNING: The TechPreviewUnsafeFailForward upgrade strategy is unsafe and may result in unexpected behavior or unrecoverable data loss unless you have deep understanding of the set of operators being managed in the namespace.   
Show more

## 11.1.2. .spec.selector

Description
     Selector selects the OperatorGroup’s target namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 11.1.3. .spec.selector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 11.1.4. .spec.selector.matchExpressions[]

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

## 11.1.5. .status

Description
     OperatorGroupStatus is the status for an OperatorGroupResource. 
Type
     `object`
Required
    

  * `lastUpdated`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  Conditions is an array of the OperatorGroup’s conditions.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`lastUpdated` |  `string` |  LastUpdated is a timestamp of the last time the OperatorGroup’s status was Updated.   
`namespaces` |  `array (string)` |  Namespaces is the set of target namespaces for the OperatorGroup.   
`serviceAccountRef` |  `object` |  ServiceAccountRef references the service account object specified.   
Show more

## 11.1.6. .status.conditions

Description
     Conditions is an array of the OperatorGroup’s conditions. 
Type
     `array`

## 11.1.7. .status.conditions[]

Description
     Condition contains details for one aspect of the current state of this API Resource. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `message`
  * `reason`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This may be an empty string.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more

## 11.1.8. .status.serviceAccountRef

Description
     ServiceAccountRef references the service account object specified. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more
