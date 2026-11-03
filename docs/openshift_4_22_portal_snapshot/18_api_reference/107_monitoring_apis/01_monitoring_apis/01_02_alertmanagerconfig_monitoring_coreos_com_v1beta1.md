# 1.2. AlertmanagerConfig [monitoring.coreos.com/v1beta1]

Description
    

The `AlertmanagerConfig` custom resource definition (CRD) defines how `Alertmanager` objects process Prometheus alerts. It allows to specify alert grouping and routing, notification receivers and inhibition rules. 

`Alertmanager` objects select `AlertmanagerConfig` objects using label and namespace selectors. 

Type
     `object`
