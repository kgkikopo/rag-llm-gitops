# 11.4. Configuring the Google Cloud project that hosts your cluster

Before you can install OpenShift Container Platform, you must configure a Google Cloud project to host it. Proper project configuration provides the API services, service account, and permissions that the installation requires. 

## 11.4.1. Creating a Google Cloud project

To install OpenShift Container Platform, you must create a project in your Google Cloud account to host the cluster. 

**Procedure**

  * Create a project to host your OpenShift Container Platform cluster. See [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in the Google Cloud documentation. 

Important

Your Google Cloud project must use the Premium Network Service Tier if you are using installer-provisioned infrastructure. The Standard Network Service Tier is not supported for clusters installed using the installation program. The installation program configures internal load balancing for the `api-int.<cluster_name>.<base_domain>` URL; the Premium Tier is required for internal load balancing. 




## 11.4.2. Enabling API services in Google Cloud

You must enable several API services in your Google Cloud project to complete OpenShift Container Platform installation. 

**Prerequisites**

  * You created a project to host your cluster. 



**Procedure**

  * Enable the following required API services in the project that hosts your cluster. You can also enable optional API services which are not required for installation. See [Enabling services](https://cloud.google.com/service-usage/docs/enable-disable#enabling) in the Google Cloud documentation. 

Table 11.1. Required API servicesAPI service| Console service name  
---|---  
Compute Engine API  |  `compute.googleapis.com`  
Cloud Resource Manager API  |  `cloudresourcemanager.googleapis.com`  
Cloud DNS API  |  `dns.googleapis.com`  
IAM Service Account Credentials API  |  `iamcredentials.googleapis.com`  
Identity and Access Management (IAM) API  |  `iam.googleapis.com`  
Service Usage API  |  `serviceusage.googleapis.com`  
Show more

Table 11.2. Optional API servicesAPI service| Console service name  
---|---  
Cloud Deployment Manager V2 API  |  `deploymentmanager.googleapis.com`  
Google Cloud APIs  |  `cloudapis.googleapis.com`  
Service Management API  |  `servicemanagement.googleapis.com`  
Google Cloud Storage JSON API  |  `storage-api.googleapis.com`  
Cloud Storage  |  `storage-component.googleapis.com`  
Show more




## 11.4.3. Google Cloud account limits

A default OpenShift Container Platform cluster consumes specific Google Cloud resource quotas that you might need to increase before installation, depending on your region and cluster size. 

A default cluster, which contains three compute and three control plane machines, uses the following resources. Note that some resources are required only during the bootstrap process and are removed after the cluster deploys. 

Table 11.3. Google Cloud resources used in a default clusterService| Component| Location| Total resources required| Resources removed after bootstrap  
---|---|---|---|---  
Service account  |  IAM  |  Global  |  6  |  1   
Firewall rules  |  Networking  |  Global  |  11  |  1   
Forwarding rules  |  Compute  |  Global  |  2  |  0   
Health checks  |  Compute  |  Global  |  2  |  0   
Images  |  Compute  |  Global  |  1  |  0   
Networks  |  Networking  |  Global  |  1  |  0   
Routers  |  Networking  |  Global  |  1  |  0   
Routes  |  Networking  |  Global  |  2  |  0   
Subnetworks  |  Compute  |  Global  |  2  |  0   
Target pools  |  Networking  |  Global  |  2  |  0   
Show more

Note

If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region. 

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, static IP addresses, and persistent disk SSD (storage) quotas are the ones that are most likely to be insufficient. 

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit: 

  * `asia-east2`
  * `asia-northeast2`
  * `asia-south1`
  * `australia-southeast1`
  * `europe-north1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west6`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-west2`



You can increase resource quotas from the Google Cloud console, but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster. 

**Additional resources**

  * [Manage your quotas using the console (Google Cloud documentation)](https://cloud.google.com/docs/quota)
  * [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas)



## 11.4.4. Creating a service account in Google Cloud

OpenShift Container Platform requires a Google Cloud service account that provides authentication and authorization to access data in the Google APIs. If you do not have an existing IAM service account that contains the required roles in your project, you must create one. 

Note

To reduce the scope of permissions granted to the main service account in your Google Cloud project while still being able to use the Google Cloud Container Storage Interface (CSI) Driver Operator, you can transfer the control of permissions from the project-wide service account to the control plane and compute node service accounts instead, thus reducing the scope of the permission. For more information, see Section _Reducing permissions while using the Google Cloud CSI Driver Operator_. 

**Prerequisites**

  * You created a project to host your cluster. 



**Procedure**

  1. Create a service account in the project that you use to host your OpenShift Container Platform cluster. See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account) in the Google Cloud documentation. 
  2. Grant the service account the appropriate permissions. You can either grant the individual permissions that follow or assign the `Owner` role to it. See [Granting roles to a service account for specific resources](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource). 

Note

While making the service account an owner of the project is the easiest way to gain the required permissions, it means that service account has complete control over the project. You must determine if the risk that comes from offering that power is acceptable. 

  3. You can create the service account key in JSON format, or attach the service account to a Google Cloud virtual machine. See [Creating service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and [Creating and enabling service accounts for instances](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) in the Google Cloud documentation. 

Note

If you use a virtual machine with an attached service account to create your cluster, you must set `credentialsMode: Manual` in the `install-config.yaml` file before installation. 




### 11.4.4.1. Required Google Cloud roles

Your Google Cloud service account requires specific roles to install and manage an OpenShift Container Platform cluster, which you can scope based on your organization’s security requirements. 

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization’s security policies require a more restrictive set of permissions, you can create a service account with the following permissions. If you deploy your cluster into an existing virtual private cloud (VPC), the service account does not require certain networking permissions, which are noted in the following lists: 

The installation program requires the following roles: 

  * Compute Admin 
  * Role Administrator 
  * Security Admin 
  * Service Account Admin 
  * Service Account Key Admin 
  * Service Account User 
  * Storage Admin 



Creating network resources during installation requires the following role: 

  * DNS Administrator 



Using the Cloud Credential Operator in passthrough mode requires the following roles: 

  * Compute Load Balancer Admin 
  * Tag User 



User-provisioned Google Cloud infrastructure requires the following role: 

  * Cloud Infrastructure Manager Admin 



The following roles are applied to the service accounts that the control plane and compute machines use: 

Table 11.4. Google Cloud service account rolesAccount| Roles  
---|---  
Control Plane  |  `roles/compute.instanceAdmin`  
`roles/compute.networkAdmin`  
`roles/compute.securityAdmin`  
`roles/storage.admin`  
`roles/iam.serviceAccountUser`  
Compute  |  `roles/compute.viewer`  
`roles/storage.admin`  
`roles/artifactregistry.reader`  
Show more

## 11.4.5. Supported Google Cloud regions

You can deploy an OpenShift Container Platform cluster to specific Google Cloud regions, which determine the physical location and available machine types for your cluster infrastructure. 

You can deploy to the following Google Cloud regions: 

  * `africa-south1` (Johannesburg, South Africa) 
  * `asia-east1` (Changhua County, Taiwan) 
  * `asia-east2` (Hong Kong) 
  * `asia-northeast1` (Tokyo, Japan) 
  * `asia-northeast2` (Osaka, Japan) 
  * `asia-northeast3` (Seoul, South Korea) 
  * `asia-south1` (Mumbai, India) 
  * `asia-south2` (Delhi, India) 
  * `asia-southeast1` (Jurong West, Singapore) 
  * `asia-southeast2` (Jakarta, Indonesia) 
  * `australia-southeast1` (Sydney, Australia) 
  * `australia-southeast2` (Melbourne, Australia) 
  * `europe-central2` (Warsaw, Poland) 
  * `europe-north1` (Hamina, Finland) 
  * `europe-southwest1` (Madrid, Spain) 
  * `europe-west1` (St. Ghislain, Belgium) 
  * `europe-west2` (London, England, UK) 
  * `europe-west3` (Frankfurt, Germany) 
  * `europe-west4` (Eemshaven, Netherlands) 
  * `europe-west6` (Zürich, Switzerland) 
  * `europe-west8` (Milan, Italy) 
  * `europe-west9` (Paris, France) 
  * `europe-west12` (Turin, Italy) 
  * `me-central1` (Doha, Qatar, Middle East) 
  * `me-central2` (Dammam, Saudi Arabia, Middle East) 
  * `me-west1` (Tel Aviv, Israel) 
  * `northamerica-northeast1` (Montréal, Québec, Canada) 
  * `northamerica-northeast2` (Toronto, Ontario, Canada) 
  * `southamerica-east1` (São Paulo, Brazil) 
  * `southamerica-west1` (Santiago, Chile) 
  * `us-central1` (Council Bluffs, Iowa, USA) 
  * `us-east1` (Moncks Corner, South Carolina, USA) 
  * `us-east4` (Ashburn, Northern Virginia, USA) 
  * `us-east5` (Columbus, Ohio) 
  * `us-south1` (Dallas, Texas) 
  * `us-west1` (The Dalles, Oregon, USA) 
  * `us-west2` (Los Angeles, California, USA) 
  * `us-west3` (Salt Lake City, Utah, USA) 
  * `us-west4` (Las Vegas, Nevada, USA) 



Note

To determine which machine type instances are available by region and zone, see the Google [documentation](https://cloud.google.com/compute/docs/regions-zones#available). 

## 11.4.6. Installing and configuring CLI tools for Google Cloud

Before you deploy OpenShift Container Platform on Google Cloud with user-provisioned infrastructure, you must set up the required CLI tools to create and manage your cloud resources. 

**Prerequisites**

  * You created a project to host your cluster. 
  * You created a service account and granted it the required permissions. 



**Procedure**

  1. Install the following binaries in `$PATH`: 

     * `gcloud`
     * `gsutil`

See [Install the latest Cloud SDK version](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version) in the Google Cloud documentation. 

  2. Authenticate using the `gcloud` tool with your configured service account. 

See [Authorizing with a service account](https://cloud.google.com/sdk/docs/authorizing#authorizing_with_a_service_account) in the Google Cloud documentation.
