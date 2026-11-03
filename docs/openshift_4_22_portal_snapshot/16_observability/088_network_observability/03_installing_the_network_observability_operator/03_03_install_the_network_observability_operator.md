# 3.3. Install the Network Observability Operator

Install the Network Observability Operator and use the setup wizard to create the `FlowCollector` custom resource definition (CRD) to complete the initial configuration. 

You can set specifications in the web console when you create the `FlowCollector`. 

Important

The actual memory consumption of the Operator depends on your cluster size and the number of resources deployed. Memory consumption might need to be adjusted accordingly. For more information refer to "Network Observability controller manager pod runs out of memory" in the "Important Flow Collector configuration considerations" section. 

**Prerequisites**

  * If you choose to use Loki, install the [Loki Operator version 5.7+](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel8-operator/622b46bcae289285d6fcda39). 
  * You must have `cluster-admin` privileges. 
  * One of the following supported architectures is required: `amd64`, `ppc64le`, `arm64`, or `s390x`. 
  * Any CPU supported by Red Hat Enterprise Linux (RHEL) 9. 
  * Must be configured with OVN-Kubernetes as the main network plugin, and optionally using secondary interfaces with Multus and SR-IOV. 



Note

Additionally, this installation example uses the `netobserv` namespace, which is used across all components. You can optionally use a different namespace. 

**Procedure**

  1. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
  2. Choose **Network Observability Operator** from the list of available Operators in the software catalog, and click **Install**. 
  3. Select the checkbox `Enable Operator recommended cluster monitoring on this Namespace`. 
  4. Navigate to **Operators** **Installed Operators**. Under Provided APIs for Network Observability, select the **Flow Collector** link. 
  5. Follow the **Network Observability FlowCollector setup** wizard. 
  6. Click **Create**. 



**Verification**

To confirm this was successful, when you navigate to **Observe** you should see **Network Traffic** listed in the options. 

In the absence of **Application Traffic** within the OpenShift Container Platform cluster, default filters might show that there are "No results", which results in no visual flow. Beside the filter selections, select **Clear all filters** to see the flow. 

## 3.3.1. Important FlowCollector configuration considerations

Review essential `FlowCollector` configuration options before initial deployment to avoid pod disruptions caused by later reconfiguration. Key settings include Kafka integration, enriched flow data exports, SR-IOV traffic monitoring, and advanced tracking for DNS and packet drops. 

Once you create the `FlowCollector` instance, you can reconfigure it, but the pods are terminated and recreated again, which can be disruptive. 

Therefore, you can consider configuring the following options when creating the `FlowCollector` for the first time. 

**Additional resources**

  * [Configuring the Flow Collector resource with Kafka](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-flowcollector-kafka-config_network_observability "6.4. Configure the FlowCollector resource with Kafka")
  * [Export enriched network flow data to Kafka or IPFIX](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-enriched-flows_network_observability "6.5. Export enriched network flow data")
  * [Configuring monitoring for SR-IOV interface traffic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-secondary-networks#network-observability-SR-IOV-config_network-observability-secondary-networks "17.2. Configure monitoring for SR-IOV interface traffic")
  * [Working with conversation tracking](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-observe-network-traffic#network-observability-working-with-conversations_nw-observe-network-traffic "11.2.5. Work with conversation tracking")
  * [Working with DNS tracking](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-observe-network-traffic#network-observability-dns-tracking_nw-observe-network-traffic "11.1.6. Work with DNS tracking")
  * [Working with packet drops](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-observe-network-traffic#network-observability-packet-drops_nw-observe-network-traffic "11.1.4. Work with packet drops")
  * [Flow Collector API Reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-api-reference#flowcollector-api_network_observability "19.1.1. FlowCollector API")
  * [Flow Collector sample resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-flowcollector-view_network_observability "6.1. View the FlowCollector resource")
  * [Resource considerations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-resources-table_network_observability "6.9.1. Resource considerations")
  * [Troubleshooting network observability controller manager pod runs out of memory](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/installing-troubleshooting#controller-manager-pod-runs-out-of-memory_network-observability-troubleshooting "20.5. Network observability controller manager pod runs out of memory")
  * [Network observability architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-network-observability-operator#network-observability-architecture_nw-network-observability-operator "5.2. Network Observability Operator architecture")
