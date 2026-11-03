# 5.20. Red Hat Advanced Cluster Management (RHACM) CRs

The following custom resources (CRs) configure Red Hat Advanced Cluster Management (RHACM) for the telco hub cluster. 

Table 5.6. RHACM CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
RHACM  |  `acmAgentServiceConfig.yaml` |  Creates a policy to manage copying data from an object bucket claim into a secret for Observability to connect to Thanos.  |  No   
RHACM  |  `acmMCE.yaml` |  Defines the MultiCluster Engine configuration required by ACM.  |  No   
RHACM  |  `acmMCH.yaml` |  Configures a `MultiClusterHub` CR with high availability, enabling various components and specifying installation settings.  |  No   
RHACM  |  `acmMirrorRegistryCM.yaml` |  Defines the SSL certificates and mirror registry configuration for various Red Hat and OpenShift Container Platform registries used by the `multicluster-engine` in the `multicluster-engine` namespace.  |  No   
RHACM  |  `acmNS.yaml` |  Defines the `open-cluster-management` namespace with a label to enable cluster monitoring.  |  No   
RHACM  |  `acmOperGroup.yaml` |  Defines an OperatorGroup for the `open-cluster-management` namespace, targeting the same namespace.  |  No   
RHACM  |  `acmPerfSearch.yaml` |  Configures search for Open Cluster Management by defining various parameters and API settings.  |  No   
RHACM  |  `acmProvisioning.yaml` |  Configures a provisioning resource in the metal3.io/v1alpha1 API version to watch all namespaces.  |  No   
RHACM  |  `acmSubscription.yaml` |  Subscribes to the RHACM Operator using automatic install plan approval.  |  No   
RHACM  |  `observabilityMCO.yaml` |  Configures `MultiClusterObservability` for managing observability and alerting across multiple clusters.  |  No   
RHACM  |  `observabilityNS.yaml` |  Creates an `open-cluster-management-observability` namespace.  |  No   
RHACM  |  `observabilityOBC.yaml` |  Creates an `ObjectBucketClaim` CR in the `open-cluster-management-observability` namespace.  |  No   
RHACM  |  `observabilitySecret.yaml` |  Creates a Secret CR in the `open-cluster-management-observability` namespace for storing Docker configuration details.  |  No   
RHACM  |  `observabilityRoutePolicy.yaml` |  Policy to propagate RHACM observability route to the managed cluster.  |  No   
RHACM  |  `pullSecretMCSB.yaml` |  Creates a `ManagedClusterSetBinding` CR for the pull secret policy.  |  No   
RHACM  |  `pullSecretPlacementBinding.yaml` |  Creates the `PlacementBinding` CR needed for the pull secret policy.  |  No   
RHACM  |  `pullSecretPlacement.yaml` |  Creates the `Placement` CR against local cluster needed for the pull secret policy.  |  No   
RHACM  |  `pullSecretPolicy.yaml` |  Creates a policy to copy the global pull secret into observability namespaces.  |  No   
RHACM  |  `thanosSecretPlacementBinding.yaml` |  Creates the `PlacementBinding` CR needed for the thanos secret policy.  |  No   
RHACM  |  `thanosSecretPlacement.yaml` |  Creates the `Placement` CR against local cluster needed for the thanos secret policy.  |  No   
RHACM  |  `thanosSecretPolicy.yaml` |  Creates a policy to copy data from an object bucket claim into a secret for observability to connect to Thanos.  |  No   
TALM  |  `talmSubscription.yaml` |  Creates a `Subscription` CR for TALM.  |  No   
Show more
