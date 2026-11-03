# 2.6. Configure a private storage endpoint on Azure

You can configure the Image Registry Operator to use a private Azure storage endpoint so that registry storage is not exposed through a public-facing endpoint. 

You can leverage the Image Registry Operator to use private endpoints on Azure, which enables seamless configuration of private storage accounts when OpenShift Container Platform is deployed on private Azure clusters. This allows you to deploy the image registry without exposing public-facing storage endpoints. 

Important

Do not configure a private storage endpoint on Microsoft Azure Red Hat OpenShift (ARO), because the endpoint can put your Microsoft Azure Red Hat OpenShift cluster in an unrecoverable state. 

You can configure the Image Registry Operator to use private storage endpoints on Azure in one of two ways: 

  * By configuring the Image Registry Operator to discover the VNet and subnet names 
  * With user-provided Azure Virtual Network (VNet) and subnet names 



## 2.6.1. Limitations for configuring a private storage endpoint on Azure

The following limitations apply when configuring a private storage endpoint on Azure: 

  * When configuring the Image Registry Operator to use a private storage endpoint, public network access to the storage account is disabled. Consequently, pulling images from the registry outside of OpenShift Container Platform only works by setting `disableRedirect: true` in the registry Operator configuration. With redirect enabled, the registry redirects the client to pull images directly from the storage account, which will no longer work due to disabled public network access. For more information, see "Disabling redirect when using a private storage endpoint on Azure". 
  * This operation cannot be undone by the Image Registry Operator. 



## 2.6.2. Configure a private storage endpoint on Azure by enabling the Image Registry Operator to discover VNet and subnet names

You can configure a private Azure storage endpoint by enabling the Image Registry Operator to discover the VNet and subnet, allowing registry storage without public network access. 

The following procedure shows you how to set up a private storage endpoint on Azure by configuring the Image Registry Operator to discover VNet and subnet names. 

**Prerequisites**

  * You have configured the image registry to run on Azure. 
  * Your network has been set up using the Installer Provisioned Infrastructure installation method. 

For users with a custom network setup, see "Configuring a private storage endpoint on Azure with user-provided VNet and subnet names". 




**Procedure**

  1. Edit the Image Registry Operator `config` object and set `networkAccess.type` to `Internal`: 

```shell-session
$ oc edit configs.imageregistry/cluster
```


```shell-session
# ...
spec:
  # ...
   storage:
      azure:
        # ...
        networkAccess:
          type: Internal
# ...
```


  2. Optional: Enter the following command to confirm that the Operator has completed provisioning. This might take a few minutes. 

```shell-session
$ oc get configs.imageregistry/cluster -o=jsonpath="{.spec.storage.azure.privateEndpointName}" -w
```


  3. Optional: If the registry is exposed by a route, and you are configuring your storage account to be private, you must disable redirect if you want pulls external to the cluster to continue to work. Enter the following command to disable redirect on the Image Operator configuration: 

```shell-session
$ oc patch configs.imageregistry cluster --type=merge -p '{"spec":{"disableRedirect": true}}'
```


Note

When redirect is enabled, pulling images from outside of the cluster will not work. 




**Verification**

  1. Fetch the registry service name by running the following command: 

```shell-session
$ oc get imagestream -n openshift
```


**Example output**

```shell-session
NAME   IMAGE REPOSITORY                                                 TAGS     UPDATED
cli    image-registry.openshift-image-registry.svc:5000/openshift/cli   latest   8 hours ago
...
```


  2. Enter debug mode by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  3. Run the suggested `chroot` command. For example: 

```shell-session
$ chroot /host
```


  4. Enter the following command to log in to your container registry: 

```shell-session
$ podman login --tls-verify=false -u unused -p $(oc whoami -t) image-registry.openshift-image-registry.svc:5000
```


**Example output**

```shell-session
Login Succeeded!
```


  5. Enter the following command to verify that you can pull an image from the registry: 

```shell-session
$ podman pull --tls-verify=false image-registry.openshift-image-registry.svc:5000/openshift/tools
```


**Example output**

```shell-session
Trying to pull image-registry.openshift-image-registry.svc:5000/openshift/tools/openshift/tools...
Getting image source signatures
Copying blob 6b245f040973 done
Copying config 22667f5368 done
Writing manifest to image destination
Storing signatures
22667f53682a2920948d19c7133ab1c9c3f745805c14125859d20cede07f11f9
```


## 2.6.3. Configure a private storage endpoint on Azure with user-provided VNet and subnet names

You can configure a private Azure storage endpoint for the image registry by specifying user-provided VNet and subnet names, enabling registry storage without public network access. 

Use the following procedure to configure a storage account that has public network access disabled and is exposed behind a private storage endpoint on Azure. 

**Prerequisites**

  * You have configured the image registry to run on Azure. 
  * You must know the VNet and subnet names used for your Azure environment. 
  * If your network was configured in a separate resource group in Azure, you must also know its name. 



**Procedure**

  1. Edit the Image Registry Operator `config` object and configure the private endpoint using your VNet and subnet names: 

```shell-session
$ oc edit configs.imageregistry/cluster
```


```shell-session
# ...
spec:
  # ...
   storage:
      azure:
        # ...
        networkAccess:
          type: Internal
          internal:
            subnetName: <subnet_name>
            vnetName: <vnet_name>
            networkResourceGroupName: <network_resource_group_name>
# ...
```


  2. Optional: Enter the following command to confirm that the Operator has completed provisioning. This might take a few minutes. 

```shell-session
$ oc get configs.imageregistry/cluster -o=jsonpath="{.spec.storage.azure.privateEndpointName}" -w
```


Note

When redirect is enabled, pulling images from outside of the cluster will not work. 




**Verification**

  1. Fetch the registry service name by running the following command: 

```shell-session
$ oc get imagestream -n openshift
```


**Example output**

```shell-session
NAME   IMAGE REPOSITORY                                                 TAGS     UPDATED
cli    image-registry.openshift-image-registry.svc:5000/openshift/cli   latest   8 hours ago
...
```


  2. Enter debug mode by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  3. Run the suggested `chroot` command. For example: 

```shell-session
$ chroot /host
```


  4. Enter the following command to log in to your container registry: 

```shell-session
$ podman login --tls-verify=false -u unused -p $(oc whoami -t) image-registry.openshift-image-registry.svc:5000
```


**Example output**

```shell-session
Login Succeeded!
```


  5. Enter the following command to verify that you can pull an image from the registry: 

```shell-session
$ podman pull --tls-verify=false image-registry.openshift-image-registry.svc:5000/openshift/tools
```


**Example output**

```shell-session
Trying to pull image-registry.openshift-image-registry.svc:5000/openshift/tools/openshift/tools...
Getting image source signatures
Copying blob 6b245f040973 done
Copying config 22667f5368 done
Writing manifest to image destination
Storing signatures
22667f53682a2920948d19c7133ab1c9c3f745805c14125859d20cede07f11f9
```


## 2.6.4. Optional: Disabling redirect when using a private storage endpoint on Azure

You can disable redirect when using a private Azure storage endpoint so that users outside the cluster can pull images through the image registry route. 

By default, redirect is enabled when using the image registry. Redirect allows off-loading of traffic from the registry pods into the object storage, which makes pull faster. When redirect is enabled and the storage account is private, users from outside of the cluster are unable to pull images from the registry. 

In some cases, users might want to disable redirect so that users from outside of the cluster can pull images from the registry. 

**Prerequisites**

  * You have configured the image registry to run on Azure. 
  * You have configured a route. 



**Procedure**

  * Enter the following command to disable redirect on the image registry configuration: 

```shell-session
$ oc patch configs.imageregistry cluster --type=merge -p '{"spec":{"disableRedirect": true}}'
```


**Verification**

  1. Fetch the registry service name by running the following command: 

```shell-session
$ oc get imagestream -n openshift
```


**Example output**

```shell-session
NAME   IMAGE REPOSITORY                                           TAGS     UPDATED
cli    default-route-openshift-image-registry.<cluster_dns>/cli   latest   8 hours ago
...
```


  2. Enter the following command to log in to your container registry: 

```shell-session
$ podman login --tls-verify=false -u unused -p $(oc whoami -t) default-route-openshift-image-registry.<cluster_dns>
```


**Example output**

```shell-session
Login Succeeded!
```


  3. Enter the following command to verify that you can pull an image from the registry: 

```shell-session
$ podman pull --tls-verify=false default-route-openshift-image-registry.<cluster_dns>
/openshift/tools
```


**Example output**

```shell-session
Trying to pull default-route-openshift-image-registry.<cluster_dns>/openshift/tools...
Getting image source signatures
Copying blob 6b245f040973 done
Copying config 22667f5368 done
Writing manifest to image destination
Storing signatures
22667f53682a2920948d19c7133ab1c9c3f745805c14125859d20cede07f11f9
```
