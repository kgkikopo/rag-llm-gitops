# 2.4. Creating a service principal

To enable OpenShift Container Platform to create Azure resources, you must create a service principal that represents the installation program in Azure Resource Manager. 

**Prerequisites**

  * Install or update the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest). 
  * Your Azure account has the required roles for the subscription that you use. 



**Procedure**

  1. Register your environment: 

```shell-session
$ az cloud register -n AzureStackCloud --endpoint-resource-manager <endpoint>
```


`<endpoint>` is the Azure Resource Manager endpoint, `https://management.<region>.<fqdn>/`. 

See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure-stack/mdc/azure-stack-version-profiles-azurecli-2-tzl#connect-to-azure-stack-hub) for details. 

  2. Set the active environment: 

```shell-session
$ az cloud set -n AzureStackCloud
```


  3. Update your environment configuration to use the specific API version for Azure Stack Hub: 

```shell-session
$ az cloud update --profile 2019-03-01-hybrid
```


  4. Log in to the Azure CLI: 

```shell-session
$ az login
```


If you are in a multitenant environment, you must also supply the tenant ID. 

  5. If your Azure account uses subscriptions, ensure that you are using the right subscription: 

     1. View the list of available accounts and record the `tenantId` value for the subscription you want to use for your cluster: 

```shell-session
$ az account list --refresh
```


**Example output**

```shell-session
[
  {
    "cloudName": AzureStackCloud",
    "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
    "isDefault": true,
    "name": "Subscription Name",
    "state": "Enabled",
    "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee",
    "user": {
      "name": "you@example.com",
      "type": "user"
    }
  }
]
```


     2. View your active account details and confirm that the `tenantId` value matches the subscription you want to use: 

```shell-session
$ az account show
```


**Example output**

```shell-session
{
  "environmentName": AzureStackCloud",
  "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee",
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
```


Ensure that the value of the `tenantId` parameter is the correct subscription ID. 

     3. If you are not using the right subscription, change the active subscription: 

```shell-session
$ az account set -s <subscription_id>
```


For `<subscription_id>`, specify the subscription ID. 

     4. Verify the subscription ID update: 

```shell-session
$ az account show
```


**Example output**

```shell-session
{
  "environmentName": AzureStackCloud",
  "id": "33212d16-bdf6-45cb-b038-f6565b61edda",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee",
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
```


  6. Record the `tenantId` and `id` parameter values from the output. You need these values during the OpenShift Container Platform installation. 
  7. Create the service principal for your account: 

```shell-session
$ az ad sp create-for-rbac --role Contributor --name <service_principal> \
  --scopes /subscriptions/<subscription_id> \
  --years <years>
```


where: 

`<service_principal>`
     Specifies the service principal name. 
`<subscription_id>`
     Specifies the subscription ID. 
`<years>`
    

Specifies the number of years. By default, a service principal expires in one year. By using the `--years` option you can extend the validity of your service principal. 

**Example output**

```shell-session
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
}
```


  8. Record the values of the `appId` and `password` parameters from the previous output. You need these values during OpenShift Container Platform installation. 



**Additional resources**

  * [About the Cloud Credential Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#about-cloud-credential-operator-modes)
