# 2.6. Running a cluster on Oracle Edge Cloud

To run a cluster on Oracle® Edge Cloud, you must first convert your generated Agent ISO image into an OCI image, upload it to an OCI Home Region Bucket, and then import the uploaded image to the Oracle Edge Cloud system. 

Note

Oracle Edge Cloud supports the following OpenShift Container Platform cluster topologies: 

  * Installing an OpenShift Container Platform cluster on a single node. 
  * A highly available cluster that has a minimum of three control plane instances and two compute instances. 
  * A compact three-node cluster that has a minimum of three control plane instances. 



**Prerequisites**

  * You generated an Agent ISO image. See the "Creating configuration files for installing a cluster on Oracle Edge Cloud" section. 



**Procedure**

  1. Convert the agent ISO image to an OCI image, upload it to an OCI Home Region Bucket, and then import the uploaded image to the Oracle Edge Cloud system. See "Prepare the OpenShift Master Images" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer (Oracle documentation)](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) for instructions. 
  2. Create control plane instances on Oracle Edge Cloud. See "Create control plane instances on C3 and Master Node LB Backend Sets" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer (Oracle documentation)](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) for instructions. 
  3. Create a compute instance from the supplied base image for your cluster topology. See "Add worker nodes" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer (Oracle documentation)](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) for instructions. 

Important

Before you create the compute instance, check that you have enough memory and disk resources for your cluster. Additionally, ensure that at least one compute instance has the same IP address as the address stated under `rendezvousIP` in the `agent-config.yaml` file.
