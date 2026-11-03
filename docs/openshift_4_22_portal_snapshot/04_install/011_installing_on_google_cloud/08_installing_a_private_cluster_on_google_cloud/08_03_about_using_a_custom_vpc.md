# 8.3. About using a custom VPC

In OpenShift Container Platform 4.22, you can deploy a cluster into an existing VPC and subnets in Google Cloud to help avoid limit constraints in new accounts or to more easily abide by the operational constraints that your company’s guidelines set. 

You must also use existing routing rules. This installation option is a good choice if you cannot obtain the infrastructure creation permissions that are required to create the VPC yourself. 

## 8.3.1. Requirements for using your VPC

The installation program will no longer create the following components: 

  * VPC 
  * Subnets 
  * Cloud router 
  * Cloud NAT 
  * NAT IP addresses 



If you use a custom VPC, you must correctly configure it and its subnets for the installation program and the cluster to use. The installation program cannot subdivide network ranges for the cluster to use, set route tables for the subnets, or set VPC options such as DHCP, so you must do so before you install the cluster. 

Your VPC and subnets must meet the following characteristics: 

  * The VPC must be in the same Google Cloud project that you deploy the OpenShift Container Platform cluster to. 
  * To allow access to the internet from the control plane and compute machines, you must configure cloud NAT on the subnets to allow egress to it. These machines do not have a public address. Even if you do not require access to the internet, you must allow egress to the VPC network to obtain the installation program and images. Because multiple cloud NATs cannot be configured on the shared subnets, the installation program cannot configure it. 



To ensure that the subnets that you provide are suitable, the installation program confirms the following data: 

  * All the subnets that you specify exist and belong to the VPC that you specified. 
  * The subnet CIDRs belong to the machine CIDR. 
  * You must provide a subnet to deploy the cluster control plane and compute machines to. You can use the same subnet for both machine types. 



If you delete a cluster that uses an existing VPC, the VPC is not deleted. 

## 8.3.2. Division of permissions

Starting with OpenShift Container Platform 4.3, you do not need all of the permissions that are required for an installation program-provisioned infrastructure cluster to deploy a cluster. This change mimics the division of permissions that you might have at your company: some individuals can create different resources in your clouds than others. For example, you might be able to create application-specific items, such as instances, buckets, and load balancers, but not networking-related components, such as VPCs, subnets, or Ingress rules. 

The Google Cloud credentials that you use when you create your cluster do not need the networking permissions that are required to make VPCs and core networking components within the VPC, such as subnets, routing tables, internet gateways, NAT, and VPN. You still need permission to make the application resources that the machines within the cluster require, such as load balancers, security groups, storage, and nodes. 

## 8.3.3. Isolation between clusters

If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is preserved by firewall rules that reference the machines in your cluster by the cluster’s infrastructure ID. Only traffic within the cluster is allowed. 

If you deploy multiple clusters to the same VPC, the following components might share access between clusters: 

  * The API, which is globally available with an external publishing strategy or available throughout the network in an internal publishing strategy 
  * Debugging tools, such as ports on VM instances that are open to the machine CIDR for SSH and ICMP access
