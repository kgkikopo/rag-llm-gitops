# 13.2. About managed policies used with Topology Aware Lifecycle Manager

The Topology Aware Lifecycle Manager (TALM) uses RHACM policies for cluster updates. 

TALM can be used to manage the rollout of any policy CR where the `remediationAction` field is set to `inform`. Supported use cases include the following: 

  * Manual user creation of policy CRs 
  * Automatically generated policies from the `PolicyGenerator` or `PolicyGentemplate` custom resource definition (CRD) 



Note

Using the `PolicyGentemplate` CRD is the recommended method for automatic policy generation. 

For policies that update an Operator subscription with manual approval, TALM provides additional functionality that approves the installation of the updated Operator. 

For more information about managed policies, "Policy Overview" in the RHACM documentation. 

**Additional resources**

  * [Policy Overview](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#policy-overview)



**Additional resources**

  * [About the PolicyGenerator CRD](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-the-policygentemplate_ztp-configuring-managed-clusters-policygenerator "10.1.2. About the PolicyGenerator CRD")
