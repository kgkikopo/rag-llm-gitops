# 3.9. Telco core deployment components

The following sections describe the various OpenShift Container Platform components and configurations that you use to configure the hub cluster with Red Hat Advanced Cluster Management (RHACM). 

## 3.9.1. Red Hat Advanced Cluster Management

RHACM provides Multi Cluster Engine (MCE) installation and ongoing lifecycle management for deployed clusters. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

RHACM provides Multi Cluster Engine (MCE) installation and ongoing GitOps ZTP lifecycle management for deployed clusters. You manage cluster configuration and upgrades declaratively by applying `Policy` custom resources (CRs) to clusters during maintenance windows. 

You apply policies with the RHACM policy controller as managed by TALM. Configuration, upgrades, and cluster status are managed through the policy controller. 

When installing managed clusters, RHACM applies labels and initial ignition configuration to individual nodes in support of custom disk partitioning, allocation of roles, and allocation to machine config pools. You define these configurations with `SiteConfig` or `ClusterInstance` CRs. 

Limits and requirements
    

  * Hub cluster sizing is discussed in [Sizing your cluster](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/install/index#sizing-your-cluster). 
  * RHACM scaling limits are described in [Performance and Scalability](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/install/index#performance-and-scalability). 



Engineering considerations
    

  * When managing multiple clusters with unique content per installation, site, or deployment, using RHACM hub templating is strongly recommended. With RHACM hub templating, you can apply a consistent set of policies to clusters while providing unique values per installation. 



**Additional resources**

  * [Using GitOps ZTP to provision clusters at the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#about-ztp_ztp-deploying-far-edge-clusters-at-scale)
  * [Red Hat Advanced Cluster Management for Kubernetes](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes)



## 3.9.2. Topology Aware Lifecycle Manager

TALM manages how changes are rolled out to managed clusters in the network. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

TALM is an Operator that runs only on the hub cluster. TALM manages how changes including cluster and Operator upgrades, configurations, and so on, are rolled out to managed clusters in the network. TALM has the following core features: 

  * Provides sequenced updates of cluster configurations and upgrades (OpenShift Container Platform and Operators) as defined by cluster policies. 
  * Provides for deferred application of cluster updates. 
  * Supports progressive rollout of policy updates to sets of clusters in user configurable batches. 
  * Allows for per-cluster actions by adding `ztp-done` or similar user-defined labels to clusters. 



Limits and requirements
    

  * Supports concurrent cluster deployments in batches of 400 



Engineering considerations
    

  * Only policies with the `ran.openshift.io/ztp-deploy-wave` annotation are applied by TALM during initial cluster installation. 
  * Any policy can be remediated by TALM under control of a user created `ClusterGroupUpgrade` CR. 
  * Set the `MachineConfigPool` (`mcp`) CR `paused` field to true during a cluster upgrade maintenance window and set the `maxUnavailable` field to the maximum tolerable value. This prevents multiple cluster node reboots during upgrade, which results in a shorter overall upgrade. When you unpause the `mcp` CR, all the configuration changes are applied with a single reboot. 

Note

During installation, custom `mcp` CRs can be paused along with setting `maxUnavailable` to 100% to improve installation times. 

  * You can orchestrate upgrades for OpenShift Container Platform, Day 2 OLM operators, and custom configurations using a ClusterGroupUpgrade (CGU) CR that defines the required policies. 

    * An EUS to EUS upgrade can be orchestrated using chained CGU CRs. 
    * Control of MCP pause can be managed through policy in the CGU CRs for a full control plane and worker node rollout of upgrades. 
    * For more information, see "Performing an EUS-to-EUS update for telco core clusters". 




**Additional resources**

  * [Updating managed clusters with the Topology Aware Lifecycle Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-talm-for-cluster-updates)



## 3.9.3. GitOps Operator and GitOps ZTP plugins

The GitOps Operator provides a GitOps-driven infrastructure for managing cluster deployment and configuration. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

The GitOps Operator provides a GitOps driven infrastructure for managing cluster deployment and configuration. Cluster definitions and configuration are maintained in a Git repository. 

The SiteConfig Operator generates installation CRs from `ClusterInstance` CRs. 

Important

From OpenShift Container Platform 4.21, you must use `ClusterInstance` CRs and the SiteConfig Operator to define managed cluster installations. With this release, support for defining managed cluster installations with the `SiteConfig` CR is removed. 

GitOps ZTP plugins provide support for automatically wrapping configuration CRs in policies based on RHACM `PolicyGenerator` CRs. 

You should structure the Git repository according to the release version, with all necessary artifacts added to the repository, such as the `ClusterInstance`, `PolicyGenerator`, and supporting reference CRs. This structure enables deploying and managing multiple versions of the OpenShift Container Platform and configuration versions to clusters simultaneously and through upgrades. 

The recommended Git structure keeps reference CRs in a directory separate from customer or partner provided content. This means that you can import reference updates by simply overwriting existing content. Customer or partner supplied CRs can be provided in a parallel directory to the reference CRs for easy inclusion in the generated configuration policies. 

Limits and requirements
    

  * Each ArgoCD application supports up to 1000 nodes on a hub cluster conforming to the Hub RDS. Multiple ArgoCD applications can be used to achieve the maximum number of clusters supported by a single hub cluster. 
  * Use the `extraManifestsRefs` field in the `ClusterInstance` CR to reference `ConfigMap` resources that contain additional manifests to apply at install time. 



Engineering considerations
    

  * To avoid confusion or unintentional overwriting when updating content, you should use unique and distinguishable names for custom CRs in the `reference-crs/` directory under core-overlay and extra manifests in git. 
  * The `ClusterInstance` CR allows multiple `ConfigMap` references in the `extraManifestsRefs` field for additional install-time manifests. 



**Additional resources**

  * [Preparing the GitOps ZTP site configuration repository for version independence](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-preparing-the-ztp-git-repository-ver-ind_ztp-preparing-the-hub-cluster)
  * [Adding custom content to the GitOps ZTP pipeline](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-adding-new-content-to-gitops-ztp_ztp-advanced-policy-config)



## 3.9.4. Agent-based Installer

The Agent-based Installer provides an installation method for OpenShift Container Platform in environments without existing deployment infrastructure. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

The recommended method for Telco Core cluster installation is using Red Hat Advanced Cluster Management. The Agent Based Installer (ABI) is a separate installation flow for Openshift in environments without existing infrastructure for running cluster deployments. Use the ABI to install OpenShift Container Platform on bare-metal servers without requiring additional servers or VMs for managing the installation, but does not provide ongoing lifecycle management, monitoring or automations. The ABI can be run on any system for example, from a laptop to generate an ISO installation image. The ISO is used as the installation media for the cluster control plane nodes. You can monitor the progress by using the ABI from any system with network connectivity to the control plane node’s API interfaces. 

ABI supports the following: 

  * Installation from declarative CRs 
  * Installation in disconnected environments 
  * No additional servers required to support installation, for example, the bastion node is no longer needed 



Limits and requirements
    

  * Disconnected installation requires a registry with all required content mirrored and reachable from the installed host. 



Engineering considerations
    

  * Networking configuration should be applied as NMState configuration during installation as opposed to Day 2 configuration using the NMState Operator. 



**Additional resources**

  * [Installing an OpenShift Container Platform cluster with the Agent-based Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#installing-with-agent-based-installer)
