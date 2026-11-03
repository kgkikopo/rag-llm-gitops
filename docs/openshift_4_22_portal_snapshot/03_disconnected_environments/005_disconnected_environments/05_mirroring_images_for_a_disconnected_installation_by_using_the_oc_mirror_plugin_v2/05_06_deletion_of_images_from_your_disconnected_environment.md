# 5.6. Deletion of images from your disconnected environment

If you have previously deployed images using the oc-mirror plugin v2, you can delete these images to free up space in your mirror registry. 

oc-mirror plugin v2 does not automatically prune images that are not included in the `ImageSetConfiguration` file. This prevents accidentally deleting necessary or deployed images when making changes to the `ImageSetConfig.yaml` file. 

To delete images, you can use the `DeleteImageSetConfiguration` file that was automatically pinned by digest during the mirroring process, or you can manually create a new file. 

In the following example, the `DeleteImageSetConfiguration` file removes the following images: 

  * All release images for OpenShift Container Platform 4.13.3. 
  * The `aws-load-balancer-operator` v0.0.1 bundle and all its related images. 
  * The additional images for `ubi` and `ubi-minimal`, referenced by their corresponding digests. 



**Example`DeleteImageSetConfiguration` file**

```yaml
apiVersion: mirror.openshift.io/v2alpha1
kind: DeleteImageSetConfiguration
delete:
  platform:
    channels:
      - name: stable-4.13
        minVersion: 4.13.3
        maxVersion: 4.13.3
  operators:
    - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.12
      packages:
      - name: aws-load-balancer-operator
         minVersion: 0.0.1
         maxVersion: 0.0.1
  additionalImages:
    - name: registry.redhat.io/ubi8/ubi@sha256:bce7e9f69fb7d4533447232478fd825811c760288f87a35699f9c8f030f2c1a6
    - name: registry.redhat.io/ubi8/ubi-minimal@sha256:8bedbe742f140108897fb3532068e8316900d9814f399d676ac78b46e740e34e
```


Important

  * Consider using the mirror-to-disk and disk-to-mirror workflows to reduce deletion issues. 
  * In oc-mirror plugin v2, you must use explicit registry hostnames for all images listed under `additionalImages`. Otherwise, images are mirrored to incorrect target paths. 



oc-mirror plugin v2 deletes only the manifests of the images, which does not reduce the storage occupied in the registry. 

To free up storage space from unnecessary images, such as those with deleted manifests, you must enable the garbage collector on your container registry. With the garbage collector enabled, the registry will delete the image blobs that no longer have references to any manifests, reducing the storage previously occupied by the deleted blobs. The process for enabling the garbage collector differs depending on your container registry. 

For more information, see "Resolving storage cleanup issues in the distribution registry". 

Important

  * To skip deleting the Operator catalog image while you are deleting Operator images, you must list the specific Operators under the Operator catalog image in the `DeleteImageSetConfiguration` file. This ensures that only the specified Operators are deleted, not the catalog image. 

If only the Operator catalog image is specified, all Operators within that catalog, as well as the catalog image itself, will be deleted. 

  * oc-mirror plugin v2 does not delete Operator catalog images automatically because other Operators may still be deployed and depend on these images. 

If you are certain that no Operators from a catalog remain in the registry or cluster, you can explicitly add the catalog image to `additionalImages` in `DeleteImageSetConfiguration` to remove it. 

  * Garbage collection behavior depends on the registry. Some registries do not automatically remove deleted images, requiring a system administrator to manually trigger garbage collection to free up space. 



**Additional resources**

  * [Resolving storage cleanup issues in the distribution registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/about-installing-oc-mirror-v2#oc-mirror-v2-procedure-garbage-collector_about-installing-oc-mirror-v2 "5.6.1. Resolving storage cleanup issues in the distribution registry")



## 5.6.1. Resolving storage cleanup issues in the distribution registry

A known issue in the distribution registry prevents the garbage collector from freeing up storage as expected. This issue does not occur when you use Red Hat Quay. 

**Procedure**

  * Choose the appropriate method to work around the known issue in the distribution registry: 

    * To restart the container registry, run the following command: 

```shell-session
$ podman restart <registry_container>
```


    * To disable caching in the registry configuration, perform the following steps: 

      1. To disable the `blobdescriptor` cache, modify the `/etc/docker/registry/config.yml` file: 

```yaml
version: 0.1
log:
  fields:
    service: registry
storage:
  cache:
    blobdescriptor: ""
  filesystem:
    rootdirectory: /var/lib/registry
http:
  addr: :5000
  headers:
    X-Content-Type-Options: [nosniff]
health:
  storagedriver:
    enabled: true
    interval: 10s
    threshold: 3
```


      2. To apply the changes, restart the container registry by running the following command: 

```shell-session
$ podman restart <registry_container>
```


## 5.6.2. Deleting images from a disconnected environment

You can delete images from a disconnected environment using the oc-mirror plugin. 

**Prerequisites**

  * You have enabled garbage collection in your environment to delete images that no longer reference manifests. 



**Procedure**

  1. Create a `delete-image-set-config.yaml` file and include the following content: 

**`DeleteImageSetConfiguration` file**

```yaml
apiVersion: mirror.openshift.io/v2alpha1
kind: DeleteImageSetConfiguration
delete:
  platform:
    channels:
      - name: <channel_name>
        minVersion: <channel_min_version>
        maxVersion: <channel_max_version>
  operators:
    - catalog: <operator_catalog_name>
      packages:
      - name: <operator_name>
         minVersion: <operator_max_version>
         maxVersion: <operator_min_version>
  additionalImages:
    - name: <additional_images>
```


where: 

`delete.platform.channels.name`
     Specifies the name of the OpenShift Container Platform channel to delete, for example `stable-4.15`. 
`delete.platform.channels.minVersion` and `delete.platform.channels.maxVersion`
     Specifies a version range of the images to delete within the channel, for example `4.15.0` for the minimum version and `4.15.1` for the maximum version. To delete only one version’s images, use that version number for both the `minVersion` and `maxVersion` fields. 
`delete.operators.catalog`
     Specifies an Operator catalog image containing the Operators to delete, for example `registry.redhat.io/redhat/redhat-operator-index:v4.14`. The Operator catalog image will not get deleted. Its presence in the registry might be necessary for other Operators still remaining on the cluster. 
`delete.operators.packages.name`
     Specifies a specific Operator to delete, for example `aws-load-balancer-operator`. 
`delete.operators.packages.minVersion` and `delete.operators.packages.maxVersion`
     Specifies a version range of the images to delete for the Operator, for example `0.0.1` for the minimum version and `0.0.2` for the maximum version. 

  2. Create a `delete-images.yaml` file by running the following command: 

```shell-session
$ oc-mirror delete --config delete-image-set-config.yaml --workspace file://<previously_mirrored_work_folder> --v2 --generate docker://<remote_registry>
```


where: 

`<previously_mirrored_work_folder>`
     Specifies the directory where images were previously mirrored to or stored during the mirroring process. 
`<remote_registry>`
    

Specifies the URL or address of the remote container registry from which images will be deleted. 

Important

When deleting images, specify the correct workspace directory. Modify or delete the cache directory only when starting mirroring from scratch, such as setting up a new cluster. Incorrect changes to the cache directory might disrupt further mirroring operations. 

  3. Go to the `<previously_mirrored_work_folder>/delete` directory that was created. 
  4. Verify that the `delete-images.yaml` file has been generated. 
  5. Manually ensure that each image listed in the file is no longer needed by the cluster and can be safely removed from the registry. 
  6. After you generate the `delete-images` YAML file, delete the images from the remote registry by running the following command: 

```shell-session
$ oc-mirror delete --v2 --delete-yaml-file <previously_mirrored_work_folder>/working-dir/delete/delete-images.yaml docker://<remote_registry>
```


where: 

<previously_mirrored_work_folder>
     Specifies the directory where images were previously mirrored or stored during the mirroring process. 
<remote_registry>
    

Specifies the URL or address of the remote container registry from which images will be deleted. 

Important

When using the mirror-to-mirror method to mirror images, images are not cached locally, so you cannot delete images from a local cache.
