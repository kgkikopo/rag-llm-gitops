# 5.3. Recommended node host practices

You can configure the `podsPerCore` and `maxPods` parameters to control the maximum number of pods that can be scheduled on a node. 

The OpenShift Container Platform node configuration file contains important options. For example, two parameters control the maximum number of pods that can be scheduled to a node: `podsPerCore` and `maxPods`. 

When both options are in use, the lower of the two values limits the number of pods on a node. Exceeding these values can result in the following conditions: 

  * Increased CPU utilization. 
  * Slow pod scheduling. 
  * Potential out-of-memory scenarios, depending on the amount of memory in the node. 
  * Exhausting the pool of IP addresses. 
  * Resource overcommitting, leading to poor user application performance. 



Important

In Kubernetes, a pod that is holding a single container actually uses two containers. The second container is used to set up networking prior to the actual container starting. Therefore, a system running 10 pods will actually have 20 containers running. 

Note

Disk IOPS throttling from the cloud provider might have an impact on CRI-O and kubelet. They might get overloaded when there are large number of I/O intensive pods running on the nodes. It is recommended that you monitor the disk I/O on the nodes and use volumes with sufficient throughput for the workload. 

The `podsPerCore` parameter sets the number of pods that the node can run based on the number of processor cores on the node. For example, if `podsPerCore` is set to `10` on a node with 4 processor cores, the maximum number of pods allowed on the node is `40`. 

```yaml
kubeletConfig:
  podsPerCore: 10
```


Setting `podsPerCore` to `0` disables this limit. The default is `0`. The value of the `podsPerCore` parameter cannot exceed the value of the `maxPods` parameter. 

The `maxPods` parameter sets the number of pods that the node can run to a fixed value, regardless of the properties of the node. 

```yaml
 kubeletConfig:
    maxPods: 250
```


## 5.3.1. Create a KubeletConfig CR to edit kubelet parameters

You can use a `KubeletConfig` custom resource (CR) to edit a kubelet parameters without modifing the kubelet configuration directly. 

Note

As the fields in the `kubeletConfig` object are passed directly to the kubelet from upstream Kubernetes, the kubelet validates those values directly. Invalid values in the `kubeletConfig` object might cause cluster nodes to become unavailable. For valid values, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/). 

You can set most kubelet configuration options. You cannot overwrite the following options: 

  * `CgroupDriver`
  * `ClusterDNS`
  * `ClusterDomain`
  * `StaticPodPath`



Consider the following guidance: 

  * Edit an existing `KubeletConfig` CR to modify existing settings or add new settings, instead of creating a CR for each change. It is recommended that you create a CR only to modify a different machine config pool, or for changes that are intended to be temporary, so that you can revert the changes. 
  * Create one `KubeletConfig` CR for each machine config pool with all the config changes you want for that pool. 
  * As needed, create multiple `KubeletConfig` CRs with a limit of 10 per cluster. For the first `KubeletConfig` CR, the Machine Config Operator (MCO) creates a machine config appended with `kubelet`. With each subsequent CR, the controller creates another `kubelet` machine config with a numeric suffix. For example, if you have a `kubelet` machine config with a `-2` suffix, the next `kubelet` machine config is appended with `-3`. 

Important

The Machine Config Operator does not merge multiple `KubeletConfig` CRs that target the same machine config pool. Each CR generates a separate machine config that writes the kubelet configuration. The most recently created `KubeletConfig` CR takes precedence and overrides the kubelet settings from earlier CRs for that pool. 

To apply multiple kubelet settings to the same pool, include all of the settings in a single `KubeletConfig` CR. 




Note

If you are applying a kubelet or container runtime config to a custom machine config pool, the custom role in the `machineConfigSelector` must match the name of the custom machine config pool. 

For example, because the following custom machine config pool is named `infra`, the custom role must also be `infra`: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: infra
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,infra]}
# ...
```


If you want to delete the machine configs, delete them in reverse order to avoid exceeding the limit. For example, you delete the `kubelet-3` machine config before deleting the `kubelet-2` machine config. 

Note

If you have a machine config with a `kubelet-9` suffix, and you create another `KubeletConfig` CR, a new machine config is not created, even if there are fewer than 10 `kubelet` machine configs. 

The following example command and output show a `KubeletConfig` CR: 

```shell-session
$ oc get kubeletconfig
```


```shell-session
NAME                      AGE
set-kubelet-config        15m
```


The following example command and output show a `KubeletConfig` machine config: 

```shell-session
$ oc get mc | grep kubelet
```


```shell-session
...
99-worker-generated-kubelet-1                  b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             26m
...
```


The following procedure is an example to show how to configure the maximum number of pods per node, the maximum PIDs per node, and the maximum container log size size on the worker nodes. 

**Prerequisites**

  1. Obtain the label associated with the static `MachineConfigPool` CR for the type of node you want to configure. Perform one of the following steps: 

     1. View the machine config pool: 

```shell-session
$ oc describe machineconfigpool <name>
```


For example: 

```shell-session
$ oc describe machineconfigpool worker
```


**Example output**

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  creationTimestamp: 2019-02-08T14:52:39Z
  generation: 1
  labels:
    custom-kubelet: set-kubelet-config
```


The `metadata.labels` parameter specifies labels you can use with a `KubeletConfig` CR. 

     2. If the label is not present, add a key/value pair: 

```shell-session
$ oc label machineconfigpool worker custom-kubelet=set-kubelet-config
```


**Procedure**

  1. View the available machine configuration objects that you can select: 

```shell-session
$ oc get machineconfig
```


By default, the two kubelet-related configs are `01-master-kubelet` and `01-worker-kubelet`. 

  2. Check the current value for the maximum pods per node: 

```shell-session
$ oc describe node <node_name>
```


For example: 

```shell-session
$ oc describe node ci-ln-5grqprb-f76d1-ncnqq-worker-a-mdv94
```


Look for `value: pods: <value>` in the `Allocatable` stanza: 

**Example output**

```shell-session
Allocatable:
 attachable-volumes-aws-ebs:  25
 cpu:                         3500m
 hugepages-1Gi:               0
 hugepages-2Mi:               0
 memory:                      15341844Ki
 pods:                        250
```


  3. Configure the worker nodes as needed: 

     1. Create a YAML file similar to the following that contains the kubelet configuration: 

Important

Kubelet configurations that target a specific machine config pool also affect any dependent pools. For example, creating a kubelet configuration for the pool containing worker nodes will also apply to any subset pools, including the pool containing infrastructure nodes. To avoid this, you must create a new machine config pool with a selection expression that only includes worker nodes, and have your kubelet configuration target this new pool. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: set-kubelet-config
spec:
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: set-kubelet-config
  kubeletConfig:
      podPidsLimit: 8192
      containerLogMaxSize: 50Mi
      maxPods: 500
```


where: 

`spec.machineConfigPoolSelector.matchLabels`
     Specifies the label from the machine config pool. 
`spec.kubeletConfig`
    

Specifies the kubelet configuration. For example: 

        * Use `podPidsLimit` to set the maximum number of PIDs in any pod. 
        * Use `containerLogMaxSize` to set the maximum size of the container log file before it is rotated. 
        * Use `maxPods` to set the maximum pods per node. 
        * Use `nodeStatusMaxImages` to set how many images the node reports. If a node contains more than 50 images, pod scheduling might be imbalanced because the image list is shortened to 50 by default. Set `nodeStatusMaxImages` to `-1` to disable that limit. 

Note

The rate at which the kubelet talks to the API server depends on queries per second (QPS) and burst values. The default values, `50` for `kubeAPIQPS` and `100` for `kubeAPIBurst`, are sufficient if there are limited pods running on each node. It is recommended to update the kubelet QPS and burst rates if there are enough CPU and memory resources on the node. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: set-kubelet-config
spec:
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: set-kubelet-config
  kubeletConfig:
    maxPods: <pod_count>
    kubeAPIBurst: <burst_rate>
    kubeAPIQPS: <QPS>
```


     2. Update the machine config pool for workers with the label: 

```shell-session
$ oc label machineconfigpool worker custom-kubelet=set-kubelet-config
```


     3. Create the `KubeletConfig` object: 

```shell-session
$ oc create -f change-maxPods-cr.yaml
```


**Verification**

  1. Verify that the `KubeletConfig` object is created: 

```shell-session
$ oc get kubeletconfig
```


**Example output**

```shell-session
NAME                      AGE
set-kubelet-config        15m
```


Depending on the number of worker nodes in the cluster, wait for the worker nodes to be rebooted one by one. For a cluster with 3 worker nodes, this could take about 10 to 15 minutes. 

  2. Verify that the changes are applied to the node: 

     1. Check on a worker node that the `maxPods` value changed: 

```shell-session
$ oc describe node <node_name>
```


     2. Locate the `Allocatable` stanza: 

```shell-session
 ...
Allocatable:
  attachable-volumes-gce-pd:  127
  cpu:                        3500m
  ephemeral-storage:          123201474766
  hugepages-1Gi:              0
  hugepages-2Mi:              0
  memory:                     14225400Ki
  pods:                       500
 ...
```


In this example, the `pods` parameter should report the value you set in the `KubeletConfig` object. 

  3. Verify the change in the `KubeletConfig` object: 

```shell-session
$ oc get kubeletconfigs set-kubelet-config -o yaml
```


This should show a status of `True` and `type:Success`, as shown in the following example: 

```yaml
spec:
  kubeletConfig:
    containerLogMaxSize: 50Mi
    maxPods: 500
    podPidsLimit: 8192
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: set-kubelet-config
status:
  conditions:
  - lastTransitionTime: "2021-06-30T17:04:07Z"
    message: Success
    status: "True"
    type: Success
```


## 5.3.2. Modifying the number of unavailable worker nodes

You can speed up kubelet configuration rollouts on large clusters by increasing the number of worker nodes that can be unavailable during machine config pool updates. 

By default, only one machine is allowed to be unavailable when applying the kubelet-related configuration to the available worker nodes. For a large cluster, it can take a long time for the configuration change to be reflected. At any time, you can adjust the number of machines that are updating to speed up the process. 

**Procedure**

  1. Edit the `worker` machine config pool: 

```shell-session
$ oc edit machineconfigpool worker
```


  2. Add the `maxUnavailable` field and set the value: 

```yaml
spec:
  maxUnavailable: <node_count>
```


Important

When setting the value, consider the number of worker nodes that can be unavailable without affecting the applications running on the cluster. 




## 5.3.3. Control plane node sizing

The control plane node resource requirements depend on the number and type of nodes and objects in the cluster. Reference the control plane node size recommendations to better understand your sizing needs. 

The following control plane node size recommendations are based on the results of a control plane density focused testing, or _Cluster-density_. This test creates the following objects across a given number of namespaces: 

  * 1 image stream 
  * 1 build 
  * 5 deployments, with 2 pod replicas in a `sleep` state, mounting 4 secrets, 4 config maps, and 1 downward API volume each 
  * 5 services, each one pointing to the TCP/8080 and TCP/8443 ports of one of the previous deployments 
  * 1 route pointing to the first of the previous services 
  * 10 secrets containing 2048 random string characters 
  * 10 config maps containing 2048 random string characters 



Number of compute nodes| Cluster-density (namespaces)| CPU cores| Memory (GB)  
---|---|---|---  
24  |  500  |  4  |  16   
120  |  1000  |  8  |  32   
252  |  4000  |  16, but 24 if using the OVN-Kubernetes network plug-in  |  64, but 128 if using the OVN-Kubernetes network plug-in   
501, but untested with the OVN-Kubernetes network plug-in  |  4000  |  16  |  96   
Show more

The data from the table above is based on an OpenShift Container Platform running on top of AWS, using r5.4xlarge instances as control-plane nodes and m5.2xlarge instances as compute nodes. 

On a large and dense cluster with three control plane nodes, the CPU and memory usage will spike up when one of the nodes is stopped, rebooted, or fails. The failures can be due to unexpected issues with power, network, underlying infrastructure, or intentional cases where the cluster is restarted after shutting it down to save costs. The remaining two control plane nodes must handle the load in order to be highly available, which leads to increase in the resource usage. This is also expected during upgrades because the control plane nodes are cordoned, drained, and rebooted serially to apply the operating system updates, as well as the control plane Operators update. To avoid cascading failures, keep the overall CPU and memory resource usage on the control plane nodes to at most 60% of all available capacity to handle the resource usage spikes. Increase the CPU and memory on the control plane nodes accordingly to avoid potential downtime due to lack of resources. 

Important

The node sizing varies depending on the number of nodes and object counts in the cluster. It also depends on whether the objects are actively being created on the cluster. During object creation, the control plane is more active in terms of resource usage compared to when the objects are in the `Running` phase. 

Operator Lifecycle Manager (OLM) runs on the control plane nodes and its memory footprint depends on the number of namespaces and user installed operators that OLM needs to manage on the cluster. Control plane nodes need to be sized accordingly to avoid OOM kills. Following data points are based on the results from cluster maximums testing. 

Number of namespaces| OLM memory at idle state (GB)| OLM memory with 5 user operators installed (GB)  
---|---|---  
500  |  0.823  |  1.7   
1000  |  1.2  |  2.5   
1500  |  1.7  |  3.2   
2000  |  2  |  4.4   
3000  |  2.7  |  5.6   
4000  |  3.8  |  7.6   
5000  |  4.2  |  9.02   
6000  |  5.8  |  11.3   
7000  |  6.6  |  12.9   
8000  |  6.9  |  14.8   
9000  |  8  |  17.7   
10,000  |  9.9  |  21.6   
Show more

Important

You can modify the control plane node size in a running OpenShift Container Platform 4.22 cluster for the following configurations only: 

  * Clusters installed with a user-provisioned installation method. 
  * AWS clusters installed with an installer-provisioned infrastructure installation method. 
  * Clusters that use a control plane machine set to manage control plane machines. 



For all other configurations, you must estimate your total node count and use the suggested control plane node size during installation. 

Note

In OpenShift Container Platform 4.22, half of a CPU core (500 millicore) is now reserved by the system by default compared to OpenShift Container Platform 3.11 and previous versions. The sizes are determined taking that into consideration. 

## 5.3.4. Set up CPU Manager

To configure CPU manager, create a `KubeletConfig` custom resource (CR) and apply it to the required set of nodes. 

**Procedure**

  1. Label a node by running the following command: 

```shell-session
# oc label node perf-node.example.com cpumanager=true
```


  2. To enable CPU Manager for all compute nodes, edit the CR by running the following command: 

```shell-session
# oc edit machineconfigpool worker
```


  3. Add the `custom-kubelet: cpumanager-enabled` label to `metadata.labels` section. 

```yaml
metadata:
  creationTimestamp: 2020-xx-xxx
  generation: 3
  labels:
    custom-kubelet: cpumanager-enabled
```


  4. Create a `KubeletConfig`, `cpumanager-kubeletconfig.yaml`, custom resource (CR). Refer to the label created in the previous step to have the correct nodes updated with the new kubelet config. See the `machineConfigPoolSelector` section: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: cpumanager-enabled
spec:
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: cpumanager-enabled
  kubeletConfig:
     cpuManagerPolicy: static
     cpuManagerReconcilePeriod: 5s
```


     * `cpuManagerPolicy` specifies a policy: 

       * `none`. This policy explicitly enables the existing default CPU affinity scheme, providing no affinity beyond what the scheduler does automatically. This is the default policy. 
       * `static`. This policy allows containers in guaranteed pods with integer CPU requests. It also limits access to exclusive CPUs on the node. If `static`, you must use a lowercase `s`. 

     * `cpuManagerReconcilePeriod` is optional. Specify the CPU Manager reconcile frequency. The default is `5s`. 

  5. Create the dynamic kubelet config by running the following command: 

```shell-session
# oc create -f cpumanager-kubeletconfig.yaml
```


This adds the CPU Manager feature to the kubelet config and, if needed, the Machine Config Operator (MCO) reboots the node. To enable CPU Manager, a reboot is not needed. 

  6. Check for the merged kubelet config by running the following command: 

```shell-session
# oc get machineconfig 99-worker-XXXXXX-XXXXX-XXXX-XXXXX-kubelet -o json | grep ownerReference -A7
```


**Example output**

```plaintext
       "ownerReferences": [
            {
                "apiVersion": "machineconfiguration.openshift.io/v1",
                "kind": "KubeletConfig",
                "name": "cpumanager-enabled",
                "uid": "7ed5616d-6b72-11e9-aae1-021e1ce18878"
            }
        ]
```


  7. Check the compute node for the updated `kubelet.conf` file by running the following command: 

```shell-session
# oc debug node/perf-node.example.com
sh-4.2# cat /host/etc/kubernetes/kubelet.conf | grep cpuManager
```


The following is example output: 

```shell-session
cpuManagerPolicy: static
cpuManagerReconcilePeriod: 5s
```


     * `cpuManagerPolicy` is defined when you create the `KubeletConfig` CR. 
     * `cpuManagerReconcilePeriod` is defined when you create the `KubeletConfig` CR. 

  8. Create a project by running the following command: 

```shell-session
$ oc new-project <project_name>
```


  9. Create a pod that requests a core or multiple cores. Both limits and requests must have their CPU value set to a whole integer. That is the number of cores that will be dedicated to this pod: 

```shell-session
# cat cpumanager-pod.yaml
```


**Example output**

```yaml
apiVersion: v1
kind: Pod
metadata:
  generateName: cpumanager-
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: cpumanager
    image: gcr.io/google_containers/pause:3.2
    resources:
      requests:
        cpu: 1
        memory: "1G"
      limits:
        cpu: 1
        memory: "1G"
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  nodeSelector:
    cpumanager: "true"
```


  10. Create the pod: 

```shell-session
# oc create -f cpumanager-pod.yaml
```


**Verification**

  1. Verify that the pod is scheduled to the node that you labeled by running the following command: 

```shell-session
# oc describe pod cpumanager
```


**Example output**

```shell-session
Name:               cpumanager-6cqz7
Namespace:          default
Priority:           0
PriorityClassName:  <none>
Node:  perf-node.example.com/xxx.xx.xx.xxx
...
 Limits:
      cpu:     1
      memory:  1G
    Requests:
      cpu:        1
      memory:     1G
...
QoS Class:       Guaranteed
Node-Selectors:  cpumanager=true
```


  2. Verify that a CPU has been exclusively assigned to the pod by running the following command: 

```shell-session
# oc describe node --selector='cpumanager=true' | grep -i cpumanager- -B2
```


**Example output**

```shell-session
NAMESPACE    NAME                CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
cpuman       cpumanager-mlrrz    1 (28%)       1 (28%)     1G (13%)         1G (13%)       27m
```


  3. Verify that the `cgroups` are set up correctly. Get the process ID (PID) of the `pause` process by running the following commands: 

```shell-session
# oc debug node/perf-node.example.com
```


```shell-session
sh-4.2# systemctl status | grep -B5 pause
```


Note

If the output returns multiple pause process entries, you must identify the correct pause process. 

**Example output**

```shell-session
# ├─init.scope
│ └─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 17
└─kubepods.slice
  ├─kubepods-pod69c01f8e_6b74_11e9_ac0f_0a2b62178a22.slice
  │ ├─crio-b5437308f1a574c542bdf08563b865c0345c8f8c0b0a655612c.scope
  │ └─32706 /pause
```


  4. Verify that pods of quality of service (QoS) tier `Guaranteed` are placed within the `kubepods.slice` subdirectory by running the following commands: 

```shell-session
# cd /sys/fs/cgroup/kubepods.slice/kubepods-pod69c01f8e_6b74_11e9_ac0f_0a2b62178a22.slice/crio-b5437308f1ad1a7db0574c542bdf08563b865c0345c86e9585f8c0b0a655612c.scope
```


```shell-session
# for i in `ls cpuset.cpus cgroup.procs` ; do echo -n "$i "; cat $i ; done
```


Note

Pods of other QoS tiers end up in child `cgroups` of the parent `kubepods`. 

**Example output**

```shell-session
cpuset.cpus 1
tasks 32706
```


  5. Check the allowed CPU list for the task by running the following command: 

```shell-session
# grep ^Cpus_allowed_list /proc/32706/status
```


**Example output**

```shell-session
 Cpus_allowed_list:    1
```


  6. Verify that another pod on the system cannot run on the core allocated for the `Guaranteed` pod. For example, to verify the pod in the `besteffort` QoS tier, run the following commands: 

```shell-session
# cat /sys/fs/cgroup/kubepods.slice/kubepods-besteffort.slice/kubepods-besteffort-podc494a073_6b77_11e9_98c0_06bba5c387ea.slice/crio-c56982f57b75a2420947f0afc6cafe7534c5734efc34157525fa9abbf99e3849.scope/cpuset.cpus
```


```shell-session
# oc describe node perf-node.example.com
```


**Example output**

```shell-session
...
Capacity:
 attachable-volumes-aws-ebs:  39
 cpu:                         2
 ephemeral-storage:           124768236Ki
 hugepages-1Gi:               0
 hugepages-2Mi:               0
 memory:                      8162900Ki
 pods:                        250
Allocatable:
 attachable-volumes-aws-ebs:  39
 cpu:                         1500m
 ephemeral-storage:           124768236Ki
 hugepages-1Gi:               0
 hugepages-2Mi:               0
 memory:                      7548500Ki
 pods:                        250
-------                               ----                           ------------  ----------  ---------------  -------------  ---
  default                                 cpumanager-6cqz7               1 (66%)       1 (66%)     1G (12%)         1G (12%)       29m

Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests          Limits
  --------                    --------          ------
  cpu                         1440m (96%)       1 (66%)
```


This VM has two CPU cores. The `system-reserved` setting reserves 500 millicores, meaning that half of one core is subtracted from the total capacity of the node to arrive at the `Node Allocatable` amount. You can see that `Allocatable CPU` is 1500 millicores. This means you can run one of the CPU Manager pods since each will take one whole core. A whole core is equivalent to 1000 millicores. If you try to schedule a second pod, the system will accept the pod, but it will never be scheduled: 

```shell-session
NAME                    READY   STATUS    RESTARTS   AGE
cpumanager-6cqz7        1/1     Running   0          33m
cpumanager-7qc2t        0/1     Pending   0          11s
```
