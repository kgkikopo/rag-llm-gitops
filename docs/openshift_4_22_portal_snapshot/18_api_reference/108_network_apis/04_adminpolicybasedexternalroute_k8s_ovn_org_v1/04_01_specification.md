# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  AdminPolicyBasedExternalRouteSpec defines the desired state of AdminPolicyBasedExternalRoute   
`status` |  `object` |  AdminPolicyBasedRouteStatus contains the observed status of the AdminPolicyBased route types.   
Show more

## 4.1.1. .spec

Description
     AdminPolicyBasedExternalRouteSpec defines the desired state of AdminPolicyBasedExternalRoute 
Type
     `object`
Required
    

  * `from`
  * `nextHops`



Property| Type| Description  
---|---|---  
`from` |  `object` |  From defines the selectors that will determine the target namespaces to this CR.   
`nextHops` |  `object` |  NextHops defines two types of hops: Static and Dynamic. Each hop defines at least one external gateway IP.   
Show more

## 4.1.2. .spec.from

Description
     From defines the selectors that will determine the target namespaces to this CR. 
Type
     `object`
Required
    

  * `namespaceSelector`



Property| Type| Description  
---|---|---  
`namespaceSelector` |  `object` |  NamespaceSelector defines a selector to be used to determine which namespaces will be targeted by this CR   
Show more

## 4.1.3. .spec.from.namespaceSelector

Description
     NamespaceSelector defines a selector to be used to determine which namespaces will be targeted by this CR 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 4.1.4. .spec.from.namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 4.1.5. .spec.from.namespaceSelector.matchExpressions[]

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

## 4.1.6. .spec.nextHops

Description
     NextHops defines two types of hops: Static and Dynamic. Each hop defines at least one external gateway IP. 
Type
     `object`

Property| Type| Description  
---|---|---  
`dynamic` |  `array` |  DynamicHops defines a slices of DynamicHop. This field is optional.   
`dynamic[]` |  `object` |  DynamicHop defines the configuration for a dynamic external gateway interface. These interfaces are wrapped around a pod object that resides inside the cluster. The field NetworkAttachmentName captures the name of the multus network name to use when retrieving the gateway IP to use. The PodSelector and the NamespaceSelector are mandatory fields.   
`static` |  `array` |  StaticHops defines a slice of StaticHop. This field is optional.   
`static[]` |  `object` |  StaticHop defines the configuration of a static IP that acts as an external Gateway Interface. IP field is mandatory.   
Show more

## 4.1.7. .spec.nextHops.dynamic

Description
     DynamicHops defines a slices of DynamicHop. This field is optional. 
Type
     `array`

## 4.1.8. .spec.nextHops.dynamic[]

Description
     DynamicHop defines the configuration for a dynamic external gateway interface. These interfaces are wrapped around a pod object that resides inside the cluster. The field NetworkAttachmentName captures the name of the multus network name to use when retrieving the gateway IP to use. The PodSelector and the NamespaceSelector are mandatory fields. 
Type
     `object`
Required
    

  * `namespaceSelector`
  * `podSelector`



Property| Type| Description  
---|---|---  
`bfdEnabled` |  `boolean` |  BFDEnabled determines if the interface implements the Bidirectional Forward Detection protocol. Defaults to false.   
`namespaceSelector` |  `object` |  NamespaceSelector defines a selector to filter the namespaces where the pod gateways are located.   
`networkAttachmentName` |  `string` |  NetworkAttachmentName determines the multus network name to use when retrieving the pod IPs that will be used as the gateway IP. When this field is empty, the logic assumes that the pod is configured with HostNetwork and is using the node’s IP as gateway.   
`podSelector` |  `object` |  PodSelector defines the selector to filter the pods that are external gateways.   
Show more

## 4.1.9. .spec.nextHops.dynamic[].namespaceSelector

Description
     NamespaceSelector defines a selector to filter the namespaces where the pod gateways are located. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 4.1.10. .spec.nextHops.dynamic[].namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 4.1.11. .spec.nextHops.dynamic[].namespaceSelector.matchExpressions[]

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

## 4.1.12. .spec.nextHops.dynamic[].podSelector

Description
     PodSelector defines the selector to filter the pods that are external gateways. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 4.1.13. .spec.nextHops.dynamic[].podSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 4.1.14. .spec.nextHops.dynamic[].podSelector.matchExpressions[]

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

## 4.1.15. .spec.nextHops.static

Description
     StaticHops defines a slice of StaticHop. This field is optional. 
Type
     `array`

## 4.1.16. .spec.nextHops.static[]

Description
     StaticHop defines the configuration of a static IP that acts as an external Gateway Interface. IP field is mandatory. 
Type
     `object`
Required
    

  * `ip`



Property| Type| Description  
---|---|---  
`bfdEnabled` |  `boolean` |  BFDEnabled determines if the interface implements the Bidirectional Forward Detection protocol. Defaults to false.   
`ip` |  `string` |  IP defines the static IP to be used for egress traffic. The IP can be either IPv4 or IPv6.   
Show more

## 4.1.17. .status

Description
     AdminPolicyBasedRouteStatus contains the observed status of the AdminPolicyBased route types. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  Captures the time when the last change was applied.   
`messages` |  `array (string)` |  An array of Human-readable messages indicating details about the status of the object.   
`status` |  `string` |  A concise indication of whether the AdminPolicyBasedRoute resource is applied with success   
Show more
