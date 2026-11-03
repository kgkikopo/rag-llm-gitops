# Chapter 13. Updating managed clusters with the Topology Aware Lifecycle Manager

You can use the Topology Aware Lifecycle Manager (TALM) to manage the software lifecycle of multiple clusters. TALM uses Red Hat Advanced Cluster Management (RHACM) policies to perform changes on the target clusters. 

Using RHACM and `PolicyGenerator` CRs is the recommended approach for managing policies and deploying them to managed clusters. This replaces the use of `PolicyGenTemplate` CRs for this purpose. For more information about `PolicyGenerator` resources, see the RHACM [Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/governance/policy-deployment#integrate-policy-generator) documentation.

- [13.1. About the Topology Aware Lifecycle Manager configuration](13_01_about_the_topology_aware_lifecycle_manager_configuration.md)
- [13.2. About managed policies used with Topology Aware Lifecycle Manager](13_02_about_managed_policies_used_with_topology_aware_lifecycle_manager.md)
- [13.3. Installing the Topology Aware Lifecycle Manager by using the web console](13_03_installing_the_topology_aware_lifecycle_manager_by_using_the_web_console.md)
- [13.4. Installing the Topology Aware Lifecycle Manager by using the CLI](13_04_installing_the_topology_aware_lifecycle_manager_by_using_the_cli.md)
- [13.5. About the ClusterGroupUpgrade CR](13_05_about_the_clustergroupupgrade_cr.md)
- [13.6. Update policies on managed clusters](13_06_update_policies_on_managed_clusters.md)
- [13.7. Using the container image pre-cache feature](13_07_using_the_container_image_pre_cache_feature.md)
- [13.8. Troubleshooting the Topology Aware Lifecycle Manager](13_08_troubleshooting_the_topology_aware_lifecycle_manager.md)
