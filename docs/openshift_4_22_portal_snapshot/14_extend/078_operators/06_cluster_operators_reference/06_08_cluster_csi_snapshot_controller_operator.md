# 6.8. Cluster CSI Snapshot Controller Operator

The Cluster CSI Snapshot Controller Operator is an optional cluster capability that can be disabled by cluster administrators during installation. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_. 

The Cluster CSI Snapshot Controller Operator installs and maintains the CSI Snapshot Controller. The CSI Snapshot Controller is responsible for watching the `VolumeSnapshot` CRD objects and manages the creation and deletion lifecycle of volume snapshots. 

**Additional resources**

  * [CSI snapshot controller capability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-csi-snapshot-controller-operator_cluster-capabilities)
  * [cluster-csi-snapshot-controller-operator](https://github.com/openshift/cluster-csi-snapshot-controller-operator)
