# Chapter 22. Improving cluster stability in high latency environments using worker latency profiles

To improve cluster stability in high latency environments, apply worker latency profiles. 

If as a cluster administrator, you performed latency tests for platform verification, you might discover the need to adjust the operation of the cluster to ensure stability in cases of high latency. 

As a cluster administrator, you need to change only one parameter, recorded in a file, which controls four parameters affecting how supervisory processes read status and interpret the health of the cluster. Changing only the one parameter provides cluster tuning in an easy, supportable manner. 

The `Kubelet` process provides the starting point for monitoring cluster health. The `Kubelet` sets status values for all nodes in the OpenShift Container Platform cluster. The Kubernetes Controller Manager (`kube controller`) reads the status values every 10 seconds, by default. If the `kube controller` cannot read a node status value, it loses contact with that node after a configured period. The default behavior is: 

  1. The node controller on the control plane updates the node health to `Unhealthy` and marks the node `Ready` condition `Unknown`. 
  2. In response, the scheduler stops scheduling pods to that node. 
  3. The Node Lifecycle Controller adds a `node.kubernetes.io/unreachable` taint with a `NoExecute` effect to the node and schedules any pods on the node for eviction after five minutes, by default. 



This behavior can cause problems if your network is prone to latency issues, especially if you have nodes at the network edge. In some cases, the Kubernetes Controller Manager might not receive an update from a healthy node due to network latency. The `Kubelet` evicts pods from the node even though the node is healthy. 

To avoid this problem, you can use _worker latency profiles_ to adjust the frequency that the `Kubelet` and the Kubernetes Controller Manager wait for status updates before taking action. These adjustments help to ensure that your cluster runs properly if network latency between the control plane and the worker nodes is not optimal. 

These worker latency profiles contain three sets of parameters that are predefined with carefully tuned values to control the reaction of the cluster to increased latency. There is no need to experimentally find the best values manually. 

You can configure worker latency profiles when installing a cluster or at any time you notice increased latency in your cluster network.

- [22.1. Understanding worker latency profiles](22_01_understanding_worker_latency_profiles.md)
- [22.2. Implement worker latency profiles at cluster creation](22_02_implement_worker_latency_profiles_at_cluster_creation.md)
- [22.3. Use and change worker latency profiles](22_03_use_and_change_worker_latency_profiles.md)
- [22.4. Display resulting values of worker latency profile](22_04_display_resulting_values_of_worker_latency_profile.md)
