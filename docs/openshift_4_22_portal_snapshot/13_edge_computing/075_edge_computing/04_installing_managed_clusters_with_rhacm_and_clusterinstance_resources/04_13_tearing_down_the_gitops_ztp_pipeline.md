# 4.13. Tearing down the GitOps ZTP pipeline

You can remove the ArgoCD pipeline and all generated GitOps Zero Touch Provisioning (ZTP) artifacts. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 



**Procedure**

  1. Detach all clusters from Red Hat Advanced Cluster Management (RHACM) on the hub cluster. 
  2. Delete the `kustomization.yaml` file in the `deployment` directory using the following command: 

```shell-session
$ oc delete -k out/argocd/deployment
```


  3. Commit and push your changes to the site repository.
