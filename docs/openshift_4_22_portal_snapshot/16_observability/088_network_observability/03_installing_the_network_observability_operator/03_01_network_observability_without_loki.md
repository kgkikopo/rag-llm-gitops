# 3.1. Network observability without Loki

Compare the features available with network observability with and without installing the Loki Operator. 

If you only want to export flows to a Kafka consumer or IPFIX collector, or you only need dashboard metrics, then you do not need to install Loki or provide storage for Loki. The following table compares available features with and without Loki. 

Table 3.1. Comparison of feature availability with and without Loki | **With Loki**| **Without Loki**  
---|---|---  
**Exporters** |  X  |  X   
**Multi-tenancy** |  X  |  X   
**Complete filtering and aggregations capabilities** [1] |  X  |   
**Partial filtering and aggregations capabilities** [2] |  X  |  X   
**Flow-based metrics and dashboards** |  X  |  X   
**Traffic flows view overview** [3] |  X  |  X   
**Traffic flows view table** |  X  |   
**Topology view** |  X  |  X   
**OpenShift Container Platform console Network Traffic tab integration** |  X  |  X   
Show more

  1. Such as per pod. 
  2. Such as per workload or namespace. 
  3. Statistics on packet drops are only available with Loki. 



**Additional resources**

  * [Export enriched network flow data](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-enriched-flows_network_observability "6.5. Export enriched network flow data")
