# 1.3. Session affinity

You can use _session affinity_ if you want to ensure that each time you connect to a <service_VIP>:<Port>, the traffic is always load balanced to the same back end. For more information, including how to set session affinity based on a client’s IP address, see "Session affinity in Kubernetes". 

## 1.3.1. Stickiness timeout for session affinity

The OVN-Kubernetes network plugin for OpenShift Container Platform calculates the stickiness timeout for a session from a client based on the last packet. 

For example, if you run a `curl` command 10 times, the sticky session timer starts from the tenth packet not the first. 

As a result, if the client is continuously contacting the service, then the session never times out. The timeout starts when the service has not received a packet for the amount of time set by the `timeoutSeconds` parameter. For more information about `timeoutSeconds`, see "Session stickiness timeout in Kubernetes". 

**Additional resources**

  * [Session affinity in Kubernetes](https://kubernetes.io/docs/reference/networking/virtual-ips/#session-affinity)
  * [Session stickiness timeout in Kubernetes](https://kubernetes.io/docs/reference/networking/virtual-ips/#session-stickiness-timeout)



**Additional resources**

  * [Open Virtual Network website](https://www.ovn.org/en/)
  * [Configuring an egress firewall for a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-egress-firewall-ovn)
  * [About network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#about-network-policy)
  * [Logging network policy events](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#logging-network-security)
  * [Enabling multicast for a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ovn-kubernetes_network_plugin/nw-ovn-kubernetes-enabling-multicast "Chapter 13. Enabling multicast for a project")
  * [Configuring IPsec encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-ipsec-ovn)
  * [Network [operator.openshift.io/v1]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#network-operator-openshift-io-v1)
