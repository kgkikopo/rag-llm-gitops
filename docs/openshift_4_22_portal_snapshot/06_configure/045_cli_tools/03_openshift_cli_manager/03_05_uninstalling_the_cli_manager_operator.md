# 3.5. Uninstalling the CLI Manager Operator

You can remove the CLI Manager Operator from OpenShift Container Platform by uninstalling the CLI Manager Operator and removing its related resources. 

Important

Using the CLI Manager Operator to install and manage plugins for the OpenShift CLI is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

## 3.5.1. Uninstalling the CLI Manager Operator

You can uninstall the CLI Manager Operator by using the web console. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * You have access to the OpenShift Container Platform web console. 
  * The CLI Manager Operator is installed. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Uninstall the CLI Manager Operator by completing the following steps: 

     1. Navigate to **Ecosystem** **Installed Operators**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-CLI_tools-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **CLI Manager Operator** entry and click **Uninstall Operator**. 
     3. In the confirmation dialog, click **Uninstall**. 




## 3.5.2. Removing CLI Manager Operator resources

Optionally, after you uninstall the CLI Manager Operator, you can remove its related resources from your cluster. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Remove the `openshift-cli-manager-operator` namespace: 

     1. Navigate to **Administration** **Namespaces**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-CLI_tools-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **openshift-cli-manager-operator** entry and select **Delete Namespace**. 
     3. In the confirmation dialog, enter `openshift-cli-manager-operator` in the field and click **Delete**.
