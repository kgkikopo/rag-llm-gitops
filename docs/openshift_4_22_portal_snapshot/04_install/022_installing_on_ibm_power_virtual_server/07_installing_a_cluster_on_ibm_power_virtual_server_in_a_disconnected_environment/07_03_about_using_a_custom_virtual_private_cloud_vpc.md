# 7.3. About using a custom Virtual Private Cloud (VPC)

In OpenShift Container Platform 4.22, you can deploy a cluster into the subnets of an existing IBM® Virtual Private Cloud (VPC). 

## 7.3.1. Requirements for using your Virtual Private Cloud (VPC)

You must correctly configure the existing VPC and its subnets before you install the cluster. The installation program does not create a VPC or VPC subnet in this scenario. 

The installation program cannot: 

  * Subdivide network ranges for the cluster to use 
  * Set route tables for the subnets 
  * Set VPC options such as DHCP 



Note

The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail. 

## 7.3.2. Virtual Private Cloud (VPC) validation

The VPC and all of the subnets must be in an existing resource group. The cluster is deployed to this resource group. 

As part of the installation, specify the following in the `install-config.yaml` file: 

  * The name of the resource group 
  * The name of VPC 
  * The name of the VPC subnet 



To ensure that the subnets that you give are suitable, the installation program confirms that all of the subnets you specify exist. 

Note

Subnet IDs are not supported. 

## 7.3.3. Isolation between clusters

If you deploy OpenShift Container Platform to an existing network, cluster service isolation decreases in the following ways: 

  * ICMP Ingress is allowed to the entire network. 
  * TCP port 22 Ingress (SSH) is allowed to the entire network. 
  * Control plane TCP 6443 Ingress (Kubernetes API) is allowed to the entire network. 
  * Control plane TCP 22623 Ingress (MCS) is allowed to the entire network.
