# 17.4. Node power consumption and realtime processing with workload hints

You can create a performance profile appropriate for the hardware and topology of an environment by using the Performance Profile Creator (PPC) tool. 

The following table describes the possible values set for the `power-consumption-mode` flag associated with the PPC tool and the workload hint that is applied. 

Table 17.3. Impact of combinations of power consumption and real-time settings on latencyPerformance Profile creator setting| Hint| Environment| Description  
---|---|---|---  
Default  |  `workloadHints: highPowerConsumption: false realTime: false` |  High throughput cluster without latency requirements  |  Performance achieved through CPU partitioning only.   
Low-latency  |  `workloadHints: highPowerConsumption: false realTime: true` |  Regional data-centers  |  Both energy savings and low-latency are desirable: compromise between power management, latency and throughput.   
Ultra-low-latency  |  `workloadHints: highPowerConsumption: true realTime: true` |  Far edge clusters, latency critical workloads  |  Optimized for absolute minimal latency and maximum determinism at the cost of increased power consumption.   
Per-pod power management  |  `workloadHints: realTime: true highPowerConsumption: false perPodPowerManagement: true` |  Critical and non-critical workloads  |  Allows for power management per pod.   
Show more

The following configuration is commonly used in a telco RAN DU deployment: 

```yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: workload-hints
    spec:
      ...
      workloadHints:
        realTime: true
        highPowerConsumption: false
        perPodPowerManagement: false
```


`perPodPowerManagement`
     Specifies to disable some debugging and monitoring features that can affect system latency. 

Note

If you do not set the `realTime` workload hint, the hint defaults to `true`. 

For more information about how combinations of power consumption and real-time settings impact latency, see "Understanding workload hints". 

**Additional resources**

  * [Understanding workload hints](https://access.redhat.com/articles/7081587)
