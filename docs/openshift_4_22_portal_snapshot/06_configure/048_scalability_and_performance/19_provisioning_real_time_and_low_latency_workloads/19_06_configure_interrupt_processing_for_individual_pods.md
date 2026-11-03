# 19.6. Configure interrupt processing for individual pods

To achieve low latency for workloads, some containers require that the CPUs they are pinned to do not process device interrupts. You can use the `irq-load-balancing.crio.io` pod annotation to control whether device interrupts are processed on CPUs where the pinned containers are running. 

The annotation supports the following values: 

`disable`
     Disables IRQ load balancing for all CPUs allocated to the container. Use this value for latency-sensitive workloads when you want to exclude container CPUs from interrupt handling. 
`housekeeping`
     Preserves IRQ handling on the first CPU that is allocated to the container, including that CPU’s thread siblings. The subsequent CPUs allocated to the container are excluded from interrupt processing. This configuration also injects the `OPENSHIFT_HOUSEKEEPING_CPUS` environment variable into the container. Use this variable to see which CPUs are designated for housekeeping tasks. 

You can use the `housekeeping` value to reduce the overall CPU footprint by allowing a small subset of container CPUs to handle both application housekeeping work and system interrupts. 

Note

When using the `housekeeping` value, the CPUs designated for housekeeping handle interrupts for the entire system. 

**Prerequisites**

  * You configured a performance profile for the node. 
  * You set the `globallyDisableIrqLoadBalancing` field to `false` in the performance profile. 



**Procedure**

  1. Create the `Pod` resource and configure the `irq-load-balancing.crio.io` annotation: 

**Example pod specification**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dpdk-workload
  annotations:
    irq-load-balancing.crio.io: "disable"
spec:
  runtimeClassName: performance-<profile_name>
  containers:
  - name: app
    image: example-image
    resources:
      requests:
        cpu: "8"
        memory: "4Gi"
      limits:
        cpu: "8"
        memory: "4Gi"
```


     * `metadata.annotations.irq-load-balancing.crio.io`: Specifies if device interrupts are processed on the container CPUs. Set to `disable` to prevent all container CPUs from handling IRQs, or set to `housekeeping` to allow the first allocated CPU and its thread siblings to handle IRQs while excluding the remaining CPUs from IRQ handling. 
     * `spec.runtimeClassName`: Specifies the runtime class for the performance profile. Replace `<profile_name>` with the name of your performance profile. 

  2. Apply the `Pod` resource by running the following command: 

```shell-session
$ oc apply -f pod.yaml
```


**Verification**

  1. Verify the CPUs assigned to the pod: 

```shell-session
$ oc exec <pod_name> -- cat /sys/fs/cgroup/cpuset.cpus
```


  2. For pods using the `housekeeping` annotation, verify the housekeeping CPU environment variable: 

```shell-session
$ oc exec <pod_name> -- printenv OPENSHIFT_HOUSEKEEPING_CPUS
```


Replace `<pod_name>` with the name of the pod. 

  3. On the worker node, verify the CPUs excluded from IRQ handling: 

```shell-session
$ grep IRQBALANCE_BANNED_CPUS /etc/sysconfig/irqbalance
```


The output is a hexadecimal bitmask representing the CPUs excluded from IRQ handling. 




**Additional resources**

  * [Managing device interrupt processing for guaranteed pod isolated CPUs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#managing-device-interrupt-processing-for-guaranteed-pod-isolated-cpus_cnf-tuning-low-latency-nodes-with-perf-profile "17.11. Managing device interrupt processing for guaranteed pod isolated CPUs")
