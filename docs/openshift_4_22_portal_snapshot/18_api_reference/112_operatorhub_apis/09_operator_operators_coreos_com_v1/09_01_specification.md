# 9.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  OperatorSpec defines the desired state of Operator   
`status` |  `object` |  OperatorStatus defines the observed state of an Operator and its components   
Show more

## 9.1.1. .spec

Description
     OperatorSpec defines the desired state of Operator 
Type
     `object`

## 9.1.2. .status

Description
     OperatorStatus defines the observed state of an Operator and its components 
Type
     `object`

Property| Type| Description  
---|---|---  
`components` |  `object` |  Components describes resources that compose the operator.   
Show more

## 9.1.3. .status.components

Description
     Components describes resources that compose the operator. 
Type
     `object`
Required
    

  * `labelSelector`



Property| Type| Description  
---|---|---  
`labelSelector` |  `object` |  LabelSelector is a label query over a set of resources used to select the operator’s components   
`refs` |  `array` |  Refs are a set of references to the operator’s component resources, selected with LabelSelector.   
`refs[]` |  `object` |  RichReference is a reference to a resource, enriched with its status conditions.   
Show more

## 9.1.4. .status.components.labelSelector

Description
     LabelSelector is a label query over a set of resources used to select the operator’s components 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 9.1.5. .status.components.labelSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 9.1.6. .status.components.labelSelector.matchExpressions[]

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

## 9.1.7. .status.components.refs

Description
     Refs are a set of references to the operator’s component resources, selected with LabelSelector. 
Type
     `array`

## 9.1.8. .status.components.refs[]

Description
     RichReference is a reference to a resource, enriched with its status conditions. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`conditions` |  `array` |  Conditions represents the latest state of the component.   
`conditions[]` |  `object` |  Condition represent the latest available observations of an component’s state.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 9.1.9. .status.components.refs[].conditions

Description
     Conditions represents the latest state of the component. 
Type
     `array`

## 9.1.10. .status.components.refs[].conditions[]

Description
     Condition represent the latest available observations of an component’s state. 
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  Last time the condition transitioned from one status to another.   
`lastUpdateTime` |  `string` |  Last time the condition was probed   
`message` |  `string` |  A human readable message indicating details about the transition.   
`reason` |  `string` |  The reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of condition.   
Show more
