# 1.2. Overview

You can install OpenShift Container Platform on Oracle Edge Cloud by using the Assisted Installer. 

For an alternative installation method, see "Installing a cluster on Oracle® Edge Cloud by using the Agent-based Installer". 

Preinstallation considerations
    

  * Ensure that your installation meets the prerequisites specified for Oracle. For details, see the "Access and Considerations" section in the Oracle documentation. 
  * Ensure that your infrastructure is certified and uses a compatible cloud instance type. For details, see "Oracle Cloud Infrastructure". 
  * Ensure that you are performing the installation on a virtual machine. 



Installation process
    

The installation process builds a bastion host within the designated compartment of the OpenShift Container Platform cluster. The bastion host is used to run two Terraform scripts: 

  * The first script builds IAM Resources in the OCI Home region of the Oracle® Edge Cloud system (two Dynamic Groups and one Policy). 
  * The second script builds the infrastructure resources on the Oracle® Edge Cloud system to support the OpenShift Container Platform cluster, including the OpenShift Container Platform VCN, public and private subnets, load balancers, Internet GW, NAT GW, and DNS server. The script includes all the resources needed to activate the control plane nodes and compute nodes that form a cluster. 



The bastion host is installed in the designated OpenShift Container Platform Compartment and configured to communicate through a designated Oracle® Edge Cloud DRG Subnet or Internet GW Subnet within the Oracle® Edge Cloud parent tenancy. 

The installation process subsequently provisions three control plane (master) nodes and three compute (worker) nodes, together with the external and internal Load Balancers that form the cluster. This is the standard implementation for Oracle Edge Cloud. 

Main steps
    

The main steps of the procedure are as follows: 

  1. Preparing the Oracle® Edge Cloud bastion server. 
  2. Running the Terraform script via the Home region. 
  3. Preparing the OpenShift Container Platform image for Oracle Edge Cloud. 
  4. Running the Terraform script via the Oracle® Edge Cloud region. 
  5. Installing the cluster by using the Assisted Installer web console. 



**Additional resources**

  * [Access and considerations (Oracle documentation)](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP)
  * [Oracle Cloud Infrastructure](https://catalog.redhat.com/cloud/detail/216977)
