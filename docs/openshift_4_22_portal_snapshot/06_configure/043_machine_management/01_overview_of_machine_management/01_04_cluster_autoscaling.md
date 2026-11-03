# 1.4. Cluster autoscaling

You can automatically scale your OpenShift Container Platform cluster to ensure flexibility for changing workloads. 

To [autoscale](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/applying-autoscaling "Chapter 7. Applying autoscaling to an OpenShift Container Platform cluster") your cluster, you must first deploy a cluster autoscaler, and then deploy a machine autoscaler for each compute machine set. 

  * The [_cluster autoscaler_](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/applying-autoscaling#cluster-autoscaler-about_applying-autoscaling "7.1. The cluster autoscaler") increases and decreases the size of the cluster based on deployment needs. 
  * The [_machine autoscaler_](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/applying-autoscaling#machine-autoscaler-about_applying-autoscaling "7.2. About the machine autoscaler") adjusts the number of machines in the compute machine sets that you deploy in your OpenShift Container Platform cluster.
