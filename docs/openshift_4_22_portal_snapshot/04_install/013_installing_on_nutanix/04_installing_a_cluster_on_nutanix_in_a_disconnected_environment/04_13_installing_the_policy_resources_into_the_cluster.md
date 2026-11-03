# 4.13. Installing the policy resources into the cluster

Mirroring the OpenShift Container Platform content using the oc-mirror OpenShift CLI (oc) plugin creates resources, which include `catalogSource-certified-operator-index.yaml` and `imageContentSourcePolicy.yaml`. 

  * The `ImageContentSourcePolicy` resource associates the mirror registry with the source registry and redirects image pull requests from the online registries to the mirror registry. 
  * The `CatalogSource` resource is used by Operator Lifecycle Manager (OLM) Classic to retrieve information about the available Operators in the mirror registry, which lets users discover and install Operators. 

Note

OLM v1 uses the `ClusterCatalog` resource to retrieve information about the available cluster extensions in the mirror registry. 

The oc-mirror plugin v1 does not generate `ClusterCatalog` resources automatically; you must manually create them. The oc-mirror plugin v2 does, however, generate `ClusterCatalog` resources automatically. 

For more information on creating and applying `ClusterCatalog` resources, see "Adding a catalog to a cluster" in "Extensions". 




After you install the cluster, you must install these resources into the cluster. 

**Prerequisites**

  * You have mirrored the image set to the registry mirror in the disconnected environment. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Log in to the OpenShift CLI as a user with the `cluster-admin` role. 
  2. Apply the YAML files from the results directory to the cluster: 

```shell-session
$ oc apply -f ./oc-mirror-workspace/results-<id>/
```


**Verification**

  1. Verify that the `ImageContentSourcePolicy` resources were successfully installed: 

```shell-session
$ oc get imagecontentsourcepolicy
```


  2. Verify that the `CatalogSource` resources were successfully installed: 

```shell-session
$ oc get catalogsource --all-namespaces
```


**Additional resources**

  * [Adding a catalog to a cluster in Extensions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extensions/#olmv1-adding-a-catalog-to-a-cluster_managing-catalogs)
