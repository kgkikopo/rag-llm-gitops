# 2.5. IBM Cloud IAM policies and API key

To install OpenShift Container Platform into your IBM Cloud® account, the installation program requires an IAM API key, which provides authentication and authorization to access IBM Cloud® service APIs. You can use an existing IAM API key that contains the required policies or create a new one. 

For an IBM Cloud® IAM overview, see the "IBM Cloud® IAM overview" documentation. 

## 2.5.1. Prerequisite permissions

Table 2.1. Prerequisite permissionsRole| Access  
---|---  
Viewer, Operator, Editor, Administrator, Reader, Writer, Manager  |  Internet Services service in <resource_group> resource group   
Viewer, Operator, Editor, Administrator, User API key creator, Service ID creator  |  IAM Identity Service service   
Viewer, Operator, Administrator, Editor, Reader, Writer, Manager, Console Administrator  |  VPC Infrastructure Services service in <resource_group> resource group   
Viewer  |  Resource Group: Access to view the resource group itself. The resource type should equal `Resource group`, with a value of <your_resource_group_name>.   
Show more

## 2.5.2. Cluster-creation permissions

Table 2.2. Cluster-creation permissionsRole| Access  
---|---  
Viewer  |  <resource_group> (Resource Group Created for Your Team)   
Viewer, Operator, Editor, Reader, Writer, Manager  |  All Identity and IAM enabled services in Default resource group   
Viewer, Reader  |  Internet Services service   
Viewer, Operator, Reader, Writer, Manager, Content Reader, Object Reader, Object Writer, Editor  |  Cloud Object Storage service   
Viewer  |  Default resource group: The resource type should equal `Resource group`, with a value of `Default`. If your account administrator changed your account’s default resource group to something other than Default, use that value instead.   
Viewer, Operator, Editor, Reader, Manager  |  Workspace for IBM Power® Virtual Server service in <resource_group> resource group   
Viewer, Operator, Editor, Reader, Writer, Manager, Administrator  |  Internet Services service in <resource_group> resource group: CIS functional scope string equals reliability   
Viewer, Operator, Editor  |  Transit Gateway service   
Viewer, Operator, Editor, Administrator, Reader, Writer, Manager, Console Administrator  |  VPC Infrastructure Services service <resource_group> resource group   
Show more

## 2.5.3. Access policy assignment

In IBM Cloud® IAM, access policies can be attached to different subjects: 

  * Access group (Recommended) 
  * Service ID 
  * User 



Note

The recommended method is to define IAM access policies in an access group. This helps organize all the access required for OpenShift Container Platform and enables you to onboard users and service IDs to this group. You can also assign access to users and service IDs directly, if desired. 

For more information, see "Access groups" and "Users and service IDs". 

**Additional resources**

  * [IBM Cloud® IAM overview](https://cloud.ibm.com/docs/account?topic=account-iamoverview)
  * [Access groups (IBM Cloud® documentation)](https://cloud.ibm.com/docs/account?topic=account-groups)
  * [Users and service IDs (IBM Cloud® documentation)](https://cloud.ibm.com/docs/account?topic=account-assign-access-resources)



## 2.5.4. Creating an API key

You must create a user API key or a service ID API key for your IBM Cloud® account. 

**Prerequisites**

  * You have assigned the required access policies to your IBM Cloud® account. 
  * You have attached your IAM access policies to an access group, or other appropriate resource. 



**Procedure**

  * Create an API key, depending on how you defined your IAM access policies. 

For example, if you assigned your access policies to a user, you must create a user API key. If you assigned your access policies to a service ID, you must create a service ID API key. If your access policies are assigned to an access group, you can use either API key type. For more information on IBM Cloud® API keys, see "User API key", "Service ID API key", and "Understanding API keys". 




**Additional resources**

  * [User API key (IBM Cloud® documentation)](https://cloud.ibm.com/docs/account?topic=account-userapikey)
  * [Service ID API key (IBM Cloud® documentation)](https://cloud.ibm.com/docs/account?topic=account-serviceidapikeys)
  * [Understanding API keys (IBM Cloud® documentation)](https://cloud.ibm.com/docs/account?topic=account-manapikey&interface=ui)
