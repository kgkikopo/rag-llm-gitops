# Chapter 14. Expanding single-node OpenShift clusters with GitOps ZTP

You can expand single-node OpenShift clusters with GitOps Zero Touch Provisioning (ZTP). When you add a worker node to single-node OpenShift clusters, the original single-node OpenShift cluster retains the control plane node role. Adding a worker node does not require any downtime for the existing single-node OpenShift cluster. 

Note

You can only expand a single-node OpenShift cluster with one additional worker node. It is not recommended to expand a single-node OpenShift cluster with more than one worker node. 

If you require workload partitioning on the worker node, you must deploy and remediate the managed cluster policies on the hub cluster before installing the node. This way, the workload partitioning `MachineConfig` objects are rendered and associated with the `worker` machine config pool before the GitOps ZTP workflow applies the `MachineConfig` ignition file to the worker node. 

It is recommended that you first remediate the policies, and then install the worker node. If you create the workload partitioning manifests after installing the worker node, you must drain the node manually and delete all the pods managed by daemon sets. When the managing daemon sets create the new pods, the new pods undergo the workload partitioning process. 

Important

Adding a worker node to single-node OpenShift clusters with GitOps ZTP is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Additional resources**

  * [Reference configuration for deploying vDUs on single-node OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/sno-configure-for-vdu "Chapter 7. Recommended single-node OpenShift cluster configuration for vDU application workloads")
  * [Adding worker nodes to single-node OpenShift clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-sno-worker-nodes)
  * [Removing managed cluster nodes by using the command line interface](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.10/html/clusters/cluster_mce_overview#auto-remove-host-steps-cli)

- [14.1. Applying profiles to the worker node with PolicyGenerator or PolicyGenTemplate resources](14_01_applying_profiles_to_the_worker_node_with_policygenerator_or_policygentemplate_resources.md)
- [14.2. Ensuring PTP and SR-IOV daemon selector compatibility](14_02_ensuring_ptp_and_sr_iov_daemon_selector_compatibility.md)
- [14.3. PTP and SR-IOV node selector compatibility](14_03_ptp_and_sr_iov_node_selector_compatibility.md)
- [14.4. Using PolicyGenerator CRs to apply worker node policies to the worker node](14_04_using_policygenerator_crs_to_apply_worker_node_policies_to_the_worker_node.md)
- [14.5. Using PolicyGenTemplate CRs to apply worker node policies to the worker node](14_05_using_policygentemplate_crs_to_apply_worker_node_policies_to_the_worker_node.md)
- [14.6. Adding an additional worker node single-node OpenShift clusters with GitOps ZTP](14_06_adding_an_additional_worker_node_single_node_openshift_clusters_with_gitops_ztp.md)
