# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is the specification of the desired behavior of Tuned. More info: <https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status>  
`status` |  `object` |  TunedStatus is the status for a Tuned resource.   
Show more

## 6.1.1. .spec

Description
     spec is the specification of the desired behavior of Tuned. More info: <https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status>
Type
     `object`

Property| Type| Description  
---|---|---  
`managementState` |  `string` |  managementState indicates whether the registry instance represented by this config instance is under operator management or not. Valid values are Force, Managed, Unmanaged, and Removed.   
`profile` |  `array` |  Tuned profiles.   
`profile[]` |  `object` |  A Tuned profile.   
`recommend` |  `array` |  Selection logic for all Tuned profiles.   
`recommend[]` |  `object` |  Selection logic for a single Tuned profile.   
Show more

## 6.1.2. .spec.profile

Description
     Tuned profiles. 
Type
     `array`

## 6.1.3. .spec.profile[]

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

## 6.1.4. .spec.recommend

Description
     Selection logic for all Tuned profiles. 
Type
     `array`

## 6.1.5. .spec.recommend[]

Description
     Selection logic for a single Tuned profile. 
Type
     `object`
Required
    

  * `priority`
  * `profile`



Property| Type| Description  
---|---|---  
`machineConfigLabels` |  `object (string)` |  MachineConfigLabels specifies the labels for a MachineConfig. The MachineConfig is created automatically to apply additional host settings (e.g. kernel boot parameters) profile 'Profile' needs and can only be applied by creating a MachineConfig. This involves finding all MachineConfigPools with machineConfigSelector matching the MachineConfigLabels and setting the profile 'Profile' on all nodes that match the MachineConfigPools' nodeSelectors.   
`match` |  `array` |  Rules governing application of a Tuned profile connected by logical OR operator.   
`match[]` |  `object` |  Rules governing application of a Tuned profile.   
`operand` |  `object` |  Optional operand configuration.   
`priority` |  `integer` |  Tuned profile priority. Highest priority is 0.   
`profile` |  `string` |  Name of the Tuned profile to recommend.   
Show more

## 6.1.6. .spec.recommend[].match

Description
     Rules governing application of a Tuned profile connected by logical OR operator. 
Type
     `array`

## 6.1.7. .spec.recommend[].match[]

Description
     Rules governing application of a Tuned profile. 
Type
     `object`
Required
    

  * `label`



Property| Type| Description  
---|---|---  
`label` |  `string` |  Node or Pod label name.   
`match` |  `array (undefined)` |  Additional rules governing application of the tuned profile connected by logical AND operator.   
`type` |  `string` |  Match type: [node/pod]. If omitted, "node" is assumed.   
`value` |  `string` |  Node or Pod label value. If omitted, the presence of label name is enough to match.   
Show more

## 6.1.8. .spec.recommend[].operand

Description
     Optional operand configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`debug` |  `boolean` |  turn debugging on/off for the TuneD daemon: true/false (default is false)   
`tunedConfig` |  `object` |  Global configuration for the TuneD daemon as defined in tuned-main.conf   
`verbosity` |  `integer` |  klog logging verbosity   
Show more

## 6.1.9. .spec.recommend[].operand.tunedConfig

Description
     Global configuration for the TuneD daemon as defined in tuned-main.conf 
Type
     `object`

Property| Type| Description  
---|---|---  
`reapply_sysctl` |  `boolean` |  turn reapply_sysctl functionality on/off for the TuneD daemon: true/false   
Show more

## 6.1.10. .status

Description
     TunedStatus is the status for a Tuned resource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represents the state of the Tuned profile   
`conditions[]` |  `object` |  StatusCondition represents a partial state of the per-node Profile application.   
Show more

## 6.1.11. .status.conditions

Description
     conditions represents the state of the Tuned profile 
Type
     `array`

## 6.1.12. .status.conditions[]

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
