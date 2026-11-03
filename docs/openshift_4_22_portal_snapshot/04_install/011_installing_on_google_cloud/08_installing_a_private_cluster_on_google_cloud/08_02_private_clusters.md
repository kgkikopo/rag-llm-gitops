# 8.2. Private clusters

You can deploy a private OpenShift Container Platform cluster that does not expose external endpoints. Private clusters are accessible from only an internal network and are not visible to the internet. 

By default, OpenShift Container Platform is provisioned to use publicly-accessible DNS and endpoints. A private cluster sets the DNS, Ingress Controller, and API server to private when you deploy your cluster. This means that the cluster resources are only accessible from your internal network and are not visible to the internet. 

Important

If the cluster has any public subnets, load balancer services created by administrators might be publicly accessible. To ensure cluster security, verify that these services are explicitly annotated as private. 

To deploy a private cluster, you must: 

  * Use existing networking that meets your requirements. Your cluster resources might be shared between other clusters on the network. 
  * Deploy from a machine that has access to: 

    * The API services for the cloud to which you provision. 
    * The hosts on the network that you provision. 
    * The internet to obtain installation media. 




## 8.2.1. Private clusters in Google Cloud

To create a private cluster on Google Cloud, provide an existing VPC network and subnets, and specify `publish: Internal` in your `install-config.yaml` file. The installation program resolves required DNS records and configures the Ingress Operator and API server for internal traffic only. 

The cluster still requires access to internet to access the Google Cloud APIs. 

The following items are not required or created when you install a private cluster: 

  * Public subnets 
  * Public network load balancers, which support public ingress 
  * A public DNS zone that matches the `baseDomain` for the cluster 



The installation program does use the `baseDomain` that you specify to create a private DNS zone and the required records for the cluster. The cluster is configured so that the Operators do not create public records for the cluster and all cluster machines are placed in the private subnets that you specify. 

Because it is not possible to limit access to external load balancers based on source tags, the private cluster uses only internal load balancers to allow access to internal instances. 

The internal load balancer relies on instance groups rather than the target pools that the network load balancers use. The installation program creates instance groups for each zone, even if there is no instance in that group. 

  * The cluster IP address is internal only. 
  * One forwarding rule manages both the Kubernetes API and machine config server ports. 
  * The backend service consists of each zone’s instance group and, while it exists, the bootstrap instance group. 
  * The firewall uses a single rule that is based on only internal source ranges. 



### 8.2.1.1. Limitations

No health check for the Machine config server, `/healthz`, runs because of a difference in load balancer functionality. Two internal load balancers cannot share a single IP address, but two network load balancers can share a single external IP address. Instead, the health of an instance is determined entirely by the `/readyz` check on port 6443.
