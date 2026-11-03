# 5.16. Hub cluster components

The following sections highly hub cluster components. 

## 5.16.1. Red Hat Advanced Cluster Management (RHACM)

Red Hat Advanced Cluster Management (RHACM) provides multicluster engine installation and ongoing lifecycle management for OpenShift Container Platform clusters. 

You can manage cluster configuration and upgrades declaratively by applying Policy custom resources (CRs) during maintenance windows. 

New in this release
    

  * No reference design updates in this release. 



Description
    

Red Hat Advanced Cluster Management (RHACM) provides multicluster engine installation and ongoing lifecycle management functionality for deployed clusters. You can manage cluster configuration and upgrades declaratively by applying `Policy` custom resources (CRs) to clusters during maintenance windows. 

RHACM provides functionality such as the following: 

  * Zero touch provisioning (ZTP) and ongoing scaling of clusters using the multicluster engine component in RHACM. 
  * Configuration, upgrades, and cluster status through the RHACM policy controller. 
  * During managed cluster installation, RHACM can apply labels to individual nodes as configured through the `ClusterInstance` CR. 
  * The Topology Aware Lifecycle Manager component of RHACM provides phased rollout of configuration changes to managed clusters. 
  * The RHACM multicluster engine Observability component provides selective monitoring, dashboards, alerts, and metrics. The recommended method for single-node OpenShift cluster installation is the image-based installation method in multicluster engine, which uses the `ClusterInstance` CR for cluster definition. 



The recommended method for single-node OpenShift upgrade is the image-based upgrade method. 

Note

The RHACM multicluster engine Observability component brings you a centralized view of the health and status of all the managed clusters. By default, every managed cluster is enabled to send metrics and alerts, created by their Cluster Monitoring Operator (CMO), back to Observability. For more information, see "Observability". 

Limits and requirements
    

  * For more information about limits on number of clusters managed by a single hub cluster, see "Telco management hub cluster use model". 
  * The number of managed clusters that can be effectively managed by the hub depends on various factors, including: 

    * Resource availability at each managed cluster 
    * Policy complexity and cluster size 
    * Network utilization 
    * Workload demands and distribution 

  * The hub and managed clusters must maintain sufficient bidirectional connectivity. Refer to the RHACM Hub Network Configuration for further details. 



Engineering considerations
    

  * You can configure the cluster backup and restore Operator to include third-party resources. 
  * The use of RHACM hub side templating when defining configuration through policy is strongly recommended. This feature reduces the number of policies needed to manage the fleet by enabling for each cluster or for each group. For example, regional or hardware type content to be templated in a policy and substituted on cluster or group basis. 
  * Managed clusters typically have some number of configuration values which are specific to an individual cluster. These should be managed using RHACM policy hub side templating with values pulled from `ConfigMap` CRs based on the cluster name. 



**Additional resources**

  * * [Hub Network Configuration](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/networking/networking#hub-network-config)
  * [Multi Cluster Engine](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/clusters/index#cluster_mce_overview)
  * [Governance](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/governance/index)
  * [Topology Aware Lifecycle Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-talm-for-cluster-updates)
  * [MultiClusterHub Observability](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/observability/index)
  * [Business continuity](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/business_continuity/index#business-cont-overview)
  * [Performance and scalability](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/install/installing#performance-and-scalability)
  * [Network configuration](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/clusters/index#mce-network-configuration)



## 5.16.2. Topology Aware Lifecycle Manager

Topology Aware Lifecycle Manager is an Operator that runs on the OpenShift Container Platform hub cluster to manage the progressive rollout of cluster upgrades, Operator upgrades, and configuration changes to managed cluster fleets. 

It supports configurable batch sizes, per-cluster labeling, and optional pre-caching of images before upgrades. 

New in this release
    

  * No reference design updates in this release. 



Description
    

TALM is an Operator that runs only on the hub cluster for managing how changes like cluster upgrades, Operator upgrades, and cluster configuration are rolled out to the network. TALM supports the following features: 

  * Progressive rollout of policy updates to fleets of clusters in user configurable batches. 
  * Per-cluster actions add `ztp-done` labels or other user-configurable labels following configuration changes to managed clusters. 
  * TALM supports optional pre-caching of OpenShift Container Platform, OLM Operator, and additional images to single-node OpenShift clusters before initiating an upgrade. The pre-caching feature is not applicable when using the recommended image-based upgrade method for upgrading single-node OpenShift clusters. 

    * Specifying optional pre-caching configurations with `PreCachingConfig` CRs. 
    * Configurable image filtering to exclude unused content. 
    * Storage validation before and after pre-caching, using defined space requirement parameters. 




Limits and requirements
    

  * TALM supports concurrent cluster upgrades in batches of 500. 
  * Pre-caching is limited to single-node OpenShift cluster topology. 



Engineering considerations
    

  * The `PreCachingConfig` custom resource (CR) is optional. You do not need to create it if you want to pre-cache platform-related images only, such as OpenShift Container Platform and OLM. 
  * TALM supports the use of hub-side templating with Red Hat Advanced Cluster Management policies. 



## 5.16.3. GitOps Operator and GitOps ZTP

GitOps Operator and GitOps ZTP provide a GitOps-based infrastructure for managing cluster deployment and configuration in OpenShift Container Platform. 

You can maintain cluster definitions as a declarative state in Git and apply `ClusterInstance` custom resources (CRs) to the hub cluster for rendering as installation CRs. 

New in this release
    

  * No reference design updates in this release 



Description
    

GitOps Operator and GitOps ZTP provide a GitOps-based infrastructure for managing cluster deployment and configuration. Cluster definitions and configurations are maintained as a declarative state in Git. You can apply `ClusterInstance` custom resources (CRs) to the hub cluster where the `SiteConfig` Operator renders them as installation CRs. In earlier releases, a GitOps ZTP plugin supported the generation of installation CRs from `SiteConfig` CRs. This plugin is now deprecated. A separate GitOps ZTP plugin is available to enable automatic wrapping of configuration CRs into policies based on the `PolicyGenerator` or the `PolicyGenTemplate` CRs. 

You can deploy and manage multiple versions of OpenShift Container Platform on managed clusters by using the baseline reference configuration CRs. You can use custom CRs alongside the baseline CRs. To maintain multiple per-version policies simultaneously, use Git to manage the versions of the source and policy CRs by using the `PolicyGenerator` or the `PolicyGenTemplate` CRs. 

Limits and requirements
    

  * To ensure consistent and complete cleanup of managed clusters and their associated resources during cluster or node deletion, you must configure ArgoCD to use background deletion mode. 



Engineering considerations
    

  * To avoid confusion or unintentional overwrite when updating content, use unique and distinguishable names for custom CRs in the `source-crs` directory and extra manifests. 
  * Keep reference source CRs in a separate directory from custom CRs. This facilitates easy update of reference CRs as required. 
  * To help with multiple versions, keep all source CRs and policy creation CRs in versioned Git repositories to ensure consistent generation of policies for each OpenShift Container Platform version. 



**Additional resources**

  * [ClusterInstance CR](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/siteconfig-intro)
  * [PolicyGenTemplate CRs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-configuring-managed-clusters-policies)
  * [GitOps ZTP version independence](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-preparing-the-ztp-git-repository-ver-ind_ztp-preparing-the-hub-cluster)



## 5.16.4. Local Storage Operator

The Local Storage Operator creates persistent volumes (PVs) that applications in OpenShift Container Platform can consume as PersistentVolumeClaim (PVC) resources. The number and type of PVs you create depends on your storage requirements. 

New in this release
    

  * No reference design updates in this release 



Description
     You can create persistent volumes that can be used as `PVC` resources by applications with the Local Storage Operator. The number and type of `PV` resources that you create depends on your requirements. 
Engineering considerations
    

  * Create backing storage for `PV` CRs before creating the persistent volume. This can be a partition, a local volume, LVM volume, or full disk. 
  * Refer to the device listing in `LocalVolume` CRs by the hardware path used to access each device to ensure correct allocation of disks and partitions, for example, `/dev/disk/by-path/<id>`. Logical names (for example, `/dev/sda`) are not guaranteed to be consistent across node reboots. 



## 5.16.5. Red Hat OpenShift Data Foundation

Red Hat OpenShift Data Foundation provides file, block, and object storage services to the OpenShift Container Platform hub cluster. It is the recommended storage solution for telco hub cluster deployments. 

New in this release
    

  * No reference design updates in this release 



Description
     Red Hat OpenShift Data Foundation provides file, block, and object storage services to the hub cluster. 
Limits and requirements
    

  * Red Hat OpenShift Data Foundation (ODF) in internal mode requires the Local Storage Operator to define a storage class which will provide the necessary underlying storage. 
  * When doing the planning for a telco management cluster, consider the ODF infrastructure and networking requirements. 
  * Dual stack support is limited. ODF IPv4 is supported on dual-stack clusters. 



Engineering considerations
    

  * Address capacity warnings promptly as recovery can be difficult in case of storage capacity exhaustion, see [Capacity planning](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.22/html-single/planning_your_deployment/index#capacity_planning). 



**Additional resources**

  * [Support OpenShift dual stack with OpenShift Data Foundation using IPv4](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.13/html-single/4.13_release_notes/index#support_openshift_dual_stack_with_odf_using_ipv4)
  * [Infrastructure requirements](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.15/html-single/planning_your_deployment/index#infrastructure-requirements_rhodf)
  * [Network requirements](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.15/html-single/planning_your_deployment/index#network-requirements_rhodf)
  * [Storage cluster deployment approaches](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.17/html-single/planning_your_deployment/index#network-requirements_rhodf)



## 5.16.6. Logging

The Cluster Logging Operator collects and ships logs off OpenShift Container Platform hub cluster nodes for remote archival and analysis. The reference configuration uses Kafka to ship audit and infrastructure logs to a remote archive. 

New in this release
    

  * No reference design updates in this release 



Limits and requirements
    

  * The reference configuration does not include local log storage. 
  * The reference configuration does not include aggregation of managed cluster logs at the hub cluster. 



Engineering considerations
    

  * The impact of cluster CPU use is based on the number or size of logs generated and the amount of log filtering configured. 
  * The reference configuration does not include shipping of application logs. The inclusion of application logs in the configuration requires you to evaluate the application logging rate and have sufficient additional CPU resources allocated to the reserved set. 



## 5.16.7. OpenShift API for Data Protection

OpenShift API for Data Protection (OADP) is automatically installed and managed by Red Hat Advanced Cluster Management (RHACM) when the backup feature is enabled, facilitating backup and restore of workloads in OpenShift Container Platform clusters. 

Enabling OADP is required for RHACM disaster recovery solutions. 

New in this release
    

  * No reference design updates in this release 



Description
    

The OpenShift API for Data Protection (OADP) Operator is automatically installed and managed by Red Hat Advanced Cluster Management (RHACM) when the backup feature is enabled. 

The OADP Operator facilitates the backup and restore of workloads in OpenShift Container Platform clusters. Based on the upstream open source project Velero, it allows you to backup and restore all Kubernetes resources for a given project, including persistent volumes. 

While it is not mandatory to have it on the hub cluster, it is highly recommended for cluster backup, disaster recovery and high availability architecture for the hub cluster. The OADP Operator must be enabled to use the disaster recovery solutions for RHACM. The reference configuration enables backup (OADP) through the `MultiClusterHub` custom resource (CR) provided by the RHACM Operator. 

Limits and requirements
    

  * Only one version of OADP can be installed on a cluster. The version installed by RHACM must be used for RHACM disaster recovery features. 



Engineering considerations
    

  * No engineering consideration updates in this release. 



## 5.16.8. cert-manager Operator

The cert-manager Operator for OpenShift Container Platform manages the lifecycle of TLS certificates for hub cluster components and workloads. 

New in this release
    

  * No reference design updates in this release. 



Description
    

The cert-manager Operator for OpenShift Container Platform manages the lifecycle of TLS certificates for cluster components and workloads. The cert-manager Operator automates certificate issuance, renewal, and rotation, eliminating manual certificate management. The reference configuration includes the cert-manager Operator to optionally manage certificates for the API server and ingress controller endpoints. 

You can use RHACM `CertificatePolicy` resources to monitor certificate health across all managed clusters. 

Limits and requirements
    

  * The reference configuration includes only the ACME DNS01 challenge type for platform certificate issuance. 



Engineering considerations
    

  * Use RHACM `CertificatePolicy` resources on the hub cluster to monitor certificate expiration and compliance across managed clusters. 
  * Optionally, configure a `PrometheusRule` on the hub cluster to generate alerts based on policy compliance status.
