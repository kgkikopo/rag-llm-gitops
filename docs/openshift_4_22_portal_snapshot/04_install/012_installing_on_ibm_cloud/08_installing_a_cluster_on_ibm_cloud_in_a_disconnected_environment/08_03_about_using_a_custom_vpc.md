# 8.3. About using a custom VPC

You can deploy OpenShift Container Platform into the subnets of an existing IBM® Virtual Private Cloud (VPC) to avoid account limit constraints or comply with your company’s infrastructure guidelines. 

Because the installation program cannot know what other components are in your existing subnets, it cannot choose subnet CIDRs and so forth. You must configure networking for the subnets to which you will install the cluster. 

## 8.3.1. Requirements for using your VPC

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

## 8.3.2. VPC validation

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

## 8.3.3. Isolation between clusters

If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is reduced in the following ways: 

  * You can install multiple OpenShift Container Platform clusters in the same VPC. 
  * ICMP ingress is allowed to the entire network. 
  * TCP port 22 ingress (SSH) is allowed to the entire network. 
  * Control plane TCP 6443 ingress (Kubernetes API) is allowed to the entire network. 
  * Control plane TCP 22623 ingress (MCS) is allowed to the entire network. 



## 8.3.4. Allowing endpoint gateway traffic

If you are using IBM Cloud® Virtual Private endpoints, your Virtual Private Cloud (VPC) must be configured to allow traffic to and from the endpoint gateways. 

A VPC’s default security group is configured to allow all outbound traffic to endpoint gateways. Therefore, the simplest way to allow traffic between your VPC and endpoint gateways is to modify the default security group to allow inbound traffic on port 443. 

Note

If you choose to configure a new security group, the security group must be configured to allow both inbound and outbound traffic. 

**Prerequisites**

  * You have installed the IBM Cloud® Command Line Interface utility (`ibmcloud`). 



**Procedure**

  1. Obtain the identifier for the default security group by running the following command: 

```shell-session
$ DEFAULT_SG=$(ibmcloud is vpc <your_vpc_name> --output JSON | jq -r '.default_security_group.id')
```


  2. Add a rule that allows inbound traffic on port 443 by running the following command: 

```shell-session
$ ibmcloud is security-group-rule-add $DEFAULT_SG inbound tcp --remote 0.0.0.0/0 --port-min 443 --port-max 443
```


Note

Be sure that your endpoint gateways are configured to use this security group.
