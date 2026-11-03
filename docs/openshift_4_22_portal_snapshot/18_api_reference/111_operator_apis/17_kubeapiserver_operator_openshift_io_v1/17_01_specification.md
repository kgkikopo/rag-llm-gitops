# 17.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is the specification of the desired behavior of the Kubernetes API Server   
`status` |  `object` |  status is the most recently observed status of the Kubernetes API Server   
Show more

## 17.1.1. .spec

Description
     spec is the specification of the desired behavior of the Kubernetes API Server 
Type
     `object`

Property| Type| Description  
---|---|---  
`eventTTLMinutes` |  `integer` |  eventTTLMinutes specifies the amount of time that the events are stored before being deleted. The TTL is allowed between 5 minutes minimum up to a maximum of 180 minutes (3 hours).  Lowering this value will reduce the storage required in etcd. Note that this setting will only apply to new events being created and will not update existing events.  When omitted this means no opinion, and the platform is left to choose a reasonable default, which is subject to change over time. The current default value is 3h (180 minutes).   
`failedRevisionLimit` |  `integer` |  failedRevisionLimit is the number of failed static pod installer revisions to keep on disk and in the api -1 = unlimited, 0 or unset = 5 (default)   
`forceRedeploymentReason` |  `string` |  forceRedeploymentReason can be used to force the redeployment of the operand by providing a unique string. This provides a mechanism to kick a previously failed deployment and provide a reason why you think it will work this time instead of failing again on the same config.   
`logLevel` |  `string` |  logLevel is an intent based logging for an overall component. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for their operands.  Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`managementState` |  `string` |  managementState indicates whether and how the operator should manage the component   
`observedConfig` |  ``  |  observedConfig holds a sparse config that controller has observed from the cluster state. It exists in spec because it is an input to the level for the operator   
`operatorLogLevel` |  `string` |  operatorLogLevel is an intent based logging for the operator itself. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for themselves.  Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`succeededRevisionLimit` |  `integer` |  succeededRevisionLimit is the number of successful static pod installer revisions to keep on disk and in the api -1 = unlimited, 0 or unset = 5 (default)   
`unsupportedConfigOverrides` |  ``  |  unsupportedConfigOverrides overrides the final configuration that was computed by the operator. Red Hat does not support the use of this field. Misuse of this field could lead to unexpected behavior or conflict with other configuration options. Seek guidance from the Red Hat support before using this field. Use of this property blocks cluster upgrades, it must be removed before upgrading your cluster.   
Show more

## 17.1.2. .status

Description
     status is the most recently observed status of the Kubernetes API Server 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is a list of conditions and their status   
`conditions[]` |  `object` |  OperatorCondition is just the standard condition fields.   
`generations` |  `array` |  generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction.   
`generations[]` |  `object` |  GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made.   
`latestAvailableRevision` |  `integer` |  latestAvailableRevision is the deploymentID of the most recent deployment   
`latestAvailableRevisionReason` |  `string` |  latestAvailableRevisionReason describe the detailed reason for the most recent deployment   
`nodeStatuses` |  `array` |  nodeStatuses track the deployment values and errors across individual nodes   
`nodeStatuses[]` |  `object` |  NodeStatus provides information about the current state of a particular node managed by this operator.   
`observedGeneration` |  `integer` |  observedGeneration is the last generation change you’ve dealt with   
`readyReplicas` |  `integer` |  readyReplicas indicates how many replicas are ready and at the desired state   
`serviceAccountIssuers` |  `array` |  serviceAccountIssuers tracks history of used service account issuers. The item without expiration time represents the currently used service account issuer. The other items represents service account issuers that were used previously and are still being trusted. The default expiration for the items is set by the platform and it defaults to 24h. see: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection>  
`serviceAccountIssuers[]` |  `object` |   
`version` |  `string` |  version is the level this availability applies to   
Show more

## 17.1.3. .status.conditions

Description
     conditions is a list of conditions and their status 
Type
     `array`

## 17.1.4. .status.conditions[]

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

## 17.1.5. .status.generations

Description
     generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. 
Type
     `array`

## 17.1.6. .status.generations[]

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

## 17.1.7. .status.nodeStatuses

Description
     nodeStatuses track the deployment values and errors across individual nodes 
Type
     `array`

## 17.1.8. .status.nodeStatuses[]

Description
     NodeStatus provides information about the current state of a particular node managed by this operator. 
Type
     `object`
Required
    

  * `nodeName`



Property| Type| Description  
---|---|---  
`currentRevision` |  `integer` |  currentRevision is the generation of the most recently successful deployment. Can not be set on creation of a nodeStatus. Updates must only increase the value.   
`lastFailedCount` |  `integer` |  lastFailedCount is how often the installer pod of the last failed revision failed.   
`lastFailedReason` |  `string` |  lastFailedReason is a machine readable failure reason string.   
`lastFailedRevision` |  `integer` |  lastFailedRevision is the generation of the deployment we tried and failed to deploy.   
`lastFailedRevisionErrors` |  `array (string)` |  lastFailedRevisionErrors is a list of human readable errors during the failed deployment referenced in lastFailedRevision.   
`lastFailedTime` |  `string` |  lastFailedTime is the time the last failed revision failed the last time.   
`lastFallbackCount` |  `integer` |  lastFallbackCount is how often a fallback to a previous revision happened.   
`nodeName` |  `string` |  nodeName is the name of the node   
`targetRevision` |  `integer` |  targetRevision is the generation of the deployment we’re trying to apply. Can not be set on creation of a nodeStatus.   
Show more

## 17.1.9. .status.serviceAccountIssuers

Description
     serviceAccountIssuers tracks history of used service account issuers. The item without expiration time represents the currently used service account issuer. The other items represents service account issuers that were used previously and are still being trusted. The default expiration for the items is set by the platform and it defaults to 24h. see: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection>
Type
     `array`

## 17.1.10. .status.serviceAccountIssuers[]

Description
    
Type
     `object`

Property| Type| Description  
---|---|---  
`expirationTime` |  `string` |  expirationTime is the time after which this service account issuer will be pruned and removed from the trusted list of service account issuers.   
`name` |  `string` |  name is the name of the service account issuer   
Show more
