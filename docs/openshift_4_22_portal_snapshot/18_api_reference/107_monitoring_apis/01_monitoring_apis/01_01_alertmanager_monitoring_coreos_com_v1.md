# 1.1. Alertmanager [monitoring.coreos.com/v1]

Description
    

The `Alertmanager` custom resource definition (CRD) defines a desired [Alertmanager](<https://prometheus.io/docs/alerting>) setup to run in a Kubernetes cluster. It allows to specify many options such as the number of replicas, persistent storage and many more. 

For each `Alertmanager` resource, the Operator deploys a `StatefulSet` in the same namespace. When there are two or more configured replicas, the Operator runs the Alertmanager instances in high-availability mode. 

The resource defines via label and namespace selectors which `AlertmanagerConfig` objects should be associated to the deployed Alertmanager instances. 

Type
     `object`
