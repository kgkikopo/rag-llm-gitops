# 8.5. Uninstalling the web terminal

Uninstalling the Web Terminal Operator does not remove any of the custom resource definitions (CRDs) or managed resources that are created when the Operator is installed. For security purposes, you must manually uninstall these components. By removing these components, you save cluster resources because terminals do not idle when the Operator is uninstalled. 

Uninstalling the web terminal is a two-step process: 

  1. Uninstall the Web Terminal Operator and related custom resources (CRs) that were added when you installed the Operator. 
  2. Uninstall the DevWorkspace Operator and its related custom resources that were added as a dependency of the Web Terminal Operator. 



## 8.5.1. Removing the Web Terminal Operator

You can uninstall the web terminal by removing the Web Terminal Operator and custom resources used by the Operator. 

**Prerequisites**

  * You have access to the OpenShift Container Platform web console as a user with the `cluster-admin` role. 
  * You have installed the `oc` CLI. 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Scroll the filter list or type a keyword into the **Filter by name** box to find the Web Terminal Operator. 
  3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) for the Web Terminal Operator, and then select **Uninstall Operator**. 
  4. In the **Uninstall Operator** confirmation dialog box, click **Uninstall** to remove the Operator, Operator deployments, and pods from the cluster. The Operator stops running and no longer receives updates. 



## 8.5.2. Removing the DevWorkspace Operator

To completely uninstall the web terminal, you must also remove the DevWorkspace Operator and custom resources used by the Operator. 

Important

The DevWorkspace Operator is a standalone Operator and might be required as a dependency for other Operators installed in the cluster. Follow the steps below only if you are sure that the DevWorkspace Operator is no longer needed. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster with cluster administrator permissions. 
  * You have installed the `oc` CLI. 



**Procedure**

  1. Remove the `DevWorkspace` custom resources used by the Operator, along with any related Kubernetes objects: 

```shell-session
$ oc delete devworkspaces.workspace.devfile.io --all-namespaces --all --wait
```


```shell-session
$ oc delete devworkspaceroutings.controller.devfile.io --all-namespaces --all --wait
```


Warning

If this step is not complete, finalizers make it difficult to fully uninstall the Operator. 

  2. Remove the CRDs used by the Operator: 

Warning

The DevWorkspace Operator provides custom resource definitions (CRDs) that use conversion webhooks. Failing to remove these CRDs can cause issues in the cluster. 

```shell-session
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspaceroutings.controller.devfile.io
```


```shell-session
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspaces.workspace.devfile.io
```


```shell-session
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspacetemplates.workspace.devfile.io
```


```shell-session
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspaceoperatorconfigs.controller.devfile.io
```


  3. Verify that all involved custom resource definitions are removed. The following command should not display any output: 

```shell-session
$ oc get customresourcedefinitions.apiextensions.k8s.io | grep "devfile.io"
```


  4. Remove the `devworkspace-webhook-server` deployment, mutating, and validating webhooks: 

```shell-session
$ oc delete deployment/devworkspace-webhook-server -n openshift-operators
```


```shell-session
$ oc delete mutatingwebhookconfigurations controller.devfile.io
```


```shell-session
$ oc delete validatingwebhookconfigurations controller.devfile.io
```


Note

If you remove the `devworkspace-webhook-server` deployment without removing the mutating and validating webhooks, you cannot use `oc exec` commands to run commands in a container in the cluster. After you remove the webhooks you can use the `oc exec` commands again. 

  5. Remove any remaining services, secrets, and config maps. Depending on the installation, some resources included in the following commands might not exist in the cluster. 

```shell-session
$ oc delete all --selector app.kubernetes.io/part-of=devworkspace-operator,app.kubernetes.io/name=devworkspace-webhook-server -n openshift-operators
```


```shell-session
$ oc delete serviceaccounts devworkspace-webhook-server -n openshift-operators
```


```shell-session
$ oc delete clusterrole devworkspace-webhook-server
```


```shell-session
$ oc delete clusterrolebinding devworkspace-webhook-server
```


  6. Uninstall the DevWorkspace Operator: 

     1. In the **Administrator** perspective of the web console, navigate to **Ecosystem** **Installed Operators**. 
     2. Scroll the filter list or type a keyword into the **Filter by name** box to find the DevWorkspace Operator. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) for the Operator, and then select **Uninstall Operator**. 
     4. In the **Uninstall Operator** confirmation dialog box, click **Uninstall** to remove the Operator, Operator deployments, and pods from the cluster. The Operator stops running and no longer receives updates.
