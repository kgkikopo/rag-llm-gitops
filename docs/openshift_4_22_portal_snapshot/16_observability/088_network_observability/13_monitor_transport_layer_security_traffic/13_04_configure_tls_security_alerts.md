# 13.4. Configure TLS security alerts

The Network Observability Operator `TLSInsecureVersion` health rule alerts when network traffic uses deprecated or insecure TLS versions. 

When TLS tracking is enabled, this rule alerts when traffic uses deprecated TLS protocols (TLS 1.0, TLS 1.1, or SSL variants). 

**Prerequisites**

  * Network Observability Operator is installed and running. 
  * TLS tracking is enabled in the `FlowCollector` resource. 
  * You have `cluster-admin` privileges. 



**Procedure**

  1. Edit the `FlowCollector` custom resource by running the following command: 

```shell-session
$ oc edit flowcollector cluster
```


  2. Configure the `TLSInsecureVersion` health rule in the `spec.processor.metrics.healthRules` field: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    metrics:
      healthRules:
      - template: TLSInsecureVersion
        mode: Alert
        variants:
        - thresholds:
            warning: "5"
          groupBy: Namespace
# ...
```


where: 

`mode`
     Set to `Alert` to generate Prometheus alerts, or `Recording` to display violations in the **Network Health** dashboard without triggering alerts. 
`thresholds.warning`
     Threshold percentage. Alert fires when more than 5% of TLS traffic uses insecure versions (TLS 1.0, TLS 1.1, or SSL). 
`groupBy`
    

Group alerts by `Namespace`, `Node`, or `Workload`. Omit `groupBy` for cluster-wide aggregation. 

Note

Customizing a health rule replaces the default configuration. To retain default settings, manually include them in the custom resource. 

  3. Optional: To disable the `TLSInsecureVersion` alert entirely, add it to the `disableAlerts` list: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    metrics:
      disableAlerts:
      - TLSInsecureVersion
```


  4. Save and exit your editor. 



**Verification**

  1. Verify the Network Observability Operator created the alerting rule by running the following command: 

```shell-session
$ oc get prometheusrule -n netobserv
```


**Example output**

```shell-session
NAME                               AGE
netobserv-health-alerts            5m
```


  2. In the OpenShift Container Platform web console, go to **Observe** **Alerting**. 
  3. Select the **Alerting Rules** tab. 
  4. Filter on `TLSInsecureVersion` to view the generated alert variants (for example, `TLSInsecureVersion_PerNamespaceWarning`). 
  5. When network observability detects insecure TLS traffic exceeding the configured threshold, alerts are triggered and are displayed in the **Alerts** view. 
  6. Verify that TLS security violations are displayed in the **Network Health** dashboard: 

     1. Go to **Observe** **Network Traffic**. 
     2. Click the **Health** tab. 
     3. Select the **Namespaces** , **Nodes** , or **Workloads** tab based on your `groupBy` configuration. 
     4. TLS security violations appear in the health dashboard with links to investigate the affected traffic.
