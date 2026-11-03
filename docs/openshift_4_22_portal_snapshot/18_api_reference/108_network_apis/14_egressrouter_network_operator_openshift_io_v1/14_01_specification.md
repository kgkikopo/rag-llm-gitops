# 14.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of the desired egress router.   
`status` |  `object` |  Observed status of EgressRouter.   
Show more

## 14.1.1. .spec

Description
     Specification of the desired egress router. 
Type
     `object`
Required
    

  * `addresses`
  * `mode`
  * `networkInterface`



Property| Type| Description  
---|---|---  
`addresses` |  `array` |  List of IP addresses to configure on the pod’s secondary interface.   
`addresses[]` |  `object` |  EgressRouterAddress contains a pair of IP CIDR and gateway to be configured on the router’s interface   
`mode` |  `string` |  mode depicts the mode that is used for the egress router. The default mode is "Redirect" and is the only supported mode currently.   
`networkInterface` |  `object` |  Specification of interface to create/use. The default is macvlan. Currently only macvlan is supported.   
`redirect` |  `object` |  redirect represents the configuration parameters specific to redirect mode.   
Show more

## 14.1.2. .spec.addresses

Description
     List of IP addresses to configure on the pod’s secondary interface. 
Type
     `array`

## 14.1.3. .spec.addresses[]

Description
     EgressRouterAddress contains a pair of IP CIDR and gateway to be configured on the router’s interface 
Type
     `object`
Required
    

  * `ip`



Property| Type| Description  
---|---|---  
`gateway` |  `string` |  IP address of the next-hop gateway, if it cannot be automatically determined. Can be IPv4 or IPv6.   
`ip` |  `string` |  ip is the address to configure on the router’s interface. Can be IPv4 or IPv6.   
Show more

## 14.1.4. .spec.networkInterface

Description
     Specification of interface to create/use. The default is macvlan. Currently only macvlan is supported. 
Type
     `object`

Property| Type| Description  
---|---|---  
`macvlan` |  `object` |  Arguments specific to the interfaceType macvlan   
Show more

## 14.1.5. .spec.networkInterface.macvlan

Description
     Arguments specific to the interfaceType macvlan 
Type
     `object`
Required
    

  * `mode`



Property| Type| Description  
---|---|---  
`master` |  `string` |  Name of the master interface. Need not be specified if it can be inferred from the IP address.   
`mode` |  `string` |  mode depicts the mode that is used for the macvlan interface; one of Bridge|Private|VEPA|Passthru. The default mode is "Bridge".   
Show more

## 14.1.6. .spec.redirect

Description
     redirect represents the configuration parameters specific to redirect mode. 
Type
     `object`

Property| Type| Description  
---|---|---  
`fallbackIP` |  `string` |  fallbackIP specifies the remote destination’s IP address. Can be IPv4 or IPv6. If no redirect rules are specified, all traffic from the router are redirected to this IP. If redirect rules are specified, then any connections on any other port (undefined in the rules) on the router will be redirected to this IP. If redirect rules are specified and no fallback IP is provided, connections on other ports will simply be rejected.   
`redirectRules` |  `array` |  List of L4RedirectRules that define the DNAT redirection from the pod to the destination in redirect mode.   
`redirectRules[]` |  `object` |  L4RedirectRule defines a DNAT redirection from a given port to a destination IP and port.   
Show more

## 14.1.7. .spec.redirect.redirectRules

Description
     List of L4RedirectRules that define the DNAT redirection from the pod to the destination in redirect mode. 
Type
     `array`

## 14.1.8. .spec.redirect.redirectRules[]

Description
     L4RedirectRule defines a DNAT redirection from a given port to a destination IP and port. 
Type
     `object`
Required
    

  * `destinationIP`
  * `port`
  * `protocol`



Property| Type| Description  
---|---|---  
`destinationIP` |  `string` |  IP specifies the remote destination’s IP address. Can be IPv4 or IPv6.   
`port` |  `integer` |  port is the port number to which clients should send traffic to be redirected.   
`protocol` |  `string` |  protocol can be TCP, SCTP or UDP.   
`targetPort` |  `integer` |  targetPort allows specifying the port number on the remote destination to which the traffic gets redirected to. If unspecified, the value from "Port" is used.   
Show more

## 14.1.9. .status

Description
     Observed status of EgressRouter. 
Type
     `object`
Required
    

  * `conditions`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  Observed status of the egress router   
`conditions[]` |  `object` |  EgressRouterStatusCondition represents the state of the egress router’s managed and monitored components.   
Show more

## 14.1.10. .status.conditions

Description
     Observed status of the egress router 
Type
     `array`

## 14.1.11. .status.conditions[]

Description
     EgressRouterStatusCondition represents the state of the egress router’s managed and monitored components. 
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  ``  |  lastTransitionTime is the time of the last update to the current status property.   
`message` |  `string` |  message provides additional information about the current condition. This is only to be consumed by humans. It may contain Line Feed characters (U+000A), which should be rendered as new lines.   
`reason` |  `string` |  reason is the CamelCase reason for the condition’s current status.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type specifies the aspect reported by this condition; one of Available, Progressing, Degraded   
Show more
