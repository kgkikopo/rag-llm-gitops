# Chapter 10. Multiple regions and zones configuration for a cluster on VMware vSphere

As an administrator, you can specify multiple regions and zones for your OpenShift Container Platform cluster that runs on a VMware vSphere instance. This configuration reduces the risk of a hardware failure or network outage causing your cluster to fail. 

A failure domain configuration lists parameters that create a topology. The following list states some of these parameters: 

  * `computeCluster`
  * `datacenter`
  * `datastore`
  * `networks`
  * `resourcePool`



After you define multiple regions and zones for your OpenShift Container Platform cluster, you can create or migrate nodes to another failure domain. 

Important

If you want to migrate pre-existing OpenShift Container Platform cluster compute nodes to a failure domain, you must define a new compute machine set for the compute node. This new machine set can scale up a compute node according to the topology of the failure domain, and scale down the pre-existing compute node. 

The cloud provider adds `topology.kubernetes.io/zone` and `topology.kubernetes.io/region` labels to any compute node provisioned by a machine set resource.

- [10.1. Specifying multiple regions and zones for your cluster on vSphere](10_01_specifying_multiple_regions_and_zones_for_your_cluster_on_vsphere.md)
- [10.2. Enabling a multiple layer 2 network for your cluster](10_02_enabling_a_multiple_layer_2_network_for_your_cluster.md)
- [10.3. Parameters for the cluster-wide infrastructure CRD](10_03_parameters_for_the_cluster_wide_infrastructure_crd.md)
- [10.4. Specifying multiple host groups for your cluster on vSphere](10_04_specifying_multiple_host_groups_for_your_cluster_on_vsphere.md)
