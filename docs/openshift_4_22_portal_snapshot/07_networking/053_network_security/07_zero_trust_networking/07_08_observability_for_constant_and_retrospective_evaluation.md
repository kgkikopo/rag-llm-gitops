# 7.8. Observability for constant, and retrospective, evaluation

After you have a running cluster, you want to be able to observe the traffic and verify that the traffic comports with the defined rules. This is important for intrusion detection, forensics, and is helpful for operational load management. 

Leverage: 

  * [Network Observability Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_observability/#installing-network-observability-operators): Allows for inspection, monitoring, and alerting on network connections to pods and nodes in the cluster. 
  * [Red Hat Advanced Cluster Management (RHACM) for Kubernetes](https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes): Monitors, collects, and evaluates system-level events such as process execution, network connections and flows, and privilege escalation. It can determine a baseline for a cluster, and then detect anomalous activity and alert you about it. 
  * [Red Hat OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-about): Can [monitor traffic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-kiali-overview_ossm-architecture) entering and leaving a pod. 
  * [Red Hat OpenShift Distributed Tracing Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#understanding-distributed-tracing): For suitably instrumented applications, you can see all traffic associated with a particular action as it splits into sub-requests to microservices. This allows you to identify bottlenecks within a distributed application.
