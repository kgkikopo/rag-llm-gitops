# 6.2. Machine roles in OpenShift Container Platform

OpenShift Container Platform assigns hosts different roles. These roles define the function of the machine within the cluster. The cluster contains definitions for the standard `master` and `worker` role types. 

Note

The cluster also contains the definition for the `bootstrap` role. The installation program uses the bootstrap machine only during cluster deployment. See the cluster installation documentation to learn more about its role. 

Control plane and node host compatibility
    

The OpenShift Container Platform version must match between control plane host and node host. For example, in a 4.22 cluster, all control plane hosts must be 4.22 and all nodes must be 4.22. 

Temporary mismatches during cluster upgrades are acceptable. For example, when upgrading from the previous OpenShift Container Platform version to 4.22, some nodes upgrade to 4.22 before others. Prolonged skewing of control plane hosts and node hosts might expose older compute machines to bugs and missing features. Users can resolve skewed control plane hosts and node hosts as soon as possible. 

The `kubelet` service must not be newer than `kube-apiserver`, and can be up to two minor versions older depending on whether your OpenShift Container Platform version is odd or even. The table below shows the appropriate version compatibility: 

OpenShift Container Platform version| Supported `kubelet` skew  
---|---  
Odd OpenShift Container Platform minor versions [1] |  Up to one version older   
Even OpenShift Container Platform minor versions [2] |  Up to two versions older   
Show more

  1. For example, OpenShift Container Platform 4.11, 4.13. 
  2. For example, OpenShift Container Platform 4.10, 4.12. 



Cluster workers
    

In a Kubernetes cluster, worker nodes run and manage the actual workloads requested by Kubernetes users. The worker nodes advertise their capacity and the scheduler, which is a control plane service, determines on which nodes to start pods and containers. The following important services run on each worker node: 

  * CRI-O, which is the container engine. 
  * kubelet, which is the service that accepts and fulfills requests for running and stopping container workloads. 
  * A service proxy, which manages communication for pods across workers. 
  * The crun or runC low-level container runtime, which creates and runs containers. 

Note

For information about how to enable runC instead of the default crun, see the documentation for creating a `ContainerRuntimeConfig` CR. 

In OpenShift Container Platform, compute machine sets control the compute machines, which are assigned the `worker` machine role. Machines with the `worker` role drive compute workloads that are governed by a specific machine pool that autoscales them. Because OpenShift Container Platform has the capacity to support multiple machine types, the machines with the `worker` role are classed as _compute_ machines. In this release, the terms _worker machine_ and _compute machine_ are used interchangeably because the only default type of compute machine is the worker machine. In future versions of OpenShift Container Platform, different types of compute machines, such as infrastructure machines, might be used by default. 

Note

Compute machine sets are groupings of compute machine resources under the `machine-api` namespace. Compute machine sets are configurations that start new compute machines on a specific cloud provider. Conversely, machine config pools (MCPs) are part of the Machine Config Operator (MCO) namespace. An MCP is used to group machines together so the MCO can manage their configurations and facilitate their upgrades. 




Cluster control planes
    

In a Kubernetes cluster, the _master_ nodes run services that are required to control the Kubernetes cluster. In OpenShift Container Platform, the control plane consists of control plane machines that have a `master` machine role. They contain more than just the Kubernetes services for managing the OpenShift Container Platform cluster. 

For most OpenShift Container Platform clusters, control plane machines are defined by a series of standalone machine API resources. For supported cloud provider and OpenShift Container Platform version combinations, control planes can be managed with control plane machine sets. Extra controls apply to control plane machines to prevent you from deleting all of the control plane machines and making the cluster inoperable. Exactly three control plane nodes must be used for all production deployments. 

Note

On a bare-metal platform, you can scale a cluster to three, four, or five control plane nodes. For best results, use odd size control plane nodes, such as three or five, on a cluster. A four-node control plane has the same etcd one failure tolerance as three nodes. Only a five-node control plane can tolerate two simultaneous failures. 

Adding a fourth control plane node means etcd needs three healthy members instead of two. Until the fourth node is healthy, losing one of the original nodes breaks quorum and takes the cluster down. 

\+ Services that fall under the Kubernetes category on the control plane include the Kubernetes API server, etcd, the Kubernetes controller manager, and the Kubernetes scheduler. 

\+ .Kubernetes services that run on the control plane 

Component| Description  
---|---  
Kubernetes API server  |  The Kubernetes API server validates and configures the data for pods, services, and replication controllers. It also provides a focal point for the shared state of the cluster.   
etcd  |  etcd stores the persistent control plane state while other components watch etcd for changes to bring themselves into the specified state.   
Kubernetes controller manager  |  The Kubernetes controller manager watches etcd for changes to objects such as replication, namespace, and service account controller objects, and then uses the API to enforce the specified state. Several such processes create a cluster with one active leader at a time.   
Kubernetes scheduler  |  The Kubernetes scheduler watches for newly created pods without an assigned node and selects the best node to host the pod.   
Show more

\+ There are also OpenShift services that run on the control plane, which include the OpenShift API server, OpenShift controller manager, OpenShift OAuth API server, and OpenShift OAuth server. 

\+ .OpenShift services that run on the control plane 

Component| Description  
---|---  
OpenShift API server  |  The OpenShift API server validates and configures the data for OpenShift resources, such as projects, routes, and templates.  The OpenShift API server is managed by the OpenShift API Server Operator.   
OpenShift controller manager  |  The OpenShift controller manager watches etcd for changes to OpenShift objects, such as project, route, and template controller objects, and then uses the API to enforce the specified state.  The OpenShift controller manager is managed by the OpenShift Controller Manager Operator.   
OpenShift OAuth API server  |  The OpenShift OAuth API server validates and configures the data to authenticate to OpenShift Container Platform, such as users, groups, and OAuth tokens.  The OpenShift OAuth API server is managed by the Cluster Authentication Operator.   
OpenShift OAuth server  |  Users request tokens from the OpenShift OAuth server to authenticate themselves to the API.  The OpenShift OAuth server is managed by the Cluster Authentication Operator.   
Show more

\+ Some of these services on the control plane machines run as systemd services, while others run as static pods. 

\+ Systemd services are appropriate for services that must always start on that particular system shortly after it starts. For control plane machines, such as those include sshd, that allow remote login. It also includes services such as: 

\+ * The CRI-O container engine (crio), which runs and manages the containers. OpenShift Container Platform 4.22 uses CRI-O instead of the Docker Container Engine. * Kubelet (kubelet), which accepts requests for managing containers on the machine from control plane services. 

\+ CRI-O and Kubelet must run directly on the host as systemd services because they need to be running before you can run other containers. 

\+ The `installer-*` and `revision-pruner-*` control plane pods must run with root permissions because they write to the `/etc/kubernetes` directory, which is owned by the root user. These pods are in the following namespaces: 

  * `openshift-etcd`
  * `openshift-kube-apiserver`
  * `openshift-kube-controller-manager`
  * `openshift-kube-scheduler`
