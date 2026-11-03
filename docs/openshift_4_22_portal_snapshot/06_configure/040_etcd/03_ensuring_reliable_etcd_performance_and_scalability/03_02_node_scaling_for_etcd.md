# 3.2. Node scaling for etcd

In general, clusters must have 3 control plane nodes. However, if your cluster is installed on a bare metal platform, it can have up to 5 control plane nodes. If your bare-metal cluster has fewer than 5 control plane nodes, you can scale up the cluster as a postinstallation task. 

For example, to scale from 3 to 4 control plane nodes after installation, you can add a host and install it as a control plane node. Then, the etcd Operator scales accordingly to account for the additional control plane node. 

Scaling a cluster to 4 or 5 control plane nodes is available only on bare metal platforms. 

For more information about how to scale control plane nodes by using the Assisted Installer, see "Adding hosts" and "Replacing a control plane node in a healthy cluster". 

Note

While adding control plane nodes can increase reliability and availability, it can decrease throughput and increase latency, affecting performance. 

The following table shows failure tolerance for clusters of different sizes: 

Table 3.1. Failure tolerances by cluster sizeCluster size| Majority| Failure tolerance  
---|---|---  
1 node  |  1  |  0   
3 nodes  |  2  |  1   
4 nodes  |  3  |  1   
5 nodes  |  3  |  2   
Show more

For more information about recovering from quorum loss, see "Restoring to an earlier cluster state". 

**Additional resources**

  * [Adding hosts](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/installing-with-api#adding-hosts_installing-with-api)
  * [Replacing a control plane node in a healthy cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/expanding-the-cluster#installing-control-plane-node-healthy-cluster_expanding-the-cluster)
  * [Expanding the cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/expanding-the-cluster)
  * [Restoring to an earlier cluster state](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#dr-restoring-cluster-state)
