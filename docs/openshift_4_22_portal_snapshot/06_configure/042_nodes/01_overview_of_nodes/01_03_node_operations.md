# 1.3. Node operations

Find procedures for reading, managing, and enhancing nodes in an OpenShift Container Platform cluster. 

## 1.3.1. Read operations

The read operations allow an administrator or a developer to get information about nodes in an OpenShift Container Platform cluster. 

  * [List all the nodes in a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-viewing-listing_nodes-nodes-viewing "6.1.1. About listing all the nodes in a cluster"). 
  * Get information about a node, such as memory and CPU usage, health, status, and age. 
  * [List pods running on a node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-viewing-listing-pods_nodes-nodes-viewing "6.1.2. Listing pods on a node in your cluster"). 



## 1.3.2. Management operations

As an administrator, you can easily manage a node in an OpenShift Container Platform cluster through several tasks: 

  * [Add or update node labels](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-working-updating_nodes-nodes-working "6.2.2. Understanding how to update labels on nodes"). A label is a key-value pair applied to a `Node` object. You can control the scheduling of pods using labels. 
  * Change node configuration using a custom resource definition (CRD), or the `kubeletConfig` object. 
  * Configure nodes to allow or disallow the scheduling of pods. Healthy worker nodes with a `Ready` status allow pod placement by default while the control plane nodes do not; you can change this default behavior by [configuring the worker nodes to be unschedulable](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-working-marking_nodes-nodes-working "6.2.3. Understanding how to mark nodes as unschedulable or schedulable") and [the control plane nodes to be schedulable](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-working-marking_nodes-nodes-working "6.2.3. Understanding how to mark nodes as unschedulable or schedulable"). 
  * [Allocate resources for nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-resources-configuring "6.12. Allocating resources for nodes in an OpenShift Container Platform cluster") using the `system-reserved` setting. You can allow OpenShift Container Platform to automatically determine the optimal `system-reserved` CPU and memory resources for your nodes, or you can manually determine and set the best resources for your nodes. 
  * [Configure the number of pods that can run on a node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-managing-max-pods-proc_nodes-nodes-managing-max-pods "6.5.1. Configure the maximum number of pods per node") based on the number of processor cores on the node, a hard limit, or both. 
  * Reboot a node gracefully using [pod anti-affinity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-rebooting-affinity_nodes-nodes-rebooting "6.9.2. Rebooting a node using pod anti-affinity"). 
  * [Delete a node from a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-working-deleting_nodes-nodes-working "6.2.5. Deleting nodes from a cluster") by scaling down the cluster using a compute machine set. To delete a node from a bare-metal cluster, you must first drain all pods on the node and then manually delete the node. 



## 1.3.3. Enhancement operations

OpenShift Container Platform allows you to do more than just access and manage nodes; as an administrator, you can perform the following tasks on nodes to make the cluster more efficient, application-friendly, and to provide a better environment for your developers. 

  * Manage node-level tuning for high-performance applications that require some level of kernel tuning by [using the Node Tuning Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-node-tuning-operator "6.7. Using the Node Tuning Operator"). 
  * Enable TLS security profiles on the node to protect communication between the kubelet and the Kubernetes API server. 
  * [Run background tasks on nodes automatically with daemon sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/using-jobs-and-daemon-sets#nodes-pods-daemonsets "5.1. Running background tasks on nodes automatically with daemon sets"). You can create and use daemon sets to create shared storage, run a logging pod on every node, or deploy a monitoring agent on all nodes. 
  * [Free node resources using garbage collection](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-garbage-collection "6.11. Freeing node resources using garbage collection"). You can ensure that your nodes are running efficiently by removing terminated containers and the images not referenced by any running pods. 
  * [Add kernel arguments to a set of nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-nodes#nodes-nodes-kernel-arguments_nodes-nodes-managing "6.3.4. Add kernel arguments to nodes"). 
  * Configure an OpenShift Container Platform cluster to have worker nodes at the network edge (remote worker nodes). For information on the challenges of having remote worker nodes in an OpenShift Container Platform cluster and some recommended approaches for managing pods on a remote worker node, see [Using remote worker nodes at the network edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/remote-worker-nodes-on-the-network-edge#nodes-edge-remote-workers "9.1. Using remote worker nodes at the network edge").
