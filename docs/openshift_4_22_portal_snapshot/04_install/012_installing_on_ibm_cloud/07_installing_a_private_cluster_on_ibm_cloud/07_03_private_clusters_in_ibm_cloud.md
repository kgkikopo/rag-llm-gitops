# 7.3. Private clusters in IBM Cloud

To create a private cluster on IBM Cloud®, you must provide an existing private VPC and subnets. The installation program must also resolve the DNS records that the cluster requires, and configures the Ingress Operator and API server for only internal traffic. 

The cluster still requires access to internet to access the IBM Cloud® APIs. 

The following items are not required or created when you install a private cluster: 

  * Public subnets 
  * Public network load balancers, which support public ingress 
  * A public DNS zone that matches the `baseDomain` for the cluster 



The installation program does use the `baseDomain` that you specify to create a private DNS zone and the required records for the cluster. The cluster is configured so that the Operators do not create public records for the cluster and all cluster machines are placed in the private subnets that you specify. 

## 7.3.1. Limitations

Private clusters on IBM Cloud® are subject only to the limitations associated with the existing VPC that was used for cluster deployment.
