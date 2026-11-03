# 14.5. Configure custom metrics by using FlowMetric API

Configure the `FlowMetric` API to create custom Prometheus metrics by mapping flow log fields as labels to meet specific monitoring needs. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. In the **Provided APIs** heading for the **NetObserv Operator** , select **FlowMetric**. 
  3. In the **Project:** dropdown list, select the project of the Network Observability Operator instance. 
  4. Click **Create FlowMetric**. 
  5. Configure the `FlowMetric` resource. See "Custom metrics configuration examples". 



**Verification**

  1. Once the pods refresh, navigate to **Observe** **Metrics**. 
  2. In the **Expression** field, type the metric name to view the corresponding result. You can also enter an expression, such as `topk(5, sum(rate(netobserv_cluster_external_ingress_bytes_total{DstK8S_Namespace="my-namespace"}[2m])) by (DstK8S_HostName, DstK8S_OwnerName, DstK8S_OwnerType))`



## 14.5.1. Custom metrics configuration examples

To monitor specific network behaviors not covered by default metrics, such as external traffic volume or latency spikes, use the `FlowMetric` custom resource (CR). These examples provide the configuration needed to generate targeted Prometheus metrics from network flows. 

### 14.5.1.1. Tracking ingress bytes from cluster external sources

To measure the volume of data entering the cluster from external networks, use the following `FlowMetric` configuration. This metric helps identify potential bandwidth issues or unexpected external data transfer costs. 

```yaml
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flowmetric-cluster-external-ingress-traffic
  namespace: netobserv
spec:
  metricName: cluster_external_ingress_bytes_total
  type: Counter
  valueField: Bytes
  direction: Ingress
  labels: [DstK8S_HostName,DstK8S_Namespace,DstK8S_OwnerName,DstK8S_OwnerType]
  filters:
  - field: SrcSubnetLabel
    matchType: Absence
```


where: 

`metadata.namespace`
     Specifies the namespace where the `FlowMetric` resources are created. This must match the namespace defined in the `FlowCollector` resource `spec.namespace` field, which is `netobserv` by default. 
`spec.metricName`
     Specifies the name of the Prometheus metric, which in the OpenShift Container Platform web console appears with the prefix `netobserv-<metricName>`. 
`spec.type`
     Specifies the type of metric. The `Counter` type is useful for counting bytes or packets. 
`spec.direction`
     Specifies the direction of traffic to capture. If not specified, both ingress and egress are captured, which can lead to duplicated counts. 
`spec.labels`
     Specifies the labels that define what the metrics look like, the relationship between the different entities, and the metrics cardinality. For example, `SrcK8S_Name` is a high cardinality metric. 
`spec.filters`
     Specifies the criteria to refine results based on the listed criteria. In this example, selecting only the cluster external traffic is done by matching only flows where `SrcSubnetLabel` is absent. This assumes the subnet labels feature is enabled (via `spec.processor.subnetLabels`), which is done by default 

### 14.5.1.2. Monitoring RTT latency for cluster external ingress traffic

To analyze the performance of external connections and identify high-latency paths, use the following `FlowMetric` configuration. This metric converts nanoseconds to seconds to align with standard Prometheus latency dashboards. 

```yaml
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flowmetric-cluster-external-ingress-rtt
  namespace: netobserv
spec:
  metricName: cluster_external_ingress_rtt_seconds
  type: Histogram
  valueField: TimeFlowRttNs
  direction: Ingress
  labels: [DstK8S_HostName,DstK8S_Namespace,DstK8S_OwnerName,DstK8S_OwnerType]
  filters:
  - field: SrcSubnetLabel
    matchType: Absence
  - field: TimeFlowRttNs
    matchType: Presence
  divider: "1000000000"
  buckets: [".001", ".005", ".01", ".02", ".03", ".04", ".05", ".075", ".1", ".25", "1"]
```


where: 

`metadata.namespace`
     Specifies the namespace where the `FlowMetric` resources are created. This must match the namespace defined in the `FlowCollector` resource `spec.namespace` field, which is `netobserv` by default. 
`spec.type`
     Specifies the type of metric. The `Histogram` type is useful for a latency value, such as `TimeFlowRttNs`. 
`spec.divider`
     Specifies the value used to divide the metric. Because the Round-trip time (RTT) is provided as nanoseconds in flows, use a divider of 1,000,000,000 to convert the value into seconds, which is standard in Prometheus guidelines. 
`spec.buckets`
     Specifies custom buckets for RTT precision. The optimal precision ranges between 5ms and 250ms.
