# 13.1. About the Topology Aware Lifecycle Manager configuration

The Topology Aware Lifecycle Manager (TALM) manages the deployment of Red Hat Advanced Cluster Management (RHACM) policies for one or more OpenShift Container Platform clusters. Using TALM in a large network of clusters allows the phased rollout of policies to the clusters in limited batches. 

This helps to minimize possible service disruptions when updating. With TALM, you can control the following actions: 

  * The timing of the update 
  * The number of RHACM-managed clusters 
  * The subset of managed clusters to apply the policies to 
  * The update order of the clusters 
  * The set of policies remediated to the cluster 
  * The order of policies remediated to the cluster 
  * The assignment of a canary cluster 



For single-node OpenShift, the Topology Aware Lifecycle Manager (TALM) offers pre-caching images for clusters with limited bandwidth. 

TALM supports the orchestration of the OpenShift Container Platform y-stream and z-stream updates, and day-two operations on y-streams and z-streams.
