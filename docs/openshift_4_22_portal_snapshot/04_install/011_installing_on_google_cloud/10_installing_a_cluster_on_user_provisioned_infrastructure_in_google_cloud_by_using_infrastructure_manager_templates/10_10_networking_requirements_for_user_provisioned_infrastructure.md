# 10.10. Networking requirements for user-provisioned infrastructure

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files. 

## 10.10.1. Setting the cluster node hostnames through DHCP

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start before this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node. 

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation. 

## 10.10.2. Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster. 

This section provides details about the ports that are required. 

Important

In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat. 

Table 10.7. Ports used for all-machine to all-machine communicationsProtocol| Port| Description  
---|---|---  
ICMP  |  N/A  |  Network reachability tests   
TCP  |  `1936` |  Metrics   
`9000`-`9999` |  Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`.   
`10250`-`10259` |  The default ports that Kubernetes reserves   
`22623` |  The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines.   
UDP  |  `6081` |  Geneve   
`9000`-`9999` |  Host level services, including the node exporter on ports `9100`-`9101`.   
`500` |  IPsec IKE packets   
`4500` |  IPsec NAT-T packets   
`123` |  Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`.   
TCP/UDP  |  `30000`-`32767` |  Kubernetes node port   
ESP  |  N/A  |  IPsec Encapsulating Security Payload (ESP)   
Show more

Table 10.8. Ports used for all-machine to control plane communicationsProtocol| Port| Description  
---|---|---  
TCP  |  `6443` |  Kubernetes API   
Show more

Table 10.9. Ports used for control plane machine to control plane machine communicationsProtocol| Port| Description  
---|---|---  
TCP  |  `2379`-`2380` |  etcd server and peer ports   
Show more
