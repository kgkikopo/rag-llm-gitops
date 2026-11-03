# Chapter 6. Control plane architecture

You can use a _control plane_ , which is composed of control plane machines, to manage the OpenShift Container Platform cluster. The control plane machines manage workloads on the compute machines, which are also known as worker machines. 

The cluster manages all upgrades to the machines by the actions of the Cluster Version Operator (CVO), the Machine Config Operator, and a set of individual Operators.

- [6.1. Node configuration management with machine config pools](06_01_node_configuration_management_with_machine_config_pools.md)
- [6.2. Machine roles in OpenShift Container Platform](06_02_machine_roles_in_openshift_container_platform.md)
- [6.3. Operators in OpenShift Container Platform](06_03_operators_in_openshift_container_platform.md)
- [6.4. etcd key-value store](06_04_etcd_key_value_store.md)
