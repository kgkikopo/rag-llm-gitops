# 1.3. Environment requirements

Before you install an OpenShift Container Platform cluster, verify that your infrastructure, account privileges, and network configuration meet the Nutanix AOS environment requirements needed for a successful installation. 

## 1.3.1. Infrastructure requirements

You can install OpenShift Container Platform on on-premise Nutanix clusters, Nutanix Cloud Clusters (NC2) on Amazon Web Services (AWS), or NC2 on Microsoft Azure. 

## 1.3.2. Required account privileges

The installation program requires access to a Nutanix account with the necessary permissions to deploy the cluster and to maintain the daily operation of it. The following options are available to you: 

  * You can use a local Prism Central user account with administrative privileges. Using a local account is the quickest way to grant access to an account with the required permissions. 
  * If your organization’s security policies require that you use a more restrictive set of permissions, use the permissions that are listed in the following table to create a custom Cloud Native role in Prism Central. You can then assign the role to a user account that is a member of a Prism Central authentication directory. 



Consider the following when managing this user account: 

  * When assigning entities to the role, ensure that the user can access only the Prism Element and subnet that are required to deploy the virtual machines. 
  * Ensure that the user is a member of the project to which it needs to assign virtual machines. 



Table 1.2. Required permissions for creating a Custom Cloud Native roleNutanix Object| When required| Required permissions in Nutanix API| Description  
---|---|---|---  
Categories  |  Always  | 

  * `Create_Category_Mapping`
  * `Create_Or_Update_Name_Category`
  * `Create_Or_Update_Value_Category`
  * `Delete_Category_Mapping`
  * `Delete_Name_Category`
  * `Delete_Value_Category`
  * `View_Category_Mapping`
  * `View_Name_Category`
  * `View_Value_Category`

|  Create, read, and delete categories that are assigned to the OpenShift Container Platform machines.   
Images  |  Always  | 

  * `Create_Image`
  * `Delete_Image`
  * `View_Image`

|  Create, read, and delete the operating system images used for the OpenShift Container Platform machines.   
Virtual Machines  |  Always  | 

  * `Create_Virtual_Machine`
  * `Delete_Virtual_Machine`
  * `View_Virtual_Machine`

|  Create, read, and delete the OpenShift Container Platform machines.   
Clusters  |  Always  |  `View_Cluster` |  View the Prism Element clusters that host the OpenShift Container Platform machines.   
Subnets  |  Always  |  `View_Subnet` |  View the subnets that host the OpenShift Container Platform machines.   
Projects  |  If you will associate a project with compute machines, control plane machines, or all machines.  |  `View_Project` |  View the projects defined in Prism Central and allow a project to be assigned to the OpenShift Container Platform machines.   
Tasks  |  Always  |  `View_Task` |  Fetch and view tasks on the Prism Element that contain OpenShift Container Platform machines and nodes.   
Hosts  |  If you use GPUs with compute machines.  |  `View_Host` |  Fetch and view hosts on the Prism Element that have GPUs attached.   
Show more

## 1.3.3. Cluster limits

Available resources vary between clusters. The number of possible clusters within a Nutanix environment is limited primarily by available storage space and any limitations associated with the resources that the cluster creates, and resources that you require to deploy the cluster, such a IP addresses and networks. 

## 1.3.4. Cluster resources

A minimum of 800 GB of storage is required to use a standard cluster. 

When you deploy a OpenShift Container Platform cluster that uses installer-provisioned infrastructure, the installation program must be able to create several resources in your Nutanix instance. Although these resources use 856 GB of storage, the bootstrap node is destroyed as part of the installation process. 

A standard OpenShift Container Platform installation creates the following resources: 

  * 1 label 
  * Virtual machines: 

    * 1 disk image 
    * 1 temporary bootstrap node 
    * 3 control plane nodes 
    * 3 compute machines 




## 1.3.5. Networking requirements

You must use either AHV IP Address Management (IPAM) or Dynamic Host Configuration Protocol (DHCP) for the network and ensure that it is configured to provide persistent IP addresses to the cluster machines. Additionally, create the following networking resources before you install the OpenShift Container Platform cluster: 

  * IP addresses 
  * DNS records 



Nutanix Flow Virtual Networking is supported for new cluster installations. To use this feature, enable Flow Virtual Networking on your AHV cluster before installing. 

Note

It is recommended that each OpenShift Container Platform node in the cluster have access to a Network Time Protocol (NTP) server that is discoverable via DHCP. Installation is possible without an NTP server. However, an NTP server prevents errors typically associated with asynchronous server clocks. 

## 1.3.6. Required IP Addresses

An installer-provisioned installation requires two static virtual IP (VIP) addresses: 

  * A VIP address for the API is required. This address is used to access the cluster API. 
  * A VIP address for ingress is required. This address is used for cluster ingress traffic. 



You specify these IP addresses when you install the OpenShift Container Platform cluster. 

## 1.3.7. DNS records

You must create DNS records for two static IP addresses in the appropriate DNS server for the Nutanix instance that hosts your OpenShift Container Platform cluster. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster. 

If you use your own DNS or DHCP server, you must also create records for each node, including the bootstrap, control plane, and compute nodes. 

A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`. 

Table 1.3. Required DNS recordsComponent| Record| Description  
---|---|---  
API VIP  |  `api.<cluster_name>.<base_domain>.` |  This DNS A/AAAA or CNAME record must point to the load balancer for the control plane machines. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
Ingress VIP  |  `*.apps.<cluster_name>.<base_domain>.` |  A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the worker nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.   
Show more

## 1.3.8. Additional resources

  * [Nutanix Cloud Clusters on AWS](https://www.nutanix.com/products/nutanix-cloud-clusters/aws)
  * [Nutanix Cloud Clusters on Microsoft Azure](https://www.nutanix.com/products/nutanix-cloud-clusters/azure)
  * [Custom Cloud Native role](https://opendocs.nutanix.com/guides/cloud_native_role/)
  * [Assigning a role](https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Security-Guide:ssp-ssp-role-assignment-pc-t.html)
  * [Adding a user to a project](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Admin-Center-Guide-vpc_2023_1_0_1:ssp-projects-add-users-t.html)
  * [Flow Virtual Networking overview](https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Flow-Virtual-Networking-Guide-vpc_2024_1:ear-flow-nw-overview-pc.html)
