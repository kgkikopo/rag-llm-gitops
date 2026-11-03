# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |   
`status` |  `object` |  ProfileStatus is the status for a Profile resource; the status is for internal use only and its fields may be changed/removed in the future.   
Show more

## 4.1.1. .spec

Description
    
Type
     `object`
Required
    

  * `config`



Property| Type| Description  
---|---|---  
`config` |  `object` |   
`profile` |  `array` |  Tuned profiles.   
`profile[]` |  `object` |  A Tuned profile.   
Show more

## 4.1.2. .spec.config

Description
    
Type
     `object`
Required
    

  * `tunedProfile`



Property| Type| Description  
---|---|---  
`debug` |  `boolean` |  option to debug TuneD daemon execution   
`providerName` |  `string` |  Name of the cloud provider as taken from the Node providerID: <ProviderName>://<ProviderSpecificNodeID>  
`tunedConfig` |  `object` |  Global configuration for the TuneD daemon as defined in tuned-main.conf   
`tunedProfile` |  `string` |  TuneD profile to apply   
`verbosity` |  `integer` |  klog logging verbosity   
Show more

## 4.1.3. .spec.config.tunedConfig

Description
     Global configuration for the TuneD daemon as defined in tuned-main.conf 
Type
     `object`

Property| Type| Description  
---|---|---  
`reapply_sysctl` |  `boolean` |  turn reapply_sysctl functionality on/off for the TuneD daemon: true/false   
Show more

## 4.1.4. .spec.profile

Description
     Tuned profiles. 
Type
     `array`

## 4.1.5. .spec.profile[]

Description
     A Tuned profile. 
Type
     `object`
Required
    

  * `data`
  * `name`



Property| Type| Description  
---|---|---  
`data` |  `string` |  Specification of the Tuned profile to be consumed by the Tuned daemon.   
`name` |  `string` |  Name of the Tuned profile to be used in the recommend section.   
Show more

## 4.1.6. .status

Description
     ProfileStatus is the status for a Profile resource; the status is for internal use only and its fields may be changed/removed in the future. 
Type
     `object`
Required
    

  * `tunedProfile`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represents the state of the per-node Profile application   
`conditions[]` |  `object` |  StatusCondition represents a partial state of the per-node Profile application.   
`observedGeneration` |  `integer` |  If set, this represents the .metadata.generation that the conditions were set based upon.   
`tunedProfile` |  `string` |  the current profile in use by the Tuned daemon   
Show more

## 4.1.7. .status.conditions

Description
     conditions represents the state of the per-node Profile application 
Type
     `array`

## 4.1.8. .status.conditions[]

Description
     StatusCondition represents a partial state of the per-node Profile application. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the time of the last update to the current status property.   
`message` |  `string` |  message provides additional information about the current condition. This is only to be consumed by humans.   
`reason` |  `string` |  reason is the CamelCase reason for the condition’s current status.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type specifies the aspect reported by this condition.   
Show more
