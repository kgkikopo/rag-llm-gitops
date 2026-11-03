# Chapter 1. Observing and updating the node network state and configuration

To observe and update the node network state and configuration in your cluster, you can use the Kubernetes NMState Operator. You can view network states, create and manage network configuration policies, and configure interfaces on cluster nodes. 

For more information about how to install the NMState Operator, see [Kubernetes NMState Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#k8s-nmstate-about-the-k8s-nmstate-operator). 

Important

You cannot modify an existing `br-ex` bridge, an OVN-Kubernetes-managed Open vSwitch bridge, or any interfaces, bonds, VLANs, and so on that associate with the `br-ex` bridge. However, you can configure a customized br-ex bridge. 

For more information, see "Creating a manifest object that includes a customized br-ex bridge" in the _Deploying installer-provisioned clusters on bare metal_ document or the _Installing a user-provisioned cluster on bare metal_ document.

- [1.1. View the network state of a node by using the CLI](01_01_view_the_network_state_of_a_node_by_using_the_cli.md)
- [1.2. View a graphical representation of the network state of a node (NNS) topology from the web console](01_02_view_a_graphical_representation_of_the_network_state_of_a_node_nns_topology_from_the_web_console.md)
- [1.3. View the list of NodeNetworkState resources](01_03_view_the_list_of_nodenetworkstate_resources.md)
- [1.4. About the NodeNetworkConfigurationPolicy manifest file](01_04_about_the_nodenetworkconfigurationpolicy_manifest_file.md)
- [1.5. Manage policy from the web console](01_05_manage_policy_from_the_web_console.md)
- [1.6. Update the NodeNetworkConfigurationPolicy manifest file](01_06_update_the_nodenetworkconfigurationpolicy_manifest_file.md)
- [1.7. Manage the NodeNetworkConfigurationPolicy manifest file](01_07_manage_the_nodenetworkconfigurationpolicy_manifest_file.md)
- [1.8. Configure alternative network interface names](01_08_configure_alternative_network_interface_names.md)
- [1.9. Example policy configurations for different interfaces](01_09_example_policy_configurations_for_different_interfaces.md)
- [1.10. Create an IP over InfiniBand interface on nodes](01_10_create_an_ip_over_infiniband_interface_on_nodes.md)
- [1.11. Example policy configurations that use dynamic matching and templating](01_11_example_policy_configurations_that_use_dynamic_matching_and_templating.md)
- [1.12. Examples: IP management](01_12_examples_ip_management.md)
- [1.13. Enable IP forwarding on specific interfaces](01_13_enable_ip_forwarding_on_specific_interfaces.md)
- [1.14. Routes and route rules](01_14_routes_and_route_rules.md)
