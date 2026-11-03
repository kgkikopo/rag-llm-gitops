# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  EgressQoSSpec defines the desired state of EgressQoS   
`status` |  `object` |  EgressQoSStatus defines the observed state of EgressQoS   
Show more

## 10.1.1. .spec

Description
     EgressQoSSpec defines the desired state of EgressQoS 
Type
     `object`
Required
    

  * `egress`



Property| Type| Description  
---|---|---  
`egress` |  `array` |  a collection of Egress QoS rule objects   
`egress[]` |  `object` |   
Show more

## 10.1.2. .spec.egress

Description
     a collection of Egress QoS rule objects 
Type
     `array`

## 10.1.3. .spec.egress[]

Description
    
Type
     `object`
Required
    

  * `dscp`



Property| Type| Description  
---|---|---  
`dscp` |  `integer` |  DSCP marking value for matching pods' traffic.   
`dstCIDR` |  `string` |  DstCIDR specifies the destination’s CIDR. Only traffic heading to this CIDR will be marked with the DSCP value. This field is optional, and in case it is not set the rule is applied to all egress traffic regardless of the destination.   
`podSelector` |  `object` |  PodSelector applies the QoS rule only to the pods in the namespace whose label matches this definition. This field is optional, and in case it is not set results in the rule being applied to all pods in the namespace.   
Show more

## 10.1.4. .spec.egress[].podSelector

Description
     PodSelector applies the QoS rule only to the pods in the namespace whose label matches this definition. This field is optional, and in case it is not set results in the rule being applied to all pods in the namespace. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 10.1.5. .spec.egress[].podSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 10.1.6. .spec.egress[].podSelector.matchExpressions[]

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

## 10.1.7. .status

Description
     EgressQoSStatus defines the observed state of EgressQoS 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  An array of condition objects indicating details about status of EgressQoS object.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example,  type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields }   
`status` |  `string` |  A concise indication of whether the EgressQoS resource is applied with success.   
Show more

## 10.1.8. .status.conditions

Description
     An array of condition objects indicating details about status of EgressQoS object. 
Type
     `array`

## 10.1.9. .status.conditions[]

Description
    

Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, 

```plaintext
type FooStatus struct{
    // Represents the observations of a foo's current state.
    // Known .status.conditions.type are: "Available", "Progressing", and "Degraded"
    // +patchMergeKey=type
    // +patchStrategy=merge
    // +listType=map
    // +listMapKey=type
    Conditions []metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"`
```


```plaintext
    // other fields
}
```


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
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)   
Show more
