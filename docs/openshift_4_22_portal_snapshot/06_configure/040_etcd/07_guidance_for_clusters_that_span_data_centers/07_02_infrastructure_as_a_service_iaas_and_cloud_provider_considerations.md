# 7.2. Infrastructure as a Service (IaaS) and cloud provider considerations

Review infrastructure and cloud provider constraints for multisite OpenShift Container Platform control planes so you can plan maximum transmission unit (MTU), latency, and storage requirements. 

This guidance applies to any infrastructure provider for which OpenShift Container Platform control plane nodes are supported by the user-provisioned infrastructure installer (platform=none) or the agent-based installer (platform=metal) using the ”User Managed Network” option. 

Installer-provisioned infrastructure installers are not covered by these guidelines, however, where possible, installer-provisioned infrastructure deployments will span zones or availability zones on cloud or IaaS providers if possible by following these or similar guidelines. This means infrastructure provider-specific integrations will not be available; for example, integration with cloud provider services such as storage services and load balancers. Provider-specific services might still be used as external services. 

Using different infrastructure platform providers for control plane nodes is discouraged; for example, mixing nodes across IaaS, cloud, and bare metal as control plane nodes. Consider the following guidelines when such combinations are needed: 

  * The minimum effective MTU across the infrastructure should be the maximum MTU used for the deployment. Using a lower MTU is acceptable. See "Understanding and Validating MTU setting with OpenShift Container Platform 4.x" for more information. 
  * The combined disk and network latency and jitter must keep an etcd peer round-trip time (RTT) of less than 100 ms. This is not the same as the network RTT. 
  * Layered products might have lower latency requirements. In those cases, the latency limits are dictated by the requirements of the architecture supported by the layered product. For example, OpenShift Container Platform cluster deployments that span data centers with Red Hat OpenShift Data Foundation must have a latency requirement of less than 10 ms RTT. For those cases, follow the specific product guidance. 
  * For guidance on cluster deployments that span data centers using OpenShift Data Foundation as the storage provider, see "Configuring OpenShift Data Foundation Disaster Recovery for OpenShift Workloads". 



**Additional resources**

  * [Understanding and Validating MTU setting with OpenShift Container Platform 4.x (Red Hat Knowledgebase)](https://access.redhat.com/articles/7010220)
  * [Configuring OpenShift Data Foundation Disaster Recovery for OpenShift Workloads](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.19/html-single/configuring_openshift_data_foundation_disaster_recovery_for_openshift_workloads/index)
