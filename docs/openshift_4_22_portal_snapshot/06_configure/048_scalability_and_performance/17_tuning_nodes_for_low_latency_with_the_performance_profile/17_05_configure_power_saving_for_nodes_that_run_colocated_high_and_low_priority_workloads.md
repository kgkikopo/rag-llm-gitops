# 17.5. Configure power saving for nodes that run colocated high and low priority workloads

You can enable power savings for a node that has low priority workloads that are colocated with high priority workloads without impacting the latency or throughput of the high priority workloads. Power saving is possible without modifications to the workloads themselves. 

Important

The feature is supported on Intel Ice Lake and later generations of Intel CPUs. The capabilities of the processor might impact the latency and throughput of the high priority workloads. 

**Prerequisites**

  * You enabled C-states and operating system controlled P-states in the BIOS 



**Procedure**

  1. Generate a `PerformanceProfile` with the `per-pod-power-management` argument set to `true`: 

```shell-session
$ podman run --entrypoint performance-profile-creator -v \
/must-gather:/must-gather:z registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.22 \
--mcp-name=worker-cnf --reserved-cpu-count=20 --rt-kernel=true \
--split-reserved-cpus-across-numa=false --topology-manager-policy=single-numa-node \
--must-gather-dir-path /must-gather --power-consumption-mode=low-latency \
--per-pod-power-management=true > my-performance-profile.yaml
```


The `power-consumption-mode` argument must be `default` or `low-latency` when the `per-pod-power-management` argument is set to `true`. 

**Example`PerformanceProfile` with `perPodPowerManagement`**

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
     name: performance
spec:
    [.....]
    workloadHints:
        realTime: true
        highPowerConsumption: false
        perPodPowerManagement: true
# ...
```


  2. Set the default `cpufreq` governor as an additional kernel argument in the `PerformanceProfile` custom resource (CR): 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
     name: performance
spec:
    ...
    additionalKernelArgs:
    - cpufreq.default_governor=schedutil
# ...
```


where: 

`cpufreq.default_governor=schedutil`
     Specifies using the `schedutil` governor. You can use other governors, such as the `ondemand` or `powersave` governors. 

  3. Set the maximum CPU frequency in the `TunedPerformancePatch` CR: 

```yaml
spec:
  profile:
  - data: |
      [sysfs]
      /sys/devices/system/cpu/intel_pstate/max_perf_pct = <x>
```


where: 

`/sys/devices/system/cpu/intel_pstate/max_perf_pct`
     Specifies the `max_perf_pct` that controls the maximum frequency that the `cpufreq` driver is allowed to set as a percentage of the maximum supported cpu frequency. This value applies to all CPUs. You can check the maximum supported frequency in `/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq`. As a starting point, you can use a percentage that caps all CPUs at the `All Cores Turbo` frequency. The `All Cores Turbo` frequency is the frequency that all cores will run at when the cores are all fully occupied.
