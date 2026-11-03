# 14.1. Networking overview for hosted control planes

Proper network design can ensure the performance, automation, and security of hosted control planes. Your network configuration depends on the segmentation that you need and the provider that you use, such as a cloud provider, bare metal on the Agent platform, or OpenShift Virtualization. 

For example, for hosted control planes on OpenShift Virtualization, you can create `NodePool` virtual machines (VMs) with different network configurations, including using the pod network and bridging an external network into the VMs. Network latency and throughput are important factors to ensure control-plane communication, workload traffic, and storage access. The use of dedicated physical network adapters can ensure adequate throughput and low latency for all components. 

## 14.1.1. Control plane and data plane networking considerations

When you consider your networking configuration for hosted control planes, remember the structure of the control plane and data plane: 

Control plane
    

The control plane includes pods that run on the management cluster in a dedicated namespace. The pods expose the hosted control plane `kube-apiserver` component, OAuth, Ignition server, and Konnectivity service. Hosted cluster nodes access those services through the data plane network, so the services must be reachable from the data plane network, even if a firewall is in place. 

The management cluster hosts different control planes, and their services are exposed through its network. Network segmentation by API is not currently supported. 

Data plane
    

The data plane includes the compute, storage, and networking where workloads and applications run. It has a minimum of 2 compute nodes. 

For example, the data plane includes compute nodes that are represented by bare-metal servers or VMs that are hosted on OpenShift Virtualization. For OpenShift Virtualization, you can host different data planes on the management cluster. For bare-metal servers or an external OpenShift Virtualization cluster, you can host data planes by external infrastructure. 

Some VLAN-based network segmentation is possible if the following conditions are true: 

  * All of the configured VLANs can route traffic to the endpoints of the API, OAuth, Ignition server, and Konnectivity service. 
  * Hosted cluster users can access the API and OAuth. 



The node pools in hosted clusters on the data plane depend on the components that run on the control plane, such as Konnectivity, Ignition, and OAuth. By default, you install those components by using a `Route` endpoint publishing strategy, and admit them on the default ingress controller, which is often installed on primary networks from the management cluster. To segment this implementation on a secondary network, you must change several network flows between the control plane and the data plane. 

## 14.1.2. DHCP requirements for hosted control planes

The requirements for Dynamic Host Configuration Protocol (DHCP) differ depending on your platform provider: 

  * For bare metal providers, you can use dynamic or manual IP segmentation, so a DHCP server is not mandatory. Ensure that the same node always has the same IP address. 
  * For OpenShift Virtualization, dynamic IP assignment is the only option, so a DHCP server is mandatory.
