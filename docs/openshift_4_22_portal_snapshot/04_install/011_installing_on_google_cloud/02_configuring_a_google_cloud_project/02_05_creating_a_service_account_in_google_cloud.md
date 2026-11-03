# 2.5. Creating a service account in Google Cloud

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




**Additional resources**

  * [Reducing permissions while using the Google Cloud CSI Driver Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-gcp-pd-reduce-permissions_persistent-storage-csi-gcp-pd)



## 2.5.1. Required Google Cloud roles

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



The following roles are applied to the service accounts that the control plane and compute machines use: 

Table 2.4. Google Cloud service account rolesAccount| Roles  
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

## 2.5.2. Required Google Cloud permissions for installer-provisioned infrastructure

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. 

If your organization’s security policies require a more restrictive set of permissions, you can create [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles) with the necessary permissions. 

The following permissions are required for the installer-provisioned infrastructure for creating and deleting the OpenShift Container Platform cluster. 

The following permissions are required for creating network resources: 

  * `compute.addresses.create`
  * `compute.addresses.createInternal`
  * `compute.addresses.delete`
  * `compute.addresses.get`
  * `compute.addresses.list`
  * `compute.addresses.use`
  * `compute.addresses.useInternal`
  * `compute.firewalls.create`

    * This permission is not required if you install into an existing VPC and manage your own firewall rules. See the _Managing your own firewall rules_ section. 

  * `compute.firewalls.delete`

    * This permission is not required if you install into an existing VPC and manage your own firewall rules. See the _Managing your own firewall rules_ section. 

  * `compute.firewalls.get`
  * `compute.firewalls.list`
  * `compute.forwardingRules.create`
  * `compute.forwardingRules.get`
  * `compute.forwardingRules.list`
  * `compute.forwardingRules.setLabels`
  * `compute.globalAddresses.create`
  * `compute.globalAddresses.get`
  * `compute.globalAddresses.use`
  * `compute.globalForwardingRules.create`
  * `compute.globalForwardingRules.get`
  * `compute.globalForwardingRules.setLabels`
  * `compute.networks.create`
  * `compute.networks.get`
  * `compute.networks.list`
  * `compute.networks.updatePolicy`
  * `compute.networks.use`
  * `compute.routers.create`
  * `compute.routers.get`
  * `compute.routers.list`
  * `compute.routers.update`
  * `compute.routes.list`
  * `compute.subnetworks.create`
  * `compute.subnetworks.get`
  * `compute.subnetworks.list`
  * `compute.subnetworks.use`
  * `compute.subnetworks.useExternalIp`



The following permissions are required for creating load balancer resources: 

  * `compute.backendServices.create`
  * `compute.backendServices.get`
  * `compute.backendServices.list`
  * `compute.backendServices.update`
  * `compute.backendServices.use`
  * `compute.regionBackendServices.create`
  * `compute.regionBackendServices.get`
  * `compute.regionBackendServices.list`
  * `compute.regionBackendServices.update`
  * `compute.regionBackendServices.use`
  * `compute.targetPools.addInstance`
  * `compute.targetPools.create`
  * `compute.targetPools.get`
  * `compute.targetPools.list`
  * `compute.targetPools.removeInstance`
  * `compute.targetPools.use`
  * `compute.targetTcpProxies.create`
  * `compute.targetTcpProxies.get`
  * `compute.targetTcpProxies.use`



The following permissions are required for creating DNS resources: 

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.managedZones.create`
  * `dns.managedZones.get`
  * `dns.managedZones.list`
  * `dns.networks.bindPrivateDNSZone`
  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.list`



The following permissions are required for creating Service Account resources: 

  * `iam.serviceAccountKeys.create`
  * `iam.serviceAccountKeys.delete`
  * `iam.serviceAccountKeys.get`
  * `iam.serviceAccountKeys.list`
  * `iam.serviceAccounts.actAs`

    * This permission can be limited to act as the control plane and compute service accounts. Alternatively, you may grant the service account that the installation program uses the `iam.serviceAccountUser` role on the control plane and compute service accounts. 

  * `iam.serviceAccounts.create`
  * `iam.serviceAccounts.delete`
  * `iam.serviceAccounts.get`
  * `iam.serviceAccounts.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`

    * This permission is not required if you use `credentialsMode: Manual` and supply your own service accounts for compute and control plane nodes. 




The following permissions are required for creating compute resources: 

  * `compute.disks.create`
  * `compute.disks.get`
  * `compute.disks.list`
  * `compute.disks.setLabels`
  * `compute.instanceGroups.create`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.get`
  * `compute.instanceGroups.list`
  * `compute.instanceGroups.update`
  * `compute.instanceGroups.use`
  * `compute.instances.create`
  * `compute.instances.delete`
  * `compute.instances.get`
  * `compute.instances.list`
  * `compute.instances.setLabels`
  * `compute.instances.setMetadata`
  * `compute.instances.setServiceAccount`
  * `compute.instances.setTags`
  * `compute.instances.use`
  * `compute.machineTypes.get`
  * `compute.machineTypes.list`



The following permissions are required for creating storage resources: 

  * `storage.buckets.create`
  * `storage.buckets.delete`
  * `storage.buckets.get`
  * `storage.buckets.list`
  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`



The following permissions are required for creating health check resources: 

  * `compute.healthChecks.create`
  * `compute.healthChecks.get`
  * `compute.healthChecks.list`
  * `compute.healthChecks.useReadOnly`
  * `compute.httpHealthChecks.create`
  * `compute.httpHealthChecks.get`
  * `compute.httpHealthChecks.list`
  * `compute.httpHealthChecks.useReadOnly`
  * `compute.regionHealthChecks.create`
  * `compute.regionHealthChecks.get`
  * `compute.regionHealthChecks.useReadOnly`



The following permissions are required to get Google Cloud zone and region related information: 

  * `compute.globalOperations.get`
  * `compute.regionOperations.get`
  * `compute.regions.get`
  * `compute.regions.list`
  * `compute.zoneOperations.get`
  * `compute.zones.get`
  * `compute.zones.list`



The following permissions are required for checking services and quotas 

  * `monitoring.timeSeries.list`
  * `serviceusage.quotas.get`
  * `serviceusage.services.list`



The following IAM permissions are required for installation: 

  * `iam.roles.create`
  * `iam.roles.get`
  * `iam.roles.update`



The following permission is required when authenticating without a service account key: 

  * `iam.serviceAccounts.signBlob`



The following permission is required when providing Key Management Service (KMS) key rings: 

  * `cloudkms.keyRings.list`



The following optional Images permission is for installation: 

  * `compute.images.list`



The following optional permission is for running gather bootstrap: 

  * `compute.instances.getSerialPortOutput`



The following permissions are required for deleting network resources: 

  * `compute.addresses.delete`
  * `compute.addresses.deleteInternal`
  * `compute.addresses.list`
  * `compute.addresses.setLabels`
  * `compute.firewalls.delete`
  * `compute.firewalls.list`
  * `compute.forwardingRules.delete`
  * `compute.forwardingRules.list`
  * `compute.globalAddresses.delete`
  * `compute.globalAddresses.list`
  * `compute.globalForwardingRules.delete`
  * `compute.globalForwardingRules.list`
  * `compute.networks.delete`
  * `compute.networks.list`
  * `compute.networks.updatePolicy`
  * `compute.routers.delete`
  * `compute.routers.list`
  * `compute.routes.list`
  * `compute.subnetworks.delete`
  * `compute.subnetworks.list`



The following permissions are required for deleting load balancer resources: 

  * `compute.backendServices.delete`
  * `compute.backendServices.list`
  * `compute.regionBackendServices.delete`
  * `compute.regionBackendServices.list`
  * `compute.targetPools.delete`
  * `compute.targetPools.list`
  * `compute.targetTcpProxies.delete`
  * `compute.targetTcpProxies.list`



The following permissions are required for deleting DNS resources: 

  * `dns.changes.create`
  * `dns.managedZones.delete`
  * `dns.managedZones.get`
  * `dns.managedZones.list`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.list`



The following permissions are required for deleting Service Account resources: 

  * `iam.serviceAccounts.delete`
  * `iam.serviceAccounts.get`
  * `iam.serviceAccounts.list`
  * `resourcemanager.projects.getIamPolicy`



The following permissions are required for deleting compute resources: 

  * `compute.disks.delete`
  * `compute.disks.list`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.list`
  * `compute.instances.delete`
  * `compute.instances.list`
  * `compute.instances.stop`
  * `compute.machineTypes.list`



The following permissions are required for deleting storage resources: 

  * `storage.buckets.delete`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.list`
  * `storage.objects.delete`
  * `storage.objects.list`



The following permissions are required for deleting health check resources: 

  * `compute.healthChecks.delete`
  * `compute.healthChecks.list`
  * `compute.httpHealthChecks.delete`
  * `compute.httpHealthChecks.list`
  * `compute.regionHealthChecks.delete`
  * `compute.regionHealthChecks.list`



The following Image permission is required for deletion: 

  * `compute.images.list`



## 2.5.3. Required Google Cloud permissions for shared VPC installations

When you are installing a cluster to a [shared VPC](https://cloud.google.com/vpc/docs/shared-vpc), you must configure the service account for both the host project and the service project. 

Important

You can use granular permissions for a Cloud Credential Operator (CCO) that operates in either Manual or Mint credentials mode. For more information about the minimum permissions required for a standard installation that is configured with either of these credentials modes, see "Required Google Cloud permissions for installer-provisioned infrastructure". 

You cannot use granular permissions in Passthrough credentials mode. For more information about the minimum roles required, see "Required Google Cloud roles". 

If you are not installing to a shared Virtual Private Cloud (VPC), you can skip the procedure. 

Important

When installing a cluster on a shared VPC by using short-lived credentials, you must grant the `compute.subnetworks.use` permission in the host project to Day 2 Operator service accounts. 

After using the `ccoctl` utility to generate the Google Cloud credentials, manually grant this permission to the Cluster CAPI Operator and Machine API Operator service accounts. 

Ensure that the host project applies one of the following configurations to the service account, noting that the permissions for creating and deleting firewalls are not required if you manage your own firewall rules: 

**Example 2.1. Required permissions for creating firewalls in the host project**

  * `projects/<host-project>/roles/dns.networks.bindPrivateDNSZone`
  * `roles/compute.networkAdmin`
  * `roles/compute.securityAdmin`



**Example 2.2. Required permissions for deleting firewalls in the host project**

  * `compute.firewalls.delete`
  * `compute.networks.updatePolicy`



**Example 2.3. Required minimal permissions**

  * `projects/<host-project>/roles/dns.networks.bindPrivateDNSZone`
  * `roles/compute.networkUser`



If you do not supply a service account for control plane nodes in the `install-config.yaml` file, grant the following permissions to the service account in the host project. If you do not supply a service account for compute nodes in the `install-config.yaml` file, grant the following permissions to the service account in the host project for cluster destruction. If you do supply service accounts for control plane and compute nodes, you do not need to grant the following permissions. 

  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`



The following permissions are required when you select a separate project for the location of the DNS zone or zones. These permissions are also required when the DNS zone or zones are located in a third project. 

**Example 2.4. Required minimal permissions for provisioning DNS resources in a separate project**

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.managedZones.create`
  * `dns.managedZones.delete`
  * `dns.managedZones.get`
  * `dns.managedZones.list`
  * `dns.managedZones.update`
  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.list`



## 2.5.4. Required Google Cloud permissions for user-provided service accounts

If your organization’s security policies prevent the installation program from creating service accounts, you can provide your own service accounts with the required roles for the control plane and compute nodes. 

By default, the installation program creates a service account for the control plane and compute nodes. The service account that the installation program uses requires the roles and permissions that are listed in the _Creating a service account in Google Cloud_ section, and the `resourcemanager.projects.getIamPolicy` and `resourcemanager.projects.setIamPolicy` permissions. These permissions should be applied to the service account in the host project. If this approach does not meet the security requirements of your organization, you can provide a service account email address for the control plane or compute nodes in the `install-config.yaml` file. For more information, see the _Installation configuration parameters for Google Cloud_ page. If you provide a service account for control plane nodes during an installation into a shared VPC, you must grant that service account the `roles/compute.networkUser` role in the host project. If you want the installation program to automatically create firewall rules when you supply the control plane service account, you must grant that service account the `roles/compute.networkAdmin` and `roles/compute.securityAdmin` roles in the host project. If you only supply the `roles/compute.networkUser` role, you must create the firewall rules manually. 

Important

The following roles are required for user-provided service accounts for control plane and compute nodes. 

The following roles are required for user-provided service accounts for control plane nodes: 

  * `roles/compute.instanceAdmin`
  * `roles/compute.networkAdmin`
  * `roles/compute.securityAdmin`
  * `roles/storage.admin`



The following roles are required for user-provided service accounts for compute nodes: 

  * `roles/compute.viewer`
  * `roles/storage.admin`
  * `roles/artifactregistry.reader`
