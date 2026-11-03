# 4.1. Controlling pod placement using the scheduler

You can rely on the default pod scheduling or use the advanced pod scheduling tool for greater control over pod scheduling. Pod scheduling is an internal process that determines placement of new pods onto nodes within the cluster. 

The scheduler code has a clean separation that watches new pods as they get created and identifies the most suitable node to host them. It then creates bindings (pod to node bindings) for the pods using the master API. 

Default pod scheduling
     OpenShift Container Platform comes with a default scheduler that serves the needs of most users. The default scheduler uses both inherent and customization tools to determine the best fit for a pod. 
Advanced pod scheduling
    

In situations where you might want more control over where new pods are placed, the OpenShift Container Platform advanced scheduling features allow you to configure a pod so that the pod is required or has a preference to run on a particular node or alongside a specific pod. 

You can control pod placement by using the following scheduling features: 

  * Scheduler profiles 
  * Pod affinity and anti-affinity rules 
  * Node affinity 
  * Node selectors 
  * Taints and tolerations 
  * Node overcommitment 



## 4.1.1. About the default scheduler

The default OpenShift Container Platform pod scheduler is responsible for determining the placement of new pods onto nodes within the cluster. It reads data from the pod and finds a node that is a good fit based on configured profiles. It is completely independent and exists as a standalone solution. It does not modify the pod; it creates a binding for the pod that ties the pod to the particular node. 

### 4.1.1.1. Understanding default scheduling

The existing generic scheduler is the default platform-provided scheduler _engine_ that selects a node to host the pod. 

The default scheduler selects the node in a three-step operation: 

Filters the nodes
     The available nodes are filtered based on the constraints or requirements specified. This is done by running each node through the list of filter functions called _predicates_ , or _filters_. 
Prioritizes the filtered list of nodes
     This is achieved by passing each node through a series of _priority_ , or _scoring_ , functions that assign it a score between 0 - 10, with 0 indicating a bad fit and 10 indicating a good fit to host the pod. The scheduler configuration can also take in a simple _weight_ (positive numeric value) for each scoring function. The node score provided by each scoring function is multiplied by the weight (default weight for most scores is 1) and then combined by adding the scores for each node provided by all the scores. This weight attribute can be used by administrators to give higher importance to some scores. 
Selects the best fit node
     The nodes are sorted based on their scores and the node with the highest score is selected to host the pod. If multiple nodes have the same high score, then one of them is selected at random. 

### 4.1.1.2. Scheduler use cases

You can configure the cluster scheduler to apply affinity and anti-affinity policies across customizable infrastructure topological levels to meet application latency and high-availability requirements. 

Infrastructure topological levels
    

Administrators can define multiple topological levels for their infrastructure (nodes) by specifying labels on nodes. For example: `region=r1`, `zone=z1`, `rack=s1`. 

These label names have no particular meaning and administrators are free to name their infrastructure levels anything, such as city/building/room. Also, administrators can define any number of levels for their infrastructure topology, with three levels usually being adequate (such as: `regions` `zones` `racks`). Administrators can specify affinity and anti-affinity rules at each of these levels in any combination. 

Affinity
    

Administrators should be able to configure the scheduler to specify affinity at any topological level, or even at multiple levels. Affinity at a particular level indicates that all pods that belong to the same service are scheduled onto nodes that belong to the same level. This handles any latency requirements of applications by allowing administrators to ensure that peer pods do not end up being too geographically separated. If no node is available within the same affinity group to host the pod, then the pod is not scheduled. 

If you need greater control over where the pods are scheduled, see "Controlling pod placement on nodes using node affinity rules" and "Placing pods relative to other pods using affinity and anti-affinity rules". 

These advanced scheduling features allow administrators to specify which node a pod can be scheduled on and to force or reject scheduling relative to other pods. 

Anti-affinity
    

Administrators should be able to configure the scheduler to specify anti-affinity at any topological level, or even at multiple levels. Anti-affinity (or 'spread') at a particular level indicates that all pods that belong to the same service are spread across nodes that belong to that level. This ensures that the application is well spread for high availability purposes. The scheduler tries to balance the service pods across all applicable nodes as evenly as possible. 

If you need greater control over where the pods are scheduled, see "Controlling pod placement on nodes using node affinity rules" and "Placing pods relative to other pods using affinity and anti-affinity rules". 

These advanced scheduling features allow administrators to specify which node a pod can be scheduled on and to force or reject scheduling relative to other pods. 

## 4.1.2. Additional resources

  * [Scheduler profiles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-profiles "4.2. Scheduling pods using a scheduler profile")
  * [Pod affinity and anti-affinity rules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-pod-affinity "4.3. Placing pods relative to other pods using affinity and anti-affinity rules")
  * [Node affinity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-node-affinity-about_nodes-scheduler-node-affinity "4.4.1. Understanding node affinity")
  * [Node selectors](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-node-selectors "4.7. Placing pods on specific nodes using node selectors")
  * [Taints and tolerations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-taints-tolerations "4.6. Controlling pod placement using node taints")
  * [Node overcommitment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-overcommit "4.5. Placing pods onto overcommited nodes")
  * [Controlling pod placement on nodes using node affinity rules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-node-affinity "4.4. Controlling pod placement on nodes using node affinity rules")
  * [Placing pods relative to other pods using affinity and anti-affinity rules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-pod-affinity "4.3. Placing pods relative to other pods using affinity and anti-affinity rules")
