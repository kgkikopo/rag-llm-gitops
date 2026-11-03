# 2.3. Network requirements

Virtualized control plane deployments require specific network connectivity between VMs, worker nodes, and external services. 

Configure networking to meet the following requirements: 

  * L2 network connectivity between control plane VMs. The OpenShift Container Platform installation program requires all control plane nodes to share the same L2 network segment. 
  * L3 connectivity without network address translation (NAT) between the control plane VMs and worker nodes. Worker nodes must be able to route traffic directly to the control plane VMs. During installation, the bootstrap VM also requires L3 connectivity to the control plane. 
  * External access to the cluster API. 
  * Access to container image registries. 
  * DNS resolution for cluster components. 



You can use either dynamic or static IP addressing for the control plane VMs: 

  * For deployments that use DHCP, configure static MAC addresses on the primary network interfaces of the VMs and create DHCP reservations for each MAC address. This ensures consistent IP assignment across VM restarts. 
  * For deployments that use static IP addressing, define the network configuration in your `install-config.yaml` or Agent-based installation manifests.
