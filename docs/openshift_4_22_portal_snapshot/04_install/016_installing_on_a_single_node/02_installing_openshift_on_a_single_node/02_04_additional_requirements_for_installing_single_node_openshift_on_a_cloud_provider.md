# 2.4. Additional requirements for installing single-node OpenShift on a cloud provider

Compared to installing a high-availability cluster, there are additional requirements for installing single-node OpenShift. 

The documentation for installer-provisioned installation on cloud providers is based on a high availability cluster consisting of three control plane nodes. When referring to the documentation, consider the differences between the requirements for a single-node OpenShift cluster and a high availability cluster. 

  * A high availability cluster requires a temporary bootstrap machine, three control plane machines, and at least two compute machines. For a single-node OpenShift cluster, you need only a temporary bootstrap machine and one cloud instance for the control plane node and no compute nodes. 
  * The minimum resource requirements for high availability cluster installation include a control plane node with 4 vCPUs and 100GB of storage. For a single-node OpenShift cluster, you must have a minimum of 4 vCPUs and 120GB of storage. 

Important

Running single-node OpenShift on 4 vCPUs leaves very little "headroom" for user applications, and creates a high risk of resource contention and performance degradation. 

To ensure cluster stability at this threshold, you must take steps to minimize the total resource footprint of the cluster, such as limiting the amount of workloads running on the cluster or limiting cluster capabilities. For more information, see "Cluster capabilities". 

Otherwise, it is recommended to provide more compute resources to the cluster. 

  * The `controlPlane.replicas` setting in the `install-config.yaml` file should be set to `1`. 
  * The `compute.replicas` setting in the `install-config.yaml` file should be set to `0`. This makes the control plane node schedulable. 



**Additional resources**

  * [Cluster capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-capabilities)
