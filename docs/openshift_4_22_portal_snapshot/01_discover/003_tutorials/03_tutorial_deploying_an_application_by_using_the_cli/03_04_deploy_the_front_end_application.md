# 3.4. Deploy the front-end application

Deploy the front-end application that provides the external-facing web component for the tutorial. 

The simplest way to deploy an application in OpenShift Container Platform is to run a provided container image. 

The following procedure deploys `parksmap`, which is the front-end component of the `national-parks-app` application. The web application displays an interactive map of the locations of national parks across the world. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Deploy the `parksmap` application by running the following command: 

```shell-session
$ oc new-app quay.io/openshiftroadshow/parksmap:latest --name=parksmap -l 'app=national-parks-app,component=parksmap,role=frontend,app.kubernetes.io/part-of=national-parks-app'
```


**Example output**

```plaintext
--> Found container image 0c2f55f (4 years old) from quay.io for "quay.io/openshiftroadshow/parksmap:latest"

    * An image stream tag will be created as "parksmap:latest" that will track this image

--> Creating resources with label app=national-parks-app,app.kubernetes.io/part-of=national-parks-app,component=parksmap,role=frontend ...
    imagestream.image.openshift.io "parksmap" created
    deployment.apps "parksmap" created
    service "parksmap" created
--> Success
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose service/parksmap'
    Run 'oc status' to view your app.
```


**Additional resources**

  * [oc new-app](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-new-app)



## 3.4.1. Expose the front-end service

By default, services running on OpenShift Container Platform are not accessible externally. To expose your service so that external clients can access it, you can create a _route_. 

A `Route` object is a OpenShift Container Platform networking resource similar to a Kubernetes `Ingress` object. The default OpenShift Container Platform router (HAProxy) uses the HTTP header of the incoming request to determine where to proxy the connection. 

Optionally, you can define security, such as TLS, for the route. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 
  * You have `cluster-admin` or project-level `admin` privileges. 



**Procedure**

  * Create a route to expose the `parksmap` front-end application by running the following command: 

```shell-session
$ oc create route edge parksmap --service=parksmap
```


**Verification**

  * Verify that the application route was successfully created by running the following command: 

```shell-session
$ oc get route parksmap
```


**Example output**

```shell-session
NAME        HOST/PORT                                                   PATH   SERVICES   PORT       TERMINATION   WILDCARD
parksmap    parksmap-user-getting-started.apps.cluster.example.com             parksmap   8080-tcp   edge          None
```


**Additional resources**

  * [oc create route edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-create-route-edge)
  * [oc get](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-get)



## 3.4.2. View pod details

Retrieve detailed pod information to confirm the running status and resource configuration of the applications in this tutorial. 

OpenShift Container Platform uses the Kubernetes concept of a _pod_ , which is one or more containers deployed together on one host, and the smallest compute unit that can be defined, deployed, and managed. Pods are the rough equivalent of a machine instance, physical or virtual, to a container. 

You can view the pods in your cluster and to determine the health of those pods and the cluster as a whole. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 



**Procedure**

  * List all pods in the current project by running the following command: 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                       READY   STATUS    RESTARTS   AGE
parksmap-5f9579955-6sng8   1/1     Running   0          77s
```


  * Show details for a pod by running the following command: 

```shell-session
$ oc describe pod parksmap-5f9579955-6sng8
```


**Example output**

```shell-session
Name:             parksmap-5f9579955-6sng8
Namespace:        user-getting-started
Priority:         0
Service Account:  default
Node:             ci-ln-fr1rt92-72292-4fzf9-worker-a-g9g7c/10.0.128.4
Start Time:       Wed, 26 Mar 2025 14:03:19 -0400
Labels:           app=national-parks-app
                  app.kubernetes.io/part-of=national-parks-app
                  component=parksmap
                  deployment=parksmap
                  pod-template-hash=848bd4954b
                  role=frontend
...
```


  * View logs for a pod by running the following command: 

```shell-session
$ oc logs parksmap-5f9579955-6sng8
```


**Example output**

```shell-session
...
2025-03-26 18:03:24.774  INFO 1 --- [           main] o.s.m.s.b.SimpleBrokerMessageHandler     : Started.
2025-03-26 18:03:24.798  INFO 1 --- [           main] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat started on port(s): 8080 (http)
2025-03-26 18:03:24.801  INFO 1 --- [           main] c.o.evg.roadshow.ParksMapApplication     : Started ParksMapApplication in 4.053 seconds (JVM running for 4.46)
```


**Additional resources**

  * [oc describe](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-describe)
  * [oc get](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-get)
  * [Viewing pods](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#viewing-pods)
  * [Viewing pod logs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#viewing-pod-logs)



## 3.4.3. Scale up the deployment

Scale the application deployment up or down to meet workload demands. 

In Kubernetes, a `Deployment` object defines how an application deploys. In most cases when you deploy an application, OpenShift Container Platform creates the `Pod`, `Service`, `ReplicaSet`, and `Deployment` resources for you. 

When you deploy the `parksmap` image, a deployment resource is created. In this example, only one pod is deployed. You might want to scale up your application to keep up with user demand or to ensure that your application is always running even if one pod is down. 

The following procedure scales the `parksmap` deployment to use two instances. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 



**Procedure**

  * Scale your deployment from one pod instance to two pod instances by running the following command: 

```shell-session
$ oc scale --replicas=2 deployment/parksmap
```


**Example output**

```plaintext
deployment.apps/parksmap scaled
```


**Verification**

  * Verify that your deployment scaled up properly by running the following command: 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                       READY   STATUS    RESTARTS   AGE
parksmap-5f9579955-6sng8   1/1     Running   0          7m39s
parksmap-5f9579955-8tgft   1/1     Running   0          24s
```


Verify that two `parksmap` pods are listed. 

Tip

To scale your deployment back down to one pod instance, pass in `1` to the `--replicas` option: 

```shell-session
$ oc scale --replicas=1 deployment/parksmap
```


**Additional resources**

  * [oc scale](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-scale)
