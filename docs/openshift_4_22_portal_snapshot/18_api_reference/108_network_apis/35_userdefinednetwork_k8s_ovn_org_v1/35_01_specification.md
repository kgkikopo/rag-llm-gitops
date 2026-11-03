# 35.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  UserDefinedNetworkSpec defines the desired state of UserDefinedNetworkSpec.   
`status` |  `object` |  UserDefinedNetworkStatus contains the observed status of the UserDefinedNetwork.   
Show more

## 35.1.1. .spec

Description
     UserDefinedNetworkSpec defines the desired state of UserDefinedNetworkSpec. 
Type
     `object`
Required
    

  * `topology`



Property| Type| Description  
---|---|---  
`layer2` |  `object` |  Layer2 is the Layer2 topology configuration.   
`layer3` |  `object` |  Layer3 is the Layer3 topology configuration.   
`topology` |  `string` |  Topology describes network configuration.  Allowed values are "Layer3", "Layer2". Layer3 topology creates a layer 2 segment per node, each with a different subnet. Layer 3 routing is used to interconnect node subnets. Layer2 topology creates one logical switch shared by all nodes.   
Show more

## 35.1.2. .spec.layer2

Description
     Layer2 is the Layer2 topology configuration. 
Type
     `object`
Required
    

  * `role`



Property| Type| Description  
---|---|---  
`defaultGatewayIPs` |  `array (string)` |  defaultGatewayIPs specifies the default gateway IP used in the internal OVN topology.  Dual-stack clusters may set 2 IPs (one for each IP family), otherwise only 1 IP is allowed. This field is only allowed for "Primary" network. It is not recommended to set this field without explicit need and understanding of the OVN network topology. When omitted, an IP from the subnets field is used.   
`infrastructureSubnets` |  `array (string)` |  infrastructureSubnets specifies a list of internal CIDR ranges that OVN-Kubernetes will reserve for internal network infrastructure. Any IP addresses within these ranges cannot be assigned to workloads. When omitted, OVN-Kubernetes will automatically allocate IP addresses from `subnets` for its infrastructure needs. When there are not enough available IPs in the provided infrastructureSubnets, OVN-Kubernetes will automatically allocate IP addresses from subnets for its infrastructure needs. When `reservedSubnets` is also specified the CIDRs cannot overlap. When `defaultGatewayIPs` is also specified, the default gateway IPs must belong to one of the infrastructure subnet CIDRs. Each item should be in range of the specified CIDR(s) in `subnets`. The maximum number of entries allowed is 4. The format should match standard CIDR notation (for example, "10.128.0.0/16"). This field must be omitted if `subnets` is unset or `ipam.mode` is `Disabled`.   
`ipam` |  `object` |  IPAM section contains IPAM-related configuration for the network.   
`joinSubnets` |  `array (string)` |  JoinSubnets are used inside the OVN network topology.  Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. This field is only allowed for "Primary" network. It is not recommended to set this field without explicit need and understanding of the OVN network topology. When omitted, the platform will choose a reasonable default which is subject to change over time.   
`mtu` |  `integer` |  MTU is the maximum transmission unit for a network. MTU is optional, if not provided, the globally configured value in OVN-Kubernetes (defaults to 1400) is used for the network.   
`reservedSubnets` |  `array (string)` |  reservedSubnets specifies a list of CIDRs reserved for static IP assignment, excluded from automatic allocation. reservedSubnets is optional. When omitted, all IP addresses in `subnets` are available for automatic assignment. IPs from these ranges can still be requested through static IP assignment. Each item should be in range of the specified CIDR(s) in `subnets`. The maximum number of entries allowed is 25. The format should match standard CIDR notation (for example, "10.128.0.0/16"). This field must be omitted if `subnets` is unset or `ipam.mode` is `Disabled`.   
`role` |  `string` |  Role describes the network role in the pod.  Allowed value is "Secondary". Secondary network is only assigned to pods that use `k8s.v1.cni.cncf.io/networks` annotation to select given network.   
`subnets` |  `array (string)` |  Subnets are used for the pod network across the cluster. Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed.  The format should match standard CIDR notation (for example, "10.128.0.0/16"). This field must be omitted if `ipam.mode` is `Disabled`.   
Show more

## 35.1.3. .spec.layer2.ipam

Description
     IPAM section contains IPAM-related configuration for the network. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lifecycle` |  `string` |  Lifecycle controls IP addresses management lifecycle.  The only allowed value is Persistent. When set, OVN Kubernetes assigned IP addresses will be persisted in an `ipamclaims.k8s.cni.cncf.io` object. These IP addresses will be reused by other pods if requested. Only supported when mode is `Enabled`.   
`mode` |  `string` |  Mode controls how much of the IP configuration will be managed by OVN. `Enabled` means OVN-Kubernetes will apply IP configuration to the SDN infrastructure and it will also assign IPs from the selected subnet to the individual pods. `Disabled` means OVN-Kubernetes will only assign MAC addresses and provide layer 2 communication, letting users configure IP addresses for the pods. `Disabled` is only available for Secondary networks. By disabling IPAM, any Kubernetes features that rely on selecting pods by IP will no longer function (such as network policy, services, etc). Additionally, IP port security will also be disabled for interfaces attached to this network. Defaults to `Enabled`.   
Show more

## 35.1.4. .spec.layer3

Description
     Layer3 is the Layer3 topology configuration. 
Type
     `object`
Required
    

  * `role`
  * `subnets`



Property| Type| Description  
---|---|---  
`joinSubnets` |  `array (string)` |  JoinSubnets are used inside the OVN network topology.  Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. This field is only allowed for "Primary" network. It is not recommended to set this field without explicit need and understanding of the OVN network topology. When omitted, the platform will choose a reasonable default which is subject to change over time.   
`mtu` |  `integer` |  MTU is the maximum transmission unit for a network.  MTU is optional, if not provided, the globally configured value in OVN-Kubernetes (defaults to 1400) is used for the network.   
`role` |  `string` |  Role describes the network role in the pod.  Allowed values are "Primary" and "Secondary". Primary network is automatically assigned to every pod created in the same namespace. Secondary network is only assigned to pods that use `k8s.v1.cni.cncf.io/networks` annotation to select given network.   
`subnets` |  `array` |  Subnets are used for the pod network across the cluster.  Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. Given subnet is split into smaller subnets for every node.   
`subnets[]` |  `object` |   
Show more

## 35.1.5. .spec.layer3.subnets

Description
    

Subnets are used for the pod network across the cluster. 

Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. Given subnet is split into smaller subnets for every node. 

Type
     `array`

## 35.1.6. .spec.layer3.subnets[]

Description
    
Type
     `object`
Required
    

  * `cidr`



Property| Type| Description  
---|---|---  
`cidr` |  `string` |  CIDR specifies L3Subnet, which is split into smaller subnets for every node.   
`hostSubnet` |  `integer` |  HostSubnet specifies the subnet size for every node.  When not set, it will be assigned automatically.   
Show more

## 35.1.7. .status

Description
     UserDefinedNetworkStatus contains the observed status of the UserDefinedNetwork. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
Show more

## 35.1.8. .status.conditions

Description
    
Type
     `array`

## 35.1.9. .status.conditions[]

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
