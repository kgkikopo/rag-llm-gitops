# 6.23. Kubernetes Controller Manager Operator

The Kubernetes Controller Manager Operator manages and updates the Kubernetes Controller Manager deployed on top of OpenShift Container Platform. The Operator is based on OpenShift Container Platform `library-go` framework and it is installed via the Cluster Version Operator (CVO). 

It contains the following components: 

  * Operator 
  * Bootstrap manifest renderer 
  * Installer based on static pods 
  * Configuration observer 



By default, the Operator exposes Prometheus metrics through the `metrics` service. 

**Additional resources**

  * [`cluster-kube-controller-manager-operator`](https://github.com/openshift/cluster-kube-controller-manager-operator)
