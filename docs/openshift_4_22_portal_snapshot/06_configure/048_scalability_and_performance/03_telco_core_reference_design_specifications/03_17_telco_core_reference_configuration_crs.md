# 3.17. Telco core reference configuration CRs

Use the following custom resources (CRs) to configure and deploy OpenShift Container Platform clusters with the telco core profile. Use the CRs to form the common baseline used in all the specific use models unless otherwise indicated. 

## 3.17.1. Extract the telco core reference design configuration CRs

You can extract the complete set of custom resources (CRs) for the telco core profile from the `telco-core-rds-rhel9` container image. The container image has both the required CRs, and the optional CRs, for the telco core profile. 

**Prerequisites**

  * You have installed `podman`. 



**Procedure**

  1. Log on to the container image registry with your credentials by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


  2. Extract the content from the `telco-core-rds-rhel9` container image by running the following commands: 

```shell-session
$ mkdir -p ./out
```


```shell-session
$ podman run -it registry.redhat.io/openshift4/openshift-telco-core-rds-rhel9:v4.22 | base64 -d | tar xv -C out
```


**Verification**

  * The `out` directory has the following directory structure. You can view the telco core CRs in the `out/telco-core-rds/` directory by running the following command: 

```shell-session
$ tree -L 4
```


**Example output**

```plaintext
.
├── configuration
│   ├── compare.sh
│   ├── core-baseline.yaml
│   ├── core-finish.yaml
│   ├── core-overlay.yaml
│   ├── core-upgrade.yaml
│   ├── kustomization.yaml
│   ├── Makefile
│   ├── ns.yaml
│   ├── README.md
│   ├── reference-crs
│   │   ├── custom-manifests
│   │   │   ├── mcp-worker-1.yaml
│   │   │   ├── mcp-worker-2.yaml
│   │   │   ├── mcp-worker-3.yaml
│   │   │   └── README.md
│   │   ├── optional
│   │   │   ├── logging
│   │   │   ├── networking
│   │   │   ├── other
│   │   │   └── tuning
│   │   └── required
│   │       ├── networking
│   │       ├── other
│   │       ├── performance
│   │       ├── scheduling
│   │       └── storage
│   ├── reference-crs-kube-compare
│   │   ├── compare_ignore
│   │   ├── comparison-overrides.yaml
│   │   ├── metadata.yaml
│   │   ├── optional
│   │   │   ├── logging
│   │   │   ├── networking
│   │   │   ├── other
│   │   │   └── tuning
│   │   ├── ReferenceVersionCheck.yaml
│   │   ├── required
│   │   │   ├── networking
│   │   │   ├── other
│   │   │   ├── performance
│   │   │   ├── scheduling
│   │   │   └── storage
│   │   ├── unordered_list.tmpl
│   │   └── version_match.tmpl
│   └── template-values
│       ├── hw-types.yaml
│       └── regional.yaml
├── install
│   ├── custom-manifests
│   │   ├── mcp-worker-1.yaml
│   │   ├── mcp-worker-2.yaml
│   │   └── mcp-worker-3.yaml
│   ├── example-standard.yaml
│   ├── extra-manifests
│   │   ├── control-plane-load-kernel-modules.yaml
│   │   ├── kdump-master.yaml
│   │   ├── kdump-worker.yaml
│   │   ├── mc_rootless_pods_selinux.yaml
│   │   ├── mount_namespace_config_master.yaml
│   │   ├── mount_namespace_config_worker.yaml
│   │   ├── sctp_module_mc.yaml
│   │   └── worker-load-kernel-modules.yaml
│   └── README.md
└── README.md
```


## 3.17.2. Compare a cluster with the telco core reference configuration

After you deploy a telco core cluster, you can use the `cluster-compare` OpenShift CLI (`oc`) plugin to assess compliance with the telco core reference design specifications (RDS). 

The plugin-specific reference configuration for telco core is packaged in a container image with the telco core CRs. 

For further information about the `cluster-compare` plugin, see "Understanding the cluster-compare plugin". 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have credentials to access the `registry.redhat.io` container image registry. 
  * You installed the `cluster-compare` plugin. 



**Procedure**

  1. Log on to the container image registry with your credentials by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


  2. Extract the content from the `telco-core-rds-rhel9` container image by running the following commands: 

```shell-session
$ mkdir -p ./out
```


```shell-session
$ podman run -it registry.redhat.io/openshift4/openshift-telco-core-rds-rhel9:v4.22 | base64 -d | tar xv -C out
```


You can view the reference configuration in the `out/telco-core-rds/configuration/reference-crs-kube-compare` directory by running the following command: 

```shell-session
$ tree -L 2
```


  3. Example output 

```plaintext
.
├── compare_ignore
├── comparison-overrides.yaml
├── metadata.yaml
├── optional
│   ├── logging
│   ├── networking
│   ├── other
│   └── tuning
├── ReferenceVersionCheck.yaml
├── required
│   ├── networking
│   ├── other
│   ├── performance
│   ├── scheduling
│   └── storage
├── unordered_list.tmpl
└── version_match.tmpl
```


     * `metadata.yaml` is the configuration file for the reference configuration. 
     * `optional` is the directory for optional templates. 
     * `required` is the directory for required templates. 

  4. Compare the configuration for your cluster to the telco core reference configuration by running the following command: 

```shell-session
$ oc cluster-compare -r out/telco-core-rds/configuration/reference-crs-kube-compare/metadata.yaml
```


**Example output**

```shell-session
W1212 14:13:06.281590   36629 compare.go:425] Reference Contains Templates With Types (kind) Not Supported By Cluster: BFDProfile, BGPAdvertisement, BGPPeer, ClusterLogForwarder, Community, IPAddressPool, MetalLB, MultiNetworkPolicy, NMState, NUMAResourcesOperator, NUMAResourcesScheduler, NodeNetworkConfigurationPolicy, SriovNetwork, SriovNetworkNodePolicy, SriovOperatorConfig, StorageCluster

...

**********************************

Cluster CR: config.openshift.io/v1_OperatorHub_cluster
Reference File: required/other/operator-hub.yaml
Diff Output: diff -u -N /tmp/MERGED-2801470219/config-openshift-io-v1_operatorhub_cluster /tmp/LIVE-2569768241/config-openshift-io-v1_operatorhub_cluster
--- /tmp/MERGED-2801470219/config-openshift-io-v1_operatorhub_cluster	2024-12-12 14:13:22.898756462 +0000
+++ /tmp/LIVE-2569768241/config-openshift-io-v1_operatorhub_cluster	2024-12-12 14:13:22.898756462 +0000
@@ -1,6 +1,6 @@
 apiVersion: config.openshift.io/v1
 kind: OperatorHub
 metadata:
+  annotations:
+    include.release.openshift.io/hypershift: "true"
   name: cluster
-spec:
-  disableAllDefaultSources: true

**********************************

Summary
CRs with diffs: 3/4
CRs in reference missing from the cluster: 22
other:
  other:
    Missing CRs:
    - optional/other/control-plane-load-kernel-modules.yaml
    - optional/other/worker-load-kernel-modules.yaml
required-networking:
  networking-root:
    Missing CRs:
    - required/networking/nodeNetworkConfigurationPolicy.yaml
  networking-sriov:
    Missing CRs:
    - required/networking/sriov/sriovNetwork.yaml
    - required/networking/sriov/sriovNetworkNodePolicy.yaml
    - required/networking/sriov/SriovOperatorConfig.yaml
    - required/networking/sriov/SriovSubscription.yaml
    - required/networking/sriov/SriovSubscriptionNS.yaml
    - required/networking/sriov/SriovSubscriptionOperGroup.yaml
required-other:
  scheduling:
    Missing CRs:
    - required/other/catalog-source.yaml
    - required/other/icsp.yaml
required-performance:
  performance:
    Missing CRs:
    - required/performance/PerformanceProfile.yaml
required-scheduling:
  scheduling:
    Missing CRs:
    - required/scheduling/nrop.yaml
    - required/scheduling/NROPSubscription.yaml
    - required/scheduling/NROPSubscriptionNS.yaml
    - required/scheduling/NROPSubscriptionOperGroup.yaml
    - required/scheduling/sched.yaml
required-storage:
  storage-odf:
    Missing CRs:
    - required/storage/odf-external/01-rook-ceph-external-cluster-details.secret.yaml
    - required/storage/odf-external/02-ocs-external-storagecluster.yaml
    - required/storage/odf-external/odfNS.yaml
    - required/storage/odf-external/odfOperGroup.yaml
    - required/storage/odf-external/odfSubscription.yaml
No CRs are unmatched to reference CRs
Metadata Hash: fe41066bac56517be02053d436c815661c9fa35eec5922af25a1be359818f297
No patched CRs
```


Where: 

Cluster CR
     The CR under comparison. The plugin displays each CR with a difference from the corresponding template. 
Reference File
     The template matching with the CR for comparison. 
Diff Output
     The output in Linux diff format shows the difference between the template and the cluster CR. 
Summary
     After the plugin reports the line diffs for each CR, the summary of differences are reported. 
CRs with diffs
     The number of CRs in the comparison with differences from the corresponding templates. 
CRs in reference missing from the cluster
     The number of CRs represented in the reference configuration, but missing from the live cluster. 
Missing CRs
     The list of CRs represented in the reference configuration, but missing from the live cluster. 
No CRs are unmatched to reference CRs
     The CRs that did not match to a corresponding template in the reference configuration. 
Metadata Hash
     Identifies the reference configuration. 
No patched CRs
     The list of patched CRs. 




**Additional resources**

  * [Understanding the cluster-compare plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/comparing-cluster-configurations#understanding-the-cluster-compare-plugin "6.1. Understanding the cluster-compare plugin")



## 3.17.3. Node configuration reference CRs

Use the following custom resources (CRs) to configure node settings for the telco core profile. 

Table 3.2. Node configuration CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Additional kernel modules  |  `control-plane-load-kernel-modules.yaml` |  Optional. Configures the kernel modules for control plane nodes.  |  No   
Additional kernel modules  |  `sctp_module_mc.yaml` |  Optional. Loads the SCTP kernel module in worker nodes.  |  No   
Additional kernel modules  |  `worker-load-kernel-modules.yaml` |  Optional. Configures kernel modules for worker nodes.  |  No   
Container mount namespace hiding  |  `mount_namespace_config_master.yaml` |  Configures a mount namespace for sharing container-specific mounts between kubelet and CRI-O on control plane nodes.  |  No   
Container mount namespace hiding  |  `mount_namespace_config_worker.yaml` |  Configures a mount namespace for sharing container-specific mounts between kubelet and CRI-O on worker nodes.  |  No   
Kdump enable  |  `kdump-master.yaml` |  Configures kdump crash reporting on master nodes.  |  No   
Kdump enable  |  `kdump-worker.yaml` |  Configures kdump crash reporting on worker nodes.  |  No   
Show more

## 3.17.4. Cluster infrastructure reference CRs

Use the following custom resources (CRs) to configure cluster infrastructure components for the telco core profile. 

Table 3.3. Cluster infrastructure CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Cluster logging  |  `ClusterLogForwarder.yaml` |  Configures a log forwarding instance with the specified service account and verifies that the configuration is valid.  |  Yes   
Cluster logging  |  `ClusterLogNS.yaml` |  Configures the cluster logging namespace.  |  Yes   
Cluster logging  |  `ClusterLogOperGroup.yaml` |  Creates the Operator group in the openshift-logging namespace, allowing the Cluster Logging Operator to watch and manage resources.  |  Yes   
Cluster logging  |  `ClusterLogServiceAccount.yaml` |  Configures the cluster logging service account.  |  Yes   
Cluster logging  |  `ClusterLogServiceAccountAuditBinding.yaml` |  Grants the collect-audit-logs cluster role to the logs collector service account.  |  Yes   
Cluster logging  |  `ClusterLogServiceAccountInfrastructureBinding.yaml` |  Allows the collector service account to collect logs from infrastructure resources.  |  Yes   
Cluster logging  |  `ClusterLogSubscription.yaml` |  Creates a subscription resource for the Cluster Logging Operator with manual approval for install plans.  |  Yes   
Disconnected configuration  |  `catalog-source.yaml` |  Defines a disconnected Red Hat Operators catalog.  |  No   
Disconnected configuration  |  `idms.yaml` |  Defines a list of mirrored repository digests for the disconnected registry.  |  No   
Disconnected configuration  |  `operator-hub.yaml` |  Defines an OperatorHub configuration which disables all default sources.  |  No   
Monitoring and observability  |  `monitoring-config-cm.yaml` |  Configuring storage and retention for Prometheus and Alertmanager.  |  Yes   
Power management  |  `PerformanceProfile.yaml` |  Defines a performance profile resource, specifying CPU isolation, hugepages configuration, and workload hints for performance optimization on selected nodes.  |  No   
Show more

## 3.17.5. Resource tuning reference CRs

Use the following custom resources (CRs) to configure resource tuning for the telco core profile. 

Table 3.4. Resource tuning CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
System reserved capacity  |  `control-plane-system-reserved.yaml` |  Optional. Configures kubelet, enabling auto-sizing reserved resources for the control plane node pool.  |  No   
Show more

## 3.17.6. Networking reference CRs

Use the following custom resources (CRs) to configure networking components for the telco core profile. 

Table 3.5. Networking CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Baseline  |  `Network.yaml` |  Configures the default cluster network, specifying OVN Kubernetes settings like routing via the host. It also allows the definition of additional networks, including custom CNI configurations, and enables the use of MultiNetworkPolicy CRs for network policies across multiple networks.  |  No   
Baseline  |  `networkAttachmentDefinition.yaml` |  Optional. Defines a NetworkAttachmentDefinition resource specifying network configuration details such as node selector and CNI configuration.  |  No   
Load Balancer  |  `addr-pool.yaml` |  Configures MetalLB to manage a pool of IP addresses with auto-assign enabled for dynamic allocation of IPs from the specified range.  |  No   
Load Balancer  |  `bfd-profile.yaml` |  Configures bidirectional forwarding detection (BFD) with customized intervals, detection multiplier, and modes for quicker network fault detection and load balancing failover.  |  No   
Load Balancer  |  `bgp-advr.yaml` |  Defines a BGP advertisement resource for MetalLB, specifying how an IP address pool is advertised to BGP peers. This enables fine-grained control over traffic routing and announcements.  |  No   
Load Balancer  |  `bgp-peer.yaml` |  Defines a BGP peer in MetalLB, representing a BGP neighbor for dynamic routing.  |  No   
Load Balancer  |  `community.yaml` |  Defines a MetalLB community, which groups one or more BGP communities under a named resource. Communities can be applied to BGP advertisements to control routing policies and change traffic routing.  |  No   
Load Balancer  |  `metallb.yaml` |  Defines the MetalLB resource in the cluster.  |  No   
Load Balancer  |  `metallbNS.yaml` |  Defines the metallb-system namespace in the cluster.  |  No   
Load Balancer  |  `metallbOperGroup.yaml` |  Defines the Operator group for the MetalLB Operator.  |  No   
Load Balancer  |  `metallbSubscription.yaml` |  Creates a subscription resource for the MetalLB Operator with manual approval for install plans.  |  No   
Multus - Tap CNI for rootless DPDK pods  |  `mc_rootless_pods_selinux.yaml` |  Configures a MachineConfig resource which sets an SELinux boolean for the tap CNI plugin on worker nodes.  |  Yes   
NMState Operator  |  `NMState.yaml` |  Defines an NMState resource that is used by the NMState Operator to manage node network configurations.  |  No   
NMState Operator  |  `NMStateNS.yaml` |  Creates the NMState Operator namespace.  |  No   
NMState Operator  |  `NMStateOperGroup.yaml` |  Creates the Operator group in the openshift-nmstate namespace, allowing the NMState Operator to watch and manage resources.  |  No   
NMState Operator  |  `NMStateSubscription.yaml` |  Creates a subscription for the NMState Operator, managed through OLM.  |  No   
SR-IOV Network Operator  |  `sriovNetwork.yaml` |  Defines an SR-IOV network specifying network capabilities, IP address management (ipam), and the associated network namespace and resource.  |  No   
SR-IOV Network Operator  |  `sriovNetworkNodePolicy.yaml` |  Configures network policies for SR-IOV devices on specific nodes, including customization of device selection, VF allocation (numVfs), node-specific settings (nodeSelector), and priorities.  |  No   
SR-IOV Network Operator  |  `SriovOperatorConfig.yaml` |  Configures various settings for the SR-IOV Operator, including enabling the injector and Operator webhook, disabling pod draining, and defining the node selector for the configuration daemon.  |  No   
SR-IOV Network Operator  |  `SriovSubscription.yaml` |  Creates a subscription for the SR-IOV Network Operator, managed through OLM.  |  No   
SR-IOV Network Operator  |  `SriovSubscriptionNS.yaml` |  Creates the SR-IOV Network Operator subscription namespace.  |  No   
SR-IOV Network Operator  |  `SriovSubscriptionOperGroup.yaml` |  Creates the Operator group for the SR-IOV Network Operator, allowing it to watch and manage resources in the target namespace.  |  No   
Show more

## 3.17.7. Scheduling reference CRs

Use the following custom resources (CRs) to configure scheduling for the telco core profile. 

Table 3.6. Scheduling CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
NUMA-aware scheduler  |  `nrop.yaml` |  Enables the NUMA Resources Operator, aligning workloads with specific NUMA node configurations. Required for clusters with multi-NUMA nodes.  |  No   
NUMA-aware scheduler  |  `NROPSubscription.yaml` |  Creates a subscription for the NUMA Resources Operator, managed through OLM. Required for clusters with multi-NUMA nodes.  |  No   
NUMA-aware scheduler  |  `NROPSubscriptionNS.yaml` |  Creates the NUMA Resources Operator subscription namespace. Required for clusters with multi-NUMA nodes.  |  No   
NUMA-aware scheduler  |  `NROPSubscriptionOperGroup.yaml` |  Creates the Operator group in the numaresources-operator namespace, allowing the NUMA Resources Operator to watch and manage resources. Required for clusters with multi-NUMA nodes.  |  No   
NUMA-aware scheduler  |  `sched.yaml` |  Configures a topology-aware scheduler in the cluster that can handle NUMA aware scheduling of pods across nodes.  |  No   
NUMA-aware scheduler  |  `Scheduler.yaml` |  Configures control plane nodes as non-schedulable for workloads.  |  No   
Show more

## 3.17.8. Storage reference CRs

Use the following custom resources (CRs) to configure storage for the telco core profile. 

Table 3.7. Storage CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
External ODF configuration  |  `01-rook-ceph-external-cluster-details.secret.yaml` |  Defines a Secret resource containing base64-encoded configuration data for an external Ceph cluster in the openshift-storage namespace.  |  No   
External ODF configuration  |  `02-ocs-external-storagecluster.yaml` |  Defines an OpenShift Container Storage (OCS) storage resource which configures the cluster to use an external storage back end.  |  No   
External ODF configuration  |  `odfNS.yaml` |  Creates the monitored openshift-storage namespace for the OpenShift Data Foundation Operator.  |  No   
External ODF configuration  |  `odfOperGroup.yaml` |  Creates the Operator group in the openshift-storage namespace, allowing the OpenShift Data Foundation Operator to watch and manage resources.  |  No   
External ODF configuration  |  `odfSubscription.yaml` |  Creates the OpenShift Data Foundation Operator subscription, managed through OLM.  |  No   
Show more

## 3.17.9. Security reference CRs

Use the following custom resources (CRs) to configure security components for the telco core profile. 

Table 3.8. Security CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Cert-Manager  |  `certManagerNS.yaml` |  Defines the cert-manager-operator namespace.  |  Yes   
Cert-Manager  |  `certManagerOperatorgroup.yaml` |  Defines the OperatorGroup for cert-manager.  |  Yes   
Cert-Manager  |  `certManagerSubscription.yaml` |  Installs the OpenShift cert-manager operator.  |  Yes   
Cert-Manager  |  `certManagerClusterIssuer.yaml` |  Configures an ACME ClusterIssuer using Let’s Encrypt with DNS-01 challenge.  |  Yes   
Cert-Manager  |  `apiServerCertificate.yaml` |  Creates a certificate for the API Server endpoint.  |  Yes   
Cert-Manager  |  `ingressCertificate.yaml` |  Creates a wildcard certificate for the Ingress/Router.  |  Yes   
Cert-Manager  |  `apiServerConfig.yaml` |  Configures OpenShift to use the cert-manager generated API Server certificate.  |  Yes   
Cert-Manager  |  `ingressControllerConfig.yaml` |  Configures OpenShift to use the cert-manager generated Ingress certificate.  |  Yes   
Show more
