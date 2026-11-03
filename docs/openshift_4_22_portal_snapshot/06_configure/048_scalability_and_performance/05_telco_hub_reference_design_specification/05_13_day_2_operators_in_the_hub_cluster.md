# 5.13. Day 2 Operators in the hub cluster

The management hub cluster relies on a set of Day 2 Operators to provide critical management services and infrastructure. Use Operator versions that match the set of managed cluster versions in your fleet. 

Install Day 2 Operators using Operator Lifecycle Manager (OLM) and `Subscription` custom resources (CRs). `Subscription` CRs identify the specific Day 2 Operator to install, the catalog in which the Operator is found, and the appropriate version channel for the Operator. By default OLM installs and attempt to keep Operators updated with the latest z-stream version available in the channel. By default all Subscriptions are set with an `installPlanApproval: Automatic` value. In this mode, OLM automatically installs new Operator versions when they are available in the catalog and channel. 

Note

Setting `installPlanApproval` to automatic exposes the risk of the Operator being updated outside of defined maintenance windows if the catalog index is updated to include newer Operator versions. In a disconnected environment where you are building and maintaining a curated set of Operators and versions in the catalog, and if you follow a strategy of creating a new catalog index for updated versions, the risk of the Operators being inadvertently updated is largely removed. However, if you want to further close this risk, the `Subscription` CRs can be set to `installPlanApproval: Manual` which prevents Operators from being updated without explicit administrator approval. 

Limits and requirements
    

  * When upgrading a telco hub cluster, the versions of OpenShift Container Platform and Operators must meet the requirements of all relevant compatibility matrixes. 



**Additional resources**

  * [Red Hat Advanced Cluster Management for Kubernetes 2.11 Support Matrix](https://access.redhat.com/articles/7073065)
  * [OpenShift Operator lifecycles](https://access.redhat.com/support/policy/updates/openshift_operators)
  * For more information about telco hub cluster update requirements, see: 

    * [Recommended hub cluster specifications and managed cluster limits for GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-gitops-ztp-max-spoke-clusters_ztp-preparing-the-hub-cluster). 
    * [Red Hat Advanced Cluster Management for Kubernetes 2.11 Support Matrix](https://access.redhat.com/articles/7073065)
    * [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators)

  * For more information about updating the hub cluster, see: 

    * [Introduction to OpenShift updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#understanding-openshift-updates)
    * [Upgrading your hub cluster](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/install/index#upgrading-hub)
    * [Updating GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-updating-gitops)
