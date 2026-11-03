# 2.3. Creating OCI infrastructure resources and services

You must create an Oracle Edge Cloud environment on your virtual machine (VM) shape. By creating this environment, you can install OpenShift Container Platform and deploy a cluster on an infrastructure that supports a wide range of cloud options and strong security policies. 

Having prior knowledge of Oracle Cloud Infrastructure (OCI) components can help you with understanding the concept of OCI resources and how you can configure them to meet your organizational needs. 

Important

To ensure compatibility with OpenShift Container Platform, you must set `A` as the record type for each DNS record and name records as follows: 

  * `api.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer 
  * `api-int.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer 
  * `*.apps.<cluster_name>.<base_domain>`, which targets the `ingressVIP` parameter of the Ingress load balancer 



The `api.*` and `api-int.*` DNS records relate to control plane machines, so you must ensure that all nodes in your installed OpenShift Container Platform cluster can access these DNS records. 

**Prerequisites**

  * You configured an OCI account to host the OpenShift Container Platform cluster. See "Access and Considerations" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) (Oracle documentation). 



**Procedure**

  * Create the required OCI resources and services. 

For more information, see "Terraform Script Execution" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) (Oracle documentation). 




**Additional resources**

  * [Learn About Oracle Cloud Basics (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/concepts.htm)
