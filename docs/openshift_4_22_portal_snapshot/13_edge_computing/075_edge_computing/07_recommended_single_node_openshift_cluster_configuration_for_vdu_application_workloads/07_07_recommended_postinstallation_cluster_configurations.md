# 7.7. Recommended postinstallation cluster configurations

**Additional resources**

When the cluster installation is complete, the ZTP pipeline applies the following custom resources (CRs) that are required to run DU workloads. 

Note

In GitOps ZTP v4.10 and earlier, you configure UEFI secure boot with a `MachineConfig` CR. This is no longer required in GitOps ZTP v4.11 and later. In v4.11, you configure UEFI secure boot for single-node OpenShift clusters by updating the `spec.nodes[].bootMode` field in the `ClusterInstance` CR that you use to install the cluster. For more information, see "Deploying a managed cluster with ClusterInstance and GitOps ZTP". 

**Additional resources**

  * [Deploying a managed cluster with ClusterInstance and GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites#ztp-deploying-a-site_ztp-deploying-far-edge-sites "4.6. Deploy a managed cluster with ClusterInstance and GitOps ZTP")



## 7.7.1. Operators

Single-node OpenShift clusters that run DU workloads require the following Operators to be installed: 

  * Local Storage Operator 
  * Logging Operator 
  * PTP Operator 
  * SR-IOV Network Operator 



You also need to configure a custom `CatalogSource` CR, disable the default `OperatorHub` configuration, and configure an `ImageContentSourcePolicy` mirror registry that is accessible from the clusters that you install. 

**Recommended Storage Operator namespace and Operator group configuration (`StorageNS.yaml`, `StorageOperGroup.yaml`)**

```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-local-storage
  annotations:
    workload.openshift.io/allowed: management
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-local-storage
  namespace: openshift-local-storage
  annotations: {}
spec:
  targetNamespaces:
    - openshift-local-storage
```


**Recommended Cluster Logging Operator namespace and Operator group configuration (`ClusterLogNS.yaml`, `ClusterLogOperGroup.yaml`)**

```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-logging
  annotations:
    workload.openshift.io/allowed: management
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-logging
  namespace: openshift-logging
  annotations: {}
spec:
  targetNamespaces:
    - openshift-logging
```


**Recommended PTP Operator namespace and Operator group configuration (`PtpSubscriptionNS.yaml`, `PtpSubscriptionOperGroup.yaml`)**

```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-ptp
  annotations:
    workload.openshift.io/allowed: management
  labels:
    openshift.io/cluster-monitoring: "true"
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ptp-operators
  namespace: openshift-ptp
  annotations: {}
spec:
  targetNamespaces:
    - openshift-ptp
```


**Recommended SR-IOV Operator namespace and Operator group configuration (`SriovSubscriptionNS.yaml`, `SriovSubscriptionOperGroup.yaml`)**

```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-sriov-network-operator
  annotations:
    workload.openshift.io/allowed: management
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: sriov-network-operators
  namespace: openshift-sriov-network-operator
  annotations: {}
spec:
  targetNamespaces:
    - openshift-sriov-network-operator
```


**Recommended`CatalogSource` configuration (`DefaultCatsrc.yaml`)**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: default-cat-source
  namespace: openshift-marketplace
  annotations:
    target.workload.openshift.io/management: '{"effect": "PreferredDuringScheduling"}'
spec:
  displayName: default-cat-source
  image: $imageUrl
  publisher: Red Hat
  sourceType: grpc
  updateStrategy:
    registryPoll:
      interval: 1h
status:
  connectionState:
    lastObservedState: READY
```


**Recommended`ImageContentSourcePolicy` configuration (`DisconnectedICSP.yaml`)**

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: ImageContentSourcePolicy
metadata:
  name: disconnected-internal-icsp
  annotations: {}
spec:
#    repositoryDigestMirrors:
#    - $mirrors
```


**Recommended`OperatorHub` configuration (`OperatorHub.yaml`)**

```yaml
apiVersion: config.openshift.io/v1
kind: OperatorHub
metadata:
  name: cluster
  annotations: {}
spec:
  disableAllDefaultSources: true
```


## 7.7.2. Operator subscriptions

Single-node OpenShift clusters that run DU workloads require the following `Subscription` CRs. The subscription provides the location to download the following Operators: 

  * Local Storage Operator 
  * Logging Operator 
  * PTP Operator 
  * SR-IOV Network Operator 
  * SRIOV-FEC Operator 



For each Operator subscription, specify the channel to get the Operator from. The recommended channel is `stable`. 

You can specify `Manual` or `Automatic` updates. In `Automatic` mode, the Operator automatically updates to the latest versions in the channel as they become available in the registry. In `Manual` mode, new Operator versions are installed only when they are explicitly approved. 

Tip

Use `Manual` mode for subscriptions. This allows you to control the timing of Operator updates to fit within scheduled maintenance windows. 

**Recommended Local Storage Operator subscription (`StorageSubscription.yaml`)**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: local-storage-operator
  namespace: openshift-local-storage
  annotations: {}
spec:
  channel: "stable"
  name: local-storage-operator
  source: redhat-operators-disconnected
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
```


**Recommended SR-IOV Operator subscription (`SriovSubscription.yaml`)**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: sriov-network-operator-subscription
  namespace: openshift-sriov-network-operator
  annotations: {}
spec:
  channel: "stable"
  name: sriov-network-operator
  source: redhat-operators-disconnected
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
```


**Recommended PTP Operator subscription (`PtpSubscription.yaml`)**

```yaml
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: ptp-operator-subscription
  namespace: openshift-ptp
  annotations: {}
spec:
  channel: "stable"
  name: ptp-operator
  source: redhat-operators-disconnected
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
```


**Recommended Cluster Logging Operator subscription (`ClusterLogSubscription.yaml`)**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cluster-logging
  namespace: openshift-logging
  annotations: {}
spec:
  channel: "stable-6.6"
  name: cluster-logging
  source: redhat-operators-disconnected
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
```


## 7.7.3. Cluster logging and log forwarding

Single-node OpenShift clusters that run DU workloads require logging and log forwarding for debugging. The following custom resources (CRs) are required. 

**Recommended ClusterLogForwarder.yaml**

```yaml
apiVersion: "observability.openshift.io/v1"
kind: ClusterLogForwarder
metadata:
  name: instance
  namespace: openshift-logging
  annotations: {}
spec:
  # outputs: $outputs
  # pipelines: $pipelines
  serviceAccount:
    name: logcollector
#apiVersion: "observability.openshift.io/v1"
#kind: ClusterLogForwarder
#metadata:
#  name: instance
#  namespace: openshift-logging
# spec:
#   outputs:
#   - type: "kafka"
#     name: kafka-open
#     # below url is an example
#     kafka:
#       url: tcp://10.46.55.190:9092/test
#   filters:
#   - name: test-labels
#     type: openshiftLabels
#     openshiftLabels:
#       label1: test1
#       label2: test2
#       label3: test3
#       label4: test4
#   pipelines:
#   - name: all-to-default
#     inputRefs:
#     - audit
#     - infrastructure
#     filterRefs:
#     - test-labels
#     outputRefs:
#     - kafka-open
#   serviceAccount:
#     name: logcollector
```


Note

Set the `spec.outputs.kafka.url` field to the URL of the Kafka server where the logs are forwarded to. 

**Recommended ClusterLogNS.yaml**

```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-logging
  annotations:
    workload.openshift.io/allowed: management
```


**Recommended ClusterLogOperGroup.yaml**

```yaml
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-logging
  namespace: openshift-logging
  annotations: {}
spec:
  targetNamespaces:
    - openshift-logging
```


**Recommended ClusterLogServiceAccount.yaml**

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: logcollector
  namespace: openshift-logging
  annotations: {}
```


**Recommended ClusterLogServiceAccountAuditBinding.yaml**

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: logcollector-audit-logs-binding
  annotations: {}
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: collect-audit-logs
subjects:
  - kind: ServiceAccount
    name: logcollector
    namespace: openshift-logging
```


**Recommended ClusterLogServiceAccountInfrastructureBinding.yaml**

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: logcollector-infrastructure-logs-binding
  annotations: {}
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: collect-infrastructure-logs
subjects:
  - kind: ServiceAccount
    name: logcollector
    namespace: openshift-logging
```


**Recommended ClusterLogSubscription.yaml**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cluster-logging
  namespace: openshift-logging
  annotations: {}
spec:
  channel: "stable-6.6"
  name: cluster-logging
  source: redhat-operators-disconnected
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
```


## 7.7.4. Performance profile

Single-node OpenShift clusters that run DU workloads require a Node Tuning Operator performance profile to use real-time host capabilities and services. 

Note

In earlier versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator. 

The following example `PerformanceProfile` CR illustrates the required single-node OpenShift cluster configuration. 

**Recommended performance profile configuration (`PerformanceProfile.yaml`)**

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  # if you change this name make sure the 'include' line in TunedPerformancePatch.yaml
  # matches this name: include=openshift-node-performance-${PerformanceProfile.metadata.name}
  # Also in file 'validatorCRs/informDuValidator.yaml':
  # name: 50-performance-${PerformanceProfile.metadata.name}
  name: openshift-node-performance-profile
  annotations:
    ran.openshift.io/reference-configuration: "ran-du.redhat.com"
spec:
  additionalKernelArgs:
    - "rcupdate.rcu_normal_after_boot=0"
    - "efi=runtime"
    - "vfio_pci.enable_sriov=1"
    - "vfio_pci.disable_idle_d3=1"
    - "module_blacklist=irdma"
  cpu:
    isolated: $isolated
    reserved: $reserved
  hugepages:
    defaultHugepagesSize: $defaultHugepagesSize
    pages:
      - size: $size
        count: $count
        node: $node
  machineConfigPoolSelector:
    pools.operator.machineconfiguration.openshift.io/$mcp: ""
  nodeSelector:
    node-role.kubernetes.io/$mcp: ''
  numa:
    topologyPolicy: "restricted"
  # To use the standard (non-realtime) kernel, set enabled to false
  realTimeKernel:
    enabled: true
  workloadHints:
    # WorkloadHints defines the set of upper level flags for different type of workloads.
    # See https://github.com/openshift/cluster-node-tuning-operator/blob/master/docs/performanceprofile/performance_profile.md#workloadhints
    # for detailed descriptions of each item.
    # The configuration below is set for a low latency, performance mode.
    realTime: true
    highPowerConsumption: false
    perPodPowerManagement: false
```


Table 7.3. PerformanceProfile CR options for single-node OpenShift clustersPerformanceProfile CR field| Description  
---|---  
`metadata.name` |  Ensure that `name` matches the following fields set in related GitOps ZTP custom resources (CRs): 

  * `include=openshift-node-performance-${PerformanceProfile.metadata.name}` in `TunedPerformancePatch.yaml`
  * `name: 50-performance-${PerformanceProfile.metadata.name}` in `validatorCRs/informDuValidator.yaml`

  
`spec.additionalKernelArgs` |  `"efi=runtime"` Configures UEFI secure boot for the cluster host.   
`spec.cpu.isolated` |  Set the isolated CPUs. Ensure all of the Hyper-Threading pairs match.  Important The reserved and isolated CPU pools must not overlap and together must span all available cores. CPU cores that are not accounted for cause an undefined behaviour in the system.   
`spec.cpu.reserved` |  Set the reserved CPUs. When workload partitioning is enabled, system processes, kernel threads, and system container threads are restricted to these CPUs. All CPUs that are not isolated should be reserved.   
`spec.hugepages.pages` | 

  * Set the number of huge pages (`count`) 
  * Set the huge pages size (`size`). 
  * Set `node` to the NUMA node where the `hugepages` are allocated (`node`) 

  
`spec.realTimeKernel` |  Set `enabled` to `true` to use the realtime kernel.   
`spec.workloadHints` |  Use `workloadHints` to define the set of top level flags for different type of workloads. The example configuration configures the cluster for low latency and high performance.   
Show more

## 7.7.5. Configuring cluster time synchronization

Run a one-time system time synchronization job for control plane or worker nodes. 

**Recommended one time time-sync for control plane nodes (`99-sync-time-once-master.yaml`)**

```yaml
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 99-sync-time-once-master
spec:
  config:
    ignition:
      version: 3.2.0
    systemd:
      units:
        - contents: |
            [Unit]
            Description=Sync time once
            After=network-online.target
            Wants=network-online.target
            [Service]
            Type=oneshot
            TimeoutStartSec=300
            ExecStart=/usr/sbin/chronyd -n -f /etc/chrony.conf -q
            RemainAfterExit=yes
            [Install]
            WantedBy=multi-user.target
          enabled: true
          name: chrony-wait.service
```


**Recommended one time time-sync for worker nodes (`99-sync-time-once-worker.yaml`)**

```yaml
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-sync-time-once-worker
spec:
  config:
    ignition:
      version: 3.2.0
    systemd:
      units:
        - contents: |
            [Unit]
            Description=Sync time once
            After=network-online.target
            Wants=network-online.target
            [Service]
            Type=oneshot
            TimeoutStartSec=300
            ExecStart=/usr/sbin/chronyd -n -f /etc/chrony.conf -q
            RemainAfterExit=yes
            [Install]
            WantedBy=multi-user.target
          enabled: true
          name: chrony-wait.service
```


## 7.7.6. PTP

Single-node OpenShift clusters use Precision Time Protocol (PTP) for network time synchronization. 

The following example `PtpConfig` custom resources (CRs) illustrate configurations for ordinary clocks, boundary clocks, and Telecom Grandmaster clocks on supported Intel Ethernet hardware. You must select the profile that matches your qualified GNR-D hardware layout and complete interface renaming prerequisites before you apply Granite Rapids-D Telecom Grandmaster YAML on Intel Granite Rapids-D servers. 

**Recommended PTP ordinary clock configuration (`PtpConfigSlave.yaml`)**

```yaml
apiVersion: ptp.openshift.io/v1
kind: PtpConfig
metadata:
  name: ordinary
  namespace: openshift-ptp
  annotations: {}
spec:
  profile:
    - name: "ordinary"
      # The interface name is hardware-specific
      interface: $interface
      ptp4lOpts: "-2 -s"
      phc2sysOpts: "-a -r -n 24"
      ptpSchedulingPolicy: SCHED_FIFO
      ptpSchedulingPriority: 10
      ptpSettings:
        logReduce: "true"
      ptp4lConf: |
        [global]
        #
        # Default Data Set
        #
        twoStepFlag 1
        slaveOnly 1
        priority1 128
        priority2 128
        domainNumber 24
        #utc_offset 37
        clockClass 255
        clockAccuracy 0xFE
        offsetScaledLogVariance 0xFFFF
        free_running 0
        freq_est_interval 1
        dscp_event 0
        dscp_general 0
        dataset_comparison G.8275.x
        G.8275.defaultDS.localPriority 128
        #
        # Port Data Set
        #
        logAnnounceInterval -3
        logSyncInterval -4
        logMinDelayReqInterval -4
        logMinPdelayReqInterval -4
        announceReceiptTimeout 3
        syncReceiptTimeout 0
        delayAsymmetry 0
        fault_reset_interval -4
        neighborPropDelayThresh 20000000
        masterOnly 0
        G.8275.portDS.localPriority 128
        #
        # Run time options
        #
        assume_two_step 0
        logging_level 6
        path_trace_enabled 0
        follow_up_info 0
        hybrid_e2e 0
        inhibit_multicast_service 0
        net_sync_monitor 0
        tc_spanning_tree 0
        tx_timestamp_timeout 50
        unicast_listen 0
        unicast_master_table 0
        unicast_req_duration 3600
        use_syslog 1
        verbose 0
        summary_interval 0
        kernel_leap 1
        check_fup_sync 0
        clock_class_threshold 7
        #
        # Servo Options
        #
        pi_proportional_const 0.0
        pi_integral_const 0.0
        pi_proportional_scale 0.0
        pi_proportional_exponent -0.3
        pi_proportional_norm_max 0.7
        pi_integral_scale 0.0
        pi_integral_exponent 0.4
        pi_integral_norm_max 0.3
        step_threshold 2.0
        first_step_threshold 0.00002
        max_frequency 900000000
        clock_servo pi
        sanity_freq_limit 200000000
        ntpshm_segment 0
        #
        # Transport options
        #
        transportSpecific 0x0
        ptp_dst_mac 01:1B:19:00:00:00
        p2p_dst_mac 01:80:C2:00:00:0E
        udp_ttl 1
        udp6_scope 0x0E
        uds_address /var/run/ptp4l
        #
        # Default interface options
        #
        clock_type OC
        network_transport L2
        delay_mechanism E2E
        time_stamping hardware
        tsproc_mode filter
        delay_filter moving_median
        delay_filter_length 10
        egressLatency 0
        ingressLatency 0
        boundary_clock_jbod 0
        #
        # Clock description
        #
        productDescription ;;
        revisionData ;;
        manufacturerIdentity 00:00:00
        userDescription ;
        timeSource 0xA0
  recommend:
    - profile: "ordinary"
      priority: 4
      match:
        - nodeLabel: "node-role.kubernetes.io/$mcp"
```


**Recommended boundary clock configuration (`PtpConfigBoundary.yaml`)**

```yaml
apiVersion: ptp.openshift.io/v1
kind: PtpConfig
metadata:
  name: boundary
  namespace: openshift-ptp
  annotations: {}
spec:
  profile:
    - name: "boundary"
      ptp4lOpts: "-2"
      phc2sysOpts: "-a -r -n 24"
      ptpSchedulingPolicy: SCHED_FIFO
      ptpSchedulingPriority: 10
      ptpSettings:
        logReduce: "true"
      ptp4lConf: |
        # The interface name is hardware-specific
        [$iface_slave]
        masterOnly 0
        [$iface_master_1]
        masterOnly 1
        [$iface_master_2]
        masterOnly 1
        [$iface_master_3]
        masterOnly 1
        [global]
        #
        # Default Data Set
        #
        twoStepFlag 1
        slaveOnly 0
        priority1 128
        priority2 128
        domainNumber 24
        #utc_offset 37
        clockClass 248
        clockAccuracy 0xFE
        offsetScaledLogVariance 0xFFFF
        free_running 0
        freq_est_interval 1
        dscp_event 0
        dscp_general 0
        dataset_comparison G.8275.x
        G.8275.defaultDS.localPriority 128
        #
        # Port Data Set
        #
        logAnnounceInterval -3
        logSyncInterval -4
        logMinDelayReqInterval -4
        logMinPdelayReqInterval -4
        announceReceiptTimeout 3
        syncReceiptTimeout 0
        delayAsymmetry 0
        fault_reset_interval -4
        neighborPropDelayThresh 20000000
        masterOnly 0
        G.8275.portDS.localPriority 128
        #
        # Run time options
        #
        assume_two_step 0
        logging_level 6
        path_trace_enabled 0
        follow_up_info 0
        hybrid_e2e 0
        inhibit_multicast_service 0
        net_sync_monitor 0
        tc_spanning_tree 0
        tx_timestamp_timeout 50
        unicast_listen 0
        unicast_master_table 0
        unicast_req_duration 3600
        use_syslog 1
        verbose 0
        summary_interval 0
        kernel_leap 1
        check_fup_sync 0
        clock_class_threshold 135
        #
        # Servo Options
        #
        pi_proportional_const 0.0
        pi_integral_const 0.0
        pi_proportional_scale 0.0
        pi_proportional_exponent -0.3
        pi_proportional_norm_max 0.7
        pi_integral_scale 0.0
        pi_integral_exponent 0.4
        pi_integral_norm_max 0.3
        step_threshold 2.0
        first_step_threshold 0.00002
        max_frequency 900000000
        clock_servo pi
        sanity_freq_limit 200000000
        ntpshm_segment 0
        #
        # Transport options
        #
        transportSpecific 0x0
        ptp_dst_mac 01:1B:19:00:00:00
        p2p_dst_mac 01:80:C2:00:00:0E
        udp_ttl 1
        udp6_scope 0x0E
        uds_address /var/run/ptp4l
        #
        # Default interface options
        #
        clock_type BC
        network_transport L2
        delay_mechanism E2E
        time_stamping hardware
        tsproc_mode filter
        delay_filter moving_median
        delay_filter_length 10
        egressLatency 0
        ingressLatency 0
        boundary_clock_jbod 0
        #
        # Clock description
        #
        productDescription ;;
        revisionData ;;
        manufacturerIdentity 00:00:00
        userDescription ;
        timeSource 0xA0
  recommend:
    - profile: "boundary"
      priority: 4
      match:
        - nodeLabel: "node-role.kubernetes.io/$mcp"
```


**Recommended PTP Westport Channel e810 grandmaster clock configuration (`PtpConfigGmWpc.yaml`)**

```yaml
# The grandmaster profile is provided for testing only
# It is not installed on production clusters
apiVersion: ptp.openshift.io/v1
kind: PtpConfig
metadata:
  name: grandmaster
  namespace: openshift-ptp
  annotations: {}
spec:
  profile:
    - name: "grandmaster"
      ptp4lOpts: "-2 --summary_interval -4"
      phc2sysOpts: -r -u 0 -m -w -N 8 -R 16 -s $iface_master -n 24
      ptpSchedulingPolicy: SCHED_FIFO
      ptpSchedulingPriority: 10
      ptpSettings:
        logReduce: "true"
      plugins:
        e810:
          enableDefaultConfig: false
          settings:
            LocalMaxHoldoverOffSet: 1500
            LocalHoldoverTimeout: 14400
            MaxInSpecOffset: 1500
          pins: $e810_pins
          #  "$iface_master":
          #    "U.FL2": "0 2"
          #    "U.FL1": "0 1"
          #    "SMA2": "0 2"
          #    "SMA1": "0 1"
          ublxCmds:
            - args: #ubxtool -P 29.20 -z CFG-HW-ANT_CFG_VOLTCTRL,1
                - "-P"
                - "29.20"
                - "-z"
                - "CFG-HW-ANT_CFG_VOLTCTRL,1"
              reportOutput: false
            - args: #ubxtool -P 29.20 -e GPS
                - "-P"
                - "29.20"
                - "-e"
                - "GPS"
              reportOutput: false
            - args: #ubxtool -P 29.20 -d Galileo
                - "-P"
                - "29.20"
                - "-d"
                - "Galileo"
              reportOutput: false
            - args: #ubxtool -P 29.20 -d GLONASS
                - "-P"
                - "29.20"
                - "-d"
                - "GLONASS"
              reportOutput: false
            - args: #ubxtool -P 29.20 -d BeiDou
                - "-P"
                - "29.20"
                - "-d"
                - "BeiDou"
              reportOutput: false
            - args: #ubxtool -P 29.20 -d SBAS
                - "-P"
                - "29.20"
                - "-d"
                - "SBAS"
              reportOutput: false
            - args: #ubxtool -P 29.20 -t -w 5 -v 1 -e SURVEYIN,600,50000
                - "-P"
                - "29.20"
                - "-t"
                - "-w"
                - "5"
                - "-v"
                - "1"
                - "-e"
                - "SURVEYIN,600,50000"
              reportOutput: true
            - args: #ubxtool -P 29.20 -p MON-HW
                - "-P"
                - "29.20"
                - "-p"
                - "MON-HW"
              reportOutput: true
            - args: #ubxtool -P 29.20 -p CFG-MSG,1,38,248
                - "-P"
                - "29.20"
                - "-p"
                - "CFG-MSG,1,38,248"
              reportOutput: true
      ts2phcOpts: " "
      ts2phcConf: |
        [nmea]
        ts2phc.master 1
        [global]
        use_syslog  0
        verbose 1
        logging_level 7
        ts2phc.pulsewidth 100000000
        #cat /dev/GNSS to find available serial port
        #example value of gnss_serialport is /dev/ttyGNSS_1700_0
        ts2phc.nmea_serialport $gnss_serialport
        leapfile  /usr/share/zoneinfo/leap-seconds.list
        [$iface_master]
        ts2phc.extts_polarity rising
        ts2phc.extts_correction 0
      ptp4lConf: |
        [$iface_master]
        masterOnly 1
        [$iface_master_1]
        masterOnly 1
        [$iface_master_2]
        masterOnly 1
        [$iface_master_3]
        masterOnly 1
        [global]
        #
        # Default Data Set
        #
        twoStepFlag 1
        priority1 128
        priority2 128
        domainNumber 24
        #utc_offset 37
        clockClass 6
        clockAccuracy 0x27
        offsetScaledLogVariance 0xFFFF
        free_running 0
        freq_est_interval 1
        dscp_event 0
        dscp_general 0
        dataset_comparison G.8275.x
        G.8275.defaultDS.localPriority 128
        #
        # Port Data Set
        #
        logAnnounceInterval -3
        logSyncInterval -4
        logMinDelayReqInterval -4
        logMinPdelayReqInterval 0
        announceReceiptTimeout 3
        syncReceiptTimeout 0
        delayAsymmetry 0
        fault_reset_interval -4
        neighborPropDelayThresh 20000000
        masterOnly 0
        G.8275.portDS.localPriority 128
        #
        # Run time options
        #
        assume_two_step 0
        logging_level 6
        path_trace_enabled 0
        follow_up_info 0
        hybrid_e2e 0
        inhibit_multicast_service 0
        net_sync_monitor 0
        tc_spanning_tree 0
        tx_timestamp_timeout 50
        unicast_listen 0
        unicast_master_table 0
        unicast_req_duration 3600
        use_syslog 1
        verbose 0
        summary_interval -4
        kernel_leap 1
        check_fup_sync 0
        clock_class_threshold 7
        #
        # Servo Options
        #
        pi_proportional_const 0.0
        pi_integral_const 0.0
        pi_proportional_scale 0.0
        pi_proportional_exponent -0.3
        pi_proportional_norm_max 0.7
        pi_integral_scale 0.0
        pi_integral_exponent 0.4
        pi_integral_norm_max 0.3
        step_threshold 2.0
        first_step_threshold 0.00002
        clock_servo pi
        sanity_freq_limit  200000000
        ntpshm_segment 0
        #
        # Transport options
        #
        transportSpecific 0x0
        ptp_dst_mac 01:1B:19:00:00:00
        p2p_dst_mac 01:80:C2:00:00:0E
        udp_ttl 1
        udp6_scope 0x0E
        uds_address /var/run/ptp4l
        #
        # Default interface options
        #
        clock_type BC
        network_transport L2
        delay_mechanism E2E
        time_stamping hardware
        tsproc_mode filter
        delay_filter moving_median
        delay_filter_length 10
        egressLatency 0
        ingressLatency 0
        boundary_clock_jbod 0
        #
        # Clock description
        #
        productDescription ;;
        revisionData ;;
        manufacturerIdentity 00:00:00
        userDescription ;
        timeSource 0x20
  recommend:
    - profile: "grandmaster"
      priority: 4
      match:
        - nodeLabel: "node-role.kubernetes.io/$mcp"
```


Important

Telecom Grandmaster clock configuration on Intel Granite Rapids-D (GNR-D) hardware is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Recommended PTP Granite Rapids-D Telecom Grandmaster clock configuration (`PtpConfigGnrdTGM.yaml`)**

```yaml
# Example Telecom Grandmaster PtpConfig for Intel Granite Rapids-D (GNR-D).
#
# Note:  This example configuration should be customized to match the desired
# configuration For this GNR-D T-GM configuration, we support GNSS incoming to
# the onboard connection, and up to 24 Time Transmitter ports including any NAC
# ports and any additional Carter Flats ports.
apiVersion: ptp.openshift.io/v1
kind: PtpConfig
metadata:
  name: gnrd-tgm
  namespace: openshift-ptp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "10"
spec:
  profile:
    - name: "grandmaster"
      ptp4lOpts: "-2 --summary_interval -4"
      phc2sysOpts: -r -u 0 -m -w -N 8 -R 16 -n 24 -s eno8703
      ptpSchedulingPolicy: SCHED_FIFO
      ptpSchedulingPriority: 10
      ptpSettings:
        logReduce: "true"
      plugins:
        e830:
          devices:
            - enp108s0f0
            - enp110s0f0
        e825:
          devices:
            - eno8703
          settings:
            LocalMaxHoldoverOffSet: 1500
            LocalHoldoverTimeout: 14400
            MaxInSpecOffset: 100
          ublxCmds:
            - args: #ubxtool -P 29.25 -z CFG-HW-ANT_CFG_VOLTCTRL,1
                - "-P"
                - "29.25"
                - "-z"
                - "CFG-HW-ANT_CFG_VOLTCTRL,1"
              reportOutput: false
            - args: #ubxtool -P 29.25 -e GPS
                - "-P"
                - "29.25"
                - "-e"
                - "GPS"
              reportOutput: false
            - args: #ubxtool -P 29.25 -d Galileo
                - "-P"
                - "29.25"
                - "-d"
                - "Galileo"
              reportOutput: false
            - args: #ubxtool -P 29.25 -d GLONASS
                - "-P"
                - "29.25"
                - "-d"
                - "GLONASS"
              reportOutput: false
            - args: #ubxtool -P 29.25 -d BeiDou
                - "-P"
                - "29.25"
                - "-d"
                - "BeiDou"
              reportOutput: false
            - args: #ubxtool -P 29.25 -d SBAS
                - "-P"
                - "29.25"
                - "-d"
                - "SBAS"
              reportOutput: false
            - args: #ubxtool -P 29.25 -t -w 5 -v 1 -e SURVEYIN,600,50000
                - "-P"
                - "29.25"
                - "-t"
                - "-w"
                - "5"
                - "-v"
                - "1"
                - "-e"
                - "SURVEYIN,600,50000"
              reportOutput: true
            - args: #ubxtool -P 29.25 -p MON-HW
                - "-P"
                - "29.25"
                - "-p"
                - "MON-HW"
              reportOutput: true
            - args: #ubxtool -P 29.25 -p CFG-MSG,1,38,300
                - "-P"
                - "29.25"
                - "-p"
                - "CFG-MSG,1,38,248"
              reportOutput: true
      ts2phcOpts: "-m"
      ts2phcConf: |
        [nmea]
        ts2phc.master 1
        [global]
        use_syslog  0
        verbose 1
        logging_level 7
        ts2phc.pulsewidth 100000000
        ts2phc.nmea_serialport /dev/ttyACM0
        [eno8703]
        ts2phc.extts_polarity rising
        ts2phc.extts_correction 0
        ts2phc.master  0
        ts2phc.channel 0
        ts2phc.pin_index 1
        # This should be one section per Carter Flats (e830) card:
        [enp108s0f0]
        ts2phc.extts_polarity rising
        ts2phc.extts_correction 0
        ts2phc.master 0
        ts2phc.channel 0
        ts2phc.pin_index 1
        [enp110s0f0]
        ts2phc.extts_polarity rising
        ts2phc.extts_correction 0
        ts2phc.master 0
        ts2phc.channel 0
        ts2phc.pin_index 1
      ptp4lConf: |
        # All TimeTransmitter ports should be outlined here with 'masterOnly 1'
        #[eno8303]
        # ** Host management interface
        [eno8403]
        masterOnly 1
        [eno8503]
        masterOnly 1
        [eno8603]
        masterOnly 1
        [eno8703]
        masterOnly 1
        [eno8803]
        masterOnly 1
        [eno8903]
        masterOnly 1
        [eno9003]
        masterOnly 1
        [enp108s0f0]
        masterOnly 1
        [enp108s0f1]
        masterOnly 1
        [enp108s0f2]
        masterOnly 1
        [enp108s0f3]
        masterOnly 1
        [enp108s0f4]
        masterOnly 1
        [enp108s0f5]
        masterOnly 1
        [enp108s0f6]
        masterOnly 1
        [enp108s0f7]
        masterOnly 1
        [enp110s0f0]
        masterOnly 1
        [enp110s0f1]
        masterOnly 1
        [enp110s0f2]
        masterOnly 1
        [enp110s0f3]
        masterOnly 1
        [enp110s0f4]
        masterOnly 1
        [enp110s0f5]
        masterOnly 1
        [enp110s0f6]
        masterOnly 1
        [enp110s0f7]
        masterOnly 1
        [global]
        #
        # Default Data Set
        #
        twoStepFlag 1
        priority1 128
        priority2 128
        domainNumber 24
        #utc_offset 37
        clockClass 6
        clockAccuracy 0x27
        offsetScaledLogVariance 0xFFFF
        free_running 0
        freq_est_interval 1
        dscp_event 0
        dscp_general 0
        dataset_comparison G.8275.x
        G.8275.defaultDS.localPriority 128
        #
        # Port Data Set
        #
        logAnnounceInterval -3
        logSyncInterval -4
        logMinDelayReqInterval -4
        logMinPdelayReqInterval 0
        announceReceiptTimeout 3
        syncReceiptTimeout 0
        delayAsymmetry 0
        fault_reset_interval 4
        neighborPropDelayThresh 20000000
        masterOnly 0
        G.8275.portDS.localPriority 128
        #
        # Run time options
        #
        assume_two_step 0
        logging_level 6
        path_trace_enabled 0
        follow_up_info 0
        hybrid_e2e 0
        inhibit_multicast_service 0
        net_sync_monitor 0
        tc_spanning_tree 0
        tx_timestamp_timeout 50
        unicast_listen 0
        unicast_master_table 0
        unicast_req_duration 3600
        use_syslog 1
        verbose 0
        summary_interval -4
        kernel_leap 1
        check_fup_sync 0
        #
        # Servo Options
        #
        pi_proportional_const 0.0
        pi_integral_const 0.0
        pi_proportional_scale 0.0
        pi_proportional_exponent -0.3
        pi_proportional_norm_max 0.7
        pi_integral_scale 0.0
        pi_integral_exponent 0.4
        pi_integral_norm_max 0.3
        step_threshold 0.0
        first_step_threshold 0.00002
        clock_servo pi
        sanity_freq_limit  200000000
        ntpshm_segment 0
        #
        # Transport options
        #
        transportSpecific 0x0
        ptp_dst_mac 01:1B:19:00:00:00
        p2p_dst_mac 01:80:C2:00:00:0E
        udp_ttl 1
        udp6_scope 0x0E
        uds_address /var/run/ptp4l
        #
        # Default interface options
        #
        clock_type BC
        network_transport L2
        delay_mechanism E2E
        time_stamping hardware
        tsproc_mode filter
        delay_filter moving_median
        delay_filter_length 10
        egressLatency 0
        ingressLatency 0
        boundary_clock_jbod 1
        #
        # Clock description
        #
        productDescription ;;
        revisionData ;;
        manufacturerIdentity 00:00:00
        userDescription ;
        timeSource 0x20
  recommend:
    - match:
      - nodeLabel: node-role.kubernetes.io/$mcp
      priority: 4
      profile: grandmaster
```


The following optional `PtpOperatorConfig` CR configures PTP events reporting for the node. 

**Recommended PTP events configuration (`PtpOperatorConfigForEvent.yaml`)**

```yaml
apiVersion: ptp.openshift.io/v1
kind: PtpOperatorConfig
metadata:
  name: default
  namespace: openshift-ptp
  annotations: {}
spec:
  daemonNodeSelector:
    node-role.kubernetes.io/$mcp: ""
  ptpEventConfig:
    apiVersion: $event_api_version
    enableEventPublisher: true
    transportHost: "http://ptp-event-publisher-service-NODE_NAME.openshift-ptp.svc.cluster.local:9043"
```


**Additional resources**

  * [Configuring linuxptp services as a Telecom Grandmaster clock on Intel Granite Rapids-D hardware](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/advanced_networking/#configuring-linuxptp-services-as-grandmaster-clock-gnrd_configuring-ptp)



## 7.7.7. Extended Tuned profile

Single-node OpenShift clusters that run DU workloads require additional performance tuning configurations necessary for high-performance workloads. The following example `Tuned` CR extends the `Tuned` profile: 

**Recommended extended`Tuned` profile configuration (`TunedPerformancePatch.yaml`)**

```yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: performance-patch
  namespace: openshift-cluster-node-tuning-operator
  annotations: {}
spec:
  profile:
    - name: performance-patch
      # Please note:
      # - The 'include' line must match the associated PerformanceProfile name, following below pattern
      #   include=openshift-node-performance-${PerformanceProfile.metadata.name}
      # - When using the standard (non-realtime) kernel, remove the kernel.timer_migration override from
      #   the [sysctl] section and remove the entire section if it is empty.
      data: |
        [main]
        summary=Configuration changes profile inherited from performance created tuned
        include=openshift-node-performance-openshift-node-performance-profile
        [scheduler]
        group.ice-ptp=0:f:10:*:ice-ptp.*
        group.ice-gnss=0:f:10:*:ice-gnss.*
        group.ice-dplls=0:f:10:*:ice-dplls.*
        [service]
        service.stalld=start,enable
        service.chronyd=stop,disable
  recommend:
    - machineConfigLabels:
        machineconfiguration.openshift.io/role: "$mcp"
      priority: 19
      profile: performance-patch
```


Table 7.4. Tuned CR options for single-node OpenShift clustersTuned CR field| Description  
---|---  
`spec.profile.data` | 

  * The `include` line that you set in `spec.profile.data` must match the associated `PerformanceProfile` CR name. For example, `include=openshift-node-performance-${PerformanceProfile.metadata.name}`. 

  
Show more

## 7.7.8. SR-IOV

Single root I/O virtualization (SR-IOV) is commonly used to enable fronthaul and midhaul networks. The following YAML example configures SR-IOV for a single-node OpenShift cluster. 

Note

The configuration of the `SriovNetwork` CR will vary depending on your specific network and infrastructure requirements. 

**Recommended`SriovOperatorConfig` CR configuration (`SriovOperatorConfig.yaml`)**

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
  annotations: {}
spec:
  configDaemonNodeSelector:
    "node-role.kubernetes.io/$mcp": ""
  # Injector and OperatorWebhook pods can be disabled (set to "false") below
  # to reduce the number of management pods. It is recommended to start with the
  # webhook and injector pods enabled, and only disable them after verifying the
  # correctness of user manifests.
  #   If the injector is disabled, containers using sr-iov resources must explicitly assign
  #   them in the  "requests"/"limits" section of the container spec, for example:
  #    containers:
  #    - name: my-sriov-workload-container
  #      resources:
  #        limits:
  #          openshift.io/<resource_name>:  "1"
  #        requests:
  #          openshift.io/<resource_name>:  "1"
  enableInjector: false
  enableOperatorWebhook: false
  logLevel: 0
```


Table 7.5. SriovOperatorConfig CR options for single-node OpenShift clustersSriovOperatorConfig CR field| Description  
---|---  
`spec.enableInjector` |  Disable `Injector` pods to reduce the number of management pods. Start with the `Injector` pods enabled, and only disable them after verifying the user manifests. If the injector is disabled, containers that use SR-IOV resources must explicitly assign them in the `requests` and `limits` section of the container spec.  For example:  `containers: - name: my-sriov-workload-container resources: limits: openshift.io/<resource_name>: "1" requests: openshift.io/<resource_name>: "1"`  
`spec.enableOperatorWebhook` |  Disable `OperatorWebhook` pods to reduce the number of management pods. Start with the `OperatorWebhook` pods enabled, and only disable them after verifying the user manifests.   
Show more

**Recommended`SriovNetwork` configuration (`SriovNetwork.yaml`)**

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: ""
  namespace: openshift-sriov-network-operator
  annotations: {}
spec:
  #  resourceName: ""
  networkNamespace: openshift-sriov-network-operator
#  vlan: ""
#  spoofChk: ""
#  ipam: ""
#  linkState: ""
#  maxTxRate: ""
#  minTxRate: ""
#  vlanQoS: ""
#  trust: ""
#  capabilities: ""
```


Table 7.6. SriovNetwork CR options for single-node OpenShift clustersSriovNetwork CR field| Description  
---|---  
`spec.vlan` |  Configure `vlan` with the VLAN for the midhaul network.   
Show more

**Recommended`SriovNetworkNodePolicy` CR configuration (`SriovNetworkNodePolicy.yaml`)**

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: $name
  namespace: openshift-sriov-network-operator
  annotations: {}
spec:
  # The attributes for Mellanox/Intel based NICs as below.
  #     deviceType: netdevice/vfio-pci
  #     isRdma: true/false
  deviceType: $deviceType
  isRdma: $isRdma
  nicSelector:
    # The exact physical function name must match the hardware used
    pfNames: [$pfNames]
  nodeSelector:
    node-role.kubernetes.io/$mcp: ""
  numVfs: $numVfs
  priority: $priority
  resourceName: $resourceName
```


Table 7.7. SriovNetworkPolicy CR options for single-node OpenShift clustersSriovNetworkNodePolicy CR field| Description  
---|---  
`spec.deviceType` |  Configure `deviceType` as `vfio-pci` or `netdevice`. For Mellanox NICs, set `deviceType: netdevice`, and `isRdma: true`. For Intel based NICs, set `deviceType: vfio-pci` and `isRdma: false`.   
`spec.nicSelector.pfNames` |  Specifies the interface connected to the fronthaul network.   
`spec.numVfs` |  Specifies the number of VFs for the fronthaul network.   
`spec.nicSelector.pfNames` |  The exact name of physical function must match the hardware.   
Show more

**Recommended SR-IOV kernel configurations (`07-sriov-related-kernel-args-master.yaml`)**

```yaml
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 07-sriov-related-kernel-args-master
spec:
  config:
    ignition:
      version: 3.2.0
  kernelArguments:
    - intel_iommu=on
    - iommu=pt
```


## 7.7.9. Console Operator

Use the cluster capabilities feature to prevent the Console Operator from being installed. When the node is centrally managed it is not needed. Removing the Operator provides additional space and capacity for application workloads. 

To disable the Console Operator during the installation of the managed cluster, set the following in the `spec.installConfigOverrides` field of the `ClusterInstance` custom resource (CR): 

```yaml
installConfigOverrides:  "{\"capabilities\":{\"baselineCapabilitySet\": \"None\" }}"
```


## 7.7.10. Alertmanager

Single-node OpenShift clusters that run DU workloads require reduced CPU resources consumed by the OpenShift Container Platform monitoring components. The following `ConfigMap` custom resource (CR) disables Alertmanager. 

**Recommended cluster monitoring configuration (`ReduceMonitoringFootprint.yaml`)**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
  annotations: {}
data:
  config.yaml: |
    alertmanagerMain:
      enabled: false
    telemeterClient:
      enabled: false
    prometheusK8s:
       retention: 24h
```


## 7.7.11. Operator Lifecycle Manager

Single-node OpenShift clusters that run distributed unit workloads require consistent access to CPU resources. 

Operator Lifecycle Manager (OLM) collects performance data from Operators at regular intervals, resulting in an increase in CPU utilisation. The following `ConfigMap` custom resource (CR) disables the collection of Operator performance data by OLM. 

**Recommended cluster OLM configuration (`ReduceOLMFootprint.yaml`)**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: collect-profiles-config
  namespace: openshift-operator-lifecycle-manager
data:
  pprof-config.yaml: |
    disabled: True
```


## 7.7.12. LVM Storage

You can dynamically provision local storage on single-node OpenShift clusters with Logical Volume Manager (LVM) Storage. 

Note

The recommended storage solution for single-node OpenShift is the Local Storage Operator. Alternatively, you can use LVM Storage but it requires additional CPU resources to be allocated. 

The following YAML example configures the storage of the node to be available to OpenShift Container Platform applications. 

**Recommended`LVMCluster` configuration (`StorageLVMCluster.yaml`)**

```yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: lvmcluster
  namespace: openshift-storage
  annotations: {}
spec: {}
#example: creating a vg1 volume group leveraging all available disks on the node
#         except the installation disk.
#  storage:
#    deviceClasses:
#    - name: vg1
#      thinPoolConfig:
#        name: thin-pool-1
#        sizePercent: 90
#        overprovisionRatio: 10
```


Table 7.8. LVMCluster CR options for single-node OpenShift clustersLVMCluster CR field| Description  
---|---  
`deviceSelector.paths` |  Configure the disks used for LVM storage. If no disks are specified, the LVM Storage uses all the unused disks in the specified thin pool.   
Show more

## 7.7.13. Network diagnostics

Single-node OpenShift clusters that run DU workloads require less inter-pod network connectivity checks to reduce the additional load created by these pods. The following custom resource (CR) disables these checks. 

**Recommended network diagnostics configuration (`DisableSnoNetworkDiag.yaml`)**

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
  annotations: {}
spec:
  disableNetworkDiagnostics: true
```


**Additional resources**

  * [Deploying far edge sites using ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites "Chapter 4. Installing managed clusters with RHACM and ClusterInstance resources")
