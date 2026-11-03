# 12.2. Health rule threshold and grouping customization

Health rules in the Network Observability Operator are defined by using rule templates and variants in the `spec.processor.metrics.healthRules` field of the `FlowCollector` custom resource (CR). 

Customizing these templates allows for flexible, fine-grained alerting tailored to specific environment needs. 

For each template, a list of variants can be defined, each with distinct thresholds and grouping configurations. 

The following example shows a `FlowCollector` configuration with custom health rules: 

```yaml
apiVersion: flows.netobserv.io/v1beta1
kind: FlowCollector
metadata:
  name: flow-collector
spec:
  processor:
    metrics:
      healthRules:
      - template: PacketDropsByKernel
        mode: Alert # or Recording
        variants:
        # Triggered when aggregate cluster traffic reaches 10% drops
        - thresholds:
            critical: "10"
        # Triggered per-node with increasing severity levels
        - thresholds:
            critical: "15"
            warning: "10"
            info: "5"
          groupBy: Node
```


`spec.processor.metrics.healthRules.template`
     Specifies the name of the predefined rule template. 
`spec.processor.metrics.healthRules.mode`
     Specifies whether the rule functions as an `Alert` or a `Recording` rule. 
`spec.processor.metrics.healthRules.variants.thresholds`
     Specifies the numerical values that trigger the rule. Multiple severity levels, such as `critical`, `warning`, or `info`, can be defined within a single variant. 
`spec.processor.metrics.healthRules.variants.groupBy`
     Specifies the dimension used to aggregate the metric, such as `Node` or `Namespace`. 

Note

Customizing a rule replaces the default configuration for that template. To retain default configurations, the default settings must be manually included in the custom resource. 

## 12.2.1. Health rule query and metadata reference

The `FlowCollector` health rule API maps to the Prometheus Operator to generate `PrometheusRule` objects. Use these base Prometheus Query Language (PromQL) patterns and metadata configurations to create custom health rules for network observability. 

The `PrometheusRule` resource in the `netobserv` namespace can be viewed by running the following command: 

```shell-session
$ oc get prometheusrules -n netobserv -o yaml
```


### 12.2.1.1. Customize alert logic with PromQL: Incoming traffic surge

The following PromQL query calculates the byte rate from the `openshift-ingress` namespace to any workload namespace over a 30-minute interval: 

```plaintext
sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace)
```


Queries can be customized to filter low-bandwidth data, compare time periods, and establish thresholds. 

Data filtering
    

Appending `> 1000` to the query removes rates lower than `1 KB/s` to filter low-bandwidth traffic. 

`(sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace) > 1000)`

Note

The byte rate is relative to the sampling interval in the `FlowCollector` CR. Normalizing byte rates with the `netobserv_agent_sampling_rate` metric decouples the PromQL expression from the sampling configuration. 

Time comparison
    

The `offset` modifier compares data across different time periods. For example, `offset 1d` retrieves data from the previous day. 

`sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace)`

Threshold application
     A final threshold filters increases of less than a specific percentage. For example, `> 100` removes increases lower than 100%. 

The following example shows a complete PromQL expression for a `PrometheusRule`: 

```plaintext
expr: |-
  (100 *
    (
      (sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace) > 1000)
      - sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace)
    )
    / sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace))
  > 100
```


### 12.2.1.2. Alert metadata fields

Rule definitions require specific metadata for the Prometheus `Alertmanager` service and the **Network Health** dashboard. The following example shows an `AlertingRule` resource with configured metadata: 

```yaml
apiVersion: monitoring.openshift.io/v1
kind: AlertingRule
metadata:
  name: netobserv-alerts
  namespace: openshift-monitoring
spec:
  groups:
  - name: NetObservAlerts
    rules:
    - alert: NetObservIncomingBandwidth
      annotations:
        netobserv_io_network_health: '{"namespaceLabels":["DstK8S_Namespace"],"threshold":"100","unit":"%","upperBound":"500"}'
        message: |-
          Surge of incoming traffic detected: current traffic to {{ $labels.DstK8S_Namespace }} increased by more than 100% since yesterday.
        summary: "Surge in incoming traffic"
      expr: |-
        # ... (PromQL expression)
      for: 1m
      labels:
        app: netobserv
        netobserv: "true"
        severity: warning
```


`spec.groups.rules.alert.labels.netobserv`
     Specifies that the **Network Health** dashboard must detect the alert when set to `true`. 
`spec.groups.rules.alert.labels.severity`
     Specifies the alert severity. Valid values are `critical`, `warning`, or `info`. 

### 12.2.1.3. The netobserv_io_network_health annotation fields

The optional `netobserv_io_network_health` annotation is a JSON string that controls how the alert renders on the **Network Health** page. 

Table 12.1. Fields for the netobserv_io_network_health annotationField| Type| Description  
---|---|---  
`contextTab` |  String  |  The context tab in which the alert is displayed. Valid values include `netobserv`, `ovn`, `kiali`, or other third-party context identifiers. If not specified, the alert is displayed in the default NetObserv tab.   
`displayName` |  String  |  A custom display name for the alert shown in the **Network Health** UI. If not specified, the alert uses the default naming convention.   
`namespaceLabels` |  List of strings  |  One or more labels containing namespaces. Alerts are displayed under the **Namespaces** tab.   
`nodeLabels` |  List of strings  |  One or more labels containing node names. Alerts are displayed under the **Nodes** tab.   
`workloadLabels` |  List of strings  |  One or more labels containing owner or workload names. Alerts are displayed under the **Owners** tab when `kindLabels` is also provided.   
`kindLabels` |  List of strings  |  One or more labels containing owner or workload kinds. Must be provided alongside `workloadLabels` for the alert to be displayed under the **Owners** tab.   
`threshold` |  String  |  The alert threshold. This value should match the threshold in the PromQL expression.   
`unit` |  String  |  The data unit for display purposes.   
`upperBound` |  String  |  An upper bound value used to calculate scores on a closed scale. Metric values exceeding this bound are clamped.   
Show more

Note

If both `namespaceLabels` and `nodeLabels` are provided, `namespaceLabels` takes priority. If neither is provided, the alert is displayed under the **Global** tab. 

## 12.2.2. Configure custom health rules

Create custom health rules by using Prometheus Query Language (PromQL) to define an `AlertingRule` resource. These rules trigger alerts based on specific network metrics, such as traffic surges. 

**Prerequisites**

  * Access to the cluster with `cluster-admin` privileges. 
  * The Network Observability Operator is installed. 
  * OpenShift Container Platform 4.16 or later is installed. 
  * Familiarity with PromQL. 



Important

Custom `PrometheusRule` resources are not owned by the `FlowCollector` resource. Custom rules created in the `netobserv` namespace might be deleted if the Network Observability Operator is uninstalled. To prevent data loss, create custom rules in a different namespace, such as `openshift-monitoring`, and maintain a backup in version control. 

**Procedure**

  1. Define an `AlertingRule` resource in a YAML file, for example, `custom-alert.yaml`. 
  2. Apply the custom alert rule by running the following command: 

```shell-session
$ oc apply -f custom-alert.yaml
```


**Verification**

  1. Confirm the `PrometheusRule` resource was created in the target namespace by running the following command: 

```shell-session
$ oc get prometheusrules -n <namespace> -o yaml
```


  2. Confirm the rule is active in the OpenShift Container Platform web console: 

     1. Navigate to **Observe** **Alerting** to see the firing status. 
     2. Navigate to **Observe** **Network Health** to view the dashboard integration.
