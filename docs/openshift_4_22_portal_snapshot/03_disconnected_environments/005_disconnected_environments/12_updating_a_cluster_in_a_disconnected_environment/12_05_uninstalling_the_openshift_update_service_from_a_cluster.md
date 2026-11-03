# 12.5. Uninstalling the OpenShift Update Service from a cluster

You can remove a local copy of the OpenShift Update Service (OSUS) from your cluster. To do this, you must first delete the OSUS application and then uninstall the OSUS Operator. 

## 12.5.1. Deleting an OpenShift Update Service application

You can delete an OpenShift Update Service application by using the OpenShift Container Platform web console or CLI. 

### 12.5.1.1. Deleting an OpenShift Update Service application by using the web console

You can use the OpenShift Container Platform web console to delete an OpenShift Update Service application by using the OpenShift Update Service Operator. 

**Prerequisites**

  * The OpenShift Update Service Operator has been installed. 



**Procedure**

  1. In the web console, click **Ecosystem** **Installed Operators**. 
  2. Choose **OpenShift Update Service** from the list of installed Operators. 
  3. Click the **Update Service** tab. 
  4. From the list of installed OpenShift Update Service applications, select the application to be deleted and then click **Delete UpdateService**. 
  5. From the **Delete UpdateService?** confirmation dialog, click **Delete** to confirm the deletion. 



### 12.5.1.2. Deleting an OpenShift Update Service application by using the CLI

You can use the OpenShift CLI (`oc`) to delete an OpenShift Update Service application. 

**Procedure**

  1. Get the OpenShift Update Service application name using the namespace the OpenShift Update Service application was created in, for example, `openshift-update-service`: 

```shell-session
$ oc get updateservice -n openshift-update-service
```


**Example output**

```shell-session
NAME      AGE
service   6s
```


  2. Delete the OpenShift Update Service application using the `NAME` value from the previous step and the namespace the OpenShift Update Service application was created in, for example, `openshift-update-service`: 

```shell-session
$ oc delete updateservice service -n openshift-update-service
```


**Example output**

```shell-session
updateservice.updateservice.operator.openshift.io "service" deleted
```


## 12.5.2. Uninstall the OpenShift Update Service Operator

You can uninstall the OpenShift Update Service Operator by using the OpenShift Container Platform web console or CLI. 

### 12.5.2.1. Uninstall the OpenShift Update Service Operator by using the web console

You can use the OpenShift Container Platform web console to uninstall the OpenShift Update Service Operator. 

**Prerequisites**

  * All OpenShift Update Service applications have been deleted. 



**Procedure**

  1. In the web console, click **Ecosystem** **Installed Operators**. 
  2. Select **OpenShift Update Service** from the list of installed Operators and click **Uninstall Operator**. 
  3. From the **Uninstall Operator?** confirmation dialog, click **Uninstall** to confirm the uninstallation. 



### 12.5.2.2. Uninstall the OpenShift Update Service Operator by using the CLI

You can use the OpenShift CLI (`oc`) to uninstall the OpenShift Update Service Operator. 

**Prerequisites**

  * All OpenShift Update Service applications have been deleted. 



**Procedure**

  1. Change to the project containing the OpenShift Update Service Operator, for example, `openshift-update-service`: 

```shell-session
$ oc project openshift-update-service
```


**Example output**

```shell-session
Now using project "openshift-update-service" on server "https://example.com:6443".
```


  2. Get the name of the OpenShift Update Service Operator operator group: 

```shell-session
$ oc get operatorgroup
```


**Example output**

```shell-session
NAME                             AGE
openshift-update-service-fprx2   4m41s
```


  3. Delete the operator group, for example, `openshift-update-service-fprx2`: 

```shell-session
$ oc delete operatorgroup openshift-update-service-fprx2
```


**Example output**

```shell-session
operatorgroup.operators.coreos.com "openshift-update-service-fprx2" deleted
```


  4. Get the name of the OpenShift Update Service Operator subscription: 

```shell-session
$ oc get subscription
```


**Example output**

```shell-session
NAME                      PACKAGE                   SOURCE                        CHANNEL
update-service-operator   update-service-operator   updateservice-index-catalog   v1
```


  5. Using the `Name` value from the previous step, check the current version of the subscribed OpenShift Update Service Operator in the `currentCSV` field: 

```shell-session
$ oc get subscription update-service-operator -o yaml | grep " currentCSV"
```


**Example output**

```shell-session
  currentCSV: update-service-operator.v0.0.1
```


  6. Delete the subscription, for example, `update-service-operator`: 

```shell-session
$ oc delete subscription update-service-operator
```


**Example output**

```shell-session
subscription.operators.coreos.com "update-service-operator" deleted
```


  7. Delete the CSV for the OpenShift Update Service Operator using the `currentCSV` value from the previous step: 

```shell-session
$ oc delete clusterserviceversion update-service-operator.v0.0.1
```


**Example output**

```shell-session
clusterserviceversion.operators.coreos.com "update-service-operator.v0.0.1" deleted
```
