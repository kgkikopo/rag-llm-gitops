# 2.1. Secondary networks in OpenShift Container Platform

OpenShift Container Platform provides the following CNI plugins for creating secondary networks in your cluster: 

  * **bridge** : To configure a bridge-based secondary network to allow pods on the same host to communicate with each other and the host, use the following procedure: 

    * [Configure a bridge-based secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-multus-bridge-object_configuring-additional-network-cni "4.2.1. Configuration for a bridge secondary network")

  * **bond-cni** : To provide a method for aggregating multiple network interfaces into a single logical _bonded_ interface, use the following procedure: 

    * [Configure a Bond CNI secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-multus-bond-cni-object_configuring-additional-network-cni "4.2.2. Configuration for a Bond CNI secondary network")

  * **host-device** : To allow pods access to a physical Ethernet network device on the host system, use the following procedure: 

    * [Configure a host-device secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-multus-host-device-object_configuring-additional-network-cni "4.2.3. Configuration for a host device secondary network")

  * **ipvlan** : Allow pods on a host to communicate with other hosts and pods on those hosts, similar to a macvlan-based secondary network. Unlike a macvlan-based secondary network, each pod shares the same MAC address as the parent physical network interface. Use the following procedure: 

    * [Configure an ipvlan-based secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-multus-ipvlan-object_configuring-additional-network-cni "4.2.6. Configuration for an IPVLAN secondary network")

  * **VLAN** : To allow VLAN-based network isolation and connectivity for pods, use the following procedure: 

    * [Configure a VLAN-based secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-multus-vlan-object_configuring-additional-network-cni "4.2.5. Configuration for a VLAN secondary network")

  * **macvlan** : To allow pods on a host to communicate with other hosts and pods on those hosts by using a physical network interface. Each pod that is attached to a macvlan-based secondary network is provided a unique MAC address: 

    * [Configure a macvlan-based secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-multus-macvlan-object_configuring-additional-network-cni "4.2.7. Configuration for a MACVLAN secondary network")

  * **TAP** : A TAP device enables user space programs to send and receive network packets. To create a TAP device inside the container namespace, use the following procedure: 

    * [Configure a TAP-based secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-multus-tap-object_configuring-additional-network-cni "4.2.8. Configuration for a TAP secondary network")

  * **SR-IOV** : To allow pods to attach to a virtual function (VF) interface on SR-IOV capable hardware on the host system. 

    * [Configure an SR-IOV based secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#about-sriov)

  * **route-override** : To allow pods to override and set routes, use the following procedure: 

    * [Configure a `route-override` based secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/multiple_networks/secondary-networks#nw-route-override-cni_configuring-additional-network-cni "4.2.10. Configure routes using the route-override plugin on a secondary network")
