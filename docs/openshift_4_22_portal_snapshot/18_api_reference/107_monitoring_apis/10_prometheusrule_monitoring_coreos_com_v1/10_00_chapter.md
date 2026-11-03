# Chapter 10. PrometheusRule [monitoring.coreos.com/v1]

Description
    

The `PrometheusRule` custom resource definition (CRD) defines [alerting](<https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>) and [recording](<https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/>) rules to be evaluated by `Prometheus` or `ThanosRuler` objects. 

`Prometheus` and `ThanosRuler` objects select `PrometheusRule` objects using label and namespace selectors. 

Type
     `object`
Required
    

  * `spec`

- [10.1. Specification](10_01_specification.md)
- [10.2. API endpoints](10_02_api_endpoints.md)
