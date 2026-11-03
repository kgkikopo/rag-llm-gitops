# 4.3. Pod classless inter-domain routing (CIDR)

In the pod CIDR field, you must specify the IP address range for pods. 

The pod CIDR is the same as the `clusterNetwork` CIDR and the cluster CIDR. The range must be large enough to accommodate your workload. The address block must not overlap with any external service accessed from within the cluster. The default is `10.128.0.0/14`. You can expand the range after cluster installation. 

**Additional resources**

  * [Cluster Network Operator configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-operator-cr_cluster-network-operator)
  * [Configuring the cluster network range](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/configuring_network_settings/#configuring-cluster-network-range)
  * [Increasing the cluster network hostPrefix](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#increasing-cluster-network-hostprefix)
