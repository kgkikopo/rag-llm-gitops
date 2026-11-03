# Chapter 11. Handling machine configuration for hosted control planes

In a standalone OpenShift Container Platform cluster, a machine config pool manages a set of nodes. You can handle a machine configuration by using the `MachineConfigPool` custom resource (CR). 

Tip

You can reference any `machineconfiguration.openshift.io` resources in the `nodepool.spec.config` field of the `NodePool` CR. 

In hosted control planes, the `MachineConfigPool` CR does not exist. A node pool contains a set of compute nodes. You can handle a machine configuration by using node pools. 

You can manage your workloads in your hosted cluster by using the cluster autoscaler. 

Note

In OpenShift Container Platform 4.18 or later, the default container runtime for worker nodes is changed from runC to crun.

- [11.1. Configure node pools for hosted control planes](11_01_configure_node_pools_for_hosted_control_planes.md)
- [11.2. Reference the kubelet configuration in node pools](11_02_reference_the_kubelet_configuration_in_node_pools.md)
- [11.3. Configure node tuning in a hosted cluster](11_03_configure_node_tuning_in_a_hosted_cluster.md)
- [11.4. Deploy the SR-IOV Operator for hosted control planes](11_04_deploy_the_sr_iov_operator_for_hosted_control_planes.md)
- [11.5. Configure the NTP server for hosted clusters](11_05_configure_the_ntp_server_for_hosted_clusters.md)
- [11.6. Scale down the data plane to zero](11_06_scale_down_the_data_plane_to_zero.md)
- [11.7. Scale up and down workloads in a hosted cluster](11_07_scale_up_and_down_workloads_in_a_hosted_cluster.md)
- [11.8. Scale up workloads in a hosted cluster](11_08_scale_up_workloads_in_a_hosted_cluster.md)
- [11.9. Autoscaling to and from zero on hosted control planes node pools](11_09_autoscaling_to_and_from_zero_on_hosted_control_planes_node_pools.md)
- [11.10. Set the priority expander in a hosted cluster](11_10_set_the_priority_expander_in_a_hosted_cluster.md)
- [11.11. Balance ignored labels in a hosted cluster](11_11_balance_ignored_labels_in_a_hosted_cluster.md)
