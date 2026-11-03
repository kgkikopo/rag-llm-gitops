# Chapter 6. Configuring the Network Observability Operator

Configure the Network Observability Operator by updating the cluster-wide `FlowCollector` API resource (cluster) to manage component configurations and flow collection settings. 

The `FlowCollector` is explicitly created during installation. Since this resource operates cluster-wide, only a single `FlowCollector` is allowed, and it must be named `cluster`. For more information, see the "`FlowCollector` API reference".

- [6.1. View the FlowCollector resource](06_01_view_the_flowcollector_resource.md)
- [6.2. OpenShift TLS security profile support](06_02_openshift_tls_security_profile_support.md)
- [6.3. Grant permissions for custom namespace and secret access](06_03_grant_permissions_for_custom_namespace_and_secret_access.md)
- [6.4. Configure the FlowCollector resource with Kafka](06_04_configure_the_flowcollector_resource_with_kafka.md)
- [6.5. Export enriched network flow data](06_05_export_enriched_network_flow_data.md)
- [6.6. Update the FlowCollector resource](06_06_update_the_flowcollector_resource.md)
- [6.7. Filter network flows at ingestion](06_07_filter_network_flows_at_ingestion.md)
- [6.8. Configure quick filters](06_08_configure_quick_filters.md)
- [6.9. Resource management and performance considerations](06_09_resource_management_and_performance_considerations.md)
