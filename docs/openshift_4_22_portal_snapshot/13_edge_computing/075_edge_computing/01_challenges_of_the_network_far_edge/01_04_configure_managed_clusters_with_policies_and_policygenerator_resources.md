# 1.4. Configure managed clusters with policies and PolicyGenerator resources

GitOps Zero Touch Provisioning (ZTP) uses Red Hat Advanced Cluster Management (RHACM) to configure clusters by using a policy-based governance approach to applying the configuration. 

The policy generator is a plugin for the GitOps Operator that enables the creation of RHACM policies from a concise template. The tool can combine multiple CRs into a single policy, and you can generate multiple policies that apply to various subsets of clusters in your fleet. 

Note

For scalability and to reduce the complexity of managing configurations across the fleet of clusters, use configuration CRs with as much commonality as possible. 

  * Where possible, apply configuration CRs using a fleet-wide common policy. 
  * The next preference is to create logical groupings of clusters to manage as much of the remaining configurations as possible under a group policy. 
  * When a configuration is unique to an individual site, use RHACM templating on the hub cluster to inject the site-specific data into a common or group policy. Alternatively, apply an individual site policy for the site. 



The following diagram shows how the policy generator interacts with GitOps and RHACM in the configuration phase of cluster deployment. 

![Policy generator](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Edge_computing-en-US/images/20ee6312e63aade50a51c024c2a6608c/217_OpenShift_Zero_Touch_Provisioning_updates_1022_3.png) ![Policy generator](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Edge_computing-en-US/images/20ee6312e63aade50a51c024c2a6608c/217_OpenShift_Zero_Touch_Provisioning_updates_1022_3.png)

For large fleets of clusters, it is typical for there to be a high-level of consistency in the configuration of those clusters. 

The following recommended structuring of policies combines configuration CRs to meet several goals: 

  * Describe common configurations once and apply to the fleet. 
  * Minimize the number of maintained and managed policies. 
  * Support flexibility in common configurations for cluster variants. 



Table 1.1. Recommended PolicyGenerator policy categoriesPolicy category| Description  
---|---  
Common  |  A policy that exists in the common category is applied to all clusters in the fleet. Use common `PolicyGenerator` CRs to apply common installation settings across all cluster types.   
Groups  |  A policy that exists in the groups category is applied to a group of clusters in the fleet. Use group `PolicyGenerator` CRs to manage specific aspects of single-node, three-node, and standard cluster installations. Cluster groups can also follow geographic region, hardware variant, etc.   
Sites  |  A policy that exists in the sites category is applied to a specific cluster site. Any cluster can have its own specific policies maintained.   
Show more

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs. 

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation. 

**Additional resources**

  * [Configuring managed cluster policies by using PolicyGenerator resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-configuring-managed-clusters-policygenerator "10.1. Configuring managed cluster policies by using PolicyGenerator resources")
  * [Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-comparing-pgt-and-rhacm-pg-patching-strategies_ztp-configuring-managed-clusters-policygenerator "10.1.1. Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching")
  * [Preparing the GitOps ZTP Git repository](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-preparing-the-hub-cluster#ztp-preparing-the-ztp-git-repository_ztp-preparing-the-hub-cluster "2.9. Prepare the GitOps ZTP site configuration repository")
