# 19.1. Network observability API specifications

Reference documentation for Network Observability custom resources and flow data formats. 

## 19.1.1. FlowCollector API

The `FlowCollector` resource configures the Network Observability Operator. 

  * [FlowCollector API for network observability 2.0](https://github.com/openshift/network-observability-operator/blob/release-2.0/docs/flowcollector-flows-netobserv-io-v1beta2.adoc)
  * [FlowCollector API for network observability 1.12](https://github.com/openshift/network-observability-operator/blob/release-1.12/docs/flowcollector-flows-netobserv-io-v1beta2.adoc)



## 19.1.2. FlowMetric API

The `FlowMetric` resource creates custom metrics from collected flow logs. 

  * [FlowMetric API for network observability 2.0](https://github.com/openshift/network-observability-operator/blob/release-2.0/docs/flowmetric-flows-netobserv-io-v1alpha1.adoc)
  * [FlowMetric API for network observability 1.12](https://github.com/openshift/network-observability-operator/blob/release-1.12/docs/flowmetric-flows-netobserv-io-v1alpha1.adoc)



## 19.1.3. FlowCollectorSlice API

The `FlowCollectorSlice` resource enables per-tenant flow collection configuration. 

  * [FlowCollectorSlice API for network observability 2.0](https://github.com/openshift/network-observability-operator/blob/release-2.0/docs/FlowCollectorSlice.md)
  * [FlowCollectorSlice API for network observability 1.12](https://github.com/openshift/network-observability-operator/blob/release-1.12/docs/FlowCollectorSlice.md)



## 19.1.4. Network flows format

The network flows format reference describes the structure and fields of flow data. 

  * [Network flows format reference for network observability 2.0](https://github.com/openshift/network-observability-operator/blob/release-2.0/docs/flows-format.adoc)
  * [Network flows format reference for network observability 1.12](https://github.com/openshift/network-observability-operator/blob/release-1.12/docs/flows-format.adoc)



## 19.1.5. Network Observability CLI usage

The Network Observability CLI (`oc netobserv`) provides feature and filtering parity with the Network Observability Operator. Use command-line arguments to dynamically toggle features and isolate specific cluster network traffic flows. 

  * [Network Observability CLI usage](https://github.com/netobserv/netobserv-cli/blob/main/docs/netobserv_cli.adoc)
