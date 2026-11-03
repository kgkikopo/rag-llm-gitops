# 14.3. Firewall, port, and service requirements for hosted control planes

Ensure that you meet the firewall, port, and service requirements so that ports can communicate between the management cluster, the control plane, and hosted clusters. 

## 14.3.1. Bare metal firewall, port, and service requirements

You must meet the firewall, port, and service requirements so that ports can communicate between the management cluster, the control plane, and hosted clusters. 

Note

Services run on their default ports. However, if you use the `NodePort` publishing strategy, services run on the port that is assigned by the `NodePort` service. 

Use firewall rules, security groups, or other access controls to restrict access to only required sources. Avoid exposing ports publicly unless necessary. For production deployments, use a load balancer to simplify access through a single IP address. 

If your hub cluster has a proxy configuration, ensure that it can reach the hosted cluster API endpoint by adding all hosted cluster API endpoints to the `noProxy` field on the `Proxy` object. For more information, see "Configuring the cluster-wide proxy". 

A hosted control plane exposes the following services on bare metal: 

  * `APIServer`

    * The `APIServer` service runs on port 6443 by default and requires ingress access for communication between the control plane components. 
    * If you use MetalLB load balancing, allow ingress access to the IP range that is used for load balancer IP addresses. 

  * `OAuthServer`

    * The `OAuthServer` service runs on port 443 by default when you use the route and ingress to expose the service. 
    * If you use the `NodePort` publishing strategy, use a firewall rule for the `OAuthServer` service. 

  * `Konnectivity`

    * The `Konnectivity` service runs on port 443 by default when you use the route and ingress to expose the service. 
    * The `Konnectivity` agent establishes a reverse tunnel to allow the control plane to access the network for the hosted cluster. The agent uses egress to connect to the `Konnectivity` server. The server is exposed by using either a route on port 443 or a manually assigned `NodePort`. 
    * If the cluster API server address is an internal IP address, allow access from the workload subnets to the IP address on port 6443. 
    * If the address is an external IP address, allow egress on port 6443 to that external IP address from the nodes. 

  * `Ignition`

    * The `Ignition` service runs on port 443 by default when you use the route and ingress to expose the service. 
    * If you use the `NodePort` publishing strategy, use a firewall rule for the `Ignition` service. 




You do not need the following services on bare metal: 

  * `OVNSbDb`
  * `OIDC`



## 14.3.2. OpenShift Virtualization firewall and port requirements

Ensure that you meet the firewall and port requirements so that ports can communicate between the management cluster, the control plane, and hosted clusters. 

  * The `kube-apiserver` service runs on port 6443 by default and requires ingress access for communication between the control plane components. 

    * If you use the `NodePort` publishing strategy, ensure that the node port that is assigned to the `kube-apiserver` service is exposed. 
    * If you use MetalLB load balancing, allow ingress access to the IP range that is used for load balancer IP addresses. 

  * If you use the `NodePort` publishing strategy, use a firewall rule for the `ignition-server` and `Oauth-server` settings. 
  * The `konnectivity` agent, which establishes a reverse tunnel to allow bi-directional communication on the hosted cluster, requires egress access to the cluster API server address on port 6443. With that egress access, the agent can reach the `kube-apiserver` service. 

    * If the cluster API server address is an internal IP address, allow access from the workload subnets to the IP address on port 6443. 
    * If the address is an external IP address, allow egress on port 6443 to that external IP address from the nodes. 

  * If you change the default port of 6443, adjust the rules to reflect that change. 
  * Ensure that you open any ports that are required by the workloads that run in the clusters. 
  * Use firewall rules, security groups, or other access controls to restrict access to only required sources. Avoid exposing ports publicly unless necessary. 
  * For production deployments, use a load balancer to simplify access through a single IP address. 



## 14.3.3. Firewall, port, and service requirements for non-bare-metal agent machines

You must meet the firewall and port requirements so that ports can communicate between the management cluster, the control plane, and hosted clusters. 

Note

Services run on their default ports. However, if you use the `NodePort` publishing strategy, services run on the port that is assigned by the `NodePort` service. 

Use firewall rules, security groups, or other access controls to restrict access to only required sources. Avoid exposing ports publicly unless necessary. For production deployments, use a load balancer to simplify access through a single IP address. 

A hosted control plane exposes the following services on non-bare-metal agent machines: 

  * `APIServer`

    * The `APIServer` service runs on port 6443 by default and requires ingress access for communication between the control plane components. 
    * If you use MetalLB load balancing, allow ingress access to the IP range that is used for load balancer IP addresses. 

  * `OAuthServer`

    * The `OAuthServer` service runs on port 443 by default when you use the route and ingress to expose the service. 
    * If you use the `NodePort` publishing strategy, use a firewall rule for the `OAuthServer` service. 

  * `Konnectivity`

    * The `Konnectivity` service runs on port 443 by default when you use the route and ingress to expose the service. 
    * The `Konnectivity` agent establishes a reverse tunnel to allow the control plane to access the network for the hosted cluster. The agent uses egress to connect to the `Konnectivity` server. The server is exposed by using either a route on port 443 or a manually assigned `NodePort`. 
    * If the cluster API server address is an internal IP address, allow access from the workload subnets to the IP address on port 6443. 
    * If the address is an external IP address, allow egress on port 6443 to that external IP address from the nodes. 

  * `Ignition`

    * The `Ignition` service runs on port 443 by default when you use the route and ingress to expose the service. 
    * If you use the `NodePort` publishing strategy, use a firewall rule for the `Ignition` service. 




You do not need the following services on non-bare-metal agent machines: 

  * `OVNSbDb`
  * `OIDC`



## 14.3.4. Example firewall configuration

Review an example of what the firewall configuration looks like for a typical hosted control planes on AWS deployment that uses `Route` service publishing. 

Ingress rules
    

  * Port `6443`/TCP: Kubernetes API server, from compute nodes and external clients 
  * Port `443`/TCP: OpenShift Router for Ignition or Konnectivity routes, from compute nodes 



Egress rules
    

  * Port `443`/TCP: HTTPS, to container registries, routes, and external services 
  * Port `6443`/TCP: Management cluster API, to management cluster 
  * Port `53`/TCP and UDP: DNS, to DNS servers 



If you use `NodePort` or `LoadBalancer` service publishing instead of `Route` service publishing, the following rules apply: 

  * Port `8091`/TCP: Konnectivity server, from compute nodes 
  * Port `8443`/TCP: Ignition Proxy, from compute nodes during the bootstrap process, `NodePort` publishing strategy only 
  * Port `9090`/TCP: Ignition server, from compute nodes during the bootstrap process, `NodePort` publishing strategy only
