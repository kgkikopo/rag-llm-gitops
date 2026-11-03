# Chapter 3. Updating GitOps ZTP

You can update the GitOps Zero Touch Provisioning (ZTP) infrastructure independently from the hub cluster, Red Hat Advanced Cluster Management (RHACM), and the managed OpenShift Container Platform clusters. 

Note

You can update the Red Hat OpenShift GitOps Operator when new versions become available. When updating the GitOps ZTP plugin, review the updated files in the reference configuration and ensure that the changes meet your requirements. 

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs. 

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation. 

**Additional resources**

  * [Configuring managed cluster policies by using PolicyGenerator resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-configuring-managed-clusters-policygenerator "10.1. Configuring managed cluster policies by using PolicyGenerator resources")
  * [Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-comparing-pgt-and-rhacm-pg-patching-strategies_ztp-configuring-managed-clusters-policygenerator "10.1.1. Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching")

- [3.1. Overview of the GitOps ZTP update process](03_01_overview_of_the_gitops_ztp_update_process.md)
- [3.2. Preparing for the upgrade](03_02_preparing_for_the_upgrade.md)
- [3.3. Labeling the existing clusters](03_03_labeling_the_existing_clusters.md)
- [3.4. Stopping the existing GitOps ZTP applications](03_04_stopping_the_existing_gitops_ztp_applications.md)
- [3.5. Required changes to the Git repository](03_05_required_changes_to_the_git_repository.md)
- [3.6. Installing the new GitOps ZTP applications](03_06_installing_the_new_gitops_ztp_applications.md)
- [3.7. Pulling ISO images for the desired OpenShift Container Platform version](03_07_pulling_iso_images_for_the_desired_openshift_container_platform_version.md)
- [3.8. Rolling out the GitOps ZTP configuration changes](03_08_rolling_out_the_gitops_ztp_configuration_changes.md)
