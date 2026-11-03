# Chapter 6. Assigning a secondary network to a VRF

As a cluster administrator, you can configure a secondary network for a virtual routing and forwarding (VRF) domain by using the CNI VRF plugin. The virtual network that this plugin creates is associated with the physical interface that you specify. 

Using a secondary network with a VRF instance has the following advantages: 

Workload isolation
     Isolate workload traffic by configuring a VRF instance for the secondary network. 
Improved security
     Enable improved security through isolated network paths in the VRF domain. 
Multi-tenancy support
     Support multi-tenancy through network segmentation with a unique routing table in the VRF domain for each tenant. 

Note

Applications that use VRFs must bind to a specific device. The common usage is to use the `SO_BINDTODEVICE` option for a socket. The `SO_BINDTODEVICE` option binds the socket to the device that is specified in the passed interface name, for example, `eth1`. To use the `SO_BINDTODEVICE` option, the application must have `CAP_NET_RAW` capabilities. 

Using a VRF through the `ip vrf exec` command is not supported in OpenShift Container Platform pods. To use VRF, bind applications directly to the VRF interface. 

**Additional resources**

  * [About virtual routing and forwarding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/virtual-routing-and-forwarding#cnf-about-virtual-routing-and-forwarding_about-virtual-routing-and-forwarding "5.1. About virtual routing and forwarding")

- [6.1. Create a secondary network attachment with the CNI VRF plugin](06_01_create_a_secondary_network_attachment_with_the_cni_vrf_plugin.md)
