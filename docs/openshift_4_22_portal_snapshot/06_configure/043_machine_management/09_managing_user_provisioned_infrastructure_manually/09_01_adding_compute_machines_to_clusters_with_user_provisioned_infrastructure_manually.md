# 9.1. Adding compute machines to clusters with user-provisioned infrastructure manually

To scale a OpenShift Container Platform cluster that uses user-provisioned infrastructure, you can manually add compute machines during or after installation. The postinstallation process requires some of the same configuration files and parameters that you used for installation. 

## 9.1.1. Adding compute machines to Amazon Web Services

You can add more compute machines to your OpenShift Container Platform cluster on AWS. 

See [Adding compute machines to AWS by using CloudFormation templates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-user-provisioned-infrastructure-manually#adding-aws-compute-user-infra "9.2. Adding compute machines to AWS by using CloudFormation templates") for more information. 

## 9.1.2. Adding compute machines to Microsoft Azure

You can add more compute machines to your OpenShift Container Platform cluster on Microsoft Azure. 

See [Creating additional worker machines in Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installation-creating-azure-worker_installing-azure-user-infra) for more information. 

## 9.1.3. Adding compute machines to Azure Stack Hub

You can add more compute machines to your OpenShift Container Platform cluster on Azure Stack Hub. 

See [Creating additional worker machines in Azure Stack Hub](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installation-creating-azure-worker_installing-azure-stack-hub-user-infra) for more information. 

## 9.1.4. Adding compute machines to Google Cloud

You can add more compute machines to your OpenShift Container Platform cluster on GCP. 

See [Creating additional worker machines in Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installation-creating-gcp-worker_installing-restricted-networks-gcp) for more information. 

## 9.1.5. Adding compute machines to vSphere

You can use compute machine sets to automate the creation of additional compute machines for your OpenShift Container Platform cluster on vSphere. 

See [use compute machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-vsphere "2.9. Creating a compute machine set on vSphere") for more information. 

You can manually add more compute machines to your cluster. 

See [Adding compute machines to vSphere manually](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-user-provisioned-infrastructure-manually#adding-vsphere-compute-user-infra "9.3. Adding compute machines to vSphere manually") for more information. 

You can add bare-metal compute machines to your cluster. 

See [Adding bare-metal compute machines to a vSphere cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-user-provisioned-infrastructure-manually#adding-bare-metal-compute-vsphere-user-infra "9.4. Adding bare-metal compute machines to a vSphere cluster") for more information. 

Important

Bare-metal nodes on VMware vSphere clusters is generally available for OpenShift Container Platform 4.22.13 and later. However, this feature is Technology Preview for 4.21 through 4.22.12. 

## 9.1.6. Adding compute machines to bare metal

You can add more compute machines to your OpenShift Container Platform cluster on bare metal. 

See [Adding compute machines to bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-user-provisioned-infrastructure-manually#adding-bare-metal-compute-user-infra "9.5. Adding compute machines to bare metal") for more information.
