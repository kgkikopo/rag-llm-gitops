# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of machine health check policy   
`status` |  `object` |  Most recently observed status of MachineHealthCheck resource   
Show more

## 8.1.1. .spec

Description
     Specification of machine health check policy 
Type
     `object`

Property| Type| Description  
---|---|---  
`maxUnhealthy` |  `integer-or-string` |  Any farther remediation is only allowed if at most "MaxUnhealthy" machines selected by "selector" are not healthy. Expects either a postive integer value or a percentage value. Percentage values must be positive whole numbers and are capped at 100%. Both 0 and 0% are valid and will block all remediation. Defaults to 100% if not set.   
`nodeStartupTimeout` |  `string` |  Machines older than this duration without a node will be considered to have failed and will be remediated. To prevent Machines without Nodes from being removed, disable startup checks by setting this value explicitly to "0". Expects an unsigned duration string of decimal numbers each with optional fraction and a unit suffix, eg "300ms", "1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".   
`remediationTemplate` |  `object` |  remediationTemplate is a reference to a remediation template provided by an infrastructure provider.  This field is completely optional, when filled, the MachineHealthCheck controller creates a new object from the template referenced and hands off remediation of the machine to a controller that lives outside of Machine API Operator.   
`selector` |  `object` |  Label selector to match machines whose health will be exercised. Note: An empty selector will match all machines.   
`unhealthyConditions` |  `array` |  unhealthyConditions contains a list of the conditions that determine whether a node is considered unhealthy. The conditions are combined in a logical OR, i.e. if any of the conditions is met, the node is unhealthy.   
`unhealthyConditions[]` |  `object` |  UnhealthyCondition represents a Node condition type and value with a timeout specified as a duration. When the named condition has been in the given status for at least the timeout value, a node is considered unhealthy.   
Show more

## 8.1.2. .spec.remediationTemplate

Description
    

remediationTemplate is a reference to a remediation template provided by an infrastructure provider. 

This field is completely optional, when filled, the MachineHealthCheck controller creates a new object from the template referenced and hands off remediation of the machine to a controller that lives outside of Machine API Operator. 

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

## 8.1.3. .spec.selector

Description
     Label selector to match machines whose health will be exercised. Note: An empty selector will match all machines. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 8.1.4. .spec.selector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 8.1.5. .spec.selector.matchExpressions[]

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

## 8.1.6. .spec.unhealthyConditions

Description
     unhealthyConditions contains a list of the conditions that determine whether a node is considered unhealthy. The conditions are combined in a logical OR, i.e. if any of the conditions is met, the node is unhealthy. 
Type
     `array`

## 8.1.7. .spec.unhealthyConditions[]

Description
     UnhealthyCondition represents a Node condition type and value with a timeout specified as a duration. When the named condition has been in the given status for at least the timeout value, a node is considered unhealthy. 
Type
     `object`

Property| Type| Description  
---|---|---  
`status` |  `string` |   
`timeout` |  `string` |  Expects an unsigned duration string of decimal numbers each with optional fraction and a unit suffix, eg "300ms", "1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".   
`type` |  `string` |   
Show more

## 8.1.8. .status

Description
     Most recently observed status of MachineHealthCheck resource 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions defines the current state of the MachineHealthCheck   
`conditions[]` |  `object` |  Condition defines an observation of a Machine API resource operational state.   
`currentHealthy` |  `integer` |  total number of machines counted by this machine health check   
`expectedMachines` |  `integer` |  total number of machines counted by this machine health check   
`remediationsAllowed` |  `integer` |  remediationsAllowed is the number of further remediations allowed by this machine health check before maxUnhealthy short circuiting will be applied   
Show more

## 8.1.9. .status.conditions

Description
     conditions defines the current state of the MachineHealthCheck 
Type
     `array`

## 8.1.10. .status.conditions[]

Description
     Condition defines an observation of a Machine API resource operational state. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  A human readable message indicating details about the transition. This field may be empty.   
`reason` |  `string` |  The reason for the condition’s last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may not be empty.   
`severity` |  `string` |  severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important.   
Show more
