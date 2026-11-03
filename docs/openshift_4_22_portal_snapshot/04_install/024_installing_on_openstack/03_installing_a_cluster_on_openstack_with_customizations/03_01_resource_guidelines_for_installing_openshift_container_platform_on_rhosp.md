# 3.1. Resource guidelines for installing OpenShift Container Platform on RHOSP

To support an OpenShift Container Platform installation, your Red Hat OpenStack Platform (RHOSP) quota must meet certain requirements. 

Table 3.1. Recommended resources for a default OpenShift Container Platform cluster on RHOSPResource| Value  
---|---  
Floating IP addresses  |  3   
Ports  |  15   
Routers  |  1   
Subnets  |  1   
RAM  |  88 GB   
vCPUs  |  22   
Volume storage  |  275 GB   
Instances  |  7   
Security groups  |  3   
Security group rules  |  60   
Server groups  |  2 - plus 1 for each additional availability zone in each machine pool   
Show more

A cluster might function with fewer than recommended resources, but cluster performance is not guaranteed. 

Important

If RHOSP object storage (Swift) is available and operated by a user account with the `swiftoperator` role, Swift is used as the default backend for the OpenShift Container Platform image registry. In this case, the volume storage requirement is 175 GB. Swift space requirements vary depending on the size of the image registry. 

Note

By default, your security group and security group rule quotas might be low. If you encounter problems, run `openstack quota set --secgroups 3 --secgroup-rules 60 <project>` as an administrator to increase them. 

An OpenShift Container Platform deployment comprises control plane machines, compute machines, and a bootstrap machine. 

## 3.1.1. Control plane machines

By default, the OpenShift Container Platform installation process creates three control plane machines. 

Each machine requires: 

  * An instance from the RHOSP quota 
  * A port from the RHOSP quota 
  * A flavor with at least 16 GB memory and 4 vCPUs 
  * At least 100 GB storage space from the RHOSP quota 



## 3.1.2. Compute machines

By default, the OpenShift Container Platform installation process creates three compute machines. 

Each machine requires: 

  * An instance from the RHOSP quota 
  * A port from the RHOSP quota 
  * A flavor with at least 8 GB memory and 2 vCPUs 
  * At least 100 GB storage space from the RHOSP quota 



Tip

Compute machines host the applications that you run on OpenShift Container Platform; aim to run as many as you can. 

## 3.1.3. Bootstrap machine

During installation, a bootstrap machine is temporarily provisioned to stand up the control plane. After the production control plane is ready, the bootstrap machine is deprovisioned. 

The bootstrap machine requires: 

  * An instance from the RHOSP quota 
  * A port from the RHOSP quota 
  * A flavor with at least 16 GB memory and 4 vCPUs 
  * At least 100 GB storage space from the RHOSP quota 



## 3.1.4. Load balancing requirements for user-provisioned infrastructure

Before you install OpenShift Container Platform, you can provision your own API and application ingress load balancing infrastructure to use in place of the default, internal load balancing solution. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

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

Table 3.2. Application Ingress load balancerPort| Back-end machines (pool members)| Internal| External| Description  
---|---|---|---|---  
`443` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTPS traffic   
`80` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTP traffic   
Show more

Note

If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. 

### 3.1.4.1. Example load balancer configuration for clusters that are deployed with user-managed load balancers

This section provides an example API and application Ingress load balancer configuration that meets the load balancing requirements for clusters that are deployed with user-managed load balancers. The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another. 

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
