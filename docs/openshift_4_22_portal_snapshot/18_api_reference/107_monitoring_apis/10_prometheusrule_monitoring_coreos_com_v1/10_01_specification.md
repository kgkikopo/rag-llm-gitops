# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec defines the specification of desired alerting rule definitions for Prometheus.   
`status` |  `object` |  status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.  Most recent observed status of the PrometheusRule. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>  
Show more

## 10.1.1. .spec

Description
     spec defines the specification of desired alerting rule definitions for Prometheus. 
Type
     `object`

Property| Type| Description  
---|---|---  
`groups` |  `array` |  groups defines the content of Prometheus rule file   
`groups[]` |  `object` |  RuleGroup is a list of sequentially evaluated recording and alerting rules.   
Show more

## 10.1.2. .spec.groups

Description
     groups defines the content of Prometheus rule file 
Type
     `array`

## 10.1.3. .spec.groups[]

Description
     RuleGroup is a list of sequentially evaluated recording and alerting rules. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`interval` |  `string` |  interval defines how often rules in the group are evaluated.   
`labels` |  `object (string)` |  labels define the labels to add or overwrite before storing the result for its rules. The labels defined at the rule level take precedence.  It requires Prometheus >= 3.0.0. The field is ignored for Thanos Ruler.   
`limit` |  `integer` |  limit defines the number of alerts an alerting rule and series a recording rule can produce. Limit is supported starting with Prometheus >= 2.31 and Thanos Ruler >= 0.24.   
`name` |  `string` |  name defines the name of the rule group.   
`partial_response_strategy` |  `string` |  partial_response_strategy is only used by ThanosRuler and will be ignored by Prometheus instances. More info: <https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md#partial-response>  
`query_offset` |  `string` |  query_offset defines the offset the rule evaluation timestamp of this particular group by the specified duration into the past.  It requires Prometheus >= v2.53.0. It is not supported for ThanosRuler.   
`rules` |  `array` |  rules defines the list of alerting and recording rules.   
`rules[]` |  `object` |  Rule describes an alerting or recording rule See Prometheus documentation: [alerting](<https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>) or [recording](<https://www.prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules>) rule   
Show more

## 10.1.4. .spec.groups[].rules

Description
     rules defines the list of alerting and recording rules. 
Type
     `array`

## 10.1.5. .spec.groups[].rules[]

Description
     Rule describes an alerting or recording rule See Prometheus documentation: [alerting](<https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>) or [recording](<https://www.prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules>) rule 
Type
     `object`
Required
    

  * `expr`



Property| Type| Description  
---|---|---  
`alert` |  `string` |  alert defines the name of the alert. Must be a valid label value. Only one of `record` and `alert` must be set.   
`annotations` |  `object (string)` |  annotations defines annotations to add to each alert. Only valid for alerting rules.   
`expr` |  `integer-or-string` |  expr defines the PromQL expression to evaluate.   
`for` |  `string` |  for defines how alerts are considered firing once they have been returned for this long.   
`keep_firing_for` |  `string` |  keep_firing_for defines how long an alert will continue firing after the condition that triggered it has cleared.   
`labels` |  `object (string)` |  labels defines labels to add or overwrite.   
`record` |  `string` |  record defines the name of the time series to output to. Must be a valid metric name. Only one of `record` and `alert` must be set.   
Show more

## 10.1.6. .status

Description
    

status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled. 

Most recent observed status of the PrometheusRule. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

Type
     `object`

Property| Type| Description  
---|---|---  
`bindings` |  `array` |  bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource.   
`bindings[]` |  `object` |  WorkloadBinding is a link between a configuration resource and a workload resource.   
Show more

## 10.1.7. .status.bindings

Description
     bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource. 
Type
     `array`

## 10.1.8. .status.bindings[]

Description
     WorkloadBinding is a link between a configuration resource and a workload resource. 
Type
     `object`
Required
    

  * `group`
  * `name`
  * `namespace`
  * `resource`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions defines the current state of the configuration resource when bound to the referenced Workload object.   
`conditions[]` |  `object` |  ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager or ThanosRuler.   
`group` |  `string` |  group defines the group of the referenced resource.   
`name` |  `string` |  name defines the name of the referenced object.   
`namespace` |  `string` |  namespace defines the namespace of the referenced object.   
`resource` |  `string` |  resource defines the type of resource being referenced (e.g. Prometheus, PrometheusAgent, ThanosRuler or Alertmanager).   
Show more

## 10.1.9. .status.bindings[].conditions

Description
     conditions defines the current state of the configuration resource when bound to the referenced Workload object. 
Type
     `array`

## 10.1.10. .status.bindings[].conditions[]

Description
     ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager or ThanosRuler. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime defines the time of the last update to the current status property.   
`message` |  `string` |  message defines the human-readable message indicating details for the condition’s last transition.   
`observedGeneration` |  `integer` |  observedGeneration defines the .metadata.generation that the condition was set based upon. For instance, if `.metadata.generation` is currently 12, but the `.status.conditions[].observedGeneration` is 9, the condition is out of date with respect to the current state of the object.   
`reason` |  `string` |  reason for the condition’s last transition.   
`status` |  `string` |  status of the condition.   
`type` |  `string` |  type of the condition being reported. Currently, only "Accepted" is supported.   
Show more
