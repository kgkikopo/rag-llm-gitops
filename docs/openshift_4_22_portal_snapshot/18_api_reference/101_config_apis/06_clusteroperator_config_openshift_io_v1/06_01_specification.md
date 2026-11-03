# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds configuration that could apply to any operator.   
`status` |  `object` |  status holds the information about the state of an operator. It is consistent with status information across the Kubernetes ecosystem.   
Show more

## 6.1.1. .spec

Description
     spec holds configuration that could apply to any operator. 
Type
     `object`

## 6.1.2. .status

Description
     status holds the information about the state of an operator. It is consistent with status information across the Kubernetes ecosystem. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions describes the state of the operator’s managed and monitored components.   
`conditions[]` |  `object` |  ClusterOperatorStatusCondition represents the state of the operator’s managed and monitored components.   
`extension` |  ``  |  extension contains any additional status information specific to the operator which owns this status object.   
`relatedObjects` |  `array` |  relatedObjects is a list of objects that are "interesting" or related to this operator. Common uses are: 1. the detailed resource driving the operator 2. operator namespaces 3. operand namespaces   
`relatedObjects[]` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
`versions` |  `array` |  versions is a slice of operator and operand version tuples. Operators which manage multiple operands will have multiple operand entries in the array. Available operators must report the version of the operator itself with the name "operator". An operator reports a new "operator" version when it has rolled out the new version to all of its operands.   
`versions[]` |  `object` |   
Show more

## 6.1.3. .status.conditions

Description
     conditions describes the state of the operator’s managed and monitored components. 
Type
     `array`

## 6.1.4. .status.conditions[]

Description
     ClusterOperatorStatusCondition represents the state of the operator’s managed and monitored components. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the time of the last update to the current status property.   
`message` |  `string` |  message provides additional information about the current condition. This is only to be consumed by humans. It may contain Line Feed characters (U+000A), which should be rendered as new lines.   
`reason` |  `string` |  reason is the CamelCase reason for the condition’s current status.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type specifies the aspect reported by this condition.   
Show more

## 6.1.5. .status.relatedObjects

Description
     relatedObjects is a list of objects that are "interesting" or related to this operator. Common uses are: 1. the detailed resource driving the operator 2. operator namespaces 3. operand namespaces 
Type
     `array`

## 6.1.6. .status.relatedObjects[]

Description
     ObjectReference contains enough information to let you inspect or modify the referred object. 
Type
     `object`
Required
    

  * `group`
  * `name`
  * `resource`



Property| Type| Description  
---|---|---  
`group` |  `string` |  group of the referent.   
`name` |  `string` |  name of the referent.   
`namespace` |  `string` |  namespace of the referent.   
`resource` |  `string` |  resource of the referent.   
Show more

## 6.1.7. .status.versions

Description
     versions is a slice of operator and operand version tuples. Operators which manage multiple operands will have multiple operand entries in the array. Available operators must report the version of the operator itself with the name "operator". An operator reports a new "operator" version when it has rolled out the new version to all of its operands. 
Type
     `array`

## 6.1.8. .status.versions[]

Description
    
Type
     `object`
Required
    

  * `name`
  * `version`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the particular operand this version is for. It usually matches container images, not operators.   
`version` |  `string` |  version indicates which version of a particular operand is currently being managed. It must always match the Available operand. If 1.0.0 is Available, then this must indicate 1.0.0 even if the operator is trying to rollout 1.1.0   
Show more
