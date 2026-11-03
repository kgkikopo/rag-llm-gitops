# 6.2. Preparing a parallel Argo CD pipeline for ClusterInstance CRs

Create a parallel Argo CD project and application to manage the new `ClusterInstance` CRs and associated cluster resources. 

**Prerequisites**

  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have configured your GitOps ZTP environment successfully. 
  * You have installed and configured the Assisted Installer service successfully. 
  * You have access to the Git repository that contains your single-node OpenShift cluster configurations. 



**Procedure**

  1. Create YAML files for the parallel Argo project and application: 

     1. Create a YAML file that defines the `AppProject` resource: 

**Example`ztp-app-project-v2.yaml` file**

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: ztp-app-project
  namespace: openshift-gitops
  annotations:
    argocd.argoproj.io/sync-wave: "100"
spec:
  clusterResourceWhitelist:
  - group: 'hive.openshift.io'
    kind: ClusterImageSet
  - group: 'cluster.open-cluster-management.io'
    kind: ManagedCluster
  - group: ''
    kind: Namespace
  destinations:
  - namespace: '*'
    server: '*'
  namespaceResourceWhitelist:
  - group: ''
    kind: ConfigMap
  - group: ''
    kind: Namespace
  - group: ''
    kind: Secret
  - group: 'extensions.hive.openshift.io'
    kind: ImageClusterInstall
  - group: 'metal3.io'
    kind: DataImage
  - group: 'siteconfig.open-cluster-management.io'
    kind: ClusterInstance
  sourceRepos:
  - '*'
```


where: 

`spec.namespaceResourceWhitelist[].kind`
     The `ClusterInstance` CR manages the `siteconfig.open-cluster-management.io` object instead of the `SiteConfig` CR. 

     2. Create a YAML file that defines the `Application` resource: 

**Example`clusters-v2.yaml` file**

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: clusters-v2
  namespace: openshift-gitops
spec:
  destination:
    namespace: clusters-sub
    server: https://kubernetes.default.svc
  ignoreDifferences:
  - group: cluster.open-cluster-management.io
    kind: ManagedCluster
    managedFieldsManagers:
    - controller
  project: ztp-app-project-v2
  source:
    path: site-configs-v2
    repoURL: http://infra.5g-deployment.lab:3000/student/ztp-repository.git
    targetRevision: main
  syncPolicy:
    syncOptions:
    - CreateNamespace=true
    - PrunePropagationPolicy=background
    - RespectIgnoreDifferences=true
```


where: 

`spec.project`
     Specifies the Argo CD project. The value must match the name of the `AppProject` resource created in the previous step. 
`spec.source.path`
    

Specifies the root folder in your Git repository that will contain the `ClusterInstance` CRs and associated resources. 

Note

By default, `auto-sync` is enabled. However, synchronization only occurs when you push configuration data for the cluster to the new configuration folder, or in this example, the `site-configs-v2/` folder. 

  2. Create and commit a root folder in your Git repository that will contain the `ClusterInstance` CRs and associated resources, for example: 

```bash
$ mkdir site-configs-v2
$ touch site-configs-v2/.gitkeep
$ git commit -s -m “Creates cluster-instance folder”
$ git push origin main
```


     * The `.gitkeep` file is a placeholder to ensure that the empty folder is tracked by Git. 

Note

You only need to create and commit the root `site-configs-v2/` folder during pipeline setup. You will mirror the complete `site-configs/` folder structure into `site-configs-v2/` during the cluster migration procedure. 

  3. Apply the `AppProject` and `Application` resources to the hub cluster by running the following commands: 

```bash
$ oc apply -f ztp-app-project-v2.yaml
$ oc apply -f clusters-v2.yaml
```


**Verification**

  1. Verify that the original Argo CD project, `ztp-app-project`, and the new Argo CD project, `ztp-app-project-v2` are present on the hub cluster by running the following command: 

```bash
$ oc get appprojects -n openshift-gitops
```


**Example output**

```bash
NAME                 AGE
default              46h
policy-app-project   42h
ztp-app-project      18h
ztp-app-project-v2    14s
```


  2. Verify that the original Argo CD application, `clusters`, and the new Argo CD application, `clusters-v2` are present on the hub cluster by running the following command: 

```bash
$ oc get application.argo -n openshift-gitops
```


**Example output**

```bash
NAME                       SYNC STATUS   HEALTH STATUS
clusters                   Synced        Healthy
clusters-v2                Synced        Healthy
policies                   Synced        Healthy
```
