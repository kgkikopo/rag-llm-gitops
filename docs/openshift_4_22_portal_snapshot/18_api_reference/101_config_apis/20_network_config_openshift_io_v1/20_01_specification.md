# 20.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration. As a general rule, this SHOULD NOT be read directly. Instead, you should consume the NetworkStatus, as it indicates the currently deployed configuration. Currently, most spec fields are immutable after installation. Please view the individual ones for further details on each.   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 20.1.1. .spec

Description
     spec holds user settable values for configuration. As a general rule, this SHOULD NOT be read directly. Instead, you should consume the NetworkStatus, as it indicates the currently deployed configuration. Currently, most spec fields are immutable after installation. Please view the individual ones for further details on each. 
Type
     `object`

Property| Type| Description  
---|---|---  
`clusterNetwork` |  `array` |  IP address pool to use for pod IPs. This field is immutable after installation.   
`clusterNetwork[]` |  `object` |  ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated.   
`externalIP` |  `object` |  externalIP defines configuration for controllers that affect Service.ExternalIP. If nil, then ExternalIP is not allowed to be set.   
`networkDiagnostics` |  `object` |  networkDiagnostics defines network diagnostics configuration.  Takes precedence over spec.disableNetworkDiagnostics in network.operator.openshift.io. If networkDiagnostics is not specified or is empty, and the spec.disableNetworkDiagnostics flag in network.operator.openshift.io is set to true, the network diagnostics feature will be disabled.   
`networkType` |  `string` |  networkType is the plugin that is to be deployed (e.g. OVNKubernetes). This should match a value that the cluster-network-operator understands, or else no networking will be installed. Currently supported values are: - OVNKubernetes This field is immutable after installation.   
`serviceNetwork` |  `array (string)` |  IP address pool for services. Currently, we only support a single entry here. This field is immutable after installation.   
`serviceNodePortRange` |  `string` |  The port range allowed for Services of type NodePort. If not specified, the default of 30000-32767 will be used. Such Services without a NodePort specified will have one automatically allocated from this range. This parameter can be updated after the cluster is installed.   
Show more

## 20.1.2. .spec.clusterNetwork

Description
     IP address pool to use for pod IPs. This field is immutable after installation. 
Type
     `array`

## 20.1.3. .spec.clusterNetwork[]

Description
     ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated. 
Type
     `object`

Property| Type| Description  
---|---|---  
`cidr` |  `string` |  The complete block for pod IPs.   
`hostPrefix` |  `integer` |  The size (prefix) of block to allocate to each node. If this field is not used by the plugin, it can be left unset.   
Show more

## 20.1.4. .spec.externalIP

Description
     externalIP defines configuration for controllers that affect Service.ExternalIP. If nil, then ExternalIP is not allowed to be set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`autoAssignCIDRs` |  `array (string)` |  autoAssignCIDRs is a list of CIDRs from which to automatically assign Service.ExternalIP. These are assigned when the service is of type LoadBalancer. In general, this is only useful for bare-metal clusters. In Openshift 3.x, this was misleadingly called "IngressIPs". Automatically assigned External IPs are not affected by any ExternalIPPolicy rules. Currently, only one entry may be provided.   
`policy` |  `object` |  policy is a set of restrictions applied to the ExternalIP field. If nil or empty, then ExternalIP is not allowed to be set.   
Show more

## 20.1.5. .spec.externalIP.policy

Description
     policy is a set of restrictions applied to the ExternalIP field. If nil or empty, then ExternalIP is not allowed to be set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`allowedCIDRs` |  `array (string)` |  allowedCIDRs is the list of allowed CIDRs.   
`rejectedCIDRs` |  `array (string)` |  rejectedCIDRs is the list of disallowed CIDRs. These take precedence over allowedCIDRs.   
Show more

## 20.1.6. .spec.networkDiagnostics

Description
    

networkDiagnostics defines network diagnostics configuration. 

Takes precedence over spec.disableNetworkDiagnostics in network.operator.openshift.io. If networkDiagnostics is not specified or is empty, and the spec.disableNetworkDiagnostics flag in network.operator.openshift.io is set to true, the network diagnostics feature will be disabled. 

Type
     `object`

Property| Type| Description  
---|---|---  
`mode` |  `string` |  mode controls the network diagnostics mode  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is All.   
`sourcePlacement` |  `object` |  sourcePlacement controls the scheduling of network diagnostics source deployment  See NetworkDiagnosticsSourcePlacement for more details about default values.   
`targetPlacement` |  `object` |  targetPlacement controls the scheduling of network diagnostics target daemonset  See NetworkDiagnosticsTargetPlacement for more details about default values.   
Show more

## 20.1.7. .spec.networkDiagnostics.sourcePlacement

Description
    

sourcePlacement controls the scheduling of network diagnostics source deployment 

See NetworkDiagnosticsSourcePlacement for more details about default values. 

Type
     `object`

Property| Type| Description  
---|---|---  
`nodeSelector` |  `object (string)` |  nodeSelector is the node selector applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `kubernetes.io/os: linux`.   
`tolerations` |  `array` |  tolerations is a list of tolerations applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is an empty list.   
`tolerations[]` |  `object` |  The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.   
Show more

## 20.1.8. .spec.networkDiagnostics.sourcePlacement.tolerations

Description
    

tolerations is a list of tolerations applied to network diagnostics components 

When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is an empty list. 

Type
     `array`

## 20.1.9. .spec.networkDiagnostics.sourcePlacement.tolerations[]

Description
     The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. 
Type
     `object`

Property| Type| Description  
---|---|---  
`effect` |  `string` |  Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.   
`key` |  `string` |  Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.   
`operator` |  `string` |  Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators).   
`tolerationSeconds` |  `integer` |  TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.   
`value` |  `string` |  Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.   
Show more

## 20.1.10. .spec.networkDiagnostics.targetPlacement

Description
    

targetPlacement controls the scheduling of network diagnostics target daemonset 

See NetworkDiagnosticsTargetPlacement for more details about default values. 

Type
     `object`

Property| Type| Description  
---|---|---  
`nodeSelector` |  `object (string)` |  nodeSelector is the node selector applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `kubernetes.io/os: linux`.   
`tolerations` |  `array` |  tolerations is a list of tolerations applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `- operator: "Exists"` which means that all taints are tolerated.   
`tolerations[]` |  `object` |  The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.   
Show more

## 20.1.11. .spec.networkDiagnostics.targetPlacement.tolerations

Description
    

tolerations is a list of tolerations applied to network diagnostics components 

When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `- operator: "Exists"` which means that all taints are tolerated. 

Type
     `array`

## 20.1.12. .spec.networkDiagnostics.targetPlacement.tolerations[]

Description
     The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. 
Type
     `object`

Property| Type| Description  
---|---|---  
`effect` |  `string` |  Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.   
`key` |  `string` |  Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.   
`operator` |  `string` |  Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators).   
`tolerationSeconds` |  `integer` |  TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.   
`value` |  `string` |  Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.   
Show more

## 20.1.13. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`

Property| Type| Description  
---|---|---  
`clusterNetwork` |  `array` |  IP address pool to use for pod IPs.   
`clusterNetwork[]` |  `object` |  ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated.   
`clusterNetworkMTU` |  `integer` |  clusterNetworkMTU is the MTU for inter-pod networking.   
`conditions` |  `array` |  conditions represents the observations of a network.config current state. Known .status.conditions.type are: "NetworkDiagnosticsAvailable"   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`migration` |  `object` |  migration contains the cluster network migration configuration.   
`networkType` |  `string` |  networkType is the plugin that is deployed (e.g. OVNKubernetes).   
`serviceNetwork` |  `array (string)` |  IP address pool for services. Currently, we only support a single entry here.   
Show more

## 20.1.14. .status.clusterNetwork

Description
     IP address pool to use for pod IPs. 
Type
     `array`

## 20.1.15. .status.clusterNetwork[]

Description
     ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated. 
Type
     `object`

Property| Type| Description  
---|---|---  
`cidr` |  `string` |  The complete block for pod IPs.   
`hostPrefix` |  `integer` |  The size (prefix) of block to allocate to each node. If this field is not used by the plugin, it can be left unset.   
Show more

## 20.1.16. .status.conditions

Description
     conditions represents the observations of a network.config current state. Known .status.conditions.type are: "NetworkDiagnosticsAvailable" 
Type
     `array`

## 20.1.17. .status.conditions[]

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

## 20.1.18. .status.migration

Description
     migration contains the cluster network migration configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`mtu` |  `object` |  mtu is the MTU configuration that is being deployed.   
`networkType` |  `string` |  networkType is the target plugin that is being deployed. DEPRECATED: network type migration is no longer supported, so this should always be unset.   
Show more

## 20.1.19. .status.migration.mtu

Description
     mtu is the MTU configuration that is being deployed. 
Type
     `object`

Property| Type| Description  
---|---|---  
`machine` |  `object` |  machine contains MTU migration configuration for the machine’s uplink.   
`network` |  `object` |  network contains MTU migration configuration for the default network.   
Show more

## 20.1.20. .status.migration.mtu.machine

Description
     machine contains MTU migration configuration for the machine’s uplink. 
Type
     `object`

Property| Type| Description  
---|---|---  
`from` |  `integer` |  from is the MTU to migrate from.   
`to` |  `integer` |  to is the MTU to migrate to.   
Show more

## 20.1.21. .status.migration.mtu.network

Description
     network contains MTU migration configuration for the default network. 
Type
     `object`

Property| Type| Description  
---|---|---  
`from` |  `integer` |  from is the MTU to migrate from.   
`to` |  `integer` |  to is the MTU to migrate to.   
Show more
