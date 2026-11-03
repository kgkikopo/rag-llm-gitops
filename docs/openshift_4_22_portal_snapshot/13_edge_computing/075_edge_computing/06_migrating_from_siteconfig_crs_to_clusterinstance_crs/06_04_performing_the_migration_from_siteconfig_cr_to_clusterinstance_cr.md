# 6.4. Performing the migration from SiteConfig CR to ClusterInstance CR

Migrate a single-node OpenShift cluster from using a `SiteConfig` CR to a `ClusterInstance` CR by removing the `SiteConfig` CR from the old pipeline, and adding a corresponding `ClusterInstance` CR to the new pipeline. 

**Prerequisites**

  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have set up the parallel Argo CD pipeline, including the Argo CD project and application, that will manage the cluster using the `ClusterInstance` CR. 
  * The Argo CD application managing the original `SiteConfig` CR pipeline is configured with the sync policy `prune=false`. This setting ensures that resources remain intact after you remove the target cluster from this application. 
  * You have access to the Git repository that contains your single-node OpenShift cluster configurations. 
  * You have Red Hat Advanced Cluster Management (RHACM) version 2.12 or later installed in the hub cluster. 
  * The SiteConfig Operator is installed and running in the hub cluster. 
  * You have installed Podman and you have access to the registry.redhat.io container image registry. 



**Procedure**

  1. Mirror the `site-configs` folder structure to the new `site-configs-v2` directory that will contain the `ClusterInstance` CRs, for example: 

```plaintext
site-configs-v2/
├── hub-1/
│   └── extra-manifest/
├── pre-reqs/
│   └── sno1/
├── reference-manifest/
│   └── 4.22/
└── resources/
```


where: 

`hub-1/`
     Contains the `ClusterInstance` CR for each cluster. 
`pre-reqs/sno1/`
     Contains the required pre-requisite resources for the target cluster, such as the image registry pull secret and the baseboard management controller credentials. 

  2. Remove the target cluster from the original Argo CD application by commenting out the resources in the related files in Git: 

     1. Comment out the target cluster from the `site-configs/kustomization.yaml` file, for example: 

```bash
$ cat site-configs/kustomization.yaml
```


**Example updated`site-configs/kustomization.yaml` file**

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
   - pre-reqs/
   #- resources/
generators:
   #- hub-1/sno1.yaml
   - hub-1/sno2.yaml
   - hub-1/sno3.yaml
```


     2. Comment out the target cluster from the `site-configs/pre-reqs/kustomization.yaml` file. This removes the `site-configs/pre-reqs/sno1` folder, which also requires migration and has resources such as the image registry pull secret, the baseboard management controller credentials, and so on, for example: 

```bash
$ cat site-configs/pre-reqs/kustomization.yaml
```


**Example updated`site-configs/pre-reqs/kustomization.yaml` file**

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  #- sno1/
  - sno2/
  - sno3/
```


  3. Commit the changes to the Git repository. 

Note

After you commit the changes, the original Argo CD application reports an `OutOfSync` sync status because the Argo CD application still attempts to monitor the status of the taget cluster’s resources. However, because the sync policy is set to `prune=false`, the Argo CD application does not delete any resources. 

  4. To ensure that the original Argo CD application no longer manages the cluster resources, you can remove the Argo CD application label from the resources by running the following command: 

```bash
$ for cr in bmh,hfs,clusterdeployment,agentclusterinstall,infraenv,nmstateconfig,configmap,klusterletaddonconfig,secrets; do oc label $cr app.kubernetes.io/instance- --all -n sno1; done && oc label ns sno1 app.kubernetes.io/instance- && oc label managedclusters sno1 app.kubernetes.io/instance-
```


The Argo CD application label is removed from all resources in the `sno1` namespace and the sync status returns to `Synced`. 

  5. Create the `ClusterInstance` CR for the target cluster by using the `siteconfig-converter` tool packaged with the `ztp-site-generate` container image: 

Note

The siteconfig-converter tool cannot translate earlier versions of the `AgentClusterInstall` resource that uses the following deprecated fields in the `SiteConfig` CR: 

     * `apiVIP`
     * `ingressVIP`
     * `manifestsConfigMapRef`

To solve this issue, you can do one of the following options: 

     * Create a custom cluster template that includes these fields. For more information about creating custom templates, see [Creating custom templates with the SiteConfig operator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.13/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/siteconfig-intro#create-custom-templates)
     * Suppress the creation of the `AgentClusterInstall` resource by adding it to the `suppressedManifests` list in the `ClusterInstance` CR, or by using the `-s` flag in the `siteconfig-converter` tool. You must remove the resource from the `suppressedManifests` list when reinstalling the cluster. 

     1. Pull the `ztp-site-generate` container image by running the following command: 

```bash
podman pull registry.redhat.io/openshift4/ztp-site-generate-rhel8:4.22
```


     2. Run the `siteconfig-converter` tool interactively through the container by running the following command: 

```bash
$ podman run -v "${PWD}":/resources:Z,U -it registry.redhat.io/openshift4/ztp-site-generate-rhel8:{product-version} siteconfig-converter -d /resources/<output_folder> /resources/<path_to_siteconfig_resource>
```


        * Replace `<output_folder>` with the output directory for the generated files. 
        * Replace `<path_to_siteconfig_resource>` with the path to the target `SiteConfig` CR file. 

**Example output**

```bash
Successfully read SiteConfig: sno1/sno1
Converted cluster 1 (sno1) to ClusterInstance: /resources/output/sno1.yaml
WARNING: Added default extraManifest ConfigMap 'extra-manifests-cm' to extraManifestsRefs. This configmap is created automatically.
Successfully converted 1 cluster(s) to ClusterInstance files in /resources/output: sno1.yaml
Generating ConfigMap kustomization files...
Using ConfigMap name: extra-manifests-cm, namespace: sno1, manifests directory: extra-manifests
Generating ConfigMap kustomization files with name: extra-manifests-cm, namespace: sno1, manifests directory: extra-manifests
Generating extraManifests for SiteConfig: /resources/sno1.yaml
Successfully generated extra manifests in /resources/output/extra-manifests
--- Kustomization.yaml Generator ---
Scanning directory: /resources/output/extra-manifests
Found and adding: extra-manifests/enable-crun-master.yaml
Found and adding: extra-manifests/enable-crun-worker.yaml
------------------------------------
kustomization-configMapGenerator-snippet.yaml generated successfully at: /resources/output/kustomization-configMapGenerator-snippet.yaml
Content:
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
configMapGenerator:
    - files:
        - extra-manifests/enable-crun-master.yaml
        - extra-manifests/enable-crun-worker.yaml
      name: extra-manifests-cm
      namespace: sno1
generatorOptions:
    disableNameSuffixHash: true

------------------------------------
```


Note

The `ClusterInstance` CR requires the extra manifests to be defined in a `ConfigMap` resource. 

To meet this requirement, the `siteconfig-converter` tool generates a `kustomization.yaml` snippet. The generated snippet uses Kustomize’s `configMapGenerator` to automatically package your manifest files into the required `ConfigMap` resource. You must merge this snippet into your original `kustomization.yaml` file to ensure that the `ConfigMap` resource is created and managed alongside your other cluster resources. 

  6. Configure the new Argo CD application to manage the target cluster by referencing it in the new pipelines `Kustomization` files, for example: 

```bash
$ cat site-configs-v2/kustomization.yaml
```


**Example updated`site-configs-v2/kustomization.yaml` file**

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - resources/
  - pre-reqs/
  - hub-1/sno1.yaml
```


```bash
$ cat  site-configs-v2/pre-reqs/kustomization.yaml
```


**Example updated`site-configs-v2/pre-reqs/kustomization.yaml` file**

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - sno1/
```


  7. Commit the changes to the Git repository. 



**Verification**

  1. Verify that the `ClusterInstance` CR is successfully deployed and the provisioning status complete by running the following command: 

```bash
$ oc get clusterinstance -A
```


**Example output**

```bash
NAME                                                         PAUSED   PROVISIONSTATUS   PROVISIONDETAILS         AGE
clusterinstance.siteconfig.open-cluster-management.io/sno1            Completed         Provisioning completed   27s
```


At this point, the new Argo CD application that uses the `ClusterInstance` CR is managing the `sno1` cluster. You can continue to migrate one or more clusters at a time by repeating these steps until all target clusters are migrated to the new pipeline. 

  2. Verify the folder structure and files in the `site-configs-v2/` directory contain the migrated resources for the `sno1` cluster, for example: 

```plaintext
site-configs-v2/
├── hub-1/
│   ├── sno1.yaml
├── extra-manifest/
│   ├── enable-crun-worker.yaml
│   └── enable-crun-master.yaml
├── kustomization.yaml
├── pre-reqs/
│   └── sno1/
│       ├── bmc-credentials.yaml
│       ├── namespace.yaml
│       └── pull-secret.yaml
├── kustomization.yaml
├── reference-manifest/
│   └── 4.22/
└── resources/
    ├── active-ocp-version.yaml
    └── kustomization.yaml
```


where: 

`hub-1/sno1.yaml`
     The `ClusterInstance` CR for the `sno1` cluster. 
`extra-manifest/`
     Contains the extra manifests automatically generated by the `siteconfig-converter` tool and referenced by the `ClusterInstance` CR. 
`kustomization.yaml`
     The `kustomization.yaml` snippet generated by the tool to create the `ConfigMap` resources that specify the extra manifests. Merge this snippet with your original `kustomization.yaml` file. 




**Additional resources**

  * [Enabling the SiteConfig operator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.12/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/siteconfig-intro#enable)



## 6.4.1. Reference flags for the siteconfig-converter tool

The following matrix describes the flags for the `siteconfig-converter` tool. 

Flag| Type| Description  
---|---|---  
-d  |  string  |  Define the output directory for the converted `ClusterInstance` custom resources (CRs). This flag is required.   
-t  |  string  |  Define a comma-separated list of template references for clusters in namespace/name format. The default value is `open-cluster-management/ai-cluster-templates-v1`.   
-n  |  string  |  Define a comma-separated list of template references for nodes in namespace/name format. The default value is `open-cluster-management/ai-node-templates-v1`.   
-m  |  string  |  Define a comma-separated list of `ConfigMap` names to use for extra manifests references.   
-s  |  string  |  Define a comma-separated list of manifest names to suppress at the cluster level.   
-w  |  boolean  |  Write conversion warnings as comments to the head of the converted YAML files. The default value is `false`.   
-c  |  boolean  |  Copy comments from the original `SiteConfig` CRs to the converted `ClusterInstance` CRs. The default is false.   
Show more
