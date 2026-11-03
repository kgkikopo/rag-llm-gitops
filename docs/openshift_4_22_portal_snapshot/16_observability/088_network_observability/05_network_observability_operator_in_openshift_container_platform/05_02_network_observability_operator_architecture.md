# 5.2. Network Observability Operator architecture

Review the Network Observability Operator architecture, detailing how the `FlowCollector` resource manages the `eBPF agent`, which collects and enriches flows, sending the data to Loki for storage or Prometheus for metrics. 

The Network Observability Operator provides the `FlowCollector` API, which is instantiated at installation and configured to reconcile the `eBPF agent`, the `flowlogs-pipeline`, and the `netobserv-plugin` components. Only a single `FlowCollector` per cluster is supported. 

The `eBPF agent` runs on each cluster node with some privileges to collect network flows. The `flowlogs-pipeline` receives the network flows data and enriches the data with Kubernetes identifiers. If you choose to use Loki, the `flowlogs-pipeline` sends flow logs data to Loki for storing and indexing. The `netobserv-plugin`, which is a dynamic OpenShift Container Platform web console plugin, queries Loki to fetch network flows data. Cluster-admins can view the data in the web console. 

If you do not use Loki, you can generate metrics with Prometheus. Those metrics and their related dashboards are accessible in the web console. For more information, see "Network Observability without Loki". 

![Network Observability eBPF export architecture](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/4f6103cf90d1fc732ac861b8720c2b91/network-observability-architecture.png) ![Network Observability eBPF export architecture](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/4f6103cf90d1fc732ac861b8720c2b91/network-observability-architecture.png)

There are three deployment model options for the Network Observability Operator. 

Note

The Network Observability Operator does not manage Loki or other data stores. You must install Loki separately by using the Loki Operator. If you use Kafka, you must install it separately by using the Kafka Operator. 

Service deployment model
     When the `spec.deploymentModel` field in the `FlowCollector` resource is set to `Service`, agents are deployed per node as daemon sets. The `flowlogs-pipeline` is a standard deployment with a service. You can scale the `flowlogs-pipeline` component by using the `spec.processor.consumerReplicas` field. 
Direct deployment model
     When the `spec.deploymentModel` field is set to `Direct`, agents and the `flowlogs-pipeline` are both deployed per node as daemon sets. This model is suitable for technology assessments and small clusters. However, it is less memory-efficient in large clusters because each instance of `flowlogs-pipeline` caches the same cluster information. 
Kafka deployment model (optional)
    

If you use the Kafka option, the `eBPF agent` sends the network flow data to Kafka. You can scale the `flowlogs-pipeline` component by using the `spec.processor.consumerReplicas` field. The `flowlogs-pipeline` component reads from the Kafka topic before sending data to Loki, as shown in the following diagram. 

![Network Observability using Kafka](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/c5ad5d7a43c0edced45290056ced0c80/network-observability-arch-kafka-FLP.png) ![Network Observability using Kafka](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/c5ad5d7a43c0edced45290056ced0c80/network-observability-arch-kafka-FLP.png)

**Additional resources**

  * [Network Observability without Loki](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/installing-network-observability-operators#network-observability-without-loki_network_observability "3.1. Network observability without Loki")
