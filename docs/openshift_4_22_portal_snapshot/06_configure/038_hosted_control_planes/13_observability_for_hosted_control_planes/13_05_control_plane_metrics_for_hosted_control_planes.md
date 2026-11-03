# 13.5. Control plane metrics for hosted control planes

You can observe hosted control plane health from the hosted cluster monitoring stack when metrics forwarding is enabled. 

With propagated metrics, you can diagnose API server, etcd, Operator, and scheduling issues from the hosted cluster web console and CLI without management cluster credentials. Selected control plane metrics are propagated from the management cluster into the hosted cluster platform Prometheus. 

After you enable forwarding on the `HostedCluster` resource, you can use familiar PromQL queries, alerts, and dashboards. 

Important

For OpenShift Container Platform 4.22.7 and earlier, the `hypershift.openshift.io/enable-metrics-forwarding` annotation was the mechanism for enabling metrics forwarding. As of OpenShift Container Platform 4.22.8, this annotation is deprecated. When the `spec.monitoring.metricsForwarding` field is set on a `HostedCluster` object, the spec field takes precedence over the annotation. The annotation continues to be honored for clusters that have not yet set the `spec.monitoring` field. 

For information about migrating from the annotation to the new API, see "Migrating from annotation-based to API-based metrics forwarding". 

## 13.5.1. Metrics forwarding architecture

When you enable metrics forwarding, hosted control planes deploys components on both the management cluster and the hosted cluster. 

On the management cluster, in the hosted control plane namespace, the following steps take place: 

  * The `endpoint-resolver` deployment discovers pod IP addresses for control plane components. 
  * The `metrics-proxy` deployment scrapes control plane pods, applies per-component metric filters, injects OpenShift Container Platform-compatible labels, and serves aggregated metrics at paths, such as `/metrics/kube-apiserver` and `/metrics/etcd`, behind a TLS-passthrough Route. 



On the hosted cluster, in the `openshift-monitoring` namespace, the following steps take place: 

  * The `control-plane-metrics-forwarder` deployment runs HAProxy and TCP-proxies scrape requests to the management cluster `metrics-proxy` Route. 
  * A `PodMonitor` named `control-plane-metrics-forwarder` configures platform Prometheus to scrape the forwarder using mutual TLS (mTLS). 



The data path is as follows: 

  1. Platform Prometheus in the hosted cluster discovers the `PodMonitor` and scrapes the metrics-forwarder. 
  2. The metrics-forwarder forwards the scrape over mTLS to the management cluster `metrics-proxy` Route. 
  3. The metrics-proxy scrapes control plane pods through the endpoint-resolver and returns filtered, relabeled metrics. 



## 13.5.2. Enable metrics forwarding

You can enable control plane metrics forwarding independently for each hosted cluster by setting the `spec.monitoring.metricsForwarding` field on the `HostedCluster` object. 

As a result, you can select different metrics sets for different hosted clusters on the same management cluster without changing the global HyperShift Operator configuration. 

**Prerequisites**

  * You are running OpenShift Container Platform 4.22.8 or later. 
  * You have a hosted cluster already provisioned. 
  * You have cluster administrator access to the management cluster or a `kubeconfig` file with access to the namespace that contains the `HostedCluster` resource. The `HostedCluster` object exists on the management cluster. 
  * A remote write endpoint and certificates are already configured at the management cluster level for metrics ingestion. 



**Procedure**

  1. Enable metrics forwarding on the hosted cluster by entering the following command: 

```shell-session
$ oc patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type merge \
  -p '{"spec":{"monitoring":{"metricsForwarding":{"mode":"Forward"}}}}'
```


Replace `<hosted_cluster_namespace>` with the namespace of the hosted cluster and `<hosted_cluster_name>` with the name of the hosted cluster. 

  2. Optional: Specify the metrics set for this hosted cluster. 

If you omit this step, the cluster inherits the global `METRICS_SET` environment variable from the HyperShift Operator deployment, which defaults to `Telemetry`. 

Set `spec.monitoring.metricsSet` to a cluster-level default by entering the following command: 

```shell-session
$ oc patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type merge \
  -p '{"spec":{"monitoring":{"metricsSet":"<metrics_set>"}}}'
```


Replace `<metrics_set>` with one of the following values: 

`Telemetry`
     The default. Forwards only the minimal set of metrics required for OpenShift Telemetry. 
`SRE`
     Forwards the Telemetry set plus additional metrics defined in the `sre-metric-set` `ConfigMap`. Required for SRE dashboards and alerts. 
`All`
     Forwards all metrics without filtering. Use for debugging. Produces significantly higher metrics volume. 

  3. Optional: Set a forwarding-path override for the metrics set. 

Use `spec.monitoring.metricsForwarding.metricsSet` when you need the forwarding path to use a different metrics set than the cluster default. This field takes precedence over `spec.monitoring.metricsSet` and the global `METRICS_SET` variable. 

```shell-session
$ oc patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type merge \
  -p '{"spec":{"monitoring":{"metricsForwarding":{"mode":"Forward","metricsSet":"<metrics_set>"}}}}'
```


Note

The patch includes `"mode":"Forward"` alongside `metricsSet` because `metricsForwarding` is a nested object in a JSON merge patch. If you set `spec.monitoring.metricsForwarding` for the first time without having already set `mode`, omitting `mode` from the patch leaves it as an empty string, which disables forwarding. 




**Verification**

  1. Confirm the `metrics-proxy` deployment is running in the hosted control plane namespace on the management cluster by entering the following command: 

```shell-session
$ oc get deployment metrics-proxy -n <hcp_namespace>
```


Replace `<hcp_namespace>` with the hosted control plane namespace, which follows the format `<hosted_cluster_namespace>-<hosted_cluster_name>`, with any dots in the cluster name replaced by dashes. For example, if the `HostedCluster` is in the `clusters` namespace and named `my-cluster`, the hosted control plane namespace is `clusters-my-cluster`. 

The output shows `2/2` ready replicas. 

  2. Confirm the `control-plane-metrics-forwarder` deployment is running in the `openshift-monitoring` namespace on the hosted cluster by entering the following command: 

```shell-session
$ oc get deployment -n openshift-monitoring control-plane-metrics-forwarder \
  --kubeconfig <hosted_cluster_kubeconfig>
```


The output shows `1/1` ready replicas. 

  3. Verify that platform Prometheus in the hosted cluster is scraping control plane metrics by querying a forwarded metric, such as `apiserver_request_total`, from the hosted cluster Prometheus endpoint. 

Note

If the deprecated `hypershift.openshift.io/enable-metrics-forwarding` annotation is also set on the `HostedCluster` object, the `spec.monitoring.metricsForwarding` field takes precedence. 




## 13.5.3. Migrate from annotation-based to API-based metrics forwarding

To preserve metrics forwarding continuity, you can migrate hosted clusters from the deprecated `hypershift.openshift.io/enable-metrics-forwarding` annotation to the `spec.monitoring.metricsForwarding` field on the `HostedCluster` API. 

The spec field takes precedence as soon as it is set, and the annotation remains in place until you remove it. 

**Prerequisites**

  * One or more hosted clusters use the `hypershift.openshift.io/enable-metrics-forwarding: "true"` annotation. 
  * You have cluster administrator access to the management cluster. 
  * You are running OpenShift Container Platform 4.22.8 or later. 



**Procedure**

  1. Identify which hosted clusters have the annotation set by entering the following command: 

```shell-session
$ oc get hostedclusters -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.metadata.annotations.hypershift\.openshift\.io/enable-metrics-forwarding}{"\n"}{end}'
```


The output lists namespace, name, and annotation value for each hosted cluster. Clusters that show `true` in the third column require migration. 

  2. Determine the metrics set value to use for each cluster. 

The annotation enables forwarding but does not specify a metrics set. The HyperShift Operator uses the global `METRICS_SET` environment variable as the source. 

Check the global `METRICS_SET` value by entering the following command: 

```shell-session
$ oc get deployment -n hypershift operator \
  -o jsonpath='{.spec.template.spec.containers[?(@.name=="operator")].env[?(@.name=="METRICS_SET")].value}'
```


In the command, `hypershift` is the namespace where the HyperShift Operator is typically installed, and `operator` is the standard deployment name. These values might differ in non-standard installations. 

Note the returned value. This value is the metrics set that the annotated clusters currently use. Map the value to the `MetricsSet` enum: `Telemetry`, `SRE`, or `All`. 

  3. For each cluster that requires migration, set `spec.monitoring.metricsForwarding` by entering the following command: 

```shell-session
$ oc patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type merge \
  -p '{"spec":{"monitoring":{"metricsForwarding":{"mode":"Forward","metricsSet":"<metrics_set>"}}}}'
```


Replace `<hosted_cluster_namespace>` with the namespace of the hosted cluster, `<hosted_cluster_name>` with the name of the hosted cluster, and `<metrics_set>` with the value you identified in the previous step. 

As soon as the spec field is set, it takes precedence over the annotation. Metrics forwarding continues without interruption. 

  4. Verify that metrics forwarding remains active after the patch. 

     1. Confirm the `metrics-proxy` deployment in the hosted control plane namespace is healthy by entering the following command: 

```shell-session
$ oc get deployment metrics-proxy -n <hcp_namespace>
```


Replace `<hcp_namespace>` with the hosted control plane namespace, which follows the format `<hosted_cluster_namespace>-<hosted_cluster_name>`, with any dots in the cluster name replaced by dashes. 

The `READY` column shows `2/2`. 

     2. Confirm the `control-plane-metrics-forwarder` deployment in the hosted cluster is healthy by entering the following command: 

```shell-session
$ oc get deployment -n openshift-monitoring control-plane-metrics-forwarder \
  --kubeconfig <hosted_cluster_kubeconfig>
```


The `READY` column shows `1/1`. 

  5. Optional: After confirming that forwarding is active through the spec field, remove the now-redundant annotation by entering the following command: 

```shell-session
$ oc annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  hypershift.openshift.io/enable-metrics-forwarding-
```


This step is safe because the spec field is now authoritative. Removing the annotation has no effect on metrics forwarding behavior. 




**Verification**

  * After you migrate all clusters, verify that no remaining clusters use the deprecated annotation by re-running the identification command in step 1 and confirming that the output is empty. 



## 13.5.4. Query control plane metrics in hosted clusters by using the CLI

After you enable metrics forwarding, you can verify that control plane metrics are ingested and query them from the CLI. 

Use the same PromQL patterns as standalone OpenShift Container Platform clusters because the metrics-proxy injects compatible labels. 

**Prerequisites**

  * Metrics forwarding is enabled on the `HostedCluster` resource. For enablement steps, see "Enabling metrics forwarding". 
  * You have `cluster-admin` access to the hosted cluster. 
  * At least two minutes have elapsed since you enabled forwarding so Prometheus can complete initial scrapes. 



**Procedure**

  1. Verify that the `control-plane-metrics-forwarder` deployment exists in the `openshift-monitoring` namespace: 

```shell-session
$ oc get deployment control-plane-metrics-forwarder -n openshift-monitoring
```


Note

Control plane metrics are available when the Cluster Monitoring Operator and platform Prometheus are running, even if no compute nodes are scheduled. Data-plane node and workload metrics still require compute nodes. 

  2. Verify that the `control-plane-metrics-forwarder` `PodMonitor` exists: 

```shell-session
$ oc get podmonitor control-plane-metrics-forwarder -n openshift-monitoring
```


  3. Optional: Verify that management-cluster components are running by logging in to the management cluster: 

     1. Enter the following command: 

```shell-session
$ oc get deployment endpoint-resolver metrics-proxy -n <hcp_namespace>
```


Replace `<hcp_namespace>` with the namespace for your hosted cluster. Typically, the format of the namespace is `<hosted_cluster_namespace>-<hosted_cluster_name>`. 

     2. Enter the following command: 

```shell-session
$ oc get route metrics-proxy -n <hcp_namespace>
```


  4. Verify that Prometheus scraped targets for the forwarder report: 

```shell-session
$ oc exec -n openshift-monitoring prometheus-k8s-0 -c prometheus -- \
  curl -s http://localhost:9090/api/v1/targets \
  | jq '.data.activeTargets[] | select(.scrapePool | contains("control-plane-metrics-forwarder")) | {scrapePool, scrapeUrl: .scrapeUrl, health}'
```


You should see one target per forwarded component with the status of `"health": "up"`. 

  5. Confirm that Kubernetes API server metrics are ingested by querying `apiserver_request_total`: 

```shell-session
$ oc exec -n openshift-monitoring prometheus-k8s-0 -c prometheus -- \
  curl -gs 'http://localhost:9090/api/v1/query?query=apiserver_request_total{job="apiserver"}' \
  | jq '.data.result | length'
```


A nonzero result confirms that API server metrics are available in the guest cluster monitoring stack. 




**Additional resources**

  * [Exposed metrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-metrics_olm-understanding-metrics)



## 13.5.5. Query control plane metrics in hosted clusters by using the web console

After you enable metrics forwarding, you can verify that control plane metrics are ingested and query them from the web console. 

Use the same PromQL patterns as standalone OpenShift Container Platform clusters because the metrics-proxy injects compatible labels. 

**Prerequisites**

  * Metrics forwarding is enabled on the `HostedCluster` resource. For enablement steps, see "Enabling metrics forwarding". 
  * You have `cluster-admin` access to the hosted cluster. 
  * At least two minutes have elapsed since you enabled forwarding so Prometheus can complete initial scrapes. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console for the hosted cluster. 
  2. Click **Observe** **Metrics**. 
  3. In the query field, enter a PromQL expression and run the query. 

Use the following examples: 

**Operator health**

```plaintext
csv_succeeded{job="olm-operator-metrics"} == 0
```


This query lists CSVs that are not in the `Succeeded` state. 

**API server request rate**

```plaintext
sum(rate(apiserver_request_total{job="apiserver"}[5m])) by (verb, code)
```


**Scheduler activity**

```plaintext
sum(rate(scheduler_schedule_attempts_total[5m])) by (result)
```


This query is available on OpenShift Container Platform 4.22 and later with metrics forwarding enabled. 

**Workload-oriented API saturation**

```plaintext
apiserver_current_inflight_requests{job="apiserver"}
```


**Scheduling backlog**

```plaintext
scheduler_pending_pods
```


**Controller workqueue depth**

```plaintext
workqueue_depth{job="kube-controller-manager"}
```


For `csv_succeeded` and other OLM metrics, see "Exposed metrics". 




**Verification**

  * Prometheus targets for `control-plane-metrics-forwarder` scrape pools report the `health: up` status. 
  * PromQL queries for `apiserver_request_total{job="apiserver"}` return nonzero results. 
  * Example queries in the web console return time series for enabled components. 



**Additional resources**

  * [Exposed metrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-metrics_olm-understanding-metrics)



## 13.5.6. Import control plane health dashboards

You can import a sample Grafana dashboard that visualizes propagated control plane metrics in the hosted cluster web console. The dashboard covers API server, etcd, cluster Operators, scheduler, controller manager, and OLM health panels. 

**Prerequisites**

  * Metrics forwarding is enabled and verified. 
  * The HyperShift Operator uses `METRICS_SET=All` or `METRICS_SET=SRE` with a matching `sre-metric-set` `ConfigMap` object in the hosted control plane namespace. The default `Telemetry` metrics set forwards only a small metric subset and leaves most dashboard panels empty. 
  * You have `cluster-admin` access to the hosted cluster. 



**Procedure**

  1. Download the sample dashboard JSON file by entering the following command: 

```shell-session
$ curl -LO https://raw.githubusercontent.com/openshift/hypershift/main/contrib/metrics/guest-control-plane-dashboard.json
```


Note

If you deploy user-workload Grafana through the Grafana Operator, import the dashboard JSON as a `GrafanaDashboard` custom resource instead of using a console `ConfigMap` object. 

  2. Create a `ConfigMap` object from the dashboard file in the `openshift-config-managed` namespace by entering the following command: 

```shell-session
$ oc create configmap guest-control-plane-dashboard \
  --from-file=guest-control-plane-dashboard.json=guest-control-plane-dashboard.json \
  -n openshift-config-managed
```


  3. Label the `ConfigMap` object so the console discovers it as a dashboard by entering the following command: 

```shell-session
$ oc label configmap guest-control-plane-dashboard \
  console.openshift.io/dashboard=true \
  -n openshift-config-managed
```


  4. Log in to the web console and click **Observe** **Dashboards**. 
  5. Select the **Hosted Cluster Control Plane** dashboard. 
  6. Optional: If you use `METRICS_SET=SRE` on the HyperShift Operator, configure the Operator and create or update the `sre-metric-set` `ConfigMap` object in the hosted control plane namespace with relabel configurations that forward the dashboard metric names. 

     1. Log in to the management cluster and set the metrics set on the HyperShift Operator by entering the following command: 

```shell-session
$ oc set env -n hypershift deployment/operator METRICS_SET=SRE
```


     2. Replace `<hcp_namespace>` with your hosted control plane namespace and create the `ConfigMap` object: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: sre-metric-set
  namespace: <hcp_namespace>
data:
  config: |
    kubeAPIServer:
      - action: keep
        sourceLabels: ["__name__"]
        regex: "(apiserver_request_total|apiserver_request_duration_seconds_bucket|apiserver_current_inflight_requests|apiserver_storage_objects)"
    etcd:
      - action: keep
        sourceLabels: ["__name__"]
        regex: "(etcd_mvcc_db_total_size_in_bytes|etcd_mvcc_db_total_size_in_use_in_bytes|etcd_disk_wal_fsync_duration_seconds_bucket|etcd_disk_backend_commit_duration_seconds_bucket|etcd_network_peer_round_trip_time_seconds_bucket|etcd_server_leader_changes_seen_total|etcd_server_has_leader)"
    kubeControllerManager:
      - action: keep
        sourceLabels: ["__name__"]
        regex: "(workqueue_depth|workqueue_adds_total)"
    kubeScheduler:
      - action: keep
        sourceLabels: ["__name__"]
        regex: "(scheduler_e2e_scheduling_duration_seconds_count|scheduler_schedule_attempts_total|scheduler_pending_pods)"
    cvo:
      - action: keep
        sourceLabels: ["__name__"]
        regex: "(cluster_version|cluster_operator_up|cluster_operator_conditions)"
    olm:
      - action: keep
        sourceLabels: ["__name__"]
        regex: "(csv_succeeded)"
```


This configuration forwards 20 metric names across five components that the dashboard uses. 

For full `SRE` metrics set configuration, see "Configuring the SRE metrics set". 

     3. Apply the `ConfigMap` object on the management cluster: 

```shell-session
$ oc apply -f sre-metric-set.yaml
```


The Control Plane Operator detects the `ConfigMap` object change and updates the `metrics-proxy` configuration. 




**Verification**

  * The dashboard is displayed under **Observe** **Dashboards** in the web console. 
  * Panels display data when the configured metrics set includes the required metric names. 
  * The etcd database size panels show current use relative to the 8 GB limit.
