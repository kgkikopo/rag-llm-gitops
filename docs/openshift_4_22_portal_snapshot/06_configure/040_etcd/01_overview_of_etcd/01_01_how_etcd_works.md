# 1.1. How etcd works

The etcd Operator deploys and manages the etcd cluster for the OpenShift Container Platform control plane by observing state, analyzing differences, and correcting drift. 

To ensure a reliable approach to cluster configuration and management, etcd uses the etcd Operator. The Operator simplifies the use of etcd on a Kubernetes container platform such as OpenShift Container Platform. 

Additionally, you can use the etcd Operator to deploy and manage the etcd cluster for the OpenShift Container Platform control plane. The etcd Operator manages the cluster state in the following ways: 

  * Observes the cluster state by using the Kubernetes API 
  * Analyzes differences between the current state and the required state 
  * Corrects the differences through the etcd cluster management APIs, the Kubernetes API, or both 



Note

etcd holds the cluster state, which is constantly updated. This state is continuously persisted, which leads to a high number of small changes at high frequency. As a result, it is critical to back up the etcd cluster member with fast, low-latency I/O. For more information about best practices for etcd, see "Recommended etcd practices". 

**Additional resources**

  * [Recommended etcd practices](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-practices "Chapter 2. Recommended etcd practices")
