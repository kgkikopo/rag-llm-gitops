# 6.3. Private clusters in IBM Power Virtual Server

To create a private cluster on IBM Power® Virtual Server, you must provide an existing private Virtual Private Cloud (VPC) and subnets to host the cluster. The installation program configures the Ingress Operator and API server for only internal traffic. 

The cluster still requires access to internet to access the IBM Cloud® APIs. 

The following items are not required or created when you install a private cluster: 

  * Public subnets 
  * Public network load balancers, which support public Ingress 
  * A public DNS zone that matches the `baseDomain` for the cluster 



You will also need to create an IBM® DNS service containing a DNS zone that matches your `baseDomain`. Unlike standard deployments on Power VS which use IBM® CIS for DNS, you must use IBM® DNS for your DNS service. 

## 6.3.1. Limitations

Private clusters on IBM Power® Virtual Server are subject only to the limitations associated with the existing VPC that was used for cluster deployment.
