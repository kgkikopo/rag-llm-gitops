# Chapter 7. PodMonitor [monitoring.coreos.com/v1]

Description
    

The `PodMonitor` custom resource definition (CRD) defines how `Prometheus` and `PrometheusAgent` can scrape metrics from a group of pods. Among other things, it allows to specify: * The pods to scrape via label selectors. * The container ports to scrape. * Authentication credentials to use. * Target and metric relabeling. 

`Prometheus` and `PrometheusAgent` objects select `PodMonitor` objects using label and namespace selectors. 

Type
     `object`
Required
    

  * `spec`

- [7.1. Specification](07_01_specification.md)
- [7.2. API endpoints](07_02_api_endpoints.md)
