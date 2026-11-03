# Chapter 12. Scheduling NUMA-aware workloads

To deploy high performance workloads with optimal efficiency, use NUMA-aware scheduling. This feature aligns pods with the underlying hardware topology in your OpenShift Container Platform cluster, minimizing latency and maximizing resource utilization. 

By using the NUMA Resources Operator, you can schedule high-performance workloads in the same NUMA zone. The Operator deploys a node resources exporting agent that reports on available cluster node NUMA resources, and a secondary scheduler that manages the workloads.

- [12.1. About NUMA](12_01_about_numa.md)
- [12.2. About NUMA-aware scheduling](12_02_about_numa_aware_scheduling.md)
- [12.3. NUMA resource scheduling strategies](12_03_numa_resource_scheduling_strategies.md)
- [12.4. Installing the NUMA Resources Operator](12_04_installing_the_numa_resources_operator.md)
- [12.5. Configuring a single NUMA node policy](12_05_configuring_a_single_numa_node_policy.md)
- [12.6. Scheduling NUMA-aware workloads](12_06_scheduling_numa_aware_workloads.md)
- [12.7. NUMA Resources Operator support for schedulable control-plane nodes](12_07_numa_resources_operator_support_for_schedulable_control_plane_nodes.md)
- [12.8. Configure polling operations for NUMA resources updates](12_08_configure_polling_operations_for_numa_resources_updates.md)
- [12.9. Topology-aware scheduler scalability](12_09_topology_aware_scheduler_scalability.md)
- [12.10. Troubleshoot NUMA-aware scheduling](12_10_troubleshoot_numa_aware_scheduling.md)
