# 6.3. Transitioning the active-ocp-version ClusterImageSet

Optionally, the `active-ocp-version` `ClusterImageSet` is a GitOps Zero Touch Provisioning (ZTP) convention used in GitOps ZTP deployments. 

It provides a single, central definition of the OpenShift Container Platform release image to use when provisioning clusters. By default, this resource is synchronized to the hub cluster from the `site-config/resources/` folder. 

If your deployment uses an `active-ocp-version` `ClusterImageSet` CR, you must migrate it to the `resources/` folder in the new directroy that contains `ClusterInstance` CRs. This prevents synchronization conflicts because both Argo CD applications cannot manage the same resource. 

**Prerequisites**

  * You have completed the procedure to create the parallel Argo CD pipeline for `ClusterInstance` CRs. 
  * The Argo CD application points to the folder in your Git repository that will contain the new `ClusterInstance` CRs and associated cluster resouces. In this example, the `site-configs-v2/` Argo CD application points to the `site-configs-v2/` folder. 
  * Your Git repository contains an `active-ocp-version.yaml` manifest in the `resources/` folder. 



**Procedure**

  1. Copy the `resources/` folder from the `site-configs/` directory into the new `site-configs-v2/` directory: 

```bash
$ cp -r site-configs/resources site-configs-v2/
```


  2. Remove the reference to the `resources/` folder from the `site-configs/kustomization.yaml` file. This ensures that the old `clusters` Argo CD application no longer manages the `active-ocp-version` resource. 

**Example updated`site-configs/resources/kustomization.yaml` file**

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
   - pre-reqs/
   #- resources/
generators:
   - hub-1/sno1.yaml
   - hub-1/sno2.yaml
   - hub-1/sno3.yaml
```


  3. Add the `resources/` folder to the `site-configs-v2/kustomization.yaml` file. This step transfers ownership of the `ClusterImageSet` to the new `clusters-v2` application. 

**Example updated`site-configs-v2/kustomization.yaml` file**

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - resources/
```


  4. Commit and push the changes to the Git repository. 



**Verification**

  1. In Argo CD, verify that the `clusters-v2` application is **Healthy** and **Synced**. 
  2. If the `active-ocp-version` `ClusterImageSet` resource in the `cluster` Argo application is out of sync, you can remove the Argo CD application label by running the following command: 

```bash
$ oc label clusterimageset active-ocp-version app.kubernetes.io/instance-
```


**Example output**

```bash
clusterimageset.hive.openshift.io/active-ocp-version unlabeled
```
