# 2.10. Adding services to a service mesh

A project contains services; however, the services are only available if you add the project to the service mesh. 

## 2.10.1. About adding projects to a service mesh

After installing the Operators and creating the `ServiceMeshControlPlane` resource, add one or more projects to the service mesh. 

Note

In OpenShift Container Platform, a project is essentially a Kubernetes namespace with additional annotations, such as the range of user IDs that can be used in the project. Typically, the OpenShift Container Platform web console uses the term project, and the CLI uses the term namespace, but the terms are essentially synonymous. 

You can add projects to an existing service mesh using either the OpenShift Container Platform web console or the CLI. There are three methods to add a project to a service mesh: 

  * Specifying the project name in the `ServiceMeshMemberRoll` resource. 
  * Configuring label selectors in the `spec.memberSelectors` field of the `ServiceMeshMemberRoll` resource. 
  * Creating the `ServiceMeshMember` resource in the project. 



If you use the first method, then you must create the `ServiceMeshMemberRoll` resource. 

## 2.10.2. Creating the Red Hat OpenShift Service Mesh member roll

The `ServiceMeshMemberRoll` lists the projects that belong to the Service Mesh control plane. Only projects listed in the `ServiceMeshMemberRoll` are affected by the control plane. A project does not belong to a service mesh until you add it to the member roll for a particular control plane deployment. 

You must create a `ServiceMeshMemberRoll` resource named `default` in the same project as the `ServiceMeshControlPlane`, for example `istio-system`. 

### 2.10.2.1. Creating the member roll from the web console

You can add one or more projects to the Service Mesh member roll from the web console. In this example, `istio-system` is the name of the Service Mesh control plane project. 

**Prerequisites**

  * An installed, verified Red Hat OpenShift Service Mesh Operator. 
  * List of existing projects to add to the service mesh. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. If you do not already have services for your mesh, or you are starting from scratch, create a project for your applications. It must be different from the project where you installed the Service Mesh control plane. 

     1. Navigate to **Home** **Projects**. 
     2. Enter a name in the **Name** field. 
     3. Click **Create**. 

  3. Navigate to **Ecosystem** **Installed Operators**. 
  4. Click the **Project** menu and choose the project where your `ServiceMeshControlPlane` resource is deployed from the list, for example `istio-system`. 
  5. Click the Red Hat OpenShift Service Mesh Operator. 
  6. Click the **Istio Service Mesh Member Roll** tab. 
  7. Click **Create ServiceMeshMemberRoll**
  8. Click **Members** , then enter the name of your project in the **Value** field. You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource. 
  9. Click **Create**. 



### 2.10.2.2. Creating the member roll from the CLI

You can add a project to the `ServiceMeshMemberRoll` from the command line. 

**Prerequisites**

  * An installed, verified Red Hat OpenShift Service Mesh Operator. 
  * List of projects to add to the service mesh. 
  * Access to the OpenShift CLI (`oc`). 



**Procedure**

  1. Log in to the OpenShift Container Platform CLI. 

```shell-session
$ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
```


  2. If you do not already have services for your mesh, or you are starting from scratch, create a project for your applications. It must be different from the project where you installed the Service Mesh control plane. 

```shell-session
$ oc new-project <your-project>
```


  3. To add your projects as members, modify the following example YAML. You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource. In this example, `istio-system` is the name of the Service Mesh control plane project. 

**Example servicemeshmemberroll-default.yaml**

```yaml
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system
spec:
  members:
    # a list of projects joined into the service mesh
    - your-project-name
    - another-project-name
```


  4. Run the following command to upload and create the `ServiceMeshMemberRoll` resource in the `istio-system` namespace. 

```shell-session
$ oc create -n istio-system -f servicemeshmemberroll-default.yaml
```


  5. Run the following command to verify the `ServiceMeshMemberRoll` was created successfully. 

```shell-session
$ oc get smmr -n istio-system default
```


The installation has finished successfully when the `STATUS` column is `Configured`. 




## 2.10.3. About adding projects using the ServiceMeshMemberRoll resource

Using the `ServiceMeshMemberRoll` resource is the simplest way to add a project to a service mesh. To add a project, specify the project name in the `spec.members` field of the `ServiceMeshMemberRoll` resource. The `ServiceMeshMemberRoll` resource specifies which projects are controlled by the `ServiceMeshControlPlane` resource. 

![Adding project using `ServiceMeshMemberRoll` resource image](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/9fdd62329fa28022e3dcca9df5861e18/ossm-adding-project-using-smmr.png) ![Adding project using `ServiceMeshMemberRoll` resource image](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/9fdd62329fa28022e3dcca9df5861e18/ossm-adding-project-using-smmr.png)

Note

Adding projects using this method requires the user to have the `update servicemeshmemberrolls` and the `update pods` privileges in the project that is being added. 

  * If you already have an application, workload, or service to add to the service mesh, see the following: 

    * Adding or removing projects from the mesh using the `ServiceMeshMemberRoll` resource with the web console 
    * Adding or removing projects from the mesh using the `ServiceMeshMemberRoll` resource with the CLI 

  * Alternatively, to install a sample application called Bookinfo and add it to a `ServiceMeshMemberRoll` resource, see the Bookinfo example application tutorial. 



### 2.10.3.1. Adding or removing projects from the mesh using the ServiceMeshMemberRoll resource with the web console

You can add or remove projects from the mesh using the `ServiceMeshMemberRoll` resource with the OpenShift Container Platform web console. You can add any number of projects, but a project can only belong to one mesh. 

The `ServiceMeshMemberRoll` resource is deleted when its corresponding `ServiceMeshControlPlane` resource is deleted. 

**Prerequisites**

  * An installed, verified Red Hat OpenShift Service Mesh Operator. 
  * An existing `ServiceMeshMemberRoll` resource. 
  * The name of the project with the `ServiceMeshMemberRoll` resource. 
  * The names of the projects you want to add or remove from the mesh. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Navigate to **Ecosystem** **Installed Operators**. 
  3. Click the **Project** menu and choose the project where your `ServiceMeshControlPlane` resource is deployed from the list. For example `istio-system`. 
  4. Click the Red Hat OpenShift Service Mesh Operator. 
  5. Click the **Istio Service Mesh Member Roll** tab. 
  6. Click the `default` link. 
  7. Click the YAML tab. 
  8. Modify the YAML to add projects as members (or delete them to remove existing members). You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource. 

**Example servicemeshmemberroll-default.yaml**

```yaml
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system #control plane project
spec:
  members:
    # a list of projects joined into the service mesh
    - your-project-name
    - another-project-name
```


  9. Click **Save**. 
  10. Click **Reload**. 



### 2.10.3.2. Adding or removing projects from the mesh using ServiceMeshMemberRoll resource with the CLI

You can add one or more projects to the mesh using the `ServiceMeshMemberRoll` resource with the CLI. You can add any number of projects, but a project can only belong to one mesh. 

The `ServiceMeshMemberRoll` resource is deleted when its corresponding `ServiceMeshControlPlane` resource is deleted. 

**Prerequisites**

  * An installed, verified Red Hat OpenShift Service Mesh Operator. 
  * An existing `ServiceMeshMemberRoll` resource. 
  * The name of the project with the `ServiceMeshMemberRoll` resource. 
  * The names of the projects you want to add or remove from the mesh. 
  * Access to the OpenShift CLI (`oc`). 



**Procedure**

  1. Log in to the OpenShift Container Platform CLI. 
  2. Edit the `ServiceMeshMemberRoll` resource. 

```shell-session
$ oc edit smmr -n <controlplane-namespace>
```


  3. Modify the YAML to add or remove projects as members. You can add any number of projects, but a project can only belong to one `ServiceMeshMemberRoll` resource. 

**Example servicemeshmemberroll-default.yaml**

```yaml
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system #control plane project
spec:
  members:
    # a list of projects joined into the service mesh
    - your-project-name
    - another-project-name
```


  4. Save the file and exit the editor. 



## 2.10.4. About adding projects using the ServiceMeshMember resource

A `ServiceMeshMember` resource provides a way to add a project to a service mesh without modifying the `ServiceMeshMemberRoll` resource. To add a project, create a `ServiceMeshMember` resource in the project that you want to add to the service mesh. When the Service Mesh Operator processes the `ServiceMeshMember` object, the project appears in the `status.members` list of the `ServiceMeshMemberRoll` resource. Then, the services that reside in the project are made available to the mesh. 

![Adding project using `ServiceMeshMember` resource image](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/1afa6b490d576140209bb078c2c2b9af/ossm-adding-project-using-smm.png) ![Adding project using `ServiceMeshMember` resource image](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/1afa6b490d576140209bb078c2c2b9af/ossm-adding-project-using-smm.png)

The mesh administrator must grant each mesh user permission to reference the `ServiceMeshControlPlane` resource in the `ServiceMeshMember` resource. With this permission in place, a mesh user can add a project to a mesh even when that user does not have direct access rights for the service mesh project or the `ServiceMeshMemberRoll` resource. For more information, see Creating the Red Hat OpenShift Service Mesh members. 

### 2.10.4.1. Adding a project to the mesh using the ServiceMeshMember resource with the web console

You can add one or more projects to the mesh using the `ServiceMeshMember` resource with the OpenShift Container Platform web console. 

**Prerequisites**

  * You have installed the Red Hat OpenShift Service Mesh Operator. 
  * You know the name of the `ServiceMeshControlPlane` resource and the name of the project that the resource belongs to. 
  * You know the name of the project you want to add to the mesh. 
  * A service mesh administrator must explicitly grant access to the service mesh. Administrators can grant users permissions to access the mesh by assigning them the `mesh-user` `Role` using a `RoleBinding` or `ClusterRoleBinding`. For more information, see _Creating the Red Hat OpenShift Service Mesh members_. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Navigate to **Ecosystem** **Installed Operators**. 
  3. Click the **Project** menu and choose the project that you want to add to the mesh from the drop-down list. For example, `istio-system`. 
  4. Click the Red Hat OpenShift Service Mesh Operator. 
  5. Click the **Istio Service Mesh Member** tab. 
  6. Click **Create ServiceMeshMember**
  7. Accept the default name for the `ServiceMeshMember`. 
  8. Click to expand **ControlPlaneRef**. 
  9. In the **Namespace** field, select the project that the `ServiceMeshControlPlane` resource belongs to. For example, `istio-system`. 
  10. In the **Name** field, enter the name of the `ServiceMeshControlPlane` resource that this namespace belongs to. For example, `basic`. 
  11. Click **Create**. 



**Verification**

  1. Confirm the `ServiceMeshMember` resource was created and that the project was added to the mesh by using the following steps: 

     1. Click the resource name, for example, `default`. 
     2. View the **Conditions** section shown at the end of the screen. 
     3. Confirm that the `Status` of the `Reconciled` and `Ready` conditions is `True`. 

If the `Status` is `False`, see the `Reason` and `Message` columns for more information. 




### 2.10.4.2. Adding a project to the mesh using the ServiceMeshMember resource with the CLI

You can add one or more projects to the mesh using the `ServiceMeshMember` resource with the CLI. 

**Prerequisites**

  * You have installed the Red Hat OpenShift Service Mesh Operator. 
  * You know the name of the `ServiceMeshControlPlane` resource and the name of the project it belongs to. 
  * You know the name of the project you want to add to the mesh. 
  * A service mesh administrator must explicitly grant access to the service mesh. Administrators can grant users permissions to access the mesh by assigning them the `mesh-user` `Role` using a `RoleBinding` or `ClusterRoleBinding`. For more information, see _Creating the Red Hat OpenShift Service Mesh members_. 



**Procedure**

  1. Log in to the OpenShift Container Platform CLI. 
  2. Create the YAML file for the `ServiceMeshMember` manifest. The manifest adds the `my-application` project to the service mesh that was created by the `ServiceMeshControlPlane` resource deployed in the `istio-system` namespace: 

```yaml
apiVersion: maistra.io/v1
kind: ServiceMeshMember
metadata:
  name: default
  namespace: my-application
spec:
  controlPlaneRef:
    namespace: istio-system
    name: basic
```


  3. Apply the YAML file to create the `ServiceMeshMember` resource: 

```shell-session
$ oc apply -f <file-name>
```


**Verification**

  * Verify that the namespace is part of the mesh by running the following command. Confirm the that the value `True` appears in the `READY` column. 

```shell-session
$ oc get smm default -n my-application
```


**Example output**

```shell-session
NAME      CONTROL PLANE        READY   AGE
default   istio-system/basic   True    2m11s
```


  * Alternatively, view the `ServiceMeshMemberRoll` resource to confirm that the `my-application` namespace is displayed in the `status.members` and `status.configuredMembers` fields of the `ServiceMeshMemberRoll` resource. 

```shell-session
$ oc describe smmr default -n istio-system
```


**Example output**

```shell-session
Name:         default
Namespace:    istio-system
Labels:       <none>
# ...
Status:
# ...
  Configured Members:
    default
    my-application
# ...
  Members:
    default
    my-application
```


## 2.10.5. About adding projects using label selectors

For cluster-wide deployments, you can use label selectors to add projects to the mesh. Label selectors specified in the `ServiceMeshMemberRoll` resource enable the Service Mesh Operator to add or remove namespaces to or from the mesh based on namespace labels. Unlike other standard OpenShift Container Platform resources that you can use to specify a single label selector, you can use the `ServiceMeshMemberRoll` resource to specify multiple label selectors. 

![Adding project using label selector image](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/a1b754791ccb959357dc771433bf146c/ossm-adding-project-using-label-selector.png) ![Adding project using label selector image](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/a1b754791ccb959357dc771433bf146c/ossm-adding-project-using-label-selector.png)

If the labels for a namespace match any of the selectors specified in the `ServiceMeshMemberRoll` resource, then the namespace is included in the mesh. 

Note

In OpenShift Container Platform, a project is essentially a Kubernetes namespace with additional annotations, such as the range of user IDs that can be used in the project. Typically, the OpenShift Container Platform web console uses the term _project_ , and the CLI uses the term _namespace_ , but the terms are essentially synonymous. 

### 2.10.5.1. Adding a project to the mesh using label selectors with the web console

You can use labels selectors to add a project to the Service Mesh with the OpenShift Container Platform web console. 

**Prerequisites**

  * You have installed the Red Hat OpenShift Service Mesh Operator. 
  * The deployment has an existing `ServiceMeshMemberRoll` resource. 
  * You are logged in to the OpenShift Container Platform web console as `cluster-admin`. 



**Procedure**

  1. Navigate to **Ecosystem** **Installed Operators**. 
  2. Click the **Project** menu, and from the drop-down list, select the project where your `ServiceMeshMemberRoll` resource is deployed. For example, **istio-system**. 
  3. Click the Red Hat OpenShift Service Mesh Operator. 
  4. Click the **Istio Service Mesh Member Roll** tab. 
  5. Click **Create ServiceMeshMember Roll**. 
  6. Accept the default name for the `ServiceMeshMemberRoll`. 
  7. In the **Labels** field, enter key-value pairs to define the labels that identify which namespaces to include in the service mesh. If a project namespace has either label specified by the selectors, then the project namespace is included in the service mesh. You do not need to include both labels. 

For example, entering `mykey=myvalue` includes all namespaces with this label as part of the mesh. When the selector identifies a match, the project namespace is added to the service mesh. 

Entering `myotherkey=myothervalue` includes all namespaces with this label as part of the mesh. When the selector identifies a match, the project namespace is added to the service mesh. 

  8. Click **Create**. 



### 2.10.5.2. Adding a project to the mesh using label selectors with the CLI

You can use label selectors to add a project to the Service Mesh with the CLI. 

**Prerequisites**

  * You have installed the Red Hat OpenShift Service Mesh Operator. 
  * The deployment has an existing `ServiceMeshMemberRoll` resource. 
  * You are logged in to OpenShift Container Platform as`cluster-admin`. 



**Procedure**

  1. Log in to the OpenShift Container Platform CLI. 
  2. Edit the `ServiceMeshMemberRoll` resource. 

```shell-session
$ oc edit smmr default -n istio-system
```


You can deploy the Service Mesh control plane to any project provided that it is separate from the project that contains your services. 

  3. Modify the YAML file to include namespace label selectors in the `spec.memberSelectors` field of the `ServiceMeshMemberRoll` resource. 

Note

Instead of using the `matchLabels` field, you can also use the `matchExpressions` field in the selector. 

```yaml
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
  namespace: istio-system
spec:
  memberSelectors: 
```


1

```yaml
  - matchLabels: 
```


2

```yaml
      mykey: myvalue 
```


3

```yaml
  - matchLabels: 
```


4

```yaml
      myotherkey: myothervalue 
```


5

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO20-1)
    

Contains the label selectors used to identify which project namespaces are included in the service mesh. If a project namespace has either label specified by the selectors, then the project namespace is included in the service mesh. The project namespace does not need both labels to be included. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO20-2) [3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO20-3)
    

Specifies all namespaces with the `mykey=myvalue` label. When the selector identifies a match, the project namespace is added to the service mesh. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO20-4) [5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO20-5)
    

Specifies all namespaces with the `myotherkey=myothervalue` label. When the selector identifies a match, the project namespace is added to the service mesh. 




## 2.10.6. Bookinfo example application

The Bookinfo example application allows you to test your Red Hat OpenShift Service Mesh 2.6.11 installation on OpenShift Container Platform. 

The Bookinfo application displays information about a book, similar to a single catalog entry of an online book store. The application displays a page that describes the book, book details (ISBN, number of pages, and other information), and book reviews. 

The Bookinfo application consists of these microservices: 

  * The `productpage` microservice calls the `details` and `reviews` microservices to populate the page. 
  * The `details` microservice contains book information. 
  * The `reviews` microservice contains book reviews. It also calls the `ratings` microservice. 
  * The `ratings` microservice contains book ranking information that accompanies a book review. 



There are three versions of the reviews microservice: 

  * Version v1 does not call the `ratings` Service. 
  * Version v2 calls the `ratings` Service and displays each rating as one to five black stars. 
  * Version v3 calls the `ratings` Service and displays each rating as one to five red stars. 



### 2.10.6.1. Installing the Bookinfo application

This tutorial walks you through how to create a sample application by creating a project, deploying the Bookinfo application to that project, and viewing the running application in Service Mesh. 

**Prerequisites**

  * OpenShift Container Platform 4.1 or higher installed. 
  * Red Hat OpenShift Service Mesh 2.6.11 installed. 
  * Access to the OpenShift CLI (`oc`). 
  * You are logged in to OpenShift Container Platform as`cluster-admin`. 



Note

The Bookinfo sample application cannot be installed on IBM Z® and IBM Power®. 

Note

The commands in this section assume the Service Mesh control plane project is `istio-system`. If you installed the control plane in another namespace, edit each command before you run it. 

**Procedure**

  1. Click **Home** **Projects**. 
  2. Click **Create Project**. 
  3. Enter `bookinfo` as the **Project Name** , enter a **Display Name** , and enter a **Description** , then click **Create**. 

     * Alternatively, you can run this command from the CLI to create the `bookinfo` project. 

```shell-session
$ oc new-project bookinfo
```


  4. Click **Ecosystem** **Installed Operators**. 
  5. Click the **Project** menu and use the Service Mesh control plane namespace. In this example, use `istio-system`. 
  6. Click the **Red Hat OpenShift Service Mesh** Operator. 
  7. Click the **Istio Service Mesh Member Roll** tab. 

     1. If you have already created a Istio Service Mesh Member Roll, click the name, then click the YAML tab to open the YAML editor. 
     2. If you have not created a `ServiceMeshMemberRoll`, click **Create ServiceMeshMemberRoll**. 

  8. Click **Members** , then enter the name of your project in the **Value** field. 
  9. Click **Create** to save the updated Service Mesh Member Roll. 

     1. Or, save the following example to a YAML file. 

**Bookinfo ServiceMeshMemberRoll example servicemeshmemberroll-default.yaml**

```yaml
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
spec:
  members:
  - bookinfo
```


     2. Run the following command to upload that file and create the `ServiceMeshMemberRoll` resource in the `istio-system` namespace. In this example, `istio-system` is the name of the Service Mesh control plane project. 

```shell-session
$ oc create -n istio-system -f servicemeshmemberroll-default.yaml
```


  10. Run the following command to verify the `ServiceMeshMemberRoll` was created successfully. 

```shell-session
$ oc get smmr -n istio-system -o wide
```


The installation has finished successfully when the `STATUS` column is `Configured`. 

```shell-session
NAME      READY   STATUS       AGE   MEMBERS
default   1/1     Configured   70s   ["bookinfo"]
```


  11. From the CLI, deploy the Bookinfo application in the _`bookinfo`_ project by applying the `bookinfo.yaml` file: 

```bash
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-2.6/samples/bookinfo/platform/kube/bookinfo.yaml
```


You should see output similar to the following: 

```shell-session
service/details created
serviceaccount/bookinfo-details created
deployment.apps/details-v1 created
service/ratings created
serviceaccount/bookinfo-ratings created
deployment.apps/ratings-v1 created
service/reviews created
serviceaccount/bookinfo-reviews created
deployment.apps/reviews-v1 created
deployment.apps/reviews-v2 created
deployment.apps/reviews-v3 created
service/productpage created
serviceaccount/bookinfo-productpage created
deployment.apps/productpage-v1 created
```


  12. Create the ingress gateway by applying the `bookinfo-gateway.yaml` file: 

```bash
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-2.6/samples/bookinfo/networking/bookinfo-gateway.yaml
```


You should see output similar to the following: 

```shell-session
gateway.networking.istio.io/bookinfo-gateway created
virtualservice.networking.istio.io/bookinfo created
```


  13. Set the value for the `GATEWAY_URL` parameter: 

```shell-session
$ export GATEWAY_URL=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.host}')
```


### 2.10.6.2. Adding default destination rules

Before you can use the Bookinfo application, you must first add default destination rules. There are two preconfigured YAML files, depending on whether or not you enabled mutual transport layer security (TLS) authentication. 

**Procedure**

  1. To add destination rules, run one of the following commands: 

     * If you did not enable mutual TLS: 

```bash
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-2.6/samples/bookinfo/networking/destination-rule-all.yaml
```


     * If you enabled mutual TLS: 

```bash
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-2.6/samples/bookinfo/networking/destination-rule-all-mtls.yaml
```


You should see output similar to the following: 

```shell-session
destinationrule.networking.istio.io/productpage created
destinationrule.networking.istio.io/reviews created
destinationrule.networking.istio.io/ratings created
destinationrule.networking.istio.io/details created
```


### 2.10.6.3. Verifying the Bookinfo installation

To confirm that the sample Bookinfo application was successfully deployed, perform the following steps. 

**Prerequisites**

  * Red Hat OpenShift Service Mesh installed. 
  * Complete the steps for installing the Bookinfo sample app. 
  * You are logged in to OpenShift Container Platform as`cluster-admin`. 



**Procedure from CLI**

  1. Verify that all pods are ready with this command: 

```shell-session
$ oc get pods -n bookinfo
```


All pods should have a status of `Running`. You should see output similar to the following: 

```shell-session
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-55b869668-jh7hb        2/2     Running   0          12m
productpage-v1-6fc77ff794-nsl8r   2/2     Running   0          12m
ratings-v1-7d7d8d8b56-55scn       2/2     Running   0          12m
reviews-v1-868597db96-bdxgq       2/2     Running   0          12m
reviews-v2-5b64f47978-cvssp       2/2     Running   0          12m
reviews-v3-6dfd49b55b-vcwpf       2/2     Running   0          12m
```


  2. Run the following command to retrieve the URL for the product page: 

```shell-session
echo "http://$GATEWAY_URL/productpage"
```


  3. Copy and paste the output in a web browser to verify the Bookinfo product page is deployed. 



**Procedure from Kiali web console**

  1. Obtain the address for the Kiali web console. 

     1. Log in to the OpenShift Container Platform web console. 
     2. Navigate to **Networking** **Routes**. 
     3. On the **Routes** page, select the Service Mesh control plane project, for example `istio-system`, from the **Namespace** menu. 

The **Location** column displays the linked address for each route. 

     4. Click the link in the **Location** column for Kiali. 
     5. Click **Log In With OpenShift**. The Kiali **Overview** screen presents tiles for each project namespace. 

  2. In Kiali, click **Graph**. 
  3. Select bookinfo from the **Namespace** list, and App graph from the **Graph Type** list. 
  4. Click **Display idle nodes** from the **Display** menu. 

This displays nodes that are defined but have not received or sent requests. It can confirm that an application is properly defined, but that no request traffic has been reported. 

![Kiali displaying bookinfo application](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/3b5cf079c8338b3554382168075fffb3/ossm-kiali-graph-bookinfo.png) ![Kiali displaying bookinfo application](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/3b5cf079c8338b3554382168075fffb3/ossm-kiali-graph-bookinfo.png)

     * Use the **Duration** menu to increase the time period to help ensure older traffic is captured. 
     * Use the **Refresh Rate** menu to refresh traffic more or less often, or not at all. 

  5. Click **Services** , **Workloads** or **Istio Config** to see list views of bookinfo components, and confirm that they are healthy. 



### 2.10.6.4. Removing the Bookinfo application

Follow these steps to remove the Bookinfo application. 

**Prerequisites**

  * OpenShift Container Platform 4.1 or higher installed. 
  * Red Hat OpenShift Service Mesh 2.6.11 installed. 
  * Access to the OpenShift CLI (`oc`). 



#### 2.10.6.4.1. Delete the Bookinfo project

**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Click to **Home** **Projects**. 
  3. Click the `bookinfo` menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) , and then click **Delete Project**. 
  4. Type `bookinfo` in the confirmation dialog box, and then click **Delete**. 

     * Alternatively, you can run this command using the CLI to create the `bookinfo` project. 

```shell-session
$ oc delete project bookinfo
```


#### 2.10.6.4.2. Remove the Bookinfo project from the Service Mesh member roll

**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Click **Ecosystem** **Installed Operators**. 
  3. Click the **Project** menu and choose `istio-system` from the list. 
  4. Click the **Istio Service Mesh Member Roll** link under **Provided APIS** for the **Red Hat OpenShift Service Mesh** Operator. 
  5. Click the `ServiceMeshMemberRoll` menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) and select **Edit Service Mesh Member Roll**. 
  6. Edit the default Service Mesh Member Roll YAML and remove `bookinfo` from the **members** list. 

     * Alternatively, you can run this command using the CLI to remove the `bookinfo` project from the `ServiceMeshMemberRoll`. In this example, `istio-system` is the name of the Service Mesh control plane project. 

```shell-session
$ oc -n istio-system patch --type='json' smmr default -p '[{"op": "remove", "path": "/spec/members", "value":["'"bookinfo"'"]}]'
```


  7. Click **Save** to update Service Mesh Member Roll. 



## 2.10.7. Next steps

  * To continue the installation process, you must [enable sidecar injection](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#deploying-applications-ossm "2.11. Enabling sidecar injection").
