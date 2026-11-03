# Chapter 11. ServiceMonitor [monitoring.coreos.com/v1]

Description
    

The `ServiceMonitor` custom resource definition (CRD) defines how `Prometheus` and `PrometheusAgent` can scrape metrics from a group of services. Among other things, it allows to specify: * The services to scrape via label selectors. * The container ports to scrape. * Authentication credentials to use. * Target and metric relabeling. 

`Prometheus` and `PrometheusAgent` objects select `ServiceMonitor` objects using label and namespace selectors. 

Type
     `object`
Required
    

  * `spec`

- [11.1. Specification](11_01_specification.md)
- [11.2. API endpoints](11_02_api_endpoints.md)
