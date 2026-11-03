# 12.7. NUMA Resources Operator support for schedulable control-plane nodes

You can enable schedulable control plane nodes to run user-defined pods, effectively turning the nodes into hybrid control plane and compute nodes. This configuration is especially beneficial in resource-constrained environments, such as compact clusters. 

When enabled, the NUMA Resources Operator can apply its topology-aware scheduling to the nodes for guaranteed workloads, ensuring pods are placed according to the best NUMA affinity. 

Traditionally, control plane nodes in OpenShift Container Platform are dedicated to running critical cluster services. Enabling schedulable control plane nodes allows user-defined Pods to be scheduled on the nodes. 

You can make control plane nodes schedulable by setting the `mastersSchedulable` field to true in the `schedulers.config.openshift.io` resource. 

Note

When you enable schedulable control plane nodes, enabling workload partitioning is strongly recommended to safeguard critical infrastructure pods from resource starvation. This process restricts infrastructure components, like the `ovnkube-node` process, to dedicated, reserved CPUs. However, the OVS dynamic pinning feature relies on `ovnkube-node` having access to the CPUs designated for bustable/best-effort pods to correctly identify and use non-pinned CPUs. When workload partitioning configures the `ovnkube-node` process with CPU affinity for reserved CPUs, this dynamic pinning mechanism breaks. 

The NUMA Resources Operator provides topology-aware scheduling for workloads that need a specific NUMA affinity. When control plane nodes are made schedulable, the management capabilities of the Operator can be applied to them, just as they are to compute nodes. This ensures that NUMA-aware pods are placed on a node with the best NUMA topology, whether it is a control plane or compute node. 

When configuring the NUMA Resources Operator, its management scope is determined by the `nodeGroups` field in its custom resource (CR). This principle applies to both compact and multi-node clusters. 

Compact clusters
     In a compact cluster, all nodes are configured as schedulable control plane nodes. The NUMA Resources Operator can be configured to manage all nodes in the cluster. Follow the deployment instructions for more details on the process. 
Multi-Node OpenShift (MNO) clusters
     In a Multi-Node OpenShift Container Platform cluster, control plane nodes are made schedulable in addition to existing compute nodes. To manage these nodes, you can configure the NUMA Resources Operator by defining separate `nodeGroups` in the `NUMAResourcesOperator` CR for the control plane and compute nodes. This ensures that the NUMA Resources Operator correctly schedules pods on both sets of nodes based on resource availability and NUMA topology. 

Note

Modifying a performance profile often triggers control plane node reboots. Due to stricter Pod Disruption Budgets (PDBs) on control plane nodes, the cluster’s resilience mechanisms are activated. These mechanisms prevent the forced eviction of protected but unhealthy pods such as those in `CrashLoopBackOff`, which causes the Machine Config Pool (MCP) to stall during the reboot process. 

If the MCP becomes stuck due to this behavior, intervention is required to resolve the issue and allow the control plane upgrade to complete. 

To resolve this, administrators have two options: 

  1. Temporarily relax the PDB restrictions to allow the required eviction. 
  2. Manually delete the unhealthy pods to force the MCP to reconcile and continue the drain process. 



## 12.7.1. Configure NUMA Resources Operator on schedulable control plane nodes

To run workloads on control plane nodes, configure the NUMA Resources Operator (NROP) to manage them as schedulable. This configuration is ideal for compact clusters and multi-node OpenShift (MNO) environments where control plane nodes also function as compute nodes. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in as a user with `cluster-admin` privileges. 
  * Install the NUMA Resources Operator. 



**Procedure**

  1. To enable Topology Aware Scheduling (TAS) on control plane nodes, configure the nodes to be schedulable first. This allows the NUMA Resources Operator to deploy and manage pods on them. Without this action, the operator cannot deploy the pods required to gather NUMA topology information from these nodes. Follow these steps to make the control plane nodes schedulable: 

     1. Edit the `schedulers.config.openshift.io` resource by running the following command: 

```shell-session
$ oc edit schedulers.config.openshift.io cluster
```


     2. In the editor, set the `mastersSchedulable` field to `true`, then save and exit the editor. 

```yaml
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  creationTimestamp: "2019-09-10T03:04:05Z"
  generation: 1
  name: cluster
  resourceVersion: "433"
  selfLink: /apis/config.openshift.io/v1/schedulers/cluster
  uid: a636d30a-d377-11e9-88d4-0a60097bee62
spec:
  mastersSchedulable: true
status: {}
#...
```


  2. To configure the NUMA Resources Operator, you must create a single NUMAResourcesOperator custom resource (CR) on the cluster. The `nodeGroups` configuration within this CR specifies the node pools the Operator must manage. 

Note

Before configuring `nodeGroups`, ensure the specified node pool meets all prerequisites detailed in Section 12.5, "Configuring a single NUMA node policy." The NUMA Resources Operator requires all nodes within a group to be identical. Non-compliant nodes prevent the NUMA Resources Operator from performing the expected topology-aware scheduling for the entire pool. 

You can specify multiple non-overlapping node sets for the NUMA Resources Operator to manage. Each of these sets should correspond to a different machine config pool (MCP). The NUMA Resources Operator then manages the schedulable control plane nodes within these specified node groups. 

     1. For a compact cluster, the compact cluster’s master nodes are also the schedulable nodes, so specify only the master pool. Create the following `nodeGroups` configuration in the `NUMAResourcesOperator` CR: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesOperator
metadata:
  name: numaresourcesoperator
spec:
  nodeGroups:
    - poolName: master
# ...
```


Note

Configuring a compact cluster with a worker pool in addition to the `master` pool should be avoided. While this setup does not break the cluster or affect operator functionality, it can lead to redundant or duplicate pods and create unnecessary noise in the system. The worker pool is essentially a pointless, empty MCP in this context and serves no purpose. 

     2. For an MNO cluster where both control plane and compute nodes are schedulable, you have the option to configure the NUMA Resources Operator to manage multiple `nodeGroups`. You can specify which nodes to include by adding their corresponding MCPs to the `nodeGroups` list in the `NUMAResourcesOperator` CR. The configuration depends entirely on your specific requirements. For example, to manage both the `master` and `worker-cnf` pools, create the following `nodeGroups` configuration in the NUMAResourcesOperator CR: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesOperator
metadata:
  name: numaresourcesoperator
spec:
  nodeGroups:
    - poolName: master
    - poolName: worker-cnf
# ...
```


Note

You can customize this list to include any combination of nodeGroups for management with Topology-Aware Scheduling. To prevent duplicate, pending pods, you must ensure that each `poolName` in the configuration corresponds to a MachineConfigPool (MCP) with a unique node selector label. The label must be applied only to the nodes within that specific pool and must not overlap with labels on any other nodes in the cluster. The `worker-cnf` MCP designates a set of nodes that run telecommunications workloads. 

     3. After you update the `nodeGroups` field in the `NUMAResourcesOperator` CR to reflect your cluster’s configuration, apply the changes by running the following command: 

```shell-session
$ oc apply -f <filename>.yaml
```


Note

Replace `<filename>.yaml` with the name of your configuration file. 




**Verification**

After applying the configuration, verify that the NUMA Resources Operator is correctly managing the schedulable control plane nodes by performing the following checks: 

  1. Confirm that the control plane nodes have the worker role and are schedulable by running the following command: 

```shell-session
$ oc get nodes
```


**Example output:**

```shell-session
NAME                STATUS   ROLES                         AGE     VERSION
worker-0            Ready    worker,worker-cnf             100m    v1.35.4
worker-1            Ready    worker                        93m     v1.35.4
master-0            Ready    control-plane,master,worker   108m    v1.35.4
master-1            Ready    control-plane,master,worker   107m    v1.35.4
master-2            Ready    control-plane,master,worker   107m    v1.35.4
worker-2            Ready    worker                        100m    v1.35.4
```


  2. Verify that the NUMA Resources Operator’s pods are running on the intended nodes by running the following command. You should see a numaresourcesoperator pod for each node group you specified in the CR: 

```shell-session
$ oc get pods -n openshift-numaresources -o wide
```


**Example output:**

```shell-session
NAME                                               READY   STATUS    RESTARTS   AGE     IP            NODE       NOMINATED NODE   READINESS GATES
numaresources-controller-manager-bdbdd574-xx6bw    1/1     Running   0          49m     10.130.0.17   master-0   <none>           <none>
numaresourcesoperator-master-lprrh                 2/2     Running   0          20m     10.130.0.20   master-0   <none>           2/2
numaresourcesoperator-master-qk6k4                 2/2     Running   0          20m     10.129.0.50   master-2   <none>           2/2
numaresourcesoperator-master-zm79n                 2/2     Running   0          20m     10.128.0.44   master-1   <none>           2/2
numaresourcesoperator-worker-cnf-gqlmd             2/2     Running   0          4m27s   10.128.2.21   worker-0   <none>           2/2
```


  3. Confirm that the NUMA Resources Operator has collected and reported the NUMA topology data for all nodes in the specified groups by running the following command: 

```shell-session
$ oc get noderesourcetopologies.topology.node.k8s.io
```


**Example output:**

```shell-session
NAME          AGE
worker-0      6m11s
master-0      22m
master-1      21m
master-2      21m
```


The presence of a `NodeResourceTopology` resource for a node confirms that the NUMA Resources Operator was able to schedule a pod on it to collect the data, enabling topology-aware scheduling. 

  4. Inspect a single Node Resource Topology by running the following command: 

```shell-session
$ oc get noderesourcetopologies <master_node_name> -o yaml
```


**Example output:**

```yaml
apiVersion: topology.node.k8s.io/v1alpha2
attributes:
- name: nodeTopologyPodsFingerprint
  value: pfp0v001ef46db3751d8e999
- name: nodeTopologyPodsFingerprintMethod
  value: with-exclusive-resources
- name: topologyManagerScope
  value: container
- name: topologyManagerPolicy
  value: single-numa-node
kind: NodeResourceTopology
metadata:
  annotations:
    k8stopoawareschedwg/rte-update: periodic
    topology.node.k8s.io/fingerprint: pfp0v001ef46db3751d8e999
  creationTimestamp: "2025-09-23T10:18:34Z"
  generation: 1
  name: master-0
  resourceVersion: "58173"
  uid: 35c0d27e-7d9f-43d3-bab9-2ebc0d385861
zones:
- costs:
  - name: node-0
    value: 10
  name: node-0
  resources:
  - allocatable: "3"
    available: "2"
    capacity: "4"
    name: cpu
  - allocatable: "1476189952"
    available: "1378189952"
    capacity: "1576189952"
    name: memory
  type: Node
# ...
```


The presence of this resource for a node with a master role proves that the NUMA Resources Operator was able to deploy its discovery pods onto that node. These pods are what gather the NUMA topology data, and they can only be scheduled on nodes that are considered schedulable. 

The output confirms that the procedure to make the master nodes schedulable was successful, as the NUMA Resources Operator has now collected and reported the NUMA-related information for that specific control plane node.
