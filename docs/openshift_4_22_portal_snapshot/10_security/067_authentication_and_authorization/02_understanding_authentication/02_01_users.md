# 2.1. Users

A user in OpenShift Container Platform is an entity that makes API requests and can be granted permissions through role assignments. Users include regular users, system users for infrastructure components, and service accounts associated with projects. 

Several types of users can exist: 

User type| Description  
---|---  
`Regular users` |  This is the way most interactive OpenShift Container Platform users are represented. Regular users are created automatically in the system upon first login or can be created via the API. Regular users are represented with the `User` object. Examples: `joe` `alice`  
`System users` |  Many of these are created automatically when the infrastructure is defined, mainly for the purpose of enabling the infrastructure to interact with the API securely. They include a cluster administrator (with access to everything), a per-node user, users for use by routers and registries, and various others. Finally, there is an `anonymous` system user that is used by default for unauthenticated requests. Examples: `system:admin` `system:openshift-registry` `system:node:node1.example.com`  
`Service accounts` |  These are special system users associated with projects; some are created automatically when the project is first created, while project administrators can create more for the purpose of defining access to the contents of each project. Service accounts are represented with the `ServiceAccount` object. Examples: `system:serviceaccount:default:deployer` `system:serviceaccount:foo:builder`  
Show more

Each user must authenticate in some way to access OpenShift Container Platform. API requests with no authentication or invalid authentication are authenticated as requests by the `anonymous` system user. After authentication, policy determines what the user is authorized to do.
