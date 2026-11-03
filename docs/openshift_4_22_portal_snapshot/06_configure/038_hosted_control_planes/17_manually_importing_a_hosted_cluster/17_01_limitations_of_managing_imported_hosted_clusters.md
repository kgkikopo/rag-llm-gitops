# 17.1. Limitations of managing imported hosted clusters

Hosted clusters are automatically imported into the local multicluster engine for Kubernetes Operator, unlike a standalone OpenShift Container Platform or third-party clusters. Hosted clusters run some of their agents in the _hosted mode_ so that the agents do not use the resources of your cluster. 

If you choose to automatically import hosted clusters, you can update node pools and the control plane in hosted clusters by using the `HostedCluster` resource on the management cluster. To update node pools and a control plane, see "Updating node pools in a hosted cluster" and "Updating a control plane in a hosted cluster". 

You can import hosted clusters into a location other than the local multicluster engine Operator by using the Red Hat Advanced Cluster Management (RHACM). For more information, see "Discovering multicluster engine for Kubernetes Operator hosted clusters in Red Hat Advanced Cluster Management". 

In this topology, you must update your hosted clusters by using the command-line interface or the console of the local multicluster engine for Kubernetes Operator where the cluster is hosted. You cannot update the hosted clusters through the RHACM hub cluster. 

**Additional resources**

  * [Updating node pools in a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-updating#hcp-update-node-pools_hcp-updating "8.7. Updating node pools in a hosted cluster")
  * [Updating a control plane in a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-updating#hcp-update-ocp-hc_hcp-updating "8.8. Updating a control plane in a hosted cluster")
  * [Discovering multicluster engine for Kubernetes Operator hosted clusters in Red Hat Advanced Cluster Management](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/hosted-acm#discover-hosted-acm)
