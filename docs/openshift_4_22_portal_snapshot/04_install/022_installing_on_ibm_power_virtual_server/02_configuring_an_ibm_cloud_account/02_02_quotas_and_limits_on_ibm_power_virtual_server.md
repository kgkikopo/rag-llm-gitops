# 2.2. Quotas and limits on IBM Power Virtual Server

Default IBM Cloud® and IBM Power® Virtual Server quotas and limits affect your ability to install OpenShift Container Platform clusters. You might need to request additional resources depending on your configuration, region, or number of clusters. 

## 2.2.1. Virtual private cloud

Each OpenShift Container Platform cluster creates its own Virtual Private Cloud (VPC). The default quota of VPC instances per region is 10. If you have 10 VPC instances created, you must increase your quota before attempting an installation. 

## 2.2.2. Application load balancer

By default, each cluster creates two application load balancers (ALBs): 

  * Internal load balancer for the control plane API server 
  * External load balancer for the control plane API server 



You can create additional `LoadBalancer` service objects to create additional ALBs. The default quota of VPC ALBs are 50 per region. To have more than 50 ALBs, you must increase this quota. 

VPC ALBs are supported. Classic ALBs are not supported for IBM Power® Virtual Server. 

## 2.2.3. Transit gateways

Each OpenShift Container Platform cluster creates its own transit gateway to enable communication with a VPC. The default quota of transit gateways per IBM Cloud® account is 10. If you have 10 transit gateways created, you must increase your quota before attempting an installation. 

## 2.2.4. Dynamic host configuration protocol (DHCP) service

There is a limit of one Dynamic Host Configuration Protocol (DHCP) service per IBM Power® Virtual Server instance. 

## 2.2.5. Virtual server instances

By default, a cluster creates server instances with the following resources: 

  * 0.5 CPUs 
  * 32 GB RAM 
  * System Type: `s922`
  * Processor Type: `uncapped`, `shared`
  * Storage Tier: `Tier-3`



The installation program creates the following nodes: 

  * One bootstrap machine, which the installation process removes after the installation is complete 
  * Three control plane nodes 
  * Three compute nodes 



**Additional resources**

  * [Quotas and service limits](https://cloud.ibm.com/docs/vpc?topic=vpc-quotas)
  * [Creating an IBM Power Virtual Server](https://cloud.ibm.com/docs/power-iaas?topic=power-iaas-creating-power-virtual-server)
