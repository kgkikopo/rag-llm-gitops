# Chapter 16. Scheduling resources

Taints and tolerations help you control which nodes host certain pods. Use these tools, along with node selectors, to guide the placement of network observability components. 

A node selector specifies a map of key/value pairs that are defined using custom labels on nodes and selectors specified in pods. 

For the pod to be eligible to run on a node, the pod must have the same key/value node selector as the label on the node.

- [16.1. Network observability deployment in specific nodes](16_01_network_observability_deployment_in_specific_nodes.md)
