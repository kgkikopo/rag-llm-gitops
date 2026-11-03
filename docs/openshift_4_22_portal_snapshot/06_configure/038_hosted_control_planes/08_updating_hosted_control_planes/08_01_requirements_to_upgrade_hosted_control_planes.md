# 8.1. Requirements to upgrade hosted control planes

The multicluster engine for Kubernetes Operator can manage one or more OpenShift Container Platform clusters. After you create a hosted cluster on OpenShift Container Platform, you must import your hosted cluster in the multicluster engine Operator as a managed cluster. 

You can then use the OpenShift Container Platform cluster as a management cluster. 

Consider the following requirements before you start updating hosted control planes: 

  * You must use the bare metal platform for an OpenShift Container Platform cluster when using OpenShift Virtualization as a provider. 
  * You must use bare metal or OpenShift Virtualization as the cloud platform for the hosted cluster. You can find the platform type of your hosted cluster in the `spec.Platform.type` specification of the `HostedCluster` custom resource (CR). 



Important

You must update hosted control planes in the following order: 

  1. Upgrade an OpenShift Container Platform cluster to the latest version. For more information, see "Updating a cluster using the web console" or "Updating a cluster using the CLI". 
  2. Upgrade the multicluster engine Operator to the latest version. For more information, see "Updating installed Operators". 
  3. Upgrade the hosted cluster and node pools from the previous OpenShift Container Platform version to the latest version. For more information, see "Updating a control plane in a hosted cluster" and "Updating node pools in a hosted cluster". 



**Additional resources**

  * [Updating a cluster using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-web-console)
  * [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-cli)
  * [Updating installed Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-upgrading-operators)
  * [Updating a control plane in a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-updating#hcp-update-ocp-hc_hcp-updating "8.8. Updating a control plane in a hosted cluster")
  * [Updating node pools in a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-updating#hcp-update-node-pools_hcp-updating "8.7. Updating node pools in a hosted cluster")
