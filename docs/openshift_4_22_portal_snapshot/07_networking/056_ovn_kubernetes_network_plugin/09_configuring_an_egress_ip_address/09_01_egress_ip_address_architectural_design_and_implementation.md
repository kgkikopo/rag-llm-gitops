# 9.1. Egress IP address architectural design and implementation

By using the OpenShift Container Platform egress IP address functionality, you can ensure that the traffic from one or more pods in one or more namespaces has a consistent source IP address for services outside the cluster network. 

For example, you might have a pod that periodically queries a database that is hosted on a server outside of your cluster. To enforce access requirements for the server, a packet filtering device is configured to allow traffic only from specific IP addresses. 

To ensure that you can reliably allow access to the server from only that specific pod, you can configure a specific egress IP address for the pod that makes the requests to the server. 

An egress IP address assigned to a namespace is different from an egress router, which is used to send traffic to specific destinations. 

In some cluster configurations, application pods and ingress router pods run on the same node. If you configure an egress IP address for an application project in this scenario, the IP address is not used when you send a request to a route from the application project. 

Important

Egress IP addresses must not be configured in any Linux network configuration files, such as `ifcfg-eth0`. 

Important

The assignment of egress IP addresses to control plane nodes with the EgressIP feature is not supported on a cluster provisioned on Amazon Web Services (AWS). For more information, see "BZ#2039656". 

The following examples illustrate the annotation from nodes on several public cloud providers. The annotations are indented for readability. 

**Example`cloud.network.openshift.io/egress-ipconfig` annotation on AWS**

```yaml
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
```


The following sections describe the IP address capacity for supported public cloud environments for use in your capacity calculation. 

Amazon Web Services (AWS) IP address capacity limits
     On AWS, constraints on IP address assignments depend on the instance type configured. For more information, see "IP addresses per network interface per instance type". 
Google Cloud IP address capacity limits
     On Google Cloud, the networking model implements additional node IP addresses through IP address aliasing, rather than IP address assignments. However, IP address capacity maps directly to IP aliasing capacity. 

The following capacity limits exist for IP aliasing assignment: 

  * Per node, the maximum number of IP aliases, both IPv4 and IPv6, is 100. 
  * Per VPC, the maximum number of IP aliases is unspecified, but OpenShift Container Platform scalability testing reveals the maximum to be approximately 15,000. 



For more information, see "Per instance" quotas and "Alias IP ranges overview". 

Microsoft Azure IP address capacity limits
    

On Azure, the following capacity limits exist for IP address assignment: 

  * Per NIC, the maximum number of assignable IP addresses, for both IPv4 and IPv6, is 256. 
  * Per virtual network, the maximum number of assigned IP addresses cannot exceed 65,536. 



For more information, see "Networking limits". 

**Additional resources**

  * [BZ#2039656 (Red Hat Bugzilla)](https://bugzilla.redhat.com/show_bug.cgi?id=2039656)
  * [Per instance (Google Cloud documentation)](https://cloud.google.com/vpc/docs/quota#per_instance)
  * [Alias IP ranges overview (Google Cloud documentation)](https://cloud.google.com/vpc/docs/alias-ip)
  * [Networking limits (Microsoft Azure documentation)](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits?toc=/azure/virtual-network/toc.json#networking-limits)
  * [IP addresses per network interface per instance type (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)



## 9.1.1. Platform support

The Egress IP address feature that runs on a primary host network is supported on specific platforms. 

The following table shows supported platforms for egress IP on primary host networks: 

Platform| Supported  
---|---  
Bare metal  |  Yes   
VMware vSphere  |  Yes   
Red Hat OpenStack Platform (RHOSP)  |  Yes   
Amazon Web Services (AWS)  |  Yes   
Google Cloud  |  Yes   
Microsoft Azure  |  Yes   
IBM Z® and IBM® LinuxONE  |  Yes   
IBM Z® and IBM® LinuxONE for Red Hat Enterprise Linux (RHEL) KVM  |  Yes   
IBM Power®  |  Yes   
Nutanix  |  Yes   
Show more

Important

Support for egress IP addresses in Microsoft Azure is restricted to the infra subnet. As a workaround for this limitation, you can use a Network Address Translation (NAT) gateway instead of a general purpose public load balancer. 

The Egress IP address feature that runs on secondary host networks is supported on the following platform: 

Platform| Supported  
---|---  
Bare metal  |  Yes   
Show more

## 9.1.2. Public cloud platform considerations

Typically, public cloud providers place a limit on egress IP addresses. You must understand the existence of a constraint on the absolute number of assignable IP addresses per node for clusters provisioned on public cloud infrastructure. 

The maximum number of assignable IP addresses per node, or the _IP capacity_ , can be described in the following formula: 

```plaintext
IP capacity = public cloud default capacity - sum(current IP assignments)
```


While the Egress IP addresses capability manages the IP address capacity per node, ensure you plan for this constraint in your deployments. For example, if a public cloud provider limits IP address capacity to 10 IP addresses per node, and you have 8 nodes, the total number of assignable IP addresses is only 80. To achieve a higher IP address capacity, you would need to allocate additional nodes. For example, if you needed 150 assignable IP addresses, you would need to allocate 7 additional nodes. 

To confirm the IP capacity and subnets for any node in your public cloud environment, you can enter the `oc get node <node_name> -o yaml` command. The `cloud.network.openshift.io/egress-ipconfig` annotation includes capacity and subnet information for the node. 

The annotation value is an array with a single object with fields that provide the following information for the primary network interface: 

  * `interface`: Specifies the interface ID on AWS and Azure and the interface name on Google Cloud. 
  * `ifaddr`: Specifies the subnet mask for one or both IP address families. 
  * `capacity`: Specifies the IP address capacity for the node. On AWS, the IP address capacity is provided per IP address family. On Azure and Google Cloud, the IP address capacity includes both IPv4 and IPv6 addresses. 



Automatic attachment and detachment of egress IP addresses for traffic between nodes are available. Traffic from many pods in namespaces can have a consistent source IP address to locations outside of the cluster. 

Note

When an RHOSP cluster administrator assigns a floating IP to the reservation port, OpenShift Container Platform cannot delete the reservation port. The `CloudPrivateIPConfig` object cannot perform delete and move operations until an RHOSP cluster administrator unassigns the floating IP from the reservation port. 

The following examples illustrate the annotation from nodes on several public cloud providers. The annotations are indented for readability. 

**Example`cloud.network.openshift.io/egress-ipconfig` annotation on AWS**

```yaml
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
```


**Example`cloud.network.openshift.io/egress-ipconfig` annotation on Google Cloud**

```yaml
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"nic0",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ip":14}
  }
]
```


## 9.1.3. Considerations for using an egress IP address on additional network interfaces

In OpenShift Container Platform, egress IP addresses provide administrators a way to control network traffic. You can use egress IP addresses with a `br-ex` Open vSwitch (OVS) bridge interface. You can also use any physical interface that has IP connectivity enabled. 

You can inspect your network interface type by running the following command: 

```shell-session
$ ip -details link show
```


The primary network interface is assigned a node IP address which also contains a subnet mask. You can retrieve this node IP address information from the Kubnernetes node object. Inspect the `k8s.ovn.org/node-primary-ifaddr` annotation for each node in your cluster. In an IPv4 cluster, this annotation is similar to the following example: `"k8s.ovn.org/node-primary-ifaddr: {"ipv4":"192.168.111.23/24"}"`. 

If the egress IP address is not within the subnet of the primary network interface subnet, use another Linux network interface. This interface must not be of the primary network interface type. With this approach, an administrator can provide a greater level of control over networking aspects such as routing, addressing, segmentation, and security policies. With this feature, you can route workload traffic over specific network interfaces for purposes such as traffic segmentation or meeting specialized requirements. 

If the egress IP address is not within the subnet of the primary network interface, then the selection of another network interface for egress traffic might occur if they are present on a node. 

You can determine which other network interfaces might support egress IP address addresses by inspecting the `k8s.ovn.org/host-cidrs` Kubernetes node annotation. This annotation contains the addresses and subnet mask found for the primary network interface. The annotation also contains additional network interface addresses and subnet mask information. These addresses and subnet masks are assigned to network interfaces that use the longest prefix match routing mechanism to determine which network interface supports the egress IP address. For more information, see "Longest prefix match routing" in the _Additional resources_ section. 

Note

By using OVN-Kubernetes, you can control how outbound traffic leaves the cluster. You can configure traffic from specific namespaces or pods to exit through a chosen network interface and use a designated egress IP address. This configuration routes application traffic over specific network paths, providing better network isolation and traffic management. 

As an administrator who wants an egress IP address and traffic to route over a particular interface that is not the primary network interface, you must meet the following conditions: 

  * OpenShift Container Platform is installed on a bare-metal cluster. This feature is disabled within a cloud or a hypervisor environment. 
  * Your OpenShift Container Platform pods are not configured as _host-networked_. 
  * You understand that if a network interface is removed or if the IP address and subnet mask which allows the egress IP address to be hosted on the interface is removed, reconfiguration of the egress IP address occurs. Consequently, the egress IP address might get assigned to another node and interface. 
  * You configured a NIC with routes by ensuring a gateway exists in the main routing table. As a postinstallation task, Red Hat does not support configuring a NIC on a cluster that uses OVN-Kubernetes. 
  * Routes associated with an egress interface get copied from the main routing table to the routing table that was created to support the Egress IP object. 
  * You can use an Egress IP address on a secondary network interface card (NIC). However, you must use the Node Tuning Operator to enable IP forwarding on the secondary NIC. 

Important

Red Hat does not support EgressIP multi-NIC configurations when the target network interface is bound to a VRF instance. 




**Additional resources**

  * [Longest prefix match routing (NetworkLessons documentation)](https://networklessons.com/cisco/ccna-200-301/longest-prefix-match-routing)



## 9.1.4. Architectural diagram of an egress IP address configuration

To better understand egress IP address configuration, reference the architectural diagram. 

The following diagram shows an egress IP address configuration. The diagram describes four pods in two different namespaces running on three nodes in a cluster. The nodes are assigned IP addresses from the `192.168.126.0/18` CIDR block on the host network. 

Both Node 1 and Node 3 are labeled with `k8s.ovn.org/egress-assignable: ""` and thus available for the assignment of egress IP addresses. 

The dashed lines in the diagram depict the traffic flow from pod1, pod2, and pod3 traveling through the pod network to egress the cluster from Node 1 and Node 3. When an external service receives traffic from any of the pods selected by the example `EgressIP` object, the source IP address is either `192.168.126.10` or `192.168.126.102`. The traffic is balanced roughly equally between these two nodes. 

Based on the diagram, the following manifest file defines namespaces: 

**Namespace objects**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: namespace1
  labels:
    env: prod
---
apiVersion: v1
kind: Namespace
metadata:
  name: namespace2
  labels:
    env: prod
```


Based on the diagram, the following `EgressIP` object describes a configuration that selects all pods in any namespace with the `env` label set to `prod`. The egress IP addresses for the selected pods are `192.168.126.10` and `192.168.126.102`. 

**`EgressIP` object**

```yaml
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egressips-prod
spec:
  egressIPs:
  - 192.168.126.10
  - 192.168.126.102
  namespaceSelector:
    matchLabels:
      env: prod
status:
  items:
  - node: node1
    egressIP: 192.168.126.10
  - node: node3
    egressIP: 192.168.126.102
```


For the configuration in the previous example, OpenShift Container Platform assigns both egress IP addresses to the available nodes. The `status` field reflects whether and where the egress IP addresses are assigned.
