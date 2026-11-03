# 2.11. Securing networks

You can manage network security at several levels, such as by using network namespaces and network policies. 

At the pod level, network namespaces can prevent containers from seeing other pods or the host system by restricting network access. Network policies give you control over allowing and rejecting connections. You can manage ingress and egress traffic to and from your containerized applications. 

## 2.11.1. Use network namespaces

You can use software-defined networking (SDN) in OpenShift Container Platform to give a unified cluster network that enables communication between containers across the cluster. 

Network policy mode, by default, makes all pods in a project accessible from other pods and network endpoints. To isolate one or more pods in a project, you can create `NetworkPolicy` objects in that project to indicate the allowed incoming connections. Using multitenant mode, you can provide project-level isolation for pods and services. 

## 2.11.2. Isolate pods with network policies

Using _network policies_ , you can isolate pods from each other in the same project. Network policies can deny all network access to a pod, only allow connections for the Ingress Controller, reject connections from pods in other projects, or set similar rules for how networks behave. 

**Additional resources**

  * [About network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#about-network-policy)



## 2.11.3. Use multiple pod networks

Each running container has only one network interface by default. You can use the Multus CNI plugin to create multiple CNI networks and attach any of those networks to a pod to separate private data onto a more restricted network. 

**Additional resources**

  * [Using multiple networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#understanding-multiple-networks)



## 2.11.4. Isolate applications

You can segment network traffic on a single cluster to make multitenant clusters that isolate users, teams, applications, and environments from non-global resources. 

## 2.11.5. Secure ingress traffic

There are many security implications related to how you configure access to your Kubernetes services from outside of your OpenShift Container Platform cluster. 

In addition to exposing HTTP and HTTPS routes, ingress routing allows you to set up `NodePort` or `LoadBalancer` ingress types. NodePort exposes an application’s service API object from each cluster worker. LoadBalancer lets you assign an external load balancer to an associated service API object in your OpenShift Container Platform cluster. 

**Additional resources**

  * [Configuring ingress cluster traffic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#configuring-ingress-cluster-traffic-ingress-controller)



## 2.11.6. Secure egress traffic

A cluster administrator can control egress traffic by using either a router or firewall method. For example, you can use the IP allow list to control database access. A cluster administrator can assign one or more egress IP addresses to a project by configuring an egress IP address. 

Likewise, a cluster administrator can prevent egress traffic from going outside of an OpenShift Container Platform cluster by using an egress firewall. 

By assigning a fixed egress IP address, you can have all outgoing traffic assigned to that IP address for a particular project. With the egress firewall, you can prevent a pod from connecting to an external network, prevent a pod from connecting to an internal network, or limit a pod’s access to specific internal subnets. 

**Additional resources**

  * [Configuring an egress firewall for a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-egress-firewall-ovn)
  * [Configuring IPsec encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-ipsec-ovn)
