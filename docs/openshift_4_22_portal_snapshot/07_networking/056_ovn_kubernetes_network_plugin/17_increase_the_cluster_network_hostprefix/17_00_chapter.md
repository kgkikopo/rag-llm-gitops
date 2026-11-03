# Chapter 17. Increase the cluster network hostPrefix

You can increase the number of pod IP addresses available on each node by enlarging each node’s OVN-Kubernetes pod subnet after installation. This workflow updates the `k8s.ovn.org/node-subnets` node annotation while the Cluster Version Operator and Cluster Network Operator are scaled down. 

Important

  * Enlarging per-node subnets does not change the support for increased pod density or the number of pods that can be supported per node. Red Hat supports tested cluster maximums rather than absolute cluster maximums. You must still adhere to the cluster scalability limits, node resources, workload behavior, and operational constraints. See "Planning your environment according to object maximums". 
  * This procedure applies only to the cluster network, is supported only with OVN-Kubernetes, and requires sequential node maintenance to apply the updated per-node subnet size.

- [17.1. Cluster network hostPrefix overview](17_01_cluster_network_hostprefix_overview.md)
- [17.2. Planning for a cluster network hostPrefix increase](17_02_planning_for_a_cluster_network_hostprefix_increase.md)
- [17.3. Increase the per-node subnet size](17_03_increase_the_per_node_subnet_size.md)
- [17.4. Node drain options for hostPrefix changes](17_04_node_drain_options_for_hostprefix_changes.md)
- [17.5. Troubleshooting hostPrefix increases](17_05_troubleshooting_hostprefix_increases.md)
- [17.6. Additional resources](17_06_additional_resources.md)
