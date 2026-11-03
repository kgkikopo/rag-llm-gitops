# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec describes the desired state of this AlertRelabelConfig object.   
`status` |  `object` |  status describes the current state of this AlertRelabelConfig object.   
Show more

## 4.1.1. .spec

Description
     spec describes the desired state of this AlertRelabelConfig object. 
Type
     `object`
Required
    

  * `configs`



Property| Type| Description  
---|---|---  
`configs` |  `array` |  configs is a list of sequentially evaluated alert relabel configs.   
`configs[]` |  `object` |  RelabelConfig allows dynamic rewriting of label sets for alerts. See Prometheus documentation: - <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs> \- <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>  
Show more

## 4.1.2. .spec.configs

Description
     configs is a list of sequentially evaluated alert relabel configs. 
Type
     `array`

## 4.1.3. .spec.configs[]

Description
     RelabelConfig allows dynamic rewriting of label sets for alerts. See Prometheus documentation: - <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs> \- <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>
Type
     `object`

Property| Type| Description  
---|---|---  
`action` |  `string` |  action to perform based on regex matching. Must be one of: 'Replace', 'Keep', 'Drop', 'HashMod', 'LabelMap', 'LabelDrop', or 'LabelKeep'. Default is: 'Replace'   
`modulus` |  `integer` |  modulus to take of the hash of the source label values. This can be combined with the 'HashMod' action to set 'target_label' to the 'modulus' of a hash of the concatenated 'source_labels'. This is only valid if sourceLabels is not empty and action is not 'LabelKeep' or 'LabelDrop'.   
`regex` |  `string` |  regex against which the extracted value is matched. Default is: '(.*)' regex is required for all actions except 'HashMod'   
`replacement` |  `string` |  replacement value against which a regex replace is performed if the regular expression matches. This is required if the action is 'Replace' or 'LabelMap' and forbidden for actions 'LabelKeep' and 'LabelDrop'. Regex capture groups are available. Default is: '$1'   
`separator` |  `string` |  separator placed between concatenated source label values. When omitted, Prometheus will use its default value of ';'.   
`sourceLabels` |  `array (string)` |  sourceLabels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the 'Replace', 'Keep', and 'Drop' actions. Not allowed for actions 'LabelKeep' and 'LabelDrop'.   
`targetLabel` |  `string` |  targetLabel to which the resulting value is written in a 'Replace' action. It is required for 'Replace' and 'HashMod' actions and forbidden for actions 'LabelKeep' and 'LabelDrop'. Regex capture groups are available.   
Show more

## 4.1.4. .status

Description
     status describes the current state of this AlertRelabelConfig object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions contains details on the state of the AlertRelabelConfig, may be empty.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
Show more

## 4.1.5. .status.conditions

Description
     conditions contains details on the state of the AlertRelabelConfig, may be empty. 
Type
     `array`

## 4.1.6. .status.conditions[]

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
