# 22.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |   
`status` |  `object` |  IPAMClaimStatus contains the observed status of the IPAMClaim.   
Show more

## 22.1.1. .spec

Description
    
Type
     `object`
Required
    

  * `interface`
  * `network`



Property| Type| Description  
---|---|---  
`interface` |  `string` |  The pod interface name for which this allocation was created   
`network` |  `string` |  The network name for which this persistent allocation was created   
Show more

## 22.1.2. .status

Description
     IPAMClaimStatus contains the observed status of the IPAMClaim. 
Type
     `object`
Required
    

  * `ips`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  Conditions contains details for one aspect of the current state of this API Resource   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`ips` |  `array (string)` |  The list of IP addresses (v4, v6) that were allocated for the pod interface   
`ownerPod` |  `object` |  The name of the pod holding the IPAMClaim   
Show more

## 22.1.3. .status.conditions

Description
     Conditions contains details for one aspect of the current state of this API Resource 
Type
     `array`

## 22.1.4. .status.conditions[]

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

## 22.1.5. .status.ownerPod

Description
     The name of the pod holding the IPAMClaim 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |   
Show more
