# Chapter 4. Understanding Windows container workloads

You can use the Windows Machine Config Operator (WMCO) to run Microsoft Windows Server containers on OpenShift Container Platform. 

For those that administer heterogeneous environments with a mix of Linux and Windows workloads, OpenShift Container Platform allows you to deploy Windows workloads running on Windows Server containers while also providing traditional Linux workloads hosted on Red Hat Enterprise Linux CoreOS (RHCOS) or Red Hat Enterprise Linux (RHEL). 

Note

Multi-tenancy for clusters that have Windows nodes is not supported. Clusters are considered _multi-tenant_ when multiple workloads operate on shared infrastructure and resources. If one or more workloads running on an infrastructure cannot be trusted, the multi-tenant environment is considered _hostile_. 

Hostile multi-tenant clusters introduce security concerns in all Kubernetes environments. Additional security features, such as pod security policies or more fine-grained role-based access control (RBAC) for nodes, make exploiting your environment more difficult. However, if you choose to run hostile multi-tenant workloads, a hypervisor is the only security option you should use. The security domain for Kubernetes encompasses the entire cluster, not an individual node. For these types of hostile multi-tenant workloads, you should use physically isolated clusters. 

Windows Server Containers provide resource isolation using a shared kernel but are not intended to be used in hostile multitenancy scenarios.

- [4.1. Windows workload management](04_01_windows_workload_management.md)
- [4.2. Windows node services](04_02_windows_node_services.md)
- [4.3. Additional resources](04_03_additional_resources.md)
