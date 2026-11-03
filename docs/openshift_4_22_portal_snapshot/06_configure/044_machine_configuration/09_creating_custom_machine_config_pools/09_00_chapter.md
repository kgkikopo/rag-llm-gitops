# Chapter 9. Creating custom machine config pools

You can create custom machine config pools (MCP) to manage compute nodes for custom use cases that extend outside of the default node types. By using a custom machine config pool, you can deploy changes targeted only at nodes in the custom pool. 

Custom machine config pools inherit their configurations from the `worker` machine config pool. Changes made to the `worker` machine config pool apply to nodes in the custom pool. However, changes made to the custom machine config pool apply only to the nodes in the custom pool. For more information on custom machine config pools, see "Node configuration management with machine config pools". 

Note

Custom machine config pools for the control plane nodes are not supported. 

For example, you could use a custom machine config pool to create an _infrastructure_ node. Components that you move to an infrastructure node do not need to be accounted for during sizing. For more information on infrastructure nodes, see "Creating infrastructure machine sets". 

After you create the custom machine config pool, you can boot new nodes directly to the pool by creating a new machine set. Or, you can add existing nodes to the custom pool by using labels.

- [9.1. Create a custom machine config pool with a new node](09_01_create_a_custom_machine_config_pool_with_a_new_node.md)
- [9.2. Create a custom machine config pool for an existing node](09_02_create_a_custom_machine_config_pool_for_an_existing_node.md)
- [9.3. Additional resources](09_03_additional_resources.md)
