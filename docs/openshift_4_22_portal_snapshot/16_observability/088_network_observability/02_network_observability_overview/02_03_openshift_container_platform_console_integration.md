# 2.3. OpenShift Container Platform console integration

The Network Observability Operator integrates with the OpenShift Container Platform console to visualize and analyze network traffic through views that display traffic overviews, topology graphs, and detailed flow tables for troubleshooting connectivity issues. 

The Network observability metrics dashboards in **Observe** **Dashboards** are available only to users with administrator access. 

Note

To enable multi-tenancy for developer access and for administrators with limited access to namespaces, you must specify permissions by defining roles. For more information, see "Enabling multi-tenancy in network observability". 

**Additional resources**

  * [Enable multi-tenancy in network observability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/installing-network-observability-operators#network-observability-multi-tenancy_network_observability "3.4. Enable multi-tenancy in network observability")



## 2.3.1. Network observability metrics dashboards

The network observability dashboards in the OpenShift Container Platform console provide cluster traffic pattern monitoring, metric filtering, and Network Observability Operator health tracking. 

In the OpenShift Container Platform console on the **Overview** tab, you can view the overall aggregated metrics of the network traffic flow on the cluster. You can choose to display the information by cluster, node, namespace, owner, pod, and service. Filters and display options can further refine the metrics. For more information, see "Observing the network traffic from the Overview view". 

In **Observe** **Dashboards** , the **Netobserv** dashboards provide a quick overview of the network flows in your OpenShift Container Platform cluster. The **Netobserv/Health** dashboard provides metrics about the health of the Operator. For more information, see "Network observability metrics" and "Viewing health information". 

**Additional resources**

  * [Observing the network traffic from the Overview view](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-observe-network-traffic#network-observability-network-traffic-overview-view_nw-observe-network-traffic "11.1. Observe the network traffic from the Overview view")
  * [Network observability metrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/metrics-dashboards-alerts#network-observability-metrics_metrics-dashboards-alerts "14.2. Network observability metrics")
  * [Health dashboards](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-operator-monitoring#network-observability-health-dashboard-overview_network_observability "15.1. Health dashboards")



## 2.3.2. Network observability topology views

The network observability topology view in the OpenShift Container Platform console displays a graphical representation of traffic flow between components, which you can refine using various filters and display options. 

The OpenShift Container Platform console offers the **Topology** tab which represents traffic between the OpenShift Container Platform components as a network graph. You can refine the graph by using the filters and display options. You can access the information for cluster, zone, udn, node, namespace, owner, pod, and service. 

## 2.3.3. Traffic flow tables

The **Traffic flow** tables in the OpenShift Container Platform console provide detailed network flow data with filtering options, customizable columns, and tools to analyze connection patterns and troubleshoot issues. 

The **Traffic flows** tab in the OpenShift Container Platform web console displays the data of the network flows and the amount of traffic.
