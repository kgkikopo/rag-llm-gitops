# 2.29. Uninstalling Service Mesh

To uninstall Red Hat OpenShift Service Mesh from an existing OpenShift Container Platform instance and remove its resources, you must delete the control plane, delete the Operators, and run commands to manually remove some resources. 

## 2.29.1. Removing the Red Hat OpenShift Service Mesh control plane

To uninstall Service Mesh from an existing OpenShift Container Platform instance, first you delete the Service Mesh control plane and the Operators. Then, you run commands to remove residual resources. 

### 2.29.1.1. Removing the Service Mesh control plane using the web console

You can remove the Red Hat OpenShift Service Mesh control plane by using the web console. 

**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Click the **Project** menu and select the project where you installed the Service Mesh control plane, for example **istio-system**. 
  3. Navigate to **Ecosystem** **Installed Operators**. 
  4. Click **Service Mesh Control Plane** under **Provided APIs**. 
  5. Click the `ServiceMeshControlPlane` menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) . 
  6. Click **Delete Service Mesh Control Plane**. 
  7. Click **Delete** on the confirmation dialog window to remove the `ServiceMeshControlPlane`. 



### 2.29.1.2. Removing the Service Mesh control plane using the CLI

You can remove the Red Hat OpenShift Service Mesh control plane by using the CLI. In this example, `istio-system` is the name of the control plane project. 

**Procedure**

  1. Log in to the OpenShift Container Platform CLI. 
  2. Run the following command to delete the `ServiceMeshMemberRoll` resource. 

```shell-session
$ oc delete smmr -n istio-system default
```


  3. Run this command to retrieve the name of the installed `ServiceMeshControlPlane`: 

```shell-session
$ oc get smcp -n istio-system
```


  4. Replace `<name_of_custom_resource>` with the output from the previous command, and run this command to remove the custom resource: 

```shell-session
$ oc delete smcp -n istio-system <name_of_custom_resource>
```


## 2.29.2. Removing the installed Operators

You must remove the Operators to successfully remove Red Hat OpenShift Service Mesh. After you remove the Red Hat OpenShift Service Mesh Operator, you must remove the Kiali Operator, the Red Hat OpenShift Distributed Tracing Platform (Jaeger) Operator, and the OpenShift Elasticsearch Operator. 

### 2.29.2.1. Removing the Operators

Follow this procedure to remove the Operators that make up Red Hat OpenShift Service Mesh. Repeat the steps for each of the following Operators. 

  * Red Hat OpenShift Service Mesh 
  * Kiali 
  * Red Hat OpenShift Distributed Tracing Platform (Jaeger) 
  * OpenShift Elasticsearch 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. From the **Ecosystem** **Installed Operators** page, scroll or type a keyword into the **Filter by name** to find each Operator. Then, click the Operator name. 
  3. On the **Operator Details** page, select **Uninstall Operator** from the **Actions** menu. Follow the prompts to uninstall each Operator. 



## 2.29.3. Clean up Operator resources

You can manually remove resources left behind after removing the Red Hat OpenShift Service Mesh Operator using the OpenShift Container Platform web console. 

**Prerequisites**

  * An account with cluster administration access. If you use Red Hat OpenShift Dedicated, you must have an account with the `dedicated-admin` role. 
  * Access to the OpenShift CLI (`oc`). 



**Procedure**

  1. Log in to the OpenShift Container Platform CLI as a cluster administrator. 
  2. Run the following commands to clean up resources after uninstalling the Operators. If you intend to keep using Distributed Tracing Platform (Jaeger) as a stand-alone service without service mesh, do not delete the Jaeger resources. 

Note

The OpenShift Elasticsearch Operator is installed in `openshift-operators-redhat` by default. The other Operators are installed in the `openshift-operators` namespace by default. If you installed the Operators in another namespace, replace `openshift-operators` with the name of the project where the Red Hat OpenShift Service Mesh Operator was installed. 

```shell-session
$ oc -n openshift-operators delete ds -lmaistra-version
```


```shell-session
$ oc delete clusterrole/istio-admin clusterrole/istio-cni clusterrolebinding/istio-cni clusterrole/ossm-cni clusterrolebinding/ossm-cni
```


```shell-session
$ oc delete clusterrole istio-view istio-edit
```


```shell-session
$ oc delete clusterrole jaegers.jaegertracing.io-v1-admin jaegers.jaegertracing.io-v1-crdview jaegers.jaegertracing.io-v1-edit jaegers.jaegertracing.io-v1-view
```


```shell-session
$ oc get crds -o name | grep '.*\.istio\.io' | xargs -r -n 1 oc delete
```


```shell-session
$ oc get crds -o name | grep '.*\.maistra\.io' | xargs -r -n 1 oc delete
```


```shell-session
$ oc get crds -o name | grep '.*\.kiali\.io' | xargs -r -n 1 oc delete
```


```shell-session
$ oc delete crds jaegers.jaegertracing.io
```


```shell-session
$ oc delete cm -n openshift-operators -lmaistra-version
```


```shell-session
$ oc delete sa -n openshift-operators -lmaistra-version
```
