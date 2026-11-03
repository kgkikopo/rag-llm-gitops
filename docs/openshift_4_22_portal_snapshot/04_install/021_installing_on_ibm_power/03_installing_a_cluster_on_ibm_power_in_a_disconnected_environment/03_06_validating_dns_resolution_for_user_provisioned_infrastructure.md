# 3.6. Validating DNS resolution for user-provisioned infrastructure

To prevent network-related installation failures and ensure node connectivity in OpenShift Container Platform, validate your DNS configuration before deploying on user-provisioned infrastructure. 

Important

The validation steps detailed in this section must succeed before you install your cluster. 

**Prerequisites**

  * You have configured the required DNS records for your user-provisioned infrastructure. 



**Procedure**

  1. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses contained in the responses correspond to the correct components. 

     1. Perform a lookup against the Kubernetes API record name. Check that the result points to the IP address of the API load balancer: 

```shell-session
$ dig +noall +answer @<nameserver_ip> api.<cluster_name>.<base_domain>
```


Replace `<nameserver_ip>` with the IP address of the name server, `<cluster_name>` with your cluster name, and `<base_domain>` with your base domain name. 

**Example output**

```shell-session
api.ocp4.example.com.		604800	IN	A	192.168.1.5
```


     2. Perform a lookup against the Kubernetes internal API record name. Check that the result points to the IP address of the API load balancer: 

```shell-session
$ dig +noall +answer @<nameserver_ip> api-int.<cluster_name>.<base_domain>
```


**Example output**

```shell-session
api-int.ocp4.example.com.		604800	IN	A	192.168.1.5
```


     3. Test an example `*.apps.<cluster_name>.<base_domain>` DNS wildcard lookup. All of the application wildcard lookups must resolve to the IP address of the application ingress load balancer: 

```shell-session
$ dig +noall +answer @<nameserver_ip> random.apps.<cluster_name>.<base_domain>
```


**Example output**

```shell-session
random.apps.ocp4.example.com.		604800	IN	A	192.168.1.5
```


Note

In the example outputs, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation. 

You can replace `random` with another wildcard value. For example, you can query the route to the OpenShift Container Platform console: 

```shell-session
$ dig +noall +answer @<nameserver_ip> console-openshift-console.apps.<cluster_name>.<base_domain>
```


**Example output**

```shell-session
console-openshift-console.apps.ocp4.example.com. 604800 IN	A 192.168.1.5
```


     4. Run a lookup against the bootstrap DNS record name. Check that the result points to the IP address of the bootstrap node: 

```shell-session
$ dig +noall +answer @<nameserver_ip> bootstrap.<cluster_name>.<base_domain>
```


**Example output**

```shell-session
bootstrap.ocp4.example.com.		604800	IN	A	192.168.1.96
```


     5. Use this method to perform lookups against the DNS record names for the control plane and compute nodes. Check that the results correspond to the IP addresses of each node. 

  2. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names contained in the responses correspond to the correct components. 

     1. Perform a reverse lookup against the IP address of the API load balancer. Check that the response includes the record names for the Kubernetes API and the Kubernetes internal API: 

```shell-session
$ dig +noall +answer @<nameserver_ip> -x 192.168.1.5
```


**Example output**

```shell-session
5.1.168.192.in-addr.arpa. 604800	IN	PTR	api-int.ocp4.example.com.
5.1.168.192.in-addr.arpa. 604800	IN	PTR	api.ocp4.example.com.
```


where: 

`api-int.ocp4.example.com`
     Specifies the record name for the Kubernetes internal API. 
`api.ocp4.example.com`
    

Specifies the record name for the Kubernetes API. 

Note

A PTR record is not required for the OpenShift Container Platform application wildcard. No validation step is needed for reverse DNS resolution against the IP address of the application ingress load balancer. 

     2. Perform a reverse lookup against the IP address of the bootstrap node. Check that the result points to the DNS record name of the bootstrap node: 

```shell-session
$ dig +noall +answer @<nameserver_ip> -x 192.168.1.96
```


**Example output**

```shell-session
96.1.168.192.in-addr.arpa. 604800	IN	PTR	bootstrap.ocp4.example.com.
```


     3. Use this method to perform reverse lookups against the IP addresses for the control plane and compute nodes. Check that the results correspond to the DNS record names of each node.
