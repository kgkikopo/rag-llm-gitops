# 34.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is the desired state of IPAddressClaim.   
`status` |  `object` |  status is the observed state of IPAddressClaim.   
Show more

## 34.1.1. .spec

Description
     spec is the desired state of IPAddressClaim. 
Type
     `object`
Required
    

  * `poolRef`



Property| Type| Description  
---|---|---  
`clusterName` |  `string` |  clusterName is the name of the Cluster this object belongs to.   
`poolRef` |  `object` |  poolRef is a reference to the pool from which an IP address should be created.   
Show more

## 34.1.2. .spec.poolRef

Description
     poolRef is a reference to the pool from which an IP address should be created. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
Show more

## 34.1.3. .status

Description
     status is the observed state of IPAddressClaim. 
Type
     `object`

Property| Type| Description  
---|---|---  
`addressRef` |  `object` |  addressRef is a reference to the address that was created for this claim.   
`conditions` |  `array` |  conditions summarises the current state of the IPAddressClaim   
`conditions[]` |  `object` |  Condition defines an observation of a Cluster API resource operational state.   
`v1beta2` |  `object` |  v1beta2 groups all the fields that will be added or modified in IPAddressClaim’s status with the V1Beta2 version.   
Show more

## 34.1.4. .status.addressRef

Description
     addressRef is a reference to the address that was created for this claim. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 34.1.5. .status.conditions

Description
     conditions summarises the current state of the IPAddressClaim 
Type
     `array`

## 34.1.6. .status.conditions[]

Description
     Condition defines an observation of a Cluster API resource operational state. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This field may be empty.   
`reason` |  `string` |  reason is the reason for the condition’s last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty.   
`severity` |  `string` |  severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important.   
Show more

## 34.1.7. .status.v1beta2

Description
     v1beta2 groups all the fields that will be added or modified in IPAddressClaim’s status with the V1Beta2 version. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represents the observations of a IPAddressClaim’s current state.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
Show more

## 34.1.8. .status.v1beta2.conditions

Description
     conditions represents the observations of a IPAddressClaim’s current state. 
Type
     `array`

## 34.1.9. .status.v1beta2.conditions[]

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
