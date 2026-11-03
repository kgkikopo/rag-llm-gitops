# 5.23. Logging reference CRs

The following custom resources (CRs) configure logging for the telco hub cluster. 

Table 5.9. Logging CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Cluster Logging Operator  |  `clusterLogForwarder.yaml` |  Defines the `ClusterLogForwarder` CR to send logs to configured outputs.  |  Yes   
Cluster Logging Operator  |  `clusterLogNS.yaml` |  Configures a namespace for the Cluster Logging Operator.  |  Yes   
Cluster Logging Operator  |  `clusterLogOperGroup.yaml` |  Configures an Operator group for the Cluster Logging Operator.  |  Yes   
Cluster Logging Operator  |  `clusterLogServiceAccount.yaml` |  Defines the `ServiceAccount` CR used by Cluster Logging Operator components.  |  Yes   
Cluster Logging Operator  |  `clusterLogServiceAccountAuditBinding.yaml` |  Binds the Cluster Logging `ServiceAccount` CR to audit log roles.  |  Yes   
Cluster Logging Operator  |  `clusterLogServiceAccountInfrastructureBinding.yaml` |  Binds the Cluster Logging `ServiceAccount` CR to infrastructure log roles.  |  Yes   
Cluster Logging Operator  |  `clusterLogSubscription.yaml` |  Defines a subscription for installing and managing the Cluster Logging Operator.  |  Yes   
Show more
