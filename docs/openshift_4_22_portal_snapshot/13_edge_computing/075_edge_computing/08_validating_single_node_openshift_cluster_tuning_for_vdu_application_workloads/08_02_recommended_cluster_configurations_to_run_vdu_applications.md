# 8.2. Recommended cluster configurations to run vDU applications

Clusters running virtualized distributed unit (vDU) applications require a highly tuned and optimized configuration. The following information describes the various elements that you require to support vDU workloads in OpenShift Container Platform 4.22 clusters. 

## 8.2.1. Recommended cluster MachineConfig CRs for single-node OpenShift clusters

Check that the `MachineConfig` custom resources (CRs) that you extract from the `ztp-site-generate` container are applied in the cluster. The CRs can be found in the extracted `out/source-crs/extra-manifest/` folder. 

The following `MachineConfig` CRs from the `ztp-site-generate` container configure the cluster host: 

Table 8.2. Recommended GitOps ZTP MachineConfig CRsMachineConfig CR| Description  
---|---  
`01-container-mount-ns-and-kubelet-conf-master.yaml` `01-container-mount-ns-and-kubelet-conf-worker.yaml` |  Configures the container mount namespace and kubelet configuration.   
`03-sctp-machine-config-master.yaml` `03-sctp-machine-config-worker.yaml` |  Loads the SCTP kernel module. These `MachineConfig` CRs are optional and can be omitted if you do not require this kernel module.   
`06-kdump-master.yaml` `06-kdump-worker.yaml` |  Configures kdump crash reporting for the cluster.   
`07-sriov-related-kernel-args-master.yaml` |  Configures SR-IOV kernel arguments in the cluster.   
`08-set-rcu-normal-master.yaml` `08-set-rcu-normal-worker.yaml` |  Disables `rcu_expedited` mode after the cluster has rebooted.   
`99-crio-disable-wipe-master.yaml` `99-crio-disable-wipe-worker.yaml` |  Disables the automatic CRI-O cache wipe following cluster reboot.   
`99-sync-time-once-master.yaml` `99-sync-time-once-worker.yaml` |  Configures the one-time check and adjustment of the system clock by the Chrony service.   
`enable-crun-master.yaml` `enable-crun-worker.yaml` |  Enables the `crun` OCI container runtime.   
`extra-manifest/enable-cgroups-v1.yaml` `source-crs/extra-manifest/enable-cgroups-v1.yaml` |  Enables cgroups v1 during cluster installation and when generating RHACM cluster policies.   
Show more

Note

In OpenShift Container Platform 4.14 and later, you configure workload partitioning with the `cpuPartitioningMode` field in the `ClusterInstance` CR. 

**Additional resources**

  * [Workload partitioning in single-node OpenShift with GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/sno-configure-for-vdu#ztp-workload-partitioning-sno_sno-configure-for-vdu "7.5. Workload partitioning in single-node OpenShift with GitOps ZTP")
  * [Extracting source CRs from the ztp-site-generate container](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-preparing-the-hub-cluster#ztp-preparing-the-ztp-git-repository_ztp-preparing-the-hub-cluster "2.9. Prepare the GitOps ZTP site configuration repository")



## 8.2.2. Recommended cluster Operators

The following Operators are required for clusters running virtualized distributed unit (vDU) applications and are a part of the baseline reference configuration: 

  * Node Tuning Operator (NTO). NTO packages functionality that was previously delivered with the Performance Addon Operator, which is now a part of NTO. 
  * PTP Operator 
  * SR-IOV Network Operator 
  * Red Hat OpenShift Logging Operator 
  * Local Storage Operator 



## 8.2.3. Recommended cluster kernel configuration

Always use the latest supported real-time kernel version in your cluster. Ensure that you apply the following configurations in the cluster: 

  1. Ensure that the following `additionalKernelArgs` are set in the cluster performance profile: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
# ...
spec:
  additionalKernelArgs:
  - "rcupdate.rcu_normal_after_boot=0"
  - "efi=runtime"
  - "vfio_pci.enable_sriov=1"
  - "vfio_pci.disable_idle_d3=1"
  - "module_blacklist=irdma"

  # ...
```


  2. Optional: Set the CPU frequency under the `hardwareTuning` field: 

You can use hardware tuning to tune CPU frequencies for reserved and isolated core CPUs. For FlexRAN like applications, hardware vendors recommend that you run CPU frequencies below the default provided frequencies. It is highly recommended that, before setting any frequencies, you refer to the hardware vendor’s guidelines for maximum frequency settings for your processor generation. This example sets the frequencies for reserved and isolated CPUs to 2500 MHz: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: openshift-node-performance-profile
spec:
      cpu:
        isolated: "2-19,22-39"
        reserved: "0-1,20-21"
      hugepages:
        defaultHugepagesSize: 1G
        pages:
          - size: 1G
            count: 32
      realTimeKernel:
          enabled: true
      hardwareTuning:
          isolatedCpuFreq: 2500000
          reservedCpuFreq: 2500000
```


  3. Ensure that the `performance-patch` profile in the `Tuned` CR configures the correct CPU isolation set that matches the `isolated` CPU set in the related `PerformanceProfile` CR, for example: 

```yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: performance-patch
  namespace: openshift-cluster-node-tuning-operator
  annotations:
    ran.openshift.io/ztp-deploy-wave: "10"
spec:
  profile:
    - name: performance-patch
      # The 'include' line must match the associated PerformanceProfile name, for example:
      # include=openshift-node-performance-${PerformanceProfile.metadata.name}
      # When using the standard (non-realtime) kernel, remove the kernel.timer_migration override from the [sysctl] section
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
# ...
```


## 8.2.4. Check the realtime kernel version

Always use the latest version of the realtime kernel in your OpenShift Container Platform clusters. If you are unsure about the kernel version that is in use in the cluster, you can compare the current realtime kernel version to the release version with the following procedure. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 
  * You have installed `podman`. 



**Procedure**

  1. Run the following command to get the cluster version: 

```shell-session
$ OCP_VERSION=$(oc get clusterversion version -o jsonpath='{.status.desired.version}{"\n"}')
```


  2. Get the release image SHA number: 

```shell-session
$ DTK_IMAGE=$(oc adm release info --image-for=driver-toolkit quay.io/openshift-release-dev/ocp-release:$OCP_VERSION-x86_64)
```


  3. Run the release image container and extract the kernel version that is packaged with cluster’s current release: 

```shell-session
$ podman run --rm $DTK_IMAGE rpm -qa | grep 'kernel-rt-core-' | sed 's#kernel-rt-core-##'
```


**Example output**

```shell-session
4.18.0-305.49.1.rt7.121.el8_4.x86_64
```


This is the default realtime kernel version that ships with the release. 

Note

The realtime kernel is denoted by the string `.rt` in the kernel version. 




**Verification**

Check that the kernel version listed for the cluster’s current release matches actual realtime kernel that is running in the cluster. Run the following commands to check the running realtime kernel version: 

  1. Open a remote shell connection to the cluster node: 

```shell-session
$ oc debug node/<node_name>
```


  2. Check the realtime kernel version: 

```shell-session
sh-4.4# uname -r
```


**Example output**

```shell-session
4.18.0-305.49.1.rt7.121.el8_4.x86_64
```
