# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  HostFirmwareSettingsSpec defines the desired state of HostFirmwareSettings.   
`status` |  `object` |  HostFirmwareSettingsStatus defines the observed state of HostFirmwareSettings.   
Show more

## 8.1.1. .spec

Description
     HostFirmwareSettingsSpec defines the desired state of HostFirmwareSettings. 
Type
     `object`
Required
    

  * `settings`



Property| Type| Description  
---|---|---  
`settings` |  `integer-or-string` |  Settings are the desired firmware settings stored as name/value pairs.   
Show more

## 8.1.2. .status

Description
     HostFirmwareSettingsStatus defines the observed state of HostFirmwareSettings. 
Type
     `object`
Required
    

  * `settings`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  Track whether settings stored in the spec are valid based on the schema   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`lastUpdated` |  `string` |  Time that the status was last updated   
`schema` |  `object` |  FirmwareSchema is a reference to the Schema used to describe each FirmwareSetting. By default, this will be a Schema in the same Namespace as the settings but it can be overwritten in the Spec   
`settings` |  `object (string)` |  Settings are the firmware settings stored as name/value pairs   
Show more

## 8.1.3. .status.conditions

Description
     Track whether settings stored in the spec are valid based on the schema 
Type
     `array`

## 8.1.4. .status.conditions[]

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

## 8.1.5. .status.schema

Description
     FirmwareSchema is a reference to the Schema used to describe each FirmwareSetting. By default, this will be a Schema in the same Namespace as the settings but it can be overwritten in the Spec 
Type
     `object`
Required
    

  * `name`
  * `namespace`



Property| Type| Description  
---|---|---  
`name` |  `string` |  `name` is the reference to the schema.   
`namespace` |  `string` |  `namespace` is the namespace of the where the schema is stored.   
Show more
