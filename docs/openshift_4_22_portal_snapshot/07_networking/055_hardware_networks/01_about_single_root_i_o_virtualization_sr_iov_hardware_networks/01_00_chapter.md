# Chapter 1. About Single Root I/O Virtualization (SR-IOV) hardware networks

To share a single physical device with multiple pods, implement the Single Root I/O Virtualization (SR-IOV) specification. This standard enables flexible PCI device assignment, allowing a device to show as multiple separate physical devices for efficient resource allocation. 

Note

As of OpenShift Container Platform 4.21, the SR-IOV Operator can support ARM hardware. 

You can configure a Single Root I/O Virtualization (SR-IOV) device in your cluster by using the [SR-IOV Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator). 

SR-IOV can segment a compliant network device, recognized on the host node as a physical function (PF), into multiple virtual functions (VFs). The VF is used like any other network device. The SR-IOV network device driver for the device determines how the VF is exposed in the container: 

  * `netdevice` driver: A regular kernel network device in the `netns` of the container 
  * `vfio-pci` driver: A character device mounted in the container 



You can use SR-IOV network devices with additional networks on your OpenShift Container Platform cluster installed on bare metal or Red Hat OpenStack Platform (RHOSP) infrastructure for applications that require high bandwidth or low latency. 

The SR-IOV Network Operator is supported on the following platforms: 

  * Bare metal 
  * Red Hat OpenStack Platform (RHOSP) 



Note

For a list of devices, such as network interface controllers (NICs) that OpenShift Container Platform supports, see [Red Hat certified hardware](https://catalog.redhat.com/en/hardware) on the Red Hat Ecosystem Catalog. The following example, finds the Intel X710 network adapter: 

  1. From the Red Hat certified hardware webpage, click **Explore** from the **Components** tile. 
  2. From the **Provider** drop-down menu, click the **Intel Corporation** checkbox. 
  3. From the **Platform** drop-down menu, click the **Red Hat OpenShift Container Platform** checkbox. 
  4. Find the **Intel® Ethernet Server Adapter X710** network adapter from the list and then click on its tile. A new webpage opens that shows information for the network adapter. 



You can configure multi-network policies for SR-IOV networks. The support for this is technology preview and SR-IOV additional networks are only supported with kernel NICs. They are not supported for Data Plane Development Kit (DPDK) applications. 

Note

Creating multi-network policies on SR-IOV networks might not deliver the same performance to applications compared to SR-IOV networks without a multi-network policy configured. 

Important

Multi-network policies for SR-IOV network is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

You can enable SR-IOV on a node by using the following command: 

```shell-session
$ oc label node <node_name> feature.node.kubernetes.io/network-sriov.capable="true"
```

- [1.1. Additional resources](01_01_additional_resources.md)
- [1.2. Components that manage SR-IOV network devices](01_02_components_that_manage_sr_iov_network_devices.md)
- [1.3. Additional resources](01_03_additional_resources.md)
- [1.4. Next steps](01_04_next_steps.md)
