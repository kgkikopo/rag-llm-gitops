# 2.2. Differences between hosted control planes and OpenShift Container Platform

Hosted control planes is a form factor of OpenShift Container Platform. Hosted clusters and the standalone OpenShift Container Platform clusters are configured and managed differently. 

See the following tables to understand the differences between OpenShift Container Platform and hosted control planes: 

## 2.2.1. Cluster creation and lifecycle

OpenShift Container Platform| Hosted control planes  
---|---  
You install a standalone OpenShift Container Platform cluster by using the `openshift-install` binary or the Assisted Installer.  |  You install a hosted cluster by using the `hypershift.openshift.io` API resources such as `HostedCluster` and `NodePool`, on an existing OpenShift Container Platform cluster.   
Show more

## 2.2.2. Cluster configuration

OpenShift Container Platform| Hosted control planes  
---|---  
You configure cluster-scoped resources such as authentication, API server, and proxy by using the `config.openshift.io` API group.  |  You configure resources that impact the control plane in the `HostedCluster` resource.   
Show more

## 2.2.3. etcd encryption

OpenShift Container Platform| Hosted control planes  
---|---  
You configure etcd encryption by using the `APIServer` resource with AES-GCM or AES-CBC. For more information, see "Enabling etcd encryption".  |  You configure etcd encryption by using the `HostedCluster` resource in the `SecretEncryption` field with AES-CBC or KMS for Amazon Web Services.   
Show more

## 2.2.4. Operators and control plane

OpenShift Container Platform| Hosted control planes  
---|---  
A standalone OpenShift Container Platform cluster contains separate Operators for each control plane component.  |  A hosted cluster contains a single Operator named Control Plane Operator that runs in the hosted control plane namespace on the management cluster.   
etcd uses storage that is mounted on the control plane nodes. The etcd cluster Operator manages etcd.  |  etcd uses a persistent volume claim for storage and is managed by the Control Plane Operator.   
The Ingress Operator, network related Operators, and Operator Lifecycle Manager (OLM) run on the cluster.  |  The Ingress Operator, network related Operators, and Operator Lifecycle Manager (OLM) run in the hosted control plane namespace on the management cluster.   
The OAuth server runs inside the cluster and is exposed through a route in the cluster.  |  The OAuth server runs inside the control plane and is exposed through a route, node port, or load balancer on the management cluster.   
Show more

## 2.2.5. Updates

OpenShift Container Platform| Hosted control planes  
---|---  
The Cluster Version Operator (CVO) orchestrates the update process and monitors the `ClusterVersion` resource. Administrators and OpenShift components can interact with the CVO through the `ClusterVersion` resource. The `oc adm upgrade` command results in a change to the `ClusterVersion.Spec.DesiredUpdate` field in the `ClusterVersion` resource.  |  The hosted control planes update results in a change to the `.spec.release.image` field in the `HostedCluster` and `NodePool` resources. Any changes to the `ClusterVersion` resource are ignored.   
After you update an OpenShift Container Platform cluster, both the control plane and compute machines are updated.  |  After you update the hosted cluster, only the control plane is updated. You perform node pool updates separately.   
Show more

## 2.2.6. Machine configuration and management

OpenShift Container Platform| Hosted control planes  
---|---  
The `MachineSets` resource manages machines in the `openshift-machine-api` namespace.  |  The `NodePool` resource manages machines on the management cluster.   
A set of control plane machines are available.  |  A set of control plane machines do not exist.   
You enable a machine health check by using the `MachineHealthCheck` resource.  |  You enable a machine health check through the `.spec.management.autoRepair` field in the `NodePool` resource.   
You enable autoscaling by using the `ClusterAutoscaler` and `MachineAutoscaler` resources.  |  You enable autoscaling through the `spec.autoScaling` field in the `NodePool` resource.   
Machines and machine sets are exposed in the cluster.  |  Machines, machine sets, and machine deployments from upstream Cluster CAPI Operator are used to manage machines but are not exposed to the user.   
All machine sets are upgraded automatically when you update the cluster.  |  You update your node pools independently from the hosted cluster updates.   
Only an in-place upgrade is supported in the cluster.  |  Both replace and in-place upgrades are supported in the hosted cluster.   
The Machine Config Operator manages configurations for machines.  |  The Machine Config Operator does not exist in hosted control planes.   
You configure machine Ignition by using the `MachineConfig`, `KubeletConfig`, and `ContainerRuntimeConfig` resources that are selected from a `MachineConfigPool` selector.  |  You configure the `MachineConfig`, `KubeletConfig`, and `ContainerRuntimeConfig` resources through the config map referenced in the `spec.config` field of the `NodePool` resource.   
The Machine Config Daemon (MCD) manages configuration changes and updates on each of the nodes.  |  For an in-place upgrade, the node pool controller creates a run-once pod that updates a machine based on your configuration.   
You can modify the machine configuration resources such as the SR-IOV Operator.  |  You cannot modify the machine configuration resources.   
Show more

## 2.2.7. Networking

OpenShift Container Platform| Hosted control planes  
---|---  
The Kube API server communicates with nodes directly, because the Kube API server and nodes exist in the same Virtual Private Cloud (VPC).  |  The Kube API server communicates with nodes through Konnectivity. The Kube API server and nodes exist in a different Virtual Private Cloud (VPC).   
Nodes communicate with the Kube API server through the internal load balancer.  |  Nodes communicate with the Kube API server through an external load balancer or a node port.   
Show more

## 2.2.8. Web console

OpenShift Container Platform| Hosted control planes  
---|---  
The web console shows the status of a control plane.  |  The web console does not show the status of a control plane.   
You can update your cluster by using the web console.  |  You cannot update the hosted cluster by using the web console.   
The web console displays the infrastructure resources such as machines.  |  The web console does not display the infrastructure resources.   
You can configure machines through the `MachineConfig` resource by using the web console.  |  You cannot configure machines by using the web console.   
Show more

**Additional resources**

  * [Enabling etcd encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#etcd-encrypt)
