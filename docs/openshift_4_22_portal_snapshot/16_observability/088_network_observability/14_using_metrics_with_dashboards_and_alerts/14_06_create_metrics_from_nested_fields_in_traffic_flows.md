# 14.6. Create metrics from nested fields in Traffic flows

Create a `FlowMetric` custom resource to generate metrics for nested or array fields in the **Traffic flows** table, such as **Network events** or **Interfaces**. 

Important

OVN Observability / Viewing `NetworkEvents` is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

Important

OVN Observability and the ability to view and track network events is available only in OpenShift Container Platform 4.17 and 4.18. 

The following example shows how to generate metrics from the **Network events** field for network policy events. 

**Prerequisites**

  * Enable `NetworkEvents feature`. See the Additional resources for how to do this. 
  * A network policy specified. 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. In the **Provided APIs** heading for the **NetObserv Operator** , select **FlowMetric**. 
  3. In the **Project** dropdown list, select the project of the Network Observability Operator instance. 
  4. Click **Create FlowMetric**. 
  5. Create `FlowMetric` resources to add the following configurations: 

**Configuration counting network policy events per policy name and namespace**

```yaml
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: network-policy-events
  namespace: netobserv
spec:
  metricName: network_policy_events_total
  type: Counter
  labels: [NetworkEvents>Type, NetworkEvents>Namespace, NetworkEvents>Name, NetworkEvents>Action, NetworkEvents>Direction]
  filters:
  - field: NetworkEvents>Feature
    value: acl
  flatten: [NetworkEvents]
  remap:
    "NetworkEvents>Type": type
    "NetworkEvents>Namespace": namespace
    "NetworkEvents>Name": name
    "NetworkEvents>Direction": direction
```


where: 

`spec.labels`
     Specifies the labels that represent the nested fields for **Network Events** from the **Traffic flows** table. Each network event has a specific type, namespace, name, action, and direction. You can alternatively specify `Interfaces` if `NetworkEvents` is unavailable in your version of OpenShift Container Platform. 
`spec.flatten`
     Specifies an optional field that contains a list of items to be represented as distinct items. 
`spec.remap`
     Specifies an optional set of fields to rename in Prometheus. 




**Verification**

  1. In the web console, navigate to **Observe** **Dashboards** and scroll down to see the **Network Policy** tab. 
  2. You should begin seeing metrics filter in based on the metric you created along with the network policy specifications. 



Important

High cardinality can affect the memory usage of Prometheus. You can check if specific labels have high cardinality in the network flows format. See "Network Flows format reference". 

**Additional resources**

  * [Network Flows format reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-api-reference#network-flows-format_network_observability "19.1.4. Network flows format")
