# 12.10. Troubleshoot NUMA-aware scheduling

To resolve common problems with NUMA-aware pod scheduling, troubleshoot your cluster configuration. Identifying and fixing these issues ensures that your pods are optimally aligned with underlying hardware for high-performance workloads. 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * Logged in as a user with cluster-admin privileges. 
  * Installed the NUMA Resources Operator and deploy the NUMA-aware secondary scheduler. 



**Procedure**

  1. Verify that the `noderesourcetopologies` CRD is deployed in the cluster by running the following command: 

```shell-session
$ oc get crd | grep noderesourcetopologies
```


**Example output**

```shell-session
NAME                                                              CREATED AT
noderesourcetopologies.topology.node.k8s.io                       2022-01-18T08:28:06Z
```


  2. Check that the NUMA-aware scheduler name matches the name specified in your NUMA-aware workloads by running the following command: 

```shell-session
$ oc get numaresourcesschedulers.nodetopology.openshift.io numaresourcesscheduler -o json | jq '.status.schedulerName'
```


**Example output**

```shell-session
topo-aware-scheduler
```


  3. Verify that NUMA-aware schedulable nodes have the `noderesourcetopologies` CR applied to them. Run the following command: 

```shell-session
$ oc get noderesourcetopologies.topology.node.k8s.io
```


**Example output**

```shell-session
NAME                    AGE
compute-0.example.com   17h
compute-1.example.com   17h
```


Note

The number of nodes should equal the number of worker nodes that are configured by the machine config pool (`mcp`) worker definition. 

  4. Verify the NUMA zone granularity for all schedulable nodes by running the following command: 

```shell-session
$ oc get noderesourcetopologies.topology.node.k8s.io -o yaml
```


**Example output**

```yaml
apiVersion: v1
items:
- apiVersion: topology.node.k8s.io/v1
  kind: NodeResourceTopology
  metadata:
    annotations:
      k8stopoawareschedwg/rte-update: periodic
    creationTimestamp: "2022-06-16T08:55:38Z"
    generation: 63760
    name: worker-0
    resourceVersion: "8450223"
    uid: 8b77be46-08c0-4074-927b-d49361471590
  topologyPolicies:
  - SingleNUMANodeContainerLevel
  zones:
  - costs:
    - name: node-0
      value: 10
    - name: node-1
      value: 21
    name: node-0
    resources:
    - allocatable: "38"
      available: "38"
      capacity: "40"
      name: cpu
    - allocatable: "134217728"
      available: "134217728"
      capacity: "134217728"
      name: hugepages-2Mi
    - allocatable: "262352048128"
      available: "262352048128"
      capacity: "270107316224"
      name: memory
    - allocatable: "6442450944"
      available: "6442450944"
      capacity: "6442450944"
      name: hugepages-1Gi
    type: Node
  - costs:
    - name: node-0
      value: 21
    - name: node-1
      value: 10
    name: node-1
    resources:
    - allocatable: "268435456"
      available: "268435456"
      capacity: "268435456"
      name: hugepages-2Mi
    - allocatable: "269231067136"
      available: "269231067136"
      capacity: "270573244416"
      name: memory
    - allocatable: "40"
      available: "40"
      capacity: "40"
      name: cpu
    - allocatable: "1073741824"
      available: "1073741824"
      capacity: "1073741824"
      name: hugepages-1Gi
    type: Node
- apiVersion: topology.node.k8s.io/v1
  kind: NodeResourceTopology
  metadata:
    annotations:
      k8stopoawareschedwg/rte-update: periodic
    creationTimestamp: "2022-06-16T08:55:37Z"
    generation: 62061
    name: worker-1
    resourceVersion: "8450129"
    uid: e8659390-6f8d-4e67-9a51-1ea34bba1cc3
  topologyPolicies:
  - SingleNUMANodeContainerLevel
  zones:
  - costs:
    - name: node-0
      value: 10
    - name: node-1
      value: 21
    name: node-0
    resources:
    - allocatable: "38"
      available: "38"
      capacity: "40"
      name: cpu
    - allocatable: "6442450944"
      available: "6442450944"
      capacity: "6442450944"
      name: hugepages-1Gi
    - allocatable: "134217728"
      available: "134217728"
      capacity: "134217728"
      name: hugepages-2Mi
    - allocatable: "262391033856"
      available: "262391033856"
      capacity: "270146301952"
      name: memory
    type: Node
  - costs:
    - name: node-0
      value: 21
    - name: node-1
      value: 10
    name: node-1
    resources:
    - allocatable: "40"
      available: "40"
      capacity: "40"
      name: cpu
    - allocatable: "1073741824"
      available: "1073741824"
      capacity: "1073741824"
      name: hugepages-1Gi
    - allocatable: "268435456"
      available: "268435456"
      capacity: "268435456"
      name: hugepages-2Mi
    - allocatable: "269192085504"
      available: "269192085504"
      capacity: "270534262784"
      name: memory
    type: Node
kind: List
metadata:
  resourceVersion: ""
  selfLink: ""
# ...
```


     * `zones`: Each stanza under `zones` describes the resources for a single NUMA zone. 
     * `costs.resources`: Specifies the current state of the NUMA zone resources. Check that resources listed under `items.zones.resources.available` correspond to the exclusive NUMA zone resources allocated to each guaranteed pod. 




## 12.10.1. Report more exact resource availability

To report more exact resource availability and minimize Topology Affinity Errors, enable the `cacheResyncPeriod` specification for the NUMA Resources Operator. 

This configuration monitors pending resources on nodes and synchronizes them in the scheduler cache, though lower intervals increase network load. 

The lower the interval, the greater the network load. The `cacheResyncPeriod` specification is disabled by default. 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Delete the currently running `NUMAResourcesScheduler` resource: 

     1. Get the active `NUMAResourcesScheduler` by running the following command: 

```shell-session
$ oc get NUMAResourcesScheduler
```


**Example output**

```shell-session
NAME                     AGE
numaresourcesscheduler   92m
```


     2. Delete the secondary scheduler resource by running the following command: 

```shell-session
$ oc delete NUMAResourcesScheduler numaresourcesscheduler
```


**Example output**

```shell-session
numaresourcesscheduler.nodetopology.openshift.io "numaresourcesscheduler" deleted
```


  2. Save the following YAML in the file `nro-scheduler-cacheresync.yaml`. This example changes the log level to `Debug`: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: numaresourcesscheduler
spec:
  imageSpec: "registry.redhat.io/openshift4/noderesourcetopology-scheduler-container-rhel8:v4.22"
  cacheResyncPeriod: "5s"
```


     * `spec.cacheResyncPeriod`: Enter an interval value in seconds for synchronization of the scheduler cache. A value of `5s` is typical for most implementations. 

  3. Create the updated `NUMAResourcesScheduler` resource by running the following command: 

```shell-session
$ oc create -f nro-scheduler-cacheresync.yaml
```


**Example output**

```shell-session
numaresourcesscheduler.nodetopology.openshift.io/numaresourcesscheduler created
```


**Verification**

  1. Check that the NUMA-aware scheduler was successfully deployed: 

     1. Run the following command to check that the CRD is created successfully: 

```shell-session
$ oc get crd | grep numaresourcesschedulers
```


**Example output**

```shell-session
NAME                                                              CREATED AT
numaresourcesschedulers.nodetopology.openshift.io                 2022-02-25T11:57:03Z
```


     2. Check that the new custom scheduler is available by running the following command: 

```shell-session
$ oc get numaresourcesschedulers.nodetopology.openshift.io
```


**Example output**

```shell-session
NAME                     AGE
numaresourcesscheduler   3h26m
```


  2. Check that the logs for the scheduler show the increased log level: 

     1. Get the list of pods running in the `openshift-numaresources` namespace by running the following command: 

```shell-session
$ oc get pods -n openshift-numaresources
```


**Example output**

```shell-session
NAME                                               READY   STATUS    RESTARTS   AGE
numaresources-controller-manager-d87d79587-76mrm   1/1     Running   0          46h
numaresourcesoperator-worker-5wm2k                 2/2     Running   0          45h
numaresourcesoperator-worker-pb75c                 2/2     Running   0          45h
secondary-scheduler-7976c4d466-qm4sc               1/1     Running   0          21m
```


     2. Get the logs for the secondary scheduler pod by running the following command: 

```shell-session
$ oc logs secondary-scheduler-7976c4d466-qm4sc -n openshift-numaresources
```


**Example output**

```shell-session
...
I0223 11:04:55.614788       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.Namespace total 11 items received
I0223 11:04:56.609114       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.ReplicationController total 10 items received
I0223 11:05:22.626818       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.StorageClass total 7 items received
I0223 11:05:31.610356       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.PodDisruptionBudget total 7 items received
I0223 11:05:31.713032       1 eventhandlers.go:186] "Add event for scheduled pod" pod="openshift-marketplace/certified-operators-thtvq"
I0223 11:05:53.461016       1 eventhandlers.go:244] "Delete event for scheduled pod" pod="openshift-marketplace/certified-operators-thtvq"
```


## 12.10.2. Change where high-performance workloads run

To optimize the processing of high-performance workloads, change the default placement behavior of the NUMA-aware secondary scheduler. With this configuration, you can assign workloads to a specific NUMA node within a compute node instead of relying on default resource availability. 

If you want to change where the workloads run, you can add the `scoringStrategy` setting to the `NUMAResourcesScheduler` custom resource and set its value to either `MostAllocated` or `BalancedAllocation`. 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * Logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Delete the currently running `NUMAResourcesScheduler` resource by using the following steps: 

     1. Get the active `NUMAResourcesScheduler` by running the following command: 

```shell-session
$ oc get NUMAResourcesScheduler
```


**Example output**

```shell-session
NAME                     AGE
numaresourcesscheduler   92m
```


     2. Delete the secondary scheduler resource by running the following command: 

```shell-session
$ oc delete NUMAResourcesScheduler numaresourcesscheduler
```


**Example output**

```shell-session
numaresourcesscheduler.nodetopology.openshift.io "numaresourcesscheduler" deleted
```


  2. Save the following YAML in the file `nro-scheduler-mostallocated.yaml`. This example changes the `scoringStrategy` to `MostAllocated`: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: numaresourcesscheduler
spec:
  imageSpec: "registry.redhat.io/openshift4/noderesourcetopology-scheduler-container-rhel8:v{product-version}"
  scoringStrategy:
        type: "MostAllocated"
# ...
```


`spec.imageSpec.scoringStrategy`: If the `scoringStrategy` configuration is omitted, the default of `LeastAllocated` applies. 

  3. Create the updated `NUMAResourcesScheduler` resource by running the following command: 

```shell-session
$ oc create -f nro-scheduler-mostallocated.yaml
```


**Example output**

```shell-session
numaresourcesscheduler.nodetopology.openshift.io/numaresourcesscheduler created
```


**Verification**

  1. Check that the NUMA-aware scheduler was successfully deployed by using the following steps: 

     1. Run the following command to check that the custom resource definition (CRD) is created successfully: 

```shell-session
$ oc get crd | grep numaresourcesschedulers
```


**Example output**

```shell-session
NAME                                                              CREATED AT
numaresourcesschedulers.nodetopology.openshift.io                 2022-02-25T11:57:03Z
```


     2. Check that the new custom scheduler is available by running the following command: 

```shell-session
$ oc get numaresourcesschedulers.nodetopology.openshift.io
```


**Example output**

```shell-session
NAME                     AGE
numaresourcesscheduler   3h26m
```


  2. Verify that the `ScoringStrategy` has been applied correctly by running the following command to check the relevant `ConfigMap` resource for the scheduler: 

```shell-session
$ oc get -n openshift-numaresources cm topo-aware-scheduler-config -o yaml | grep scoring -A 1
```


**Example output**

```shell-session
scoringStrategy:
  type: MostAllocated
```


## 12.10.3. Check the NUMA-aware scheduler logs

To troubleshoot problems with the NUMA-aware scheduler, review the scheduler logs. If necessary, increase the log level in the `NUMAResourcesScheduler` custom resource (CR) to capture more detailed diagnostic data. 

Acceptable values are `Normal`, `Debug`, and `Trace`, with `Trace` being the most verbose option. 

Note

To change the log level of the secondary scheduler, delete the running scheduler resource and re-deploy it with the changed log level. The scheduler is unavailable for scheduling new workloads during this downtime. 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Delete the currently running `NUMAResourcesScheduler` resource: 

     1. Get the active `NUMAResourcesScheduler` by running the following command: 

```shell-session
$ oc get NUMAResourcesScheduler
```


**Example output**

```shell-session
NAME                     AGE
numaresourcesscheduler   90m
```


     2. Delete the secondary scheduler resource by running the following command: 

```shell-session
$ oc delete NUMAResourcesScheduler numaresourcesscheduler
```


**Example output**

```shell-session
numaresourcesscheduler.nodetopology.openshift.io "numaresourcesscheduler" deleted
```


  2. Save the following YAML in the file `nro-scheduler-debug.yaml`. This example changes the log level to `Debug`: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: numaresourcesscheduler
spec:
  imageSpec: "registry.redhat.io/openshift4/noderesourcetopology-scheduler-container-rhel8:v4.22"
  logLevel: Debug
# ...
```


  3. Create the updated `Debug` logging `NUMAResourcesScheduler` resource by running the following command: 

```shell-session
$ oc create -f nro-scheduler-debug.yaml
```


**Example output**

```shell-session
numaresourcesscheduler.nodetopology.openshift.io/numaresourcesscheduler created
```


**Verification**

  1. Check that the NUMA-aware scheduler was successfully deployed: 

     1. Run the following command to check that the CRD is created successfully: 

```shell-session
$ oc get crd | grep numaresourcesschedulers
```


**Example output**

```shell-session
NAME                                                              CREATED AT
numaresourcesschedulers.nodetopology.openshift.io                 2022-02-25T11:57:03Z
```


     2. Check that the new custom scheduler is available by running the following command: 

```shell-session
$ oc get numaresourcesschedulers.nodetopology.openshift.io
```


**Example output**

```shell-session
NAME                     AGE
numaresourcesscheduler   3h26m
```


  2. Check that the logs for the scheduler shows the increased log level: 

     1. Get the list of pods running in the `openshift-numaresources` namespace by running the following command: 

```shell-session
$ oc get pods -n openshift-numaresources
```


**Example output**

```shell-session
NAME                                               READY   STATUS    RESTARTS   AGE
numaresources-controller-manager-d87d79587-76mrm   1/1     Running   0          46h
numaresourcesoperator-worker-5wm2k                 2/2     Running   0          45h
numaresourcesoperator-worker-pb75c                 2/2     Running   0          45h
secondary-scheduler-7976c4d466-qm4sc               1/1     Running   0          21m
```


     2. Get the logs for the secondary scheduler pod by running the following command: 

```shell-session
$ oc logs secondary-scheduler-7976c4d466-qm4sc -n openshift-numaresources
```


**Example output**

```shell-session
...
I0223 11:04:55.614788       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.Namespace total 11 items received
I0223 11:04:56.609114       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.ReplicationController total 10 items received
I0223 11:05:22.626818       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.StorageClass total 7 items received
I0223 11:05:31.610356       1 reflector.go:535] k8s.io/client-go/informers/factory.go:134: Watch close - *v1.PodDisruptionBudget total 7 items received
I0223 11:05:31.713032       1 eventhandlers.go:186] "Add event for scheduled pod" pod="openshift-marketplace/certified-operators-thtvq"
I0223 11:05:53.461016       1 eventhandlers.go:244] "Delete event for scheduled pod" pod="openshift-marketplace/certified-operators-thtvq"
```


## 12.10.4. Troubleshoot the resource topology exporter

To resolve unexpected results in `noderesourcetopologies` objects, inspect the `resource-topology-exporter` logs. Reviewing this diagnostic data helps you identify and fix configuration issues within your cluster. 

Note

Ensure that the NUMA resource topology exporter instances in the cluster are named for nodes they refer to. For example, a compute node with the name `worker` should have a corresponding `noderesourcetopologies` object called `worker`. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Get the daemonsets managed by the NUMA Resources Operator. Each daemonset has a corresponding `nodeGroup` in the `NUMAResourcesOperator` CR. Run the following command: 

```shell-session
$ oc get numaresourcesoperators.nodetopology.openshift.io numaresourcesoperator -o jsonpath="{.status.daemonsets[0]}"
```


**Example output**

```plaintext
{"name":"numaresourcesoperator-worker","namespace":"openshift-numaresources"}
```


  2. Get the label for the daemonset of interest using the value for `name` from the previous step: 

```shell-session
$ oc get ds -n openshift-numaresources numaresourcesoperator-worker -o jsonpath="{.spec.selector.matchLabels}"
```


**Example output**

```plaintext
{"name":"resource-topology"}
```


  3. Get the pods using the `resource-topology` label by running the following command: 

```shell-session
$ oc get pods -n openshift-numaresources -l name=resource-topology -o wide
```


**Example output**

```shell-session
NAME                                 READY   STATUS    RESTARTS   AGE    IP            NODE
numaresourcesoperator-worker-5wm2k   2/2     Running   0          2d1h   10.135.0.64   compute-0.example.com
numaresourcesoperator-worker-pb75c   2/2     Running   0          2d1h   10.132.2.33   compute-1.example.com
```


  4. Examine the logs of the `resource-topology-exporter` container running on the worker pod that corresponds to the node you are troubleshooting. Run the following command: 

```shell-session
$ oc logs -n openshift-numaresources -c resource-topology-exporter numaresourcesoperator-worker-pb75c
```


**Example output**

```shell-session
I0221 13:38:18.334140       1 main.go:206] using sysinfo:
reservedCpus: 0,1
reservedMemory:
  "0": 1178599424
I0221 13:38:18.334370       1 main.go:67] === System information ===
I0221 13:38:18.334381       1 sysinfo.go:231] cpus: reserved "0-1"
I0221 13:38:18.334493       1 sysinfo.go:237] cpus: online "0-103"
I0221 13:38:18.546750       1 main.go:72]
cpus: allocatable "2-103"
hugepages-1Gi:
  numa cell 0 -> 6
  numa cell 1 -> 1
hugepages-2Mi:
  numa cell 0 -> 64
  numa cell 1 -> 128
memory:
  numa cell 0 -> 45758Mi
  numa cell 1 -> 48372Mi
```


## 12.10.5. Correct a missing resource topology exporter config map

To correct a missing config map for the resource topology exporter (RTE), resolve misconfigured settings in your cluster. Fixing this issue ensures the NUMA Resources Operator functions properly when the logs of the RTE daemon set pods indicate missing configurations. 

The following example log message indicates a missing configuration: 

```plaintext
Info: couldn't find configuration in "/etc/resource-topology-exporter/config.yaml"
```


The previous log message indicates that the `kubeletconfig` with the required configuration was not properly applied in the cluster, resulting in a missing RTE `configmap`. For example, the following cluster is missing a `numaresourcesoperator-worker` `configmap` custom resource (CR): 

```shell-session
$ oc get configmap
```


Example output: 

```shell-session
NAME                           DATA   AGE
0e2a6bd3.openshift-kni.io      0      6d21h
kube-root-ca.crt               1      6d21h
openshift-service-ca.crt       1      6d21h
topo-aware-scheduler-config    1      6d18h
```


In a correctly configured cluster, `oc get configmap` also returns a `numaresourcesoperator-worker` `configmap` CR. 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * Logged in as a user with cluster-admin privileges. 
  * Installed the NUMA Resources Operator and deploy the NUMA-aware secondary scheduler. 



**Procedure**

  1. Compare the values for `spec.machineConfigPoolSelector.matchLabels` in `kubeletconfig` and `metadata.labels` in the `MachineConfigPool` (`mcp`) worker CR using the following commands: 

     1. Check the `kubeletconfig` labels by running the following command: 

```shell-session
$ oc get kubeletconfig -o yaml
```


**Example output**

```yaml
machineConfigPoolSelector:
  matchLabels:
    cnf-worker-tuning: enabled
```


     2. Check the `mcp` labels by running the following command: 

```shell-session
$ oc get mcp worker -o yaml
```


**Example output**

```yaml
labels:
  machineconfiguration.openshift.io/mco-built-in: ""
  pools.operator.machineconfiguration.openshift.io/worker: ""
```


The `cnf-worker-tuning: enabled` label is not present in the `MachineConfigPool` object. 

  2. Edit the `MachineConfigPool` CR to include the missing label, for example: 

```shell-session
$ oc edit mcp worker -o yaml
```


**Example output**

```yaml
labels:
  machineconfiguration.openshift.io/mco-built-in: ""
  pools.operator.machineconfiguration.openshift.io/worker: ""
  cnf-worker-tuning: enabled
```


  3. Apply the label changes and wait for the cluster to apply the updated configuration. 



**Verification**

  * Check that the missing `numaresourcesoperator-worker` `configmap` CR is applied: 

```shell-session
$ oc get configmap
```


**Example output**

```shell-session
NAME                           DATA   AGE
0e2a6bd3.openshift-kni.io      0      6d21h
kube-root-ca.crt               1      6d21h
numaresourcesoperator-worker   1      5m
openshift-service-ca.crt       1      6d21h
topo-aware-scheduler-config    1      6d18h
```


## 12.10.6. Collect NUMA Resources Operator data

You can use the `oc adm must-gather` CLI command to collect information about your cluster, including features and objects associated with the NUMA Resources Operator. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * To collect NUMA Resources Operator data with `must-gather`, you must specify the NUMA Resources Operator `must-gather` image. 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/openshift4/numaresources-must-gather-rhel9:v4.22
```
