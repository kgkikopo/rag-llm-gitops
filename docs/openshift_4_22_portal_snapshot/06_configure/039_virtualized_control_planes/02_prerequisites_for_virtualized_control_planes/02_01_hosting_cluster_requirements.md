# 2.1. Hosting cluster requirements

The hosting cluster runs the virtualized control plane VMs and manages their lifecycle through KubeVirt Redfish. 

The hosting cluster requires the following components: 

  * OpenShift Container Platform installed and operational. 
  * OpenShift Virtualization installed and configured. 
  * Sufficient compute resources to host control plane VMs. 
  * At least three physical nodes to enable anti-affinity placement, ensuring control plane VMs are spread across different physical hosts.
