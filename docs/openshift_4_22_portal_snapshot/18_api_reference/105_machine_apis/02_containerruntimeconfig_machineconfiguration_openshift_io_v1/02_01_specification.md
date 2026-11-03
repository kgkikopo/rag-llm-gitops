# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec contains the desired container runtime configuration.   
`status` |  `object` |  status contains observed information about the container runtime configuration.   
Show more

## 2.1.1. .spec

Description
     spec contains the desired container runtime configuration. 
Type
     `object`
Required
    

  * `containerRuntimeConfig`



Property| Type| Description  
---|---|---  
`containerRuntimeConfig` |  `object` |  containerRuntimeConfig defines the tuneables of the container runtime.   
`machineConfigPoolSelector` |  `object` |  machineConfigPoolSelector selects which pools the ContainerRuntimeConfig shoud apply to. A nil selector will result in no pools being selected.   
Show more

## 2.1.2. .spec.containerRuntimeConfig

Description
     containerRuntimeConfig defines the tuneables of the container runtime. 
Type
     `object`

Property| Type| Description  
---|---|---  
`defaultRuntime` |  `string` |  defaultRuntime is the name of the OCI runtime to be used as the default for containers. Allowed values are `runc` and `crun`. When set to `runc`, OpenShift will use runc to execute the container When set to `crun`, OpenShift will use crun to execute the container When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. Currently, the default is `crun`.   
`logLevel` |  `string` |  logLevel specifies the verbosity of the logs based on the level it is set to. Options are fatal, panic, error, warn, info, and debug.   
`logSizeMax` |  `integer-or-string` |  logSizeMax specifies the Maximum size allowed for the container log file. Negative numbers indicate that no size limit is imposed. If it is positive, it must be >= 8192 to match/exceed conmon’s read buffer.   
`overlaySize` |  `integer-or-string` |  overlaySize specifies the maximum size of a container image. This flag can be used to set quota on the size of container images. (default: 10GB)   
`pidsLimit` |  `integer` |  pidsLimit specifies the maximum number of processes allowed in a container   
Show more

## 2.1.3. .spec.machineConfigPoolSelector

Description
     machineConfigPoolSelector selects which pools the ContainerRuntimeConfig shoud apply to. A nil selector will result in no pools being selected. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.4. .spec.machineConfigPoolSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.5. .spec.machineConfigPoolSelector.matchExpressions[]

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

## 2.1.6. .status

Description
     status contains observed information about the container runtime configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represents the latest available observations of current state.   
`conditions[]` |  `object` |  ContainerRuntimeConfigCondition defines the state of the ContainerRuntimeConfig   
`observedGeneration` |  `integer` |  observedGeneration represents the generation observed by the controller.   
Show more

## 2.1.7. .status.conditions

Description
     conditions represents the latest available observations of current state. 
Type
     `array`

## 2.1.8. .status.conditions[]

Description
     ContainerRuntimeConfigCondition defines the state of the ContainerRuntimeConfig 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  ``  |  lastTransitionTime is the time of the last update to the current status object.   
`message` |  `string` |  message provides additional information about the current condition. This is only to be consumed by humans.   
`reason` |  `string` |  reason is the reason for the condition’s last transition. Reasons are PascalCase   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type specifies the state of the operator’s reconciliation functionality.   
Show more
