# 1.6. Requirements for a cluster using the platform "none" option

There are additional requirements when installing a cluster using the platform "none" option with the Agent-based Installer. 

Important

See "Deploying OpenShift 4.x on non-tested platforms using the bare metal install method" before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments. 

## 1.6.1. Platform "none" DNS requirements

In OpenShift Container Platform deployments, DNS name resolution is required for several components. 

The following components need DNS name resolution: 

  * The Kubernetes API 
  * The OpenShift Container Platform application wildcard 
  * The control plane and compute machines 



Reverse DNS resolution is also required for the Kubernetes API, the control plane machines, and the compute machines. 

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate. 

Note

It is recommended to use a DHCP server to provide the hostnames to each cluster node. 

The following DNS records are required for an OpenShift Container Platform cluster using the platform `none` option and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`. 

Table 1.5. Required DNS recordsComponent| Record| Description  
---|---|---  
Kubernetes API  |  `api.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
`api-int.<cluster_name>.<base_domain>.` |  A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.  Important The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods.   
Routes  |  `*.apps.<cluster_name>.<base_domain>.` |  A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console.   
Control plane machines  |  `<master><n>.<cluster_name>.<base_domain>.` |  DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster.   
Compute machines  |  `<worker><n>.<cluster_name>.<base_domain>.` |  DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster.   
Show more

Note

In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration. 

Tip

You can use the `dig` command to verify name and reverse name resolution. 

### 1.6.1.1. Example DNS configuration for platform "none" clusters

This section provides A and PTR record configuration samples that meet the DNS requirements for deploying OpenShift Container Platform using the platform `none` option. The samples are not meant to provide advice for choosing one DNS solution over another. 

In the examples, the cluster name is `ocp4` and the base domain is `example.com`. 

Example DNS A record configuration for a platform "none" cluster
     The following example is a BIND zone file that shows sample A records for name resolution in a cluster using the platform `none` option. 

**Sample DNS zone database**

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
master0.ocp4.example.com.	IN	A	192.168.1.97
master1.ocp4.example.com.	IN	A	192.168.1.98
master2.ocp4.example.com.	IN	A	192.168.1.99
;
worker0.ocp4.example.com.	IN	A	192.168.1.11
worker1.ocp4.example.com.	IN	A	192.168.1.7
;
;EOF
```


where: 

`api.ocp4.example.com.`
     Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer. 
`api-int.ocp4.example.com.`
     Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications. 
`*.apps.ocp4.example.com.`
    

Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. 

Note

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

`master0.ocp4.example.com.`-`master2.ocp4.example.com.`
     Provides name resolution for the control plane machines. 
`worker0.ocp4.example.com.`-`worker1.ocp4.example.com.`
     Provides name resolution for the compute machines. 
Example DNS PTR record configuration for a platform "none" cluster
     The following example BIND zone file shows sample PTR records for reverse name resolution in a cluster using the platform `none` option. 

**Sample DNS zone database for reverse records**

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
97.1.168.192.in-addr.arpa.	IN	PTR	master0.ocp4.example.com.
98.1.168.192.in-addr.arpa.	IN	PTR	master1.ocp4.example.com.
99.1.168.192.in-addr.arpa.	IN	PTR	master2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	worker0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	worker1.ocp4.example.com.
;
;EOF
```


where: 

`api.ocp4.example.com.`
     Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer. 
`api-int.ocp4.example.com.`
     Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications. 
`master0.ocp4.example.com.`-`master2.ocp4.example.com.`
     Provides reverse DNS resolution for the control plane machines. 
`worker0.ocp4.example.com.`-`worker1.ocp4.example.com.`
     Provides reverse DNS resolution for the compute machines. 

Note

A PTR record is not required for the OpenShift Container Platform application wildcard. 

## 1.6.2. Platform "none" Load balancing requirements

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

Note

  * These requirements do not apply to single-node OpenShift clusters using the platform `none` option. 
  * If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately. 



The load balancing infrastructure must meet the following requirements: 

  1. **API load balancer** : Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions: 

     * Layer 4 load balancing only. This can be referred to as Raw TCP, SSL Passthrough, or SSL Bridge mode. If you use SSL Bridge mode, you must enable Server Name Indication (SNI) for the API routes. 
     * A stateless load balancing algorithm. The options vary based on the load balancer implementation. 

Important

Do not configure session persistence for an API load balancer. 

Configure the following ports on both the front and back of the load balancers: 

Table 1.6. API load balancerPort| Back-end machines (pool members)| Internal| External| Description  
---|---|---|---|---  
`6443` |  Control plane. You must configure the `/readyz` endpoint for the API server health check probe.  |  X  |  X  |  Kubernetes API server   
`22623` |  Control plane.  |  X  |  |  Machine config server   
Show more

Important

The Agent-based Installer requires TCP port `8090` to be open between all hosts and the rendezvous host so that the hosts can access the Assisted Service API. Port `8090` is required only during the discovery and bootstrap phases. For more information, see "Port requirements for the rendezvous host". 

Note

The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values. 

  2. **Application Ingress load balancer** : Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. 

Configure the following conditions: 

     * Layer 4 load balancing only. This can be referred to as Raw TCP, SSL Passthrough, or SSL Bridge mode. If you use SSL Bridge mode, you must enable Server Name Indication (SNI) for the ingress routes. 
     * A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform. 

Tip

If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption. 

Configure the following ports on both the front and back of the load balancers: 

Table 1.7. Application Ingress load balancerPort| Back-end machines (pool members)| Internal| External| Description  
---|---|---|---|---  
`443` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTPS traffic   
`80` |  The machines that run the Ingress Controller pods, compute, or worker, by default.  |  X  |  X  |  HTTP traffic   
Show more

Note

If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. 




### 1.6.2.1. Example load balancer configuration for platform "none" clusters

This section provides an example API and application Ingress load balancer configuration that meets the load balancing requirements for clusters using the platform `none` option. The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another. 

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
  server master0 master0.ocp4.example.com:6443 check inter 1s
  server master1 master1.ocp4.example.com:6443 check inter 1s
  server master2 master2.ocp4.example.com:6443 check inter 1s
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server worker0 worker0.ocp4.example.com:443 check inter 1s
  server worker1 worker1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server worker0 worker0.ocp4.example.com:80 check inter 1s
  server worker1 worker1.ocp4.example.com:80 check inter 1s
```


  * Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic. 
  * Port `22623` handles the machine config server traffic and points to the control plane machines. 
  * Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. 
  * Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. 

Note

If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. 




Tip

If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node. 

**Additional resources**

  * [Port requirements for the rendezvous host](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/preparing-to-install-with-agent-based-installer#agent-install-networking-ports_preparing-to-install-with-agent-based-installer "1.5.1. Port requirements for the rendezvous host")
  * [Cluster capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-capabilities)
  * [Deploying OpenShift 4.x on non-tested platforms using the bare metal install method (Red Hat Knowledgebase article)](https://access.redhat.com/articles/4207611)
