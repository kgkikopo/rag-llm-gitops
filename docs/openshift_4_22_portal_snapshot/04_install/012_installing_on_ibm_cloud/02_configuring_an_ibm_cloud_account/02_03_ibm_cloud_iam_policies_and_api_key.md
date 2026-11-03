# 2.3. IBM Cloud IAM policies and API key

To install OpenShift Container Platform into your IBM Cloud® account, the installation program requires an IAM API key, which provides authentication and authorization to access IBM Cloud® service APIs. You can use an existing IAM API key that contains the required policies or create a new one. 

For an IBM Cloud® IAM overview, see the "IBM Cloud® IAM overview" documentation. 

## 2.3.1. Required access policies

You must assign the required access policies to your IBM Cloud® account. 

Table 2.2. Required access policiesService type| Service| Access policy scope| Platform access| Service access  
---|---|---|---|---  
Account management  |  IAM Identity Service  |  All resources or a subset of resources  |  Editor, Operator, Viewer, Administrator  |  Service ID creator   
Account management  |  Identity and Access Management  |  All resources  |  Editor, Operator, Viewer, Administrator  |   
Account management  |  Resource group only  |  All resource groups in the account  |  Administrator  |   
IAM services  |  Cloud Object Storage  |  All resources or a subset of resources  |  Editor, Operator, Viewer, Administrator  |  Reader, Writer, Manager, Content Reader, Object Reader, Object Writer   
IAM services  |  Internet Services  |  All resources or a subset of resources  |  Editor, Operator, Viewer, Administrator  |  Reader, Writer, Manager   
IAM services  |  DNS Services  |  All resources or a subset of resources  |  Editor, Operator, Viewer, Administrator  |  Reader, Writer, Manager   
IAM services  |  VPC Infrastructure Services  |  All resources or a subset of resources  |  Editor, Operator, Viewer, Administrator  |  Reader, Writer, Manager   
Show more

where: 

`All resources or a subset of resources`
     The policy access scope should be set based on how granular you want to assign access. The scope can be set to **All resources** or **Resources based on selected attributes**. 
`Identity and Access Management`
     This access policy is optional. It is only required if you want the installation program to create a resource group. For more information about resource groups, see the "IBM® resource groups documentation". 

## 2.3.2. Access policy assignment

In IBM Cloud® IAM, access policies can be attached to different subjects: 

  * Access group (Recommended) 
  * Service ID 
  * User 



Note

The recommended method is to define IAM access policies in an access group. This helps organize all the access required for OpenShift Container Platform and enables you to onboard users and service IDs to this group. You can also assign access to users and service IDs directly, if desired. 

For more information, see "Access groups" and "Users and service IDs". 

## 2.3.3. Creating an API key

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
