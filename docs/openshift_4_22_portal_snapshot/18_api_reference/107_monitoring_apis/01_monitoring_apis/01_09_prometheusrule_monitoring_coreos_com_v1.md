# 1.9. PrometheusRule [monitoring.coreos.com/v1]

Description
    

The `PrometheusRule` custom resource definition (CRD) defines [alerting](<https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>) and [recording](<https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/>) rules to be evaluated by `Prometheus` or `ThanosRuler` objects. 

`Prometheus` and `ThanosRuler` objects select `PrometheusRule` objects using label and namespace selectors. 

Type
     `object`
