# 12.1. Service accounts

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

## 12.1.1. Automatically generated image pull secrets

OpenShift Container Platform automatically creates image pull secrets for each service account to integrate the internal image registry with user authentication. 

Note

Prior to OpenShift Container Platform 4.16, a long-lived service account API token secret was also generated for each service account that was created. Starting with OpenShift Container Platform 4.16, this service account API token secret is no longer created. 

After upgrading to 4.22, any existing long-lived service account API token secrets are not deleted and will continue to function. For information about detecting long-lived API tokens that are in use in your cluster or deleting them if they are not needed, see "Long-lived service account API tokens in OpenShift Container Platform (Red Hat Knowledgebase)". 

This image pull secret is necessary to integrate the OpenShift image registry into the cluster’s user authentication and authorization system. 

However, if you do not enable the `ImageRegistry` capability or if you disable the integrated OpenShift image registry in the Cluster Image Registry Operator’s configuration, an image pull secret is not generated for each service account. 

When the integrated OpenShift image registry is disabled on a cluster that previously had it enabled, the previously generated image pull secrets are deleted automatically.
