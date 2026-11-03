# 1.1. Glossary of common terms for OpenShift Container Platform architecture

Review the architecture terms and concepts to plan and deploy the cluster infrastructure. 

access policies
     A set of roles that dictate how users, applications, and entities within a cluster interact with one another. An access policy increases cluster security. 
admission plugins
     Admission plugins enforce security policies, resource limitations, or configuration requirements. 
authentication
     To control access to an OpenShift Container Platform cluster, a cluster administrator can configure user authentication to ensure only approved users access the cluster. To interact with an OpenShift Container Platform cluster, you must authenticate with the OpenShift Container Platform API. You can authenticate by providing an OAuth access token or an X.509 client certificate in your requests to the OpenShift Container Platform API. 
bootstrap
     A temporary machine that runs minimal Kubernetes and deploys the OpenShift Container Platform control plane. 
certificate signing requests (CSRs)
     A resource requests a denoted signer to sign a certificate. This request might get approved or denied. 
Cluster Version Operator (CVO)
     An Operator that checks with the OpenShift Container Platform Update Service to see the valid updates and update paths based on current component versions and information in the graph. 
compute nodes
     Nodes that are responsible for executing workloads for cluster users. Compute nodes are also known as worker nodes. 
configuration drift
     A situation where the configuration on a node does not match what the machine config specifies. 
containers
     Lightweight and executable images that consist of software and all of its dependencies. Because containers virtualize the operating system, you can run containers anywhere, such as data centers, public or private clouds, and local hosts. 
container orchestration engine
     Software that automates the deployment, management, scaling, and networking of containers. 
container workloads
     Applications that are packaged and deployed in containers. 
control groups (cgroups)
     Partitions sets of processes into groups to manage and limit the resources processes consume. 
control plane
     A container orchestration layer that exposes the API and interfaces to define, deploy, and manage the life cycle of containers. Control planes are also known as control plane machines. 
CRI-O
     A Kubernetes native container runtime implementation that integrates with the operating system to deliver an efficient Kubernetes experience. 
deployment
     A Kubernetes resource object that maintains the life cycle of an application. 
Dockerfile
     A text file that contains the user commands to perform on a terminal to assemble the image. 
hosted control planes
    

A OpenShift Container Platform feature that enables hosting a control plane on the OpenShift Container Platform cluster from its data plane and workers. This model performs the following actions: 

  * Optimize infrastructure costs required for the control planes. 
  * Improve the cluster creation time. 
  * Enable hosting the control plane using the Kubernetes native high level primitives. For example, deployments and stateful sets. 
  * Allow a strong network segmentation between the control plane and workloads. 



hybrid cloud deployments
     Deployments that deliver a consistent platform across bare metal, virtual, private, and public cloud environments. This offers speed, agility, and portability. 
Ignition
     A utility that RHCOS uses to manipulate disks during initial configuration. It completes common disk tasks, including partitioning disks, formatting partitions, writing files, and configuring users. 
installer-provisioned infrastructure
     The installation program deploys and configures the infrastructure that the cluster runs on. 
kubelet
     A primary node agent that runs on each node in the cluster to ensure that containers are running in a pod. 
kubernetes manifest
     Specifications of a Kubernetes API object in a JSON or YAML format. A configuration file can include deployments, config maps, secrets, daemon sets. 
Machine Config Daemon (MCD)
     A daemon that regularly checks the nodes for configuration drift. 
Machine Config Operator (MCO)
     An Operator that applies the new configuration to your cluster machines. 
machine config pools (MCP)
     A group of machines, such as control plane components or user workloads, that are based on the resources that they handle. 
metadata
     Additional information about cluster deployment artifacts. 
microservices
     An approach to writing software. Applications can be separated into the smallest components, independent from each other by using microservices. 
mirror registry
     A registry that holds the mirror of OpenShift Container Platform images. 
monolithic applications
     Applications that are self-contained, built, and packaged as a single piece. 
namespaces
     A namespace isolates specific system resources that are visible to all processes. Inside a namespace, only processes that are members of that namespace can see those resources. 
networking
     Network information of OpenShift Container Platform cluster. 
node
     A worker machine in the OpenShift Container Platform cluster. A node is either a virtual machine (VM) or a physical machine. 
OpenShift CLI (`oc`)
     A command-line tool to run OpenShift Container Platform commands on the terminal. 
OpenShift Dedicated
     A managed RHEL OpenShift Container Platform offering on Amazon Web Services (AWS) and Google Cloud. OpenShift Dedicated focuses on building and scaling applications. 
OpenShift Update Service (OSUS)
     For clusters with internet access, Red Hat Enterprise Linux (RHEL) provides over-the-air updates by using an OpenShift update service as a hosted service located behind public APIs. 
OpenShift image registry
     A registry provided by OpenShift Container Platform to manage images. 
Operator
     The preferred method of packaging, deploying, and managing a Kubernetes application in an OpenShift Container Platform cluster. An Operator takes human operational knowledge and encodes it into software that is packaged and shared with customers. 
OperatorHub
     A platform that contains various OpenShift Container Platform Operators to install. 
Operator Lifecycle Manager (OLM)
     OLM helps you to install, update, and manage the lifecycle of Kubernetes native applications. OLM is an open source toolkit designed to manage Operators in an effective, automated, and scalable way. 
OSTree
     An upgrade system for Linux-based operating systems that performs atomic upgrades of complete file system trees. OSTree tracks meaningful changes to the file system tree using an addressable object store, and is designed to complement existing package management systems. 
over-the-air (OTA) updates
     The OpenShift Container Platform Update Service (OSUS) provides over-the-air updates to OpenShift Container Platform, including Red Hat Enterprise Linux CoreOS (RHCOS). 
pod
     One or more containers with shared resources, such as volume and IP addresses, running in your OpenShift Container Platform cluster. A pod is the smallest compute unit defined, deployed, and managed. 
private registry
     OpenShift Container Platform can use any server implementing the container image registry API as a source of the image which allows the developers to push and pull their private container images. 
public registry
     OpenShift Container Platform can use any server implementing the container image registry API as a source of the image which allows the developers to push and pull their public container images. 
RHEL OpenShift Container Platform Cluster Manager
     A managed service where you can install, modify, operate, and upgrade your OpenShift Container Platform clusters. 
RHEL Quay Container Registry
     A Quay.io container registry that serves most of the container images and Operators to OpenShift Container Platform clusters. 
replication controllers
     An asset that indicates how many pod replicas are required to run at a time. 
role-based access control (RBAC)
     A key security control to ensure that cluster users and workloads have only access to resources required to execute their roles. 
route
     Routes expose a service to allow for network access to pods from users and applications outside the OpenShift Container Platform instance. 
scaling
     The increasing or decreasing of resource capacity. 
service
     A service exposes a running application on a set of pods. 
Source-to-Image (S2I) image
     An image created based on the programming language of the application source code in OpenShift Container Platform to deploy applications. 
storage
     OpenShift Container Platform supports many types of storage, both for on-premise and cloud providers. You can manage container storage for persistent and non-persistent data in an OpenShift Container Platform cluster. 
Telemetry
     A component to collect information such as size, health, and status of OpenShift Container Platform. 
template
     A template describes a set of objects that can be parameterized and processed to produce a list of objects for creation by OpenShift Container Platform. 
user-provisioned infrastructure
     You can install OpenShift Container Platform on the infrastructure that you provide. You can use the installation program to generate the assets required to provision the cluster infrastructure, create the cluster infrastructure, and then deploy the cluster to the infrastructure that you provided. 
web console
     A user interface (UI) to manage OpenShift Container Platform. 
worker node
     Nodes that are responsible for executing workloads for cluster users. Worker nodes are also known as compute nodes. 

**Additional resources**

  * [Product architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/architecture "Chapter 2. OpenShift Container Platform architecture")
  * [OpenShift Container Platform networking](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_overview/#understanding-networking)
  * [OpenShift Container Platform storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#index)
  * [OpenShift Container Platform authentication](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#index)
  * [OLM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-understanding-olm)
  * [Introduction to OpenShift updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#understanding-openshift-updates)
