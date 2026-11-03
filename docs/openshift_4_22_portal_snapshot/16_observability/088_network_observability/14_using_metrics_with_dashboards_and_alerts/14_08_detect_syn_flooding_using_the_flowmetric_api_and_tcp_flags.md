# 14.8. Detect SYN flooding using the FlowMetric API and TCP flags

Deploy a custom `AlertingRule` and `FlowMetric` configuration to monitor TCP flags, enabling real-time detection and alerting for SYN flooding attacks on the cluster. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. In the **Provided APIs** heading for the **NetObserv Operator** , select **FlowMetric**. 
  3. In the **Project** dropdown list, select the project of the Network Observability Operator instance. 
  4. Click **Create FlowMetric**. 
  5. Create `FlowMetric` resources to add the following configurations: 

**Configuration counting flows per destination host and resource, with TCP flags**

```yaml
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flows-with-flags-per-destination
spec:
  metricName: flows_with_flags_per_destination_total
  type: Counter
  labels: [SrcSubnetLabel,DstSubnetLabel,DstK8S_Name,DstK8S_Type,DstK8S_HostName,DstK8S_Namespace,Flags]
```


**Configuration counting flows per source host and resource, with TCP flags**

```yaml
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flows-with-flags-per-source
spec:
  metricName: flows_with_flags_per_source_total
  type: Counter
  labels: [DstSubnetLabel,SrcSubnetLabel,SrcK8S_Name,SrcK8S_Type,SrcK8S_HostName,SrcK8S_Namespace,Flags]
```


  6. Deploy the following `AlertingRule` resource to alert for SYN flooding: 

**`AlertingRule` for SYN flooding**

```yaml
apiVersion: monitoring.openshift.io/v1
kind: AlertingRule
metadata:
  name: netobserv-syn-alerts
  namespace: openshift-monitoring
# ...
  spec:
  groups:
  - name: NetObservSYNAlerts
    rules:
    - alert: NetObserv-SYNFlood-in
      annotations:
        message: |-
          {{ $labels.job }}: incoming SYN-flood attack suspected to Host={{ $labels.DstK8S_HostName}}, Namespace={{ $labels.DstK8S_Namespace }}, Resource={{ $labels.DstK8S_Name }}. This is characterized by a high volume of SYN-only flows with different source IPs and/or ports.
        summary: "Incoming SYN-flood"
      expr: sum(rate(netobserv_flows_with_flags_per_destination_total{Flags="2"}[1m])) by (job, DstK8S_HostName, DstK8S_Namespace, DstK8S_Name) > 300
      for: 15s
      labels:
        severity: warning
        app: netobserv
    - alert: NetObserv-SYNFlood-out
      annotations:
        message: |-
          {{ $labels.job }}: outgoing SYN-flood attack suspected from Host={{ $labels.SrcK8S_HostName}}, Namespace={{ $labels.SrcK8S_Namespace }}, Resource={{ $labels.SrcK8S_Name }}. This is characterized by a high volume of SYN-only flows with different source IPs and/or ports.
        summary: "Outgoing SYN-flood"
      expr: sum(rate(netobserv_flows_with_flags_per_source_total{Flags="2"}[1m])) by (job, SrcK8S_HostName, SrcK8S_Namespace, SrcK8S_Name) > 300
      for: 15s
      labels:
        severity: warning
        app: netobserv
# ...
```


In this example, the threshold for the alert is `300`; however, you can adapt this value empirically. A threshold that is too low might produce false-positives, and if it’s too high it might miss actual attacks. 




**Verification**

  1. In the web console, click **Manage Columns** in the **Network Traffic** table view and click **TCP flags**. 
  2. In the **Network Traffic** table view, filter on **TCP protocol SYN TCPFlag**. A large number of flows with the same **byteSize** indicates a SYN flood. 
  3. Go to **Observe** **Alerting** and select the **Alerting Rules** tab. 
  4. Filter on **netobserv-synflood-in alert**. The alert should fire when SYN flooding occurs. 



**Additional resources**

  * [Filtering eBPF flow data using a global rule](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-observe-network-traffic#network-observability-filtering-ebpf-rule_nw-observe-network-traffic "11.1.10. Filter eBPF flow data using multiple rules")
  * [Creating alerting rules for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/managing_alerts/managing-alerts-as-a-developer#creating-alerting-rules-for-user-defined-projects_managing-alerts-as-a-developer)
  * [Troubleshooting high cardinality metrics- Determining why Prometheus is consuming a lot of disk space](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#determining-why-prometheus-is-consuming-disk-space_investigating-monitoring-issues)
