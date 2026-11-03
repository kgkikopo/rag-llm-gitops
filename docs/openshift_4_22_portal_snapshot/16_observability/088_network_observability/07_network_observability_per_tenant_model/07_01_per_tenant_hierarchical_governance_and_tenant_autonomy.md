# 7.1. Per-tenant hierarchical governance and tenant autonomy

Cluster administrators can maintain global governance while allowing project administrators to manage network traffic observability within their specific namespaces. 

The Network Observability Operator uses a hierarchical configuration model to support multitenancy. This architecture is beneficial for large-scale deployments and hosted control planes environments where individual teams require self-service visibility without cluster administrator intervention. 

The hierarchical model consists of the following components: 

Global governance
     The cluster administrator manages the global `FlowCollector` resource. This resource defines the observability infrastructure and determines if per-tenant configuration is permitted. 
Tenant autonomy
     The project administrator manages the `FlowCollectorSlice` resource. This namespace-scoped custom resource (CR) allows teams to define specific observability settings for their workloads.
