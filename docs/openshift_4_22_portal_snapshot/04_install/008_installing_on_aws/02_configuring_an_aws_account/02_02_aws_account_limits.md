# 2.2. AWS account limits

The OpenShift Container Platform cluster uses several Amazon Web Services (AWS) components, and the default service limits affect your ability to install OpenShift Container Platform clusters. 

If you use certain cluster configurations, deploy your cluster in certain AWS regions, or run multiple clusters from your account, you might need to request additional resources for your AWS account. 

The following table summarizes the AWS components whose limits can impact your ability to install and run OpenShift Container Platform clusters. 

Component| Number of clusters available by default| Default AWS limit| Description  
---|---|---|---  
Instance Limits  |  Varies  |  Varies  |  By default, each cluster creates the following instances: 

  * One bootstrap machine, which is removed after installation 
  * Three control plane nodes 
  * Three worker nodes 

These instance type counts are within a new account’s default limit. To deploy more worker nodes, enable autoscaling, deploy large workloads, or use a different instance type, review your account limits to ensure that your cluster can deploy the machines that you need.  In most regions, the worker machines use an `m6i.large` instance and the bootstrap and control plane machines use `m6i.xlarge` instances. In some regions, including all regions that do not support these instance types, `m5.large` and `m5.xlarge` instances are used instead.   
Elastic IPs (EIPs)  |  0 to 1  |  5 EIPs per account  |  To provision the cluster in a highly available configuration, the installation program creates a public and private subnet for each availability zone within a region. Each private subnet requires a NAT gateway, and each NAT gateway requires a separate elastic IP. Review the AWS region map to determine how many availability zones are in each region. To take advantage of the default high availability, install the cluster in a region with at least three availability zones. To install a cluster in a region with more than five availability zones, you must increase the EIP limit.  Important To use the `us-east-1` region, you must increase the EIP limit for your account.   
Virtual Private Clouds (VPCs)  |  5  |  5 VPCs per region  |  Each cluster creates its own VPC.   
Elastic Load Balancing (ELB/NLB)  |  3  |  20 per region  |  By default, each cluster creates internal and external network load balancers for the master API server and a single Classic Load Balancer for the router. Deploying more Kubernetes `Service` objects with type `LoadBalancer` will create additional load balancers.   
NAT Gateways  |  5  |  5 per availability zone  |  The cluster deploys one NAT gateway in each availability zone.   
Elastic Network Interfaces (ENIs)  |  At least 12  |  350 per region  |  The default installation creates 21 ENIs and an ENI for each availability zone in your region. For example, the `us-east-1` region contains six availability zones, so a cluster that is deployed in that zone uses 27 ENIs. Review the AWS region map to determine how many availability zones are in each region.  Additional ENIs are created for additional machines and ELB load balancers that are created by cluster usage and deployed workloads.   
VPC Gateway  |  20  |  20 per account  |  Each cluster creates a single VPC Gateway for S3 access.   
S3 buckets  |  99  |  100 buckets per account  |  Because the installation process creates a temporary bucket and the registry component in each cluster creates a bucket, you can create only 99 OpenShift Container Platform clusters per AWS account.   
Security Groups  |  250  |  2,500 per account  |  Each cluster creates 10 distinct security groups.   
Security Groups on network interfaces  |  Varies  |  5 per network interface  |  By default, AWS allows 5 security groups per network interface. The installation program creates 2 security groups for compute machines and 3 security groups for control plane machines. If you are installing a cluster into a shared VPC, there are three scenarios in which you must increase this quota: 

  * You specified 4 or more custom security groups for compute machines using the `compute.platform.aws.additionalSecurityGroupIDs` parameter in the `install-config.yaml` file. 
  * You specified 3 or more custom security groups for control plane machines using the `controlPlane.platform.aws.additionalSecurityGroupIDs` parameter in the `install-config.yaml` file. 
  * You specified 3 or more custom security groups for all machines using the `platform.aws.defaultMachinePlatform` parameter in the `install-config.yaml` file. 

You must increase the quota of security groups per network interface to a number greater than or equal to `3 + (number of control plane custom security groups OR number of default machine platform custom security groups)`, or `2 + (number of compute custom security groups OR number of default machine platform custom security groups)`, whichever is higher. If you do not specify a sufficient quota, the installation will succeed, but it will generate `SecurityGroupsPerInterfaceLimitExceeded` errors in the installation log, and the additional security groups will not be applied. The maximum allowed quota is 16 and the maximum number of user-specified security groups is 10.   
Show more

**Additional resources**

  * [Service Limits (AWS documentation)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
  * [Regions and Zones (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
  * [NAT Gateways (AWS documentation)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
  * [Elastic IP Addresses (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
  * [Region map (AWS documentation)](https://aws.amazon.com/about-aws/global-infrastructure)
  * [Elastic load balancing (AWS documentation)](https://aws.amazon.com/elasticloadbalancing)
