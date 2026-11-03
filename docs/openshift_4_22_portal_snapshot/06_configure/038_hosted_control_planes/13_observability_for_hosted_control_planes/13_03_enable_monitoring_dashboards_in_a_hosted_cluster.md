# 13.3. Enable monitoring dashboards in a hosted cluster

You can enable monitoring dashboards in a hosted cluster by creating a config map. 

**Procedure**

  1. Create the `hypershift-operator-install-flags` config map in the `local-cluster` namespace. See the following example configuration: 

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: hypershift-operator-install-flags
  namespace: local-cluster
data:
  installFlagsToAdd: "--monitoring-dashboards --metrics-set=All"
  installFlagsToRemove: ""
```


The `--monitoring-dashboards --metrics-set=All` flag adds the monitoring dashboard for all metrics. 

  2. Wait a couple of minutes for the HyperShift Operator deployment in the `hypershift` namespace to be updated to include the following environment variable: 

```yaml
    - name: MONITORING_DASHBOARDS
      value: "1"
```


When monitoring dashboards are enabled, for each hosted cluster that the HyperShift Operator manages, the Operator creates a config map named `hc-<hosted_cluster_namespace>-<hosted_cluster_name>` in the `openshift-config-managed` namespace, where `<hosted_cluster_namespace>` is the namespace of the hosted cluster and `<hosted_cluster_name>` is the name of the hosted cluster. As a result, a new dashboard is added in the administrative console of the management cluster. 

  3. To view the dashboard, log in to the management cluster’s console and go to the dashboard for the hosted cluster by clicking **Observe Dashboards**. 
  4. Optional: To disable monitoring dashboards in a hosted cluster, remove the `--monitoring-dashboards --metrics-set=All` flag from the `hypershift-operator-install-flags` config map. When you delete a hosted cluster, its corresponding dashboard is also deleted. 



**Additional resources**

  * [Customized hosted cluster identifiers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-observability#hcp-cluster-ids_hcp-observability "13.2. Customized hosted cluster identifiers")



## 13.3.1. Dashboard customization

To generate dashboards for each hosted cluster, the HyperShift Operator uses a template that is stored in the `monitoring-dashboard-template` config map in the Operator namespace (`hypershift`). This template contains a set of Grafana panels that contain the metrics for the dashboard. 

You can edit the content of the config map to customize the dashboards. 

When a dashboard is generated, the following strings are replaced with values that correspond to a specific hosted cluster: 

Name| Description  
---|---  
`__NAME__` |  The name of the hosted cluster   
`__NAMESPACE__` |  The namespace of the hosted cluster   
`__CONTROL_PLANE_NAMESPACE__` |  The namespace where the control plane pods of the hosted cluster are placed   
`__CLUSTER_ID__` |  The UUID of the hosted cluster, which matches the `_id` label of the hosted cluster metrics   
Show more

To set a custom cluster identifier when you create the hosted cluster, see "Customized hosted cluster identifiers".
