# 6.28. Marketplace Operator

The Marketplace Operator is an optional cluster capability that can be disabled by cluster administrators if it is not needed. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_. 

The Marketplace Operator simplifies the process for bringing off-cluster Operators to your cluster by using a set of default Operator Lifecycle Manager (OLM) catalogs on the cluster. 

When the Marketplace Operator is installed, it creates the `openshift-marketplace` namespace. OLM ensures catalog sources installed in the `openshift-marketplace` namespace are available for all namespaces on the cluster. 

**Additional resources**

  * [Marketplace capability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#marketplace-operator_cluster-capabilities)
  * [operator-marketplace](https://github.com/operator-framework/operator-marketplace)
