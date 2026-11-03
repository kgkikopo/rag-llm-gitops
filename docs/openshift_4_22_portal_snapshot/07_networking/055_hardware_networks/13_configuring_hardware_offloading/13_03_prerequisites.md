# 13.3. Prerequisites

Before you configure hardware offloading, ensure that the following conditions are met. 

  * Your cluster has at least one bare-metal machine with a network interface controller that is supported for hardware offloading. 
  * You installed the SR-IOV Network Operator. 
  * Your cluster uses the OVN-Kubernetes network plugin. 
  * In your OVN-Kubernetes network plugin configuration, the `gatewayConfig.routingViaHost` field is set to `false`. 



**Additional resources**

  * [Installing the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator)
  * [About the OVN-Kubernetes network plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#about-ovn-kubernetes)
  * [OVN-Kubernetes network plugin configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#gatewayConfig-object_cluster-network-operator)
