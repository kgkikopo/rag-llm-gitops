# 6.1. View the FlowCollector resource

View and modify the `FlowCollector` resource in the OpenShift Container Platform web console through the integrated setup, advanced form, or by editing the YAML directly to configure the Network Observability Operator. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. There, you can modify the `FlowCollector` resource to configure the Network Observability Operator. 



## 6.1.1. Example of a FlowCollector resource

Review a comprehensive, annotated example of the `FlowCollector` custom resource that demonstrates configurations for `eBPF` sampling, conversation tracking, Loki integration, and console quick filters. 

### 6.1.1.1. Sample FlowCollector resource

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  networkPolicy:
    enable: true
  agent:
    type: eBPF
    ebpf:
      sampling: 50
      privileged: false
      features: []
  processor:
    addZone: false
    subnetLabels:
      openShiftAutoDetect: true
      customLabels: []
    consumerReplicas: 3
  loki:
    enable: true
    mode: LokiStack
    lokiStack:
      name: loki
      namespace: netobserv-loki
  consolePlugin:
    enable: true
  exporters: []
```


where: 

`spec.agent.type`
     Must be `eBPF` as eBPF is the only OpenShift Container Platform supported option. 
`spec.agent.ebpf.sampling`
     Specifies the sampling interval. By default, eBPF sampling is set to `50`, so a packet has a 1 in 50 chance of being sampled. A lower sampling interval value requires more computational, memory, and storage resources. A value of `0` or `1` means all packets are sampled. It is recommended to start with the default value and refine it empirically to determine the optimal setting for your cluster. 
`spec.agent.ebpf.privileged`
     Specifies if the eBPF agent pods should run as privileged. Running as privileged is required for several features, such as monitoring non-default networks and tracking packet drops. For security, in accordance with the principle of least privilege, it should only be enabled when some of those features are desired. A warning will be displayed if you enabled a feature requiring privileged mode without setting it to true explicitly. 
`spec.processor.addZone`
     Used to inject cloud availability zones in network flows. 
`spec.processor.subnetLabels`
     Specifies a list of customized labels to inject in network flows, based on CIDR matching. 
`spec.processor.consumerReplicas`
     Specifies the number of replicas for the processor pods (flowlogs-pipeline). Refer to the Resource management and performance considerations section for recommendations based on the cluster size. 
`spec.loki.mode`
     Specifies how to configure the connection to Loki, depending on its installation mode. If you use the install paths described in "Installing the Loki Operator", the mode must be set to `LokiStack`, and `spec.loki.lokiStack` should refer to the installed `LokiStack` resource name and namespace. 
`spec.loki.lokistack.namespace`
     Specifies the namespace for the `LokiStack` resource. This value must match the `metadata.namespace` defined in the `LokiStack` custom resource. While this example uses `netobserv-loki`, you can use a different namespace for different components. 

**Additional resources**

  * [`FlowCollector` API reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-api-reference#flowcollector-api_network_observability "19.1.1. FlowCollector API")
  * [Working with conversation tracking](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-observe-network-traffic#network-observability-working-with-conversations_nw-observe-network-traffic "11.2.5. Work with conversation tracking")
