# 4.5. CIDR ranges for hosted control planes

To successfully deploy hosted control planes on OpenShift Container Platform, define the network environment by using specific Classless Inter-Domain Routing (CIDR) subnet ranges. 

The following Classless Inter-Domain Routing (CIDR) subnet ranges are the default settings for hosted control planes: 

  * `v4InternalSubnet`: 100.65.0.0/16 (OVN-Kubernetes) 
  * `clusterNetwork`: 10.132.0.0/14 (pod network) 
  * `serviceNetwork`: 172.31.0.0/16 



By using one of the default subnet ranges, you can avoid CIDR overlap with the management cluster and avoid connectivity issues. However, you can use other CIDR subnet ranges if they do not overlap with the management cluster.
