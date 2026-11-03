# 2.25. Troubleshooting your service mesh

This section describes how to identify and resolve common problems in Red Hat OpenShift Service Mesh. Use the following sections to help troubleshoot and debug problems when deploying Red Hat OpenShift Service Mesh on OpenShift Container Platform. 

## 2.25.1. Understanding Service Mesh versions

In order to understand what version of Red Hat OpenShift Service Mesh you have deployed on your system, you need to understand how each of the component versions is managed. 

  * **Operator** version - The most current Operator version is 2.6.11. The Operator version number only indicates the version of the currently installed Operator. Because the Red Hat OpenShift Service Mesh Operator supports multiple versions of the Service Mesh control plane, the version of the Operator does not determine the version of your deployed `ServiceMeshControlPlane` resources. 

Important

Upgrading to the latest Operator version automatically applies patch updates, but does not automatically upgrade your Service Mesh control plane to the latest minor version. 

  * **ServiceMeshControlPlane** version - The `ServiceMeshControlPlane` version determines what version of Red Hat OpenShift Service Mesh you are using. The value of the `spec.version` field in the `ServiceMeshControlPlane` resource controls the architecture and configuration settings that are used to install and deploy Red Hat OpenShift Service Mesh. When you create the Service Mesh control plane you can set the version in one of two ways: 

    * To configure in the Form View, select the version from the **Control Plane Version** menu. 
    * To configure in the YAML View, set the value for `spec.version` in the YAML file. 




Operator Lifecycle Manager (OLM) does not manage Service Mesh control plane upgrades, so the version number for your Operator and `ServiceMeshControlPlane` (SMCP) may not match, unless you have manually upgraded your SMCP. 

## 2.25.2. Troubleshooting Operator installation

In addition to the information in this section, be sure to review the following topics: 

  * [What are Operators?](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#what-are-operators?)
  * [Operator Lifecycle Management concepts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#concepts-and-resources). 
  * [OpenShift Operator troubleshooting section](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#troubleshooting-operator-issues-1). 
  * [OpenShift installation troubleshooting section](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#troubleshooting-installations-1). 



### 2.25.2.1. Validating Operator installation

When you install the Red Hat OpenShift Service Mesh Operators, OpenShift automatically creates the following objects as part of a successful Operator installation: 

  * config maps 
  * custom resource definitions 
  * deployments 
  * pods 
  * replica sets 
  * roles 
  * role bindings 
  * secrets 
  * service accounts 
  * services 



**From the OpenShift Container Platform console**

You can verify that the Operator pods are available and running by using the OpenShift Container Platform console. 

  1. Navigate to **Workloads** **Pods**. 
  2. Select the `openshift-operators` namespace. 
  3. Verify that the following pods exist and have a status of `running`: 

     * `istio-operator`
     * `jaeger-operator`
     * `kiali-operator`

  4. Select the `openshift-operators-redhat` namespace. 
  5. Verify that the `elasticsearch-operator` pod exists and has a status of `running`. 



**From the command line**

  1. Verify the Operator pods are available and running in the `openshift-operators` namespace with the following command: 

```shell-session
$ oc get pods -n openshift-operators
```


**Example output**

```shell-session
NAME                               READY   STATUS    RESTARTS   AGE
istio-operator-bb49787db-zgr87     1/1     Running   0          15s
jaeger-operator-7d5c4f57d8-9xphf   1/1     Running   0          2m42s
kiali-operator-f9c8d84f4-7xh2v     1/1     Running   0          64s
```


  2. Verify the Elasticsearch operator with the following command: 

```shell-session
$ oc get pods -n openshift-operators-redhat
```


**Example output**

```shell-session
NAME                                      READY   STATUS    RESTARTS   AGE
elasticsearch-operator-d4f59b968-796vq     1/1     Running   0          15s
```


### 2.25.2.2. Troubleshooting service mesh Operators

If you experience Operator issues: 

  * Verify your Operator subscription status. 
  * Verify that you did not install a community version of the Operator, instead of the supported Red Hat version. 
  * Verify that you have the `cluster-admin` role to install Red Hat OpenShift Service Mesh. 
  * Check for any errors in the Operator pod logs if the issue is related to installation of Operators. 



Note

You can install Operators only through the OpenShift console, the software catalog is not accessible from the command line. 

#### 2.25.2.2.1. Viewing Operator pod logs

You can view Operator logs by using the `oc logs` command. Red Hat may request logs to help resolve support cases. 

**Procedure**

  * To view Operator pod logs, enter the command: 

```shell-session
$ oc logs -n openshift-operators <podName>
```


For example, 

```shell-session
$ oc logs -n openshift-operators istio-operator-bb49787db-zgr87
```


## 2.25.3. Troubleshooting the control plane

The Service Mesh _control plane_ is composed of Istiod, which consolidates several previous control plane components (Citadel, Galley, Pilot) into a single binary. Deploying the `ServiceMeshControlPlane` also creates the other components that make up Red Hat OpenShift Service Mesh as described in the [architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-architecture_ossm-architecture "2.4.2. Service Mesh architecture") topic. 

### 2.25.3.1. Validating the Service Mesh control plane installation

When you create the Service Mesh control plane, the Service Mesh Operator uses the parameters that you have specified in the `ServiceMeshControlPlane` resource file to do the following: 

  * Creates the Istio components and deploys the following pods: 

    * `istiod`
    * `istio-ingressgateway`
    * `istio-egressgateway`
    * `grafana`
    * `prometheus`

  * Calls the Kiali Operator to create Kaili deployment based on configuration in either the SMCP or the Kiali custom resource. 

Note

You view the Kiali components under the Kiali Operator, not the Service Mesh Operator. 

  * Calls the Red Hat OpenShift Distributed Tracing Platform (Jaeger) Operator to create Distributed Tracing Platform (Jaeger) components based on configuration in either the SMCP or the Jaeger custom resource. 

Note

You view the Jaeger components under the Red Hat OpenShift Distributed Tracing Platform (Jaeger) Operator and the Elasticsearch components under the Red Hat Elasticsearch Operator, not the Service Mesh Operator. 

**From the OpenShift Container Platform console**

You can verify the Service Mesh control plane installation in the OpenShift Container Platform web console. 

    1. Navigate to **Ecosystem** **Installed Operators**. 
    2. Select the `istio-system` namespace. 
    3. Select the Red Hat OpenShift Service Mesh Operator. 

       1. Click the **Istio Service Mesh Control Plane** tab. 
       2. Click the name of your control plane, for example `basic`. 
       3. To view the resources created by the deployment, click the **Resources** tab. You can use the filter to narrow your view, for example, to check that all the **Pods** have a status of `running`. 
       4. If the SMCP status indicates any problems, check the `status:` output in the YAML file for more information. 

    4. Navigate back to **Ecosystem** **Installed Operators**. 
    5. Select the OpenShift Elasticsearch Operator. 

       1. Click the **Elasticsearch** tab. 
       2. Click the name of the deployment, for example `elasticsearch`. 
       3. To view the resources created by the deployment, click the **Resources** tab. . 
       4. If the `Status` column any problems, check the `status:` output on the **YAML** tab for more information. 

    6. Navigate back to **Ecosystem** **Installed Operators**. 
    7. Select the Red Hat OpenShift Distributed Tracing Platform (Jaeger) Operator. 

       1. Click the **Jaeger** tab. 
       2. Click the name of your deployment, for example `jaeger`. 
       3. To view the resources created by the deployment, click the **Resources** tab. 
       4. If the `Status` column indicates any problems, check the `status:` output on the **YAML** tab for more information. 

    8. Navigate to **Ecosystem** **Installed Operators**. 
    9. Select the Kiali Operator. 

       1. Click the **Istio Service Mesh Control Plane** tab. 
       2. Click the name of your deployment, for example `kiali`. 
       3. To view the resources created by the deployment, click the **Resources** tab. 
       4. If the `Status` column any problems, check the `status:` output on the **YAML** tab for more information. 




**From the command line**

  1. Run the following command to see if the Service Mesh control plane pods are available and running, where `istio-system` is the namespace where you installed the SMCP. 

```shell-session
$ oc get pods -n istio-system
```


**Example output**

```shell-session
NAME                                   READY   STATUS    RESTARTS   AGE
grafana-6776785cfc-6fz7t               2/2     Running   0          102s
istio-egressgateway-5f49dd99-l9ppq     1/1     Running   0          103s
istio-ingressgateway-6dc885c48-jjd8r   1/1     Running   0          103s
istiod-basic-6c9cc55998-wg4zq          1/1     Running   0          2m14s
jaeger-6865d5d8bf-zrfss                2/2     Running   0          100s
kiali-579799fbb7-8mwc8                 1/1     Running   0          46s
prometheus-5c579dfb-6qhjk              2/2     Running   0          115s
```


  2. Check the status of the Service Mesh control plane deployment by using the following command. Replace `istio-system` with the namespace where you deployed the SMCP. 

```shell-session
$ oc get smcp -n istio-system
```


The installation has finished successfully when the STATUS column is `ComponentsReady`. 

**Example output**

```shell-session
NAME    READY   STATUS            PROFILES      VERSION   AGE
basic   10/10   ComponentsReady   ["default"]   2.1.3     4m2s
```


If you have modified and redeployed your Service Mesh control plane, the status should read `UpdateSuccessful`. 

**Example output**

```shell-session
NAME            READY     STATUS             TEMPLATE   VERSION   AGE
basic-install   10/10     UpdateSuccessful   default     v1.1     3d16h
```


  3. If the SMCP status indicates anything other than `ComponentsReady` check the `status:` output in the SCMP resource for more information. 

```shell-session
$ oc describe smcp <smcp-name> -n <controlplane-namespace>
```


**Example output**

```shell-session
$ oc describe smcp basic -n istio-system
```


  4. Check the status of the Jaeger deployment with the following command, where `istio-system` is the namespace where you deployed the SMCP. 

```shell-session
$ oc get jaeger -n istio-system
```


**Example output**

```shell-session
NAME     STATUS    VERSION   STRATEGY   STORAGE   AGE
jaeger   Running   1.30.0    allinone   memory    15m
```


  5. Check the status of the Kiali deployment with the following command, where `istio-system` is the namespace where you deployed the SMCP. 

```shell-session
$ oc get kiali -n istio-system
```


**Example output**

```shell-session
NAME    AGE
kiali   15m
```


#### 2.25.3.1.1. Accessing the Kiali console

You can view your application’s topology, health, and metrics in the Kiali console. If your service is experiencing problems, the Kiali console lets you view the data flow through your service. You can view insights about the mesh components at different levels, including abstract applications, services, and workloads. Kiali also provides an interactive graph view of your namespace in real time. 

To access the Kiali console you must have Red Hat OpenShift Service Mesh installed, Kiali installed and configured. 

The installation process creates a route to access the Kiali console. 

If you know the URL for the Kiali console, you can access it directly. If you do not know the URL, use the following directions. 

**Procedure for administrators**

  1. Log in to the OpenShift Container Platform web console with an administrator role. 
  2. Click **Home** **Projects**. 
  3. On the **Projects** page, if necessary, use the filter to find the name of your project. 
  4. Click the name of your project, for example, `bookinfo`. 
  5. On the **Project details** page, in the **Launcher** section, click the **Kiali** link. 
  6. Log in to the Kiali console with the same user name and password that you use to access the OpenShift Container Platform console. 

When you first log in to the Kiali Console, you see the **Overview** page which displays all the namespaces in your service mesh that you have permission to view. 

If you are validating the console installation and namespaces have not yet been added to the mesh, there might not be any data to display other than `istio-system`. 




**Procedure for developers**

  1. Log in to the OpenShift Container Platform web console with a developer role. 
  2. Click **Project**. 
  3. On the **Project Details** page, if necessary, use the filter to find the name of your project. 
  4. Click the name of your project, for example, `bookinfo`. 
  5. On the **Project** page, in the **Launcher** section, click the **Kiali** link. 
  6. Click **Log In With OpenShift**. 



#### 2.25.3.1.2. Accessing the Jaeger console

To access the Jaeger console you must have Red Hat OpenShift Service Mesh installed, Red Hat OpenShift Distributed Tracing Platform (Jaeger) installed and configured. 

The installation process creates a route to access the Jaeger console. 

If you know the URL for the Jaeger console, you can access it directly. If you do not know the URL, use the following directions. 

Important

Starting with Red Hat OpenShift Service Mesh 2.5, Red Hat OpenShift Distributed Tracing Platform (Jaeger) and OpenShift Elasticsearch Operator have been deprecated and will be removed in a future release. Red Hat will provide bug fixes and support for this feature during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to Red Hat OpenShift Distributed Tracing Platform (Jaeger), you can use Red Hat OpenShift Distributed Tracing Platform instead. 

**Procedure from OpenShift console**

  1. Log in to the OpenShift Container Platform web console as a user with cluster-admin rights. If you use Red Hat OpenShift Dedicated, you must have an account with the `dedicated-admin` role. 
  2. Navigate to **Networking** **Routes**. 
  3. On the **Routes** page, select the Service Mesh control plane project, for example `istio-system`, from the **Namespace** menu. 

The **Location** column displays the linked address for each route. 

  4. If necessary, use the filter to find the `jaeger` route. Click the route **Location** to launch the console. 
  5. Click **Log In With OpenShift**. 



**Procedure from Kiali console**

  1. Launch the Kiali console. 
  2. Click **Distributed Tracing** in the left navigation pane. 
  3. Click **Log In With OpenShift**. 



**Procedure from the CLI**

  1. Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. If you use Red Hat OpenShift Dedicated, you must have an account with the `dedicated-admin` role. 

```shell-session
$ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
```


  2. To query for details of the route using the command line, enter the following command. In this example, `istio-system` is the Service Mesh control plane namespace. 

```shell-session
$ oc get route -n istio-system jaeger -o jsonpath='{.spec.host}'
```


  3. Launch a browser and navigate to `https://<JAEGER_URL>`, where `<JAEGER_URL>` is the route that you discovered in the previous step. 
  4. Log in using the same user name and password that you use to access the OpenShift Container Platform console. 
  5. If you have added services to the service mesh and have generated traces, you can use the filters and **Find Traces** button to search your trace data. 

If you are validating the console installation, there is no trace data to display. 




### 2.25.3.2. Troubleshooting the Service Mesh control plane

If you are experiencing issues while deploying the Service Mesh control plane, 

  * Ensure that the `ServiceMeshControlPlane` resource is installed in a project that is separate from your services and Operators. This documentation uses the `istio-system` project as an example, but you can deploy your control plane in any project as long as it is separate from the project that contains your Operators and services. 
  * Ensure that the `ServiceMeshControlPlane` and `Jaeger` custom resources are deployed in the same project. For example, use the `istio-system` project for both. 



## 2.25.4. Troubleshooting the data plane

The _data plane_ is a set of intelligent proxies that intercept and control all inbound and outbound network communications between services in the service mesh. 

Red Hat OpenShift Service Mesh relies on a proxy sidecar within the application’s pod to provide service mesh capabilities to the application. 

### 2.25.4.1. Troubleshooting sidecar injection

Red Hat OpenShift Service Mesh does not automatically inject proxy sidecars to pods. You must opt in to sidecar injection. 

#### 2.25.4.1.1. Troubleshooting Istio sidecar injection

Check to see if automatic injection is enabled in the Deployment for your application. If automatic injection for the Envoy proxy is enabled, there should be a `sidecar.istio.io/inject:"true"` annotation in the `Deployment` resource under `spec.template.metadata.annotations`. 

#### 2.25.4.1.2. Troubleshooting Jaeger agent sidecar injection

Check to see if automatic injection is enabled in the Deployment for your application. If automatic injection for the Jaeger agent is enabled, there should be a `sidecar.jaegertracing.io/inject:"true"` annotation in the `Deployment` resource. 

For more information about sidecar injection, see [Enabling automatic injection](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-automatic-sidecar-injection_deploying-applications-ossm "2.11.2. Enabling automatic sidecar injection")
