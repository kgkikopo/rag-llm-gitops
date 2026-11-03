# 2.1. Network Observability Operator

The Network Observability Operator monitors and analyzes cluster network traffic by deploying eBPF-based flow collection that captures, enriches, and stores network data for troubleshooting and performance analysis. 

A `FlowCollector` instance deploys pods and services that form a monitoring pipeline. 

The `eBPF` agent is deployed as a `daemonset` object and creates the network flows. The pipeline collects and enriches network flows with Kubernetes metadata before storing them in Loki or generating Prometheus metrics.
