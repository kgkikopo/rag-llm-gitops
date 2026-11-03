# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec describes the desired state of this AlertingRule object.   
`status` |  `object` |  status describes the current state of this AlertOverrides object.   
Show more

## 5.1.1. .spec

Description
     spec describes the desired state of this AlertingRule object. 
Type
     `object`
Required
    

  * `groups`



Property| Type| Description  
---|---|---  
`groups` |  `array` |  groups is a list of grouped alerting rules. Rule groups are the unit at which Prometheus parallelizes rule processing. All rules in a single group share a configured evaluation interval. All rules in the group will be processed together on this interval, sequentially, and all rules will be processed.  It’s common to group related alerting rules into a single AlertingRule resources, and within that resource, closely related alerts, or simply alerts with the same interval, into individual groups. You are also free to create AlertingRule resources with only a single rule group, but be aware that this can have a performance impact on Prometheus if the group is extremely large or has very complex query expressions to evaluate. Spreading very complex rules across multiple groups to allow them to be processed in parallel is also a common use-case.   
`groups[]` |  `object` |  RuleGroup is a list of sequentially evaluated alerting rules.   
Show more

## 5.1.2. .spec.groups

Description
    

groups is a list of grouped alerting rules. Rule groups are the unit at which Prometheus parallelizes rule processing. All rules in a single group share a configured evaluation interval. All rules in the group will be processed together on this interval, sequentially, and all rules will be processed. 

It’s common to group related alerting rules into a single AlertingRule resources, and within that resource, closely related alerts, or simply alerts with the same interval, into individual groups. You are also free to create AlertingRule resources with only a single rule group, but be aware that this can have a performance impact on Prometheus if the group is extremely large or has very complex query expressions to evaluate. Spreading very complex rules across multiple groups to allow them to be processed in parallel is also a common use-case. 

Type
     `array`

## 5.1.3. .spec.groups[]

Description
     RuleGroup is a list of sequentially evaluated alerting rules. 
Type
     `object`
Required
    

  * `name`
  * `rules`



Property| Type| Description  
---|---|---  
`interval` |  `string` |  interval is how often rules in the group are evaluated. If not specified, it defaults to the global.evaluation_interval configured in Prometheus, which itself defaults to 30 seconds. You can check if this value has been modified from the default on your cluster by inspecting the platform Prometheus configuration: The relevant field in that resource is: spec.evaluationInterval   
`name` |  `string` |  name is the name of the group.   
`rules` |  `array` |  rules is a list of sequentially evaluated alerting rules. Prometheus may process rule groups in parallel, but rules within a single group are always processed sequentially, and all rules are processed.   
`rules[]` |  `object` |  Rule describes an alerting rule. See Prometheus documentation: - <https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules>  
Show more

## 5.1.4. .spec.groups[].rules

Description
     rules is a list of sequentially evaluated alerting rules. Prometheus may process rule groups in parallel, but rules within a single group are always processed sequentially, and all rules are processed. 
Type
     `array`

## 5.1.5. .spec.groups[].rules[]

Description
     Rule describes an alerting rule. See Prometheus documentation: - <https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules>
Type
     `object`
Required
    

  * `alert`
  * `expr`



Property| Type| Description  
---|---|---  
`alert` |  `string` |  alert is the name of the alert. Must be a valid label value, i.e. may contain any Unicode character.   
`annotations` |  `object (string)` |  annotations to add to each alert. These are values that can be used to store longer additional information that you won’t query on, such as alert descriptions or runbook links.   
`expr` |  `integer-or-string` |  expr is the PromQL expression to evaluate. Every evaluation cycle this is evaluated at the current time, and all resultant time series become pending or firing alerts. This is most often a string representing a PromQL expression, e.g.: mapi_current_pending_csr > mapi_max_pending_csr In rare cases this could be a simple integer, e.g. a simple "1" if the intent is to create an alert that is always firing. This is sometimes used to create an always-firing "Watchdog" alert in order to ensure the alerting pipeline is functional.   
`for` |  `string` |  for is the time period after which alerts are considered firing after first returning results. Alerts which have not yet fired for long enough are considered pending.   
`labels` |  `object (string)` |  labels to add or overwrite for each alert. The results of the PromQL expression for the alert will result in an existing set of labels for the alert, after evaluating the expression, for any label specified here with the same name as a label in that set, the label here wins and overwrites the previous value. These should typically be short identifying values that may be useful to query against. A common example is the alert severity, where one sets `severity: warning` under the `labels` key:   
Show more

## 5.1.6. .status

Description
     status describes the current state of this AlertOverrides object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`observedGeneration` |  `integer` |  observedGeneration is the last generation change you’ve dealt with.   
`prometheusRule` |  `object` |  prometheusRule is the generated PrometheusRule for this AlertingRule. Each AlertingRule instance results in a generated PrometheusRule object in the same namespace, which is always the openshift-monitoring namespace.   
Show more

## 5.1.7. .status.prometheusRule

Description
     prometheusRule is the generated PrometheusRule for this AlertingRule. Each AlertingRule instance results in a generated PrometheusRule object in the same namespace, which is always the openshift-monitoring namespace. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the referenced PrometheusRule.   
Show more
