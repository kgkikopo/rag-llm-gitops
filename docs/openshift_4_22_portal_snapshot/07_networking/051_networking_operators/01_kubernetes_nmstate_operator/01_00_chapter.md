# Chapter 1. Kubernetes NMState Operator

The Kubernetes NMState Operator provides a Kubernetes API for performing state-driven network configuration across the OpenShift Container Platform cluster nodes with NMState. 

The Kubernetes NMState Operator provides users with functionality to configure various network interface types, DNS, and routing on cluster nodes. Additionally, the daemons on the cluster nodes periodically report on the state of each node’s network interfaces to the API server. 

Important

Red Hat supports the Kubernetes NMState Operator in production environments on bare-metal, IBM Power®, IBM Z®, IBM® LinuxONE, VMware vSphere, and Red Hat OpenStack Platform (RHOSP) installations. 

Red Hat support exists for using the Kubernetes NMState Operator on Microsoft Azure but in a limited capacity. Support is limited to configuring DNS servers on your system as a postinstallation task. 

Before you can use NMState with OpenShift Container Platform, you must install the Kubernetes NMState Operator. After you install the Kubernetes NMState Operator, you can complete the following tasks: 

  * Observing and updating the node network state and configuration 
  * Creating a manifest object that includes a customized `br-ex` bridge 



Important

The Kubernetes NMState Operator updates the network configuration of a secondary NIC. Do not use the Operator to update the primary NIC network configuration or the `br-ex` bridge on most on-premise networks. Applying a `NodeNetworkConfigurationPolicy` CR to the primary NIC or `br-ex` bridge can result in complete network loss on the affected node. This configuration requires manual recovery of the network configuration. 

For a bare-metal platform only, the Kubernetes NMState Operator can update the `br-ex` bridge network configuration. This update is supported only if you set the `br-ex` bridge as the interface in a machine config manifest file. To update the `br-ex` bridge as a postinstallation task, you must set the `br-ex` bridge as the interface in the NMState configuration of the `NodeNetworkConfigurationPolicy` custom resource (CR) for your cluster. For more information, see "Creating a manifest object that includes a customized br-ex bridge (Post-installation documentation)". 

OpenShift Container Platform uses `nmstate` to report on and configure the state of the node network. You can modify the network policy configuration by applying a single configuration manifest to the cluster. For example, you can create a Linux bridge on all nodes. 

Node networking is monitored and updated by the following objects: 

`NodeNetworkState`
     Reports the state of the network on that node. 
`NodeNetworkConfigurationPolicy`
     Describes the requested network configuration on nodes. You update the node network configuration, including adding and removing interfaces, by applying a `NodeNetworkConfigurationPolicy` CR to the cluster. 
`NodeNetworkConfigurationEnactment`
     Reports the network policies enacted upon each node. 

Note

Do not make configuration changes to the `br-ex` bridge or its underlying interfaces as a postinstallation task.

- [1.1. Installing the Kubernetes NMState Operator](01_01_installing_the_kubernetes_nmstate_operator.md)
- [1.2. Uninstalling the Kubernetes NMState Operator](01_02_uninstalling_the_kubernetes_nmstate_operator.md)
- [1.3. Additional resources](01_03_additional_resources.md)
