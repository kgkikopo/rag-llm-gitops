# 13.1. Service accounts

You can use OpenShift Container Platform service accounts to allow a OpenShift Container Platform component to directly access the API. 

Service accounts are API objects that exist within each project that provide a flexible way to control API access without sharing a regular user’s credentials. 

When you use the OpenShift Container Platform CLI or web console, your API token authenticates you to the API. You can associate a component with a service account so that they can access the API without using a regular user’s credentials. 

For example, service accounts can allow: 

  * Replication controllers to make API calls to create or delete pods 
  * Applications inside containers to make API calls for discovery purposes 
  * External applications to make API calls for monitoring or integration purposes 



Each service account’s user name is derived from its project and name: 

```plaintext
system:serviceaccount:<project>:<name>
```


Every service account is also a member of two groups: 

Group| Description  
---|---  
system:serviceaccounts  |  Includes all service accounts in the system.   
system:serviceaccounts:<project> |  Includes all service accounts in the specified project.   
Show more
