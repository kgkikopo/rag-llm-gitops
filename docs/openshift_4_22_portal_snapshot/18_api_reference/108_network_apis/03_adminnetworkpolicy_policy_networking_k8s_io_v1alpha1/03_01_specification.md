# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of the desired behavior of AdminNetworkPolicy.   
`status` |  `object` |  Status is the status to be reported by the implementation.   
Show more

## 3.1.1. .spec

Description
     Specification of the desired behavior of AdminNetworkPolicy. 
Type
     `object`
Required
    

  * `priority`
  * `subject`



Property| Type| Description  
---|---|---  
`egress` |  `array` |  Egress is the list of Egress rules to be applied to the selected pods. A total of 100 rules will be allowed in each ANP instance. The relative precedence of egress rules within a single ANP object (all of which share the priority) will be determined by the order in which the rule is written. Thus, a rule that appears at the top of the egress rules would take the highest precedence. ANPs with no egress rules do not affect egress traffic.  Support: Core   
`egress[]` |  `object` |  AdminNetworkPolicyEgressRule describes an action to take on a particular set of traffic originating from pods selected by a AdminNetworkPolicy’s Subject field. <network-policy-api:experimental:validation>  
`ingress` |  `array` |  Ingress is the list of Ingress rules to be applied to the selected pods. A total of 100 rules will be allowed in each ANP instance. The relative precedence of ingress rules within a single ANP object (all of which share the priority) will be determined by the order in which the rule is written. Thus, a rule that appears at the top of the ingress rules would take the highest precedence. ANPs with no ingress rules do not affect ingress traffic.  Support: Core   
`ingress[]` |  `object` |  AdminNetworkPolicyIngressRule describes an action to take on a particular set of traffic destined for pods selected by an AdminNetworkPolicy’s Subject field.   
`priority` |  `integer` |  Priority is a value from 0 to 1000. Rules with lower priority values have higher precedence, and are checked before rules with higher priority values. All AdminNetworkPolicy rules have higher precedence than NetworkPolicy or BaselineAdminNetworkPolicy rules The behavior is undefined if two ANP objects have same priority.  Support: Core   
`subject` |  `object` |  Subject defines the pods to which this AdminNetworkPolicy applies. Note that host-networked pods are not included in subject selection.  Support: Core   
Show more

## 3.1.2. .spec.egress

Description
    

Egress is the list of Egress rules to be applied to the selected pods. A total of 100 rules will be allowed in each ANP instance. The relative precedence of egress rules within a single ANP object (all of which share the priority) will be determined by the order in which the rule is written. Thus, a rule that appears at the top of the egress rules would take the highest precedence. ANPs with no egress rules do not affect egress traffic. 

Support: Core 

Type
     `array`

## 3.1.3. .spec.egress[]

Description
     AdminNetworkPolicyEgressRule describes an action to take on a particular set of traffic originating from pods selected by a AdminNetworkPolicy’s Subject field. <network-policy-api:experimental:validation>
Type
     `object`
Required
    

  * `action`
  * `to`



Property| Type| Description  
---|---|---  
`action` |  `string` |  Action specifies the effect this rule will have on matching traffic. Currently the following actions are supported: Allow: allows the selected traffic (even if it would otherwise have been denied by NetworkPolicy) Deny: denies the selected traffic Pass: instructs the selected traffic to skip any remaining ANP rules, and then pass execution to any NetworkPolicies that select the pod. If the pod is not selected by any NetworkPolicies then execution is passed to any BaselineAdminNetworkPolicies that select the pod.  Support: Core   
`name` |  `string` |  Name is an identifier for this rule, that may be no more than 100 characters in length. This field should be used by the implementation to help improve observability, readability and error-reporting for any applied AdminNetworkPolicies.  Support: Core   
`ports` |  `array` |  Ports allows for matching traffic based on port and protocols. This field is a list of destination ports for the outgoing egress traffic. If Ports is not set then the rule does not filter traffic via port.  Support: Core   
`ports[]` |  `object` |  AdminNetworkPolicyPort describes how to select network ports on pod(s). Exactly one field must be set.   
`to` |  `array` |  To is the List of destinations whose traffic this rule applies to. If any AdminNetworkPolicyEgressPeer matches the destination of outgoing traffic then the specified action is applied. This field must be defined and contain at least one item.  Support: Core   
`to[]` |  `object` |  AdminNetworkPolicyEgressPeer defines a peer to allow traffic to. Exactly one of the selector pointers must be set for a given peer. If a consumer observes none of its fields are set, they must assume an unknown option has been specified and fail closed.   
Show more

## 3.1.4. .spec.egress[].ports

Description
    

Ports allows for matching traffic based on port and protocols. This field is a list of destination ports for the outgoing egress traffic. If Ports is not set then the rule does not filter traffic via port. 

Support: Core 

Type
     `array`

## 3.1.5. .spec.egress[].ports[]

Description
     AdminNetworkPolicyPort describes how to select network ports on pod(s). Exactly one field must be set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`namedPort` |  `string` |  NamedPort selects a port on a pod(s) based on name.  Support: Extended  <network-policy-api:experimental>  
`portNumber` |  `object` |  Port selects a port on a pod(s) based on number.  Support: Core   
`portRange` |  `object` |  PortRange selects a port range on a pod(s) based on provided start and end values.  Support: Core   
Show more

## 3.1.6. .spec.egress[].ports[].portNumber

Description
    

Port selects a port on a pod(s) based on number. 

Support: Core 

Type
     `object`
Required
    

  * `port`
  * `protocol`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Number defines a network port value.  Support: Core   
`protocol` |  `string` |  Protocol is the network protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  Support: Core   
Show more

## 3.1.7. .spec.egress[].ports[].portRange

Description
    

PortRange selects a port range on a pod(s) based on provided start and end values. 

Support: Core 

Type
     `object`
Required
    

  * `end`
  * `start`



Property| Type| Description  
---|---|---  
`end` |  `integer` |  End defines a network port that is the end of a port range, the End value must be greater than Start.  Support: Core   
`protocol` |  `string` |  Protocol is the network protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  Support: Core   
`start` |  `integer` |  Start defines a network port that is the start of a port range, the Start value must be less than End.  Support: Core   
Show more

## 3.1.8. .spec.egress[].to

Description
    

To is the List of destinations whose traffic this rule applies to. If any AdminNetworkPolicyEgressPeer matches the destination of outgoing traffic then the specified action is applied. This field must be defined and contain at least one item. 

Support: Core 

Type
     `array`

## 3.1.9. .spec.egress[].to[]

Description
     AdminNetworkPolicyEgressPeer defines a peer to allow traffic to. Exactly one of the selector pointers must be set for a given peer. If a consumer observes none of its fields are set, they must assume an unknown option has been specified and fail closed. 
Type
     `object`

Property| Type| Description  
---|---|---  
`namespaces` |  `object` |  Namespaces defines a way to select all pods within a set of Namespaces. Note that host-networked pods are not included in this type of peer.  Support: Core   
`networks` |  `array (string)` |  Networks defines a way to select peers via CIDR blocks. This is intended for representing entities that live outside the cluster, which can’t be selected by pods, namespaces and nodes peers, but note that cluster-internal traffic will be checked against the rule as well. So if you Allow or Deny traffic to `"0.0.0.0/0"`, that will allow or deny all IPv4 pod-to-pod traffic as well. If you don’t want that, add a rule that Passes all pod traffic before the Networks rule.  Each item in Networks should be provided in the CIDR format and should be IPv4 or IPv6, for example "10.0.0.0/8" or "fd00::/8".  Networks can have upto 25 CIDRs specified.  Support: Extended  <network-policy-api:experimental>  
`nodes` |  `object` |  Nodes defines a way to select a set of nodes in the cluster. This field follows standard label selector semantics; if present but empty, it selects all Nodes.  Support: Extended  <network-policy-api:experimental>  
`pods` |  `object` |  Pods defines a way to select a set of pods in a set of namespaces. Note that host-networked pods are not included in this type of peer.  Support: Core   
Show more

## 3.1.10. .spec.egress[].to[].namespaces

Description
    

Namespaces defines a way to select all pods within a set of Namespaces. Note that host-networked pods are not included in this type of peer. 

Support: Core 

Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.11. .spec.egress[].to[].namespaces.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.12. .spec.egress[].to[].namespaces.matchExpressions[]

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

## 3.1.13. .spec.egress[].to[].nodes

Description
    

Nodes defines a way to select a set of nodes in the cluster. This field follows standard label selector semantics; if present but empty, it selects all Nodes. 

Support: Extended 

<network-policy-api:experimental>

Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.14. .spec.egress[].to[].nodes.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.15. .spec.egress[].to[].nodes.matchExpressions[]

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

## 3.1.16. .spec.egress[].to[].pods

Description
    

Pods defines a way to select a set of pods in a set of namespaces. Note that host-networked pods are not included in this type of peer. 

Support: Core 

Type
     `object`
Required
    

  * `namespaceSelector`
  * `podSelector`



Property| Type| Description  
---|---|---  
`namespaceSelector` |  `object` |  NamespaceSelector follows standard label selector semantics; if empty, it selects all Namespaces.   
`podSelector` |  `object` |  PodSelector is used to explicitly select pods within a namespace; if empty, it selects all Pods.   
Show more

## 3.1.17. .spec.egress[].to[].pods.namespaceSelector

Description
     NamespaceSelector follows standard label selector semantics; if empty, it selects all Namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.18. .spec.egress[].to[].pods.namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.19. .spec.egress[].to[].pods.namespaceSelector.matchExpressions[]

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

## 3.1.20. .spec.egress[].to[].pods.podSelector

Description
     PodSelector is used to explicitly select pods within a namespace; if empty, it selects all Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.21. .spec.egress[].to[].pods.podSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.22. .spec.egress[].to[].pods.podSelector.matchExpressions[]

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

## 3.1.23. .spec.ingress

Description
    

Ingress is the list of Ingress rules to be applied to the selected pods. A total of 100 rules will be allowed in each ANP instance. The relative precedence of ingress rules within a single ANP object (all of which share the priority) will be determined by the order in which the rule is written. Thus, a rule that appears at the top of the ingress rules would take the highest precedence. ANPs with no ingress rules do not affect ingress traffic. 

Support: Core 

Type
     `array`

## 3.1.24. .spec.ingress[]

Description
     AdminNetworkPolicyIngressRule describes an action to take on a particular set of traffic destined for pods selected by an AdminNetworkPolicy’s Subject field. 
Type
     `object`
Required
    

  * `action`
  * `from`



Property| Type| Description  
---|---|---  
`action` |  `string` |  Action specifies the effect this rule will have on matching traffic. Currently the following actions are supported: Allow: allows the selected traffic (even if it would otherwise have been denied by NetworkPolicy) Deny: denies the selected traffic Pass: instructs the selected traffic to skip any remaining ANP rules, and then pass execution to any NetworkPolicies that select the pod. If the pod is not selected by any NetworkPolicies then execution is passed to any BaselineAdminNetworkPolicies that select the pod.  Support: Core   
`from` |  `array` |  From is the list of sources whose traffic this rule applies to. If any AdminNetworkPolicyIngressPeer matches the source of incoming traffic then the specified action is applied. This field must be defined and contain at least one item.  Support: Core   
`from[]` |  `object` |  AdminNetworkPolicyIngressPeer defines an in-cluster peer to allow traffic from. Exactly one of the selector pointers must be set for a given peer. If a consumer observes none of its fields are set, they must assume an unknown option has been specified and fail closed.   
`name` |  `string` |  Name is an identifier for this rule, that may be no more than 100 characters in length. This field should be used by the implementation to help improve observability, readability and error-reporting for any applied AdminNetworkPolicies.  Support: Core   
`ports` |  `array` |  Ports allows for matching traffic based on port and protocols. This field is a list of ports which should be matched on the pods selected for this policy i.e the subject of the policy. So it matches on the destination port for the ingress traffic. If Ports is not set then the rule does not filter traffic via port.  Support: Core   
`ports[]` |  `object` |  AdminNetworkPolicyPort describes how to select network ports on pod(s). Exactly one field must be set.   
Show more

## 3.1.25. .spec.ingress[].from

Description
    

From is the list of sources whose traffic this rule applies to. If any AdminNetworkPolicyIngressPeer matches the source of incoming traffic then the specified action is applied. This field must be defined and contain at least one item. 

Support: Core 

Type
     `array`

## 3.1.26. .spec.ingress[].from[]

Description
     AdminNetworkPolicyIngressPeer defines an in-cluster peer to allow traffic from. Exactly one of the selector pointers must be set for a given peer. If a consumer observes none of its fields are set, they must assume an unknown option has been specified and fail closed. 
Type
     `object`

Property| Type| Description  
---|---|---  
`namespaces` |  `object` |  Namespaces defines a way to select all pods within a set of Namespaces. Note that host-networked pods are not included in this type of peer.  Support: Core   
`pods` |  `object` |  Pods defines a way to select a set of pods in a set of namespaces. Note that host-networked pods are not included in this type of peer.  Support: Core   
Show more

## 3.1.27. .spec.ingress[].from[].namespaces

Description
    

Namespaces defines a way to select all pods within a set of Namespaces. Note that host-networked pods are not included in this type of peer. 

Support: Core 

Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.28. .spec.ingress[].from[].namespaces.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.29. .spec.ingress[].from[].namespaces.matchExpressions[]

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

## 3.1.30. .spec.ingress[].from[].pods

Description
    

Pods defines a way to select a set of pods in a set of namespaces. Note that host-networked pods are not included in this type of peer. 

Support: Core 

Type
     `object`
Required
    

  * `namespaceSelector`
  * `podSelector`



Property| Type| Description  
---|---|---  
`namespaceSelector` |  `object` |  NamespaceSelector follows standard label selector semantics; if empty, it selects all Namespaces.   
`podSelector` |  `object` |  PodSelector is used to explicitly select pods within a namespace; if empty, it selects all Pods.   
Show more

## 3.1.31. .spec.ingress[].from[].pods.namespaceSelector

Description
     NamespaceSelector follows standard label selector semantics; if empty, it selects all Namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.32. .spec.ingress[].from[].pods.namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.33. .spec.ingress[].from[].pods.namespaceSelector.matchExpressions[]

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

## 3.1.34. .spec.ingress[].from[].pods.podSelector

Description
     PodSelector is used to explicitly select pods within a namespace; if empty, it selects all Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.35. .spec.ingress[].from[].pods.podSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.36. .spec.ingress[].from[].pods.podSelector.matchExpressions[]

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

## 3.1.37. .spec.ingress[].ports

Description
    

Ports allows for matching traffic based on port and protocols. This field is a list of ports which should be matched on the pods selected for this policy i.e the subject of the policy. So it matches on the destination port for the ingress traffic. If Ports is not set then the rule does not filter traffic via port. 

Support: Core 

Type
     `array`

## 3.1.38. .spec.ingress[].ports[]

Description
     AdminNetworkPolicyPort describes how to select network ports on pod(s). Exactly one field must be set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`namedPort` |  `string` |  NamedPort selects a port on a pod(s) based on name.  Support: Extended  <network-policy-api:experimental>  
`portNumber` |  `object` |  Port selects a port on a pod(s) based on number.  Support: Core   
`portRange` |  `object` |  PortRange selects a port range on a pod(s) based on provided start and end values.  Support: Core   
Show more

## 3.1.39. .spec.ingress[].ports[].portNumber

Description
    

Port selects a port on a pod(s) based on number. 

Support: Core 

Type
     `object`
Required
    

  * `port`
  * `protocol`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Number defines a network port value.  Support: Core   
`protocol` |  `string` |  Protocol is the network protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  Support: Core   
Show more

## 3.1.40. .spec.ingress[].ports[].portRange

Description
    

PortRange selects a port range on a pod(s) based on provided start and end values. 

Support: Core 

Type
     `object`
Required
    

  * `end`
  * `start`



Property| Type| Description  
---|---|---  
`end` |  `integer` |  End defines a network port that is the end of a port range, the End value must be greater than Start.  Support: Core   
`protocol` |  `string` |  Protocol is the network protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  Support: Core   
`start` |  `integer` |  Start defines a network port that is the start of a port range, the Start value must be less than End.  Support: Core   
Show more

## 3.1.41. .spec.subject

Description
    

Subject defines the pods to which this AdminNetworkPolicy applies. Note that host-networked pods are not included in subject selection. 

Support: Core 

Type
     `object`

Property| Type| Description  
---|---|---  
`namespaces` |  `object` |  Namespaces is used to select pods via namespace selectors.   
`pods` |  `object` |  Pods is used to select pods via namespace AND pod selectors.   
Show more

## 3.1.42. .spec.subject.namespaces

Description
     Namespaces is used to select pods via namespace selectors. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.43. .spec.subject.namespaces.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.44. .spec.subject.namespaces.matchExpressions[]

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

## 3.1.45. .spec.subject.pods

Description
     Pods is used to select pods via namespace AND pod selectors. 
Type
     `object`
Required
    

  * `namespaceSelector`
  * `podSelector`



Property| Type| Description  
---|---|---  
`namespaceSelector` |  `object` |  NamespaceSelector follows standard label selector semantics; if empty, it selects all Namespaces.   
`podSelector` |  `object` |  PodSelector is used to explicitly select pods within a namespace; if empty, it selects all Pods.   
Show more

## 3.1.46. .spec.subject.pods.namespaceSelector

Description
     NamespaceSelector follows standard label selector semantics; if empty, it selects all Namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.47. .spec.subject.pods.namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.48. .spec.subject.pods.namespaceSelector.matchExpressions[]

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

## 3.1.49. .spec.subject.pods.podSelector

Description
     PodSelector is used to explicitly select pods within a namespace; if empty, it selects all Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 3.1.50. .spec.subject.pods.podSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 3.1.51. .spec.subject.pods.podSelector.matchExpressions[]

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

## 3.1.52. .status

Description
     Status is the status to be reported by the implementation. 
Type
     `object`
Required
    

  * `conditions`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example,  type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields }   
Show more

## 3.1.53. .status.conditions

Description
    
Type
     `array`

## 3.1.54. .status.conditions[]

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
