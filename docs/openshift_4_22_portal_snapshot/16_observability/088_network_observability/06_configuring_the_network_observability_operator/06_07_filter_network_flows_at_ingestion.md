# 6.7. Filter network flows at ingestion

Create filters to reduce the number of generated network flows. Filtering network flows can reduce the resource usage of the network observability components. 

You can configure two kinds of filters: 

  * eBPF agent filters 
  * Flowlogs-pipeline filters 



## 6.7.1. eBPF agent filters

eBPF agent filters maximize performance because they take effect at the earliest stage of the network flows collection process. 

To configure eBPF agent filters with the Network Observability Operator, see "Filtering eBPF flow data using multiple rules". 

## 6.7.2. Flowlogs-pipeline filters

Flowlogs-pipeline filters provide greater control over traffic selection because they take effect later in the network flows collection process. They are primarily used to improve data storage. 

Flowlogs-pipeline filters use a simple query language to filter network flow, as shown in the following example: 

```shell-session
(srcnamespace="netobserv" OR (srcnamespace="ingress" AND dstnamespace="netobserv")) AND srckind!="service"
```


The query language uses the following syntax: 

Table 6.1. Query language syntaxCategory| Operators  
---|---  
Logical boolean operators (not case-sensitive)  |  `and`, `or`  
Comparison operators  |  `=` (equals), `!=` (not equals), `=~` (matches regexp), `!~` (not matches regexp), `<` / `<=` (less than or equal to), `>` / `>=` (greater than or equal to)   
Unary operations  |  `with(field)` (field is present), `without(field)` (field is absent)   
Parenthesis-based priority  |  N/A   
Show more

You can configure flowlogs-pipeline filters in the `spec.processor.filters` section of the `FlowCollector` resource. For example: 

**Example YAML Flowlogs-pipeline filter**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  agent:
  processor:
    filters:
      - query: |
          (SrcK8S_Namespace="netobserv" OR (SrcK8S_Namespace="openshift-ingress" AND DstK8S_Namespace="netobserv"))
        outputTarget: Loki
        sampling: 10
```


where: 

`spec.processor.filters.outputTarget`
     Specifies the output destination for matching flows, such as `Loki`, `Prometheus`, or an external system. If you omit this parameter, the system sends the flows to all configured outputs. 
`spec.processor.filters.sampling`
     Specifies an optional sampling interval to limit the number of matching flows stored or exported. For example, a value of `10` means there is a 1 in 10 chance that a flow is kept. 

**Additional resources**

  * [Filtering eBPF flow data using multiple rules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/nw-observe-network-traffic#network-observability-filtering-ebpf-rule_nw-observe-network-traffic "11.1.10. Filter eBPF flow data using multiple rules")
