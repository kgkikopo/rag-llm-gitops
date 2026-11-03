# 14.3. Create alerts

Create custom `AlertingRule` resources based on `Netobserv` dashboard metrics to define conditions that trigger alerts in the OpenShift Container Platform console. 

**Prerequisites**

  * You have access to the cluster as a user with the cluster-admin role or with view permissions for all projects. 
  * You have the Network Observability Operator installed. 



**Procedure**

  1. Create a YAML file by clicking the import icon, **+**. 
  2. Add an alerting rule configuration to the YAML file. In the YAML sample that follows, an alert is created for when the cluster ingress traffic reaches a given threshold of 10 MBps per destination workload. 

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
        message: |-
          {{ $labels.job }}: incoming traffic exceeding 10 MBps for 30s on {{ $labels.DstK8S_OwnerType }} {{ $labels.DstK8S_OwnerName }} ({{ $labels.DstK8S_Namespace }}).
        summary: "High incoming traffic."
      expr: sum(rate(netobserv_workload_ingress_bytes_total     {SrcK8S_Namespace="openshift-ingress"}[1m])) by (job, DstK8S_Namespace, DstK8S_OwnerName, DstK8S_OwnerType) > 10000000
      for: 30s
      labels:
        severity: warning
```


     * The `netobserv_workload_ingress_bytes_total` metric is enabled by default in `spec.processor.metrics.includeList`. 

  3. Click **Create** to apply the configuration file to the cluster.
