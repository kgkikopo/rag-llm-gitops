# 12.3. Performance optimization with recording rules

In large-scale clusters, recording rules optimize how Prometheus handles network data. Recording rules improve dashboard responsiveness and reduce the processing time for complex queries. 

## 12.3.1. Optimization benefits

Recording rules pre-compute complex Prometheus Query Language (PromQL) expressions and save the results as new time series. Unlike alerting rules, recording rules do not monitor thresholds. 

Using recording rules provides the following advantages: 

Improved performance
     Pre-computing Prometheus queries allows dashboards to load faster by avoiding on-demand calculations for long-term trends. 
Resource efficiency
     Calculating data at fixed intervals reduces CPU load on the Prometheus server compared to recalculating data on every dashboard refresh. 
Simplified queries
     Using short metric names, such as `cluster:network_traffic:rate_5m`, simplifies complex aggregate calculations in custom dashboards. 

## 12.3.2. Comparison of rule modes

The following table compares rule modes based on the expected outcome: 

Feature| Alerting rules| Recording rules  
---|---|---  
Primary goal  |  Issue notification.  |  Persistent metric history.   
Data output  |  Alerting state.  |  New time series metric.   
UI visibility  |  **Alerting** and **Network Health** views.  |  **Metrics Explorer** and **Network Health** views.   
Notifications  |  Triggers `Alertmanager` notifications.  |  Does not trigger notifications.   
Show more

## 12.3.3. Integrate recording rules with the health dashboard

Custom recording rules that contribute to the **Network Health** dashboard must meet specific metadata requirements. 

Label requirements
     Include the `netobserv: "true"` label in the `labels` field of the rule and the `PrometheusRule` metadata. The Network Observability Operator identifies `PrometheusRule` resources cluster-wide by using this label. 
Annotation requirements
    

Include the `netobserv.io/network-health` annotation in the `PrometheusRule` metadata. This annotation is required for recording rules to be displayed in the **Network Health** dashboard. The value is a JSON object where keys are the metric names (the `record` field of each rule). Each value consists of the following fields: 

  * `summary`: An optional short title. This field supports Prometheus template syntax, such as `{{ $labels.namespace }}`. 
  * `description`: An optional description. This field supports Prometheus template syntax. 
  * `netobserv_io_network_health`: A required JSON string that determines the health score and UI behavior. For recording rules, this JSON object supports the following fields: 

Table 12.2. Fields for the netobserv_io_network_health annotation in recording rulesField| Type| Description  
---|---|---  
`recordingThresholds` |  JSON object  |  Required. Defines the thresholds for health score calculation. Contains `info`, `warning`, and `critical` severity levels with numeric string values, such as `{"info":"10","warning":"25","critical":"50"}`.   
`contextTab` |  String  |  The context tab in which the recording rule is displayed. Valid values include `netobserv`, `ovn`, `kiali`, or other third-party context identifiers. If not specified, the recording rule is displayed in the default NetObserv tab.   
`displayName` |  String  |  A custom display name for the recording rule shown in the **Network Health** UI. If not specified, the recording rule uses the default naming convention.   
`namespaceLabels` |  List of strings  |  One or more labels containing namespaces. Recording rules are displayed under the **Namespaces** tab.   
`nodeLabels` |  List of strings  |  One or more labels containing node names. Recording rules are displayed under the **Nodes** tab.   
`workloadLabels` |  List of strings  |  One or more labels containing owner or workload names. Recording rules are displayed under the **Workloads** tab when `namespaceLabels` and `kindLabels` are also provided.   
`kindLabels` |  List of strings  |  One or more labels containing owner or workload kinds. Must be provided alongside `workloadLabels` and `namespaceLabels` for the recording rule to be displayed under the **Workloads** tab.   
`unit` |  String  |  The data unit for display purposes.   
`upperBound` |  String  |  An upper bound value used to calculate scores on a closed scale. Metric values exceeding this bound are clamped.   
Show more

Note

If both `namespaceLabels` and `nodeLabels` are provided, `namespaceLabels` takes priority. If neither is provided, the recording rule is displayed under the **Global** tab. 




## 12.3.4. Optimize dashboard metrics with recording rules

Create custom recording rules to pre-compute metrics for the **Network Health** dashboard. Recording rules require specific annotations and labels to integrate with the Network Observability Operator. 

**Prerequisites**

  * Access to the cluster with `cluster-admin` privileges. 
  * The Network Observability Operator is installed. 
  * OpenShift Container Platform 4.16 or later is installed. 
  * Familiarity with PromQL. 



Important

Custom `PrometheusRule` resources are not owned by the `FlowCollector` resource. Custom rules created in the `netobserv` namespace might be deleted if the Network Observability Operator is uninstalled. To prevent data loss, create custom rules in a different namespace, such as `openshift-monitoring`, and maintain a backup in version control. 

**Procedure**

  1. Define a `PrometheusRule` resource in a YAML file, such as `custom-recording-rule.yaml`, ensuring the `netobserv: "true"` label and `netobserv.io/network-health` annotation are included: 

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: my-recording-rules
  namespace: openshift-monitoring
  labels:
    netobserv: "true"
  annotations:
    netobserv.io/network-health: |
      {
        "my_metric_per_namespace": {
          "summary": "Custom metric is {{ $value }} in the namespace {{ $labels.namespace }}",
          "description": "Custom metric is {{ $value }} in the namespace {{ $labels.namespace }}",
          "netobserv_io_network_health": "{\"unit\":\"%\",\"upperBound\":\"100\",\"namespaceLabels\":[\"namespace\"],\"recordingThresholds\":{\"info\":\"10\",\"warning\":\"25\",\"critical\":\"50\"},\"contextTab\":\"netobserv\",\"displayName\":\"Custom Namespace Metric\"}"
        }
      }
spec:
  groups:
    - name: MyRecordingRules
      interval: 30s
      rules:
        - record: my_metric_per_namespace
          expr: (count by (namespace) (kube_pod_info) * 0 + 20)
          labels:
            netobserv: "true"
```


  2. Apply the custom recording rule by running the following command: 

```shell-session
$ oc apply -f custom-recording-rule.yaml
```


**Verification**

  1. Confirm the `PrometheusRule` resource exists by running the following command: 

```shell-session
$ oc get prometheusrules my-recording-rules -n openshift-monitoring -o yaml
```


  2. Confirm the recording rule is displayed in the OpenShift Container Platform web console by navigating to **Observe** **Network Health**.
