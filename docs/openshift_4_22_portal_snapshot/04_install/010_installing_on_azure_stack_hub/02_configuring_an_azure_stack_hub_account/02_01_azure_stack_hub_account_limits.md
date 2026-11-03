# 2.1. Azure Stack Hub account limits

The OpenShift Container Platform cluster uses a number of Microsoft Azure Stack Hub components, and the default [Quota types in Azure Stack Hub](https://docs.microsoft.com/en-us/azure-stack/operator/azure-stack-quota-types?view=azs-2102) affect your ability to install OpenShift Container Platform clusters. 

The following table summarizes the Azure Stack Hub components whose limits can impact your ability to install and run OpenShift Container Platform clusters. 

Component| Number of components required by default| Description  
---|---|---  
vCPU  |  56  |  A default cluster requires 56 vCPUs, so you must increase the account limit.  By default, each cluster creates the following instances: 

  * One bootstrap machine, which is removed after installation 
  * Three control plane machines 
  * Three compute machines 

Because the bootstrap, control plane, and worker machines use `Standard_DS4_v2` virtual machines, which use 8 vCPUs, a default cluster requires 56 vCPUs. The bootstrap node VM is used only during installation.  To deploy more worker nodes, enable autoscaling, deploy large workloads, or use a different instance type, you must further increase the vCPU limit for your account to ensure that your cluster can deploy the machines that you require.   
VNet  |  1  |  Each default cluster requires one Virtual Network (VNet), which contains two subnets.   
Network interfaces  |  7  |  Each default cluster requires seven network interfaces. If you create more machines or your deployed workloads create load balancers, your cluster uses more network interfaces.   
Network security groups  |  2  |  Each cluster creates network security groups for each subnet in the VNet. The default cluster creates network security groups for the control plane and for the compute node subnets:  |  `controlplane` |  Allows the control plane machines to be reached on port 6443 from anywhere   
---|---  
`node` |  Allows worker nodes to be reached from the internet on ports 80 and 443   
  
Network load balancers  |  3  |  Each cluster creates the following [load balancers](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview):  |  `default` |  Public IP address that load balances requests to ports 80 and 443 across worker machines   
---|---  
`internal` |  Private IP address that load balances requests to ports 6443 and 22623 across control plane machines   
`external` |  Public IP address that load balances requests to port 6443 across control plane machines   
  
If your applications create more Kubernetes `LoadBalancer` service objects, your cluster uses more load balancers.   
  
Public IP addresses  |  2  |  The public load balancer uses a public IP address. The bootstrap machine also uses a public IP address so that you can SSH into the machine to troubleshoot issues during installation. The IP address for the bootstrap node is used only during installation.   
Private IP addresses  |  7  |  The internal load balancer, each of the three control plane machines, and each of the three worker machines each use a private IP address.   
Show more

To increase an account limit, file a support request on the Azure portal. For more information, see [Request a quota limit increase for Azure Deployment Environments resources](https://learn.microsoft.com/en-us/azure/deployment-environments/how-to-request-quota-increase). 

**Additional resources**

  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)
