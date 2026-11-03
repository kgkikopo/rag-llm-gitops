# 4.7. Telco RAN DU deployment components

The following sections describe the various OpenShift Container Platform components and configurations that you use to configure the hub cluster with RHACM. 

## 4.7.1. Red Hat Advanced Cluster Management

RHACM provides Multi Cluster Engine (MCE) installation and ongoing lifecycle management functionality for deployed clusters. 

New in this release
    

  * No reference design updates in this release 



Description
    

RHACM provides Multi Cluster Engine (MCE) installation and ongoing lifecycle management functionality for deployed clusters. You manage cluster configuration and upgrades declaratively by applying `Policy` custom resources (CRs) to clusters during maintenance windows. 

RHACM provides the following functionality: 

  * Zero touch provisioning (ZTP) of clusters using the MCE component in RHACM. 
  * Configuration, upgrades, and cluster status through the RHACM policy controller. 
  * During managed cluster installation, RHACM can apply labels to individual nodes as configured through the `ClusterInstance` CR. 



The recommended method for single-node OpenShift cluster installation is the image-based installation approach, available in MCE, using the `ClusterInstance` CR for cluster definition. 

Image-based upgrade is the recommended method for single-node OpenShift cluster upgrade. 

Limits and requirements
    

  * A single hub cluster supports up to 3500 deployed single-node OpenShift clusters with 5 `Policy` CRs bound to each cluster. 



Engineering considerations
    

  * Use RHACM policy hub-side templating to better scale cluster configuration. You can significantly reduce the number of policies by using a single group policy or small number of general group policies where the group and per-cluster values are substituted into templates. 
  * Cluster specific configuration: managed clusters typically have some number of configuration values that are specific to the individual cluster. These configurations should be managed using RHACM policy hub-side templating with values pulled from `ConfigMap` CRs based on the cluster name. 
  * To save CPU resources on managed clusters, policies that apply static configurations should be unbound from managed clusters after GitOps ZTP installation of the cluster. 



**Additional resources**

  * [Using GitOps ZTP to provision clusters at the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#about-ztp_ztp-deploying-far-edge-clusters-at-scale)
  * [Red Hat Advanced Cluster Management for Kubernetes](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes)



## 4.7.2. SiteConfig Operator

The SiteConfig Operator is a template-driven solution designed to provision clusters through various installation methods. 

New in this release
    

  * No reference design updates in this release 



Description
    

The SiteConfig Operator is a template-driven solution designed to provision clusters through various installation methods. It introduces the unified `ClusterInstance` API, which replaces the deprecated `SiteConfig` API. By leveraging the `ClusterInstance` API, the SiteConfig Operator improves cluster provisioning by providing the following: 

  * Better isolation of definitions from installation methods 
  * Unification of Git and non-Git workflows 
  * Consistent APIs across installation methods 
  * Enhanced scalability 
  * Increased flexibility with custom installation templates 
  * Valuable insights for troubleshooting deployment issues 



The SiteConfig Operator provides validated default installation templates to facilitate cluster deployment through both the Assisted Installer and Image-based Installer provisioning methods: 

  * **Assisted Installer** automates the deployment of OpenShift Container Platform clusters by leveraging predefined configurations and validated host setups. It ensures that the target infrastructure meets OpenShift Container Platform requirements. The Assisted Installer streamlines the installation process while minimizing time and complexity compared to manual setup. 
  * **Image-based Installer** expedites the deployment of single-node OpenShift clusters by utilizing preconfigured and validated OpenShift Container Platform seed images. Seed images are preinstalled on target hosts, enabling rapid reconfiguration and deployment. The Image-based Installer is particularly well-suited for remote or disconnected environments because it simplifies the cluster creation process and significantly reduces deployment time. 



Limits and requirements
    

  * A single hub cluster supports up to 3500 deployed single-node OpenShift clusters. 



## 4.7.3. Topology Aware Lifecycle Manager

TALM manages how changes like cluster upgrades, Operator upgrades, and cluster configuration are rolled out to the network. 

New in this release
    

  * No reference design updates in this release 



Description
    

TALM is an Operator that runs only on the hub cluster for managing how changes like cluster upgrades, Operator upgrades, and cluster configuration are rolled out to the network. TALM supports the following features: 

  * Progressive rollout of policy updates to fleets of clusters in user configurable batches. 
  * Per-cluster actions add `ztp-done` labels or other user-configurable labels following configuration changes to managed clusters. 
  * Precaching of single-node OpenShift clusters images: TALM supports optional pre-caching of OpenShift, OLM Operator, and additional user images to single-node OpenShift clusters before initiating an upgrade. The precaching feature is not applicable when using the recommended image-based upgrade method for upgrading single-node OpenShift clusters. 

    * Specifying optional pre-caching configurations with `PreCachingConfig` CRs. Review the [sample reference `PreCachingConfig` CR](https://github.com/openshift-kni/cluster-group-upgrades-operator/blob/main/config/pre-cache/precachingconfig.yaml) for more information. 
    * Excluding unused images with configurable filtering. 
    * Enabling before and after pre-caching storage space validations with configurable space-required parameters. 




Limits and requirements
    

  * Supports concurrent cluster deployment in batches of 400 
  * Pre-caching and backup are limited to single-node OpenShift clusters only 



Engineering considerations
    

  * The `PreCachingConfig` CR is optional and does not need to be created if you only need to precache platform-related OpenShift and OLM Operator images. 
  * The `PreCachingConfig` CR must be applied before referencing it in the `ClusterGroupUpgrade` CR. 
  * Only policies with the `ran.openshift.io/ztp-deploy-wave` annotation are automatically applied by TALM during cluster installation. 
  * Any policy can be remediated by TALM under control of a user created `ClusterGroupUpgrade` CR. 



**Additional resources**

  * [Updating managed clusters with the Topology Aware Lifecycle Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-talm-for-cluster-updates)



## 4.7.4. GitOps Operator and GitOps ZTP

GitOps Operator and GitOps ZTP provide a GitOps-based infrastructure for managing cluster deployment and configuration. 

New in this release
    

  * No reference design updates in this release 



Description
    

GitOps Operator and GitOps ZTP provide a GitOps-based infrastructure for managing cluster deployment and configuration. Cluster definitions and configurations are maintained as a declarative state in Git. You can apply `ClusterInstance` CRs to the hub cluster where the `SiteConfig` Operator renders them as installation CRs. In earlier releases, a GitOps ZTP plugin supported the generation of installation CRs from `SiteConfig` CRs. This plugin is now removed. A separate GitOps ZTP plugin is available to enable automatic wrapping of configuration CRs into policies based on the `PolicyGenerator` or `PolicyGenTemplate` CR. 

You can deploy and manage multiple versions of OpenShift Container Platform on managed clusters using the baseline reference configuration CRs. You can use custom CRs alongside the baseline CRs. To maintain multiple per-version policies simultaneously, use Git to manage the versions of the source and policy CRs by using `PolicyGenerator` or `PolicyGenTemplate` CRs. RHACM `PolicyGenerator` is the recommended generator plugin starting from OpenShift Container Platform 4.19 release. 

Limits and requirements
    

  * 1000 `ClusterInstance` CRs per ArgoCD application on a hub cluster conforming to the Hub RDS. Multiple applications can be used to achieve the maximum number of clusters supported by a single hub cluster 
  * Content in the `source-crs/` directory in Git overrides content provided in the ZTP plugin container, as Git takes precedence in the search path. 
  * The `source-crs/` directory must be located in the same directory as the `kustomization.yaml` file, which includes `PolicyGenerator` CRs as a generator. Alternative locations for the `source-crs/` directory are not supported in this context. 



Engineering considerations
    

  * For multi-node cluster upgrades, you can pause `MachineConfigPool` (`MCP`) CRs during maintenance windows by setting the `paused` field to `true`. You can increase the number of simultaneously updated nodes per `MCP` CR by configuring the `maxUnavailable` setting in the `MCP` CR. The `MaxUnavailable` field defines the percentage of nodes in the pool that can be simultaneously unavailable during a `MachineConfig` update. Set `maxUnavailable` to the maximum tolerable value. This reduces the number of reboots in a cluster during upgrades which results in shorter upgrade times. When you finally unpause the `MCP` CR, all the changed configurations are applied with a single reboot. 
  * During cluster installation, you can pause custom MCP CRs by setting the paused field to true and setting `maxUnavailable` to 100% to improve installation times. 
  * Keep reference CRs and custom CRs under different directories. Doing this allows you to patch and update the reference CRs by simple replacement of all directory contents without touching the custom CRs. When managing multiple versions, the following best practices are recommended: 

    * Keep all source CRs and policy creation CRs in Git repositories to ensure consistent generation of policies for each OpenShift Container Platform version based solely on the contents in Git. 
    * Keep reference source CRs in a separate directory from custom CRs. This facilitates easy update of reference CRs as required. 

  * To avoid confusion or unintentional overwrites when updating content, it is highly recommended to use unique and distinguishable names for custom CRs in the `source-crs/` directory and extra manifests in Git. 
  * Extra installation manifests are referenced in the `ClusterInstance` CR through a `ConfigMap` CR. The `ConfigMap` CR should be stored alongside the `ClusterInstance` CR in Git, serving as the single source of truth for the cluster. If needed, you can use a `ConfigMap` generator to create the `ConfigMap` CR. 



**Additional resources**

  * [Preparing the GitOps ZTP site configuration repository for version independence](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-preparing-the-ztp-git-repository-ver-ind_ztp-preparing-the-hub-cluster)
  * [Adding custom content to the GitOps ZTP pipeline](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-adding-new-content-to-gitops-ztp_ztp-advanced-policy-config)



## 4.7.5. Agent-based installer

The optional Agent-based Installer component provides installation capabilities without centralized infrastructure. 

New in this release
    

  * No reference design updates in this release 



Description
     The optional Agent-based Installer component provides installation capabilities without centralized infrastructure. The installation program creates an ISO image that you mount to the server. When the server boots it installs OpenShift Container Platform and supplied extra manifests. The Agent-based Installer allows you to install OpenShift Container Platform without a hub cluster. A container image registry is required for cluster installation. 
Limits and requirements
    

  * You can supply a limited set of additional manifests at installation time. 
  * You must include `MachineConfiguration` CRs that are required by the RAN DU use case. 



Engineering considerations
    

  * The Agent-based Installer provides a baseline OpenShift Container Platform installation. 
  * You install Day 2 Operators and the remainder of the RAN DU use case configurations after installation. 



**Additional resources**

  * [Installing a cluster with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#installing-with-agent-based-installer)
