# 2.3. Recording the subscription and tenant IDs

To record the subscription and tenant IDs that the installation program requires for your Azure account, you can use the Azure CLI. 

**Prerequisites**

  * You have installed or updated the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest). 



**Procedure**

  1. Log in to the Azure CLI by running the following command: 

```shell-session
$ az login
```


  2. Ensure that you are using the right subscription: 

     1. View a list of available subscriptions by running the following command: 

```shell-session
$ az account list --refresh
```


**Example output**

```shell-session
[
  {
    "cloudName": "AzureCloud",
    "id": "8xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "isDefault": true,
    "name": "Subscription Name 1",
    "state": "Enabled",
    "tenantId": "6xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "user": {
      "name": "you@example.com",
      "type": "user"
    }
  },
  {
    "cloudName": "AzureCloud",
    "id": "9xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "isDefault": false,
    "name": "Subscription Name 2",
    "state": "Enabled",
    "tenantId": "7xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "user": {
      "name": "you2@example.com",
      "type": "user"
    }
  }
]
```


     2. View the details of the active account, and confirm that this is the subscription you want to use, by running the following command: 

```shell-session
$ az account show
```


**Example output**

```shell-session
{
  "environmentName": "AzureCloud",
  "id": "8xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "isDefault": true,
  "name": "Subscription Name 1",
  "state": "Enabled",
  "tenantId": "6xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
```


  3. If you are not using the right subscription: 

     1. Change the active subscription by running the following command: 

```shell-session
$ az account set -s <subscription_id>
```


     2. Verify that you are using the subscription you need by running the following command: 

```shell-session
$ az account show
```


**Example output**

```shell-session
{
  "environmentName": "AzureCloud",
  "id": "9xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "isDefault": true,
  "name": "Subscription Name 2",
  "state": "Enabled",
  "tenantId": "7xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "user": {
    "name": "you2@example.com",
    "type": "user"
  }
}
```


  4. Record the `id` and `tenantId` parameter values from the output. You require these values to install an OpenShift Container Platform cluster.
