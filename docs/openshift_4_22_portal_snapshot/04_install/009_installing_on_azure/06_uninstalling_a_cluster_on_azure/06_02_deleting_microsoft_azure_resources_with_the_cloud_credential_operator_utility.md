# 6.2. Deleting Microsoft Azure resources with the Cloud Credential Operator utility

After uninstalling an OpenShift Container Platform cluster that uses short-term credentials managed outside the cluster, you can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to remove the Microsoft Azure resources that `ccoctl` created during installation. 

**Prerequisites**

  * Extract and prepare the `ccoctl` binary. 
  * Uninstall an OpenShift Container Platform cluster on Azure that uses short-term credentials. 



**Procedure**

  * Delete the Azure resources that `ccoctl` created by running the following command: 

```shell-session
$ ccoctl azure delete \
  --name=<name> \
  --region=<azure_region> \
  --subscription-id=<azure_subscription_id> \
  --delete-oidc-resource-group
```


where: 

`<name>`
     Matches the name that was originally used to create and tag the cloud resources. 
`<azure_region>`
     is the Azure region in which to delete cloud resources. 
`<azure_subscription_id>`
     is the Azure subscription ID for which to delete cloud resources. 




**Verification**

  * To verify that the resources are deleted, query Azure. For more information, refer to Azure documentation.
