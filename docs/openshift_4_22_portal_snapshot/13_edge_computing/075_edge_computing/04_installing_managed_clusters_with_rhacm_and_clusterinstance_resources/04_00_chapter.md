# Chapter 4. Installing managed clusters with RHACM and ClusterInstance resources

You can provision OpenShift Container Platform clusters at scale with Red Hat Advanced Cluster Management (RHACM) using the assisted service and the GitOps plugin policy generator with core-reduction technology enabled. The GitOps Zero Touch Provisioning (ZTP) pipeline performs the cluster installations. GitOps ZTP can be used in a disconnected environment. 

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs. 

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation. 

**Additional resources**

  * [Configuring managed cluster policies by using PolicyGenerator resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-configuring-managed-clusters-policygenerator "10.1. Configuring managed cluster policies by using PolicyGenerator resources")
  * [Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-comparing-pgt-and-rhacm-pg-patching-strategies_ztp-configuring-managed-clusters-policygenerator "10.1.1. Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching")

- [4.1. GitOps ZTP and Topology Aware Lifecycle Manager](04_01_gitops_ztp_and_topology_aware_lifecycle_manager.md)
- [4.2. Overview of deploying managed clusters with GitOps ZTP](04_02_overview_of_deploying_managed_clusters_with_gitops_ztp.md)
- [4.3. Overview of the managed site installation process](04_03_overview_of_the_managed_site_installation_process.md)
- [4.4. Create the managed bare-metal host secrets](04_04_create_the_managed_bare_metal_host_secrets.md)
- [4.5. Configure Discovery ISO kernel arguments for installations using GitOps ZTP](04_05_configure_discovery_iso_kernel_arguments_for_installations_using_gitops_ztp.md)
- [4.6. Deploy a managed cluster with ClusterInstance and GitOps ZTP](04_06_deploy_a_managed_cluster_with_clusterinstance_and_gitops_ztp.md)
- [4.7. Managing host firmware settings with GitOps ZTP](04_07_managing_host_firmware_settings_with_gitops_ztp.md)
- [4.8. Monitor managed cluster installation progress](04_08_monitor_managed_cluster_installation_progress.md)
- [4.9. Troubleshoot GitOps ZTP by validating the installation CRs](04_09_troubleshoot_gitops_ztp_by_validating_the_installation_crs.md)
- [4.10. Troubleshooting GitOps ZTP virtual media booting on SuperMicro servers](04_10_troubleshooting_gitops_ztp_virtual_media_booting_on_supermicro_servers.md)
- [4.11. Remove a managed cluster site from the GitOps ZTP pipeline](04_11_remove_a_managed_cluster_site_from_the_gitops_ztp_pipeline.md)
- [4.12. Removing obsolete content from the GitOps ZTP pipeline](04_12_removing_obsolete_content_from_the_gitops_ztp_pipeline.md)
- [4.13. Tearing down the GitOps ZTP pipeline](04_13_tearing_down_the_gitops_ztp_pipeline.md)
