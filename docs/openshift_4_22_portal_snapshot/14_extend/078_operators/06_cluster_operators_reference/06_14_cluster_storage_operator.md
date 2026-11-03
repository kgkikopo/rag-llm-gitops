# 6.14. Cluster Storage Operator

The Cluster Storage Operator is an optional cluster capability that can be disabled by cluster administrators during installation. 

For more information about optional cluster capabilities, see "Cluster capabilities". 

The Cluster Storage Operator sets OpenShift Container Platform cluster-wide storage defaults. It ensures a default `storageclass` exists for OpenShift Container Platform clusters. It also installs Container Storage Interface (CSI) drivers which enable your cluster to use various storage backends. 

Configuration
     No configuration is required. 
Notes
     The storage class that the Operator creates can be made non-default by editing its annotation, but this storage class cannot be deleted if the Operator runs. 

**Additional resources**

  * [Storage capability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-storage-operator_cluster-capabilities)
  * [cluster-storage-operator](https://github.com/openshift/cluster-storage-operator)
