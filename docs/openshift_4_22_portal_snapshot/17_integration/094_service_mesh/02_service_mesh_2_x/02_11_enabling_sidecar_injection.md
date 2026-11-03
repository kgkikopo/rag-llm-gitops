# 2.11. Enabling sidecar injection

After adding the namespaces that contain your services to your mesh, the next step is to enable automatic sidecar injection in the Deployment resource for your application. You must enable automatic sidecar injection for each deployment. 

If you have installed the Bookinfo sample application, the application was deployed and the sidecars were injected as part of the installation procedure. If you are using your own project and service, deploy your applications on OpenShift Container Platform. 

For more information, see the OpenShift Container Platform documentation, [Understanding deployments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#understanding-deployments). 

Note

Traffic started by Init Containers, specialized containers that run before the application containers in a pod, cannot travel outside of the service mesh by default. Any action Init Containers perform that requires establishing a network traffic connection outside of the mesh fails. 

For more information about connecting Init Containers to a service, see the Red Hat Knowledgebase solution [initContainer in CrashLoopBackOff on pod with Service Mesh sidecar injected](https://access.redhat.com/solutions/6653601)

## 2.11.1. Prerequisites

  * [Services deployed to the mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-tutorial-bookinfo-overview_ossm-create-mesh "2.10.6. Bookinfo example application"), for example the Bookinfo sample application. 
  * A Deployment resource file. 



## 2.11.2. Enabling automatic sidecar injection

When deploying an application, you must opt-in to injection by configuring the label `sidecar.istio.io/inject` in `spec.template.metadata.labels` to `true` in the `deployment` object. Opting in ensures that the sidecar injection does not interfere with other OpenShift Container Platform features such as builder pods used by numerous frameworks within the OpenShift Container Platform ecosystem. 

**Prerequisites**

  * Identify the namespaces that are part of your service mesh and the deployments that need automatic sidecar injection. 



**Procedure**

  1. To find your deployments use the `oc get` command. 

```shell-session
$ oc get deployment -n <namespace>
```


For example, to view the `Deployment` YAML file for the 'ratings-v1' microservice in the `bookinfo` namespace, use the following command to see the resource in YAML format. 

```shell-session
oc get deployment -n bookinfo ratings-v1 -o yaml
```


  2. Open the application’s `Deployment` YAML file in an editor. 
  3. Add `spec.template.metadata.labels.sidecar.istio/inject` to your Deployment YAML file and set `sidecar.istio.io/inject` to `true` as shown in the following example. 

**Example snippet from bookinfo deployment-ratings-v1.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ratings-v1
  namespace: bookinfo
  labels:
    app: ratings
    version: v1
spec:
  template:
    metadata:
      labels:
        sidecar.istio.io/inject: 'true'
```


Note

Using the `annotations` parameter when enabling automatic sidecar injection is deprecated and is replaced by using the `labels` parameter. 

  4. Save the `Deployment` YAML file. 
  5. Add the file back to the project that contains your app. 

```shell-session
$ oc apply -n <namespace> -f deployment.yaml
```


In this example, `bookinfo` is the name of the project that contains the `ratings-v1` app and `deployment-ratings-v1.yaml` is the file you edited. 

```shell-session
$ oc apply -n bookinfo -f deployment-ratings-v1.yaml
```


  6. To verify that the resource uploaded successfully, run the following command. 

```shell-session
$ oc get deployment -n <namespace> <deploymentName> -o yaml
```


For example, 

```shell-session
$ oc get deployment -n bookinfo ratings-v1 -o yaml
```


## 2.11.3. Validating sidecar injection

The Kiali console offers several ways to validate whether or not your applications, services, and workloads have a sidecar proxy. 

**Figure 2.3. Missing sidecar badge**

![Missing Sidecar badge](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/d25e0e0698f35e72122ae47371680a7c/ossm-node-badge-missing-sidecar.png) ![Missing Sidecar badge](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/d25e0e0698f35e72122ae47371680a7c/ossm-node-badge-missing-sidecar.png)

The **Graph** page displays a node badge indicating a **Missing Sidecar** on the following graphs: 

  * App graph 
  * Versioned app graph 
  * Workload graph 



**Figure 2.4. Missing sidecar icon**

![Missing Sidecar icon](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/64f85f0a93c61068d57eee222be0e395/ossm-icon-missing-sidecar.png) ![Missing Sidecar icon](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Service_Mesh-en-US/images/64f85f0a93c61068d57eee222be0e395/ossm-icon-missing-sidecar.png)

The **Applications** page displays a **Missing Sidecar** icon in the **Details** column for any applications in a namespace that do not have a sidecar. 

The **Workloads** page displays a **Missing Sidecar** icon in the **Details** column for any applications in a namespace that do not have a sidecar. 

The **Services** page displays a **Missing Sidecar** icon in the **Details** column for any applications in a namespace that do not have a sidecar. When there are multiple versions of a service, you use the **Service Details** page to view **Missing Sidecar** icons. 

The **Workload Details** page has a special unified **Logs** tab that lets you view and correlate application and proxy logs. You can view the Envoy logs as another way to validate sidecar injection for your application workloads. 

The **Workload Details** page also has an **Envoy** tab for any workload that is an Envoy proxy or has been injected with an Envoy proxy. This tab displays a built-in Envoy dashboard that includes subtabs for **Clusters** , **Listeners** , **Routes** , **Bootstrap** , **Config** , and **Metrics**. 

For information about enabling Envoy access logs, see the [Troubleshooting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#enabling-envoy-access-logs "2.26.1. Enabling Envoy access logs") section. 

For information about viewing Envoy logs, see [Viewing logs in the Kiali console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-viewing-logs_observability "2.17.3.2. Viewing logs in the Kiali console"). 

## 2.11.4. Setting proxy environment variables through annotations

Configuration for the Envoy sidecar proxies is managed by the `ServiceMeshControlPlane`. 

You can set environment variables for the sidecar proxy for applications by adding pod annotations to the deployment in the `injection-template.yaml` file. The environment variables are injected to the sidecar. 

**Example injection-template.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource
spec:
  replicas: 7
  selector:
    matchLabels:
      app: resource
  template:
    metadata:
      annotations:
        sidecar.maistra.io/proxyEnv: "{ \"maistra_test_env\": \"env_value\", \"maistra_test_env_2\": \"env_value_2\" }"
```


Warning

You should never include `maistra.io/` labels and annotations when creating your own custom resources. These labels and annotations indicate that the resources are generated and managed by the Operator. If you are copying content from an Operator-generated resource when creating your own resources, do not include labels or annotations that start with `maistra.io/`. Resources that include these labels or annotations will be overwritten or deleted by the Operator during the next reconciliation. 

## 2.11.5. Updating sidecar proxies

In order to update the configuration for sidecar proxies the application administrator must restart the application pods. 

If your deployment uses automatic sidecar injection, you can update the pod template in the deployment by adding or modifying an annotation. Run the following command to redeploy the pods: 

```shell-session
$ oc patch deployment/<deployment> -p '{"spec":{"template":{"metadata":{"annotations":{"kubectl.kubernetes.io/restartedAt": "'`date -Iseconds`'"}}}}}'
```


If your deployment does not use automatic sidecar injection, you must manually update the sidecars by modifying the sidecar container image specified in the deployment or pod, and then restart the pods. 

## 2.11.6. Next steps

Configure Red Hat OpenShift Service Mesh features for your environment. 

  * [Security](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-security "2.13. Security")
  * [Traffic management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-routing-traffic "2.14. Managing traffic in your service mesh")
  * [Metrics, logs, and traces](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-observability "2.17. Metrics, logs, and traces")
