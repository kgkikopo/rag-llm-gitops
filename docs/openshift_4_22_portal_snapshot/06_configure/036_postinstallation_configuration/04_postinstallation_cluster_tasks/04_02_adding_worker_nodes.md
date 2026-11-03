# 4.2. Adding worker nodes

After you deploy your OpenShift Container Platform cluster, you can add worker nodes to scale cluster resources using the method that matches your installation type and environment. 

After you deploy your OpenShift Container Platform cluster, you can add worker nodes to scale cluster resources. There are different ways you can add worker nodes depending on the installation method and the environment of your cluster. 

## 4.2.1. Adding worker nodes to an on-premise cluster

Add worker nodes to an on-premise OpenShift Container Platform cluster by using the OpenShift CLI to generate an ISO image. 

For on-premise clusters, you can add worker nodes by using the OpenShift Container Platform CLI (`oc`) to generate an ISO image, which can then be used to boot one or more nodes in your target cluster. This process can be used regardless of how you installed your cluster. 

You can add one or more nodes at a time while customizing each node with more complex configurations, such as static network configuration, or you can specify only the MAC address of each node. Any configurations that are not specified during ISO generation are retrieved from the target cluster and applied to the new nodes. 

Preflight validation checks are also performed when booting the ISO image to inform you of failure-causing issues before you attempt to boot each node. 

**Additional resources**

  * [Adding worker nodes to an on-premise cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#adding-node-iso)



## 4.2.2. Adding worker nodes to installer-provisioned infrastructure clusters

Add worker nodes to installer-provisioned infrastructure clusters by scaling machine sets or provisioning bare-metal hosts. 

For installer-provisioned infrastructure clusters, you can manually or automatically scale the `MachineSet` object to match the number of available bare-metal hosts. 

To add a bare-metal host, you must configure all network prerequisites, configure an associated `baremetalhost` object, then provision the worker node to the cluster. You can add a bare-metal host manually or by using the web console. 

**Additional resources**

  * [Adding worker nodes using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#adding-bare-metal-host-to-cluster-using-web-console_managing-bare-metal-hosts)
  * [Adding worker nodes using YAML in the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#adding-bare-metal-host-to-cluster-using-yaml_managing-bare-metal-hosts)
  * [Manually adding a worker node to an installer-provisioned infrastructure cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#preparing-the-bare-metal-node_bare-metal-expanding)



## 4.2.3. Adding worker nodes to user-provisioned infrastructure clusters

Add worker nodes to user-provisioned infrastructure clusters by using an ISO image and Ignition config files. 

For user-provisioned infrastructure clusters, you can add worker nodes by using a RHEL or RHCOS ISO image and connecting it to your cluster using cluster Ignition config files. For RHEL worker nodes, the following example uses Ansible playbooks to add worker nodes to the cluster. For RHCOS worker nodes, the following example uses an ISO image and network booting to add worker nodes to the cluster. 

**Additional resources**

  * [Adding RHCOS worker nodes to a user-provisioned infrastructure cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-node-tasks#post-install-config-adding-fcos-compute "5.1. Adding RHCOS compute machines to an OpenShift Container Platform cluster")



## 4.2.4. Adding worker nodes to clusters managed by the Assisted Installer

Add worker nodes to Assisted Installer clusters by using Red Hat OpenShift Cluster Manager, the REST API, or a manual ISO process. 

For clusters managed by the Assisted Installer, you can add worker nodes by using the Red Hat OpenShift Cluster Manager console, the Assisted Installer REST API or you can manually add worker nodes using an ISO image and cluster Ignition config files. 

**Additional resources**

  * [Adding worker nodes using OpenShift Cluster Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#sno-adding-worker-nodes-to-sno-clusters_add-workers)
  * [Adding worker nodes using the Assisted Installer REST API](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#adding-worker-nodes-using-the-assisted-installer-api)
  * [Manually adding worker nodes to a single-node OpenShift cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#sno-adding-worker-nodes-to-single-node-clusters-manually_add-workers)



## 4.2.5. Adding worker nodes to clusters managed by the multicluster engine for Kubernetes

Add worker nodes to multicluster engine for Kubernetes clusters by using the dedicated console. 

For clusters managed by the multicluster engine for Kubernetes, you can add worker nodes by using the dedicated multicluster engine console. 

**Additional resources**

  * [Creating your cluster with the console](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.9/html/clusters/cluster_mce_overview#on-prem-creating-your-cluster-with-the-console)
