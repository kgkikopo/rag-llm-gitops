# 9.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of the desired behavior of EgressIP.   
`status` |  `object` |  Observed status of EgressIP. Read-only.   
Show more

## 9.1.1. .spec

Description
     Specification of the desired behavior of EgressIP. 
Type
     `object`
Required
    

  * `egressIPs`
  * `namespaceSelector`



Property| Type| Description  
---|---|---  
`egressIPs` |  `array (string)` |  EgressIPs is the list of egress IP addresses requested. Can be IPv4 and/or IPv6. This field is mandatory.   
`namespaceSelector` |  `object` |  NamespaceSelector applies the egress IP only to the namespace(s) whose label matches this definition. This field is mandatory.   
`podSelector` |  `object` |  PodSelector applies the egress IP only to the pods whose label matches this definition. This field is optional, and in case it is not set: results in the egress IP being applied to all pods in the namespace(s) matched by the NamespaceSelector. In case it is set: is intersected with the NamespaceSelector, thus applying the egress IP to the pods (in the namespace(s) already matched by the NamespaceSelector) which match this pod selector.   
Show more

## 9.1.2. .spec.namespaceSelector

Description
     NamespaceSelector applies the egress IP only to the namespace(s) whose label matches this definition. This field is mandatory. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 9.1.3. .spec.namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 9.1.4. .spec.namespaceSelector.matchExpressions[]

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

## 9.1.5. .spec.podSelector

Description
     PodSelector applies the egress IP only to the pods whose label matches this definition. This field is optional, and in case it is not set: results in the egress IP being applied to all pods in the namespace(s) matched by the NamespaceSelector. In case it is set: is intersected with the NamespaceSelector, thus applying the egress IP to the pods (in the namespace(s) already matched by the NamespaceSelector) which match this pod selector. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 9.1.6. .spec.podSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 9.1.7. .spec.podSelector.matchExpressions[]

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

## 9.1.8. .status

Description
     Observed status of EgressIP. Read-only. 
Type
     `object`
Required
    

  * `items`



Property| Type| Description  
---|---|---  
`items` |  `array` |  The list of assigned egress IPs and their corresponding node assignment.   
`items[]` |  `object` |  The per node status, for those egress IPs who have been assigned.   
Show more

## 9.1.9. .status.items

Description
     The list of assigned egress IPs and their corresponding node assignment. 
Type
     `array`

## 9.1.10. .status.items[]

Description
     The per node status, for those egress IPs who have been assigned. 
Type
     `object`
Required
    

  * `egressIP`
  * `node`



Property| Type| Description  
---|---|---  
`egressIP` |  `string` |  Assigned egress IP   
`node` |  `string` |  Assigned node name   
Show more
