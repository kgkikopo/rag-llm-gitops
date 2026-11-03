# 2.9. Prepare the GitOps ZTP site configuration repository

Before you can use the GitOps Zero Touch Provisioning (ZTP) pipeline, you need to prepare the Git repository to host the site configuration data. 

**Prerequisites**

  * You have configured the hub cluster GitOps applications for generating the required installation and policy custom resources (CRs). 
  * You have deployed the managed clusters using GitOps ZTP. 



**Procedure**

  1. Create a directory structure with separate paths for the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs. 

Note

Keep `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs in separate directories. Both the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` directories must contain a `kustomization.yaml` file that explicitly includes the files in that directory. 

  2. Export the `argocd` directory from the `ztp-site-generate` container image using the following commands: 

```shell-session
$ podman pull registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22
```


```shell-session
$ mkdir -p ./out
```


```shell-session
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 extract /home/ztp --tar | tar x -C ./out
```


  3. Check that the `out` directory contains the following subdirectories: 

     * `out/extra-manifest` contains the source CR files that you use to create extra manifest `ConfigMap` resources through the `configMapGenerator` in the `kustomization.yaml` file. The `ClusterInstance` CR references these `ConfigMap` resources using the `extraManifestsRefs` field. 
     * `out/source-crs` contains the source CR files that `PolicyGenerator` uses to generate the Red Hat Advanced Cluster Management (RHACM) policies. 
     * `out/argocd/deployment` contains patches and YAML files to apply on the hub cluster for use in the next step of this procedure. 
     * `out/argocd/example/clusterinstance` contains the examples for `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files that represent the recommended configuration. 

  4. Copy the `out/source-crs` folder and contents to the `PolicyGenerator` or `PolicyGentemplate` directory. 
  5. The out/extra-manifests directory contains the reference manifests for a RAN DU cluster. Copy the `out/extra-manifests` directory into the `ClusterInstance` folder. This directory should contain CRs from the `ztp-site-generate` container only. Do not add user-provided CRs here. If you want to work with user-provided CRs you must create another directory for that content. For example: 

```plaintext
example/
  ├── acmpolicygenerator
  │   ├── kustomization.yaml
  │   └── source-crs/
  ├── policygentemplates
  │   ├── kustomization.yaml
  │   └── source-crs/
  └── clusterinstance
        ├── extra-manifests
        └── kustomization.yaml
```


Note

Using `PolicyGenTemplate` CRs to manage and deploy policies to manage clusters will be deprecated in a future OpenShift Container Platform release. Equivalent and improved functionality is available by using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs. 

  6. Commit the directory structure and the `kustomization.yaml` files and push to your Git repository. The initial push to Git should include the `kustomization.yaml` files. 

You can use the directory structure under `out/argocd/example` as a reference for the structure and content of your Git repository. That structure includes `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` reference CRs for single-node, three-node, and standard clusters. Remove references to cluster types that you are not using. 

For all cluster types, you must: 

     * Add the `source-crs` subdirectory to the `acmpolicygenerator` or `policygentemplates` directory. 
     * Add the `extra-manifests` directory to the `clusterinstance` directory. 

The following example describes a set of CRs for a network of single-node clusters: 

```plaintext
example/
  ├── acmpolicygenerator
  │   ├── acm-common-ranGen.yaml
  │   ├── acm-example-sno-site.yaml
  │   ├── acm-group-du-sno-ranGen.yaml
  │   ├── group-du-sno-validator-ranGen.yaml
  │   ├── kustomization.yaml
  │   ├── source-crs/
  │   └── ns.yaml
  └── clusterinstance
        ├── example-sno.yaml
        ├── extra-manifests/
        ├── custom-manifests/
        ├── KlusterletAddonConfigOverride.yaml
        └── kustomization.yaml
```


where: 

`extra-manifests/`
     Contains reference manifests from the `ztp-container`. 
`custom-manifests/`
     Contains custom manifests. 




Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs. 

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation. 

**Additional resources**

  * [Configuring managed cluster policies by using PolicyGenerator resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-configuring-managed-clusters-policygenerator "10.1. Configuring managed cluster policies by using PolicyGenerator resources")
  * [Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-comparing-pgt-and-rhacm-pg-patching-strategies_ztp-configuring-managed-clusters-policygenerator "10.1.1. Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching")
