# 2.3. Install GitOps ZTP in a disconnected environment

Use Red Hat Advanced Cluster Management (RHACM), Red Hat OpenShift GitOps, and Topology Aware Lifecycle Manager (TALM) on the hub cluster in the disconnected environment to manage the deployment of multiple managed clusters. 

**Prerequisites**

  * You have installed the OpenShift Container Platform CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 
  * You have configured a disconnected mirror registry for use in the cluster. 

Note

The disconnected mirror registry that you create must contain a version of TALM backup and pre-cache images that matches the version of TALM running in the hub cluster. The spoke cluster must be able to resolve these images in the disconnected mirror registry. 




**Procedure**

  * Install RHACM in the hub cluster. See [Installing RHACM in a disconnected environment](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/install/installing#install-on-disconnected-networks). 
  * Install GitOps and TALM in the hub cluster. 



**Additional resources**

  * [Installing OpenShift GitOps](https://docs.openshift.com/gitops/latest/installing_gitops/installing-openshift-gitops.html#installing-openshift-gitops)
  * [Installing TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-talm-for-cluster-updates#installing-topology-aware-lifecycle-manager-using-cli_cnf-topology-aware-lifecycle-manager "13.4. Installing the Topology Aware Lifecycle Manager by using the CLI")
  * [Mirroring an Operator catalog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-mirror-catalog_olm-restricted-networks)
