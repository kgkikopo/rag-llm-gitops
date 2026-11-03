# Chapter 9. Prometheus [monitoring.coreos.com/v1]

Description
    

The `Prometheus` custom resource definition (CRD) defines a desired [Prometheus](<https://prometheus.io/docs/prometheus>) setup to run in a Kubernetes cluster. It allows to specify many options such as the number of replicas, persistent storage, and Alertmanagers where firing alerts should be sent and many more. 

For each `Prometheus` resource, the Operator deploys one or several `StatefulSet` objects in the same namespace. The number of StatefulSets is equal to the number of shards which is 1 by default. 

The resource defines via label and namespace selectors which `ServiceMonitor`, `PodMonitor`, `Probe` and `PrometheusRule` objects should be associated to the deployed Prometheus instances. 

The Operator continuously reconciles the scrape and rules configuration and a sidecar container running in the Prometheus pods triggers a reload of the configuration when needed. 

Type
     `object`
Required
    

  * `spec`

- [9.1. Specification](09_01_specification.md)
- [9.2. API endpoints](09_02_api_endpoints.md)
