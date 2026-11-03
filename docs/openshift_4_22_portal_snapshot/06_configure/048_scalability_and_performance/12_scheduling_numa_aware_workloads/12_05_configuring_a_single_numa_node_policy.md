# 12.5. Configuring a single NUMA node policy

To enable the NUMA Resources Operator, configure a single NUMA node policy on your cluster. You can implement this policy by creating a performance profile or by configuring a `KubeletConfig` custom resource (CR). 

Note

The preferred way to configure a single NUMA node policy is to apply a performance profile. You can use the Performance Profile Creator (PPC) tool to create the performance profile. If a performance profile is created on the cluster, the PPC tool automatically creates other tuning components like `KubeletConfig` and the `tuned` profile. 

For more information about creating a performance profile, see "About the Performance Profile Creator" in the "Additional resources" section. 

## 12.5.1. Managing high availability (HA) for the NUMA-aware scheduler

To ensure high availability for the NUMA-aware secondary scheduler, the NUMA Resources Operator automatically creates scheduler replicas on control plane nodes. The Operator manages this configuration by using the `spec.replicas` field in the `NUMAResourcesScheduler` custom resource (CR). 

By default, the NUMA Resources Operator automatically enables HA mode by creating one scheduler replica for each control plane node, with a maximum of three replicas. 

The following manifest demonstrates the default behavior. To automatically enable replica detection, omit the `replicas` field. 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: example-auto-ha
spec:
  imageSpec: 'registry.redhat.io/openshift4/noderesourcetopology-scheduler-rhel9:v4.22'
  # The 'replicas' field is not included, enabling auto-detection.
```


You can control scheduler behavior by using one of the following options: 

  * Customizing the number of replicas. 
  * Disabling NUMA-aware scheduling. 



### 12.5.1.1. Customize scheduler replicas

You can set a specific number of scheduler replicas by updating the `spec.replicas` field in the `NUMAResourcesScheduler` custom resource. This configuration overrides the default HA behavior. 

**Procedure**

  1. Create the `NUMAResourcesScheduler` CR with the following YAML named for example `custom-ha.yaml` that sets the number of replicas to 2: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: example-custom
spec:
  imageSpec: 'registry.redhat.io/openshift4/noderesourcetopology-scheduler-rhel9:v4.22'
  replicas: 2
# ...
```


  2. Deploy the NUMA-aware pod scheduler by running the following command: 

```shell-session
$ oc apply -f custom-ha.yaml
```


### 12.5.1.2. Disable NUMA-aware scheduling

You can disable the NUMA-aware scheduler to stop all running scheduler pods and preventing new ones from starting. 

**Procedure**

  1. Save the following minimal required YAML in the `nro-disable-scheduler.yaml` file. Disable the scheduler by setting the `spec.replicas` field to `0`. 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: example-disable
spec:
  imageSpec: 'registry.redhat.io/openshift4/noderesourcetopology-scheduler-rhel9:v4.22'
  replicas: 0
# ...
```


  2. Disable the NUMA-aware pod scheduler by running the following command: 

```shell-session
$ oc apply -f nro-disable-scheduler.yaml
```


### 12.5.1.3. Verify scheduler high availability (HA) status

You can verify the status of the NUMA-aware scheduler to ensure the scheduler is running with the expected number of replicas based on your configuration. 

**Procedure**

  1. List only the scheduler pods by running the following command: 

```shell-session
$ oc get pods -n openshift-numaresources -l app=secondary-scheduler
```


**Expected output**

```shell-session
NAME                                   READY   STATUS    RESTARTS   AGE
secondary-scheduler-5b8c9d479d-2r4p5   1/1     Running   0          5m
secondary-scheduler-5b8c9d479d-k2f3p   1/1     Running   0          5m
secondary-scheduler-5b8c9d479d-q8c7b   1/1     Running   0          5m
```


Using the default HA mode, the number of pods equals the number of control-plane nodes. A standard HA OpenShift Container Platform cluster typically has three control-plane nodes, and therefore displays three pods. If you **customized the replicas** , the number of pods matches the value you set. If you **disabled the scheduler** , there are no running pods with this label. 

Note

A limit of 3 replicas is enforced for the NUMA-aware scheduler. On a hosted control planes cluster, the scheduler pods run on the compute nodes of the hosted-cluster. 

  2. Verify the number of replicas and their status by running the following command: 

```shell-session
$ oc get deployment secondary-scheduler -n openshift-numaresources
```


**Example output**

```shell-session
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
secondary-scheduler   3/3     3            3           5m
```


In this output, 3/3 means 3 replicas are ready out of an expected 3 replicas. 

  3. For more detailed information run the following command: 

```shell-session
$ oc describe deployment secondary-scheduler -n openshift-numaresources
```


**Example output**

```yaml
Replicas:        3 desired | 3 updated | 3 total | 3 available | 0 unavailable
```


The `Replicas` line shows a deployment configured for 3 replicas, with all 3 updated and available. 




**Additional resources**

  * [Configuring image registry repository mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#images-configuration-registry-mirror-configuring_updating-disconnected-cluster)
  * [About the Performance Profile Creator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-about-the-profile-creator-tool_cnf-tuning-low-latency-nodes-with-perf-profile "17.1.1. About the Performance Profile Creator")



## 12.5.2. Sample performance profile

Reference an example YAML to understand how to use the performance profile creator (PPC) tool to create a performance profile. 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: performance
spec:
  cpu:
    isolated: "3"
    reserved: 0-2
  machineConfigPoolSelector:
    pools.operator.machineconfiguration.openshift.io/worker: ""
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  numa:
    topologyPolicy: single-numa-node
  realTimeKernel:
    enabled: true
  workloadHints:
    highPowerConsumption: true
    perPodPowerManagement: false
    realTime: true
```


where: 

`spec.pools.operator.machineconfiguration.openshift.io/worker`
     Specifies the value that must match the `MachineConfigPool` value that you want to configure the NUMA Resources Operator on. For example, you might create a `MachineConfigPool` object named `worker-cnf` that designates a set of nodes that run telecommunications workloads. The value for `MachineConfigPool` must match the `machineConfigPoolSelector` value in the `NUMAResourcesOperator` CR that you configure later in "Creating the NUMAResourcesOperator custom resource". 
`spec.numa.topologyPolicy`
    

Specifies that the `topologyPolicy` field is set to `single-numa-node` by setting the `topology-manager-policy` argument to `single-numa-node` when you run the PPC tool. 

Note

For hosted control plane clusters, the `machineConfigPoolSelector` does not have any functional effect. Node association is instead determined by the specified `NodePool` object. 

## 12.5.3. Create a KubeletConfig CR

To configure a single NUMA node policy, create and apply a KubeletConfig custom resource (CR). While applying a performance profile is recommended, you can use the alternative method to manually manage the configuration on your cluster. 

**Procedure**

  1. Create the `KubeletConfig` custom resource (CR) that configures the pod admittance policy for the machine profile: 

     1. Save the following YAML in the `nro-kubeletconfig.yaml` file: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: worker-tuning
spec:
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/worker: ""
  kubeletConfig:
    cpuManagerPolicy: "static"
    cpuManagerReconcilePeriod: "5s"
    reservedSystemCPUs: "0,1"
    memoryManagerPolicy: "Static"
    evictionHard:
      memory.available: "100Mi"
    kubeReserved:
      memory: "512Mi"
    reservedMemory:
      - numaNode: 0
        limits:
          memory: "1124Mi"
    systemReserved:
      memory: "512Mi"
    topologyManagerPolicy: "single-numa-node"
```


where: 

`spec.machineConfigPoolSelector.matchLabels.pools.operator.machineconfiguration.openshift.io/worker`
     Specifies that this label matches the `machineConfigPoolSelector` setting in the `NUMAResourcesOperator` CR that you configure later in "Creating the NUMAResourcesOperator custom resource". 
`spec.kubeletConfig.cpuManagerPolicy`
     Specifies the `static` value. You must use a lowercase `s`. 
`spec.kubeletConfig.reservedSystemCPUs`
     Adjust the field based on the CPU on your nodes. 
`spec.kubeletConfig.memoryManagerPolicy`
     Specifies `Static`. You must use an uppercase `S`. 
`spec.kubeletConfig.topologyManagerPolicy`
    

Specifies the value as `single-numa-node`. 

Note

For hosted control plane clusters, the `machineConfigPoolSelector` setting does not have any functional effect. Node association is instead determined by the specified `NodePool` object. To apply a `KubeletConfig` for hosted control plane clusters, you must create a `ConfigMap` that contains the configuration, and then reference that `ConfigMap` within the `spec.config` field of a `NodePool`. 

     2. Create the `KubeletConfig` CR by running the following command: 

```shell-session
$ oc create -f nro-kubeletconfig.yaml
```


Note

Applying performance profile or `KubeletConfig` automatically triggers rebooting of the nodes. If no reboot is triggered, you can troubleshoot the issue by looking at the labels in `KubeletConfig` that address the node group.
