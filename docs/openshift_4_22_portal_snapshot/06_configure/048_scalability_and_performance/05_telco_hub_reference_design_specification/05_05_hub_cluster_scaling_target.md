# 5.5. Hub cluster scaling target

The resource requirements for the hub cluster are directly dependent on the number of clusters being managed by the hub, the number of policies used for each managed cluster, and the set of features that are configured in Red Hat Advanced Cluster Management (RHACM). 

The hub cluster reference configuration can support up to 3500 managed single-node OpenShift clusters under the following conditions: 

  * 10 RHACM configuration policies (comprising 5 Red Hat-provided policies and up to 5 custom configuration policies) with hub-side templating bound to the 3500 clusters and configured with a 10 minute evaluation interval. 
  * Only the following RHACM add-ons are enabled: 

    * Policy controller 
    * Observability with the default configuration 

  * You deploy managed clusters by using GitOps ZTP in batches of up to 500 clusters at a time. 



The reference configuration is also validated for deployment and management of a mix of managed cluster topologies. The specific limits depend on the mix of cluster topologies, enabled RHACM features, and so on. In a mixed topology scenario, the reference hub configuration is validated with a combination of 1200 single-node OpenShift clusters, 400 compact clusters (3 nodes combined control plane and compute nodes), and 230 standard clusters (3 control plane and 2 worker nodes). 

A hub cluster conforming to this reference specification can support synchronization of 1000 single node `ClusterInstance` CRs for each ArgoCD application. You can use multiple applications to achieve the maximum number of clusters supported by a single hub cluster. 

Note

Specific dimensioning requirements are highly dependent on the cluster topology and workload. For more information, see "Storage requirements". Adjust cluster dimensions for the specific characteristics of your fleet of managed clusters.
