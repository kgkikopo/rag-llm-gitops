# 7.4. Inter-service authorization

It is critical to be able to control access to services based on the identity of the requester. This is done by the platform and does not require each application to implement it. That allows better auditing and inspection of the policies. 

Leverage: 

  * OpenShift Container Platform: Can enforce isolation in the networking layer of the platform using the Kubernetes [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_security/network-policy#about-network-policy "3.1. Creating a network policy") and [`AdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_security/admin-network-policy#ovn-k-anp "2.1. OVN-Kubernetes AdminNetworkPolicy") objects. 
  * [Red Hat OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-about): Sophisticated L4 and L7 [control of traffic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-security) using standard Istio objects and using mTLS to identify the source and destination of traffic and then apply policies based on that information.
