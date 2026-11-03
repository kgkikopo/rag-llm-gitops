# 2.1. Azure account limits

The OpenShift Container Platform cluster uses a number of Microsoft Azure components. Default subscription and service limits, quotas, and constraints can affect your ability to install OpenShift Container Platform clusters. 

For more information on Azure subscription and service limits, see "Azure subscription and service limits, quotas, and constraints". 

Important

Default limits vary by offer category types, such as Free Trial and Pay-As-You-Go, and by series, such as Dv2, F, and G. For example, the default for Enterprise Agreement subscriptions is 350 cores. 

Check the limits for your subscription type and if necessary, increase quota limits for your account before you install a default cluster on Azure. 

The following table summarizes the Azure components whose limits can impact your ability to install and run OpenShift Container Platform clusters. 

Component| Number of components required by default| Default Azure limit| Description  
---|---|---|---  
vCPU  |  44  |  20 per region  |  A default cluster requires 44 vCPUs, so you must increase the account limit.  By default, each cluster creates the following instances: 

  * One bootstrap machine, which is removed after installation 
  * Three control plane machines 
  * Three compute machines 

Because the bootstrap and control plane machines use `Standard_D8s_v3` virtual machines, which use 8 vCPUs, and the compute machines use `Standard_D4s_v3` virtual machines, which use 4 vCPUs, a default cluster requires 44 vCPUs. The bootstrap node VM, which uses 8 vCPUs, is used only during installation.  To deploy more worker nodes, enable autoscaling, deploy large workloads, or use a different instance type, you must further increase the vCPU limit for your account to ensure that your cluster can deploy the machines that you require.   
OS Disk  |  7  |  |  Each cluster machine must have a minimum of 100 GB of storage and 300 IOPS.  Note Faster storage is recommended for production clusters and clusters with intensive workloads. For more information about optimizing storage for performance, see the page titled "Optimizing storage" in the "Scalability and performance" section.   
VNet  |  1  |  1000 per region  |  Each default cluster requires one Virtual Network (VNet), which contains two subnets.   
Network interfaces  |  7  |  65,536 per region  |  Each default cluster requires seven network interfaces. If you create more machines or your deployed workloads create load balancers, your cluster uses more network interfaces.   
Network security groups  |  2  |  5000  |  Each cluster creates network security groups for each subnet in the VNet. The default cluster creates network security groups for the control plane and for the compute node subnets:  |  `controlplane` |  Allows the control plane machines to be reached on port 6443 from anywhere   
---|---  
`node` |  Allows worker nodes to be reached from the internet on ports 80 and 443   
  
Network load balancers  |  3  |  1000 per region  |  Each cluster creates the following [load balancers](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview):  |  `default` |  Public IP address that load balances requests to ports 80 and 443 across worker machines   
---|---  
`internal` |  Private IP address that load balances requests to ports 6443 and 22623 across control plane machines   
`external` |  Public IP address that load balances requests to port 6443 across control plane machines   
  
If your applications create more Kubernetes `LoadBalancer` service objects, your cluster uses more load balancers.   
  
Public IP addresses  |  3  |  |  Each of the two public load balancers uses a public IP address. The bootstrap machine also uses a public IP address so that you can SSH into the machine to troubleshoot issues during installation. The IP address for the bootstrap node is used only during installation.   
Private IP addresses  |  7  |  |  The internal load balancer, each of the three control plane machines, and each of the three worker machines each use a private IP address.   
Spot VM vCPUs (optional)  |  0  If you configure spot VMs, your cluster must have two spot VM vCPUs for every compute node.  |  20 per region  |  This is an optional component. To use spot VMs, you must increase the Azure default limit to at least twice the number of compute nodes in your cluster.  Note Using spot VMs for control plane nodes is not recommended.   
Show more

To increase an account limit, file a support request on the Azure portal. For more information, see [Request a quota limit increase for Azure Deployment Environments resources](https://learn.microsoft.com/en-us/azure/deployment-environments/how-to-request-quota-increase). 

**Additional resources**

  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)
  * [Azure subscription and service limits, quotas, and constraints (Azure documentation)](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits)
