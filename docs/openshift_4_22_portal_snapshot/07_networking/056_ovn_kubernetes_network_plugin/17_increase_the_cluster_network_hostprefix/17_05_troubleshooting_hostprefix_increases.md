# 17.5. Troubleshooting hostPrefix increases

Common issues when enlarging per-node subnets include annotation synchronization failures, pod scheduling delays, and partial-completion scenarios across nodes. 

## 17.5.1. Node does not receive an updated subnet

If a node does not reflect the expected subnet allocation after you annotate it and restart `ovnkube-node`: 

  * Confirm that the `k8s.ovn.org/node-subnets` annotation on the node shows the target prefix, for example `{"default":["10.131.0.0/21"]}`. 
  * Confirm that the Cluster Version Operator and network operator deployments are still scaled to `0` replicas while you make the change. 
  * Verify the OVN northbound logical switch for the node with `ovn-nbctl find logical_switch name=<node_name>`. 
  * Verify node readiness and that the `ovnkube-node` pod on the node is `Running`. 
  * If the enlarged subnet overlaps another node’s allocation, choose a non-overlapping block from the cluster network CIDR and update the annotation again. 



## 17.5.2. Pods do not reschedule after node drain

If workloads do not recover after draining a node: 

  * Check for pod disruption budget constraints. 
  * Check for insufficient cluster capacity on remaining schedulable nodes. 
  * Review workload-specific constraints, such as affinity, taints, tolerations, and storage requirements. 



## 17.5.3. Partial completion across nodes

If only some nodes are updated: 

  * Stop processing additional nodes until operator and workload health are restored. 
  * Confirm that each completed node is in `Ready` state. 
  * Continue only when the cluster reports stable operator conditions. 



## 17.5.4. Data to collect for a support case

Before opening a support case, collect: 

  * A must-gather capture. 
  * Current network configuration: 

```shell-session
$ oc get network.config.openshift.io cluster -o yaml
```


  * Cluster operator state: 

```shell-session
$ oc get clusteroperators network -o yaml
```


  * Node status and conditions: 

```shell-session
$ oc get nodes -o wide
$ oc describe node <node>
```


  * Recent events in affected namespaces: 

```shell-session
$ oc get events -A --sort-by=.lastTimestamp
```
