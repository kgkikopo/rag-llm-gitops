# 2.8. Installing the Operators

To install Red Hat OpenShift Service Mesh, first install the Red Hat OpenShift Service Mesh Operator and any optional Operators on OpenShift Container Platform. Then create a `ServiceMeshControlPlane` resource to deploy the control plane. 

Note

This basic installation is configured based on the default OpenShift settings and is not designed for production use. Use this default installation to verify your installation, and then configure your service mesh for your specific environment. 

**Prerequisites**

  * Read the [Preparing to install Red Hat OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#preparing-ossm-installation "2.7. Preparing to install Service Mesh") process. 
  * An account with the `cluster-admin` role. If you use Red Hat OpenShift Dedicated, you must have an account with the `dedicated-admin` role. 



The following steps show how to install a basic instance of Red Hat OpenShift Service Mesh on OpenShift Container Platform. 

Important

Starting with Red Hat OpenShift Service Mesh 2.5, Red Hat OpenShift Distributed Tracing Platform (Jaeger) and OpenShift Elasticsearch Operator are deprecated and will be removed in a future release. Red Hat will provide bug fixes and support for these features during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to Red Hat OpenShift Distributed Tracing Platform (Jaeger), you can use Red Hat OpenShift Distributed Tracing Platform instead. 

## 2.8.1. Service Mesh Operators overview

Red Hat OpenShift Service Mesh requires the use of the Red Hat OpenShift Service Mesh Operator which allows you to connect, secure, control, and observe the microservices that comprise your applications. You can also install other Operators to enhance your service mesh experience. 

Warning

Do not install Community versions of the Operators. Community Operators are not supported. 

The following Operator is required: 

Red Hat OpenShift Service Mesh Operator
     Allows you to connect, secure, control, and observe the microservices that comprise your applications. It also defines and monitors the `ServiceMeshControlPlane` resources that manage the deployment, updating, and deletion of the Service Mesh components. It is based on the open source [Istio](https://istio.io/) project. 

The following Operators are optional: 

Kiali Operator provided by Red Hat
     Provides observability for your service mesh. You can view configurations, monitor traffic, and analyze traces in a single console. It is based on the open source [Kiali](https://www.kiali.io/) project. 
Red Hat OpenShift Distributed Tracing Platform
     Provides distributed tracing to monitor and troubleshoot transactions in complex distributed systems. It is based on the open source [Grafana Tempo](https://grafana.com/oss/tempo/) project. 

The following optional Operators are deprecated: 

Important

Starting with Red Hat OpenShift Service Mesh 2.5, Red Hat OpenShift Distributed Tracing Platform (Jaeger) and OpenShift Elasticsearch Operator are deprecated and will be removed in a future release. Red Hat will provide bug fixes and support for these features during the current release lifecycle, but these features will no longer receive enhancements and will be removed. As an alternative to Red Hat OpenShift Distributed Tracing Platform (Jaeger), you can use Red Hat OpenShift Distributed Tracing Platform instead. 

Red Hat OpenShift Distributed Tracing Platform (Jaeger)
     Provides distributed tracing to monitor and troubleshoot transactions in complex distributed systems. It is based on the open source [Jaeger](https://www.jaegertracing.io/) project. 
OpenShift Elasticsearch Operator
     Provides database storage for tracing and logging with the Distributed Tracing Platform (Jaeger). It is based on the open source [Elasticsearch](https://www.elastic.co/) project. 

## 2.8.2. Installing the Operators

To install Red Hat OpenShift Service Mesh, you must install the Red Hat OpenShift Service Mesh Operator. Repeat the procedure for each additional Operator you want to install. 

Additional Operators include: 

  * Kiali Operator provided by Red Hat 
  * Tempo Operator 



Deprecated additional Operators include: 

Important

Starting with Red Hat OpenShift Service Mesh 2.5, Red Hat OpenShift Distributed Tracing Platform (Jaeger) and OpenShift Elasticsearch Operator are deprecated and will be removed in a future release. Red Hat will provide bug fixes and support for these features during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to Red Hat OpenShift Distributed Tracing Platform (Jaeger), you can use Red Hat OpenShift Distributed Tracing Platform instead. 

  * Red Hat OpenShift Distributed Tracing Platform (Jaeger) 
  * OpenShift Elasticsearch Operator 



Note

If you have already installed the OpenShift Elasticsearch Operator as part of OpenShift Logging, you do not need to install the OpenShift Elasticsearch Operator again. The Red Hat OpenShift Distributed Tracing Platform (Jaeger) Operator creates the Elasticsearch instance using the installed OpenShift Elasticsearch Operator. 

**Procedure**

  1. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role. 
  2. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
  3. Type the name of the Operator into the filter box and select the Red Hat version of the Operator. Community versions of the Operators are not supported. 
  4. Click **Install**. 
  5. On the **Install Operator** page for each Operator, accept the default settings. 
  6. Click **Install**. Wait until the Operator installs before repeating the steps for the next Operator you want to install. 

     * The Red Hat OpenShift Service Mesh Operator installs in the `openshift-operators` namespace and is available for all namespaces in the cluster. 
     * The Kiali Operator provided by Red Hat installs in the `openshift-operators` namespace and is available for all namespaces in the cluster. 
     * The Tempo Operator installs in the `openshift-tempo-operator` namespace and is available for all namespaces in the cluster. 
     * The Red Hat OpenShift Distributed Tracing Platform (Jaeger) installs in the `openshift-distributed-tracing` namespace and is available for all namespaces in the cluster. 

Important

Starting with Red Hat OpenShift Service Mesh 2.5, Red Hat OpenShift Distributed Tracing Platform (Jaeger) is deprecated and will be removed in a future release. Red Hat will provide bug fixes and support for this feature during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to Red Hat OpenShift Distributed Tracing Platform (Jaeger), you can use Red Hat OpenShift Distributed Tracing Platform instead. 

     * The OpenShift Elasticsearch Operator installs in the `openshift-operators-redhat` namespace and is available for all namespaces in the cluster. 

Important

Starting with Red Hat OpenShift Service Mesh 2.5, OpenShift Elasticsearch Operator is deprecated and will be removed in a future release. Red Hat will provide bug fixes and support for this feature during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. 




**Verification**

  * After all you have installed all four Operators, click **Ecosystem** **Installed Operators** to verify that your Operators are installed. 



## 2.8.3. Configuring the Service Mesh Operator to run on infrastructure nodes

This task should only be performed if the Service Mesh Operator runs on an infrastructure node. 

If the operator will run on a worker node, skip this task. 

**Prerequisites**

  * The Service Mesh Operator must be installed. 
  * One of the nodes comprising the deployment must be an infrastructure node. For more information, see "Creating infrastructure machine sets." 



**Procedure**

  1. List the operators installed in the namespace: 

```shell-session
$ oc -n openshift-operators get subscriptions
```


  2. Edit the Service Mesh Operator `Subscription` resource to specify where the operator should run: 

```shell-session
$ oc -n openshift-operators edit subscription <name> 
```


1

```shell-session

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO10-1)
    

`<name>` represents the name of the `Subscription` resource. The default name of the `Subscription` resource is `servicemeshoperator`. 

  3. Add the `nodeSelector` and `tolerations` to `spec.config` in the `Subscription` resource: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/servicemeshoperator.openshift-operators: ""
  name: servicemeshoperator
  namespace: openshift-operators
# ...
spec:
  config:
    nodeSelector: 
```


1

```yaml
      node-role.kubernetes.io/infra: ""
    tolerations: 
```


2

```yaml
    - effect: NoSchedule
      key: node-role.kubernetes.io/infra
      value: reserved
    - effect: NoExecute
      key: node-role.kubernetes.io/infra
      value: reserved
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO11-1)
    

Ensures that the operator pod is only scheduled on an infrastructure node. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO11-2)
    

Ensures that the pod is accepted by the infrastructure node. 




## 2.8.4. Verifying the Service Mesh Operator is running on infrastructure node

**Procedure**

  * Verify that the node associated with the Operator pod is an infrastructure node: 

```shell-session
$ oc -n openshift-operators get po -l name=istio-operator -owide
```


## 2.8.5. Next steps

  * The Red Hat OpenShift Service Mesh Operator does not create the Service Mesh custom resource definitions (CRDs) until you deploy a Service Mesh control plane. You can use the `ServiceMeshControlPlane` resource to install and configure the Service Mesh components. For more information, see [Creating the ServiceMeshControlPlane](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-create-smcp "2.9. Creating the ServiceMeshControlPlane").
