# Chapter 15. Tracking network flows

As a cluster administrator, you can collect information about pod network flows from your cluster to assist with the following areas: 

  * Monitor ingress and egress traffic on the pod network. 
  * Troubleshoot performance issues. 
  * Gather data for capacity planning and security audits. 



When you enable the collection of the network flows, only the metadata about the traffic is collected. For example, packet data is not collected, but the protocol, source address, destination address, port numbers, number of bytes, and other packet-level information is collected. 

The data is collected in one or more of the following record formats: 

  * NetFlow 
  * sFlow 
  * IPFIX 



When you configure the Cluster Network Operator (CNO) with one or more collector IP addresses and port numbers, the Operator configures Open vSwitch (OVS) on each node to send the network flows records to each collector. 

You can configure the Operator to send records to more than one type of network flow collector. For example, you can send records to NetFlow collectors and also send records to sFlow collectors. 

When OVS sends data to the collectors, each type of collector receives identical records. For example, if you configure two NetFlow collectors, OVS on a node sends identical records to the two collectors. If you also configure two sFlow collectors, the two sFlow collectors receive identical records. However, each collector type has a unique record format. 

Collecting the network flows data and sending the records to collectors affects performance. Nodes process packets at a slower rate. If the performance impact is too great, you can delete the destinations for collectors to disable collecting network flows data and restore performance. 

Note

Enabling network flow collectors might have an impact on the overall performance of the cluster network.

- [15.1. Network object configuration for tracking network flows](15_01_network_object_configuration_for_tracking_network_flows.md)
- [15.2. Adding destinations for network flows collectors](15_02_adding_destinations_for_network_flows_collectors.md)
- [15.3. Deleting all destinations for network flows collectors](15_03_deleting_all_destinations_for_network_flows_collectors.md)
- [15.4. Additional resources](15_04_additional_resources.md)
