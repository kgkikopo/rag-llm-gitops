# 2.4. Supported identities to access Azure resources

An OpenShift Container Platform cluster requires an Azure identity to create and manage Azure resources. You need a service principal, a system-assigned managed identity, or a user-assigned managed identity to complete the installation. 

  * A service principal 
  * A system-assigned managed identity 
  * A user-assigned managed identity 



For more information on Azure identities, see "Managed identity types". 

**Additional resources**

  * [Managed identity types (Azure documentation)](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview#managed-identity-types)



## 2.4.1. Required Azure roles

Before you create the identity for an OpenShift Container Platform cluster on Azure, verify that your environment meets the role and permission requirements for the identity type you plan to use. 

The following requirements must be met: 

  * The Azure account that you use to create the identity is assigned the `User Access Administrator` and `Contributor` roles. These roles are required when: 

    * Creating a service principal or user-assigned managed identity. 
    * Enabling a system-assigned managed identity on a virtual machine. 

  * If you are going to use a service principal to complete the installation, verify that the Azure account that you use to create the identity is assigned the `microsoft.directory/servicePrincipals/createAsOwner` permission in Microsoft Entra ID. 



**Additional resources**

  * [Assign Azure roles using the Azure portal (Azure documentation)](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)



### 2.4.1.1. Required Azure permissions for installer-provisioned infrastructure

The installation program requires access to a Microsoft Azure service principal or managed identity with the necessary permissions to deploy the cluster and to maintain its daily operation. These permissions must be granted to the Azure subscription that is associated with the identity. 

The following options are available to you: 

  * You can assign the identity the `Contributor` and `User Access Administrator` roles, which grant all of the required permissions. 

If you set `identity.type` to `None` in the `install-config.yaml` file, you do not need to assign the `User Access Administrator` role to the service principal. 

For more information about assigning roles, see the Azure documentation for "managing access to Azure resources using the Azure portal". 

  * If the security policies of your organization require a more restrictive set of permissions, you can create a "custom role" with the necessary permissions. 



The following permissions are required for creating an OpenShift Container Platform cluster on Microsoft Azure. 

Required permissions for creating authorization resources
    

  * `Microsoft.Authorization/policies/audit/action`
  * `Microsoft.Authorization/policies/auditIfNotExists/action`
  * `Microsoft.Authorization/roleAssignments/read`
  * `Microsoft.Authorization/roleAssignments/write`



Important

The following permissions are not required if you set `identity.type` to `None` in the `install-config.yaml` file: 

  * `Microsoft.Authorization/roleAssignments/read`
  * `Microsoft.Authorization/roleAssignments/write`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/read`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/write`
  * `Microsoft.Authorization/roleAssignments/delete`



The following permissions are not required if you set `identity.type` to `UserAssigned` in the `install-config.yaml` file and provide a user-assigned identity: 

  * `Microsoft.Authorization/roleAssignments/read`
  * `Microsoft.Authorization/roleAssignments/write`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/write`
  * `Microsoft.Authorization/roleAssignments/delete`



Required permissions for creating compute resources
    

  * `Microsoft.Compute/availabilitySets/read`
  * `Microsoft.Compute/availabilitySets/write`
  * `Microsoft.Compute/disks/beginGetAccess/action`
  * `Microsoft.Compute/disks/delete`
  * `Microsoft.Compute/disks/read`
  * `Microsoft.Compute/disks/write`
  * `Microsoft.Compute/galleries/images/read`
  * `Microsoft.Compute/galleries/images/versions/read`
  * `Microsoft.Compute/galleries/images/versions/write`
  * `Microsoft.Compute/galleries/images/write`
  * `Microsoft.Compute/galleries/read`
  * `Microsoft.Compute/galleries/write`
  * `Microsoft.Compute/snapshots/read`
  * `Microsoft.Compute/snapshots/write`
  * `Microsoft.Compute/snapshots/delete`
  * `Microsoft.Compute/virtualMachines/delete`
  * `Microsoft.Compute/virtualMachines/powerOff/action`
  * `Microsoft.Compute/virtualMachines/read`
  * `Microsoft.Compute/virtualMachines/write`



Required permissions for creating identity management resources
    

  * `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/read`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/write`



Required permissions for creating network resources
    

  * `Microsoft.Network/dnsZones/A/write`
  * `Microsoft.Network/dnsZones/CNAME/write`
  * `Microsoft.Network/dnszones/CNAME/read`
  * `Microsoft.Network/dnszones/read`
  * `Microsoft.Network/loadBalancers/backendAddressPools/join/action`
  * `Microsoft.Network/loadBalancers/backendAddressPools/read`
  * `Microsoft.Network/loadBalancers/backendAddressPools/write`
  * `Microsoft.Network/loadBalancers/read`
  * `Microsoft.Network/loadBalancers/write`
  * `Microsoft.Network/loadBalancers/inboundNatRules/read`
  * `Microsoft.Network/loadBalancers/inboundNatRules/write`
  * `Microsoft.Network/loadBalancers/inboundNatRules/join/action`
  * `Microsoft.Network/loadBalancers/inboundNatRules/delete`
  * `Microsoft.Network/routeTables/read`
  * `Microsoft.Network/routeTables/write`
  * `Microsoft.Network/routeTables/join/action`
  * `Microsoft.Network/networkInterfaces/delete`
  * `Microsoft.Network/networkInterfaces/join/action`
  * `Microsoft.Network/networkInterfaces/read`
  * `Microsoft.Network/networkInterfaces/write`
  * `Microsoft.Network/networkSecurityGroups/join/action`
  * `Microsoft.Network/networkSecurityGroups/read`
  * `Microsoft.Network/networkSecurityGroups/securityRules/delete`
  * `Microsoft.Network/networkSecurityGroups/securityRules/read`
  * `Microsoft.Network/networkSecurityGroups/securityRules/write`
  * `Microsoft.Network/networkSecurityGroups/write`
  * `Microsoft.Network/privateDnsZones/A/read`
  * `Microsoft.Network/privateDnsZones/A/write`
  * `Microsoft.Network/privateDnsZones/A/delete`
  * `Microsoft.Network/privateDnsZones/SOA/read`
  * `Microsoft.Network/privateDnsZones/read`
  * `Microsoft.Network/privateDnsZones/virtualNetworkLinks/read`
  * `Microsoft.Network/privateDnsZones/virtualNetworkLinks/write`
  * `Microsoft.Network/privateDnsZones/write`
  * `Microsoft.Network/publicIPAddresses/delete`
  * `Microsoft.Network/publicIPAddresses/join/action`
  * `Microsoft.Network/publicIPAddresses/read`
  * `Microsoft.Network/publicIPAddresses/write`
  * `Microsoft.Network/virtualNetworks/checkIpAddressAvailability/read`
  * `Microsoft.Network/virtualNetworks/join/action`
  * `Microsoft.Network/virtualNetworks/read`
  * `Microsoft.Network/virtualNetworks/subnets/join/action`
  * `Microsoft.Network/virtualNetworks/subnets/read`
  * `Microsoft.Network/virtualNetworks/subnets/write`
  * `Microsoft.Network/virtualNetworks/write`



Note

The following permissions are not required to create the private OpenShift Container Platform cluster on Azure. 

  * `Microsoft.Network/dnsZones/A/write`
  * `Microsoft.Network/dnsZones/CNAME/write`
  * `Microsoft.Network/dnszones/CNAME/read`
  * `Microsoft.Network/dnszones/read`



Required permissions for checking the health of resources
    

  * `Microsoft.Resourcehealth/healthevent/Activated/action`
  * `Microsoft.Resourcehealth/healthevent/InProgress/action`
  * `Microsoft.Resourcehealth/healthevent/Pending/action`
  * `Microsoft.Resourcehealth/healthevent/Resolved/action`
  * `Microsoft.Resourcehealth/healthevent/Updated/action`



Required permissions for creating a resource group
    

  * `Microsoft.Resources/subscriptions/resourceGroups/read`
  * `Microsoft.Resources/subscriptions/resourcegroups/write`



Optional permissions for attaching an existing user-assigned identity to a node
    

  * `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/read`



Required permissions for creating resource tags
    

  * `Microsoft.Resources/tags/write`



Required permissions for creating storage resources
    

  * `Microsoft.Storage/storageAccounts/blobServices/read`
  * `Microsoft.Storage/storageAccounts/blobServices/containers/write`
  * `Microsoft.Storage/storageAccounts/fileServices/read`
  * `Microsoft.Storage/storageAccounts/fileServices/shares/read`
  * `Microsoft.Storage/storageAccounts/fileServices/shares/write`
  * `Microsoft.Storage/storageAccounts/fileServices/shares/delete`
  * `Microsoft.Storage/storageAccounts/listKeys/action`
  * `Microsoft.Storage/storageAccounts/read`
  * `Microsoft.Storage/storageAccounts/write`



Important

The installation program creates the bootstrap ignition storage account with shared key access disabled, `allowSharedKeyAccess: false`, to align with security best practices from Microsoft. 

To provide this authorization, assign the `Storage Blob Data Contributor` role to the installing identity at the subscription or resource group scope. Without this role, installation fails during the bootstrap phase with an `AuthorizationPermissionMismatch` error. 

As a fallback, if you cannot grant the `Storage Blob Data Contributor` role, you can set `platform.azure.allowSharedKeyAccess` to `true` in the `install-config.yaml` file. This re-enables shared key authorization on the ignition storage account, allowing the existing management-plane permissions to complete the upload. 

Enabling shared key access allows any client with the storage account keys to access data without Azure Active Directory authentication; this approach weakens the access control posture of the storage account. Only enable shared key access when the data-plane role cannot be granted. 

Optional permissions for creating a private storage endpoint for the image registry
    

  * `Microsoft.Network/privateEndpoints/write`
  * `Microsoft.Network/privateEndpoints/read`
  * `Microsoft.Network/privateEndpoints/privateDnsZoneGroups/write`
  * `Microsoft.Network/privateEndpoints/privateDnsZoneGroups/read`
  * `Microsoft.Network/privateDnsZones/join/action`
  * `Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action`



Optional permissions for creating marketplace virtual machine resources
    

  * `Microsoft.MarketplaceOrdering/offertypes/publishers/offers/plans/agreements/read`
  * `Microsoft.MarketplaceOrdering/offertypes/publishers/offers/plans/agreements/write`



Optional permissions for creating compute resources
    

  * `Microsoft.Compute/availabilitySets/delete`
  * `Microsoft.Compute/images/read`
  * `Microsoft.Compute/images/write`
  * `Microsoft.Compute/images/delete`



Optional permissions for enabling user-managed encryption
    

  * `Microsoft.Compute/diskEncryptionSets/read`
  * `Microsoft.Compute/diskEncryptionSets/write`
  * `Microsoft.Compute/diskEncryptionSets/delete`
  * `Microsoft.KeyVault/vaults/read`
  * `Microsoft.KeyVault/vaults/write`
  * `Microsoft.KeyVault/vaults/delete`
  * `Microsoft.KeyVault/vaults/deploy/action`
  * `Microsoft.KeyVault/vaults/keys/read`
  * `Microsoft.KeyVault/vaults/keys/write`
  * `Microsoft.Features/providers/features/register/action`



Optional permissions for installing a cluster using the `NatGateway` outbound type
    

  * `Microsoft.Network/natGateways/read`
  * `Microsoft.Network/natGateways/write`



Optional permissions for installing a private cluster with Azure Network Address Translation (NAT)
    

  * `Microsoft.Network/natGateways/join/action`
  * `Microsoft.Network/natGateways/read`
  * `Microsoft.Network/natGateways/write`



Optional permissions for installing a private cluster with Azure firewall
    

  * `Microsoft.Network/azureFirewalls/applicationRuleCollections/write`
  * `Microsoft.Network/azureFirewalls/read`
  * `Microsoft.Network/azureFirewalls/write`
  * `Microsoft.Network/routeTables/join/action`
  * `Microsoft.Network/routeTables/read`
  * `Microsoft.Network/routeTables/routes/read`
  * `Microsoft.Network/routeTables/routes/write`
  * `Microsoft.Network/routeTables/write`
  * `Microsoft.Network/virtualNetworks/peer/action`
  * `Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read`
  * `Microsoft.Network/virtualNetworks/virtualNetworkPeerings/write`



Optional permission for running gather bootstrap
    

  * `Microsoft.Compute/virtualMachines/retrieveBootDiagnosticsData/action`



The following permissions are required for deleting an OpenShift Container Platform cluster on Microsoft Azure. You can use the same permissions to delete a private OpenShift Container Platform cluster on Azure. 

Required permissions for deleting authorization resources
    

  * `Microsoft.Authorization/roleAssignments/delete`



Required permissions for deleting compute resources
    

  * `Microsoft.Compute/disks/delete`
  * `Microsoft.Compute/galleries/delete`
  * `Microsoft.Compute/galleries/images/delete`
  * `Microsoft.Compute/galleries/images/versions/delete`
  * `Microsoft.Compute/virtualMachines/delete`



Required permissions for deleting identity management resources
    

  * `Microsoft.ManagedIdentity/userAssignedIdentities/delete`



Required permissions for deleting network resources
    

  * `Microsoft.Network/dnszones/read`
  * `Microsoft.Network/dnsZones/A/read`
  * `Microsoft.Network/dnsZones/A/delete`
  * `Microsoft.Network/dnsZones/CNAME/read`
  * `Microsoft.Network/dnsZones/CNAME/delete`
  * `Microsoft.Network/loadBalancers/delete`
  * `Microsoft.Network/networkInterfaces/delete`
  * `Microsoft.Network/networkSecurityGroups/delete`
  * `Microsoft.Network/privateDnsZones/read`
  * `Microsoft.Network/privateDnsZones/A/read`
  * `Microsoft.Network/privateDnsZones/delete`
  * `Microsoft.Network/privateDnsZones/virtualNetworkLinks/delete`
  * `Microsoft.Network/publicIPAddresses/delete`
  * `Microsoft.Network/virtualNetworks/delete`



Note

The following permissions are not required to delete a private OpenShift Container Platform cluster on Azure. 

  * `Microsoft.Network/dnszones/read`
  * `Microsoft.Network/dnsZones/A/read`
  * `Microsoft.Network/dnsZones/A/delete`
  * `Microsoft.Network/dnsZones/CNAME/read`
  * `Microsoft.Network/dnsZones/CNAME/delete`



Required permissions for checking the health of resources
    

  * `Microsoft.Resourcehealth/healthevent/Activated/action`
  * `Microsoft.Resourcehealth/healthevent/Resolved/action`
  * `Microsoft.Resourcehealth/healthevent/Updated/action`



Required permissions for deleting a resource group
    

  * `Microsoft.Resources/subscriptions/resourcegroups/delete`



Required permissions for deleting storage resources
    

  * `Microsoft.Storage/storageAccounts/delete`
  * `Microsoft.Storage/storageAccounts/listKeys/action`



Note

To install OpenShift Container Platform on Azure, you must scope the permissions to your subscription. You can re-scope these permissions to the resource group created by installation program. If the public DNS zone is present in a different resource group, then the network DNS zone related permissions must always be applied to your subscription. By default, the OpenShift Container Platform installation program assigns the Azure identity the `Contributor` role. 

You can scope all the permissions to your subscription when deleting an OpenShift Container Platform cluster. 

**Additional resources**

  * [Managing access to Azure resources using the Azure portal](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
  * [Custom roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)



**Additional resources**

  * [Managing access to Azure resources using the Azure portal (Azure documentation)](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
  * [Custom roles (Azure documentation)](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)



## 2.4.2. Using Azure managed identities

To provide the identity that the installation program requires on Azure, you can use a system-assigned or user-assigned managed identity. 

If you are unable to use a managed identity, you can use a service principal. 

**Procedure**

  1. If you are using a system-assigned managed identity, enable it on the virtual machine that you will run the installation program from. 
  2. If you are using a user-assigned managed identity: 

     1. Assign it to the virtual machine that you will run the installation program from. 
     2. Record its client ID. You require this value when installing the cluster. 

  3. Verify that the required permissions are assigned to the managed identity. 



**Additional resources**

  * [List user-assigned managed identities (Azure documentation)](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp#list-user-assigned-managed-identities)



## 2.4.3. Creating a service principal

To provide the identity that the installation program requires on Azure, you can create a service principal. 

If you are unable to use a service principal, you can use a managed identity. 

**Prerequisites**

  * You have installed or updated the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest). 
  * You have an Azure subscription ID. 
  * If you are not assigning the `Contributor` and `User Administrator Access` roles to the service principal, you have created a custom role with the required Azure permissions. 



**Procedure**

  1. Create the service principal for your account by running the following command: 

```shell-session
$ az ad sp create-for-rbac --role <role_name> \
     --name <service_principal> \
     --scopes /subscriptions/<subscription_id>
```


where: 

`<role_name>`
     Specifies the role name. You can use the `Contributor` role, or you can specify a custom role which contains the necessary permissions. 
`<service_principal>`
     Specifies the service principal name. 
`<subscription_id>`
    

Specifies the subscription ID. 

**Example output**

```shell-session
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "axxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```


Record the values of the `appId` and `password` parameters from the output. You require these values when installing the cluster. 

  2. If you assigned the `Contributor` role to your service principal, assign the `User Administrator Access` role by running the following command: 

```shell-session
$ az role assignment create --role "User Access Administrator" \
  --assignee-object-id $(az ad sp show --id <appId> --query id -o tsv) \
  --scope /subscriptions/<subscription_id>
```


where: 

`<appId>`
     Specifies the `appId` parameter value for your service principal. 
`<subscription_id>`
     Specifies the subscription ID. 




**Additional resources**

  * [About the Cloud Credential Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#about-cloud-credential-operator-modes)
