# 5.21. Storage reference CRs

The following custom resources (CRs) configure storage for the telco hub cluster. 

Table 5.7. Storage CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Local Storage Operator  |  `lsoLocalVolume.yaml` |  Defines a `LocalVolume` CR specifying local storage configuration and node selection criteria.  |  Yes   
Local Storage Operator  |  `lsoNS.yaml` |  Defines the `openshift-local-storage` namespace.  |  Yes   
Local Storage Operator  |  `lsoOperatorGroup.yaml` |  Defines an `OperatorGroup` for the `openshift-local-storage` namespace.  |  Yes   
Local Storage Operator  |  `lsoSubscription.yaml` |  Defines a `Subscription` CR for the Local Storage Operator.  |  Yes   
OpenShift Data Foundation  |  `odfNS.yaml` |  Defines the `openshift-storage namespace` with specific annotations and labels for workload management and cluster monitoring.  |  Yes   
OpenShift Data Foundation  |  `odfOperatorGroup.yaml` |  Defines an `OperatorGroup` for the `openshift-storage` namespace.  |  Yes   
OpenShift Data Foundation  |  `odfReady.yaml` |  Defines a resource to verify readiness of the ODF deployment.  |  Yes   
OpenShift Data Foundation  |  `odfSubscription.yaml` |  Configures an OpenShift Container Platform subscription to the Red Hat OpenShift Data Foundation Operator, specifying installation details such as the Operator’s name, namespace, channel, and approval strategy.  |  Yes   
OpenShift Data Foundation  |  `storageCluster.yaml` |  Defines a `StorageCluster` CR with specific resource requests and limits, storage device sets, and annotations for Argo CD synchronization.  |  No   
Show more
