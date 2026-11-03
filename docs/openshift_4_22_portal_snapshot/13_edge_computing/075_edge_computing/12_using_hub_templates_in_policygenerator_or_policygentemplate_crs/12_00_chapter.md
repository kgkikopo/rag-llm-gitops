# Chapter 12. Using hub templates in PolicyGenerator or PolicyGenTemplate CRs

Topology Aware Lifecycle Manager supports Red Hat Advanced Cluster Management (RHACM) hub cluster template functions in configuration policies used with GitOps Zero Touch Provisioning (ZTP). 

Hub-side cluster templates allow you to define configuration policies that can be dynamically customized to the target clusters. This reduces the need to create separate policies for many clusters with similar configurations but with different values. 

Important

Policy templates are restricted to the same namespace as the namespace where the policy is defined. This means you must create the objects referenced in the hub template in the same namespace where the policy is created. 

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs. 

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation. 

**Additional resources**

  * [Configuring managed cluster policies by using PolicyGenerator resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-configuring-managed-clusters-policygenerator "10.1. Configuring managed cluster policies by using PolicyGenerator resources")
  * [Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-comparing-pgt-and-rhacm-pg-patching-strategies_ztp-configuring-managed-clusters-policygenerator "10.1.1. Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching")
  * [RHACM support for template processing in configuration policies](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#template-processing)

- [12.1. Specifying group and site configurations in group PolicyGenerator or PolicyGentemplate CRs](12_01_specifying_group_and_site_configurations_in_group_policygenerator_or_policygentemplate_crs.md)
- [12.2. Syncing new ConfigMap changes to existing PolicyGenerator or PolicyGentemplate CRs](12_02_syncing_new_configmap_changes_to_existing_policygenerator_or_policygentemplate_crs.md)
