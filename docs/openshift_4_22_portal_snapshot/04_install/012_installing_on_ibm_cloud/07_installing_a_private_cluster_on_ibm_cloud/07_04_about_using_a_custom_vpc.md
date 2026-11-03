# 7.4. About using a custom VPC

You can deploy OpenShift Container Platform into the subnets of an existing IBM® Virtual Private Cloud (VPC) to avoid account limit constraints or comply with your company’s infrastructure guidelines. 

Because the installation program cannot know what other components are in your existing subnets, it cannot choose subnet CIDRs and so forth. You must configure networking for the subnets to which you will install the cluster. 

## 7.4.1. Requirements for using your VPC

You must correctly configure the existing VPC and its subnets before you install the cluster. The installation program does not create the following components: 

  * NAT gateways 
  * Subnets 
  * Route tables 
  * VPC network 



The installation program cannot: 

  * Subdivide network ranges for the cluster to use 
  * Set route tables for the subnets 
  * Set VPC options like DHCP 



Note

The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail. 

## 7.4.2. VPC validation

The VPC and all of the subnets must be in an existing resource group. The cluster is deployed to the existing VPC. 

As part of the installation, specify the following in the `install-config.yaml` file: 

  * The name of the existing resource group that contains the VPC and subnets (`networkResourceGroupName`) 
  * The name of the existing VPC (`vpcName`) 
  * The subnets that were created for control plane machines and compute machines (`controlPlaneSubnets` and `computeSubnets`) 



Note

Additional installer-provisioned cluster resources are deployed to a separate resource group (`resourceGroupName`). You can specify this resource group before installing the cluster. If undefined, a new resource group is created for the cluster. 

To ensure that the subnets that you provide are suitable, the installation program confirms the following: 

  * All of the subnets that you specify exist. 
  * For each availability zone in the region, you specify: 

    * One subnet for control plane machines. 
    * One subnet for compute machines. 

  * The machine CIDR that you specified contains the subnets for the compute machines and control plane machines. 



Note

Subnet IDs are not supported. 

## 7.4.3. Isolation between clusters

If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is reduced in the following ways: 

  * You can install multiple OpenShift Container Platform clusters in the same VPC. 
  * ICMP ingress is allowed to the entire network. 
  * TCP port 22 ingress (SSH) is allowed to the entire network. 
  * Control plane TCP 6443 ingress (Kubernetes API) is allowed to the entire network. 
  * Control plane TCP 22623 ingress (MCS) is allowed to the entire network.
