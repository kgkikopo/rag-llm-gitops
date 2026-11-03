# 13.1. About multicast

With IP multicast in OpenShift Container Platform, data is broadcast to many IP addresses simultaneously. With OVN-Kubernetes, multicast is off by default and is not affected by network policies when you enable it in a project. 

Important

  * At this time, multicast is best used for low-bandwidth coordination or service discovery and not a high-bandwidth solution. 
  * By default, network policies affect all connections in a namespace. However, multicast is unaffected by network policies. If multicast is enabled in the same namespace as your network policies, it is always allowed, even if there is a `deny-all` network policy. 
  * Cluster administrators must consider the implications of the exemption of multicast from network policies before enabling it. 



Multicast traffic between OpenShift Container Platform pods is disabled by default. If you are using the OVN-Kubernetes network plugin, you can enable multicast on a per-project basis.
