# Chapter 8. Creating infrastructure machine sets

To reduce subscription costs, you can use infrastructure machine sets to create machines that host only infrastructure components, such as the default router, the integrated container image registry, cluster metrics, and monitoring. These infrastructure machines are not counted toward the total number of subscriptions that are required to run the environment. 

For information about infrastructure nodes and which components can run on infrastructure nodes, see the "Red Hat OpenShift control plane and infrastructure nodes" section in the OpenShift sizing and subscription guide for enterprise Kubernetes document. 

To create an infrastructure node, see "Creating a compute machine set", "Creating an infrastructure node", or "Creating an infrastructure node". Use the sample compute machine set for your cloud to deploy an infrastructure machine set. Modify the sample configuration file with the details of your environment. 

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API. 

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation. 

To view the platform type for your cluster, run the following command: 

```shell-session
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

- [8.1. Move components to infrastructure nodes to reduce costs](08_01_move_components_to_infrastructure_nodes_to_reduce_costs.md)
- [8.2. Sample YAML for a compute machine set custom resource on AWS](08_02_sample_yaml_for_a_compute_machine_set_custom_resource_on_aws.md)
- [8.3. Sample YAML for a compute machine set custom resource on Azure](08_03_sample_yaml_for_a_compute_machine_set_custom_resource_on_azure.md)
- [8.4. Sample YAML for a compute machine set custom resource on Azure Stack Hub](08_04_sample_yaml_for_a_compute_machine_set_custom_resource_on_azure_stack_hub.md)
- [8.5. Sample YAML for a compute machine set custom resource on IBM Cloud](08_05_sample_yaml_for_a_compute_machine_set_custom_resource_on_ibm_cloud.md)
- [8.6. Sample YAML for a compute machine set custom resource on Google Cloud](08_06_sample_yaml_for_a_compute_machine_set_custom_resource_on_google_cloud.md)
- [8.7. Sample YAML for a compute machine set custom resource on Nutanix](08_07_sample_yaml_for_a_compute_machine_set_custom_resource_on_nutanix.md)
- [8.8. Sample YAML for a compute machine set custom resource on RHOSP](08_08_sample_yaml_for_a_compute_machine_set_custom_resource_on_rhosp.md)
- [8.9. Sample YAML for a compute machine set custom resource on vSphere](08_09_sample_yaml_for_a_compute_machine_set_custom_resource_on_vsphere.md)
- [8.10. Create a compute machine set](08_10_create_a_compute_machine_set.md)
- [8.11. Create an infrastructure node](08_11_create_an_infrastructure_node.md)
- [8.12. Create a machine config pool for infrastructure machines](08_12_create_a_machine_config_pool_for_infrastructure_machines.md)
- [8.13. Bind infrastructure node workloads using taints and tolerations](08_13_bind_infrastructure_node_workloads_using_taints_and_tolerations.md)
- [8.14. Move resources to infrastructure machine sets](08_14_move_resources_to_infrastructure_machine_sets.md)
- [8.15. Additional resources](08_15_additional_resources.md)
