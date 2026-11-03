# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler.   
`status` |  `object` |  HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.   
Show more

## 4.1.1. .spec

Description
     HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler. 
Type
     `object`
Required
    

  * `scaleTargetRef`
  * `maxReplicas`



Property| Type| Description  
---|---|---  
`behavior` |  `object` |  HorizontalPodAutoscalerBehavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively).   
`maxReplicas` |  `integer` |  maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.   
`metrics` |  `array` |  metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used). The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa. See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization.   
`metrics[]` |  `object` |  MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).   
`minReplicas` |  `integer` |  minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured. Scaling is active as long as at least one metric value is available.   
`scaleTargetRef` |  `object` |  CrossVersionObjectReference contains enough information to let you identify the referred resource.   
Show more

## 4.1.2. .spec.behavior

Description
     HorizontalPodAutoscalerBehavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). 
Type
     `object`

Property| Type| Description  
---|---|---  
`scaleDown` |  `object` |  HPAScalingRules configures the scaling behavior for one direction via scaling Policy Rules and a configurable metric tolerance.  Scaling Policy Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen.  The tolerance is applied to the metric values and prevents scaling too eagerly for small metric variations. (Note that setting a tolerance requires the beta HPAConfigurableTolerance feature gate to be enabled.)   
`scaleUp` |  `object` |  HPAScalingRules configures the scaling behavior for one direction via scaling Policy Rules and a configurable metric tolerance.  Scaling Policy Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen.  The tolerance is applied to the metric values and prevents scaling too eagerly for small metric variations. (Note that setting a tolerance requires the beta HPAConfigurableTolerance feature gate to be enabled.)   
Show more

## 4.1.3. .spec.behavior.scaleDown

Description
    

HPAScalingRules configures the scaling behavior for one direction via scaling Policy Rules and a configurable metric tolerance. 

Scaling Policy Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen. 

The tolerance is applied to the metric values and prevents scaling too eagerly for small metric variations. (Note that setting a tolerance requires the beta HPAConfigurableTolerance feature gate to be enabled.) 

Type
     `object`

Property| Type| Description  
---|---|---  
`policies` |  `array` |  policies is a list of potential scaling polices which can be used during scaling. If not set, use the default values: - For scale up: allow doubling the number of pods, or an absolute change of 4 pods in a 15s window. - For scale down: allow all pods to be removed in a 15s window.   
`policies[]` |  `object` |  HPAScalingPolicy is a single policy which must hold true for a specified past interval.   
`selectPolicy` |  `string` |  selectPolicy is used to specify which policy should be used. If not set, the default value Max is used.   
`stabilizationWindowSeconds` |  `integer` |  stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).   
`tolerance` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  tolerance is the tolerance on the ratio between the current and desired metric value under which no updates are made to the desired number of replicas (e.g. 0.01 for 1%). Must be greater than or equal to zero. If not set, the default cluster-wide tolerance is applied (by default 10%).  For example, if autoscaling is configured with a memory consumption target of 100Mi, and scale-down and scale-up tolerances of 5% and 1% respectively, scaling will be triggered when the actual consumption falls below 95Mi or exceeds 101Mi.  This is an beta field and requires the HPAConfigurableTolerance feature gate to be enabled.   
Show more

## 4.1.4. .spec.behavior.scaleDown.policies

Description
     policies is a list of potential scaling polices which can be used during scaling. If not set, use the default values: - For scale up: allow doubling the number of pods, or an absolute change of 4 pods in a 15s window. - For scale down: allow all pods to be removed in a 15s window. 
Type
     `array`

## 4.1.5. .spec.behavior.scaleDown.policies[]

Description
     HPAScalingPolicy is a single policy which must hold true for a specified past interval. 
Type
     `object`
Required
    

  * `type`
  * `value`
  * `periodSeconds`



Property| Type| Description  
---|---|---  
`periodSeconds` |  `integer` |  periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).   
`type` |  `string` |  type is used to specify the scaling policy.   
`value` |  `integer` |  value contains the amount of change which is permitted by the policy. It must be greater than zero   
Show more

## 4.1.6. .spec.behavior.scaleUp

Description
    

HPAScalingRules configures the scaling behavior for one direction via scaling Policy Rules and a configurable metric tolerance. 

Scaling Policy Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen. 

The tolerance is applied to the metric values and prevents scaling too eagerly for small metric variations. (Note that setting a tolerance requires the beta HPAConfigurableTolerance feature gate to be enabled.) 

Type
     `object`

Property| Type| Description  
---|---|---  
`policies` |  `array` |  policies is a list of potential scaling polices which can be used during scaling. If not set, use the default values: - For scale up: allow doubling the number of pods, or an absolute change of 4 pods in a 15s window. - For scale down: allow all pods to be removed in a 15s window.   
`policies[]` |  `object` |  HPAScalingPolicy is a single policy which must hold true for a specified past interval.   
`selectPolicy` |  `string` |  selectPolicy is used to specify which policy should be used. If not set, the default value Max is used.   
`stabilizationWindowSeconds` |  `integer` |  stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).   
`tolerance` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  tolerance is the tolerance on the ratio between the current and desired metric value under which no updates are made to the desired number of replicas (e.g. 0.01 for 1%). Must be greater than or equal to zero. If not set, the default cluster-wide tolerance is applied (by default 10%).  For example, if autoscaling is configured with a memory consumption target of 100Mi, and scale-down and scale-up tolerances of 5% and 1% respectively, scaling will be triggered when the actual consumption falls below 95Mi or exceeds 101Mi.  This is an beta field and requires the HPAConfigurableTolerance feature gate to be enabled.   
Show more

## 4.1.7. .spec.behavior.scaleUp.policies

Description
     policies is a list of potential scaling polices which can be used during scaling. If not set, use the default values: - For scale up: allow doubling the number of pods, or an absolute change of 4 pods in a 15s window. - For scale down: allow all pods to be removed in a 15s window. 
Type
     `array`

## 4.1.8. .spec.behavior.scaleUp.policies[]

Description
     HPAScalingPolicy is a single policy which must hold true for a specified past interval. 
Type
     `object`
Required
    

  * `type`
  * `value`
  * `periodSeconds`



Property| Type| Description  
---|---|---  
`periodSeconds` |  `integer` |  periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).   
`type` |  `string` |  type is used to specify the scaling policy.   
`value` |  `integer` |  value contains the amount of change which is permitted by the policy. It must be greater than zero   
Show more

## 4.1.9. .spec.metrics

Description
     metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used). The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa. See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization. 
Type
     `array`

## 4.1.10. .spec.metrics[]

Description
     MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once). 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`containerResource` |  `object` |  ContainerResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory). The values will be averaged together before being compared to the target. Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. Only one "target" type should be set.   
`external` |  `object` |  ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).   
`object` |  `object` |  ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).   
`pods` |  `object` |  PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value.   
`resource` |  `object` |  ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory). The values will be averaged together before being compared to the target. Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. Only one "target" type should be set.   
`type` |  `string` |  type is the type of metric source. It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object.   
Show more

## 4.1.11. .spec.metrics[].containerResource

Description
     ContainerResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory). The values will be averaged together before being compared to the target. Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. Only one "target" type should be set. 
Type
     `object`
Required
    

  * `name`
  * `target`
  * `container`



Property| Type| Description  
---|---|---  
`container` |  `string` |  container is the name of the container in the pods of the scaling target   
`name` |  `string` |  name is the name of the resource in question.   
`target` |  `object` |  MetricTarget defines the target value, average value, or average utilization of a specific metric   
Show more

## 4.1.12. .spec.metrics[].containerResource.target

Description
     MetricTarget defines the target value, average value, or average utilization of a specific metric 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the target value of the average of the metric across all relevant pods (as a quantity)   
`type` |  `string` |  type represents whether the metric type is Utilization, Value, or AverageValue   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the target value of the metric (as a quantity).   
Show more

## 4.1.13. .spec.metrics[].external

Description
     ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). 
Type
     `object`
Required
    

  * `metric`
  * `target`



Property| Type| Description  
---|---|---  
`metric` |  `object` |  MetricIdentifier defines the name and optionally selector for a metric   
`target` |  `object` |  MetricTarget defines the target value, average value, or average utilization of a specific metric   
Show more

## 4.1.14. .spec.metrics[].external.metric

Description
     MetricIdentifier defines the name and optionally selector for a metric 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the given metric   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.   
Show more

## 4.1.15. .spec.metrics[].external.target

Description
     MetricTarget defines the target value, average value, or average utilization of a specific metric 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the target value of the average of the metric across all relevant pods (as a quantity)   
`type` |  `string` |  type represents whether the metric type is Utilization, Value, or AverageValue   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the target value of the metric (as a quantity).   
Show more

## 4.1.16. .spec.metrics[].object

Description
     ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object). 
Type
     `object`
Required
    

  * `describedObject`
  * `target`
  * `metric`



Property| Type| Description  
---|---|---  
`describedObject` |  `object` |  CrossVersionObjectReference contains enough information to let you identify the referred resource.   
`metric` |  `object` |  MetricIdentifier defines the name and optionally selector for a metric   
`target` |  `object` |  MetricTarget defines the target value, average value, or average utilization of a specific metric   
Show more

## 4.1.17. .spec.metrics[].object.describedObject

Description
     CrossVersionObjectReference contains enough information to let you identify the referred resource. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  apiVersion is the API version of the referent   
`kind` |  `string` |  kind is the kind of the referent; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  name is the name of the referent; More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 4.1.18. .spec.metrics[].object.metric

Description
     MetricIdentifier defines the name and optionally selector for a metric 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the given metric   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.   
Show more

## 4.1.19. .spec.metrics[].object.target

Description
     MetricTarget defines the target value, average value, or average utilization of a specific metric 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the target value of the average of the metric across all relevant pods (as a quantity)   
`type` |  `string` |  type represents whether the metric type is Utilization, Value, or AverageValue   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the target value of the metric (as a quantity).   
Show more

## 4.1.20. .spec.metrics[].pods

Description
     PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value. 
Type
     `object`
Required
    

  * `metric`
  * `target`



Property| Type| Description  
---|---|---  
`metric` |  `object` |  MetricIdentifier defines the name and optionally selector for a metric   
`target` |  `object` |  MetricTarget defines the target value, average value, or average utilization of a specific metric   
Show more

## 4.1.21. .spec.metrics[].pods.metric

Description
     MetricIdentifier defines the name and optionally selector for a metric 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the given metric   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.   
Show more

## 4.1.22. .spec.metrics[].pods.target

Description
     MetricTarget defines the target value, average value, or average utilization of a specific metric 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the target value of the average of the metric across all relevant pods (as a quantity)   
`type` |  `string` |  type represents whether the metric type is Utilization, Value, or AverageValue   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the target value of the metric (as a quantity).   
Show more

## 4.1.23. .spec.metrics[].resource

Description
     ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory). The values will be averaged together before being compared to the target. Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. Only one "target" type should be set. 
Type
     `object`
Required
    

  * `name`
  * `target`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the resource in question.   
`target` |  `object` |  MetricTarget defines the target value, average value, or average utilization of a specific metric   
Show more

## 4.1.24. .spec.metrics[].resource.target

Description
     MetricTarget defines the target value, average value, or average utilization of a specific metric 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the target value of the average of the metric across all relevant pods (as a quantity)   
`type` |  `string` |  type represents whether the metric type is Utilization, Value, or AverageValue   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the target value of the metric (as a quantity).   
Show more

## 4.1.25. .spec.scaleTargetRef

Description
     CrossVersionObjectReference contains enough information to let you identify the referred resource. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  apiVersion is the API version of the referent   
`kind` |  `string` |  kind is the kind of the referent; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  name is the name of the referent; More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 4.1.26. .status

Description
     HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler. 
Type
     `object`
Required
    

  * `desiredReplicas`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.   
`conditions[]` |  `object` |  HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point.   
`currentMetrics` |  `array` |  currentMetrics is the last read state of the metrics used by this autoscaler.   
`currentMetrics[]` |  `object` |  MetricStatus describes the last-read state of a single metric.   
`currentReplicas` |  `integer` |  currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.   
`desiredReplicas` |  `integer` |  desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.   
`lastScaleTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.   
`observedGeneration` |  `integer` |  observedGeneration is the most recent generation observed by this autoscaler.   
Show more

## 4.1.27. .status.conditions

Description
     conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met. 
Type
     `array`

## 4.1.28. .status.conditions[]

Description
     HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastTransitionTime is the last time the condition transitioned from one status to another   
`message` |  `string` |  message is a human-readable explanation containing details about the transition   
`reason` |  `string` |  reason is the reason for the condition’s last transition.   
`status` |  `string` |  status is the status of the condition (True, False, Unknown)   
`type` |  `string` |  type describes the current condition   
Show more

## 4.1.29. .status.currentMetrics

Description
     currentMetrics is the last read state of the metrics used by this autoscaler. 
Type
     `array`

## 4.1.30. .status.currentMetrics[]

Description
     MetricStatus describes the last-read state of a single metric. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`containerResource` |  `object` |  ContainerResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.   
`external` |  `object` |  ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes object.   
`object` |  `object` |  ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).   
`pods` |  `object` |  PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second).   
`resource` |  `object` |  ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.   
`type` |  `string` |  type is the type of metric source. It will be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each corresponds to a matching field in the object.   
Show more

## 4.1.31. .status.currentMetrics[].containerResource

Description
     ContainerResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. 
Type
     `object`
Required
    

  * `name`
  * `current`
  * `container`



Property| Type| Description  
---|---|---  
`container` |  `string` |  container is the name of the container in the pods of the scaling target   
`current` |  `object` |  MetricValueStatus holds the current value for a metric   
`name` |  `string` |  name is the name of the resource in question.   
Show more

## 4.1.32. .status.currentMetrics[].containerResource.current

Description
     MetricValueStatus holds the current value for a metric 
Type
     `object`

Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the current value of the average of the metric across all relevant pods (as a quantity)   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the current value of the metric (as a quantity).   
Show more

## 4.1.33. .status.currentMetrics[].external

Description
     ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes object. 
Type
     `object`
Required
    

  * `metric`
  * `current`



Property| Type| Description  
---|---|---  
`current` |  `object` |  MetricValueStatus holds the current value for a metric   
`metric` |  `object` |  MetricIdentifier defines the name and optionally selector for a metric   
Show more

## 4.1.34. .status.currentMetrics[].external.current

Description
     MetricValueStatus holds the current value for a metric 
Type
     `object`

Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the current value of the average of the metric across all relevant pods (as a quantity)   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the current value of the metric (as a quantity).   
Show more

## 4.1.35. .status.currentMetrics[].external.metric

Description
     MetricIdentifier defines the name and optionally selector for a metric 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the given metric   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.   
Show more

## 4.1.36. .status.currentMetrics[].object

Description
     ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object). 
Type
     `object`
Required
    

  * `metric`
  * `current`
  * `describedObject`



Property| Type| Description  
---|---|---  
`current` |  `object` |  MetricValueStatus holds the current value for a metric   
`describedObject` |  `object` |  CrossVersionObjectReference contains enough information to let you identify the referred resource.   
`metric` |  `object` |  MetricIdentifier defines the name and optionally selector for a metric   
Show more

## 4.1.37. .status.currentMetrics[].object.current

Description
     MetricValueStatus holds the current value for a metric 
Type
     `object`

Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the current value of the average of the metric across all relevant pods (as a quantity)   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the current value of the metric (as a quantity).   
Show more

## 4.1.38. .status.currentMetrics[].object.describedObject

Description
     CrossVersionObjectReference contains enough information to let you identify the referred resource. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  apiVersion is the API version of the referent   
`kind` |  `string` |  kind is the kind of the referent; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  name is the name of the referent; More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 4.1.39. .status.currentMetrics[].object.metric

Description
     MetricIdentifier defines the name and optionally selector for a metric 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the given metric   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.   
Show more

## 4.1.40. .status.currentMetrics[].pods

Description
     PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second). 
Type
     `object`
Required
    

  * `metric`
  * `current`



Property| Type| Description  
---|---|---  
`current` |  `object` |  MetricValueStatus holds the current value for a metric   
`metric` |  `object` |  MetricIdentifier defines the name and optionally selector for a metric   
Show more

## 4.1.41. .status.currentMetrics[].pods.current

Description
     MetricValueStatus holds the current value for a metric 
Type
     `object`

Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the current value of the average of the metric across all relevant pods (as a quantity)   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the current value of the metric (as a quantity).   
Show more

## 4.1.42. .status.currentMetrics[].pods.metric

Description
     MetricIdentifier defines the name and optionally selector for a metric 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the given metric   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.   
Show more

## 4.1.43. .status.currentMetrics[].resource

Description
     ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. 
Type
     `object`
Required
    

  * `name`
  * `current`



Property| Type| Description  
---|---|---  
`current` |  `object` |  MetricValueStatus holds the current value for a metric   
`name` |  `string` |  name is the name of the resource in question.   
Show more

## 4.1.44. .status.currentMetrics[].resource.current

Description
     MetricValueStatus holds the current value for a metric 
Type
     `object`

Property| Type| Description  
---|---|---  
`averageUtilization` |  `integer` |  currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.   
`averageValue` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  averageValue is the current value of the average of the metric across all relevant pods (as a quantity)   
`value` |  [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  value is the current value of the metric (as a quantity).   
Show more
