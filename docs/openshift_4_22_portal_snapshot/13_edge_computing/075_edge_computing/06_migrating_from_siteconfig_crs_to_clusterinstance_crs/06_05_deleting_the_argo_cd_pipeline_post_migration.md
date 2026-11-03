# 6.5. Deleting the Argo CD pipeline post-migration

After you migrate all single-node OpenShift clusters from using `SiteConfig` CRs to `ClusterInstance` CRs, you can delete the original Argo CD application and related resources that managed the `SiteConfig` CRs. 

Note

Only delete the Argo CD application and related resources after you have confirmed that all clusters are successfully managed by the new Argo CD application that uses `ClusterInstance` CRs. Additionally, if the Argo CD project was only used for the migrated cluster’s Argo application, you can also delete this project. 

**Prerequisites**

  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * All single-node OpenShift clusters have been successfully migrated to use `ClusterInstance` CRs and are managed by another Argo CD application. 



**Procedure**

  1. Delete the original Argo CD application that managed the `SiteConfig` CRs: 

```bash
$ oc delete application.argo clusters -n openshift-gitops
```


     * Replace `clusters` with the name of your original Argo CD application. 

  2. Delete the original Argo CD project by running the following command: 

```bash
$ oc delete appproject ztp-app-project -n openshift-gitops
```


     * Replace `ztp-app-project` with the name of your original Argo CD project. 




**Verification**

  1. Confirm that the original Argo CD application is deleted by running the following command: 

```bash
$ oc get appproject -n openshift-gitops
```


**Example output**

```bash
NAME                 AGE
default              6d20h
policy-app-project   2d22h
ztpv2-app-project    44h
```


     * The original Argo CD project in this example, `ztp-app-project` is not present in the output. 

  2. Confirm that the original Argo CD project is deleted by running the following command: 

```bash
oc get applications.argo -n openshift-gitops
```


**Example output**

```bash
NAME                       SYNC STATUS   HEALTH STATUS
clusters-v2                Synced        Healthy
policies                   Synced        Healthy
```


     * The original Argo CD application in this example, `clusters` is not present in the output.
