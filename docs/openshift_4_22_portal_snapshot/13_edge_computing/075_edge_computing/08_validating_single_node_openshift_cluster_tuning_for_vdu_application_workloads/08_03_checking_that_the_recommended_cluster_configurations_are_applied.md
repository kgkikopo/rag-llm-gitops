# 8.3. Checking that the recommended cluster configurations are applied

You can check that clusters are running the correct configuration. The following procedure describes how to check the various configurations that you require to deploy a DU application in OpenShift Container Platform 4.22 clusters. 

**Prerequisites**

  * You have deployed a cluster and tuned it for vDU workloads. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Check that the default OperatorHub sources are disabled. Run the following command: 

```shell-session
$ oc get operatorhub cluster -o yaml
```


The following example output shows that all default sources are disabled: 

```yaml
spec:
    disableAllDefaultSources: true
```


  2. Check that all required `CatalogSource` resources are annotated for workload partitioning (`PreferredDuringScheduling`) by running the following command: 

```shell-session
$ oc get catalogsource -A -o jsonpath='{range .items[*]}{.metadata.name}{" -- "}{.metadata.annotations.target\.workload\.openshift\.io/management}{"\n"}{end}'
```


```shell-session
certified-operators -- {"effect": "PreferredDuringScheduling"}
community-operators -- {"effect": "PreferredDuringScheduling"}
ran-operators --
redhat-marketplace -- {"effect": "PreferredDuringScheduling"}
redhat-operators -- {"effect": "PreferredDuringScheduling"}
```


In this output, `CatalogSource` resources that are not annotated are also returned. The `ran-operators` `CatalogSource` resource is not annotated and does not have the `PreferredDuringScheduling` annotation. 

Note

In a properly configured vDU cluster, only a single annotated catalog source is listed. 

  3. Check that all applicable OpenShift Container Platform Operator namespaces are annotated for workload partitioning. This includes all Operators installed with core OpenShift Container Platform and the set of additional Operators included in the reference DU tuning configuration. Run the following command: 

```shell-session
$ oc get namespaces -A -o jsonpath='{range .items[*]}{.metadata.name}{" -- "}{.metadata.annotations.workload\.openshift\.io/allowed}{"\n"}{end}'
```


```shell-session
default --
openshift-apiserver -- management
openshift-apiserver-operator -- management
openshift-authentication -- management
openshift-authentication-operator -- management
```


Important

Additional Operators must not be annotated for workload partitioning. In the output from the previous command, additional Operators should be listed without any value on the right side of the `--` separator. 

  4. Check that the `ClusterLogging` configuration is correct. Run the following commands: 

     1. Validate that the appropriate input and output logs are configured: 

```shell-session
$ oc get -n openshift-logging ClusterLogForwarder instance -o yaml
```


```yaml
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  creationTimestamp: "2022-07-19T21:51:41Z"
  generation: 1
  name: instance
  namespace: openshift-logging
  resourceVersion: "1030342"
  uid: 8c1a842d-80c5-447a-9150-40350bdf40f0
spec:
  inputs:
  - infrastructure: {}
    name: infra-logs
  outputs:
  - name: kafka-open
    type: kafka
    url: tcp://10.46.55.190:9092/test
  pipelines:
  - inputRefs:
    - audit
    name: audit-logs
    outputRefs:
    - kafka-open
  - inputRefs:
    - infrastructure
    name: infrastructure-logs
    outputRefs:
    - kafka-open
...
```


     2. Check that the curation schedule is appropriate for your application: 

```shell-session
$ oc get -n openshift-logging clusterloggings.logging.openshift.io instance -o yaml
```


```yaml
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  creationTimestamp: "2022-07-07T18:22:56Z"
  generation: 1
  name: instance
  namespace: openshift-logging
  resourceVersion: "235796"
  uid: ef67b9b8-0e65-4a10-88ff-ec06922ea796
spec:
  collection:
    logs:
      fluentd: {}
      type: fluentd
  curation:
    curator:
      schedule: 30 3 * * *
    type: curator
  managementState: Managed
...
```


  5. Check that the web console is disabled (`managementState: Removed`) by running the following command: 

```shell-session
$ oc get consoles.operator.openshift.io cluster -o jsonpath="{ .spec.managementState }"
```


```shell-session
Removed
```


  6. Check that `chronyd` is disabled on the cluster node by running the following commands: 

```shell-session
$ oc debug node/<node_name>
```


Check the status of `chronyd` on the node: 

```shell-session
sh-4.4# chroot /host
```


```shell-session
sh-4.4# systemctl status chronyd
```


```shell-session
● chronyd.service - NTP client/server
    Loaded: loaded (/usr/lib/systemd/system/chronyd.service; disabled; vendor preset: enabled)
    Active: inactive (dead)
      Docs: man:chronyd(8)
            man:chrony.conf(5)
```


  7. Check that the PTP interface is successfully synchronized to the primary clock using a remote shell connection to the `linuxptp-daemon` container and the PTP Management Client (`pmc`) tool: 

     1. Set the `$PTP_POD_NAME` variable with the name of the `linuxptp-daemon` pod by running the following command: 

```shell-session
$ PTP_POD_NAME=$(oc get pods -n openshift-ptp -l app=linuxptp-daemon -o name)
```


     2. Run the following command to check the sync status of the PTP device: 

```shell-session
$ oc -n openshift-ptp rsh -c linuxptp-daemon-container ${PTP_POD_NAME} pmc -u -f /var/run/ptp4l.0.config -b 0 'GET PORT_DATA_SET'
```


```shell-session
sending: GET PORT_DATA_SET
  3cecef.fffe.7a7020-1 seq 0 RESPONSE MANAGEMENT PORT_DATA_SET
    portIdentity            3cecef.fffe.7a7020-1
    portState               SLAVE
    logMinDelayReqInterval  -4
    peerMeanPathDelay       0
    logAnnounceInterval     1
    announceReceiptTimeout  3
    logSyncInterval         0
    delayMechanism          1
    logMinPdelayReqInterval 0
    versionNumber           2
  3cecef.fffe.7a7020-2 seq 0 RESPONSE MANAGEMENT PORT_DATA_SET
    portIdentity            3cecef.fffe.7a7020-2
    portState               LISTENING
    logMinDelayReqInterval  0
    peerMeanPathDelay       0
    logAnnounceInterval     1
    announceReceiptTimeout  3
    logSyncInterval         0
    delayMechanism          1
    logMinPdelayReqInterval 0
    versionNumber           2
```


     3. Run the following `pmc` command to check the PTP clock status: 

```shell-session
$ oc -n openshift-ptp rsh -c linuxptp-daemon-container ${PTP_POD_NAME} pmc -u -f /var/run/ptp4l.0.config -b 0 'GET TIME_STATUS_NP'
```


```shell-session
sending: GET TIME_STATUS_NP
  3cecef.fffe.7a7020-0 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
    master_offset              10
    ingress_time               1657275432697400530
    cumulativeScaledRateOffset +0.000000000
    scaledLastGmPhaseChange    0
    gmTimeBaseIndicator        0
    lastGmPhaseChange          0x0000'0000000000000000.0000
    gmPresent                  true
    gmIdentity                 3c2c30.ffff.670e00
```


In this output: 

        * `master_offset` should be between -100 and 100 ns. 
        * `gmPresent` indicates that the PTP clock is synchronized to a primary clock, and the local clock is not the grandmaster clock. 

     4. Check that the expected `master offset` value corresponding to the value in `/var/run/ptp4l.0.config` is found in the `linuxptp-daemon-container` log: 

```shell-session
$ oc logs $PTP_POD_NAME -n openshift-ptp -c linuxptp-daemon-container
```


```shell-session
phc2sys[56020.341]: [ptp4l.1.config] CLOCK_REALTIME phc offset  -1731092 s2 freq -1546242 delay    497
ptp4l[56020.390]: [ptp4l.1.config] master offset         -2 s2 freq   -5863 path delay       541
ptp4l[56020.390]: [ptp4l.0.config] master offset         -8 s2 freq  -10699 path delay       533
```


  8. Check that the SR-IOV configuration is correct by running the following commands: 

     1. Check that the `disableDrain` value in the `SriovOperatorConfig` resource is set to `true`: 

```shell-session
$ oc get sriovoperatorconfig -n openshift-sriov-network-operator default -o jsonpath="{.spec.disableDrain}{'\n'}"
```


```shell-session
true
```


     2. Check that the `SriovNetworkNodeState` sync status is `Succeeded` by running the following command: 

```shell-session
$ oc get SriovNetworkNodeStates -n openshift-sriov-network-operator -o jsonpath="{.items[*].status.syncStatus}{'\n'}"
```


```shell-session
Succeeded
```


     3. Verify that the expected number and configuration of virtual functions (`Vfs`) under each interface configured for SR-IOV is present and correct in the `.status.interfaces` field. For example: 

```shell-session
$ oc get SriovNetworkNodeStates -n openshift-sriov-network-operator -o yaml
```


```yaml
apiVersion: v1
items:
- apiVersion: sriovnetwork.openshift.io/v1
  kind: SriovNetworkNodeState
...
  status:
    interfaces:
    ...
    - Vfs:
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.0
        vendor: "8086"
        vfID: 0
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.1
        vendor: "8086"
        vfID: 1
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.2
        vendor: "8086"
        vfID: 2
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.3
        vendor: "8086"
        vfID: 3
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.4
        vendor: "8086"
        vfID: 4
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.5
        vendor: "8086"
        vfID: 5
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.6
        vendor: "8086"
        vfID: 6
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.7
        vendor: "8086"
        vfID: 7
```


  9. Check that the cluster performance profile is correct. The `cpu` and `hugepages` sections will vary depending on your hardware configuration. Run the following command: 

```shell-session
$ oc get PerformanceProfile openshift-node-performance-profile -o yaml
```


```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  creationTimestamp: "2022-07-19T21:51:31Z"
  finalizers:
  - foreground-deletion
  generation: 1
  name: openshift-node-performance-profile
  resourceVersion: "33558"
  uid: 217958c0-9122-4c62-9d4d-fdc27c31118c
spec:
  additionalKernelArgs:
  - idle=poll
  - rcupdate.rcu_normal_after_boot=0
  - efi=runtime
  cpu:
    isolated: 2-51,54-103
    reserved: 0-1,52-53
  hugepages:
    defaultHugepagesSize: 1G
    pages:
    - count: 32
      size: 1G
  machineConfigPoolSelector:
    pools.operator.machineconfiguration.openshift.io/master: ""
  net:
    userLevelNetworking: true
  nodeSelector:
    node-role.kubernetes.io/master: ""
  numa:
    topologyPolicy: restricted
  realTimeKernel:
    enabled: true
status:
  conditions:
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "True"
    type: Available
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "True"
    type: Upgradeable
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "False"
    type: Progressing
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "False"
    type: Degraded
  runtimeClass: performance-openshift-node-performance-profile
  tuned: openshift-cluster-node-tuning-operator/openshift-node-performance-openshift-node-performance-profile
```


Note

CPU settings are dependent on the number of cores available on the server and should align with workload partitioning settings. `hugepages` configuration is server and application dependent. 

  10. Check that the `PerformanceProfile` was successfully applied to the cluster by running the following command: 

```shell-session
$ oc get performanceprofile openshift-node-performance-profile -o jsonpath="{range .status.conditions[*]}{ @.type }{' -- '}{@.status}{'\n'}{end}"
```


```shell-session
Available -- True
Upgradeable -- True
Progressing -- False
Degraded -- False
```


  11. Check the `Tuned` performance patch settings by running the following command: 

```shell-session
$ oc get tuneds.tuned.openshift.io -n openshift-cluster-node-tuning-operator performance-patch -o yaml
```


```yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  creationTimestamp: "2022-07-18T10:33:52Z"
  generation: 1
  name: performance-patch
  namespace: openshift-cluster-node-tuning-operator
  resourceVersion: "34024"
  uid: f9799811-f744-4179-bf00-32d4436c08fd
spec:
  profile:
  - data: |
      [main]
      summary=Configuration changes profile inherited from performance created tuned
      include=openshift-node-performance-openshift-node-performance-profile
      [bootloader]
      cmdline_crash=nohz_full=2-23,26-47
      [sysctl]
      kernel.timer_migration=1
      [scheduler]
      group.ice-ptp=0:f:10:*:ice-ptp.*
      [service]
      service.stalld=start,enable
      service.chronyd=stop,disable
    name: performance-patch
  recommend:
  - machineConfigLabels:
      machineconfiguration.openshift.io/role: master
    priority: 19
    profile: performance-patch
```


The CPU list in `cmdline=nohz_full=` will vary based on your hardware configuration. 

  12. Check that cluster networking diagnostics are disabled by running the following command: 

```shell-session
$ oc get networks.operator.openshift.io cluster -o jsonpath='{.spec.disableNetworkDiagnostics}'
```


```shell-session
true
```


  13. Check that the `Kubelet` housekeeping interval is tuned to slower rate. This is set in the `containerMountNS` machine config. Run the following command: 

```shell-session
$ oc describe machineconfig container-mount-namespace-and-kubelet-conf-master | grep OPENSHIFT_MAX_HOUSEKEEPING_INTERVAL_DURATION
```


```shell-session
Environment="OPENSHIFT_MAX_HOUSEKEEPING_INTERVAL_DURATION=60s"
```


  14. Check that Grafana and `alertManagerMain` are disabled and that the Prometheus retention period is set to 24h by running the following command: 

```shell-session
$ oc get configmap cluster-monitoring-config -n openshift-monitoring -o jsonpath="{ .data.config\.yaml }"
```


```shell-session
grafana:
  enabled: false
alertmanagerMain:
  enabled: false
prometheusK8s:
   retention: 24h
```


     1. Use the following commands to verify that Grafana and `alertManagerMain` routes are not found in the cluster: 

```shell-session
$ oc get route -n openshift-monitoring alertmanager-main
```


```shell-session
$ oc get route -n openshift-monitoring grafana
```


Both queries should return `Error from server (NotFound)` messages. 

  15. Check that there is a minimum of 4 CPUs allocated as `reserved` for each of the `PerformanceProfile`, `Tuned` performance-patch, workload partitioning, and kernel command-line arguments by running the following command: 

```shell-session
$ oc get performanceprofile -o jsonpath="{ .items[0].spec.cpu.reserved }"
```


```shell-session
0-3
```


Note

Depending on your workload requirements, you might require additional reserved CPUs to be allocated.
