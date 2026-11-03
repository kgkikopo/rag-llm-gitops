# 1.10. ServiceMonitor [monitoring.coreos.com/v1]

Description
    

The `ServiceMonitor` custom resource definition (CRD) defines how `Prometheus` and `PrometheusAgent` can scrape metrics from a group of services. Among other things, it allows to specify: * The services to scrape via label selectors. * The container ports to scrape. * Authentication credentials to use. * Target and metric relabeling. 

`Prometheus` and `PrometheusAgent` objects select `ServiceMonitor` objects using label and namespace selectors. 

Type
     `object`
