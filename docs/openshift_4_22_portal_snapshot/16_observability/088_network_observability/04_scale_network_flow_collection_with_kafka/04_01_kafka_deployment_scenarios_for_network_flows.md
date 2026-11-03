# 4.1. Kafka deployment scenarios for network flows

The Kafka Operator manages high-throughput and low-latency data feeds for network flow forwarding. This architecture provides a resilient and scalable solution for handling telemetry data in large-scale cluster environments. 

## 4.1.1. When to use Kafka for network flow collection

Consider using Kafka to manage your network flow data when you experience the following circumstances: 

  * High flow volumes that overwhelm the default flowlogs-pipeline buffer 
  * Need for data persistence and replay capabilities 
  * Multiple consumers requiring access to the same flow data 
  * Requirements for horizontal scaling across multiple processing nodes 



For smaller deployments with moderate flow volumes, the default configuration without Kafka is typically sufficient. 

You can install the Kafka Operator as Red Hat AMQ Streams from the Operator Hub. See "Red Hat AMQ Streams". 

Note

To uninstall Kafka, refer to the uninstallation process that corresponds with the method you used to install.
