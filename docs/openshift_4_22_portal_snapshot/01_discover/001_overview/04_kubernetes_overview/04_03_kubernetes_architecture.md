# 4.3. Kubernetes architecture

You can run Kubernetes containers across various machines and environments. 

A cluster is a single computational unit consisting of multiple nodes in a cloud environment. A Kubernetes cluster includes a control plane and compute nodes. 

The control plane node controls and maintains the state of a cluster. You can run the Kubernetes application by using compute nodes. You can use the Kubernetes namespace to differentiate cluster resources in a cluster. Namespace scoping is applicable for resource objects, such as deployments, services, and pods. You cannot use namespace for cluster-wide resource objects such as storage classes, nodes, and persistent volumes. 

**Figure 4.3. Architecture of Kubernetes**

![247 OpenShift Kubernetes Overview 2](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/c8d00fda77932b65f092760ad269d15c/247_OpenShift_Kubernetes_Overview-2.png) ![247 OpenShift Kubernetes Overview 2](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/c8d00fda77932b65f092760ad269d15c/247_OpenShift_Kubernetes_Overview-2.png)
