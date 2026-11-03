# 26.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  NetworkPolicySpec provides the specification of a NetworkPolicy   
Show more

## 26.1.1. .spec

Description
     NetworkPolicySpec provides the specification of a NetworkPolicy 
Type
     `object`

Property| Type| Description  
---|---|---  
`egress` |  `array` |  egress is a list of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8   
`egress[]` |  `object` |  NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods matched by a NetworkPolicySpec’s podSelector. The traffic must match both ports and to. This type is beta-level in 1.8   
`ingress` |  `array` |  ingress is a list of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod’s local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)   
`ingress[]` |  `object` |  NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods matched by a NetworkPolicySpec’s podSelector. The traffic must match both ports and from.   
`podSelector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  podSelector selects the pods to which this NetworkPolicy object applies. The array of rules is applied to any pods selected by this field. An empty selector matches all pods in the policy’s namespace. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is optional. If it is not specified, it defaults to an empty selector.   
`policyTypes` |  `array (string)` |  policyTypes is a list of rule types that the NetworkPolicy relates to. Valid options are ["Ingress"], ["Egress"], or ["Ingress", "Egress"]. If this field is not specified, it will default based on the existence of ingress or egress rules; policies that contain an egress section are assumed to affect egress, and all policies (whether or not they contain an ingress section) are assumed to affect ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8   
Show more

## 26.1.2. .spec.egress

Description
     egress is a list of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8 
Type
     `array`

## 26.1.3. .spec.egress[]

Description
     NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods matched by a NetworkPolicySpec’s podSelector. The traffic must match both ports and to. This type is beta-level in 1.8 
Type
     `object`

Property| Type| Description  
---|---|---  
`ports` |  `array` |  ports is a list of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.   
`ports[]` |  `object` |  NetworkPolicyPort describes a port to allow traffic on   
`to` |  `array` |  to is a list of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.   
`to[]` |  `object` |  NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed   
Show more

## 26.1.4. .spec.egress[].ports

Description
     ports is a list of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. 
Type
     `array`

## 26.1.5. .spec.egress[].ports[]

Description
     NetworkPolicyPort describes a port to allow traffic on 
Type
     `object`

Property| Type| Description  
---|---|---  
`endPort` |  `integer` |  endPort indicates that the range of ports from port to endPort if set, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port.   
`port` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  port represents the port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.   
`protocol` |  `string` |  protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  Possible enum values: - `"SCTP"` is the SCTP protocol. - `"TCP"` is the TCP protocol. - `"UDP"` is the UDP protocol.   
Show more

## 26.1.6. .spec.egress[].to

Description
     to is a list of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list. 
Type
     `array`

## 26.1.7. .spec.egress[].to[]

Description
     NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed 
Type
     `object`

Property| Type| Description  
---|---|---  
`ipBlock` |  `object` |  IPBlock describes a particular CIDR (Ex. "192.168.1.0/24","2001:db8::/64") that is allowed to the pods matched by a NetworkPolicySpec’s podSelector. The except entry describes CIDRs that should not be included within this rule.   
`namespaceSelector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  namespaceSelector selects namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.  If podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the namespaces selected by namespaceSelector.   
`podSelector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  podSelector is a label selector which selects pods. This field follows standard label selector semantics; if present but empty, it selects all pods.  If namespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy’s own namespace.   
Show more

## 26.1.8. .spec.egress[].to[].ipBlock

Description
     IPBlock describes a particular CIDR (Ex. "192.168.1.0/24","2001:db8::/64") that is allowed to the pods matched by a NetworkPolicySpec’s podSelector. The except entry describes CIDRs that should not be included within this rule. 
Type
     `object`
Required
    

  * `cidr`



Property| Type| Description  
---|---|---  
`cidr` |  `string` |  cidr is a string representing the IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64"   
`except` |  `array (string)` |  except is a slice of CIDRs that should not be included within an IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" Except values will be rejected if they are outside the cidr range   
Show more

## 26.1.9. .spec.ingress

Description
     ingress is a list of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod’s local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default) 
Type
     `array`

## 26.1.10. .spec.ingress[]

Description
     NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods matched by a NetworkPolicySpec’s podSelector. The traffic must match both ports and from. 
Type
     `object`

Property| Type| Description  
---|---|---  
`from` |  `array` |  from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.   
`from[]` |  `object` |  NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed   
`ports` |  `array` |  ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.   
`ports[]` |  `object` |  NetworkPolicyPort describes a port to allow traffic on   
Show more

## 26.1.11. .spec.ingress[].from

Description
     from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list. 
Type
     `array`

## 26.1.12. .spec.ingress[].from[]

Description
     NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed 
Type
     `object`

Property| Type| Description  
---|---|---  
`ipBlock` |  `object` |  IPBlock describes a particular CIDR (Ex. "192.168.1.0/24","2001:db8::/64") that is allowed to the pods matched by a NetworkPolicySpec’s podSelector. The except entry describes CIDRs that should not be included within this rule.   
`namespaceSelector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  namespaceSelector selects namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.  If podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the namespaces selected by namespaceSelector.   
`podSelector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  podSelector is a label selector which selects pods. This field follows standard label selector semantics; if present but empty, it selects all pods.  If namespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy’s own namespace.   
Show more

## 26.1.13. .spec.ingress[].from[].ipBlock

Description
     IPBlock describes a particular CIDR (Ex. "192.168.1.0/24","2001:db8::/64") that is allowed to the pods matched by a NetworkPolicySpec’s podSelector. The except entry describes CIDRs that should not be included within this rule. 
Type
     `object`
Required
    

  * `cidr`



Property| Type| Description  
---|---|---  
`cidr` |  `string` |  cidr is a string representing the IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64"   
`except` |  `array (string)` |  except is a slice of CIDRs that should not be included within an IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" Except values will be rejected if they are outside the cidr range   
Show more

## 26.1.14. .spec.ingress[].ports

Description
     ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. 
Type
     `array`

## 26.1.15. .spec.ingress[].ports[]

Description
     NetworkPolicyPort describes a port to allow traffic on 
Type
     `object`

Property| Type| Description  
---|---|---  
`endPort` |  `integer` |  endPort indicates that the range of ports from port to endPort if set, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port.   
`port` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  port represents the port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.   
`protocol` |  `string` |  protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  Possible enum values: - `"SCTP"` is the SCTP protocol. - `"TCP"` is the TCP protocol. - `"UDP"` is the UDP protocol.   
Show more
