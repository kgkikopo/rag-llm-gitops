# 8.1. About 802.1Q-in-802.1Q support

In traditional VLAN setups, frames contain a single VLAN tag and metadata such as Quality of Service (QoS). QinQ uses double VLAN tagging: an outer tag for the service provider and an inner tag for the customer VLAN, which enables finer traffic segmentation over a shared network. 

QinQ facilitates the creation of nested VLANs by using double VLAN tagging, enabling finer segmentation and isolation of traffic within a network environment. This approach is particularly valuable in service provider networks where you need to deliver VLAN-based services to multiple customers over a common infrastructure, while ensuring separation and isolation of traffic. 

The following diagram illustrates how OpenShift Container Platform can use SR-IOV and QinQ to achieve advanced network segmentation and isolation for containerized workloads. 

The diagram shows how double VLAN tagging (QinQ) works in a worker node with SR-IOV support. The SR-IOV virtual function (VF) located in the pod namespace, `ext0` is configured by the SR-IOV Container Network Interface (CNI) with a VLAN ID and VLAN protocol. This corresponds to the S-tag. Inside the pod, the VLAN CNI creates a subinterface using the primary interface `ext0`. This subinterface adds an internal VLAN ID using the 802.1Q protocol, which corresponds to the C-tag. 

This demonstrates how QinQ enables finer traffic segmentation and isolation within the network. The Ethernet frame structure is detailed on the right, highlighting the inclusion of both VLAN tags, EtherType, IP, TCP, and Payload sections. QinQ facilitates the delivery of VLAN-based services to multiple customers over a shared infrastructure while ensuring traffic separation and isolation. 

![Diagram showing QinQ \(double VLAN tagging\)](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hardware_networks-en-US/images/5050784ae325a100faa8d7b2192a2439/693_OpenShift_QinQ_SR-IOV_CNI_0624.png) ![Diagram showing QinQ \(double VLAN tagging\)](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hardware_networks-en-US/images/5050784ae325a100faa8d7b2192a2439/693_OpenShift_QinQ_SR-IOV_CNI_0624.png)

The OpenShift Container Platform SR-IOV solution already supports setting the VLAN protocol on the `SriovNetwork` custom resource (CR). The virtual function (VF) can use this protocol to set the VLAN tag, also known as the outer tag. Pods can then use the VLAN CNI plugin to configure the inner tag. 

**Additional resources**

  * [Configuration for an VLAN additional network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#nw-multus-vlan-object_configuring-additional-network-cni)
