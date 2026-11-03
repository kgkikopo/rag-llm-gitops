# 3.6. Deployment planning

Proper deployment planning is essential for telco core clusters to ensure high availability, minimize service disruption during upgrades, and optimize cluster performance. 

## 3.6.1. Worker Nodes and MachineConfigPools

`MachineConfigPools` (MCPs) custom resources (CR) subdivide worker nodes in telco core clusters into different node groups. Careful MCP planning minimizes deployment and upgrade time and interruption of telco-grade services. 

**Description**

Telco core clusters can use `MachineConfigPools` (MCPs) to split worker nodes into additional separate roles, for example, due to different hardware profiles. This allows custom tuning for each role and also plays a critical function in speeding up a telco core cluster deployment or upgrade. Multiple MCPs can be used to properly plan cluster upgrades across one or multiple maintenance windows. This is crucial because telco-grade services might otherwise be affected if careful planning is not considered. 

During cluster upgrades, you can pause MCPs while you upgrade the control plane. See "Performing a canary rollout update" for more information. This ensures that worker nodes are not rebooted and running workloads remain unaffected until the MCP is unpaused. 

Using careful MCP planning, you can control the timing and order of which set of nodes are upgraded at any time. For more information on how to use MCPs to plan telco upgrades, see "Applying MachineConfigPool labels to nodes before the update". 

Before beginning the initial deployment, review the following engineering considerations: 

**PerformanceProfile and Tuned profile association:**

When using PerformanceProfiles, remember that each Machine Config Pool (MCP) must be linked to exactly one PerformanceProfile or Tuned profile definition. Consequently, even if the desired configuration is identical for multiple MCPs, each MCP still requires its own dedicated PerformanceProfile definition. 

**Planning your MCP labeling strategy:**

Plan your MCP labeling with an appropriate strategy to split your worker nodes depending on parameters such as: 

  * The worker node type: identifying a group of nodes with equivalent hardware profile, for example workers for control plane Network Functions (NFs) and workers for user data plane NFs. 
  * The number of worker nodes per worker node type. 
  * The minimum number of MCPs required for an equivalent hardware profile is 1, but could be larger for larger clusters. For example, you may design for more MCPs per hardware profile to support a more granular upgrade where a smaller percentage of the cluster capacity is affected with each step. 
  * The update strategy for nodes within an MCP is by upgrade requirements and the chosen `maxUnavailable` value: 

    * Number of maintenance windows allowed 
    * Duration of a maintenance window 
    * Total number of worker nodes 
    * Desired `maxUnavailable` (number of nodes updated concurrently) for the MCP. 

  * CNF requirements for worker nodes, in terms of: 

    * Minimum availability per Pod required during an upgrade, configured with a pod disruption budget (PDB). PDBs are crucial to maintain telco service level Agreements (SLAs) during upgrades. For more information about PDB, see "Understanding how to use pod disruption budgets to specify the number of pods that must be up". 
    * Minimum true high availability required per Pod, such that each replica runs on separate hardware. 
    * Pod affinity and anti-affinity link: For more information about how to use pod affinity and anti-affinity, see "Placing pods relative to other pods using affinity and anti-affinity rules". 

  * Duration and number of upgrade maintenance windows during which telco-grade services might be affected. 



## 3.6.2. Zones

OpenShift Container Platform uses the `topology.kubernetes.io/zone` label to spread replicas across failure domains so that the loss of a single zone does not violate high-availability constraints. 

Annotating nodes for topology zones allows high-availability workloads to spread so that each zone holds only one replica from a set of replicated pods. OpenShift Container Platform applies a default `TopologySpreadConstraint` to all replica constructs, such as `Service`, `ReplicaSet`, `StatefulSet`, or `ReplicationController` resources. 

Cluster upgrades typically result in node disruption as the underlying OS is updated. In large clusters it is necessary to update multiple nodes concurrently in order to complete upgrades quickly and in as few maintenance windows as possible. By using zones to ensure pod spread, an upgrade can be applied to all nodes in a zone simultaneously (assuming sufficient spare capacity) while maintaining high availability and service availability. The recommended cluster design is to partition nodes into multiple MCPs based on the considerations above and label all nodes in a single MCP as a single zone which is distinct from zones attached to other MCPs. Using this strategy all nodes in an MCP can be updated simultaneously. 

Lifecycle hooks (readiness, liveness, startup and pre-stop) play an important role in ensuring application availability. For upgrades in particular the pre-stop hook allows applications to take necessary steps to prepare for disruption prior to being evicted from the node. 

Limits and requirements
    

  * The default TopologySpreadConstraints (TSC) only apply when an explicit TSC is not given. If your pods have explicit TSC ensure that spread based on zones is included. 
  * The cluster must have sufficient spare capacity to tolerate simultaneous update of an MCP. Otherwise the `maxUnavailable` of the MCP must be set to less than 100%. 
  * The ability to update all nodes in an MCP simultaneously further depends on workload design and ability to maintain required service levels with that level of disruption. 



Engineering Considerations
    

  * Pod drain times can significantly impact node update times. Ensure the workload design allows pods to be drained quickly. 
  * PodDisruptionBudgets (PDB) are used to enforce high availability requirements. 

    * With sufficient zones in the cluster design, a zone can be disrupted or lost without violating the PDB. If there are insufficient zones, or other scheduling constraints restrict the set of available nodes, the scheduling of pods might violate the PDB when the zone is disrupted or lost. During upgrades with simultaneous node updates this might lead to partial serialization of updates. 
    * PDB with 0 disruptable pods will block node drain and require administrator intervention. This pattern should be avoided for fast and automated upgrades. 




**Additional resources**

  * [Performing a canary rollout update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#update-using-custom-machine-config-pools)
  * [Applying MachineConfigPool labels to nodes before the update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#update-using-custom-machine-config-pools)
  * [Understanding how to use pod disruption budgets to specify the number of pods that must be up](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-pod-disruption-about_nodes-pods-configuring)
  * [Placing pods relative to other pods using affinity and anti-affinity rules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-pod-affinity)
