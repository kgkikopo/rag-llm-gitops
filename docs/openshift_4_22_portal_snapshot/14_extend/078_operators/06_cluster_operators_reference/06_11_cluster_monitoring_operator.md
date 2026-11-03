# 6.11. Cluster Monitoring Operator

The Cluster Monitoring Operator (CMO) manages and updates the Prometheus-based cluster monitoring stack deployed on top of OpenShift Container Platform. 

CRDs
    

  * `alertmanagers.monitoring.coreos.com`

    * Scope: Namespaced 
    * CR: `alertmanager`
    * Validation: Yes 

  * `prometheuses.monitoring.coreos.com`

    * Scope: Namespaced 
    * CR: `prometheus`
    * Validation: Yes 

  * `prometheusrules.monitoring.coreos.com`

    * Scope: Namespaced 
    * CR: `prometheusrule`
    * Validation: Yes 

  * `servicemonitors.monitoring.coreos.com`

    * Scope: Namespaced 
    * CR: `servicemonitor`
    * Validation: Yes 




Configuration objects
    

```shell-session
$ oc -n openshift-monitoring edit cm cluster-monitoring-config
```


**Additional resources**

  * [openshift-monitoring](https://github.com/openshift/cluster-monitoring-operator)
