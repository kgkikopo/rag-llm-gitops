# Chapter 10. Configuring an egress service

As a cluster administrator, you can configure egress traffic for pods behind a load balancer service by using an egress service. 

Important

Egress service is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

You can use the `EgressService` custom resource (CR) to manage egress traffic in the following ways: 

  * Assign a load balancer service IP address as the source IP address for egress traffic for pods behind the load balancer service. 

Assigning the load balancer IP address as the source IP address in this context is useful to present a single point of egress and ingress. For example, in some scenarios, an external system communicating with an application behind a load balancer service can expect the source and destination IP address for the application to be the same. 

Note

When you assign the load balancer service IP address to egress traffic for pods behind the service, OVN-Kubernetes restricts the ingress and egress point to a single node. This limits the load balancing of traffic that MetalLB typically provides. 

  * Assign the egress traffic for pods behind a load balancer to a different network than the default node network. 

This is useful to assign the egress traffic for applications behind a load balancer to a different network than the default network. Typically, the different network is implemented by using a VRF instance associated with a network interface.

- [10.1. Egress service custom resource](10_01_egress_service_custom_resource.md)
- [10.2. Deploy an egress service](10_02_deploy_an_egress_service.md)
