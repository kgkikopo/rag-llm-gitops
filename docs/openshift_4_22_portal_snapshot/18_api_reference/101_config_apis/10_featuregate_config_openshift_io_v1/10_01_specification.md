# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 10.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`customNoUpgrade` |  ``  |  customNoUpgrade allows the enabling or disabling of any feature. Turning this feature set on IS NOT SUPPORTED, CANNOT BE UNDONE, and PREVENTS UPGRADES. Because of its nature, this setting cannot be validated. If you have any typos or accidentally apply invalid combinations your cluster may fail in an unrecoverable way. featureSet must equal "CustomNoUpgrade" must be set to use this field.   
`featureSet` |  `string` |  featureSet changes the list of features in the cluster. The default is empty. Be very careful adjusting this setting. Turning on or off features may cause irreversible changes in your cluster which cannot be undone.   
Show more

## 10.1.2. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represent the observations of the current state. Known .status.conditions.type are: "DeterminationDegraded"   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`featureGates` |  `array` |  featureGates contains a list of enabled and disabled featureGates that are keyed by payloadVersion. Operators other than the CVO and cluster-config-operator, must read the .status.featureGates, locate the version they are managing, find the enabled/disabled featuregates and make the operand and operator match. The enabled/disabled values for a particular version may change during the life of the cluster as various .spec.featureSet values are selected. Operators may choose to restart their processes to pick up these changes, but remembering past enable/disable lists is beyond the scope of this API and is the responsibility of individual operators. Only featureGates with .version in the ClusterVersion.status will be present in this list.   
`featureGates[]` |  `object` |   
Show more

## 10.1.3. .status.conditions

Description
     conditions represent the observations of the current state. Known .status.conditions.type are: "DeterminationDegraded" 
Type
     `array`

## 10.1.4. .status.conditions[]

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

## 10.1.5. .status.featureGates

Description
     featureGates contains a list of enabled and disabled featureGates that are keyed by payloadVersion. Operators other than the CVO and cluster-config-operator, must read the .status.featureGates, locate the version they are managing, find the enabled/disabled featuregates and make the operand and operator match. The enabled/disabled values for a particular version may change during the life of the cluster as various .spec.featureSet values are selected. Operators may choose to restart their processes to pick up these changes, but remembering past enable/disable lists is beyond the scope of this API and is the responsibility of individual operators. Only featureGates with .version in the ClusterVersion.status will be present in this list. 
Type
     `array`

## 10.1.6. .status.featureGates[]

Description
    
Type
     `object`
Required
    

  * `version`



Property| Type| Description  
---|---|---  
`disabled` |  `array` |  disabled is a list of all feature gates that are disabled in the cluster for the named version.   
`disabled[]` |  `object` |   
`enabled` |  `array` |  enabled is a list of all feature gates that are enabled in the cluster for the named version.   
`enabled[]` |  `object` |   
`version` |  `string` |  version matches the version provided by the ClusterVersion and in the ClusterOperator.Status.Versions field.   
Show more

## 10.1.7. .status.featureGates[].disabled

Description
     disabled is a list of all feature gates that are disabled in the cluster for the named version. 
Type
     `array`

## 10.1.8. .status.featureGates[].disabled[]

Description
    
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the FeatureGate.   
Show more

## 10.1.9. .status.featureGates[].enabled

Description
     enabled is a list of all feature gates that are enabled in the cluster for the named version. 
Type
     `array`

## 10.1.10. .status.featureGates[].enabled[]

Description
    
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the FeatureGate.   
Show more
