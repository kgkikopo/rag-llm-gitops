# 2.2. Groups

Groups represent sets of users and simplify authorization management by allowing administrators to grant permissions to multiple users simultaneously rather than individually. OpenShift Container Platform includes both explicitly defined groups and automatically provisioned virtual groups. 

In addition to explicitly defined groups, there are also system groups, or _virtual groups_ , that are automatically provisioned by the cluster. 

The following default virtual groups are most important: 

Virtual group| Description  
---|---  
`system:authenticated` |  Automatically associated with all authenticated users.   
`system:authenticated:oauth` |  Automatically associated with all users authenticated with an OAuth access token.   
`system:unauthenticated` |  Automatically associated with all unauthenticated users.   
Show more
