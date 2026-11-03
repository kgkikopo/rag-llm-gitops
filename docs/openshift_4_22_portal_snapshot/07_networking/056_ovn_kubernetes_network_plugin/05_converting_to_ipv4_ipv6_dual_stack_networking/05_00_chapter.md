# Chapter 5. Converting to IPv4/IPv6 dual-stack networking

To enable IPv4 and IPv6 on your cluster network in OpenShift Container Platform, you can convert a single-stack cluster to dual-stack networking. After conversion, new and existing pods can use both address families when you re-create workloads as needed. 

Important

When using dual-stack networking where IPv6 is required, you cannot use IPv4-mapped IPv6 addresses, such as `::FFFF:198.51.100.1`. 

**Additional resources**

  * [OVN-Kubernetes purpose](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ovn-kubernetes_network_plugin/about-ovn-kubernetes#nw-ovn-kubernetes-purpose_about-ovn-kubernetes "1.1. OVN-Kubernetes purpose")

- [5.1. Convert to a dual-stack cluster network](05_01_convert_to_a_dual_stack_cluster_network.md)
- [5.2. Convert to a single-stack cluster network](05_02_convert_to_a_single_stack_cluster_network.md)
