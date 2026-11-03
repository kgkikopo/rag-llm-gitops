# 1.3. Preparing the Oracle Distributed Cloud environment

Before installing OpenShift Container Platform using Assisted Installer, create the necessary resources and download the configuration file in the Oracle Distributed Cloud environment. 

**Prerequisites**

  * You have an Oracle Cloud Infrastructure (OCI) account to host the cluster. 
  * If you use a firewall and you plan to use a Telemetry service, you configured your firewall to allow OpenShift Container Platform to access the sites required. 



**Procedure**

  1. Log in to your [OCI](https://cloud.oracle.com/a/) account with administrator privileges. 
  2. Configure the account by defining the [Cloud Accounts and Resources (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/install-prereq.htm). Ensure that you create the following resources: 

     1. Create a child compartment for organizing, restricting access, and setting usage limits to OCI resources. For the full procedure, see [Creating a Compartment (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_create_a_compartment.htm#To). 
     2. Create a new object storage bucket into which you will upload the discovery ISO image. For the full procedure, see [Creating an Object Storage Bucket (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top). 

  3. Download the latest versions of the following configuration files from the [`oracle-quickstart/oci-openshift`](https://github.com/oracle-quickstart/oci-openshift/releases) releases page: 

     * `create-resource-attribution-tags-vX.X.X.zip`: The Terraform stack for creating the required resource attribution tags in your OCI tenancy. 

Important

Resource attribution tags are mandatory for OpenShift Container Platform on Oracle Distributed Cloud. If you have not previously applied the `create-resource-attribution-tags` stack in your tenancy, you must download and apply it before proceeding. After the tags exist, later cluster deployments can reuse them. For more details, see [OpenShift on OCI (OSO) Prerequisites](https://github.com/oracle-quickstart/oci-openshift?tab=readme-ov-file#prerequisites). 

     * `create-cluster-vX.X.X.zip`: The Terraform stack and custom manifests for provisioning OCI resources and installing OpenShift Container Platform clusters on Oracle Distributed Cloud. 

The `create-cluster` configuration file contains the following: 

       * **Terraform Stacks** : The Terraform stack code for provisioning OCI resources to create and manage OpenShift Container Platform clusters on Oracle Distributed Cloud. 
       * **Custom Manifests** : The manifest files needed for the installation of OpenShift Container Platform clusters on Oracle Distributed Cloud. 

Note

To make any changes to the manifests, you can clone the entire Oracle GitHub repository and access the `custom_manifests` and `terraform-stacks` directories directly. For details, see [Configuration Files (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/install-prereq.htm#install-configuration-files).
