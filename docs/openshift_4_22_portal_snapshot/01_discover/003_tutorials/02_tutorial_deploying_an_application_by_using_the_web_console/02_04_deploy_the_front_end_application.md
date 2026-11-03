# 2.4. Deploy the front-end application

Deploy the front-end application that provides the external-facing web component for the tutorial. 

The simplest way to deploy an application in OpenShift Container Platform is to run a provided container image. 

The following procedure deploys `parksmap`, which is the front-end component of the `national-parks-app` application. The web application displays an interactive map of the locations of national parks across the world. 

**Procedure**

  1. From the **Quick create** ( ![fa plus circle](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/c1952cc876dd671e19fa1e45646b272c/fa-plus-circle.png) ) menu in the upper right corner, click **Container images**. 
  2. Select **Image name from external registry** and enter `quay.io/openshiftroadshow/parksmap:latest`. 
  3. Scroll to the **General** section. 
  4. In the **Application name** field, enter `national-parks-app`. 
  5. In the **Name** field, ensure that the value is `parksmap`. 
  6. Scroll to the **Deploy** section. 
  7. In the **Resource type** field, ensure that **Deployment** is selected. 
  8. In the **Advanced options** section, ensure that **Create a route** is selected. 

By default, services running on OpenShift Container Platform are not accessible externally. You must select this option to create a route so that external clients can access your service. 

  9. Click the **Labels** hyperlink. 

The application code requires certain labels to be set. 

  10. Add the following labels to the text area and press Enter after each key/value pair: 

     * `app=national-parks-app`
     * `component=parksmap`
     * `role=frontend`

  11. Click **Create**. 

You are redirected to the **Topology** page where you can see the `parksmap` deployment in the `national-parks-app` application. 




**Additional resources**

  * [Viewing the topology of your application](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#odc-viewing-application-topology_viewing-application-composition-using-topology-view)



## 2.4.1. View pod details

Retrieve detailed pod information to confirm the running status and resource configuration of the applications in this tutorial. 

OpenShift Container Platform uses the Kubernetes concept of a _pod_ , which is one or more containers deployed together on one host, and the smallest compute unit that can be defined, deployed, and managed. Pods are the rough equivalent of a machine instance, physical or virtual, to a container. 

The **Overview** panel enables you to access many features of the `parksmap` deployment. The **Details** and **Resources** tabs enable you to scale application pods and check the status of builds, services, and routes. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 



**Procedure**

  1. Navigate to **Workloads** **Topology**. 
  2. Click the `parksmap` deployment in the `national-parks-app` application. 

**Figure 2.1. Parksmap deployment**

![Topology view of parksmap deployment](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/c1a486809d0bc59bd8878098bbed759c/getting-started-examine-pod.png) ![Topology view of parksmap deployment](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/c1a486809d0bc59bd8878098bbed759c/getting-started-examine-pod.png)

This opens an overview panel with the following tabs: 

     * **Details** : View details about your deployment, edit certain settings, and scale your deployment. 
     * **Resources** : View details for the pods, services, and routes associated with your deployment. 
     * **Observe** : View metrics and events for your deployment. 

  3. To view the logs for a pod, select the **Resources** tab and click **View logs** next to the `parksmap` pod. 



**Additional resources**

  * [Interacting with applications and components](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#odc-interacting-with-applications-and-components_viewing-application-composition-using-topology-view)
  * [Scaling application pods and checking builds and routes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#odc-scaling-application-pods-and-checking-builds-and-routes_viewing-application-composition-using-topology-view)
  * [Labels and annotations used for the Topology view](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#odc-labels-and-annotations-used-for-topology-view_viewing-application-composition-using-topology-view)



## 2.4.2. Scale up the application

Scale the application deployment up or down to meet workload demands. 

In Kubernetes, a `Deployment` object defines how an application deploys. In most cases when you deploy an application, OpenShift Container Platform creates the `Pod`, `Service`, `ReplicaSet`, and `Deployment` resources for you. 

When you deploy the `parksmap` image, a deployment resource is created. In this example, only one pod is deployed. You might want to scale up your application to keep up with user demand or to ensure that your application is always running even if one pod is down. 

The following procedure scales the `parksmap` deployment to use two instances. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 



**Procedure**

  1. Navigate to **Workloads** **Topology** and click the `parksmap` deployment. 
  2. Select the **Details** tab. 
  3. Use the up arrow to scale the pod to two instances. 

**Figure 2.2. Scaling application**

![Scaling pod to two instances](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/6b84da61d28fd055de31d9413e67ddd9/getting-started-scaling-pod.png) ![Scaling pod to two instances](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/6b84da61d28fd055de31d9413e67ddd9/getting-started-scaling-pod.png)

Tip

You can use the down arrow to scale your deployment back down to one pod instance. 




**Additional resources**

  * [Recommended practices for scaling the cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#recommended-scale-practices_recommended-control-plane-practices)
