# 3.8. Rolling out the GitOps ZTP configuration changes

If any configuration changes were included in the upgrade due to implementing recommended changes, the upgrade process results in a set of policy CRs on the hub cluster in the `Non-Compliant` state. 

With the GitOps Zero Touch Provisioning (ZTP) version 4.10 and later `ztp-site-generate` container, these policies are set to `inform` mode and are not pushed to the managed clusters without an additional step by the user. This ensures that potentially disruptive changes to the clusters can be managed in terms of when the changes are made, for example, during a maintenance window, and how many clusters are updated concurrently. 

To roll out the changes, create one or more `ClusterGroupUpgrade` CRs as detailed in the TALM documentation. The CR must contain the list of `Non-Compliant` policies that you want to push out to the managed clusters as well as a list or selector of which clusters should be included in the update. 

**Additional resources**

  * [About the Topology Aware Lifecycle Manager configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-talm-for-cluster-updates#cnf-about-topology-aware-lifecycle-manager-config_cnf-topology-aware-lifecycle-manager "13.1. About the Topology Aware Lifecycle Manager configuration")
  * [About the auto-created ClusterGroupUpgrade CR for GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygentemplate-resources#talo-precache-autocreated-cgu-for-ztp_ztp-talm "11.3.8. About the auto-created ClusterGroupUpgrade CR for GitOps ZTP")
