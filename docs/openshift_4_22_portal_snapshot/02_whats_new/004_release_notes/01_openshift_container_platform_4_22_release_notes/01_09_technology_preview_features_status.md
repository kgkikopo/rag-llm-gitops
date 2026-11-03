# 1.9. Technology Preview features status

You can determine if a new feature in OpenShift Container Platform 4.22 is currently in Technology Preview before deciding to install the feature. These experimental features are not intended for production use. 

Note the following scope of support on the Red Hat Customer Portal for these features: 

[Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview)

In the following tables, features are marked with the following statuses: 

  * _Not Available_
  * _Technology Preview_
  * _General Availability_
  * _Deprecated_
  * _Removed_



## 1.9.1. AI applications Technology Preview features

Table 1.11. AI applications Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
MCP server for Red Hat OpenShift Container Platform  |  Not Available  |  Not Available  |  Technology Preview   
Show more

## 1.9.2. Authentication and authorization Technology Preview features

Table 1.12. Authentication and authorization Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Pod security admission restricted enforcement  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Show more

## 1.9.3. Edge computing Technology Preview features

Table 1.13. Edge computing Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Accelerated provisioning of GitOps ZTP  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Enabling disk encryption with TPM and PCR protection  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Configuring a local arbiter node  |  General Availability  |  General Availability  |  General Availability   
Configuring a two-node OpenShift Container Platform cluster with fencing  |  Technology Preview  |  Technology Preview  |  General Availability   
Show more

## 1.9.4. Extensions Technology Preview features

Table 1.14. Extensions Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
OLM v1 runtime validation of container images using sigstore signatures  |  Technology Preview  |  Technology Preview  |  General Availability   
OLM v1 permissions preflight check for cluster extensions  |  Technology Preview  |  Technology Preview  |  Technology Preview   
OLM v1 deploying a cluster extension in a specified namespace  |  Technology Preview  |  Technology Preview  |  Technology Preview   
OLM v1 deploying a cluster extension that uses webhooks  |  Technology Preview  |  General Availability  |  General Availability   
OLM v1 software catalog  |  Not Available  |  Technology Preview  |  Technology Preview   
OLM v1 `deploymentConfig` API for cluster extension customization  |  Not Available  |  Not Available  |  Technology Preview   
Show more

## 1.9.5. Installation Technology Preview features

Table 1.15. Installation Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Installing a cluster on Alibaba Cloud by using Assisted Installer  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Installing a cluster using Red Hat Enterprise Linux (RHEL) 10  |  Not Available  |  Not Available  |  Technology Preview   
Dedicated disk for etcd on Microsoft Azure  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Mount shared entitlements in BuildConfigs in RHEL  |  Technology Preview  |  Technology Preview  |  General Availability (through Builds for OpenShift Operator)   
OpenShift zones support for vSphere host groups  |  Technology Preview  |  Technology Preview  |  General Availability   
Selectable Cluster Inventory  |  |  |   
Enabling a user-provisioned DNS on Google Cloud  |  Technology Preview  |  General Availability  |  General Availability   
Enabling a user-provisioned DNS on Microsoft Azure  |  Not Available  |  Technology Preview  |  General Availability   
Enabling a user-provisioned DNS on Amazon Web Services (AWS)  |  Not Available  |  Technology Preview  |  Technology Preview   
Installing a cluster using Google Cloud private and restricted API endpoints  |  Not Available  |  General Availability  |  General Availability   
Installing a cluster on VMware vSphere with multiple network interface controllers  |  General Availability  |  General Availability  |  General Availability   
Red Hat Bare-Metal-as-a-Service for OpenShift (formerly known as bare-metal as a service)  |  Technology Preview  |  Technology Preview  |  General Availability   
Installing a cluster on Amazon Web Services (AWS) European Sovereign Cloud  |  Not Available  |  Not Available  |  Technology Preview   
Installing a cluster on Amazon Web Services (AWS) with dual-stack networking  |  Not Available  |  Not Available  |  Technology Preview   
Running firmware upgrades for hosts in deployed bare-metal clusters  |  Technology Preview  |  General Availability  |  General Availability   
Changing the CVO log level  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Deploying virtualized control planes with KubeVirt Redfish  |  Not Available  |  Not Available  |  Technology Preview   
Show more

Note

Fleet Management supersedes Selectable Cluster Inventory in OpenShift Container Platform 4.20 and later releases. For more information see, the Red Hat Advanced Cluster Management for Kubernetes documentation for [Fleet Management](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/release_notes/index#console-new-features). 

## 1.9.6. Machine Config Operator Technology Preview features

Table 1.16. Machine Config Operator Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Boot image management for Azure and vSphere  |  Technology Preview  |  General Availability  |  General Availability   
Boot image management for control plane nodes  |  Not available  |  Technology Preview  |  General Availability   
Image mode for OpenShift status reporting improvements  |  Not available  |  Technology Preview  |  Technology Preview   
Overriding storage or partition setup  |  Not available  |  Technology Preview  |  Technology Preview   
Show more

## 1.9.7. Machine management Technology Preview features

Table 1.17. Machine management Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Managing machines with the Cluster API for Amazon Web Services  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Managing machines with the Cluster API for Google Cloud  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Managing machines with the Cluster API for IBM Power® Virtual Server  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Managing machines with the Cluster API for Microsoft Azure  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Managing machines with the Cluster API for RHOSP  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Managing machines with the Cluster API for VMware vSphere  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Managing machines with the Cluster API for bare-metal  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Cloud controller manager for IBM Power® Virtual Server  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Adding multiple subnets to an existing VMware vSphere cluster by using compute machine sets  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Bare-metal nodes on VMware vSphere clusters  |  Not Available  |  Technology Preview  |  General Availability   
Amazon Web Services Dedicated Host support  |  Not Available  |  Not Available  |  Technology Preview   
Show more

## 1.9.8. Multi-Architecture Technology Preview features

Table 1.18. Multi-Architecture Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
`kdump` on `arm64` architecture  |  General Availability  |  General Availability  |   
`kdump` on `s390x` architecture  |  General Availability  |  General Availability  |   
`kdump` on `ppc64le` architecture  |  General Availability  |  General Availability  |   
Support for configuring the image stream import mode behavior  |  Technology Preview  |  Technology Preview  |   
Show more

## 1.9.9. Networking Technology Preview features

Table 1.19. Networking Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
eBPF manager Operator  |  Technology Preview  |  Technology Preview  |   
Advertise using L2 mode the MetalLB service from a subset of nodes, using a specific pool of IP addresses  |  Technology Preview  |  Technology Preview  |   
Updating the interface-specific safe sysctls list  |  Technology Preview  |  Technology Preview  |   
Egress service custom resource  |  Technology Preview  |  Technology Preview  |   
VRF specification in `BGPPeer` custom resource  |  Technology Preview  |  Technology Preview  |   
OVN-Kubernetes customized `br-ex` bridge on vSphere and RHOSP  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Live migration to OVN-Kubernetes from OpenShift Container Platform SDN  |  Not Available  |  Not Available  |   
Dynamic Configuration Manager (DCM)  |  Technology Preview  |  Technology Preview  |  General Availability   
SR-IOV Network Operator support for Intel C741 Emmitsburg Chipset  |  Technology Preview  |  Technology Preview  |  General Availability   
Dual-port NIC for PTP ordinary clock  |  General Availability  |  General Availability  |   
DPU Operator  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Fast IPAM for the Whereabouts IPAM CNI plugin  |  Technology Preview  |  Technology Preview  |   
Unnumbered BGP peering  |  General Availability  |  General Availability  |   
Load balancing across the aggregated bonded interface with xmitHashPolicy  |  Technology Preview  |  Technology Preview  |   
PF Status Relay Operator for high availability with SR-IOV networks  |  Technology Preview  |  Technology Preview  |   
Preconfigured user-defined network end points using MTV  |  Technology Preview  |  Technology Preview  |   
Unassisted holdover for PTP devices  |  Technology Preview  |  General Availability  |   
No-overlay mode with BGP routing  |  Not Available  |  Not Available  |  Technology Preview   
Configuring GNR-D T-BC holdover on a GNR-D platform  |  Not Available  |  Not Available  |  Technology Preview   
PTP Telecom Grandmaster (T-GM) on Intel Granite Rapids-D (GNR-D)  |  Not Available  |  Not Available  |  Technology Preview   
Show more

## 1.9.10. Node Technology Preview features

Table 1.20. Nodes Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
`MaxUnavailableStatefulSet` featureset  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Default sigstore `openshift` cluster image policy  |  Technology Preview  |  General Availability  |  General Availability   
Attribute-Based GPU Allocation  |  Technology Preview  |  General Availability  |  General Availability   
Project-scoped image pull secrets for mirrored registries  |  Not Available  |  Not Available  |  Technology Preview   
Partitionable device DRA support  |  Not Available  |  Not Available  |  Technology Preview   
Show more

## 1.9.11. Postinstallation configuration Technology Preview features

Table 1.21. Postinstallation configuration Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Expanding a bare-metal cluster using images from OCI registries  |  Not Available  |  Not Available  |  Technology Preview   
Show more

## 1.9.12. Red Hat OpenStack Platform (RHOSP) Technology Preview features

Table 1.22. RHOSP Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
RHOSP integration into the Cluster CAPI Operator  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Hosted control planes on RHOSP 17.1  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Show more

## 1.9.13. Scalability and performance Technology Preview features

Table 1.23. Scalability and performance Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
factory-precaching-cli tool  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Hyperthreading-aware CPU manager policy  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Mount namespace encapsulation  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Node Observability Operator  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Increasing the etcd database size  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Managing etcd size by setting the `eventTTLMinutes` property  |  Not available  |  Technology Preview  |  General Availability   
Pinned Image Sets  |  Technology Preview  |  Technology Preview  |  General Availability   
Configuring NUMA-aware scheduler replicas and high availability  |  General Availability  |  General Availability  |  General Availability   
Show more

## 1.9.14. Storage Technology Preview features

Table 1.24. Storage Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
AWS EFS One Zone volume  |  General Availability  |  General Availability  |  General Availability   
Azure File CSI cloning support  |  Technology Preview  |  General Availability  |  General Availability   
Azure File CSI snapshot support  |  Technology Preview  |  General Availability  |  General Availability   
Azure Disk performance plus  |  General Availability  |  General Availability  |  General Availability   
Configuring fsGroupChangePolicy per namespace  |  General Availability  |  General Availability  |  General Availability   
European Sovereign Cloud (EUSC) region  |  Not Available  |  Not Available  |  Technology Preview   
Hyperdisk Balanced HA volumes  |  Not Available  |  Not Available  |  General Availability   
LSO symlinks management  |  Not Available  |  Not Available  |  General Availability   
Increasing max number of volumes per node for vSphere  |  Technology Preview  |  Technology Preview  |  Technology Preview   
RWX/RWO SELinux mount option  |  Technology Preview  |  Technology Preview  |  Technology Preview   
CSI volume group snapshots  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Volume Attribute Classes  |  Technology Preview  |  General Availability  |  General Availability   
Volume populators  |  General Availability  |  General Availability  |  General Availability   
Show more

## 1.9.15. Web console Technology Preview features

Table 1.25. Web console Technology Preview trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Red Hat OpenShift Lightspeed in the OpenShift Container Platform web console  |  Technology Preview  |  Technology Preview  |   
Show more
