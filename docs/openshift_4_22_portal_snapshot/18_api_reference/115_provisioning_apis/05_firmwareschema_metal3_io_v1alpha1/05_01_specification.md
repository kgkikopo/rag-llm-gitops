# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  FirmwareSchemaSpec defines the desired state of FirmwareSchema.   
Show more

## 5.1.1. .spec

Description
     FirmwareSchemaSpec defines the desired state of FirmwareSchema. 
Type
     `object`
Required
    

  * `schema`



Property| Type| Description  
---|---|---  
`hardwareModel` |  `string` |  The hardware model associated with this schema   
`hardwareVendor` |  `string` |  The hardware vendor associated with this schema   
`schema` |  `object` |  Map of firmware name to schema   
`schema{}` |  `object` |  Additional data describing the firmware setting.   
Show more

## 5.1.2. .spec.schema

Description
     Map of firmware name to schema 
Type
     `object`

## 5.1.3. .spec.schema{}

Description
     Additional data describing the firmware setting. 
Type
     `object`

Property| Type| Description  
---|---|---  
`allowable_values` |  `array (string)` |  The allowable value for an Enumeration type setting.   
`attribute_type` |  `string` |  The type of setting.   
`lower_bound` |  `integer` |  The lowest value for an Integer type setting.   
`max_length` |  `integer` |  Maximum length for a String type setting.   
`min_length` |  `integer` |  Minimum length for a String type setting.   
`read_only` |  `boolean` |  Whether or not this setting is read only.   
`unique` |  `boolean` |  Whether or not this setting’s value is unique to this node, e.g. a serial number.   
`upper_bound` |  `integer` |  The highest value for an Integer type setting.   
Show more
