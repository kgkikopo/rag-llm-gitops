# 6.1. Cluster Baremetal Operator

The Cluster Baremetal Operator is an optional cluster capability that can be disabled by cluster administrators during installation. 

For more information about optional cluster capabilities, see "Cluster capabilities". 

The Cluster Baremetal Operator (CBO) deploys all the components necessary to take a bare-metal server to a fully functioning worker node ready to run OpenShift Container Platform compute nodes. 

The CBO ensures that the metal3 deployment, which consists of the Bare Metal Operator (BMO) and Ironic containers, runs on one of the control plane nodes within the OpenShift Container Platform cluster. The CBO also listens for OpenShift Container Platform updates to resources that it watches and takes appropriate action. 

**Additional resources**

  * [Bare-metal capability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-bare-metal-operator_cluster-capabilities)
  * [cluster-baremetal-operator](https://github.com/openshift/cluster-baremetal-operator)
