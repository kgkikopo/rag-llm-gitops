# Chapter 1. Understanding virtualized control planes

A virtualized control plane deployment is an OpenShift Container Platform cluster whose control plane nodes run as virtual machines (VMs) on a hosting cluster with OpenShift Virtualization. 

Important

KubeVirt Redfish is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

This architecture is useful in the following example scenarios: 

  * Regulatory requirements mandate VM-level isolation for control plane components. 
  * You want to reduce hardware costs by consolidating multiple cluster control planes on shared infrastructure. 
  * You need faster provisioning of new clusters compared to physical bare metal. 



In a virtualized control plane deployment, you have two clusters: 

Hosting cluster
     An existing OpenShift Container Platform cluster running OpenShift Virtualization that hosts the control plane VMs. 
Target cluster
     The OpenShift Container Platform cluster with control planes running on the VMs. 

KubeVirt Redfish runs on the hosting cluster and exposes the VMs through the standard Redfish API endpoints. 

With this approach, you can use installation workflows such as Agent-based Installer or GitOps Zero Touch Provisioning (ZTP), to deploy virtualized control planes exactly like physical servers with baseboard management controllers (BMCs). 

Note

Virtualized control planes differ from Hosted control planes. With virtualized control planes, the control plane runs as VMs with hypervisor-level isolation. With Hosted control planes, the control plane runs as pods with container-level isolation.

- [1.1. Virtualized control plane architecture](01_01_virtualized_control_plane_architecture.md)
- [1.2. Virtualized control plane deployment workflow](01_02_virtualized_control_plane_deployment_workflow.md)
- [1.3. Additional resources](01_03_additional_resources.md)
