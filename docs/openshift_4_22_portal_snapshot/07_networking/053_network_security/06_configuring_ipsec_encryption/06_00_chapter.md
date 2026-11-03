# Chapter 6. Configuring IPsec encryption

By enabling IPsec, you can encrypt both internal pod-to-pod cluster traffic between nodes and external traffic between pods and IPsec endpoints external to your cluster. All pod-to-pod network traffic between nodes on the OVN-Kubernetes cluster network is encrypted with IPsec in _Transport mode_. 

IPsec is disabled by default. You can enable IPsec either during or after installing the cluster. For information about cluster installation, see [OpenShift Container Platform installation overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#ocp-installation-overview). 

Note

Upgrading your cluster to OpenShift Container Platform 4.22 when the `libreswan` and `NetworkManager-libreswan` packages have different OpenShift Container Platform versions causes two consecutive compute node reboot operations. For the first reboot, the Cluster Network Operator (CNO) applies the IPsec configuration to compute nodes. For the second reboot, the Machine Config Operator (MCO) applies the latest machine configs to the cluster. 

To combine the CNO and MCO updates into a single node reboot, complete the following tasks: 

  * Before upgrading your cluster, set the `paused` parameter to `true` in the `MachineConfigPools` custom resource (CR) that groups compute nodes. 
  * After you upgrade your cluster, set the parameter to `false`. 



For more information, see [Performing a Control Plane Only update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#control-plane-only-update). 

The following support limitations exist for IPsec on a OpenShift Container Platform cluster: 

  * On IBM Cloud®, IPsec supports only network address translation-traversal (NAT-T). Encapsulating Security Payload (ESP) is not supported on this platform. 
  * If your cluster uses [hosted control planes](https://www.redhat.com/en/topics/containers/what-are-hosted-control-planes) for Red Hat OpenShift Container Platform, IPsec is not supported for IPsec encryption of either pod-to-pod or traffic to external hosts. 
  * Using ESP hardware offloading on any network interface is not supported if one or more of those interfaces is attached to Open vSwitch (OVS). Enabling IPsec for your cluster triggers the use of IPsec with interfaces attached to OVS. By default, OpenShift Container Platform disables ESP hardware offloading on any interfaces attached to OVS. 
  * If you enabled IPsec for network interfaces that are not attached to OVS, a cluster administrator must manually disable ESP hardware offloading on each interface that is not attached to OVS. 



The following list outlines key tasks in the IPsec documentation: 

  * Enable and disable IPsec after cluster installation. 
  * Configure IPsec encryption for traffic between the cluster and external hosts. 
  * Verify that IPsec encrypts traffic between pods on different nodes.

- [6.1. Modes of operation](06_01_modes_of_operation.md)
- [6.2. Prerequisites for IPsec encryption for external traffic](06_02_prerequisites_for_ipsec_encryption_for_external_traffic.md)
- [6.3. Additional resources](06_03_additional_resources.md)
- [6.4. Network connectivity requirements when IPsec is enabled](06_04_network_connectivity_requirements_when_ipsec_is_enabled.md)
- [6.5. IPsec encryption for pod-to-pod traffic](06_05_ipsec_encryption_for_pod_to_pod_traffic.md)
- [6.6. IPsec encryption for external traffic](06_06_ipsec_encryption_for_external_traffic.md)
- [6.7. Enable IPsec encryption](06_07_enable_ipsec_encryption.md)
- [6.8. Configure IPsec encryption for external traffic](06_08_configure_ipsec_encryption_for_external_traffic.md)
- [6.9. Additional resources](06_09_additional_resources.md)
- [6.10. Disable IPsec encryption for an external IPsec endpoint](06_10_disable_ipsec_encryption_for_an_external_ipsec_endpoint.md)
- [6.11. Disable IPsec encryption](06_11_disable_ipsec_encryption.md)
- [6.12. Additional resources](06_12_additional_resources.md)
