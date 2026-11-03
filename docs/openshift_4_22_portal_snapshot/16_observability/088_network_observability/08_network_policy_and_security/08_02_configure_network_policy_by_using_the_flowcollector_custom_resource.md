# 8.2. Configure network policy by using the FlowCollector custom resource

Configure ingress and egress network policies to control pod traffic for network observability components. Network policies enhance security, reduce noise, support compliance, and improve visibility into network communication. 

You can configure the `FlowCollector` custom resource (CR) to deploy network policies for network observability. By default, network policy management is enabled. 

**Prerequisites**

  * You have installed the Network Observability Operator. 
  * You have cluster administrator permissions. 



**Procedure**

  1. In the web console, go to **Ecosystem** **Installed Operators** page. 
  2. Under the **Provided APIs** heading for **Network Observability** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. 
  4. Configure the `FlowCollector` CR. A sample configuration is as follows: 

**Example`FlowCollector` CR for network policy**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  networkPolicy:
    enable: true
    additionalNamespaces: ["my-kafka-exporter"]
# ...
```


where: 

`spec.networkPolicy.enable`
     Specifies whether to enable network policy management. The default value is `true`. 
`spec.networkPolicy.additionalNamespaces`
     Specifies additional namespaces to include in the network policy. Use this parameter to add namespaces where flows are exported. For example, if you configured `spec.exporters` to a Kafka broker in a namespace such as `my-kafka-exporter`, you should include that namespace in the list.
