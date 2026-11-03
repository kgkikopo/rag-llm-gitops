# 5.4. Mirror an image set to a mirror registry

Mirroring an image set to a mirror registry ensures that the required images are available in a secure and controlled environment, facilitating smoother deployments, updates, and maintenance tasks. 

## 5.4.1. Create the image set configuration

Before you can use the oc-mirror plugin v2 to mirror images, you must create an image set configuration file. This image set configuration file defines which OpenShift Container Platform releases, Operators, and other images to mirror, along with other configuration settings for the oc-mirror plugin v2. 

**Prerequisites**

  * You have created a container image registry credentials file. For instructions, see _Configuring credentials that allow images to be mirrored_. 



**Procedure**

  * Create an `ImageSetConfiguration` YAML file and modify it to include your required images. 

**Example`ImageSetConfiguration` YAML file**

```yaml
kind: ImageSetConfiguration
apiVersion: mirror.openshift.io/v2alpha1
mirror:
  platform:
    channels:
    - name: stable-4.22 
```


1

```yaml
      minVersion: 4.22.0
      maxVersion: 4.22.0
    graph: true 
```


2

```yaml
  operators:
    - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.22 
```


3

```yaml
      packages: 
```


4

```yaml
       - name: aws-load-balancer-operator
       - name: 3scale-operator
       - name: node-observability-operator
         channels:
         - name: stable
  additionalImages: 
```


5

```yaml
   - name: registry.redhat.io/ubi8/ubi:latest
   - name: registry.redhat.io/ubi9/ubi@sha256:20f695d2a91352d4eaa25107535126727b5945bff38ed36a3e59590f495046f0
```


`mirror.platform.channels.name`
     Set the channel to retrieve OpenShift Container Platform images from. 
`mirror.platform.graph`
     Add `graph: true` to build and push the graph-data image to the mirror registry. The graph-data image is required to create OpenShift Update Service (OSUS). The `graph: true` field also generates the `UpdateService` custom resource manifest. The `oc` command-line interface (CLI) can use the `UpdateService` custom resource manifest to create OSUS. For more information, see _About the OpenShift Update Service_. 
`mirror.operators.catalog`
     Set the Operator catalog to retrieve the OpenShift Container Platform images from. 
`mirror.operators.packages`
     Specify only certain Operator packages to include in the image set. Remove this field to retrieve all packages in the catalog. 
`mirror.operators.packages.channels.name`
     Specifies only certain channels of the Operator packages to include in the image set. You must always include the default channel for the Operator package even if you do not use the bundles in that channel. You can find the default channel by running the following command: `oc mirror list operators --catalog=<catalog_name> --package=<package_name> --v2`. 
`mirror.additionalImages`
    

Specify any additional images to include in image set. 

Note

You must use explicit registry hostnames for all images listed under `additionalImages`. Without explicit hostnames, the plugin mirrors the images to unexpected target paths. 




**Additional resources**

  * [About the OpenShift Update Service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#update-service-about_understanding-openshift-updates)



## 5.4.2. Comparison of oc-mirror workflows

Use the following table to compare the supported use cases for the mirror-to-disk (m2d), disk-to-mirror (d2m), and mirror-to-mirror (m2m) workflows. 

**Use Case**| **Mirror To Disk (m2d) and Disk To Mirror (d2m)**| **Mirror To Mirror (m2m)**  
---|---|---  
The target registry exists in an environment with no internet access and no external access.  |  ✓  |   
The target registry exists in an environment with no internet access but is accessible from another machine. For example, the target registry resides in a bastion host.  |  |  ✓   
You must move content to the disconnected environment by using a physical method, such as USB devices.  |  ✓  |   
The workflow moves content directly to the target registry without generating an intermediate tar file.  |  |  ✓   
The workflow uses an internal cache to resume after failures but requires additional disk space.  |  ✓  |   
The workflow does not use a cache, restarts from the beginning after a failure, and requires no additional disk space.  |  |  ✓   
Show more

## 5.4.3. Mirror an image set in a partially disconnected environment

You can mirror image sets to a registry using the oc-mirror plugin v2 in environments with restricted internet access. 

During the mirroring process, the plugin automatically generates the `ImageSetConfiguration` and `DeleteImageSetConfiguration` files that are pinned by digest in your working directory, along with your original files that reference tags. Pinning by digest maintains consistency across your disconnected environments ensuring that you always deploy the same image, regardless of any later changes to the upstream tags. 

**Prerequisites**

  * You have access to the internet and the mirror registry in the environment where you are running the oc-mirror plugin v2. 



**Procedure**

  * Mirror the images from the specified image set configuration to a specified registry by running the following command: 

```shell-session
$ oc mirror -c <image_set_configuration> --workspace file://<file_path> docker://<mirror_registry_url> --v2 
```


1

```shell-session

```


where: 

<image_set_configuration>
     Specifies the name of the image set configuration file. 
<file_path>
     Specifies the directory where cluster resources will be generated in. 
<mirror_registry_url>
     Specifies the URL or address of the mirror registry where the images are stored and from which they need to be deleted. 




**Verification**

  1. Navigate to the `working-dir/cluster-resources` directory that was generated in the `<file_path>` directory. 
  2. Verify that the YAML files are present for the `ImageDigestMirrorSet`, `ImageTagMirrorSet`, and `CatalogSource` resources. 



**Next steps**

  * Configure your cluster to use the resources generated by oc-mirror plugin v2. 



## 5.4.4. Mirror an image set in a fully disconnected environment

You can mirror image sets in a fully disconnected environment where the OpenShift Container Platform cluster cannot access the public internet. 

The following high-level workflow describes the mirroring process: 

  1. **Mirror to disk** : Mirror the image set to an archive. 
  2. **Disk transfer** : Manually transfer the archive to the network of the disconnected mirror registry. 
  3. **Disk to mirror** : Mirror the image set from the archive to the target disconnected registry. 



### 5.4.4.1. Mirroring from mirror to disk

You can use the oc-mirror plugin v2 to generate an image set and save the content to disk. The plugin retrieves images from the source specified in the image set configuration and packs them into a tar archive. 

Transfer the generated image set to the disconnected environment and mirror it to the target registry. 

Additionally, the plugin automatically generates the `ImageSetConfiguration` and `DeleteImageSetConfiguration` files that are pinned by digest in your working directory and tar archive. Pinning by digest maintains consistency across your disconnected environments ensuring that you always deploy the same image, regardless of any later changes to the upstream tags. 

**Procedure**

  * Mirror the images from the specified image set configuration to the disk by running the following command: 

```shell-session
$ oc mirror -c <image_set_configuration> file://<file_path> --v2
```


where: 

<image_set_configuration>
     Specifies the name of the image set configuration file. 
<file_path>
     Specifies the directory where the archives containing the image sets will be generated in. 




**Verification**

  1. Navigate to the `<file_path>` directory that was generated. 
  2. Verify that the archive files have been generated. 



**Next steps**

  * Mirroring from disk to mirror 



### 5.4.4.2. Mirroring from disk to mirror

You can use the oc-mirror plugin v2 to mirror image sets from a disk to a target mirror registry. 

The oc-mirror plugin v2 retrieves container images from a local disk and transfers them to the specified mirror registry. 

**Procedure**

  1. Transfer the disk containing mirrored image sets to the environment that contains the target mirror registry. 
  2. Process the image set file on the disk and mirror the contents to a target mirror registry by running the following command: 

```shell-session
$ oc mirror -c <image_set_configuration> --from file://<file_path> docker://<mirror_registry_url> --v2
```


where: 

<image_set_configuration>
     Specifies the name of the image set configuration file. 
<file_path>
     Specifies the directory on the disk containing the archives. This folder will also contain cluster resources generated for you apply to the cluster, for example the ImageDigestMirrorSet (IDMS) or ImageTagMirrorSet (ITMS) resources. 
<mirror_registry_url>
     Specifies the URL or address of the mirror registry where the images are stored. 




**Verification**

  1. Navigate to the `cluster-resources` directory within the `working-dir` directory that was generated in the `<file_path>` directory. 
  2. Verify that the YAML files are present for the `ImageDigestMirrorSet`, `ImageTagMirrorSet`, and `CatalogSource` resources. 



**Next steps**

  * Configure your cluster to use the resources generated by oc-mirror plugin v2.
