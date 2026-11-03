# 4.2. Kubernetes resources

To extend and automate your Kubernetes cluster capabilities, you can use custom resources and Operators. 

A custom resource is an extension of the Kubernetes API. Operators are software extensions which manage applications and their components with the help of custom resources. Kubernetes uses a declarative model when you want a fixed desired result while dealing with cluster resources. By using Operators, Kubernetes defines its states in a declarative way. You can modify the Kubernetes cluster resources by using imperative commands. An Operator acts as a control loop which continuously compares the desired state of resources with the actual state of resources and puts actions in place to bring reality in line with the desired state. 

**Figure 4.2. Kubernetes cluster overview**

![247 OpenShift Kubernetes Overview 1](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/16b84090439adc71ef80265d0ed0ef48/247_OpenShift_Kubernetes_Overview-1.png) ![247 OpenShift Kubernetes Overview 1](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/16b84090439adc71ef80265d0ed0ef48/247_OpenShift_Kubernetes_Overview-1.png)

Table 4.2. Kubernetes ResourcesResource| Purpose  
---|---  
Service  |  Kubernetes uses services to expose a running application on a set of pods.   
`ReplicaSets` |  Kubernetes uses the `ReplicaSets` to maintain the constant pod number.   
Deployment  |  A resource object that maintains the life cycle of an application.   
Show more

Kubernetes is a core component of an OpenShift Container Platform. You can use OpenShift Container Platform for developing and running containerized applications. With its foundation in Kubernetes, the OpenShift Container Platform incorporates the same technology that serves as the engine for massive telecommunications, streaming video, gaming, banking, and other applications. You can extend your containerized applications beyond a single cloud to on-premise and multi-cloud environments by using the OpenShift Container Platform.
