# Chapter 3. Configuring the cluster network range

To expand the cluster network range in OpenShift Container Platform to support more nodes and IP addresses, you can modify the cluster network CIDR mask after cluster installation. This procedure requires the OVN-Kubernetes network plugin and provides more IP space for additional nodes. 

For example, if you deployed a cluster and specified `10.128.0.0/19` as the cluster network range and a host prefix of `23`, you are limited to 16 nodes. You can expand that to 510 nodes by changing the CIDR mask on a cluster to `/14`. 

The following limitations apply when modifying the cluster network IP address range: 

  * The CIDR mask size specified must always be smaller than the currently configured CIDR mask size, because you can only increase IP space by adding more nodes to an installed cluster 
  * This procedure does not change the `hostPrefix` value or per-node subnet size. To increase the effective per-node pod subnet size, see "Increasing the cluster network hostPrefix". 
  * Pods that are configured with an overridden default gateway must be recreated after the cluster network expands 



Important

You cannot expand the service network CIDR range after installing the cluster, either directly or through the ServiceCIDR API. You must configure the service network CIDR during installation using the `install-config.yaml` file. To avoid service IP address exhaustion, ensure that your initial service network range is large enough to accommodate future growth.

- [3.1. Expand the cluster network IP address range](03_01_expand_the_cluster_network_ip_address_range.md)
- [3.2. Additional resources](03_02_additional_resources.md)
