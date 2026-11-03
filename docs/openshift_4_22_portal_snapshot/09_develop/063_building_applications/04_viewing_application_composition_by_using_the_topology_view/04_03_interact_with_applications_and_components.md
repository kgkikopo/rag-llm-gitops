# 4.3. Interact with applications and components

In the **Topology** view in the **Developer** perspective of the web console, the **Graph view** provides the following options to interact with applications and components: 

  * Click **Open URL** ( ![odc open url](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/935e20fdabb88622ee5ed9c3836b9705/odc_open_url.png) ) to see your application exposed by the route on a public URL. 
  * Click **Edit Source code** to access your source code and modify it. 

Note

This feature is available only when you create applications using the **From Git** , **From Catalog** , and the **From Dockerfile** options. 

  * Hover your cursor over the lower left icon on the pod to see the name of the latest build and its status. The status of the application build is indicated as **New** ( ![odc build new](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/b4b199ee0f13773ce40eefaa019cebf3/odc_build_new.png) ), **Pending** ( ![odc build pending](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/b936431954c3678339a48fc8a4dcbf43/odc_build_pending.png) ), **Running** ( ![odc build running](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/b53ca1c32220ad9a4f50c455ea961a37/odc_build_running.png) ), **Completed** ( ![odc build completed](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/48466535c20702ed8ae9ba111939bdba/odc_build_completed.png) ), **Failed** ( ![odc build failed](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/b5ed88e2c0962b80f4d61a983f117cbb/odc_build_failed.png) ), and **Canceled** ( ![odc build canceled](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/434ad5a70d759bd165c935cf73afd081/odc_build_canceled.png) ). 
  * The status or phase of the pod is indicated by different colors and tooltips as: 

    * **Running** ( ![odc pod running](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/2b2c12ba003e6bc0a0512693ea37305c/odc_pod_running.png) ): The pod is bound to a node and all of the containers are created. At least one container is still running or is in the process of starting or restarting. 
    * **Not Ready** ( ![odc pod not ready](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/7dc55a974c78996258961aa4929d76e0/odc_pod_not_ready.png) ): The pods which are running multiple containers, not all containers are ready. 
    * **Warning**( ![odc pod warning](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/39dd029b4f05e8fe1fdba56d311be8c1/odc_pod_warning.png) ): Containers in pods are being terminated, however termination did not succeed. Some containers may be other states. 
    * **Failed**( ![odc pod failed](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/3ebd9f8177d9f96f1e6bc8bd7cf5f253/odc_pod_failed.png) ): All containers in the pod terminated but least one container has terminated in failure. That is, the container either exited with non-zero status or was terminated by the system. 
    * **Pending**( ![odc pod pending](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/6a2fa584885ce48d7b63c0184b87976b/odc_pod_pending.png) ): The pod is accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a pod spends waiting to be scheduled as well as the time spent downloading container images over the network. 
    * **Succeeded**( ![odc pod succeeded](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/389e9d0594c695f7afaa49777906ea0c/odc_pod_succeeded.png) ): All containers in the pod terminated successfully and will not be restarted. 
    * **Terminating**( ![odc pod terminating](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/1d9e41349c68d2425f56d8246187d365/odc_pod_terminating.png) ): When a pod is being deleted, it is shown as **Terminating** by some kubectl commands. **Terminating** status is not one of the pod phases. A pod is granted a graceful termination period, which defaults to 30 seconds. 
    * **Unknown**( ![odc pod unknown](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/93008c425c214b34cb4017349920feeb/odc_pod_unknown.png) ): The state of the pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the pod should be running. 

  * After you create an application and an image is deployed, the status is shown as **Pending**. After the application is built, it is displayed as **Running**. 

**Figure 4.1. Application topology**

![odc application topology](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/7d9608cc5434de0b7d15b82b336ad2a4/odc_application_topology.png) ![odc application topology](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/7d9608cc5434de0b7d15b82b336ad2a4/odc_application_topology.png)

The application resource name is appended with indicators for the different types of resource objects as follows: 

    * **CJ** : `CronJob`
    * **D** : `Deployment`
    * **DC** : `DeploymentConfig`
    * **DS** : `DaemonSet`
    * **J** : `Job`
    * **P** : `Pod`
    * **SS** : `StatefulSet`
    * ![odc serverless app](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/6af4ad8f4cd8c13ae1e4afdcf07e473b/odc_serverless_app.png) (Knative): A serverless application 

Note

Serverless applications take some time to load and display on the **Graph view**. When you deploy a serverless application, it first creates a service resource and then a revision. After that, it is deployed and displayed on the **Graph view**. If it is the only workload, you might be redirected to the **Add** page. After the revision is deployed, the serverless application is displayed on the **Graph view**.
