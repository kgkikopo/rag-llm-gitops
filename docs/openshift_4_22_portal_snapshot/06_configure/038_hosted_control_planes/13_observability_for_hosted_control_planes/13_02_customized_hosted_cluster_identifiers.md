# 13.2. Customized hosted cluster identifiers

When you enable observability for hosted control planes, control plane metrics include an `_id` label that identifies the hosted cluster. You can set `spec.clusterID` in the `HostedCluster` custom resource (CR) at creation time to use a stable identifier instead of a randomly assigned UUID. 

When you forward hosted cluster metrics to an external monitoring system, the `_id` label is commonly used to identify the cluster. If you reinstall a hosted cluster, specifying the same `clusterID` value preserves your external monitoring configuration. 

Each hosted cluster has a unique cluster identifier. The HyperShift Operator uses this identifier in telemetry and in metrics that the control plane operators produce. The identifier is exposed on time series as the `_id` label. 

If you do not specify `spec.clusterID` when you create a `HostedCluster` CR, the HyperShift controller generates a random RFC4122 UUID and sets the field for you. 

Note

The `spec.clusterID` specification is not the same as the `spec.infraID` specification. The `infraID` value identifies cloud infrastructure resources. 

## 13.2.1. Example: Setting a custom cluster identifier

You can set the `spec.clusterID` value only when you create a `HostedCluster` custom resource (CR). 

Important

After you set `spec.clusterID` is set, you cannot change it. Plan the identifier before you create the hosted cluster. 

The following example shows a `HostedCluster` CR with a custom cluster identifier set: 

**Example`HostedCluster` CR with a custom cluster identifier**

```yaml
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_cluster_namespace>
spec:
  clusterID: fa45babd-40f3-4085-9b30-8bc3b7df1557
  controllerAvailabilityPolicy: SingleReplica
  dns:
    baseDomain: example.com
  platform:
    type: AWS
  release:
    image: <ocp_release_image>
  pullSecret:
    name: <pull_secret_name>
```


The `spec.clusterID` value is the UUID that you want to use as the stable cluster identifier in metrics. The value must be a valid RFC4122 UUID: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` in hexadecimal digits. 

The value of `spec.clusterID` is added as the `_id` label on control plane metrics through Prometheus relabeling rules on `ServiceMonitor` and `PodMonitor` resources. HyperShift Operator metrics for the hosted cluster also use the same `_id` label, so you can correlate metrics from the management cluster and the hosted control plane in one query. 

For example, to filter metrics for a specific hosted cluster, use the `_id` label in a PromQL expression: 

```plaintext
{__name__=~"hypershift_.*", _id="fa45babd-40f3-4085-9b30-8bc3b7df1557"}
```


When you enable monitoring dashboards, the `_CLUSTER_ID_` placeholder in the dashboard template is replaced with the same UUID. For more information, see "Dashboard customization". 

### 13.2.1.1. Cluster identifier reuse after a reinstall

If you delete and re-create a hosted cluster, a new random `clusterID` is assigned unless you specify one. To keep the same identifier in external monitoring systems, set `spec.clusterID` in the new `HostedCluster` CR to the UUID that you used before. 

**Additional resources**

  * [Dashboard customization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-observability#hcp-customize-dashboards_hcp-observability "13.3.1. Dashboard customization")
  * [Configuring metrics sets for hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-observability#hosted-control-planes-metrics-sets_hcp-observability "13.1. Configure metrics sets for hosted control planes")
  * [Enabling monitoring dashboards in a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-observability#hosted-control-planes-monitoring-dashboard_hcp-observability "13.3. Enable monitoring dashboards in a hosted cluster")
