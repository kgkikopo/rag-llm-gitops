# 4.1. Create a KubeletConfig CR to edit kubelet parameters

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
