# Chapter 3. AlertmanagerConfig [monitoring.coreos.com/v1beta1]

Description
    

The `AlertmanagerConfig` custom resource definition (CRD) defines how `Alertmanager` objects process Prometheus alerts. It allows to specify alert grouping and routing, notification receivers and inhibition rules. 

`Alertmanager` objects select `AlertmanagerConfig` objects using label and namespace selectors. 

Type
     `object`
Required
    

  * `spec`

- [3.1. Specification](03_01_specification.md)
- [3.2. API endpoints](03_02_api_endpoints.md)
