# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  TemplateInstanceSpec describes the desired state of a TemplateInstance.   
`status` |  `object` |  TemplateInstanceStatus describes the current state of a TemplateInstance.   
Show more

## 5.1.1. .spec

Description
     TemplateInstanceSpec describes the desired state of a TemplateInstance. 
Type
     `object`
Required
    

  * `template`



Property| Type| Description  
---|---|---  
`requester` |  `object` |  TemplateInstanceRequester holds the identity of an agent requesting a template instantiation.   
`secret` |  `LocalObjectReference` |  secret is a reference to a Secret object containing the necessary template parameters.   
`template` |  `object` |  Template contains the inputs needed to produce a Config.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
Show more

## 5.1.2. .spec.requester

Description
     TemplateInstanceRequester holds the identity of an agent requesting a template instantiation. 
Type
     `object`

Property| Type| Description  
---|---|---  
`extra` |  `object` |  extra holds additional information provided by the authenticator.   
`extra{}` |  `array (string)` |   
`groups` |  `array (string)` |  groups represent the groups this user is a part of.   
`uid` |  `string` |  uid is a unique value that identifies this user across time; if this user is deleted and another user by the same name is added, they will have different UIDs.   
`username` |  `string` |  username uniquely identifies this user among all active users.   
Show more

## 5.1.3. .spec.requester.extra

Description
     extra holds additional information provided by the authenticator. 
Type
     `object`

## 5.1.4. .spec.template

Description
    

Template contains the inputs needed to produce a Config. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `objects`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`labels` |  `object (string)` |  labels is a optional set of labels that are applied to every object during the Template to Config transformation.   
`message` |  `string` |  message is an optional instructional message that will be displayed when this template is instantiated. This field should inform the user how to utilize the newly created resources. Parameter substitution will be performed on the message before being displayed so that generated credentials and other parameters can be included in the output.   
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`objects` |  [`array (RawExtension)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  objects is an array of resources to include in this template. If a namespace value is hardcoded in the object, it will be removed during template instantiation, however if the namespace value is, or contains, a ${PARAMETER_REFERENCE}, the resolved value after parameter substitution will be respected and the object will be created in that namespace.   
`parameters` |  `array` |  parameters is an optional array of Parameters used during the Template to Config transformation.   
`parameters[]` |  `object` |  Parameter defines a name/value variable that is to be processed during the Template to Config transformation.   
Show more

## 5.1.5. .spec.template.parameters

Description
     parameters is an optional array of Parameters used during the Template to Config transformation. 
Type
     `array`

## 5.1.6. .spec.template.parameters[]

Description
     Parameter defines a name/value variable that is to be processed during the Template to Config transformation. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`description` |  `string` |  description of a parameter. Optional.   
`displayName` |  `string` |  Optional: The name that will show in UI instead of parameter 'Name'   
`from` |  `string` |  from is an input value for the generator. Optional.   
`generate` |  `string` |  generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.  The only supported generator is "expression", which accepts a "from" value in the form of a simple regular expression containing the range expression "[a-zA-Z0-9]", and the length expression "a{length}".  Examples:  from | value ----------------------------- "test[0-9]{1}x" | "test7x" "[0-1]{8}" | "01001100" "0x[A-F0-9]{4}" | "0xB3AF" "[a-zA-Z0-9]{8}" | "hW4yQU5i"   
`name` |  `string` |  name must be set and it can be referenced in Template Items using ${PARAMETER_NAME}. Required.   
`required` |  `boolean` |  Optional: Indicates the parameter must have a value. Defaults to false.   
`value` |  `string` |  value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional.   
Show more

## 5.1.7. .status

Description
     TemplateInstanceStatus describes the current state of a TemplateInstance. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represent the latest available observations of a TemplateInstance’s current state.   
`conditions[]` |  `object` |  TemplateInstanceCondition contains condition information for a TemplateInstance.   
`objects` |  `array` |  objects references the objects created by the TemplateInstance.   
`objects[]` |  `object` |  TemplateInstanceObject references an object created by a TemplateInstance.   
Show more

## 5.1.8. .status.conditions

Description
     conditions represent the latest available observations of a TemplateInstance’s current state. 
Type
     `array`

## 5.1.9. .status.conditions[]

Description
     TemplateInstanceCondition contains condition information for a TemplateInstance. 
Type
     `object`
Required
    

  * `type`
  * `status`
  * `lastTransitionTime`
  * `reason`
  * `message`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastTransitionTime is the last time a condition status transitioned from one state to another.   
`message` |  `string` |  message is a human readable description of the details of the last transition, complementing reason.   
`reason` |  `string` |  reason is a brief machine readable explanation for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of True, False or Unknown.   
`type` |  `string` |  type of the condition, currently Ready or InstantiateFailure.   
Show more

## 5.1.10. .status.objects

Description
     objects references the objects created by the TemplateInstance. 
Type
     `array`

## 5.1.11. .status.objects[]

Description
     TemplateInstanceObject references an object created by a TemplateInstance. 
Type
     `object`

Property| Type| Description  
---|---|---  
`ref` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  ref is a reference to the created object. When used under .spec, only name and namespace are used; these can contain references to parameters which will be substituted following the usual rules.   
Show more
