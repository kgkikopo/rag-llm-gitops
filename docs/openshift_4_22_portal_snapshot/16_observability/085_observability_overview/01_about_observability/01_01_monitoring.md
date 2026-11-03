# 1.1. Monitoring

Monitor the in-cluster health and performance of your applications running on OpenShift Container Platform with metrics and customized alerts for CPU and memory usage, network connectivity, and other resource usage. Monitoring stack components are deployed and managed by the Cluster Monitoring Operator. 

Monitoring stack components are deployed by default in every OpenShift Container Platform installation and are managed by the Cluster Monitoring Operator (CMO). These components include Prometheus, Alertmanager, Thanos Querier, and others. The CMO also deploys the Telemeter Client, which sends a subset of data from platform Prometheus instances to Red Hat to facilitate Remote Health Monitoring for clusters. 

For more information, see [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/about_monitoring/about-ocp-monitoring) and [About remote health monitoring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#about-remote-health-monitoring).
