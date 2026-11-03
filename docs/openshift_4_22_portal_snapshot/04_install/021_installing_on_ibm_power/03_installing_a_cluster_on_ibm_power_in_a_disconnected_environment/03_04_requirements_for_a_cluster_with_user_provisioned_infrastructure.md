# 3.4. Requirements for a cluster with user-provisioned infrastructure

For a OpenShift Container Platform cluster with user-provisioned infrastructure on IBM Power®, you must deploy all required machines meeting the hardware, network, DNS, and load balancing requirements. 

## 3.4.1. Required machines for cluster installation

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails. 

The smallest OpenShift Container Platform clusters require the following hosts: 

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines. 

Table 3.1. Minimum required hostsHosts| Description  
---|---  
One temporary bootstrap machine  |  The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster.   
Three control plane machines  |  The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane.   
At least two compute machines, which are also known as worker machines.  |  The workloads requested by OpenShift Container Platform users run on the compute machines.   
Show more

Important

To maintain high availability of your cluster, use separate physical hosts for these cluster machines. 

The bootstrap, control plane, and compute machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. 

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits). 

## 3.4.2. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 3.2. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
---|---|---|---|---|---  
Bootstrap  |  RHCOS  |  2  |  16 GB  |  100 GB  |  300   
Control plane  |  RHCOS  |  2  |  16 GB  |  100 GB  |  300   
Compute  |  RHCOS  |  2  |  8 GB  |  100 GB  |  300   
Show more

  * One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs. 
  * OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance. 



Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA): 

  * x86-64 architecture requires x86-64-v2 ISA 
  * ARM64 architecture requires ARMv8.0-A ISA 
  * ppc64le architecture requires IBM® Power9 ISA 
  * s390x architecture requires IBM® z14 ISA 



For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation. 

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform. 

**Additional resources**

  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)



## 3.4.3. Minimum IBM Power requirements

Before you install OpenShift Container Platform on IBM Power®, verify that your hardware meets the minimum system requirements for processor, disk storage, network, and memory. 

  * IBM Power®9, IBM Power®10 or IBM Power®11 processor-based systems 



### 3.4.3.1. Hardware requirements

  * Six logical partitions (LPARs) across multiple PowerVM servers 



### 3.4.3.2. Operating system requirements

  * One instance of an IBM Power®9, Power10 or Power11 processor-based system 



On your IBM Power® instance, set up: 

  * Three LPARs for OpenShift Container Platform control plane machines 
  * Two LPARs for OpenShift Container Platform compute machines 
  * One LPAR for the temporary OpenShift Container Platform bootstrap machine 



### 3.4.3.3. Disk storage for the IBM Power guest virtual machines

  * Local storage, or storage provisioned by the Virtual I/O Server using vSCSI, NPIV (N-Port ID Virtualization), Fibre Channel, multipath, or SSP (shared storage pools) 



### 3.4.3.4. Network for the PowerVM guest virtual machines

  * Dedicated physical adapter, or SR-IOV virtual function 
  * Available by the Virtual I/O Server using Shared Ethernet Adapter 
  * Virtualized by the Virtual I/O Server using IBM® virtual NIC (vNIC) 



### 3.4.3.5. Storage / main memory

  * 500 GB / 16 GB for OpenShift Container Platform control plane machines 
  * 500 GB / 8 GB for OpenShift Container Platform compute machines 
  * 500 GB / 16 GB for the temporary OpenShift Container Platform bootstrap machine 



## 3.4.4. Recommended IBM Power system requirements

OpenShift Container Platform on IBM Power® requires a minimum of six LPARs across multiple PowerVM servers, with specific hardware, storage, and network configuration for each node type. 

### 3.4.4.1. Hardware requirements

  * Six LPARs across multiple PowerVM servers 



### 3.4.4.2. Operating system requirements

  * One instance of an IBM Power®9, IBM Power®10 or IBM Power®11 processor-based system 



On your IBM Power® instance, set up: 

  * Three LPARs for OpenShift Container Platform control plane machines 
  * Two LPARs for OpenShift Container Platform compute machines 
  * One LPAR for the temporary OpenShift Container Platform bootstrap machine 



### 3.4.4.3. Disk storage for the IBM Power guest virtual machines

  * Local storage, or storage provisioned by the Virtual I/O Server using vSCSI, NPIV (N-Port ID Virtualization) or SSP (shared storage pools) 



### 3.4.4.4. Network for the PowerVM guest virtual machines

  * Dedicated physical adapter, or SR-IOV virtual function 
  * Virtualized by the Virtual I/O Server using Shared Ethernet Adapter 
  * Virtualized by the Virtual I/O Server using IBM® virtual NIC (vNIC) 



### 3.4.4.5. Storage / main memory

  * 120 GB / 32 GB for OpenShift Container Platform control plane machines 
  * 120 GB / 32 GB for OpenShift Container Platform compute machines 
  * 120 GB / 16 GB for the temporary OpenShift Container Platform bootstrap machine 



## 3.4.5. Certificate signing requests management

On user-provisioned infrastructure, you must implement a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management. 

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that kubelet credentials request because it cannot confirm that the correct machine issued the request. You must find and implement a method of verifying the validity of the kubelet serving certificate requests and approving them. 

## 3.4.6. Networking requirements for user-provisioned infrastructure

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files. 

During the initial boot, the machines require an IP address configuration that is set either through a DHCP server or statically by providing the required boot options. After a network connection is established, the machines download their Ignition config files from an HTTP or HTTPS server. The Ignition config files are then used to set the exact state of each machine. The Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation. 

Note

  * Consider using a DHCP server for long-term management of the cluster machines. Ensure that the DHCP server is configured to provide persistent IP addresses, DNS server information, and hostnames to the cluster machines. 
  * If a DHCP service is not available for your user-provisioned infrastructure, you can instead provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the _Installing RHCOS and starting the OpenShift Container Platform bootstrap process_ section for more information about static IP provisioning and advanced networking options. 



The Kubernetes API server must be able to resolve the node names of the cluster machines. If the API servers and worker nodes are in different zones, you can configure a default DNS search zone to allow the API server to resolve the node names. Another supported approach is to always refer to hosts by their fully-qualified domain names in both the node objects and all DNS requests. 

### 3.4.6.1. Setting the cluster node hostnames through DHCP

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start before this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node. 

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation. 

### 3.4.6.2. Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster. 

This section provides details about the ports that are required. 

Table 3.3. Ports used for all-machine to all-machine communicationsProtocol| Port| Description  
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

Table 3.4. Ports used for all-machine to control plane communicationsProtocol| Port| Description  
---|---|---  
TCP  |  `6443` |  Kubernetes API   
Show more

Table 3.5. Ports used for control plane machine to control plane machine communicationsProtocol| Port| Description  
---|---|---  
TCP  |  `2379`-`2380` |  etcd server and peer ports   
Show more

### 3.4.6.3. NTP configuration for user-provisioned infrastructure

OpenShift Container Platform clusters are configured to use a public Network Time Protocol (NTP) server by default. If you want to use a local enterprise NTP server, or if your cluster is being deployed in a disconnected network, you can configure the cluster to use a specific time server. For more information, see the documentation for _Configuring chrony time service_. 

If a DHCP server provides NTP server information, the chrony time service on the Red Hat Enterprise Linux CoreOS (RHCOS) machines read the information and can sync the clock with the NTP servers. 

**Additional resources**

  * [Configuring chrony time service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#installation-special-config-chrony_installing-customizing)



## 3.4.7. User-provisioned DNS requirements

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes. 

The following is a list of required cluster components: 

  * The Kubernetes API 
  * The OpenShift Container Platform application wildcard 
  * The bootstrap and control plane machines 
  * The compute machines 



Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines. 

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate. 

Note

It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the _DHCP recommendations for user-provisioned infrastructure_ section for more information. 

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`. 

Table 3.6. Required DNS recordsComponent| Record| Description  
---|---|---  
Kubernetes API  |  `api.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
`api-int.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.  Important The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods.   
Routes  |  `*.apps.<cluster_name>.<base_domain>.` |  A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console.   
Bootstrap machine  |  `bootstrap.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap machine. These records must be resolvable by the nodes within the cluster.   
Control plane machines  |  `<control_plane><n>.<cluster_name>.<base_domain>.` |  DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster.   
Compute machines  |  `<compute><n>.<cluster_name>.<base_domain>.` |  DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster.   
Show more

Note

In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration. 

Tip

You can use the `dig` command to verify name and reverse name resolution. See the section on _Validating DNS resolution for user-provisioned infrastructure_ for detailed validation steps. 

### 3.4.7.1. Example DNS configuration for user-provisioned clusters

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure. 

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another. 

In the examples, the cluster name is `ocp4` and the base domain is `example.com`. 

The following example is a BIND zone file that shows sample DNS A records for name resolution in a user-provisioned cluster. 

Note

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

```plaintext
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
	IN	MX 10	smtp.example.com.
;
;
ns1.example.com.		IN	A	192.168.1.5
smtp.example.com.		IN	A	192.168.1.5
;
helper.example.com.		IN	A	192.168.1.5
helper.ocp4.example.com.	IN	A	192.168.1.5
;
api.ocp4.example.com.		IN	A	192.168.1.5
api-int.ocp4.example.com.	IN	A	192.168.1.5
;
*.apps.ocp4.example.com.	IN	A	192.168.1.5
;
bootstrap.ocp4.example.com.	IN	A	192.168.1.96
;
control-plane0.ocp4.example.com.	IN	A	192.168.1.97
control-plane1.ocp4.example.com.	IN	A	192.168.1.98
;
control-plane2.ocp4.example.com.	IN	A	192.168.1.99
;
compute0.ocp4.example.com.	IN	A	192.168.1.11
compute1.ocp4.example.com.	IN	A	192.168.1.7
;
;EOF
```


where: 

`api.ocp4.example.com.`
     Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer. 
`api-int.ocp4.example.com.`
     Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications. 
`*.apps.ocp4.example.com.`
     Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. 
`bootstrap.ocp4.example.com`
     Provides name resolution for the bootstrap machine. 
`control-plane0.ocp4.example.com`
     Provides name resolution for the control plane machines. 
`compute0.ocp4.example.com.`
     Provides name resolution for the compute machines. 

The following example BIND zone file shows sample PTR records for reverse name resolution in a user-provisioned cluster: 

```plaintext
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
;
5.1.168.192.in-addr.arpa.	IN	PTR	api.ocp4.example.com.
5.1.168.192.in-addr.arpa.	IN	PTR	api-int.ocp4.example.com.
;
96.1.168.192.in-addr.arpa.	IN	PTR	bootstrap.ocp4.example.com.
;
97.1.168.192.in-addr.arpa.	IN	PTR	control-plane0.ocp4.example.com.
98.1.168.192.in-addr.arpa.	IN	PTR	control-plane1.ocp4.example.com.
;
99.1.168.192.in-addr.arpa.	IN	PTR	control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	compute1.ocp4.example.com.
;
;EOF
```


where: 

`api.ocp4.example.com.`
     Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer. 
`api-int.ocp4.example.com.`
     Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications. 
`bootstrap.ocp4.example.com.`
     Provides reverse DNS resolution for the bootstrap machine. 
`control-plane0.ocp4.example.com.`
     Provides reverse DNS resolution for the control plane machines. 
`compute0.ocp4.example.com.`
     Provides reverse DNS resolution for the compute machines. 

Note

A PTR record is not required for the OpenShift Container Platform application wildcard. 

## 3.4.8. Load balancing requirements for user-provisioned infrastructure

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

Note

If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately. 

The load balancing infrastructure must meet the following requirements: 

  * API load balancer: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions: 

    * Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode. 
    * A stateless load balancing algorithm. The options vary based on the load balancer implementation. 




Important

Do not configure session persistence for an API load balancer. Configuring session persistence for a Kubernetes API server might cause performance issues from excess application traffic for your OpenShift Container Platform cluster and the Kubernetes API that runs inside the cluster. 

Configure the following ports on both the front and back of the API load balancers: 

Port| Back-end machines (pool members)| Internal| External| Description  
---|---|---|---|---  
`6443` |  Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. You must configure the `/readyz` endpoint for the API server health check probe.  |  X  |  X  |  Kubernetes API server   
`22623` |  Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane.  |  X  |  |  Machine config server   
Show more

Note

The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values. 

  * Application Ingress load balancer: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. Configure the following conditions: 

    * Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode. 
    * A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform. 




Tip

If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption. 

Configure the following ports on both the front and back of the load balancers: 

Table 3.7. Application Ingress load balancerPort| Back-end machines (pool members)| Internal| External| Description  
---|---|---|---|---  
`443` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTPS traffic   
`80` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTP traffic   
Show more

Note

If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. 

### 3.4.8.1. Example load balancer configuration for user-provisioned clusters

Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters. 

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another. 

Tip

If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node. 

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

Note

If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`. 

**Sample API and application Ingress load balancer configuration**

```plaintext
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
```


where: 

`listen api-server-6443`
     Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic. 
`server bootstrap bootstrap.ocp4.example.com`
     The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete. 
`listen machine-config-server`
     Port `22623` handles the machine config server traffic and points to the control plane machines. 
`listen ingress-router-443`
     Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. 
`listen ingress-router-80`
    

Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. 

Note

If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
