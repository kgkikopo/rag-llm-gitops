# 11.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec describes the configuration of the machine config node.   
`status` |  `object` |  status describes the last observed state of this machine config node.   
Show more

## 11.1.1. .spec

Description
     spec describes the configuration of the machine config node. 
Type
     `object`
Required
    

  * `configVersion`
  * `node`
  * `pool`



Property| Type| Description  
---|---|---  
`configVersion` |  `object` |  configVersion holds the desired config version for the node targeted by this machine config node resource. The desired version represents the machine config the node will attempt to update to and gets set before the machine config operator validates the new machine config against the current machine config.   
`node` |  `object` |  node contains a reference to the node for this machine config node.   
`pool` |  `object` |  pool contains a reference to the machine config pool that this machine config node’s referenced node belongs to.   
Show more

## 11.1.2. .spec.configVersion

Description
     configVersion holds the desired config version for the node targeted by this machine config node resource. The desired version represents the machine config the node will attempt to update to and gets set before the machine config operator validates the new machine config against the current machine config. 
Type
     `object`
Required
    

  * `desired`



Property| Type| Description  
---|---|---  
`desired` |  `string` |  desired is the name of the machine config that the the node should be upgraded to. This value is set when the machine config pool generates a new version of its rendered configuration. When this value is changed, the machine config daemon starts the node upgrade process. This value gets set in the machine config node spec once the machine config has been targeted for upgrade and before it is validated. Must be a lowercase RFC-1123 subdomain name (<https://tools.ietf.org/html/rfc1123>) consisting of only lowercase alphanumeric characters, hyphens (-), and periods (.), and must start and end with an alphanumeric character, and be at most 253 characters in length.   
Show more

## 11.1.3. .spec.node

Description
     node contains a reference to the node for this machine config node. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the object being referenced. For example, this can represent a machine config pool or node name. Must be a lowercase RFC-1123 subdomain name (<https://tools.ietf.org/html/rfc1123>) consisting of only lowercase alphanumeric characters, hyphens (-), and periods (.), and must start and end with an alphanumeric character, and be at most 253 characters in length.   
Show more

## 11.1.4. .spec.pool

Description
     pool contains a reference to the machine config pool that this machine config node’s referenced node belongs to. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the object being referenced. For example, this can represent a machine config pool or node name. Must be a lowercase RFC-1123 subdomain name (<https://tools.ietf.org/html/rfc1123>) consisting of only lowercase alphanumeric characters, hyphens (-), and periods (.), and must start and end with an alphanumeric character, and be at most 253 characters in length.   
Show more

## 11.1.5. .status

Description
     status describes the last observed state of this machine config node. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represent the observations of a machine config node’s current state. Valid types are: UpdatePrepared, UpdateExecuted, UpdatePostActionComplete, UpdateComplete, Updated, Resumed, Drained, AppliedFilesAndOS, Cordoned, Uncordoned, RebootedNode, NodeDegraded, PinnedImageSetsProgressing, and PinnedImageSetsDegraded. The following types are only available when the ImageModeStatusReporting feature gate is enabled: ImagePulledFromRegistry, AppliedOSImage, AppliedFiles The following types are only available when the NoRegistryClusterInstall feature gate is enabled: InternalReleaseImageDegraded   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`configVersion` |  `object` |  configVersion describes the current and desired machine config version for this node.   
`observedGeneration` |  `integer` |  observedGeneration represents the generation of the MachineConfigNode object observed by the Machine Config Operator’s controller. This field is updated when the controller observes a change to the desiredConfig in the configVersion of the machine config node spec.   
`pinnedImageSets` |  `array` |  pinnedImageSets describes the current and desired pinned image sets for this node.   
`pinnedImageSets[]` |  `object` |  MachineConfigNodeStatusPinnedImageSet holds information about the current, desired, and failed pinned image sets for the observed machine config node.   
Show more

## 11.1.6. .status.conditions

Description
     conditions represent the observations of a machine config node’s current state. Valid types are: UpdatePrepared, UpdateExecuted, UpdatePostActionComplete, UpdateComplete, Updated, Resumed, Drained, AppliedFilesAndOS, Cordoned, Uncordoned, RebootedNode, NodeDegraded, PinnedImageSetsProgressing, and PinnedImageSetsDegraded. The following types are only available when the ImageModeStatusReporting feature gate is enabled: ImagePulledFromRegistry, AppliedOSImage, AppliedFiles The following types are only available when the NoRegistryClusterInstall feature gate is enabled: InternalReleaseImageDegraded 
Type
     `array`

## 11.1.7. .status.conditions[]

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

## 11.1.8. .status.configVersion

Description
     configVersion describes the current and desired machine config version for this node. 
Type
     `object`
Required
    

  * `desired`



Property| Type| Description  
---|---|---  
`current` |  `string` |  current is the name of the machine config currently in use on the node. This value is updated once the machine config daemon has completed the update of the configuration for the node. This value should match the desired version unless an upgrade is in progress. Must be a lowercase RFC-1123 subdomain name (<https://tools.ietf.org/html/rfc1123>) consisting of only lowercase alphanumeric characters, hyphens (-), and periods (.), and must start and end with an alphanumeric character, and be at most 253 characters in length.   
`desired` |  `string` |  desired is the MachineConfig the node wants to upgrade to. This value gets set in the machine config node status once the machine config has been validated against the current machine config. Must be a lowercase RFC-1123 subdomain name (<https://tools.ietf.org/html/rfc1123>) consisting of only lowercase alphanumeric characters, hyphens (-), and periods (.), and must start and end with an alphanumeric character, and be at most 253 characters in length.   
Show more

## 11.1.9. .status.pinnedImageSets

Description
     pinnedImageSets describes the current and desired pinned image sets for this node. 
Type
     `array`

## 11.1.10. .status.pinnedImageSets[]

Description
     MachineConfigNodeStatusPinnedImageSet holds information about the current, desired, and failed pinned image sets for the observed machine config node. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`currentGeneration` |  `integer` |  currentGeneration is the generation of the pinned image set that has most recently been successfully pulled and pinned on this node.   
`desiredGeneration` |  `integer` |  desiredGeneration is the generation of the pinned image set that is targeted to be pulled and pinned on this node.   
`lastFailedGeneration` |  `integer` |  lastFailedGeneration is the generation of the most recent pinned image set that failed to be pulled and pinned on this node.   
`lastFailedGenerationError` |  `string` |  lastFailedGenerationError is the error explaining why the desired images failed to be pulled and pinned. The error is an empty string if the image pull and pin is successful.   
`name` |  `string` |  name is the name of the pinned image set. Must be a lowercase RFC-1123 subdomain name (<https://tools.ietf.org/html/rfc1123>) consisting of only lowercase alphanumeric characters, hyphens (-), and periods (.), and must start and end with an alphanumeric character, and be at most 253 characters in length.   
Show more
