# 2.1. Understand OpenShift Container Platform

You can use OpenShift Container Platform to deploy, configure, and manage the lifecycle of container-based applications. 

OpenShift Container Platform is a Kubernetes environment for managing containers and their dependencies on various computing platforms, such as bare metal, virtualized, on-premise, and in cloud. OpenShift Container Platform offers usability, stability, and customization of its components. 

OpenShift Container Platform utilises a number of computing resources, known as nodes. A node has a lightweight, secure operating system based on Red Hat Enterprise Linux (RHEL), known as Red Hat Enterprise Linux CoreOS (RHCOS). 

After a node is booted and configured, it obtains a container runtime, such as CRI-O or Docker, for managing and running the images of container workloads scheduled to it. The Kubernetes agent, or kubelet schedules container workloads on the node. The kubelet is responsible for registering the node with the cluster and receiving the details of container workloads. 

OpenShift Container Platform configures and manages the networking, load balancing and routing of the cluster. OpenShift Container Platform adds cluster services for monitoring the cluster health and performance, logging, and for managing upgrades. 

The container image registry and software catalog provide Red Hat certified products and community built softwares for providing various application services within the cluster. These applications and services manage the applications deployed in the cluster, databases, frontends and user interfaces, application runtimes and business automation, and developer services for development and testing of container applications. 

You can manage applications within the cluster either manually by configuring deployments of containers running from pre-built images or through resources known as Operators. You can build custom images from pre-build images and source code, and store these custom images locally in an internal, private or public registry. 

The Multicluster Management layer can manage multiple clusters including their deployment, configuration, compliance and distribution of workloads in a single console. 

![Red Hat OpenShift Kubernetes Engine](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/785227c5bdddf26566a9c43c0ddfcab6/oke-about-ocp-stack-image.png) ![Red Hat OpenShift Kubernetes Engine](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Overview-en-US/images/785227c5bdddf26566a9c43c0ddfcab6/oke-about-ocp-stack-image.png)
