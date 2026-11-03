# 14.2. Network isolation for hosted clusters

To provide distinct, secure environments for multiple hosted clusters that share the same management cluster, you can configure hosted clusters with specific network and virtual machine (VM) isolation levels. 

For hosted clusters, network isolation levels include container-based isolation, VM-based isolation, and physical isolation: 

Container-based isolation
     With container-based isolation, you use shared compute nodes, and isolation is enforced by policy, namespaces, and control group or SELinux boundaries. Control-plane components run as pods on the management cluster, isolated mainly by Kubernetes or Linux mechanisms, not by giving each hosted cluster its own VM or server. Each control plane runs in a dedicated namespace, with default-deny networking and a network policy that allows only defined traffic. Pods use the restricted security context constraint, with unique identifiers (UIDs) scoped for each namespace. 
VM-based isolation
    

With VM-based isolation, you run hosted control plane pods inside VMs; for example, on OpenShift Virtualization. This type of isolation is useful if you require VM-based isolation over container-based isolation for a multitenant management cluster. You add a hypervisor boundary between hosted clusters that share a management cluster. Control plane pods are pinned to dedicated VMs. 

To achieve VM-based isolation, you follow a "shared-nothing" approach, where each control plane has its own dedicated node. The management cluster must be an OpenShift Container Platform cluster on a VM so that the VM compute nodes can be used with the "shared-nothing" annotations to dedicate them to specific hosted control planes. Those hosted control planes will not share kernel space with control planes from other hosted clusters that are on the same management cluster. 

Physical isolation
     With physical isolation, you also follow a "shared-nothing" approach. Nodes for a specific hosted cluster are tainted and labeled with a specific `hypershift.openshift.io/hosted-cluster` value. Security involves the use of a network policy and physical network access control lists (ACLs) across hosted clusters. 

For more information, see "Control plane isolation" and "Distributing hosted cluster workloads". 

**Additional resources**

  * [Control plane isolation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-networking#hcp-isolation_hcp-networking "14.2.1. Control plane isolation")
  * [Distributing hosted cluster workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/preparing-to-deploy-hosted-control-planes#hcp-distribute-workloads "3.5. Distributing hosted cluster workloads")



## 14.2.1. Control plane isolation

You can configure hosted control planes to isolate network traffic or control plane pods. 

Each hosted control plane is assigned to run in a dedicated Kubernetes namespace. By default, the Kubernetes namespace denies all network traffic. 

The following network traffic is allowed through the network policy that is enforced by the Kubernetes Container Network Interface (CNI): 

  * Ingress pod-to-pod communication in the same namespace (intra-tenant) 
  * Ingress on port 6443 to the hosted `kube-apiserver` pod for the tenant 
  * Metric scraping from the management cluster Kubernetes namespace with the `network.openshift.io/policy-group: monitoring` label is allowed for monitoring 



### 14.2.1.1. Control plane pod isolation

In addition to network policies, each hosted control plane pod is run with the `restricted` security context constraint. This policy denies access to all host features and requires pods to be run with a unique identifier (UID) and with SELinux context that is allocated uniquely to each namespace that hosts a customer control plane. 

The policy ensures the following constraints: 

  * Pods cannot run as privileged. 
  * Pods cannot mount host directory volumes. 
  * Pods must run as a user in a pre-allocated range of UIDs. 
  * Pods must run with a pre-allocated Multi-Category Security (MCS) label. 
  * Pods cannot access the host network namespace. 
  * Pods cannot expose host network ports. 
  * Pods cannot access the host PID namespace. 
  * By default, pods drop the following Linux capabilities: `KILL`, `MKNOD`, `SETUID`, and `SETGID`. 



The management components, such as `kubelet` and `crio`, on each management cluster worker node are protected by an SELinux label that is not accessible to the SELinux context for pods that support hosted control planes. 

The following SELinux labels are used for key processes and sockets: 

`kubelet`
     `system_u:system_r:unconfined_service_t:s0`
`crio`
     `system_u:system_r:container_runtime_t:s0`
`crio.sock`
     `system_u:object_r:container_var_run_t:s0`
`<example user container processes>`
     `system_u:system_r:container_t:s0:c14,c24`

To achieve physical or virtual machine (VM) isolation, you need to use a "shared-nothing" approach, where each control plane has its own dedicated node. Nodes for a specific hosted cluster are tainted and labeled with a specific `hypershift.openshift.io/hosted-cluster` value. Security involves the use of a network policy and physical network access control lists (ACLs) across hosted clusters.
