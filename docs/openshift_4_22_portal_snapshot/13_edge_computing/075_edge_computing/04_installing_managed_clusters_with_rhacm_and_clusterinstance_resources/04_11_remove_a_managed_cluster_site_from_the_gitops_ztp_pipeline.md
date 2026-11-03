# 4.11. Remove a managed cluster site from the GitOps ZTP pipeline

You can remove a managed site and the associated installation and configuration policy CRs from the GitOps Zero Touch Provisioning (ZTP) pipeline. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 



**Procedure**

  1. Remove a site and the associated CRs by removing the associated `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files from the `kustomization.yaml` file. 
  2. Add the following `syncOptions` field to the ArgoCD application that manages the target site. 

```yaml
kind: Application
spec:
  syncPolicy:
    syncOptions:
    - PrunePropagationPolicy=background
```


When you run the GitOps ZTP pipeline again, the generated CRs are removed. 

  3. Optional: If you want to permanently remove a site, you should also remove the `ClusterInstance` and site-specific `PolicyGenerator` or `PolicyGentemplate` files from the Git repository. 
  4. Optional: If you want to remove a site temporarily, for example when redeploying a site, you can leave the `ClusterInstance` and site-specific `PolicyGenerator` or `PolicyGentemplate` CRs in the Git repository. 



**Additional resources**

  * [Removing a cluster from management](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.9/html/clusters/cluster_mce_overview#remove-managed-cluster)
  * [Deprovisioning clusters](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/ibio-intro#deprovision-clusters)
