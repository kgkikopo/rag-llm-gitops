# 2.4. Creating OCI infrastructure resources and services

You must create an Oracle Distributed Cloud environment on your virtual machine (VM) or bare-metal shape. By creating this environment, you can install OpenShift Container Platform and deploy a cluster on an infrastructure that supports a wide range of cloud options and strong security policies. 

Having prior knowledge of Oracle Cloud Infrastructure (OCI) components can help you with understanding the concept of OCI resources and how you can configure them to meet your organizational needs. 

The Agent-based Installer method for installing an OpenShift Container Platform cluster on Oracle Distributed Cloud requires that you manually create OCI resources and services. 

Important

To ensure compatibility with OpenShift Container Platform, you must set `A` as the record type for each DNS record and name records as follows: 

  * `api.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer 
  * `api-int.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer 
  * `*.apps.<cluster_name>.<base_domain>`, which targets the `ingressVIP` parameter of the Ingress load balancer 



The `api.*` and `api-int.*` DNS records relate to control plane machines, so you must ensure that all nodes in your installed OpenShift Container Platform cluster can access these DNS records. 

**Prerequisites**

  * You configured an OCI account to host the OpenShift Container Platform cluster. See [Prerequisites (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/install-prereq.htm). 



**Procedure**

  * Create the required OCI resources and services. 

For installations in a connected environment, see [Provisioning Cluster Infrastructure Using Terraform (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/agent-installer-using-stack.htm). 

For installations in a disconnected environment, see [Provisioning OCI Resources for the Agent-based Installer in Disconnected Environments (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/agent-prereq.htm). 




**Additional resources**

  * [Learn About Oracle Cloud Basics (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/concepts.htm)
