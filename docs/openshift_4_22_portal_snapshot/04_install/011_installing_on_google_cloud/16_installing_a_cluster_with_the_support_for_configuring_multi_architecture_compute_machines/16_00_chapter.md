# Chapter 16. Installing a cluster with the support for configuring multi-architecture compute machines

You can install an OpenShift Container Platform cluster on Google Cloud with multi-architecture support to run workloads on compute machines with different CPU architectures. 

Note

When you have nodes with different architectures in your cluster, the architecture of your image must be consistent with the architecture of the node. You must verify that the pod is assigned to the node with the appropriate architecture and that it matches the image architecture. For more information about assigning pods to nodes, see "Scheduling workloads on clusters with multi-architecture compute machines". 

You can install a Google Cloud cluster with the support for configuring multi-architecture compute machines. After installing the Google Cloud cluster, you can add multi-architecture compute machines to the cluster in the following ways: 

  * Adding 64-bit x86 compute machines to a cluster that uses 64-bit ARM control plane machines and already includes 64-bit ARM compute machines. In this case, 64-bit x86 is considered the secondary architecture. 
  * Adding 64-bit ARM compute machines to a cluster that uses 64-bit x86 control plane machines and already includes 64-bit x86 compute machines. In this case, 64-bit ARM is considered the secondary architecture. 



Note

Before adding a secondary architecture node to your cluster, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` custom resource. For more information, see "Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator".

- [16.1. Install a cluster with multi-architecture support](16_01_install_a_cluster_with_multi_architecture_support.md)
- [16.2. Additional resources](16_02_additional_resources.md)
