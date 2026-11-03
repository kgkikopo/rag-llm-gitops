# 15.5. Use the eBPF agent alert

Resolve the `NetObservAgentFlowsDropped` alert, which occurs when the eBPF agent hashmap is full, by increasing the `spec.agent.ebpf.cacheMaxFlows` value in the `FlowCollector` custom resource. 

An alert, `NetObservAgentFlowsDropped`, is also triggered when the capacity limiter is triggered. If you see this alert, consider increasing the `cacheMaxFlows` in the `FlowCollector`, as shown in the following example. 

Note

Increasing the `cacheMaxFlows` might increase the memory usage of the eBPF agent. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **Network Observability Operator** , select **Flow Collector**. 
  3. Select **cluster** , and then select the **YAML** tab. 
  4. Increase the `spec.agent.ebpf.cacheMaxFlows` value, as shown in the following YAML sample: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  agent:
    type: eBPF
    ebpf:
      cacheMaxFlows: 200000
```


where: 

`spec.agent.ebpf.cacheMaxFlows`
     Specifies the maximum number of flows to cache. If a `NetObservAgentFlowsDropped` alert occurs, increase this value from its current level. 




**Additional resources**

  * [Creating alerting rules for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/managing_alerts/managing-alerts-as-a-developer#creating-alerting-rules-for-user-defined-projects_managing-alerts-as-a-developer)
