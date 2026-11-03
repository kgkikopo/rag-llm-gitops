# 17.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Spec defines the desired state of GatewayClass.   
`status` |  `object` |  Status defines the current state of GatewayClass.  Implementations MUST populate status on all GatewayClass resources which specify their controller name.   
Show more

## 17.1.1. .spec

Description
     Spec defines the desired state of GatewayClass. 
Type
     `object`
Required
    

  * `controllerName`



Property| Type| Description  
---|---|---  
`controllerName` |  `string` |  ControllerName is the name of the controller that is managing Gateways of this class. The value of this field MUST be a domain prefixed path.  Example: "example.net/gateway-controller".  This field is not mutable and cannot be empty.  Support: Core   
`description` |  `string` |  Description helps describe a GatewayClass with more details.   
`parametersRef` |  `object` |  ParametersRef is a reference to a resource that contains the configuration parameters corresponding to the GatewayClass. This is optional if the controller does not require any additional configuration.  ParametersRef can reference a standard Kubernetes resource, i.e. ConfigMap, or an implementation-specific custom resource. The resource can be cluster-scoped or namespace-scoped.  If the referent cannot be found, refers to an unsupported kind, or when the data within that resource is malformed, the GatewayClass SHOULD be rejected with the "Accepted" status condition set to "False" and an "InvalidParameters" reason.  A Gateway for this GatewayClass may provide its own `parametersRef`. When both are specified, the merging behavior is implementation specific. It is generally recommended that GatewayClass provides defaults that can be overridden by a Gateway.  Support: Implementation-specific   
Show more

## 17.1.2. .spec.parametersRef

Description
    

ParametersRef is a reference to a resource that contains the configuration parameters corresponding to the GatewayClass. This is optional if the controller does not require any additional configuration. 

ParametersRef can reference a standard Kubernetes resource, i.e. ConfigMap, or an implementation-specific custom resource. The resource can be cluster-scoped or namespace-scoped. 

If the referent cannot be found, refers to an unsupported kind, or when the data within that resource is malformed, the GatewayClass SHOULD be rejected with the "Accepted" status condition set to "False" and an "InvalidParameters" reason. 

A Gateway for this GatewayClass may provide its own `parametersRef`. When both are specified, the merging behavior is implementation specific. It is generally recommended that GatewayClass provides defaults that can be overridden by a Gateway. 

Support: Implementation-specific 

Type
     `object`
Required
    

  * `group`
  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`group` |  `string` |  Group is the group of the referent.   
`kind` |  `string` |  Kind is kind of the referent.   
`name` |  `string` |  Name is the name of the referent.   
`namespace` |  `string` |  Namespace is the namespace of the referent. This field is required when referring to a Namespace-scoped resource and MUST be unset when referring to a Cluster-scoped resource.   
Show more

## 17.1.3. .status

Description
    

Status defines the current state of GatewayClass. 

Implementations MUST populate status on all GatewayClass resources which specify their controller name. 

Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  Conditions is the current status from the controller for this GatewayClass.  Controllers should prefer to publish conditions using values of GatewayClassConditionType for the type of each Condition.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`supportedFeatures` |  `array` |  SupportedFeatures is the set of features the GatewayClass support. It MUST be sorted in ascending alphabetical order by the Name key.   
`supportedFeatures[]` |  `object` |   
Show more

## 17.1.4. .status.conditions

Description
    

Conditions is the current status from the controller for this GatewayClass. 

Controllers should prefer to publish conditions using values of GatewayClassConditionType for the type of each Condition. 

Type
     `array`

## 17.1.5. .status.conditions[]

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

## 17.1.6. .status.supportedFeatures

Description
     SupportedFeatures is the set of features the GatewayClass support. It MUST be sorted in ascending alphabetical order by the Name key. 
Type
     `array`

## 17.1.7. .status.supportedFeatures[]

Description
    
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  FeatureName is used to describe distinct features that are covered by conformance tests.   
Show more
