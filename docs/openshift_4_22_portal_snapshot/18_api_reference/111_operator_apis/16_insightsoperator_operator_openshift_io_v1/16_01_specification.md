# 16.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is the specification of the desired behavior of the Insights.   
`status` |  `object` |  status is the most recently observed status of the Insights operator.   
Show more

## 16.1.1. .spec

Description
     spec is the specification of the desired behavior of the Insights. 
Type
     `object`

Property| Type| Description  
---|---|---  
`logLevel` |  `string` |  logLevel is an intent based logging for an overall component. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for their operands. Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`managementState` |  `string` |  managementState indicates whether and how the operator should manage the component   
`observedConfig` |  ``  |  observedConfig holds a sparse config that controller has observed from the cluster state. It exists in spec because it is an input to the level for the operator   
`operatorLogLevel` |  `string` |  operatorLogLevel is an intent based logging for the operator itself. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for themselves. Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`unsupportedConfigOverrides` |  ``  |  unsupportedConfigOverrides holds a sparse config that will override any previously set options. It only needs to be the fields to override it will end up overlaying in the following order: 1. hardcoded defaults 2. observedConfig 3. unsupportedConfigOverrides   
Show more

## 16.1.2. .status

Description
     status is the most recently observed status of the Insights operator. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is a list of conditions and their status   
`conditions[]` |  `object` |  OperatorCondition is just the standard condition fields.   
`gatherStatus` |  `object` |  gatherStatus provides basic information about the last Insights data gathering. When omitted, this means no data gathering has taken place yet.   
`generations` |  `array` |  generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction.   
`generations[]` |  `object` |  GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made.   
`insightsReport` |  `object` |  insightsReport provides general Insights analysis results. When omitted, this means no data gathering has taken place yet.   
`observedGeneration` |  `integer` |  observedGeneration is the last generation change you’ve dealt with   
`readyReplicas` |  `integer` |  readyReplicas indicates how many replicas are ready and at the desired state   
`version` |  `string` |  version is the level this availability applies to   
Show more

## 16.1.3. .status.conditions

Description
     conditions is a list of conditions and their status 
Type
     `array`

## 16.1.4. .status.conditions[]

Description
     OperatorCondition is just the standard condition fields. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |   
`message` |  `string` |   
`reason` |  `string` |   
`status` |  `string` |   
`type` |  `string` |   
Show more

## 16.1.5. .status.gatherStatus

Description
     gatherStatus provides basic information about the last Insights data gathering. When omitted, this means no data gathering has taken place yet. 
Type
     `object`

Property| Type| Description  
---|---|---  
`gatherers` |  `array` |  gatherers is a list of active gatherers (and their statuses) in the last gathering.   
`gatherers[]` |  `object` |  gathererStatus represents information about a particular data gatherer.   
`lastGatherDuration` |  `string` |  lastGatherDuration is the total time taken to process all gatherers during the last gather event.   
`lastGatherTime` |  `string` |  lastGatherTime is the last time when Insights data gathering finished. An empty value means that no data has been gathered yet.   
Show more

## 16.1.6. .status.gatherStatus.gatherers

Description
     gatherers is a list of active gatherers (and their statuses) in the last gathering. 
Type
     `array`

## 16.1.7. .status.gatherStatus.gatherers[]

Description
     gathererStatus represents information about a particular data gatherer. 
Type
     `object`
Required
    

  * `conditions`
  * `lastGatherDuration`
  * `name`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions provide details on the status of each gatherer.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields }   
`lastGatherDuration` |  `string` |  lastGatherDuration represents the time spent gathering.   
`name` |  `string` |  name is the name of the gatherer.   
Show more

## 16.1.8. .status.gatherStatus.gatherers[].conditions

Description
     conditions provide details on the status of each gatherer. 
Type
     `array`

## 16.1.9. .status.gatherStatus.gatherers[].conditions[]

Description
     Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields } 
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
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)   
Show more

## 16.1.10. .status.generations

Description
     generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. 
Type
     `array`

## 16.1.11. .status.generations[]

Description
     GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made. 
Type
     `object`

Property| Type| Description  
---|---|---  
`group` |  `string` |  group is the group of the thing you’re tracking   
`hash` |  `string` |  hash is an optional field set for resources without generation that are content sensitive like secrets and configmaps   
`lastGeneration` |  `integer` |  lastGeneration is the last generation of the workload controller involved   
`name` |  `string` |  name is the name of the thing you’re tracking   
`namespace` |  `string` |  namespace is where the thing you’re tracking is   
`resource` |  `string` |  resource is the resource type of the thing you’re tracking   
Show more

## 16.1.12. .status.insightsReport

Description
     insightsReport provides general Insights analysis results. When omitted, this means no data gathering has taken place yet. 
Type
     `object`

Property| Type| Description  
---|---|---  
`downloadedAt` |  `string` |  downloadedAt is the time when the last Insights report was downloaded. An empty value means that there has not been any Insights report downloaded yet and it usually appears in disconnected clusters (or clusters when the Insights data gathering is disabled).   
`healthChecks` |  `array` |  healthChecks provides basic information about active Insights health checks in a cluster.   
`healthChecks[]` |  `object` |  healthCheck represents an Insights health check attributes.   
Show more

## 16.1.13. .status.insightsReport.healthChecks

Description
     healthChecks provides basic information about active Insights health checks in a cluster. 
Type
     `array`

## 16.1.14. .status.insightsReport.healthChecks[]

Description
     healthCheck represents an Insights health check attributes. 
Type
     `object`
Required
    

  * `advisorURI`
  * `description`
  * `state`
  * `totalRisk`



Property| Type| Description  
---|---|---  
`advisorURI` |  `string` |  advisorURI provides the URL link to the Insights Advisor.   
`description` |  `string` |  description provides basic description of the healtcheck.   
`state` |  `string` |  state determines what the current state of the health check is. Health check is enabled by default and can be disabled by the user in the Insights advisor user interface.   
`totalRisk` |  `integer` |  totalRisk of the healthcheck. Indicator of the total risk posed by the detected issue; combination of impact and likelihood. The values can be from 1 to 4, and the higher the number, the more important the issue.   
Show more
