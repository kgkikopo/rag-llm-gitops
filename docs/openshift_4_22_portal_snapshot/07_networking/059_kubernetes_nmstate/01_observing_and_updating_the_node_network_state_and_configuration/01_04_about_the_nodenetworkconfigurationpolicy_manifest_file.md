# 1.4. About the NodeNetworkConfigurationPolicy manifest file

A `NodeNetworkConfigurationPolicy` manifest file defines policies that the Kubernetes NMState Operator uses to configure networking for nodes in your OpenShift Container Platform cluster. You can create, edit, and delete these policies to manage node network configurations. 

Important

If you want to apply multiple NNCP CRs to a node, you must create the NNCPs in a logical order that is based on the alphanumeric sorting of the policy names. The Kubernetes NMState Operator continuously checks for a newly created NNCP CR so that the Operator can instantly apply the CR to node. Consider the following logical order issue example: 

  1. You create NNCP 1 for defining the bridge interface that listens on a VLAN port, such as `eth1.1000`. 
  2. You create NNCP 2 for defining the VLAN interface and specify the port for this interface, such as `eth1.1000`. 
  3. You apply NNCP 1 before you apply NNCP 2 to the node. 



The node experiences a node connectivity issue because port `eth1.1000` does not exist. As a result, the cluster fails. 

After you apply a node network policy to a node, the Kubernetes NMState Operator configures the networking configuration for nodes according to the node network policy details. 

Warning

The following list of interface names are reserved and you cannot use the names with NMstate configurations: 

  * `br-ext`
  * `br-int`
  * `br-local`
  * `br-nexthop`
  * `br0`
  * `ext-vxlan`
  * `ext`
  * `genev_sys_*`
  * `int`
  * `k8s-*`
  * `ovn-k8s-*`
  * `patch-br-*`
  * `tun0`
  * `vxlan_sys_*`



You can create an NNCP by using either the OpenShift CLI (`oc`) or the OpenShift Container Platform web console. As a postinstallation task you can create an NNCP or edit an existing NNCP. 

Note

Before you create an NNCP, ensure that you read the "Example policy configurations for different interfaces" document. 

If you want to delete an NNCP, you can use the `oc delete nncp` command to complete this action. However, this command does not delete any objects, such as a bridge interface. 

Deleting the node network policy that added an interface to a node does not change the configuration of the policy on the node. Similarly, removing an interface does not delete the policy, because the Kubernetes NMState Operator re-adds the removed interface whenever a pod or a node is restarted. 

To effectively delete the NNCP, the node network policy, and any interfaces would typically require the following actions: 

  1. Edit the NNCP and remove interface details from the file. Ensure that you do not remove `name`, `state`, and `type` parameters from the file. 
  2. Add `state: absent` under the `interfaces.state` section of the NNCP. 
  3. Run `oc apply -f <nncp_file_name>`. After the Kubernetes NMState Operator applies the node network policy to each node in your cluster, any interface that exists on each node is now marked as _absent_. 
  4. Run `oc delete nncp` to delete the NNCP. 



**Additional resources**

  * [Example policy configurations for different interfaces](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/kubernetes_nmstate/k8s-nmstate-updating-node-network-config#virt-nmstate-example-policy-configurations_k8s-nmstate-updating-node-network-config "1.9. Example policy configurations for different interfaces")
  * [Removing an interface from nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/kubernetes_nmstate/k8s-nmstate-updating-node-network-config#virt-removing-interface-from-nodes_k8s-nmstate-updating-node-network-config "1.7.3. Remove an interface from nodes")
