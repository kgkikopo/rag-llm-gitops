# 4.7. High availability For ExternalIP

High availability for `ExternalIP` in non-cloud clusters of OpenShift Container Platform combines IP failover with `ExternalIP` auto-assignment to ensure services remain accessible when nodes fail. You can configure this by using the same CIDR range for both `ExternalIP` auto-assignment and IP failover. 

To configure high availability for `ExternalIP`, you can specify a `spec.ExternalIP.autoAssignCIDRs` range of the cluster network configuration, and then use the same range in creating the IP failover configuration. 

Because IP failover can support up to a maximum of 255 VIPs for the entire cluster, the `spec.ExternalIP.autoAssignCIDRs` must be `/24` or smaller. 

**Additional resources**

  * [Configuration for ExternalIP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#configuration-externalip_configuring-externalip)
  * [Kubernetes documentation on ExternalIP](https://kubernetes.io/docs/concepts/services-networking/service/#external-ips)
