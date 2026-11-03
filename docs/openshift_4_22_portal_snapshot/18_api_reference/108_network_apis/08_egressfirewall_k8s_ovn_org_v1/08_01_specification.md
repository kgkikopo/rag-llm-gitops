# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of the desired behavior of EgressFirewall.   
`status` |  `object` |  Observed status of EgressFirewall   
Show more

## 8.1.1. .spec

Description
     Specification of the desired behavior of EgressFirewall. 
Type
     `object`
Required
    

  * `egress`



Property| Type| Description  
---|---|---  
`egress` |  `array` |  a collection of egress firewall rule objects   
`egress[]` |  `object` |  EgressFirewallRule is a single egressfirewall rule object   
Show more

## 8.1.2. .spec.egress

Description
     a collection of egress firewall rule objects 
Type
     `array`

## 8.1.3. .spec.egress[]

Description
     EgressFirewallRule is a single egressfirewall rule object 
Type
     `object`
Required
    

  * `to`
  * `type`



Property| Type| Description  
---|---|---  
`ports` |  `array` |  ports specify what ports and protocols the rule applies to   
`ports[]` |  `object` |  EgressFirewallPort specifies the port to allow or deny traffic to   
`to` |  `object` |  to is the target that traffic is allowed/denied to   
`type` |  `string` |  type marks this as an "Allow" or "Deny" rule   
Show more

## 8.1.4. .spec.egress[].ports

Description
     ports specify what ports and protocols the rule applies to 
Type
     `array`

## 8.1.5. .spec.egress[].ports[]

Description
     EgressFirewallPort specifies the port to allow or deny traffic to 
Type
     `object`
Required
    

  * `port`
  * `protocol`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  port that the traffic must match   
`protocol` |  `string` |  protocol (tcp, udp, sctp) that the traffic must match.   
Show more

## 8.1.6. .spec.egress[].to

Description
     to is the target that traffic is allowed/denied to 
Type
     `object`

Property| Type| Description  
---|---|---  
`cidrSelector` |  `string` |  cidrSelector is the CIDR range to allow/deny traffic to. If this is set, dnsName and nodeSelector must be unset.   
`dnsName` |  `string` |  dnsName is the domain name to allow/deny traffic to. If this is set, cidrSelector and nodeSelector must be unset. For a wildcard DNS name, the '**' will match only one label. Additionally, only a single '** ' can be used at the beginning of the wildcard DNS name. For example, '*.example.com' will match 'sub1.example.com' but won’t match 'sub2.sub1.example.com'.   
`nodeSelector` |  `object` |  nodeSelector will allow/deny traffic to the Kubernetes node IP of selected nodes. If this is set, cidrSelector and DNSName must be unset.   
Show more

## 8.1.7. .spec.egress[].to.nodeSelector

Description
     nodeSelector will allow/deny traffic to the Kubernetes node IP of selected nodes. If this is set, cidrSelector and DNSName must be unset. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 8.1.8. .spec.egress[].to.nodeSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 8.1.9. .spec.egress[].to.nodeSelector.matchExpressions[]

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

## 8.1.10. .status

Description
     Observed status of EgressFirewall 
Type
     `object`

Property| Type| Description  
---|---|---  
`messages` |  `array (string)` |   
`status` |  `string` |   
Show more
