# 2.1. Quotas and limits on IBM Cloud

Default IBM Cloud® quotas and limits affect OpenShift Container Platform cluster installations. You might need to request additional IBM Cloud® resources if you use certain cluster configurations, deploy your cluster in certain regions, or run multiple clusters. 

For a comprehensive list of the default IBM Cloud® quotas and service limits, see the IBM Cloud® documentation for "Quotas and service limits". 

## 2.1.1. Virtual Private Cloud

Each OpenShift Container Platform cluster creates its own VPC. The default quota of VPCs per region is 10 and allows 10 clusters. To have more than 10 clusters in a single region, you must increase this quota. 

## 2.1.2. Application load balancer

By default, each cluster creates three application load balancers (ALBs): 

  * Internal load balancer for the control plane API server 
  * External load balancer for the control plane API server 
  * Load balancer for the router 



You can create additional `LoadBalancer` service objects to create additional ALBs. The default quota of VPC ALBs is 50 per region. To have more than 50 ALBs, you must increase this quota. 

VPC ALBs are supported. Classic ALBs are not supported for IBM Cloud®. 

## 2.1.3. Floating IP addresses

By default, the installation program distributes control plane and compute machines across all availability zones within a region to provision the cluster in a highly available configuration. In each availability zone, the installation program creates a public gateway that requires a separate floating IP address. 

The default quota for a floating IP address is 20 addresses per availability zone. The default cluster configuration yields three floating IP addresses: 

  * Two floating IP addresses in the `us-east-1` primary zone. The IP address associated with the bootstrap node is deleted after installation. 
  * One floating IP address in the `us-east-2` secondary zone. 
  * One floating IP address in the `us-east-3` secondary zone. 



IBM Cloud® can support up to 19 clusters per region in an account. If you plan to have more than 19 default clusters, you must increase this quota. 

## 2.1.4. Virtual Server Instances (VSIs)

By default, a cluster creates VSIs by using `bx2-4x16` profiles, which include the following resources by default: 

  * 4 vCPUs 
  * 16 GB RAM 



The following nodes are created: 

  * One `bx2-4x16` bootstrap machine, which is deleted after the installation is complete 
  * Three `bx2-4x16` control plane nodes 
  * Three `bx2-4x16` compute nodes 



For more information, see the IBM Cloud® documentation on "supported profiles". 

Table 2.1. VSI component quotas and limitsVSI component| Default IBM Cloud® quota| Default cluster configuration| Maximum number of clusters  
---|---|---|---  
vCPU  |  200 vCPUs per region  |  28 vCPUs, or 24 vCPUs after bootstrap removal  |  8 per region   
RAM  |  1600 GB per region  |  112 GB, or 96 GB after bootstrap removal  |  16 per region   
Storage  |  18 TB per region  |  1050 GB, or 900 GB after bootstrap removal  |  19 per region   
Show more

If you plan to exceed the resources stated in the table, you must increase your IBM Cloud® account quota. 

## 2.1.5. Block storage volumes

For each VPC machine, a block storage device is attached for its boot volume. The default cluster configuration creates seven VPC machines, resulting in seven block storage volumes. Additional Kubernetes persistent volume claims (PVCs) of the IBM Cloud® storage class create additional block storage volumes. The default quota of VPC block storage volumes is 300 per region. To have more than 300 volumes, you must increase this quota. 

**Additional resources**

  * [Quotas and service limits (IBM Cloud® documentation)](https://cloud.ibm.com/docs/vpc?topic=vpc-quotas)
  * [Supported profiles (IBM Cloud® documentation)](https://cloud.ibm.com/docs/vpc?topic=vpc-profiles)
