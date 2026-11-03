# 12.1. Identify network issues with automated health rules

Network observability identifies network issues by using automated health rules to monitor metrics. These rules trigger alerts when anomalies occur, which assists in maintaining connectivity and responding to network degradation. 

The Network Observability Operator manages a system of Prometheus-based rules that detect network problems, and converts these rules into `PrometheusRule` resources. It supports the following rule types: 

Alerting rules
     Trigger notifications through the Prometheus `Alertmanager` when network anomalies or infrastructure failures are detected. 
Recording rules
     Pre-compute complex Prometheus Query Language (PromQL) expressions into new time series to improve dashboard performance. 

## 12.1.1. Importance of network health monitoring

Maintaining reliable and secure network connectivity is critical for cluster administrators and security teams. Unresolved network issues can result in the following consequences: 

  * Application downtime caused by packet drops or DNS failures. 
  * Security risks from undetected network policy violations. 
  * Performance degradation caused by latency spikes or bandwidth saturation. 
  * Compliance issues from unmonitored network traffic. 



Early detection of these issues allows for resolution before service level objectives (SLOs) are affected. 

## 12.1.2. Automated health monitoring

The Network Observability Operator provides automated health monitoring through the following features: 

  * Pre-configured health rules: Detect common network problems by using default thresholds. 
  * Automated alerting: Integrates with the OpenShift Container Platform monitoring stack. 
  * Health dashboards: Displays health status for clusters, nodes, namespaces, and workloads. 
  * Custom rules: Supports the creation of organization-specific monitoring rules. 



Health rules monitor network flow metrics and trigger alerts when defined thresholds are exceeded. For example, the `PacketDropsByKernel` rule reports an alert when kernel packet drop rates exceed defined levels. 

## 12.1.3. Network health monitoring workflow

Monitoring network health involves the following phases: 

  * Configuring the Network Observability Operator to collect required network health data for monitoring, such as packet drops or DNS tracking. 
  * Reviewing and customizing default health rules and thresholds in the `FlowCollector` custom resource. 
  * Monitoring alerts in the OpenShift Container Platform web console in the **Observe** **Alerting** and **Observe** **Network Health** views. 
  * Creating custom health rules for specific requirements. 
  * Configuring recording rules to optimize performance for large-scale deployments. 



The `PrometheusRule` resource in the `netobserv` namespace can be viewed by running the following command: 

```shell-session
$ oc get prometheusrules -n netobserv -o yaml
```


## 12.1.4. Detect network issues with automated health rules

The Network Observability Operator includes a rule-based system to detect network anomalies and infrastructure failures. By converting configurations into alerting rules, the Operator provides automated monitoring and troubleshooting through the OpenShift Container Platform web console. 

### 12.1.4.1. Monitoring outcomes

The Network Observability Operator displays network status in the following views: 

**Alerting** UI
     Specific alerts are displayed in **Observe** **Alerting**. Notifications are managed through the Prometheus `Alertmanager`. 
**Network Health** dashboard
     A specialized dashboard in **Observe** **Network Health** provides a summary of cluster network status. 

The **Network Health** dashboard categorizes violations into tabs to isolate the scope of an issue: 

  * **Global** : Aggregate health of the cluster. 
  * **Nodes** : Violations specific to infrastructure nodes. 
  * **Namespaces** : Violations specific to individual namespaces. 
  * **Workloads** : Violations specific to resources, such as `Deployments` or `DaemonSets`. 



### 12.1.4.2. Network health context tabs

The **Network Health** dashboard organizes alerts and recording rules into separate context tabs. You can view network health from different perspectives, such as Network Observability metrics, OVN-Kubernetes platform alerts, or third-party service mesh monitoring. 

Context tabs include: 

**NetObserv**
     Default context for Network Observability Operator health rules. Rules in this context contribute to the 0-10 health score calculation. 
**External contexts**
     Read-only contexts for external monitoring sources, such as OpenShift OVN-Kubernetes platform alerts or Kiali service mesh health alerts. These contexts are displayed when external alerts are labeled for Network Health integration. External alerts provide additional visibility but do not affect the network observability health score. 

Rules are routed to a context tab based on the following priority order: 

  1. Annotation `netobserv_io_network_health` JSON field `contextTab` on the alert or recording rule. 
  2. Default: `netobserv` context for all rules with the `netobserv: "true"` label. 



### 12.1.4.3. Predefined health rules

The Network Observability Operator provides default rules for common networking scenarios. These rules are active only if the corresponding feature is enabled in the `FlowCollector` custom resource (CR). 

The following list contains a subset of available default rules: 

`PacketDropsByDevice`
     Reports a high percentage of packet drops from network devices. This rule is based on node-exporter metrics and does not require the `PacketDrop` agent feature. 
`PacketDropsByKernel`
     Reports a high percentage of packet drops by the kernel. This rule requires the `PacketDrop` agent feature. 
`IPsecErrors`
     Reports IPsec encryption errors. This rule requires the `IPSec` agent feature. 
`NetpolDenied`
     Reports traffic denied by network policies. This rule requires the `NetworkEvents` agent feature. 
`LatencyHighTrend`
     Reports a significant increase in TCP latency. This rule requires the `FlowRTT` agent feature. 
`DNSErrors`
     Reports DNS errors. This rule requires the `DNSTracking` agent feature. 
`TLSInsecureVersion`
     Reports a high percentage of TLS traffic using insecure protocol versions (TLS 1.0, TLS 1.1, or SSL variants). This rule requires the `TLSTracking` agent feature. 

The following operational alerts apply to the Network Observability Operator: 

`NetObservNoFlows`
     Reports when the pipeline is active but no flows are observed. 
`NetObservLokiError`
     Reports when flows are dropped because of Loki errors. 

For a complete list of rules and runbooks, see the [Network Observability Operator runbooks](https://github.com/openshift/runbooks/tree/master/alerts/network-observability-operator). 

### 12.1.4.4. Enable features for health monitoring

The Network Observability Operator creates rules based on the features enabled in the `FlowCollector` CR. 

For example, packet drop rules are created only if the `PacketDrop` agent feature is enabled. Rules depend on metrics; if the required metrics are unavailable, configuration warnings might appear. Configure metrics in the `spec.processor.metrics.includeList` field of the `FlowCollector` resource.
