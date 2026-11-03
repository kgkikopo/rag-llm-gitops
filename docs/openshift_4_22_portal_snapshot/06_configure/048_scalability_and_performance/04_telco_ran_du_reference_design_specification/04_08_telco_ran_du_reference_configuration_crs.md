# 4.8. Telco RAN DU reference configuration CRs

Use the following custom resources (CRs) to configure and deploy OpenShift Container Platform clusters with the telco RAN DU profile. Use the CRs to form the common baseline used in all the specific use models unless otherwise indicated. 

Note

You can extract the complete set of RAN DU CRs from the `ztp-site-generate` container image. See "Preparing the GitOps ZTP site configuration repository" for more information. 

## 4.8.1. Cluster tuning reference CRs

Use the following custom resources (CRs) to configure cluster tuning for the telco RAN DU reference design. 

Table 4.6. Cluster tuning CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Cluster capabilities  |  `example-sno.yaml` |  Representative ClusterInstance CR to install single-node OpenShift with the RAN DU profile  |  No   
Console disable  |  `cluster-tuning/console-disable/ConsoleOperatorDisable.yaml` |  Disables the Console Operator.  |  No   
Disconnected registry  |  `extra-manifest/09-openshift-marketplace-ns.yaml` |  Defines a dedicated namespace for managing the OpenShift Operator Marketplace.  |  No   
Disconnected registry  |  `disconnected-registry/DefaultCatsrc.yaml` |  Configures the catalog source for the disconnected registry.  |  No   
Disconnected registry  |  `cluster-tuning/DisableOLMPprof.yaml` |  Removes the obsolete `ConfigMap` CR that disabled OLM performance profiling in earlier releases. OLM performance profiling collection is removed in OpenShift Container Platform 4.22.  |  No   
Disconnected registry  |  `disconnected-registry/DisconnectedIDMS.yaml` |  Configures disconnected registry image content source policy.  |  No   
Disconnected registry  |  `cluster-tuning/operator-hub/OperatorHub.yaml` |  Optional, for multi-node clusters only. Configures the OperatorHub in OpenShift, disabling all default Operator sources. Not required for single-node OpenShift installs with marketplace capability disabled.  |  No   
Monitoring configuration  |  `cluster-tuning/monitoring-configuration/ReduceMonitoringFootprint.yaml` |  Reduces the monitoring footprint by disabling Alertmanager and Telemeter, and sets Prometheus retention to 24 hours  |  No   
Network diagnostics disable  |  `cluster-tuning/disabling-network-diagnostics/DisableSnoNetworkDiag.yaml` |  Configures the cluster network settings to disable built-in network troubleshooting and diagnostic features.  |  No   
Show more

## 4.8.2. Day 2 Operators reference CRs

Use the following custom resources (CRs) to configure Day 2 Operators for the telco RAN DU reference design. 

Table 4.7. Day 2 Operators CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Cluster Logging Operator  |  `cluster-logging/ClusterLogForwarder.yaml` |  Configures log forwarding for the cluster.  |  No   
Cluster Logging Operator  |  `cluster-logging/ClusterLogNS.yaml` |  Configures the namespace for cluster logging.  |  No   
Cluster Logging Operator  |  `cluster-logging/ClusterLogOperGroup.yaml` |  Configures Operator group for cluster logging.  |  No   
Cluster Logging Operator  |  `cluster-logging/ClusterLogServiceAccount.yaml` |  New in 4.18. Configures the cluster logging service account.  |  No   
Cluster Logging Operator  |  `cluster-logging/ClusterLogServiceAccountAuditBinding.yaml` |  New in 4.18. Configures the cluster logging service account.  |  No   
Cluster Logging Operator  |  `cluster-logging/ClusterLogServiceAccountInfrastructureBinding.yaml` |  New in 4.18. Configures the cluster logging service account.  |  No   
Cluster Logging Operator  |  `cluster-logging/ClusterLogSubscription.yaml` |  Manages installation and updates for the Cluster Logging Operator.  |  No   
Lifecycle Agent  |  `ibu/ImageBasedUpgrade.yaml` |  Manage the image-based upgrade process in OpenShift Container Platform.  |  Yes   
Lifecycle Agent  |  `lca/LcaSubscription.yaml` |  Manages installation and updates for the LCA Operator.  |  Yes   
Lifecycle Agent  |  `lca/LcaSubscriptionNS.yaml` |  Configures namespace for LCA subscription.  |  Yes   
Lifecycle Agent  |  `lca/LcaSubscriptionOperGroup.yaml` |  Configures the Operator group for the LCA subscription.  |  Yes   
Local Storage Operator  |  `storage-lso/StorageClass.yaml` |  Defines a storage class with a Delete reclaim policy and no dynamic provisioning in the cluster.  |  No   
Local Storage Operator  |  `storage/StorageLV.yaml` |  Configures local storage devices for the example-storage-class in the openshift-local-storage namespace, specifying device paths and filesystem type.  |  No   
Local Storage Operator  |  `storage-lso/StorageNS.yaml` |  Creates the namespace with annotations for workload management and the deployment wave for the Local Storage Operator.  |  No   
Local Storage Operator  |  `storage-lso/StorageOperGroup.yaml` |  Creates the Operator group for the Local Storage Operator.  |  No   
Local Storage Operator  |  `storage-lso/StorageSubscription.yaml` |  Creates the namespace for the Local Storage Operator with annotations for workload management and deployment wave.  |  No   
LVM Operator  |  `storage-lvm/LVMOperatorStatus.yaml` |  Verifies the installation or upgrade of the LVM Storage Operator.  |  Yes   
LVM Operator  |  `storage-lvm/StorageLVMCluster.yaml` |  Defines an LVM cluster configuration, with placeholders for storage device classes and volume group settings. Optional substitute for the Local Storage Operator.  |  No   
LVM Operator  |  `storage-lvm/StorageLVMSubscription.yaml` |  Manages installation and updates of the LVMS Operator. Optional substitute for the Local Storage Operator.  |  No   
LVM Operator  |  `storage-lvm/StorageLVMSubscriptionNS.yaml` |  Creates the namespace for the LVMS Operator with labels and annotations for cluster monitoring and workload management. Optional substitute for the Local Storage Operator.  |  No   
LVM Operator  |  `storage-lvm/StorageLVMSubscriptionOperGroup.yaml` |  Defines the target namespace for the LVMS Operator. Optional substitute for the Local Storage Operator.  |  No   
Node Tuning Operator  |  `node-tuning-operator/aarch64/PerformanceProfile.yaml` |  Configures node performance settings in an OpenShift Container Platform cluster, optimizing for low latency and real-time workloads for aarch64 CPUs.  |  No   
Node Tuning Operator  |  `node-tuning-operator/x86_64/PerformanceProfile.yaml` |  Configures node performance settings in an OpenShift Container Platform cluster, optimizing for low latency and real-time workloads for x86_64 CPUs.  |  No   
Node Tuning Operator  |  `node-tuning-operator/TunedPerformancePatch.yaml` |  Applies performance tuning settings, including scheduler groups and service configurations for nodes in the specific namespace.  |  No   
Node Tuning Operator  |  `node-tuning-operator/TunedPowerCustom.yaml` |  Applies additional powersave mode tuning as an overlay on top of TunedPerformancePatch.  |  No   
PTP fast event notifications  |  `ptp-operator/configuration/PtpConfigBoundaryForEvent.yaml` |  Configures PTP settings for PTP boundary clocks with additional options for event synchronization. Dependent on cluster role.  |  No   
PTP fast event notifications  |  `ptp-operator/configuration/PtpConfigForHAForEvent.yaml` |  Configures PTP for highly available boundary clocks with additional PTP fast event settings. Dependent on cluster role.  |  No   
PTP fast event notifications  |  `ptp-operator/configuration/PtpConfigMasterForEvent.yaml` |  Configures PTP for PTP grandmaster clocks with additional PTP fast event settings. Dependent on cluster role.  |  No   
PTP fast event notifications  |  `ptp-operator/configuration/PtpConfigSlaveForEvent.yaml` |  Configures PTP for PTP ordinary clocks with additional PTP fast event settings. Dependent on cluster role.  |  No   
PTP fast event notifications  |  `ptp-operator/PtpOperatorConfigForEvent.yaml` |  Overrides the default OperatorConfig. Configures the PTP Operator specifying node selection criteria for running PTP daemons in the openshift-ptp namespace.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigBoundary.yaml` |  Configures PTP settings for PTP boundary clocks. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigDualCardGmWpc.yaml` |  Configures PTP grandmaster clock settings for hosts that have dual NICs. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigThreeCardGmWpc.yaml` |  Configures PTP grandmaster clock settings for hosts that have 3 NICs. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigGmWpc.yaml` |  Configures PTP grandmaster clock settings for hosts that have a single NIC. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigSlave.yaml` |  Configures PTP settings for a PTP ordinary clock. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigDualFollower.yaml` |  Configures PTP settings for a PTP ordinary clock with 2 interfaces in an active/standby configuration. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigTBCWpc.yaml` |  Configures PTP as a Telecom boundary clock. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigDualCardTBCWpc.yaml` |  Configures PTP as a Telecom boundary clock for hosts that have dual NICs. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigThreeCardTBCWpc.yaml` |  Configures PTP as a Telecom boundary clock for hosts that have 3 NICs. Dependent on cluster role.  |  No   
PTP Operator  |  `ptp-operator/configuration/PtpConfigTTSCWpc.yaml` |  Configures PTP settings for a PTP Telecom Time Slave Clock with single interface. Dependent on cluster role.  |  N   
PTP Operator  |  `ptp-operator/configuration/PtpConfigGnrdBcNoHoldover.yaml` |  Configures PTP settings for a PTP Boundary Clock without holdover on GNR-D hardware. Dependent on cluster role.  |  N   
PTP Operator  |  `ptp-operator/PtpOperatorConfig.yaml` |  Configures the PTP Operator settings, specifying node selection criteria for running PTP daemons in the openshift-ptp namespace.  |  No   
PTP Operator  |  `ptp-operator/PtpSubscription.yaml` |  Manages installation and updates of the PTP Operator in the openshift-ptp namespace.  |  No   
PTP Operator  |  `ptp-operator/PtpSubscriptionNS.yaml` |  Configures the namespace for the PTP Operator.  |  No   
PTP Operator  |  `ptp-operator/PtpSubscriptionOperGroup.yaml` |  Configures the Operator group for the PTP Operator.  |  No   
PTP Operator (high availability)  |  `ptp-operator/configuration/PtpConfigBoundary.yaml` |  Configures PTP settings for highly available PTP boundary clocks.  |  No   
PTP Operator (high availability)  |  `ptp-operator/configuration/PtpConfigForHA.yaml` |  Configures PTP settings for highly available PTP boundary clocks.  |  No   
SR-IOV FEC Operator  |  `sriov-fec-operator/AcceleratorsNS.yaml` |  Configures namespace for the VRAN Acceleration Operator. Optional part of application workload.  |  Yes   
SR-IOV FEC Operator  |  `sriov-fec-operator/AcceleratorsOperGroup.yaml` |  Configures the Operator group for the VRAN Acceleration Operator. Optional part of application workload.  |  Yes   
SR-IOV FEC Operator  |  `sriov-fec-operator/AcceleratorsSubscription.yaml` |  Manages installation and updates for the VRAN Acceleration Operator. Optional part of application workload.  |  Yes   
SR-IOV FEC Operator  |  `sriov-fec-operator/SriovFecClusterConfig.yaml` |  Configures SR-IOV FPGA Ethernet Controller (FEC) settings for nodes, specifying drivers, VF amount, and node selection.  |  Yes   
SR-IOV Operator  |  `sriov-operator/SriovNetwork.yaml` |  Defines an SR-IOV network configuration, with placeholders for various network settings.  |  No   
SR-IOV Operator  |  `sriov-operator/SriovNetworkNodePolicy.yaml` |  Configures SR-IOV network settings for specific nodes, including device type, RDMA support, physical function names, and the number of virtual functions.  |  No   
SR-IOV Operator  |  `sriov-operator/SriovOperatorConfig.yaml` |  Configures SR-IOV Network Operator settings, including node selection, injector, and webhook options.  |  No   
SR-IOV Operator  |  `sriov-operator/SriovOperatorConfigForSNO.yaml` |  Configures the SR-IOV Network Operator settings for single-node OpenShift, including node selection, injector, webhook options, and disabling node drain, in the openshift-sriov-network-operator namespace.  |  No   
SR-IOV Operator  |  `sriov-operator/SriovSubscription.yaml` |  Manages the installation and updates of the SR-IOV Network Operator.  |  No   
SR-IOV Operator  |  `sriov-operator/SriovSubscriptionNS.yaml` |  Creates the namespace for the SR-IOV Network Operator with specific annotations for workload management and deployment waves.  |  No   
SR-IOV Operator  |  `sriov-operator/SriovSubscriptionOperGroup.yaml` |  Defines the target namespace for the SR-IOV Network Operators, enabling their management and deployment within this namespace.  |  No   
Show more

## 4.8.3. Machine configuration reference CRs

Use the following custom resources (CRs) to configure machine settings for the telco RAN DU reference design. 

Table 4.8. Machine configuration CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Container runtime (crun)  |  `optional-extra-manifest/enable-crun-master.yaml` |  Configures the container runtime (crun) for control plane nodes.  |  No   
Container runtime (crun)  |  `optional-extra-manifest/enable-crun-worker.yaml` |  Configures the container runtime (crun) for worker nodes.  |  No   
Kdump enable  |  `extra-manifest/06-kdump-master.yaml` |  Configures kdump crash reporting on master nodes.  |  No   
Kdump enable  |  `extra-manifest/06-kdump-worker.yaml` |  Configures kdump crash reporting on worker nodes.  |  No   
Kubelet configuration and container mount hiding  |  `extra-manifest/01-container-mount-ns-and-kubelet-conf-master.yaml` |  Configures a mount namespace for sharing container-specific mounts between kubelet and CRI-O on control plane nodes.  |  No   
Kubelet configuration and container mount hiding  |  `extra-manifest/01-container-mount-ns-and-kubelet-conf-worker.yaml` |  Configures a mount namespace for sharing container-specific mounts between kubelet and CRI-O on worker nodes.  |  No   
One-shot time sync  |  `extra-manifest/99-sync-time-once-master.yaml` |  Synchronizes time once on master nodes.  |  No   
One-shot time sync  |  `extra-manifest/99-sync-time-once-worker.yaml` |  Synchronizes time once on worker nodes.  |  No   
SCTP  |  `extra-manifest/03-sctp-machine-config-master.yaml` |  Loads the SCTP kernel module on master nodes.  |  Yes   
SCTP  |  `extra-manifest/03-sctp-machine-config-worker.yaml` |  Loads the SCTP kernel module on worker nodes.  |  Yes   
Set RCU normal  |  `extra-manifest/08-set-rcu-normal-master.yaml` |  Disables rcu_expedited by setting rcu_normal after the control plane node has booted.  |  No   
Set RCU normal  |  `extra-manifest/08-set-rcu-normal-worker.yaml` |  Disables rcu_expedited by setting rcu_normal after the worker node has booted.  |  No   
SRIOV-related kernel arguments  |  `extra-manifest/07-sriov-related-kernel-args-master.yaml` |  Enables SR-IOV support on master nodes.  |  No   
SRIOV-related kernel arguments  |  `extra-manifest/07-sriov-related-kernel-args-worker.yaml` |  Enables SR-IOV support on worker nodes.  |  No   
Show more
