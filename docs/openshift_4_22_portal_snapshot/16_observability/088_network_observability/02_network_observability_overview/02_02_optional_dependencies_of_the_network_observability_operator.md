# 2.2. Optional dependencies of the Network Observability Operator

Integrate the Network Observability Operator with optional dependencies, such as the Loki Operator for flow storage and AMQ Streams (Kafka) for resilient, large-scale data handling and scalability. 

Supported optional dependencies include the Loki Operator for flow storage, and AMQ Streams for large-scale data handling with Kafka. 

Loki Operator
     You can use Loki as the backend to store all collected flows with a maximal level of details. It is recommended to use the Red Hat supported Loki Operator to install Loki. You can also choose to use network observability without Loki, but you need to consider some factors. For more information, see "Network observability without Loki". 
AMQ Streams Operator
    

Kafka provides scalability, resiliency and high availability in the OpenShift Container Platform cluster for large scale deployments. 

Note

If you choose to use Kafka, it is recommended to use Red Hat supported AMQ Streams Operator. 

**Additional resources**

  * [Network observability without Loki](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/installing-network-observability-operators#network-observability-without-loki_network_observability "3.1. Network observability without Loki")
  * [Red Hat AMQ Streams](https://docs.redhat.com/en/documentation/red_hat_streams_for_apache_kafka/2.2)
