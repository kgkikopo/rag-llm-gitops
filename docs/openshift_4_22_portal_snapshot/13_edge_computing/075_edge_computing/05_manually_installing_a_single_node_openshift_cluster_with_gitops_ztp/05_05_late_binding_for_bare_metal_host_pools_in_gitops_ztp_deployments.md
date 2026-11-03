# 5.5. Late binding for bare-metal host pools in GitOps ZTP deployments

In the standard GitOps ZTP flow, the `InfraEnv` custom resource (CR) references a specific `ClusterDeployment` CR, and all discovered hosts are automatically associated with that cluster. 

Late binding separates host discovery from cluster assignment, so you can manage a pool of bare-metal hosts independently from cluster lifecycle. 

With late binding, you create an `InfraEnv` CR without a `ClusterDeployment` reference, so that all hosts booted from the discovery ISO remain unbound and available for assignment to any cluster. You then use the `bmac.agent-install.openshift.io/cluster-reference` annotation on `BareMetalHost` resources to declaratively bind individual hosts to specific `ClusterDeployment` CRs. This annotation-based binding is compatible with GitOps workflows such as ArgoCD. 

Late binding in the GitOps ZTP workflow is designed for environments where hardware provisioning and cluster creation happen independently. Common scenarios include: 

  * An infrastructure team boots a set of bare-metal servers from a single discovery ISO, and a platform team later assigns subsets of those hosts to different clusters as demand arises. 
  * Hardware provisioning and cluster creation are handled by different teams at different times. 
  * Spare bare metal capacity must be allocated to clusters as workload requirements change. 



If you are deploying a single cluster where all discovered hosts belong to that cluster, use the standard GitOps ZTP flow with a `ClusterDeployment` reference in the `InfraEnv` CR. 

**Additional resources**

  * [Bind bare-metal hosts to clusters using the cluster-reference annotation in GitOps ZTP deployments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-manual-install#ztp-binding-bmh-to-cluster-using-annotation_ztp-manual-install "5.6. Bind bare-metal hosts to clusters using the cluster-reference annotation in GitOps ZTP deployments")
  * [`BareMetalHost` cluster-reference annotation reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-manual-install#ztp-bmh-cluster-reference-annotation-ref_ztp-manual-install "5.7. BareMetalHost cluster-reference annotation")
  * [Binding and unbinding hosts in the RHACM documentation](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/clusters/cluster_mce_overview#bind-unbind-hosts)
