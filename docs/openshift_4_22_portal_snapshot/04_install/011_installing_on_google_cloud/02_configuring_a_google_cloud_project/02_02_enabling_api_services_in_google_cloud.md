# 2.2. Enabling API services in Google Cloud

You must enable several API services in your Google Cloud project to complete OpenShift Container Platform installation. 

**Prerequisites**

  * You created a project to host your cluster. 



**Procedure**

  * Enable the following required API services in the project that hosts your cluster. You can also enable optional API services which are not required for installation. See [Enabling services](https://cloud.google.com/service-usage/docs/enable-disable#enabling) in the Google Cloud documentation. 

Table 2.1. Required API servicesAPI service| Console service name  
---|---  
Compute Engine API  |  `compute.googleapis.com`  
Cloud Resource Manager API  |  `cloudresourcemanager.googleapis.com`  
Cloud DNS API  |  `dns.googleapis.com`  
IAM Service Account Credentials API  |  `iamcredentials.googleapis.com`  
Identity and Access Management (IAM) API  |  `iam.googleapis.com`  
Service Usage API  |  `serviceusage.googleapis.com`  
Show more

Table 2.2. Optional API servicesAPI service| Console service name  
---|---  
Google Cloud APIs  |  `cloudapis.googleapis.com`  
Service Management API  |  `servicemanagement.googleapis.com`  
Google Cloud Storage JSON API  |  `storage-api.googleapis.com`  
Cloud Storage  |  `storage-component.googleapis.com`  
Show more
