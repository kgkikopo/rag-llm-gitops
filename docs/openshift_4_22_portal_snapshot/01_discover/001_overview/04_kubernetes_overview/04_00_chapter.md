# Chapter 4. Kubernetes overview

You can run and manage container-based workloads by using Kubernetes, an open source container orchestration tool developed by Google. 

The most common Kubernetes use case is to deploy an array of interconnected microservices, building an application in a cloud native way. You can create Kubernetes clusters that can span hosts across on-premise, public, private, or hybrid clouds. 

Traditionally, applications were deployed on top of a single operating system. With virtualization, you can split the physical host into several virtual hosts. Working on virtual instances on shared resources is not optimal for efficiency and scalability. Because a virtual machine (VM) consumes as many resources as a physical machine, providing resources to a VM such as CPU, RAM, and storage can be expensive. Also, you might see your application degrading in performance due to virtual instance usage on shared resources. 

**Figure 4.1. Evolution of container technologies for classical deployments**

![247 OpenShift Kubernetes Overview](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/57e7cf27848f5d30a70a61ea778c1101/247-OpenShift-Kubernetes-Overview.png) ![247 OpenShift Kubernetes Overview](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/57e7cf27848f5d30a70a61ea778c1101/247-OpenShift-Kubernetes-Overview.png)

To solve this problem, you can use containerization technologies that segregate applications in a containerized environment. Similar to a VM, a container has its own filesystem, vCPU, memory, process space, dependencies, and more. Containers are decoupled from the underlying infrastructure, and are portable across clouds and OS distributions. Containers are inherently much lighter than a fully-featured OS, and are lightweight isolated processes that run on the operating system kernel. VMs are slower to boot, and are an abstraction of physical hardware. VMs run on a single machine with the help of a hypervisor. 

You can perform the following actions by using Kubernetes: 

  * Sharing resources 
  * Orchestrating containers across multiple hosts 
  * Installing new hardware configurations 
  * Running health checks and self-healing applications 
  * Scaling containerized applications

- [4.1. Kubernetes components](04_01_kubernetes_components.md)
- [4.2. Kubernetes resources](04_02_kubernetes_resources.md)
- [4.3. Kubernetes architecture](04_03_kubernetes_architecture.md)
- [4.4. Kubernetes conceptual guidelines](04_04_kubernetes_conceptual_guidelines.md)
