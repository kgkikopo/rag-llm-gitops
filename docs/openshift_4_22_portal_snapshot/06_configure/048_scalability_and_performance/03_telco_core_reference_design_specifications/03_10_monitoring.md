# 3.10. Monitoring

The Cluster Monitoring Operator (CMO) is included by default in OpenShift Container Platform and provides monitoring for the platform components and optionally user projects. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

The Cluster Monitoring Operator (CMO) is included by default in OpenShift Container Platform and provides monitoring (metrics, dashboards, and alerting) for the platform components and optionally user projects. You can customize the default log retention period, custom alert rules, and so on. 

Configuration of the monitoring stack is done through a single string value in the cluster-monitoring-config ConfigMap. The reference tuning merges content from two requirements: 

  * Prometheus configuration is extended to forward alerts to the Red Hat Advanced Cluster Management (RHACM) hub cluster for alert aggregation. If required, you can extend this configuration to forward alerts to additional locations. 
  * Prometheus retention period is reduced from the default. The primary metrics storage is typically external to the cluster. Metrics storage on the core cluster is typically a backup to that central store and available for local troubleshooting purposes. You can add a `remoteWrite` endpoint to the Prometheus configuration to directly forward metrics to the central store. 



In addition to the default configuration, telco core clusters typically configure pod CPU and memory metrics and alerts for user workloads. 

Engineering considerations
    

  * The Prometheus retention period is specified by the user. The value used is a tradeoff between operational requirements for maintaining historical data on the cluster against CPU and storage resources. Longer retention periods increase the need for storage and require additional CPU to manage the indexing of data. 



**Additional resources**

  * [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/about_monitoring/about-ocp-monitoring)
