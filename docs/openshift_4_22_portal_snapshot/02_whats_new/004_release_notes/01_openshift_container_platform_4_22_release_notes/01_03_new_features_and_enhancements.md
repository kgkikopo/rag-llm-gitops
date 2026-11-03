# 1.3. New features and enhancements

Before working with this release, familiarize yourself with the new features included in the OpenShift Container Platform4.22 release. 

## 1.3.1. AI applications

MCP server for Red Hat OpenShift Container Platform (Technology Preview)
     OpenShift Container Platform 4.22 introduces MCP server for Red Hat OpenShift Container Platform as a Technology Preview feature. 

When a problem occurs on your OpenShift Container Platform cluster, you want to determine exactly what is happening, so that you can fix the issue as soon as possible. The MCP server for Red Hat OpenShift Container Platform feature provides an AI tool for this purpose to quickly and easily diagnose your OpenShift Container Platform cluster. 

For more information, see [MCP server for Red Hat OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ai_applications/#mcp-server-overview-1). 

## 1.3.2. Authentication and authorization

Advanced direct authentication fields (Technology Preview)
    

You can configure advanced OIDC authentication scenarios using structured authentication fields and Common Expression Language (CEL) expressions. This feature exposes additional fields from the Kubernetes `AuthenticationConfiguration` API for flexible claim mapping and token validation. Use CEL expressions to define username and group claim fallback logic, add validation rules, and handle non-standard claim structures. This feature is available for both standalone clusters and hosted control planes. 

For more information, see [About advanced direct authentication fields](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#structured-auth-config-about). 

## 1.3.3. Cluster Version Operator

New `NetworkPolicy` parameter denies traffic for pods that are not host-networked
     A new `NetworkPolicy` parameter for the `openshift-cluster-version` namespace denies all ingress and egress traffic for pods that are not host-networked. 

Network reconfiguration for single-node OpenShift clusters
    

You can change the network configuration of a single-node OpenShift cluster without performing a full cluster redeployment by using the Lifecycle Agent. This feature supports critical edge computing scenarios such as disaster recovery and network rehoming with a stage-driven workflow that includes the ability to rollback changes on failure. 

You can change network properties such as node IP addresses, machine network CIDRs, default gateways, VLAN settings, and DNS servers. 

For more information, see [Understand single-node OpenShift network reconfiguration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-understanding-sno-ip-configuration). 

## 1.3.4. Extensions (OLM v1)

OLM v1 `deploymentConfig` API for cluster extension customization (Technology Preview)
    

The `deploymentConfig` API in the `ClusterExtension` resource enables declarative customization of Operator pod deployments, providing feature parity with `Subscription.spec.config` in OLM (Classic). Configure resource limits, node placement, environment variables, volumes, affinity rules, and pod annotations when installing cluster extensions. The format is compatible with OLM (Classic) configurations, simplifying migration. 

For more information, see [Configuring cluster extensions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extensions/#olmv1-deployment-config-api_olmv1-configuring-extensions). 

`ClusterObjectSet` API for safe phased rollouts (Technology Preview)
    

Operator Lifecycle Manager (OLM) v1 introduces the `ClusterObjectSet` API, which enables safe, phased rollouts of Kubernetes resources during ClusterExtension deployments and upgrades. A `ClusterObjectSet` object applies resources sequentially in ordered phases with built-in readiness checks, ensuring resources are created after any resources they are dependent on. 

For more information, see [ClusterObjectSets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extensions/#olmv1-clusterobjectsets_operator-controller). 

## 1.3.5. IBM Power

The IBM Power® release on OpenShift Container Platform 4.22 adds improvements and new capabilities to OpenShift Container Platform components
    

New features on IBM Power® include: 

  * Installer-provisioned infrastructure for IBM PowerVC is now generally available. 
  * Enforce RSA key format for Installer-provisioned infrastructure on IBM Power® Virtual Server. 
  * Harden the destroy logic for Installer-provisioned infrastructure on IBM Power® Virtual Server to simplify removing a cluster. 
  * Add DAL14 region to the Installer-provisioned infrastructure on IBM Power® Virtual Server. 
  * Add S1122 system type to DAL14 region in the Installer-provisioned infrastructure on IBM Power® Virtual Server. 



## 1.3.6. IBM Z and IBM LinuxONE

The IBM Z® and IBM® LinuxONE release on OpenShift Container Platform 4.22 adds improvements and new capabilities to OpenShift Container Platform components
    

New features on IBM Z® and IBM® LinuxONE include: 

  * Enables Secrets Store CSI Driver on IBM Z® 
  * Hosted Control Plane support for OpenShift Container Platform clusters deployed on OpenShift Virtualization on IBM Z® and IBM® LinuxONE 



## 1.3.7. Insights Operator

The Insights Operator collects custom resources to improve data retrieval efficiency and system performance
    

With this release, the Insights Operator now collects the `opentelemetrycollectors.opentelemetry.io` custom resource to improve data retrieval efficiency and system performance. 

To maintain security and prevent the collection of sensitive information, the Insights Operator applies the following constraints: 

  * Resource Limit: The Insights Operator collects a maximum of five OpenTelemetry Collector custom resources from the cluster. 
  * Data Masking: The Insights Operator retains only the service subsection of the `spec.config` field. It omits receivers, exporters, and other pipeline configuration details. 



These improvements allow OpenShift Container Platform to better analyze the efficiency of the data gathering process and provide more precise environment insights. ([OCPBUGS-78115](https://redhat.atlassian.net/browse/OCPBUGS-78115)) 

## 1.3.8. Installation and update

Enhancements for IBM Power Virtual Server
     The IBM Power Virtual Server Cluster CAPI Operator is enhanced to `v0.12.2` in OpenShift Container Platform version 4.22. Users are required to manually select the appropriate partner group in the `Contributing Group` field due to multiple partner confidential group memberships. This feature ensures compatibility, improves system performance, and maintains security by proper selection of partner groups. The result is an OpenShift Container Platform deployment with improved overall performance and reliability. 
Installing a cluster on Microsoft Azure with a user-provisioned DNS is generally available
    

You can enable a user-provisioned domain name server (DNS) instead of the default cluster-provisioned DNS solution. For example, your organization’s security policies might not allow the use of public DNS services such as Microsoft Azure DNS. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud. If you use this feature, you must provision the cluster first and then provide your own DNS solution that includes records for `api.<cluster_name>.<base_domain>.` and `*.apps.<cluster_name>.<base_domain>.`. 

Installing a cluster on Azure with a user-provisioned DNS was introduced in OpenShift Container Platform 4.21 with Technology Preview status. In OpenShift Container Platform 4.22, it is now generally available. 

For more information, see [Enabling a user-managed DNS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installation-azure-enabling-user-managed-DNS_installing-azure-customizations) and [Provisioning your own DNS records](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installation-azure-provisioning-own-dns-records_installing-azure-customizations). 

OpenShift zones support for vSphere host groups is generally available
    

With this release, you can map OpenShift Container Platform failure domains to VMware vSphere host groups. This means that you can make use of the high availability offered by a vSphere stretched cluster configuration. 

OpenShift zones support for vSphere host groups was introduced in OpenShift Container Platform 4.19 with Technology Preview status. In OpenShift Container Platform 4.22, it is now generally available. 

For information on configuring host groups at installation, see [VMware vSphere host group enablement](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installation-vsphere-regions-zones-host-groups_installing-vsphere-installer-provisioned-customizations). 

For information on configuring host groups for existing clusters, see [Specifying multiple host groups for your cluster on vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#specifying-host-groups-vsphere_post-install-vsphere-zones-regions-configuration). 

Installing a cluster on AWS European Sovereign Cloud (Technology Preview)
    

You can now install OpenShift Container Platform on Amazon Web Services (AWS) in the European Sovereign Cloud (EUSC) region (`eusc-de-east-1`). The AWS EUSC region is separate and independent from other AWS regions, with all the infrastructure located within the European Union (EU). You must specify a custom Amazon Machine Image (AMI) in the `platform.aws.defaultMachinePlatform.amiID` field of your `install-config.yaml` file. Other limitations also apply. The AWS EUSC region is available as a Technology Preview feature. 

For more information, see [AWS EUSC](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installation-aws-eusc_region_installing-aws-account). 

Installing a cluster on Google Cloud with N4A machine types
    

With this update, you can install a OpenShift Container Platform cluster on Google Cloud with N4A machine types. 

N4A Virtual Machines (VMs) use highly efficient Arm-based processors. N4A machines deliver exceptional performance compared to current-generation x86-based VMs, making them ideal for containerized applications and microservices on OpenShift Container Platform. 

For more information, see [Tested instance types for Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installation-gcp-tested-machine-types_installing-gcp-customizations) and [N4A machine series (Google documentation)](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series). 

Installing a cluster using Red Hat Enterprise Linux (RHEL) 10
    

With this update, you can install a cluster using RHEL version 10 as the base image for all machines in the cluster. This feature is available as a Technology Preview. To enable this feature, enable the `TechPreviewNoUpgrade` feature set and set the `osImageStream` parameter to `rhel-10` in your `install-config.yaml` file. 

For more information, see [Installation configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#installation-config-parameters-generic). 

Adding custom alerts to `oc adm upgrade recommend` command output
    

With this update, you can add the `openShiftUpdatePrecheck` label to alerts in a `PrometheusRule` custom resource (CR) so that, when you run the `oc adm upgrade recommend` command, any firing alerts with this label appear in the command output. 

For more information, see [Adding custom alerts to `oc adm upgrade recommend` command output](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#oc-adm-upgrade-recommend-custom-alert_updating-cluster-prepare). 

Deploying virtualized control planes with KubeVirt Redfish (Technology Preview)
    

You can use KubeVirt Redfish to deploy OpenShift Container Platform clusters with control plane nodes running as virtual machines on a hosting cluster with OpenShift Virtualization. Running control plane nodes as VMs provides VM-level isolation for control plane components. KubeVirt Redfish exposes VMs through the standard Redfish API, enabling existing installation methods such as installer-provisioned infrastructure, Agent-based Installer, and GitOps Zero Touch Provisioning (ZTP) to manage VM power states and boot media. The feature is available as a Technology Preview. 

For more information, see [Understanding virtualized control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/virtualized_control_planes/#vcp-overview). 

Bucketless workload identity for Google Cloud clusters
    

When installing or upgrading an OpenShift Container Platform cluster on Google Cloud with short-term credentials, you can now use the `--key-storage-method=pool-jwk-file` option with the `ccoctl gcp create-all` command to attach OIDC signing keys directly to the workload identity pool provider. This method eliminates the need to create a publicly accessible Google Cloud Storage (GCS) bucket for OIDC configuration, which reduces the public attack surface and can help meet security and network policies in restricted environments. 

For more information, see [Creating GCP resources with the Cloud Credential Operator utility](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#cco-ccoctl-creating-at-once_installing-gcp-customizations). 

Oracle Alloy General Availability
    

With this update, installing a cluster on Oracle Alloy is now Generally Available. 

For more information, see [Installing a cluster on Oracle Distributed Cloud by using the Assisted Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_oracle_distributed_cloud/#installing-oci-assisted-installer) or [Installing a cluster on Oracle Distributed Cloud by using the Agent-based Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_oracle_distributed_cloud/#installing-oci-agent-based-installer). 

## 1.3.9. Machine Config Operator

Boot nodes into a custom machine config pool
    

With this update, you can boot new nodes directly into a custom machine config pool. Before this update, you needed to create the node in the worker machine config pool, then move the node into the custom machine config pool, which requires a node reboot. By launching the node directly into the new pool, you save a node reboot cycle. 

For information, see [Creating a custom machine config pool with a new node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-config-custom-mcp-automatic_machine-config-creating-custom-mcp). 

Boot image skew enforcement
    

With this update, the Machine Config Operator (MCO) examines the boot image version reported in the `MachineConfiguration` object to determine if that boot image is appropriate for the cluster. If the boot image version is too old, the Operator reports that boot image version skew is detected and blocks cluster updates until you manually update the boot image or disable boot image skew enforcement. 

For more information, see [Boot image skew enforcement](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-skew-mgmt). 

Boot image management for control plane nodes is generally available
    

With this update, the boot image management feature for control plane nodes is generally available. With boot image management enabled, you can configure your cluster to update the node boot image whenever you update your cluster. Before this update, boot image management was supported for worker nodes only. Boot image management for control plane nodes was introduced in OpenShift Container Platform 4.21 for AWS, Google Cloud, and Azure clusters, and is now generally available for the platforms in 4.22. The boot image management feature for control plane nodes is not supported for VMware vSphere. 

For more information, see [Boot image management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-configs-configure). 

Boot image management for worker nodes is now default for Azure and vSphere
    

With this update, the boot image management feature for worker nodes is default behavior in Azure and vSphere clusters. As such, after updating to OpenShift Container Platform 4.22, the boot images in your cluster are automatically updated to version 4.22. With subsequent updates, the Machine Config Operator (MCO) again updates the boot images in your cluster. Any new nodes you create after updating are based on the new version. Current nodes are not affected by this feature. 

Before updating to 4.22, you must acknowledge this change or opt-out of this default behavior before proceeding. For information on opting out, see [Disabling boot image management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-images-disable_machine-configs-configure). 

For more information on the boot image management feature, see [Boot image management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-images_machine-configs-configure). 

Boot image update documentation
    

With this update, the Machine Config Operator documentation contains procedures to update the boot image on compute nodes for most supported OpenShift Container Platform platforms. 

For OpenShift Container Platform platforms that do not support automatic boot image updating or for clusters configured with the boot image management feature disabled, you can manually update the boot image used by the compute nodes in your cluster. 

For more information, see [Manually updating the boot image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-images-manual). 

`AppliedFilesAndOS` machine config node condition is now `AppliedFiles` and `AppliedOSImage` (Technology Preview)
    

With this update, the `AppliedFilesAndOS` condition reported by the machine config node has been split into the `AppliedFiles` and `AppliedOSImage` conditions as a Technology Preview feature. The machine config nodes custom resource monitors the progress of machine configuration updates to nodes. The `AppliedFiles` condition reports whether MCO has updated files on the node. The `AppliedOSImage` condition reports whether the MCO has updated the operating system. 

For more information, see [About node status during updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#checking-mco-node-status_machine-config-overview). 

## 1.3.10. Machine management

Bare-metal nodes on VMware vSphere clusters is generally available
    

You can add bare-metal compute machines to an existing OpenShift Container Platform cluster on vSphere. With this capability, you can migrate workloads to physical hardware without reinstalling the cluster. 

Bare-metal nodes on vSphere clusters was introduced in OpenShift Container Platform 4.21 with Technology Preview status. Beginning in OpenShift Container Platform 4.22.13, it is now generally available. 

For more information, see [Adding bare-metal compute machines to a vSphere cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#adding-bare-metal-compute-vsphere-user-infra). 

AWS Dedicated Host support (Technology Preview)
    

You can now place compute machines on Amazon Web Services (AWS) Dedicated Hosts. Dedicated Hosts are physical servers that are fully dedicated to your use. With Dedicated Hosts, you can use your existing per-socket, per-core, or per-VM software licenses and comply with corporate policies that require physical CPU assignment. 

You can configure Dedicated Host placement in the following ways: 

  * At installation, you can specify Dedicated Host IDs in the `install-config.yaml` file to place compute machines on specific Dedicated Hosts. 
  * After installation, you can use the Machine API or the Cluster API to place machines on Dedicated Hosts by using dynamic host allocation or by specifying individual Dedicated Host IDs. 



For more information, see [Installation configuration parameters for AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installation-config-parameters-aws), [Machine sets that place machines on Dedicated Hosts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#machineset-dedicated-hosts_creating-machineset-aws), and [Place machines on Dedicated Hosts by using machine templates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#machine-feature-aws-dedicated-hosts_cluster-api-config-options-aws). 

## 1.3.11. Networking

HAProxy version update to 2.8.18
     OpenShift Container Platform 4.22 now uses HAProxy version 2.8.18. With this update, the Ingress Controller benefits from the latest bug fixes and performance improvements in HAProxy. For more information about the changes in this version, see the [HAProxy 2.8.18 release notes](https://www.haproxy.org/download/2.8/src/CHANGELOG). 
Network policy enhancement
    

To reduce the cluster attack surface and ensure predictable network behavior, OpenShift Container Platform now enforces least-privilege network policies on critical networking components. Starting in 4.22, OpenShift Container Platform includes default `NetworkPolicy` objects in some of its own namespaces. Specifically, the operators that manage cluster DNS and cluster Ingress automatically install and maintain default deny-all `NetworkPolicy` objects in their respective namespaces. 

Important

Because these namespaces now operate on a deny-by-default model, any unmanaged or custom pods running in these namespaces will have their network traffic blocked. Do not modify the default `NetworkPolicy` objects that OpenShift Container Platform includes in its own namespaces by default. 

To check the namespaces that include the objects by default, you can run the following command: 

```shell-session
$ oc get networkpolicies --all-namespaces
```


The OpenShift Container Platform 4.22 release did not include these objects in all OpenShift Container Platform namespaces; later OpenShift Container Platform releases might include the objects in additional namespaces. 

IPv4 forwarding for specific network interfaces
    

You can enable IPv4 forwarding on specific network interfaces by using the Kubernetes NMState Operator. By setting the `forwarding: true` field in a `NodeNetworkConfigurationPolicy` custom resource, you can configure individual interfaces to forward IP packets without enabling global IP forwarding on the cluster. This approach improves security by keeping global forwarding disabled while allowing forwarding only on the interfaces that require it, such as secondary interfaces used by MetalLB load balancers. 

For more information, see [Enable IP forwarding on specific interfaces](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/kubernetes_nmstate/#nw-nmstate-enable-per-interface-ip-forwarding_k8s-nmstate-updating-node-network-config). 

Kubernetes NMState Operator extends metrics support
    

The Kubernetes NMState Operator can now collect metrics from the following Kubernetes components: 

  * `kubernetes_nmstate_policies_status`, which tracks the active status of `NodeNetworkConfigurationPolicy` (NNCP) resources across the cluster. 
  * `kubernetes_nmstate_enactments_status`, which tracks the active status of `NodeNetworkConfigurationEnactment` (NNCE) resources on a per-node basis. 

For more information, see [Viewing metrics collected by the Kubernetes NMState Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#viewing-stats-collected-kubernetes-nmstate-op_k8s-nmstate-about-the-k8s-nmstate-operator). 




Alternative interface names for network interfaces with the Kubernetes NMState Operator
    

Assign alternative names to network interfaces by using the Kubernetes NMState Operator. Alternative names provide consistent, descriptive labels for interfaces across cluster nodes, simplifying automation in environments where interface names vary across nodes. 

For more information, see [Configure alternative network interface names](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/kubernetes_nmstate/#k8s-nmstate-alternative-interface-names_k8s-nmstate-updating-node-network-config). 

Ingress firewall configuration with the `commatrix` plugin
    

The `commatrix` plugin generates `nftables` firewall rules in Butane format for deployment to cluster nodes. These rules restrict ingress traffic to only the flows required by deployed services, promoting a zero-trust security posture. The plugin also generates a `NodeDisruptionPolicy` patch to apply rule updates without node reboots. 

For more information, see [Generate nftables firewall rules in Butane format](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#commatrix-generate-butane_configuring-firewall). 

MetalLB ConfigurationState resource reports controller and speaker configuration health
    

You can now use the new `ConfigurationState` custom resource to verify that MetalLB has successfully applied your settings across the cluster. This feature provides a single, consistent location to identify configuration errors that were previously only visible by searching through individual node logs or FRR status reports 

MetalLB creates a `ConfigurationState` resource for the controller and for each speaker node. Each resource reports whether your configuration is valid and surfaces specific error details if validation fails, such as issues with `IPAddressPool`, `BGPPeer`, or `BFDProfile` objects. This centralized reporting helps you monitor system integrity and resolve networking conflicts more quickly. 

For more information, see [Checking MetalLB configuration status](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#nw-metallb-checking-configuration-status_monitor-metallb-config-status). 

Multi-network policy backend uses nftables
    

With this release, the multi-network policy backend uses `nftables` instead of `iptables`. The `iptables` backend has been removed and there is no option to revert to it. The `MultiNetworkPolicy` API and user-facing configuration are unchanged, so your existing multi-network policies continue to work without modification. 

For more information, see [Configuring multi-network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#configuring-multi-network-policy). 

Tune MetalLB advertisements for individual LoadBalancer services using service labels
    

With MetalLB, you can now set `spec.serviceSelectors` on `BGPAdvertisement` and `L2Advertisement` custom resources (CRs). This allows you to match LoadBalancer services by label so each advertisement applies its own BGP or Layer 2 settings to the services you choose, even when those services use the same IPAddressPool. 

For more information, see [About advertising for the IP address pools](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#about-advertise-for-ipaddress-pools). 

Immutable AWS Network Load Balancer for a service
     With this release, when deploying a service with the AWS Load Balancer the `service.beta.kubernetes.io/aws-load-balancer-type` annotation is immutable for existing services. To change the load balancer type, you must recreate the service. 
BGP EVPN for cluster user-defined networks
    

With this release, Border Gateway Protocol Ethernet Virtual Private Network (BGP EVPN) is available for primary cluster user-defined networks. Enabling this feature on OpenShift Container Platform allows a `ClusterUserDefinedNetwork` overlay network to use the EVPN control plane for deeper integration with the data center network. 

For more information, see [About BGP EVPN for primary cluster user-defined networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/advanced_networking/#about-bgp-evpn-user-defined-networks). 

NoOverlay mode with BGP routing
    

With this release, no-overlay mode with Border Gateway Protocol (BGP) routing is available as a Technology Preview feature on bare-metal clusters that use OVN-Kubernetes. No-overlay mode forwards layer 3 pod traffic on the underlay network using BGP-learned routes instead of Geneve encapsulation, which can improve east-west performance. You can enable no-overlay mode on the default layer 3 cluster network and on primary `ClusterUserDefinedNetwork` resources. 

For more information, see [Improve east-west performance by routing pods on the underlay with BGP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/advanced_networking/#no-overlay-mode-bgp-routing). 

Support for PTP boundary clock without holdover on Intel Granite Rapids-D hardware
    

You can now configure Precision Time Protocol (PTP) boundary clock (BC) without holdover on Intel Granite Rapids-D (GNR-D) hardware that uses onboard Network Acceleration Complex (NAC) ports and optional Carter Flat expansion network interface cards (NICs). 

In this deployment, one time receiver (TR) port synchronizes to an upstream timing source while time transmitter (TT) ports distribute synchronized time downstream. GNR-D BC without holdover deployments on Carter Flat hardware require a continuous upstream PTP timing source because monitored holdover is not supported. 

For more information, see [Boundary clocks without holdover on Intel Granite Rapids-D hardware](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/advanced_networking/#nw-ptp-granite-rapids-boundary-clock-overview_configuring-ptp). 

Support for Granite Rapids-D (GNR-D) telecom boundary clock with holdover on an Intel GNR-D platform (Technology Preview)
    

You can configure an Intel® Granite Rapids-D (GNR-D) platform device as telecom boundary clock (T-BC) with holdover support by using the PTP Operator. 

With this technology preview feature, you can configure T-BC holdover on GNR-D platforms `dell/XR8720t` and `hpe/EL140-Gen12`. 

In this configuration, one time receiver (TR) port synchronizes to an upstream telecom grandmaster clock, while time transmitter (TT) ports distribute synchronized time to downstream devices. If the upstream timing source degrades, disconnects, or becomes unavailable, the system enters holdover mode and maintains timing by using configured digital phase-locked loop (DPLL) devices. 

For more information, see [Configuring GNR-D T-BC holdover on a GNR-D platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/advanced_networking/#nw-ptp-gnrd-t-bc-holdover_configuring-ptp). 

PTP Telecom Grandmaster on Intel Granite Rapids-D (Technology Preview)
    

You can configure a Precision Time Protocol (PTP) Telecom Grandmaster (T-GM) on Intel Granite Rapids-D (GNR-D) servers so a single Global Navigation Satellite System (GNSS) feed synchronizes timing across onboard Network Acceleration Complex (NAC) ports and optional Carter Flat expansion network interface cards (NICs). The PTP Operator supports GNR-D deployments with the `e830` and `e825` hardware plugins and an example `PtpConfig` custom resource (CR) that you customize for your qualified hardware layout. PTP T-GM on GNR-D is available as a Technology Preview feature. 

For more information, see [Telecom Grandmaster clocks on Intel Granite Rapids-D hardware](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/advanced_networking/#nw-ptp-granite-rapids-telecom-grandmaster-clock-overview_configuring-ptp). 

Dynamic Configuration Manager General Availability
    

With this update, the HAProxy Dynamic Configuration Manager (DCM) feature is now Generally Available. You can use DCM as an alternative update mechanism that configures a running HAProxy process through a domain socket. 

For more information, see [HAProxy Dynamic Configuration Manager (DCM)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#about-haproxy-dynamic-configuration-manager_ingress-operator). 

## 1.3.12. Nodes

Image pull credential verification in multi-tenant clusters
    

With this update, administrators can use the `imagePullCredentialsVerificationPolicy` parameter in a `KubeletConfig` custom resource to enforce credential verification for cached images. This parameter forces the kubelet to re-authenticate with the container registry before it deploys a pod, ensuring that the requesting namespace has valid access rights to the image. 

The underlying `KubeletEnsureSecretPulledImages` feature gate is enabled by default. Administrators can configure specific credential provider policies to balance security and stability: 

  * `AlwaysVerify`: Enforces credential checks for all image pull requests. 
  * `NeverVerifyAllowlistedImages`: Enforces credential checks for user workloads while exempting essential infrastructure images on an allowlist. 

Before this update, multi-tenant OpenShift Container Platform clusters had a security vulnerability where the kubelet did not re-verify credentials for cached images. If one tenant pulled a private image, another tenant could deploy a pod by using that same cache without providing image pull secrets. To mitigate this previously, administrators relied on unsupported configurations. However, these workarounds caused cluster instability, risked control plane failures during registry outages, and blocked crucial cluster upgrades. 

Note

Do not use the `NeverVerifyPreloadedImages` policy when the default `KubeletEnsureSecretPulledImages` feature gate is active, as the policy might not function as expected. Use the `NeverVerifyAllowlistedImages` policy instead. 

For more information, see [Creating a KubeletConfig CRD to edit kubelet parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#create-a-kubeletconfig-crd-to-edit-kubelet-parameters_machine-configs-custom). 




CPU resource enforcement is now enabled by default
    

With this update, the `system-reserved-compressible` parameter is enabled for all clusters that do not use the reserved CPU feature. This addresses previous issues where the system reserved CPU exceeded the desired limit. This default can be overridden by configuring the `systemReservedCPU: ""` parameter in a kubelet configuration. 

For more information, see [How OpenShift Container Platform enforces system-reserved CPU](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#system-reserved-compressible_nodes-nodes-resources-configuring). 

Mount an OCI image into a pod
    

With this update, you can use an image volume to mount an Open Container Initiative (OCI)-compliant artifact directly into a pod. OCI artifacts enable users to store and distribute arbitrary files and metadata using OCI compliant container registries. 

For more information, see [Mounting OCI images and artifacts into a pod](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-image-volume). 

Configurable storage locations for CRI-O artifacts
    

With this update, you can create additional, non-default artifact storage locations in CRI-O that your pods can pull from. By using storage locations for the CRI-O container engine other than the default for OCI artifacts, complete container images, or container image layers, you can reduce application startup time and make your applications run more efficiently. 

For more information, see [Additional CRI-O storage locations for faster container startup](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-additional-crio-storage). 

Project-scoped image pull secrets for mirrored registries (Technology Preview)
    

With this update, you can pull images from mirrored registries by using project-scoped pull secrets as a technology preview feature. Before this update, you needed to use node-level secrets when pulling from a mirrored registry because the kublet does not recognize the mirror configuration, which is configured at the container-runtime level. 

For more information, see [Configuring project-scoped image pull secrets for mirrored registries](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#images-configuration-registry-mirror-project-secret_image-configuration). 

Partitionable devices are now supported with dynamic resource allocation (Technology Preview)
    

With this update, the dynamic resource allocation feature supports partitioning physical hardware into smaller, logical instances, such as Multi-Instance GPUs, based on workload demands. With this technology preview feature, you can safely and efficiently share GPUs across multiple pods. 

For more information, see [Allocating GPUs to pods by using DRA](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-allocate-dra). 

## 1.3.13. OpenShift CLI (oc)

Digest-based image pinning for the oc-mirror v2 plugin
     With this update, the oc-mirror v2 plugin pins Operator catalog images by their digest in your `ImageSetConfiguration` custom resource. Pinning by digest ensures that you always deploy the same Operator catalog image, regardless of any later changes to the upstream tags. For more information, see [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#oc-mirror-workflows-partially-disconnected-v2_about-installing-oc-mirror-v2). 
Configuration of custom target repositories and tags for additional images by using the oc-mirror v2 plugin
     With this update, when using the oc-mirror v2 plugin, you can provide custom destination repository path and tag for specific images. By using the new `targetRepo` and `targetTag` fields within the `additionalImages` section of your `ImageSetConfiguration` custom resource, you can specify the target repository and tag for an image in your target mirror registry. For more information, see [ImageSet configuration parameters for oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#oc-mirror-imageset-config-parameters-v2_about-installing-oc-mirror-v2). 
Availability of the `oc mirror list` command in oc-mirror v2 plugin
     With this update, you can use the list support feature with the oc-mirror v2 plugin. You can run the `oc mirror list` command to explore available platform and Operator content, including their specific versions, from remote and local registries. For more information, see [Creating the image set configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#oc-mirror-building-image-set-config-v2_about-installing-oc-mirror-v2). 

## 1.3.14. Postinstallation configuration

Support for the PCI addresses of NICs in `BareMetalHost` hardware data
    

With this release, the Peripheral Component Interconnect (PCI) address for each network interface controller (NIC) is available in two separate custom resources (CRs). The PCI address is located in the `status.hardware.nics[]` section of the `BareMetalHost` CR and in the `spec.hardware.nics[]` section of the `HardwareData` CR. While these are separate resources, the values in the `pciAddress` fields, for example `0000:00:03.0`, are identical. 

For more information, see [About the BareMetalHost resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bmo-about-the-baremetalhost-resource_bare-metal-postinstallation-configuration) and [The BareMetalHost status](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#the-baremetalhost-status). 

Red Hat Bare-Metal-as-a-Service for OpenShift is generally available
     With this update, Red Hat Bare-Metal-as-a-Service for OpenShift, formerly known as Bare Metal as a Service (BMaaS), is generally available. You can provision and manage bare-metal hosts by using the Metal3 API and the Bare Metal Operator (BMO). These hosts, external to the OpenShift Container Platform cluster, can run workloads that might not be suitable for containerization or virtualization, such as legacy applications or applications that require direct hardware access. For more information, see [Using Red Hat Bare-Metal-as-a-Service for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bare-metal-using-bare-metal-as-a-service). 
Expanding bare-metal clusters using OCI images and Red Hat Bare-Metal-as-a-Service for OpenShift (Technology Preview)
     With this update, you can expand your bare-metal cluster using Red Hat Bare-Metal-as-a-Service for OpenShift with images from an OCI registry as a Technology Preview feature. You can use images from public OCI registries or from the built-in cluster registry. For more information, see [Using Red Hat Bare-Metal-as-a-Service for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#using-red-hat-bare-metal-as-a-service-for-openshift). 
Adding an ARM node to an x86 bare metal cluster
    

With this update, you can add ARM nodes to bare metal clusters with x86 control planes using PXE or virtual media. You can expand your cluster by creating a `BareMetalHost` object with the `aarch64` architecture, and then scaling the machine set to deploy the new machine. 

For more information, see [Preparing the bare metal node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#preparing-the-bare-metal-node_bare-metal-expanding). 

## 1.3.15. Red Hat Enterprise Linux CoreOS (RHCOS)

RHCOS uses RHEL 9.8
     With this update, RHCOS uses Red Hat Enterprise Linux (RHEL) 9.8 packages in OpenShift Container Platform 4.22. These packages ensure that your OpenShift Container Platform instances receive the latest fixes, features, enhancements, hardware support, and driver updates. 
RHCOS 10.2 support (Technology Preview)
     With this update, you can configure your cluster to use RHCOS 10.2 as a Technology Preview feature. You can update the nodes in an existing non-production test cluster or install a new non-production test cluster. For more information, see [Setting the RHCOS version in a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-image-streams). 
Ignition update to version 2.26.1
     With this update, the Ignition utility is updated to version 2.26.1. 
Butane update to version 0.26.0
     With this update, the Butane utility is updated to version 0.26.0. 
Afterburn update to version 5.10.0
     With this update, the Afterburn utility is updated to version 5.10.0. 
coreos-installer update to version 0.26.0
     With this update, the coreos-installer utility is updated to version 0.26.0. 
Support for the numad package
     With this update, the numad package is supported. numad is an automatic NUMA affinity management daemon. It monitors NUMA topology and resource usage within a system that dynamically improves NUMA resource allocation, management, and system performance. 

## 1.3.16. Scalability and performance

NUMA-aware scheduler supports clusters with up to 500 nodes
    

With this release, you can scale the NUMA-aware secondary scheduler to support clusters with up to 500 nodes. The scheduler defaults to a `Burstable` quality of service (QoS) profile, which reduces baseline resource consumption while allowing the scheduler to scale up during peak loads. 

For more information, see [Topology-aware scheduler scalability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#cnf-topology-aware-scheduler-scalability_numa-aware). 

CRI-O ExecCPUAffinity protects low-latency workloads from exec process interruption
    

With this release, you can protect latency-sensitive workloads from performance degradation caused by `oc exec` and shell processes. When you apply a `PerformanceProfile`, the CRI-O `ExecCPUAffinity` feature automatically pins exec processes to a designated CPU within the container’s allocated set, preventing them from running on your workload CPUs. This feature is enabled by default for `Guaranteed` QoS pods with whole-integer CPU requests and requires no additional configuration. You can disable it per profile by adding the `performance.openshift.io/exec-cpu-affinity: "disable"` annotation to the `PerformanceProfile`. 

For more information, see [How `ExecCPUAffinity` prevents latency spikes from exec operations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#cnf-exec-cpu-affinity_cnf-tuning-low-latency-nodes-with-perf-profile). 

## 1.3.17. Support

Custom image configuration for the Support Log Gather
     With this update, you can collect diagnostic data by using custom images in the Support Log Gather. By pointing the `spec.imageStreamRef` field to an approved `ImageStream` tag, you can override the default image. The cluster administrators are responsible for creating and maintaining the list of allowed custom images by managing `ImageStream` resources in the Operator namespace. Each custom image requires its own `MustGather` custom resource and a service account with permissions to access the `ImageStream`. For more information, see [Configuring a Support Log Gather instance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#support-log-gather-config-cli_gathering-cluster-data). 

## 1.3.18. Storage

Adding bare-metals nodes on VMware vSphere is generally available
    

OpenShift Container Platform 4.21 added the ability to add bare-metal nodes to an OpenShift Container Platform cluster on vSphere as a Technology Preview feature. Beginning in OpenShift Container Platform 4.22.13, this feature is generally available. 

However, if you add bare-metal nodes, you must remove the vSphere Container Storage Interface (CSI) Driver, otherwise the cluster is marked as degraded. 

For information about how to add bare-metal nodes, see [Adding bare-metal nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-vsphere-adding-bm-nodes_persistent-storage-csi-vsphere). 

For information about how to remove the vSphere CSI Driver, see [Disabling and enabling storage on vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-vsphere-disable-storage-overview_persistent-storage-csi-vsphere). 

New VolumeSnapshotClass csi-gce-pd-vsc-images is generally available
     By default, you cannot restore more than six volumes per snapshot per hour. So in Kubevirt environments, you normally cannot create more than six VMs per hour from a "golden image" (templates saved as snapshots). 

For Google Cloud Platform (GCP) persistent disk (PD) storage Container Storage Interface (CSI), there is now a non-default `VolumeSnapshotClass`, named `csi-gce-pd-vsc-images`, that uses the `snapshot-type: images` parameter. When using KubeVirt, it allows you to overcome the six VMs per hour restriction, so that you can create VMs from "golden images". 

This feature is generally available in OpenShift Container Platform 4.22. 

For more information, see [Volume snapshots CRD: VolumeSnapshotClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#volume-snapshot-crds). 

Support for Hyperdisk Balanced High Availability volumes is generally available
     OpenShift Container Platform 4.22 introduces support for Hyperdisk Balanced High Availability volumes as generally available. 

Hyperdisk Balanced High Availability volumes are useful for: 

  * Protecting your applications from a zonal outage by synchronously replicating data across two zones in the same region 
  * When you require write access to the same volume in multiple zones 



For more information, see [Hyperdisk-balanced high availability disks overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-gcp-hyperdisk-ha-overview_persistent-storage-csi-gcp-pd). 

Local Storage Operator symlinks management is generally available
     To prevent storage breakage during OpenShift Container Platform upgrades, OpenShift Container Platform 4.22 provides a mechanism, the `LocalVolumeDeviceLink` Custom Resource Definition, to detect, alert, and remap broken symlinks without manual node-level intervention. 

The Local Storage Operator (LSO) traditionally creates persistent volumes (PVs) based on `/dev/disk/by-id/` paths, following the assumption that they are stable. However, Linux kernel updates, firmware updates, or `udev` rule changes can cause these supposedly stable names to change or disappear. 

Administrators have the following notification and correction options to deal with symlink disruptions: 

  * Monitoring: (default) If the current and preferred path do not match, an alert occurs, but no changes occur to the current path. 
  * Use existing path: Alerts are silenced and LSO uses the existing path. 
  * Recreate symlinks: Symlinks are recreated to point to the new, updated device path. 



For more information, see [Local Storage Operator symlinks management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#local-storage-symlinks-top-level_persistent-storage-local). 

Mutable CSI node allocatable property is generally available
     This feature allows for dynamically updating the maximum number of storage volumes a node can handle. Without this feature, volume limits are essentially immutable when a node first joins the cluster. If the environment changes—for example, if you attach a new network interface (ENI) that shares a hardware "slot" with your storage—OpenShift Container Platform does not recognize it has fewer slots available for disks, leading to pods becoming stuck. 

This feature is only supported on AWS Elastic Block Storage (EBS). 

Mutable CSI node allocatable property was introduced in OpenShift Container Platform 4.21 as a Technical Preview feature. In OpenShift Container Platform 4.22, it is supported as generally available. 

Updated release of the Secrets Store CSI Driver Operator
     The Secrets Store CSI Driver Operator version v4.22 is now based on the upstream version v1.5.6 release of secrets-store-csi-driver. OpenShift Container Platform 4.22 enables Secrets Store CSI Driver on IBM Z®. 
European Sovereign Cloud (EUSC) region (Technology Preview)
     European Sovereign Cloud (EUSC) region acts as a "digital fortress" built within a specific country’s borders. Sovereign Clouds are specifically designed to meet strict legal, jurisdictional, and security requirements of a particular nation or entity. 

In the context of storage, EUSC ensures that all data, including primary storage, backups, and the resulting metadata, resides physically within the specific nation’s borders and remains exclusively under its legal jurisdiction. 

For OpenShift Container Platform 4.22, only AWS Elastic Block Storage supports EUSC. AWS Elastic File Storage (EFS) is not supported. 

EUSC is supported as a Technology Preview feature. 

For more information about EUSC, see [Support for European Sovereign Cloud (EUSC) region](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#support-for-european-sovereign-cloud-eusc-region). 

## 1.3.19. Web console

Support for integrated OCI chart interaction
    

The OpenShift Container Platform web console now fully supports browsing, inspecting, and installing Open Container Initiative (OCI)-based Helm charts directly from configured repositories to provide functional parity with traditional HTTP(S) Helm charts. This enhancement removes the previous discovery-only limitation, enabling users to interact with and deploy OCI-based charts seamlessly within the console’s repository views. 

For more information, see [Configuring custom Helm chart repositories](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#configuring-custom-helm-chart-repositories). 

Azure Resource Group field for operator installations on Azure WIF clusters
     The operator installation page now includes a **Resource Group** field for operators who have the `token-auth-azure` annotation enabled on Azure Workload Identity Federation (WIF) clusters. As a result, operators who require an Azure resource group value, such as `ODF` (NooBaa), can complete their setup without manual workarounds. 
Install Helm charts from a direct URL
    

In the web console, you can now install a Helm chart directly from a URL, without first adding the chart to a Helm chart repository or the console catalog. Both `oci://` and `https://` URLs are supported. 

Warning

Installing a Helm chart from a direct URL bypasses the validation checks provided by the developer catalog. Install charts only from URLs you trust, because unverified charts can introduce security risks to your cluster. When possible, use charts from the developer catalog or a configured Helm repository instead. 

**Configure Basic HTTP authentication for namespace-scoped ProjectHelmChartRepository objects in the web console**
     The creation form for namespace-scoped `ProjectHelmChartRepository` objects in the OpenShift Container Platform web console now includes a **Basic HTTP authentication** field. As a result, you can select a secret that has Basic authentication credentials when you create the object. Because transmitting credentials requires a secure connection, you must use HTTPS for the repository URL when you configure Basic authentication.
