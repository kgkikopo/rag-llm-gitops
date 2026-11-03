# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is the specification of the desired behavior of the Config Operator.   
`status` |  `object` |  status defines the observed status of the Config Operator.   
Show more

## 6.1.1. .spec

Description
     spec is the specification of the desired behavior of the Config Operator. 
Type
     `object`

Property| Type| Description  
---|---|---  
`logLevel` |  `string` |  logLevel is an intent based logging for an overall component. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for their operands.  Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`managementState` |  `string` |  managementState indicates whether and how the operator should manage the component   
`observedConfig` |  ``  |  observedConfig holds a sparse config that controller has observed from the cluster state. It exists in spec because it is an input to the level for the operator   
`operatorLogLevel` |  `string` |  operatorLogLevel is an intent based logging for the operator itself. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for themselves.  Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`unsupportedConfigOverrides` |  ``  |  unsupportedConfigOverrides overrides the final configuration that was computed by the operator. Red Hat does not support the use of this field. Misuse of this field could lead to unexpected behavior or conflict with other configuration options. Seek guidance from the Red Hat support before using this field. Use of this property blocks cluster upgrades, it must be removed before upgrading your cluster.   
Show more

## 6.1.2. .status

Description
     status defines the observed status of the Config Operator. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is a list of conditions and their status   
`conditions[]` |  `object` |  OperatorCondition is just the standard condition fields.   
`generations` |  `array` |  generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction.   
`generations[]` |  `object` |  GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made.   
`latestAvailableRevision` |  `integer` |  latestAvailableRevision is the deploymentID of the most recent deployment   
`observedGeneration` |  `integer` |  observedGeneration is the last generation change you’ve dealt with   
`readyReplicas` |  `integer` |  readyReplicas indicates how many replicas are ready and at the desired state   
`version` |  `string` |  version is the level this availability applies to   
Show more

## 6.1.3. .status.conditions

Description
     conditions is a list of conditions and their status 
Type
     `array`

## 6.1.4. .status.conditions[]

Description
     OperatorCondition is just the standard condition fields. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |   
`reason` |  `string` |   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more

## 6.1.5. .status.generations

Description
     generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. 
Type
     `array`

## 6.1.6. .status.generations[]

Description
     GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made. 
Type
     `object`
Required
    

  * `group`
  * `name`
  * `namespace`
  * `resource`



Property| Type| Description  
---|---|---  
`group` |  `string` |  group is the group of the thing you’re tracking   
`hash` |  `string` |  hash is an optional field set for resources without generation that are content sensitive like secrets and configmaps   
`lastGeneration` |  `integer` |  lastGeneration is the last generation of the workload controller involved   
`name` |  `string` |  name is the name of the thing you’re tracking   
`namespace` |  `string` |  namespace is where the thing you’re tracking is   
`resource` |  `string` |  resource is the resource type of the thing you’re tracking   
Show more
