# 6.4. Cluster Autoscaler Operator

The Cluster Autoscaler Operator manages deployments of the OpenShift Cluster Autoscaler using the `cluster-api` provider. 

## 6.4.1. CRDs

  * `ClusterAutoscaler`: This is a singleton resource, which controls the configuration autoscaler instance for the cluster. The Operator only responds to the `ClusterAutoscaler` resource named `default` in the managed namespace, the value of the `WATCH_NAMESPACE` environment variable. 
  * `MachineAutoscaler`: This resource targets a node group and manages the annotations to enable and configure autoscaling for that group, the `min` and `max` size. Currently only `MachineSet` objects can be targeted. 



**Additional resources**

  * [cluster-autoscaler-operator](https://github.com/openshift/cluster-autoscaler-operator)
