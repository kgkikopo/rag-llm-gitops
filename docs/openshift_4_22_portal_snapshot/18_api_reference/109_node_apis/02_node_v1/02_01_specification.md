# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  NodeSpec describes the attributes that a node is created with.   
`status` |  `object` |  NodeStatus is information about the current status of a node.   
Show more

## 2.1.1. .spec

Description
     NodeSpec describes the attributes that a node is created with. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configSource` |  `object` |  NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22   
`externalID` |  `string` |  Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: <https://issues.k8s.io/61966>  
`podCIDR` |  `string` |  PodCIDR represents the pod IP range assigned to the node.   
`podCIDRs` |  `array (string)` |  podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.   
`providerID` |  `string` |  ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>  
`taints` |  `array` |  If specified, the node’s taints.   
`taints[]` |  `object` |  The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.   
`unschedulable` |  `boolean` |  Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: <https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration>  
Show more

## 2.1.2. .spec.configSource

Description
     NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>  
Show more

## 2.1.3. .spec.configSource.configMap

Description
     ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>
Type
     `object`
Required
    

  * `namespace`
  * `name`
  * `kubeletConfigKey`



Property| Type| Description  
---|---|---  
`kubeletConfigKey` |  `string` |  KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.   
`name` |  `string` |  Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.   
`namespace` |  `string` |  Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.   
`resourceVersion` |  `string` |  ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
`uid` |  `string` |  UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
Show more

## 2.1.4. .spec.taints

Description
     If specified, the node’s taints. 
Type
     `array`

## 2.1.5. .spec.taints[]

Description
     The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint. 
Type
     `object`
Required
    

  * `key`
  * `effect`



Property| Type| Description  
---|---|---  
`effect` |  `string` |  Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController. - `"NoSchedule"` Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler. - `"PreferNoSchedule"` Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler.   
`key` |  `string` |  Required. The taint key to be applied to a node.   
`timeAdded` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  TimeAdded represents the time at which the taint was added.   
`value` |  `string` |  The taint value corresponding to the taint key.   
Show more

## 2.1.6. .status

Description
     NodeStatus is information about the current status of a node. 
Type
     `object`

Property| Type| Description  
---|---|---  
`addresses` |  `array` |  List of addresses reachable to the node. Queried from cloud provider, if available. More info: <https://kubernetes.io/docs/reference/node/node-status/#addresses> Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See <https://pr.k8s.io/79391> for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node’s address in its own status or consumers of the downward API (status.hostIP).   
`addresses[]` |  `object` |  NodeAddress contains information for the node’s address.   
`allocatable` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.   
`capacity` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Capacity represents the total resources of a node. More info: <https://kubernetes.io/docs/reference/node/node-status/#capacity>  
`conditions` |  `array` |  Conditions is an array of current observed node conditions. More info: <https://kubernetes.io/docs/reference/node/node-status/#condition>  
`conditions[]` |  `object` |  NodeCondition contains condition information for a node.   
`config` |  `object` |  NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.   
`daemonEndpoints` |  `object` |  NodeDaemonEndpoints lists ports opened by daemons running on the Node.   
`declaredFeatures` |  `array (string)` |  DeclaredFeatures represents the features related to feature gates that are declared by the node.   
`features` |  `object` |  NodeFeatures describes the set of features implemented by the CRI implementation. The features contained in the NodeFeatures should depend only on the cri implementation independent of runtime handlers.   
`images` |  `array` |  List of container images on this node   
`images[]` |  `object` |  Describe a container image   
`nodeInfo` |  `object` |  NodeSystemInfo is a set of ids/uuids to uniquely identify the node.   
`phase` |  `string` |  NodePhase is the recently observed lifecycle phase of the node. More info: <https://kubernetes.io/docs/concepts/nodes/node/#phase> The field is never populated, and now is deprecated.  Possible enum values: - `"Pending"` means the node has been created/added by the system, but not configured. - `"Running"` means the node has been configured and has Kubernetes components running. - `"Terminated"` means the node has been removed from the cluster.   
`runtimeHandlers` |  `array` |  The available runtime handlers.   
`runtimeHandlers[]` |  `object` |  NodeRuntimeHandler is a set of runtime handler information.   
`volumesAttached` |  `array` |  List of volumes that are attached to the node.   
`volumesAttached[]` |  `object` |  AttachedVolume describes a volume attached to a node   
`volumesInUse` |  `array (string)` |  List of attachable volumes in use (mounted) by the node.   
Show more

## 2.1.7. .status.addresses

Description
     List of addresses reachable to the node. Queried from cloud provider, if available. More info: <https://kubernetes.io/docs/reference/node/node-status/#addresses> Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See <https://pr.k8s.io/79391> for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node’s address in its own status or consumers of the downward API (status.hostIP). 
Type
     `array`

## 2.1.8. .status.addresses[]

Description
     NodeAddress contains information for the node’s address. 
Type
     `object`
Required
    

  * `type`
  * `address`



Property| Type| Description  
---|---|---  
`address` |  `string` |  The node address.   
`type` |  `string` |  Node address type, one of Hostname, ExternalIP or InternalIP.   
Show more

## 2.1.9. .status.conditions

Description
     Conditions is an array of current observed node conditions. More info: <https://kubernetes.io/docs/reference/node/node-status/#condition>
Type
     `array`

## 2.1.10. .status.conditions[]

Description
     NodeCondition contains condition information for a node. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastHeartbeatTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time we got an update on a given condition.   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transit from one status to another.   
`message` |  `string` |  Human readable message indicating details about last transition.   
`reason` |  `string` |  (brief) reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of node condition.   
Show more

## 2.1.11. .status.config

Description
     NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`active` |  `object` |  NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22   
`assigned` |  `object` |  NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22   
`error` |  `string` |  Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.   
`lastKnownGood` |  `object` |  NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22   
Show more

## 2.1.12. .status.config.active

Description
     NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>  
Show more

## 2.1.13. .status.config.active.configMap

Description
     ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>
Type
     `object`
Required
    

  * `namespace`
  * `name`
  * `kubeletConfigKey`



Property| Type| Description  
---|---|---  
`kubeletConfigKey` |  `string` |  KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.   
`name` |  `string` |  Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.   
`namespace` |  `string` |  Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.   
`resourceVersion` |  `string` |  ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
`uid` |  `string` |  UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
Show more

## 2.1.14. .status.config.assigned

Description
     NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>  
Show more

## 2.1.15. .status.config.assigned.configMap

Description
     ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>
Type
     `object`
Required
    

  * `namespace`
  * `name`
  * `kubeletConfigKey`



Property| Type| Description  
---|---|---  
`kubeletConfigKey` |  `string` |  KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.   
`name` |  `string` |  Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.   
`namespace` |  `string` |  Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.   
`resourceVersion` |  `string` |  ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
`uid` |  `string` |  UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
Show more

## 2.1.16. .status.config.lastKnownGood

Description
     NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>  
Show more

## 2.1.17. .status.config.lastKnownGood.configMap

Description
     ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>
Type
     `object`
Required
    

  * `namespace`
  * `name`
  * `kubeletConfigKey`



Property| Type| Description  
---|---|---  
`kubeletConfigKey` |  `string` |  KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.   
`name` |  `string` |  Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.   
`namespace` |  `string` |  Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.   
`resourceVersion` |  `string` |  ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
`uid` |  `string` |  UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.   
Show more

## 2.1.18. .status.daemonEndpoints

Description
     NodeDaemonEndpoints lists ports opened by daemons running on the Node. 
Type
     `object`

Property| Type| Description  
---|---|---  
`kubeletEndpoint` |  `object` |  DaemonEndpoint contains information about a single Daemon endpoint.   
Show more

## 2.1.19. .status.daemonEndpoints.kubeletEndpoint

Description
     DaemonEndpoint contains information about a single Daemon endpoint. 
Type
     `object`
Required
    

  * `Port`



Property| Type| Description  
---|---|---  
`Port` |  `integer` |  Port number of the given endpoint.   
Show more

## 2.1.20. .status.features

Description
     NodeFeatures describes the set of features implemented by the CRI implementation. The features contained in the NodeFeatures should depend only on the cri implementation independent of runtime handlers. 
Type
     `object`

Property| Type| Description  
---|---|---  
`supplementalGroupsPolicy` |  `boolean` |  SupplementalGroupsPolicy is set to true if the runtime supports SupplementalGroupsPolicy and ContainerUser.   
Show more

## 2.1.21. .status.images

Description
     List of container images on this node 
Type
     `array`

## 2.1.22. .status.images[]

Description
     Describe a container image 
Type
     `object`

Property| Type| Description  
---|---|---  
`names` |  `array (string)` |  Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"]   
`sizeBytes` |  `integer` |  The size of the image in bytes.   
Show more

## 2.1.23. .status.nodeInfo

Description
     NodeSystemInfo is a set of ids/uuids to uniquely identify the node. 
Type
     `object`
Required
    

  * `machineID`
  * `systemUUID`
  * `bootID`
  * `kernelVersion`
  * `osImage`
  * `containerRuntimeVersion`
  * `kubeletVersion`
  * `kubeProxyVersion`
  * `operatingSystem`
  * `architecture`



Property| Type| Description  
---|---|---  
`architecture` |  `string` |  The Architecture reported by the node   
`bootID` |  `string` |  Boot ID reported by the node.   
`containerRuntimeVersion` |  `string` |  ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).   
`kernelVersion` |  `string` |  Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).   
`kubeProxyVersion` |  `string` |  Deprecated: KubeProxy Version reported by the node.   
`kubeletVersion` |  `string` |  Kubelet Version reported by the node.   
`machineID` |  `string` |  MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: <http://man7.org/linux/man-pages/man5/machine-id.5.html>  
`operatingSystem` |  `string` |  The Operating System reported by the node   
`osImage` |  `string` |  OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).   
`swap` |  `object` |  NodeSwapStatus represents swap memory information.   
`systemUUID` |  `string` |  SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts <https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid>  
Show more

## 2.1.24. .status.nodeInfo.swap

Description
     NodeSwapStatus represents swap memory information. 
Type
     `object`

Property| Type| Description  
---|---|---  
`capacity` |  `integer` |  Total amount of swap memory in bytes.   
Show more

## 2.1.25. .status.runtimeHandlers

Description
     The available runtime handlers. 
Type
     `array`

## 2.1.26. .status.runtimeHandlers[]

Description
     NodeRuntimeHandler is a set of runtime handler information. 
Type
     `object`

Property| Type| Description  
---|---|---  
`features` |  `object` |  NodeRuntimeHandlerFeatures is a set of features implemented by the runtime handler.   
`name` |  `string` |  Runtime handler name. Empty for the default runtime handler.   
Show more

## 2.1.27. .status.runtimeHandlers[].features

Description
     NodeRuntimeHandlerFeatures is a set of features implemented by the runtime handler. 
Type
     `object`

Property| Type| Description  
---|---|---  
`recursiveReadOnlyMounts` |  `boolean` |  RecursiveReadOnlyMounts is set to true if the runtime handler supports RecursiveReadOnlyMounts.   
`userNamespaces` |  `boolean` |  UserNamespaces is set to true if the runtime handler supports UserNamespaces, including for volumes.   
Show more

## 2.1.28. .status.volumesAttached

Description
     List of volumes that are attached to the node. 
Type
     `array`

## 2.1.29. .status.volumesAttached[]

Description
     AttachedVolume describes a volume attached to a node 
Type
     `object`
Required
    

  * `name`
  * `devicePath`



Property| Type| Description  
---|---|---  
`devicePath` |  `string` |  DevicePath represents the device path where the volume should be available   
`name` |  `string` |  Name of the attached volume   
Show more
