# Chapter 12. Using pod-level bonding

Bonding at the pod level is vital to enable workloads inside pods that require high availability and more throughput. With pod-level bonding, you can create a bond interface from multiple single root I/O virtualization (SR-IOV) virtual function interfaces in a kernel mode interface. The SR-IOV virtual functions are passed into the pod and attached to a kernel driver. 

One scenario where pod level bonding is required is creating a bond interface from multiple SR-IOV virtual functions on different physical functions. Creating a bond interface from two different physical functions on the host can be used to achieve high availability and throughput at pod level. 

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator). 

For guidance on tasks such as creating a SR-IOV network, network policies, network attachment definitions and pods, see [Configuring an SR-IOV network device](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hardware_networks/configuring-sriov-device "Chapter 2. Configuring an SR-IOV network device").

- [12.1. Configure a bond interface from two SR-IOV interfaces](12_01_configure_a_bond_interface_from_two_sr_iov_interfaces.md)
- [12.2. Create a bond network attachment definition](12_02_create_a_bond_network_attachment_definition.md)
- [12.3. Create a pod using a bond interface](12_03_create_a_pod_using_a_bond_interface.md)
