# 1.11. ThanosRuler [monitoring.coreos.com/v1]

Description
    

The `ThanosRuler` custom resource definition (CRD) defines a desired [Thanos Ruler](<https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md>) setup to run in a Kubernetes cluster. 

A `ThanosRuler` instance requires at least one compatible Prometheus API endpoint (either Thanos Querier or Prometheus services). 

The resource defines via label and namespace selectors which `PrometheusRule` objects should be associated to the deployed Thanos Ruler instances. 

Type
     `object`
