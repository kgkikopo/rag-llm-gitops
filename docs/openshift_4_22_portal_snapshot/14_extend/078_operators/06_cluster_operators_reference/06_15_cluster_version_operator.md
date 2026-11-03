# 6.15. Cluster Version Operator

Cluster Operators manage specific areas of cluster functionality. The Cluster Version Operator (CVO) manages the lifecycle of cluster Operators, many of which are installed in OpenShift Container Platform by default. 

The CVO also checks with the OpenShift Update Service to see the valid updates and update paths based on current component versions and information in the graph by collecting the status of both the cluster version and its cluster Operators. This status includes the condition type, which informs you of the health and current state of the OpenShift Container Platform cluster. 

For more information regarding cluster version condition types, see "Understanding cluster version condition types". 

**Additional resources**

  * [Understanding cluster version condition types](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#understanding-clusterversion-conditiontypes_understanding-openshift-updates)
  * [cluster-version-operator](https://github.com/openshift/cluster-version-operator)
