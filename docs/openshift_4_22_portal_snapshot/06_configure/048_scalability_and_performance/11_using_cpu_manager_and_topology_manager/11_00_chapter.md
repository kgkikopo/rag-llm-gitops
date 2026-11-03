# Chapter 11. Using CPU Manager and Topology Manager

CPU Manager manages groups of CPUs and constrains workloads to specific CPUs. 

CPU Manager is useful for workloads that have some of these attributes: 

  * Require as much CPU time as possible. 
  * Are sensitive to processor cache misses. 
  * Are low-latency network applications. 
  * Coordinate with other processes and benefit from sharing a single processor cache. 



Topology Manager collects hints from the CPU Manager, Device Manager, and other Hint Providers to align pod resources, such as CPU, SR-IOV VFs, and other device resources, for all Quality of Service (QoS) classes on the same non-uniform memory access (NUMA) node. 

Topology Manager uses topology information from the collected hints to decide if a pod can be accepted or rejected on a node, based on the configured Topology Manager policy and pod resources requested. 

Topology Manager is useful for workloads that use hardware accelerators to support latency-critical execution and high throughput parallel computation. 

To use Topology Manager you must configure CPU Manager with the `static` policy.

- [11.1. Set up CPU Manager](11_01_set_up_cpu_manager.md)
- [11.2. Topology Manager policies](11_02_topology_manager_policies.md)
- [11.3. Set up Topology Manager](11_03_set_up_topology_manager.md)
- [11.4. Pod interactions with Topology Manager policies](11_04_pod_interactions_with_topology_manager_policies.md)
