# 4.9. Descheduler

## 4.9.1. Descheduler overview

The descheduler evicts running pods so that the default scheduler can place them on more suitable nodes. 

### 4.9.1.1. Maintain cluster balance by rescheduling pods

You can use the descheduler to evict pods based on specific strategies so that the pods are rescheduled onto more appropriate nodes. 

You can benefit from descheduling running pods in situations such as the following: 

  * Nodes are underutilized or overutilized. 
  * Pod and node affinity requirements, such as taints or labels, have changed and the original scheduling decisions are no longer appropriate for certain nodes. 
  * Node failure requires pods to be moved. 
  * New nodes are added to clusters. 
  * Pods have been restarted too many times. 



Important

The descheduler does not schedule replacement of evicted pods. The scheduler automatically performs this task for the evicted pods. 

When the descheduler decides to evict pods from a node, it employs the following general mechanism: 

  * Pods in the `openshift-*` and `kube-system` namespaces are never evicted. 
  * Critical pods with `priorityClassName` set to `system-cluster-critical` or `system-node-critical` are never evicted. 
  * Static, mirrored, or standalone pods that are not part of a replication controller, replica set, deployment, stateful set, or job are never evicted because these pods are not recreated. 
  * Pods associated with daemon sets are never evicted. 
  * Pods with local storage are never evicted. 
  * Best effort pods are evicted before burstable and guaranteed pods. 
  * All types of pods with the `descheduler.alpha.kubernetes.io/evict` annotation are eligible for eviction. This annotation is used to override checks that prevent eviction, and the user can select which pod is evicted. Users should know how and if the pod will be recreated. 
  * Pods subject to pod disruption budget (PDB) are not evicted if descheduling violates its pod disruption budget (PDB). The pods are evicted by using eviction subresource to handle PDB. 



### 4.9.1.2. Descheduler profiles

Use descheduler profiles to enable specific eviction strategies that rebalance your cluster based on criteria such as pod lifecycle or node utilization. 

The following descheduler profiles are available: 

`AffinityAndTaints`
    

This profile evicts pods that violate inter-pod anti-affinity, node affinity, and node taints. 

It enables the following strategies: 

  * `RemovePodsViolatingInterPodAntiAffinity`: removes pods that are violating inter-pod anti-affinity. 
  * `RemovePodsViolatingNodeAffinity`: removes pods that are violating node affinity. 
  * `RemovePodsViolatingNodeTaints`: removes pods that are violating `NoSchedule` taints on nodes. 

Pods with a node affinity type of `requiredDuringSchedulingIgnoredDuringExecution` are removed. 




`TopologyAndDuplicates`
    

This profile evicts pods in an effort to evenly spread similar pods, or pods of the same topology domain, among nodes. 

It enables the following strategies: 

  * `RemovePodsViolatingTopologySpreadConstraint`: finds unbalanced topology domains and tries to evict pods from larger ones when `DoNotSchedule` constraints are violated. 
  * `RemoveDuplicates`: ensures that there is only one pod associated with a replica set, replication controller, deployment, or job running on same node. If there are more, those duplicate pods are evicted for better pod distribution in a cluster. 



Warning

Do not enable `TopologyAndDuplicates` with any of the following profiles: `SoftTopologyAndDuplicates` or `CompactAndScale`. Enabling these profiles together results in a conflict. 

`LifecycleAndUtilization`
    

This profile evicts long-running pods and balances resource usage between nodes. 

It enables the following strategies: 

  * `RemovePodsHavingTooManyRestarts`: removes pods whose containers have been restarted too many times. 

Pods where the sum of restarts over all containers (including Init Containers) is more than 100. 

  * `LowNodeUtilization`: finds nodes that are underutilized and evicts pods, if possible, from overutilized nodes in the hope that recreation of evicted pods will be scheduled on these underutilized nodes. 

    * A node is considered underutilized if its usage is below 20% for all thresholds (CPU, memory, and number of pods). 
    * A node is considered overutilized if its usage is above 50% for any of the thresholds (CPU, memory, and number of pods). 

Optionally, you can adjust these underutilized/overutilized threshold percentages by setting the Technology Preview field `devLowNodeUtilizationThresholds` to one the following values: `Low` for 10%/30%, `Medium` for 20%/50%, or `High` for 40%/70%. The default value is `Medium`. 

  * `PodLifeTime`: evicts pods that are too old. 

By default, pods that are older than 24 hours are removed. You can customize the pod lifetime value. 




Warning

Do not enable `LifecycleAndUtilization` with any of the following profiles: `LongLifecycle` or `CompactAndScale`. Enabling these profiles together results in a conflict. 

`SoftTopologyAndDuplicates`
    

This profile is the same as `TopologyAndDuplicates`, except that pods with soft topology constraints, such as `whenUnsatisfiable: ScheduleAnyway`, are also considered for eviction. 

Warning

Do not enable both `SoftTopologyAndDuplicates` and `TopologyAndDuplicates`. Enabling both results in a conflict. 

`EvictPodsWithLocalStorage`
     This profile allows pods with local storage to be eligible for eviction. 
`EvictPodsWithPVC`
     This profile allows pods with persistent volume claims to be eligible for eviction. If you are using `Kubernetes NFS Subdir External Provisioner`, you must add an excluded namespace for the namespace where the provisioner is installed. 
`CompactAndScale`
    

This profile enables the `HighNodeUtilization` strategy, which attempts to evict pods from underutilized nodes to allow a workload to run on a smaller set of nodes. A node is considered underutilized if its usage is below 20% for all thresholds (CPU, memory, and number of pods). 

Optionally, you can adjust the underutilized percentage by setting the Technology Preview field `devHighNodeUtilizationThresholds` to one the following values: `Minimal` for 10%, `Modest` for 20%, or `Moderate` for 30%. The default value is `Modest`. 

Warning

Do not enable `CompactAndScale` with any of the following profiles: `LifecycleAndUtilization`, `LongLifecycle`, or `TopologyAndDuplicates`. Enabling these profiles together results in a conflict. 

`KubeVirtRelieveAndMigrate`
    

The `KubeVirtRelieveAndMigrate` profile evicts pods from high-cost nodes to reduce overall resource expenses and enable workload migration. It also periodically rebalances workloads to help maintain similar spare capacity across nodes, which supports better handling of sudden workload spikes. Nodes can experience the following costs: 

  * **Resource utilization** : Increased resource pressure raises the overhead for running applications. 
  * **Node maintenance** : A higher number of containers on a node increases resource consumption and maintenance costs. 



The profile enables the `LowNodeUtilization` strategy with the alpha-level `EvictionsInBackground` feature. By default, the profile uses the `PrometheusCPUMemoryCombinedProfile` utilization metric. This metric combines CPU and memory utilization with pressure stall information (PSI) for both dimensions for comprehensive node load balancing. 

The profile also exposes the following customization fields: 

  * `devActualUtilizationProfile`: Enables load-aware descheduling. You can configure the following utilization profiles: 

    * `PrometheusCPUMemoryCombinedProfile` (default): Balances nodes based on CPU utilization, CPU PSI pressure, memory utilization, and memory PSI pressure. This profile is ideal for environments with memory overcommit enabled, as it spreads the load and prevents resource contention. 
    * `PrometheusCPUCombined`: Balances nodes based on CPU utilization and CPU PSI pressure only. Use this profile in environments without memory overcommit, where memory allocations are strictly guaranteed and CPU pressure is the primary driver for workload distribution. 

  * `devLowNodeUtilizationThresholds`: Sets experimental thresholds for the `LowNodeUtilization` strategy. Do not use this field with `devDeviationThresholds`. 
  * `devDeviationThresholds`: Treats nodes with below-average resource usage as underutilized to help redistribute workloads from overutilized nodes. Do not use this field with `devLowNodeUtilizationThresholds`. Supported values are: `Low` (10%:10%), `Medium` (20%:20%), `High` (30%:30%), `AsymmetricLow` (0%:10%), `AsymmetricMedium` (0%:20%), `AsymmetricHigh` (0%:30%). 
  * `devEnableSoftTainter`: Enables the soft-tainting component to dynamically apply or remove soft taints as scheduling hints. 



Example configuration: 

```yaml
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  managementState: Managed
  deschedulingIntervalSeconds: 30
  mode: "Automatic"
  profiles:
    - KubeVirtRelieveAndMigrate
  profileCustomizations:
    devEnableSoftTainter: true
    devDeviationThresholds: AsymmetricLow
    devActualUtilizationProfile: PrometheusCPUMemoryCombinedProfile
```


The `KubeVirtRelieveAndMigrate` profile requires PSI metrics to be enabled on all worker nodes. You can enable this by applying the following `MachineConfig` custom resource (CR): 

Example `MachineConfig` CR: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-openshift-machineconfig-worker-psi-karg
spec:
  kernelArguments:
    - psi=1
```


Note

The name of the `MachineConfig` object is significant because machine configs are processed in lexicographical order. By default, a config that starts with `98-` disables PSI. To ensure that PSI is enabled, name your config with a higher prefix, such as `99-openshift-machineconfig-worker-psi-karg`. 

You can use this profile with the `SoftTopologyAndDuplicates` profile to also rebalance pods based on soft topology constraints, which can be useful in hosted control plane environments. 

`LongLifecycle`
    

This profile balances resource usage between nodes and enables the following strategies: 

  * `RemovePodsHavingTooManyRestarts`: removes pods whose containers have been restarted too many times and pods where the sum of restarts over all containers (including Init Containers) is more than 100. Restarting the VM guest operating system does not increase this count. 
  * `LowNodeUtilization`: evicts pods from overutilized nodes when there are any underutilized nodes. The destination node for the evicted pod will be determined by the scheduler. 

    * A node is considered underutilized if its usage is below 20% for all thresholds (CPU, memory, and number of pods). 
    * A node is considered overutilized if its usage is above 50% for any of the thresholds (CPU, memory, and number of pods). 




Warning

Do not enable `LongLifecycle` with any of the following profiles: `LifecycleAndUtilization` or `CompactAndScale`. Enabling these profiles together results in a conflict. 

**Additional resources**

  * [Default scheduling](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-about "4.1. Controlling pod placement using the scheduler")



## 4.9.2. Kube Descheduler Operator release notes

Review the Kube Descheduler Operator release notes to track its development and learn what is new and changed with each release. 

The Kube Descheduler Operator allows you to evict pods so that they can be rescheduled on more appropriate nodes. 

For more information, see [About the descheduler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-descheduler-about_nodes-descheduler-about "4.9.1.1. Maintain cluster balance by rescheduling pods"). 

### 4.9.2.1. Release notes for Kube Descheduler Operator 5.4.3

Review the release notes for Kube Descheduler Operator 5.4.3 to learn what is new and updated with this release. 

Issued: 9 September 2026 

The following advisory is available for the Kube Descheduler Operator 5.4.3: 

  * [RHBA-2026:66114](https://access.redhat.com/errata/RHBA-2026:66114)



#### 4.9.2.1.1. New features and enhancements

  * This release rebuilds the base image for the Kube Descheduler Operator to improve its image grade. 



### 4.9.2.2. Release notes for Kube Descheduler Operator 5.4.2

Review the release notes for Kube Descheduler Operator 5.4.2 to learn what is new and updated with this release. 

Issued: 14 August 2026 

The following advisory is available for the Kube Descheduler Operator 5.4.2: 

  * [RHBA-2026:54867](https://access.redhat.com/errata/RHBA-2026:54867)



#### 4.9.2.2.1. New features and enhancements

  * This release rebuilds the base image for the Kube Descheduler Operator to improve its image grade. 



### 4.9.2.3. Release notes for Kube Descheduler Operator 5.4.1

Review the release notes for Kube Descheduler Operator 5.4.1 to learn what is new and updated with this release. 

Issued: 13 August 2026 

The following advisory is available for the Kube Descheduler Operator 5.4.1: 

  * [RHBA-2026:54794](https://access.redhat.com/errata/RHBA-2026:54794)



#### 4.9.2.3.1. New features and enhancements

  * This release rebuilds the base image for the Kube Descheduler Operator to improve its image grade. 



### 4.9.2.4. Release notes for Kube Descheduler Operator 5.4.0

Review the release notes for Kube Descheduler Operator 5.4.0 to learn what is new and updated with this release. 

Issued: 10 June 2026 

The following advisory is available for the Kube Descheduler Operator 5.4.0: 

  * [RHBA-2026:25062](https://access.redhat.com/errata/RHBA-2026:25062)



#### 4.9.2.4.1. New features and enhancements

  * This release of the Kube Descheduler Operator updates the Kubernetes version to 1.35. 



#### 4.9.2.4.2. Bug fixes

  * This release of the Kube Descheduler Operator addresses several Common Vulnerabilities and Exposures (CVEs). 



## 4.9.3. Evicting pods using the descheduler

You can run the descheduler in OpenShift Container Platform by installing the Kube Descheduler Operator and setting the required profiles and other customizations. 

### 4.9.3.1. Install the descheduler

The descheduler is not available by default. To enable the descheduler, you must install the Kube Descheduler Operator from the software catalog and enable one or more descheduler profiles. 

By default, the descheduler runs in predictive mode, which means that it only simulates pod evictions. You must change the mode to automatic for the descheduler to perform the pod evictions. 

Important

If you have enabled hosted control planes in your cluster, set a custom priority threshold to lower the chance that pods in the hosted control plane namespaces are evicted. Set the priority threshold class name to `hypershift-control-plane`, because it has the lowest priority value (`100000000`) of the hosted control plane priority classes. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * Access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Create the required namespace for the Kube Descheduler Operator. 

     1. Navigate to **Administration** **Namespaces** and click **Create Namespace**. 
     2. Enter `openshift-kube-descheduler-operator` in the **Name** field, enter `openshift.io/cluster-monitoring=true` in the **Labels** field to enable descheduler metrics, and click **Create**. 

  3. Install the Kube Descheduler Operator. 

     1. Navigate to **Ecosystem** **Software Catalog**. 
     2. Type **Kube Descheduler Operator** into the filter box. 
     3. Select the **Kube Descheduler Operator** and click **Install**. 
     4. On the **Install Operator** page, select **A specific namespace on the cluster**. Select **openshift-kube-descheduler-operator** from the drop-down menu. 
     5. Adjust the values for the **Update Channel** and **Approval Strategy** to the desired values. 
     6. Click **Install**. 

  4. Create a descheduler instance. 

     1. From the **Ecosystem** **Installed Operators** page, click the **Kube Descheduler Operator**. 
     2. Select the **Kube Descheduler** tab and click **Create KubeDescheduler**. 
     3. Edit the settings as necessary. 

        1. To evict pods instead of simulating the evictions, change the **Mode** field to **Automatic**. 
        2. Expand the **Profiles** section to select one or more profiles to enable. The `AffinityAndTaints` profile is enabled by default. Click **Add Profile** to select additional profiles. 

Note

Do not enable both `TopologyAndDuplicates` and `SoftTopologyAndDuplicates`. Enabling both results in a conflict. 

        3. Optional: Expand the **Profile Customizations** section to set optional configurations for the descheduler. 

           * Set a custom pod lifetime value for the `LifecycleAndUtilization` profile. Use the **podLifetime** field to set a numerical value and a valid unit (`s`, `m`, or `h`). The default pod lifetime is 24 hours (`24h`). 
           * Set a custom priority threshold to consider pods for eviction only if their priority is lower than a specified priority level. Use the **thresholdPriority** field to set a numerical priority threshold or use the **thresholdPriorityClassName** field to specify a certain priority class name. 

Note

Do not specify both **thresholdPriority** and **thresholdPriorityClassName** for the descheduler. 

           * Set specific namespaces to exclude or include from descheduler operations. Expand the **namespaces** field and add namespaces to the **excluded** or **included** list. You can only either set a list of namespaces to exclude or a list of namespaces to include. Note that protected namespaces (`openshift-*`, `kube-system`, `hypershift`) are excluded by default. 
           * Experimental: Set thresholds for underutilization and overutilization for the `LowNodeUtilization` strategy. Use the **devLowNodeUtilizationThresholds** field to set one of the following values: 

             * `Low`: 10% underutilized and 30% overutilized 
             * `Medium`: 20% underutilized and 50% overutilized (Default) 
             * `High`: 40% underutilized and 70% overutilized 

Note

This setting is experimental and should not be used in a production environment. 

        4. Optional: Use the **Descheduling Interval Seconds** field to change the number of seconds between descheduler runs. The default is `3600` seconds. 

     4. Click **Create**. 

You can also configure the profiles and settings for the descheduler later using the OpenShift CLI (`oc`). If you did not adjust the profiles when creating the descheduler instance from the web console, the `AffinityAndTaints` profile is enabled by default. 




### 4.9.3.2. Configure descheduler profiles

To manage cluster pod eviction behavior, select which descheduler profiles to enable. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 



**Procedure**

  1. Edit the `KubeDescheduler` object: 

```shell-session
$ oc edit kubedeschedulers.operator.openshift.io cluster -n openshift-kube-descheduler-operator
```


  2. Specify one or more profiles in the `spec.profiles` section. 

```yaml
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  deschedulingIntervalSeconds: 3600
  logLevel: Normal
  managementState: Managed
  operatorLogLevel: Normal
  mode: Predictive
  profileCustomizations:
    namespaces:
      excluded:
      - my-namespace
    podLifetime: 48h
    thresholdPriorityClassName: my-priority-class-name
  evictionLimits:
    total: 20
  profiles:
  - AffinityAndTaints
  - TopologyAndDuplicates
  - LifecycleAndUtilization
  - EvictPodsWithLocalStorage
  - EvictPodsWithPVC
```


where: 

`spec.mode`
     Specifies the eviction mode. By default, the descheduler does not evict pods. To evict pods, set `mode` to `Automatic`. 
`spec.profileCustomizations.namespaces`
     Specifies a list of user-created namespaces to include or exclude from descheduler operations. Use `excluded` to set a list of namespaces to exclude or use `included` to set a list of namespaces to include. Note that protected namespaces (`openshift-*`, `kube-system`, `hypershift`) are excluded by default. This value is optional. 
`spec.profileCustomizations.podLifetime`
     Specifies a custom pod lifetime value for the `LifecycleAndUtilization` profile. Valid units are `s`, `m`, or `h`. The default pod lifetime is 24 hours. This value is optional. 
`spec.profileCustomizations.thresholdPriorityClassName`
     Specifies a priority threshold to consider pods for eviction only if their priority is lower than the specified level. Use the `thresholdPriority` field to set a numerical priority threshold (for example, `10000`) or use the `thresholdPriorityClassName` field to specify a certain priority class name (for example, `my-priority-class-name`). If you specify a priority class name, it must already exist or the descheduler will throw an error. Do not set both `thresholdPriority` and `thresholdPriorityClassName`. This value is optional. 
`spec.evictionLimits.total`
     Specifies the maximum number of pods to evict during each descheduler run. This value is optional. 
`spec.profiles`
     Specifies one or more profiles to enable. Available profiles: `AffinityAndTaints`, `TopologyAndDuplicates`, `LifecycleAndUtilization`, `SoftTopologyAndDuplicates`, `EvictPodsWithLocalStorage`, `EvictPodsWithPVC`, `CompactAndScale`, and `LongLifecycle`. You can enable multiple profiles, but ensure that you do not enable profiles that conflict with each other. The order of the list of profiles is not important. 

  3. Save the file to apply the changes. 



### 4.9.3.3. Configure the descheduler interval

You can configure the amount of time between descheduler runs. The default is 3600 seconds (one hour). 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 



**Procedure**

  1. Edit the `KubeDescheduler` object: 

```shell-session
$ oc edit kubedeschedulers.operator.openshift.io cluster -n openshift-kube-descheduler-operator
```


  2. Update the `deschedulingIntervalSeconds` field to the required value: 

```yaml
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  deschedulingIntervalSeconds: 3600
...
```


Set the `spec.deschedulingIntervalSeconds` field to the number of seconds you want between descheduler runs. A value of `0` in this field runs the descheduler once and exits. 

  3. Save the file to apply the changes. 



## 4.9.4. Uninstalling the Kube Descheduler Operator

If you no longer need the Kube Descheduler Operator in your cluster, you can uninstall the Operator and remove its related resources. 

### 4.9.4.1. Uninstall the descheduler

If you no longer need the descheduler in your cluster, you can remove it by deleting the descheduler instance and uninstalling the Kube Descheduler Operator. You can also delete the `KubeDescheduler` CRD and `openshift-kube-descheduler-operator` namespace. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * Access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Delete the descheduler instance. 

     1. From the **Ecosystem** **Installed Operators** page, click **Kube Descheduler Operator**. 
     2. Select the **Kube Descheduler** tab. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **cluster** entry and select **Delete KubeDescheduler**. 
     4. In the confirmation dialog, click **Delete**. 

  3. Uninstall the Kube Descheduler Operator. 

     1. Navigate to **Ecosystem** **Installed Operators**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **Kube Descheduler Operator** entry and select **Uninstall Operator**. 
     3. In the confirmation dialog, click **Uninstall**. 

  4. Delete the `openshift-kube-descheduler-operator` namespace. 

     1. Navigate to **Administration** **Namespaces**. 
     2. Enter `openshift-kube-descheduler-operator` into the filter box. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **openshift-kube-descheduler-operator** entry and select **Delete Namespace**. 
     4. In the confirmation dialog, enter `openshift-kube-descheduler-operator` and click **Delete**. 

  5. Delete the `KubeDescheduler` CRD. 

     1. Navigate to **Administration** **Custom Resource Definitions**. 
     2. Enter `KubeDescheduler` into the filter box. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **KubeDescheduler** entry and select **Delete CustomResourceDefinition**. 
     4. In the confirmation dialog, click **Delete**.
