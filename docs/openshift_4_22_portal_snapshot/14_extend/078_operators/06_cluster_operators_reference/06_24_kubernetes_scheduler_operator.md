# 6.24. Kubernetes Scheduler Operator

The Kubernetes Scheduler Operator manages and updates the Kubernetes Scheduler deployed on top of OpenShift Container Platform. The Operator is based on the OpenShift Container Platform `library-go` framework and it is installed with the Cluster Version Operator (CVO). 

The Kubernetes Scheduler Operator contains the following components: 

  * Operator 
  * Bootstrap manifest renderer 
  * Installer based on static pods 
  * Configuration observer 



By default, the Operator exposes Prometheus metrics through the metrics service. 

## 6.24.1. Configuration

The configuration for the Kubernetes Scheduler is the result of merging: 

  * a default configuration. 
  * an observed configuration from the spec `schedulers.config.openshift.io`. 



All of these are sparse configurations, invalidated JSON snippets which are merged to form a valid configuration at the end. 

**Additional resources**

  * [cluster-kube-scheduler-operator](https://github.com/openshift/cluster-kube-scheduler-operator)
