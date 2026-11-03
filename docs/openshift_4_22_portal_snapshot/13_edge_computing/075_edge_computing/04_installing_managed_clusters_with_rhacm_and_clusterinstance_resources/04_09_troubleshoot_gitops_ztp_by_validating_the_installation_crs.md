# 4.9. Troubleshoot GitOps ZTP by validating the installation CRs

The ArgoCD pipeline uses the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` custom resources (CRs) to generate the cluster configuration CRs and Red Hat Advanced Cluster Management (RHACM) policies. Use the following steps to troubleshoot issues that might occur during this process. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 



**Procedure**

  1. Check that the installation CRs were created by using the following command: 

```shell-session
$ oc get AgentClusterInstall -n <cluster_name>
```


If no object is returned, use the following steps to troubleshoot the ArgoCD pipeline flow from `ClusterInstance` files to the installation CRs. 

  2. Verify that the `ManagedCluster` CR was generated using the `ClusterInstance` CR on the hub cluster: 

```shell-session
$ oc get managedcluster
```


  3. If the `ManagedCluster` is missing, check if the `clusters` application failed to synchronize the files from the Git repository to the hub cluster: 

```shell-session
$ oc get applications.argoproj.io -n openshift-gitops clusters -o yaml
```
