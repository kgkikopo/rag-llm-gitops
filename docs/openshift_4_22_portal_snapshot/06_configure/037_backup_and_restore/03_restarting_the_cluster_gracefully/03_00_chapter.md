# Chapter 3. Restarting the cluster gracefully

You can restart your OpenShift Container Platform cluster after a graceful shutdown by powering on nodes and verifying cluster health. The cluster returns to normal operations when nodes and Operators are healthy. 

Even though the cluster is expected to be functional after the restart, the cluster might not recover due to unexpected conditions: 

  * etcd data corruption during shutdown 
  * Node failure due to hardware 
  * Network connectivity issues 



If your cluster fails to recover, follow the steps in "Restoring to an earlier cluster state".

- [3.1. Restarting the cluster](03_01_restarting_the_cluster.md)
