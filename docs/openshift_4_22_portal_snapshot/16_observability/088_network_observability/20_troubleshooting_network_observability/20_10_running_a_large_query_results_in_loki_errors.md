# 20.10. Running a large query results in Loki errors

Understand how you can mitigate Loki timeout and request errors when running large queries by using indexed filters, leveraging Prometheus for long time ranges, creating custom metrics, or adjusting Loki and FlowCollector performance settings. 

When running large queries for a long time, Loki errors can occur, such as a `timeout` or `too many outstanding requests`. There is no complete corrective for this issue, but there are several ways to mitigate it: 

Adapt your query to add an indexed filter
     With Loki queries, you can query on both indexed and non-indexed fields or labels. Queries that contain filters on labels perform better. For example, if you query for a particular Pod, which is not an indexed field, you can add its Namespace to the query. The list of indexed fields can be found in the "Network flows format reference", in the `Loki label` column. 
Consider querying Prometheus rather than Loki
     Prometheus is a better fit than Loki to query on large time ranges. However, whether or not you can use Prometheus instead of Loki depends on the use case. For example, queries on Prometheus are much faster than on Loki, and large time ranges do not impact performance. But Prometheus metrics do not contain as much information as flow logs in Loki. The Network Observability OpenShift web console automatically favors Prometheus over Loki if the query is compatible; otherwise, it defaults to Loki. If your query does not run against Prometheus, you can change some filters or aggregations to make the switch. In the OpenShift web console, you can force the use of Prometheus. An error message is displayed when incompatible queries fail, which can help you figure out which labels to change to make the query compatible. For example, changing a filter or an aggregation from **Resource** or **Pods** to **Owner**. 
Consider using the FlowMetrics API to create your own metric
     If the data that you need isn’t available as a Prometheus metric, you can use the FlowMetrics API to create your own metric. For more information, see "FlowMetrics API Reference" and "Configuring custom metrics by using FlowMetric API". 
Configure Loki to improve the query performance
    

If the problem persists, you can consider configuring Loki to improve the query performance. Some options depend on the installation mode you used for Loki, such as using the Operator and `LokiStack`, or `Monolithic` mode, or `Microservices` mode. 

  * In `LokiStack` or `Microservices` modes, try increasing the number of querier replicas. For more information, see "LokiComponentSpec". 
  * Increase the query timeout. You must also increase the Network Observability read timeout to Loki in the `FlowCollector` `spec.loki.readTimeout`. For more information, see "QueryLimitSpec". 



## 20.10.1. Additional resources

  * [LokiComponentSpec](https://loki-operator.dev/docs/api.md/#loki-grafana-com-v1-LokiComponentSpec)
  * [QueryLimitSpec](https://loki-operator.dev/docs/api.md/#loki-grafana-com-v1-QueryLimitSpec)



**Additional resources**

  * [Network flows format reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-api-reference#network-flows-format_network_observability "19.1.4. Network flows format")
  * [FlowMetric API reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-api-reference#flowmetric-api_network_observability "19.1.2. FlowMetric API")
  * [Configuring custom metrics by using FlowMetric API](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/metrics-dashboards-alerts#network-observability-configuring-custom-metrics_metrics-dashboards-alerts "14.5. Configure custom metrics by using FlowMetric API")
