# 4.1. Limitations of load balancer services

OpenShift Container Platform clusters on Red Hat OpenStack Platform (RHOSP) use Octavia to handle load balancer services. As a result of this choice, such clusters might have functional limitations. 

OpenShift Container Platform clusters on Red Hat OpenStack Platform (RHOSP) use Octavia to handle load balancer services. As a result, your cluster has several functional limitations. 

RHOSP Octavia has two supported providers: Amphora and OVN. These providers differ in available features and implementation details. These distinctions affect load balancer services that you create on your cluster. 

## 4.1.1. Local external traffic policies

You can set the external traffic policy (ETP) parameter, `.spec.externalTrafficPolicy`, on a load balancer service to preserve the source IP address of incoming traffic when it reaches service endpoint pods. 

If your cluster uses the Amphora Octavia provider, the source IP of the traffic is replaced with the IP address of the Amphora VM. This behavior does not occur if your cluster uses the OVN Octavia provider. 

Having the `ETP` option set to `Local` requires creating health monitors for the load balancer. Without health monitors, traffic can be routed to a node that does not have a functional endpoint, which causes the connection to drop. To force Cloud Provider OpenStack to create health monitors, you must set the value of the `create-monitor` option in the cloud provider configuration to `true`. 

In RHOSP 16.2, the OVN Octavia provider does not support health monitors. Therefore, setting the ETP to `Local` is unsupported. 

In RHOSP 16.2, the Amphora Octavia provider does not support HTTP monitors on UDP pools. As a result, UDP load balancer services have `UDP-CONNECT` monitors created instead. Due to implementation details, this configuration only functions properly with the OVN-Kubernetes CNI plugin.
