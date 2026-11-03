# Chapter 4. CIDR range definitions

If your cluster uses OVN-Kubernetes, you must specify non-overlapping ranges for Classless Inter-Domain Routing (CIDR) subnet ranges. 

Important

For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` for IPv4 and `fd69::/112` for IPv6 as the default masquerade subnet. You must avoid these ranges. For upgraded clusters, there is no change to the default masquerade subnet. 

Tip

You can use the [Red Hat OpenShift Network Calculator](https://access.redhat.com/labs/ocpnc/) to decide your networking needs before setting CIDR range during cluster creation. 

You must have a Red Hat account to use the calculator. 

The following subnet types are mandatory for a cluster that uses OVN-Kubernetes: 

  * Join: Uses a join switch to connect gateway routers to distributed routers. A join switch reduces the number of IP addresses for a distributed router. For a cluster that uses the OVN-Kubernetes plugin, an IP address from a dedicated subnet is assigned to any logical port that attaches to the join switch. 
  * Masquerade: Prevents collisions for identical source and destination IP addresses that are sent from a node as hairpin traffic to the same node after a load balancer makes a routing decision. 
  * Transit: A transit switch is a type of distributed switch that spans across all nodes in the cluster. A transit switch routes traffic between different zones. For a cluster that uses the OVN-Kubernetes plugin, an IP address from a dedicated subnet is assigned to any logical port that attaches to the transit switch. 



Note

You can change the join, masquerade, and transit CIDR ranges for your cluster as a postinstallation task. 

OVN-Kubernetes, the default network provider in OpenShift Container Platform 4.14 and later versions, internally uses the following IP address subnet ranges: 

  * `V4JoinSubnet`: `100.64.0.0/16`
  * `V6JoinSubnet`: `fd98::/64`
  * `V4TransitSwitchSubnet`: `100.88.0.0/16`
  * `V6TransitSwitchSubnet`: `fd97::/64`
  * `defaultV4MasqueradeSubnet`: `169.254.0.0/17`
  * `defaultV6MasqueradeSubnet`: `fd69::/112`



Important

The earlier list includes join, transit, and masquerade IPv4 and IPv6 address subnets. If your cluster uses OVN-Kubernetes, do not include any of these IP address subnet ranges in any other CIDR definitions in your cluster or infrastructure. 

**Additional resources**

  * [Configuring OVN-Kubernetes internal IP address subnets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#configure-ovn-kubernetes-subnets)

- [4.1. Machine CIDR](04_01_machine_cidr.md)
- [4.2. Service classless inter-domain routing (CIDR)](04_02_service_classless_inter_domain_routing_cidr.md)
- [4.3. Pod classless inter-domain routing (CIDR)](04_03_pod_classless_inter_domain_routing_cidr.md)
- [4.4. Host prefix](04_04_host_prefix.md)
- [4.5. CIDR ranges for hosted control planes](04_05_cidr_ranges_for_hosted_control_planes.md)
