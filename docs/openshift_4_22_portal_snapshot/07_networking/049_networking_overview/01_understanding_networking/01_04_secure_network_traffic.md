# 1.4. Secure network traffic

OpenShift Container Platform provides tools to secure your network by creating rules that control which components are allowed to communicate. This is primarily managed through two types of policy resources: network policies and administrative network policies. 

## 1.4.1. Network policies

A network policy is a resource that allows you to control the flow of traffic at the IP address or port level. These policies operate at the namespace (project) level. This means they are typically managed by developers or project administrators to secure their specific applications. 

By default, all pods in a project can communicate with each other freely. However, when you apply a `NetworkPolicy` to a pod, it adopts a "default-deny" stance. This means it rejects any connection that is not explicitly allowed by a policy rule. You use labels and selectors to define which pods a policy applies to and what ingress and egress traffic is permitted. 

## 1.4.2. Administrative network policies

An `AdminNetworkPolicy` object is a more powerful, cluster-scoped version of a `NetworkPolicy` object. It can only be created and managed by a cluster administrator. 

Administrative network policies have a higher priority than standard `NetworkPolicy` objects. This allows administrators to enforce cluster-wide security rules that cannot be overridden by users in their own projects. For example, an administrator could use an `AdminNetworkPolicy` to block all traffic between development and production namespaces or to enforce baseline security rules for the entire cluster. 

**Additional resources**

  * [About network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#about-network-policy)
