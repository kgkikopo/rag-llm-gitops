# 5.15. Managed cluster lifecycle management

To provision and manage sites at the far edge of the network, use GitOps ZTP in a hub-and-spoke architecture, where a single hub cluster manages many managed clusters. 

Lifecycle management for spoke clusters can be divided into two different stages: cluster deployment, including OpenShift Container Platform installation, and cluster configuration. 

**Additional resources**

  * [Challenges of the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-deploying-far-edge-clusters-at-scale)



## 5.15.1. Managed cluster deployment

As of Red Hat Advanced Cluster Management (RHACM) 2.12, the SiteConfig Operator is the recommended method for deploying managed OpenShift Container Platform clusters. 

It introduces a unified `ClusterInstance` API that decouples cluster parameters from the deployment method and uses a GitOps workflow to generate installation manifests. 

Description
     As of Red Hat Advanced Cluster Management (RHACM) 2.12, using the SiteConfig Operator is the recommended method for deploying managed clusters. The SiteConfig Operator introduces a unified ClusterInstance API that decouples the parameters that define the cluster from the manner in which it is deployed. The SiteConfig Operator uses a set of cluster templates that are instantiated using the data from a `ClusterInstance` custom resource (CR) to dynamically generate installation manifests. Following the GitOps methodology, the `ClusterInstance` CR is sourced from a Git repository through ArgoCD. The `ClusterInstance` CR can be used to initiate cluster installation by using either Assisted Installer, or the image-based installation available in multicluster engine. 
Limits and requirements
    

  * The `SiteConfig` ArgoCD plugin which handles `SiteConfig` CRs is removed from OpenShift Container Platform 4.21. From this release, use `ClusterInstance` CRs to define managed cluster deployments. 
  * An HTTP server hosting the root filesystem and RHCOS live ISO images is required for cluster deployment. These images are release specific. ISO images for each OpenShift Container Platform release to be deployed must be reachable by the hub cluster and each deployed spoke cluster. Only include ISO images which exist on the HTTP server in the `AgentServiceConfig` CR. 
  * A container registry hosting all OpenShift Container Platform and day-2 OLM operator images must be reachable from all deployed spoke clusters. The hub configuration includes Kustomize overlays which you can use to provide the TLS certificates and credentials for a disconnected container registry. 



Engineering considerations
    

  * You must create a `Secret` CR with the login information for the cluster baseboard management controller (BMC). This `Secret` CR is then referenced in the `SiteConfig` CR. Integration with a secret store, such as Vault, can be used to manage the secrets. 
  * Besides offering deployment method isolation and unification of Git and non-Git workflows, the SiteConfig Operator provides better scalability, greater flexibility with the use of custom templates, and an enhanced troubleshooting experience. 



**Additional resources**

  * [SiteConfig](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/siteconfig-intro#siteconfig-intro)
  * [ClusterInstance](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/apis/apis#rhacm-docs_apis_clusterinstance_jsonclusterinstance)
  * [Creating the managed bare-metal host secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-creating-the-site-secrets_ztp-deploying-far-edge-sites)



## 5.15.2. Managed cluster updates

You can upgrade OpenShift Container Platform versions, Day 2 Operators, and managed cluster configurations by declaring the required versions in Policy custom resources (CRs). 

The Topology Aware Lifecycle Manager (TALM) manages progressive rollout of these changes across fleets of clusters. 

Description
    

You can upgrade versions of OpenShift Container Platform, Day 2 Operators, and managed cluster configurations, by declaring the required version in the `Policy` custom resources (CRs) that target the clusters to be upgraded. 

Policy controllers periodically check for policy compliance. If the result is negative, a violation report is created. If the policy remediation action is set to `enforce` the violations are remediated according to the updated policy. If the policy remediation action is set to `inform`, the process ends with a non-compliant status report and responsibility to initiate the upgrade is left to the user to perform during an appropriate maintenance window. 

The Topology Aware Lifecycle Manager (TALM) extends Red Hat Advanced Cluster Management (RHACM) with features to manage the rollout of upgrades or configuration throughout the lifecycle of the fleet of clusters. It operates in progressive, limited size batches of clusters. When upgrades to OpenShift Container Platform or the Day 2 Operators are required, TALM progressively rolls out the updates by stepping through the set of policies and switching them to an "enforce" policy to push the configuration to the managed cluster. 

The custom resource (CR) that TALM uses to build the remediation plan is the `ClusterGroupUpgrade` CR. 

You can use image-based upgrade (IBU) with the Lifecycle Agent as an alternative upgrade path for the single-node OpenShift cluster platform version. IBU uses an OCI image generated from a dedicated seed cluster to install single-node OpenShift on the target cluster. 

TALM uses the `ImageBasedGroupUpgrade` CR to roll out image-based upgrades to a set of identified clusters. 

Limits and requirements
    

  * You can perform direct upgrades for single-node OpenShift clusters using image-based upgrade for OpenShift Container Platform `<4.y>` to `<4.y+2>`, and `<4.y.z>` to `<4.y.z+n>`. 
  * Image-based upgrade uses custom images that are specific to the hardware platform that the clusters are running on. Different hardware platforms require separate seed images. 



Engineering considerations
    

  * In edge deployments, you can minimize the disruption to managed clusters by managing the timing and rollout of changes. Set all policies to `inform` to monitor compliance without triggering automatic enforcement. Similarly, configure Day 2 Operator subscriptions to manual to prevent updates from occurring outside of scheduled maintenance windows. 
  * The recommended upgrade aproach for single-node OpenShift clusters is the image-based upgrade. 
  * For multi-node cluster upgrades, consider the following `MachineConfigPool` CR configurations to reduce upgrade times: 

    * Pause configuration deployments to nodes during a maintenance window by setting the `paused` field to `true`. 
    * Adjust the `maxUnavailable` field to control how many nodes in the pool can be updated simultaneously. The `MaxUnavailable` field defines the percentage of nodes in the pool that can be simultaneously unavailable during a `MachineConfig` object update. Set `maxUnavailable` to the maximum tolerable value. This reduces the number of reboots in a cluster during upgrades which results in shorter upgrade times. 
    * Resume configuration deployments by setting the `paused` field to `false`. The configuration changes are applied in a single reboot. 

  * During cluster installation, you can pause `MachineConfigPool` CRs by setting the `paused` field to `true` and setting `maxUnavailable` to 100% to improve installation times. 



**Additional resources**

  * [Configuration policy YAML structure](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/governance/governance#configuration-policy-yaml)
  * [About the ClusterGroupUpgrade CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#talo-about-cgu-crs_cnf-topology-aware-lifecycle-manager)
  * [Understanding the image-based upgrade for single-node OpenShift clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-understanding-image-based-upgrade)
  * [Performing an image-based upgrade for single-node OpenShift clusters using GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-image-based-upgrade)



## 5.15.3. Hub cluster disaster recovery

Note that loss of the hub cluster does not typically create a service outage on the managed clusters. Functions provided by the hub cluster will be lost, such as observability, configuration, lifecycle management updates being driven through the hub cluster, and so on. 

Limits and requirements
    

  * Backup,restore and disaster recovery are offered by the cluster backup and restore Operator, which depends on the OpenShift API for Data Protection (OADP) Operator. 



Engineering considerations
    

  * You can extend the cluster backup and restore operator to third party resources of the hub cluster based on your configuration. 
  * The cluster backup and restore operator is not enabled by default in Red Hat Advanced Cluster Management (RHACM). The reference configuration enables this feature. 



**Additional resources**

  * [Business continuity](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/business_continuity/index)
