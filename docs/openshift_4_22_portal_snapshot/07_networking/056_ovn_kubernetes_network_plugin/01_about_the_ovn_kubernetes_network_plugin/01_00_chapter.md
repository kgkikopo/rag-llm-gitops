# Chapter 1. About the OVN-Kubernetes network plugin

The OpenShift Container Platform cluster uses a virtualized network for pod and service networks. The OVN-Kubernetes network plugin is the default provider that implements this virtualized overlay network by transforming configurations into OpenFlow rules to enable advanced routing and security features. 

Part of Red Hat OpenShift Networking, the OVN-Kubernetes network plugin is the default network provider for OpenShift Container Platform. OVN-Kubernetes is based on Open Virtual Network (OVN) and provides an overlay-based networking implementation. A cluster that uses the OVN-Kubernetes plugin also runs Open vSwitch (OVS) on each node. OVN configures OVS on each node to implement the declared network configuration. 

Note

OVN-Kubernetes is the default networking solution for OpenShift Container Platform and single-node OpenShift deployments. 

OVN-Kubernetes, which arose from the OVS project, uses many of the same constructs. For example, the plugin applies OpenFlow rules to direct packet routing through the network infrastructure. For more information, see the "Open Virtual Network website". 

OVN-Kubernetes is a series of daemons for OVS that transform virtual network configurations into `OpenFlow` rules. `OpenFlow` is a protocol for communicating with network switches and routers, providing a means for remotely controlling the flow of network traffic on a network device. This means that network administrators can configure, manage, and monitor the flow of network traffic. 

OVN-Kubernetes provides more of the advanced functionality not available with `OpenFlow`. OVN supports distributed virtual routing, distributed logical switches, access control, Dynamic Host Configuration Protocol (DHCP), and DNS. OVN implements distributed virtual routing within logic flows that equate to open flows. For example, if you have a pod that sends out a DHCP request to the DHCP server on the network, a logic flow rule in the request enables the OVN-Kubernetes plugin to process the packet. This means that the server can respond with gateway, DNS server, IP address, and other information. 

OVN-Kubernetes runs a daemon on each node. There are daemon sets for the databases and for the OVN controller that run on every node. The OVN controller programs the Open vSwitch daemon on the nodes to support the following network provider features: 

  * Egress IPs 
  * Firewalls 
  * Hardware offloading 
  * Hybrid networking 
  * Internet Protocol Security (IPsec) encryption 
  * IPv6 
  * Multicast. 
  * Network policy and network policy logs 
  * Routers

- [1.1. OVN-Kubernetes purpose](01_01_ovn_kubernetes_purpose.md)
- [1.2. OVN-Kubernetes IPv6 and dual-stack limitations](01_02_ovn_kubernetes_ipv6_and_dual_stack_limitations.md)
- [1.3. Session affinity](01_03_session_affinity.md)
