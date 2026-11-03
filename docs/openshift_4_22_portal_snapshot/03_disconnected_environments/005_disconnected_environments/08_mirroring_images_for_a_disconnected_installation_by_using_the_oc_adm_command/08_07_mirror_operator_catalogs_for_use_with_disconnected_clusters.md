# 8.7. Mirror Operator catalogs for use with disconnected clusters

You can mirror the Operator contents of a Red Hat-provided catalog, or a custom catalog, into a container image registry using the `oc adm catalog mirror` command. 

The target registry must support Docker v2-2. For a cluster on a restricted network, this registry can be one that the cluster has network access to, such as a mirror registry created during a restricted network cluster installation. 

Important

  * The OpenShift image registry cannot be used as the target registry because it does not support pushing without a tag, which is required during the mirroring process. 
  * Running `oc adm catalog mirror` might result in the following error: `error: unable to retrieve source image`. This error occurs when image indexes include references to images that no longer exist on the image registry. Image indexes might retain older references to allow users running those images an upgrade path to newer points on the upgrade graph. As a temporary workaround, you can use the `--skip-missing` option to bypass the error and continue downloading the image index. For more information, see "Service Mesh Operator mirroring failed". 



The `oc adm catalog mirror` command also automatically mirrors the index image that is specified during the mirroring process, whether it be a Red Hat-provided index image or your own custom-built index image, to the target registry. You can then use the mirrored index image to create a catalog source that allows Operator Lifecycle Manager (OLM) to load the mirrored catalog onto your OpenShift Container Platform cluster. 

**Additional resources**

  * [Using Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/olm-restricted-networks "Chapter 10. Using Operator Lifecycle Manager in disconnected environments")
  * [Docker v2-2](https://docs.docker.com/registry/spec/manifest-v2-2/)
  * [Service Mesh Operator mirroring failed](https://access.redhat.com/solutions/6975305)



## 8.7.1. Prerequisites for mirroring Operator catalogs

You must meet several prerequisites before you can mirror Operator catalogs for use with disconnected clusters. 

Mirroring Operator catalogs for use with disconnected clusters has several prerequisites. 

The following prerequisites must be met: 

  * Workstation with unrestricted network access. 
  * `podman` version 1.9.3 or later. 
  * If you want to filter, or _prune_ , an existing catalog and selectively mirror only a subset of Operators, see the following sections: 

    * [Installing the opm CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#cli-opm-install)
    * [Updating or filtering a file-based catalog image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-filtering-fbc_olm-managing-custom-catalogs)

  * If you want to mirror a Red Hat-provided catalog, run the following command on your workstation with unrestricted network access to authenticate with `registry.redhat.io`: 

```shell-session
$ podman login registry.redhat.io
```


  * Access to a mirror registry that supports [Docker v2-2](https://docs.docker.com/registry/spec/manifest-v2-2/). 
  * On your mirror registry, decide which repository, or namespace, to use for storing mirrored Operator content. For example, you might create an `olm-mirror` repository. 
  * If your mirror registry does not have internet access, connect removable media to your workstation with unrestricted network access. 
  * If you are working with private registries, including `registry.redhat.io`, set the `REG_CREDS` environment variable to the file path of your registry credentials for use in later steps. For example, for the `podman` CLI: 

```shell-session
$ REG_CREDS=${XDG_RUNTIME_DIR}/containers/auth.json
```


## 8.7.2. Extracting and mirroring catalog contents

The `oc adm catalog mirror` command extracts the contents of an index image to generate mirroring manifests, then automatically mirrors all image content and the index image itself to your mirror registry. 

Alternatively, if your mirror registry is on a completely disconnected, or _airgapped_ , host, you can first mirror the content to removable media, move the media to the disconnected environment, then mirror the content from the media to the registry. 

### 8.7.2.1. Mirroring catalog contents to registries on the same network

You can mirror catalog contents to registries on the same network. 

If your mirror registry is co-located on the same network as your workstation with unrestricted network access, take the following actions on your workstation. 

**Procedure**

  1. If your mirror registry requires authentication, run the following command to log in to the registry: 

```shell-session
$ podman login <mirror_registry>
```


  2. Run the following command to extract and mirror the content to the mirror registry: 

```shell-session
$ oc adm catalog mirror \
    <index_image> \
    <mirror_registry>:<port>[/<repository>] \
    [-a ${REG_CREDS}] \
    [--insecure] \
    [--index-filter-by-os='<platform>/<arch>'] \
    [--manifests-only]
```


where: 

`<index_image>`
     Specifies the index image for the catalog that you want to mirror. 
`<mirror_registry>:<port>[/<repository>]`
     Specifies the fully qualified domain name (FQDN) for the target registry to mirror the Operator contents to. The mirror registry `<repository>` can be any existing repository, or namespace, on the registry, for example `olm-mirror` as outlined in the prerequisites. If there is an existing repository found during mirroring, the repository name is added to the resulting image name. If you do not want the image name to include the repository name, omit the `<repository>` value from this line, for example `<mirror_registry>:<port>`. 
`-a ${REG_CREDS}`
     Specifies the location of your registry credentials file. `{REG_CREDS}` is required for `registry.redhat.io`. This is optional. 
`--insecure`
     Specifies the `--insecure` flag. If you do not want to configure trust for the target registry, add the `--insecure` flag. This is optional. 
`--index-filter-by-os='<platform>/<arch>'`
     Specifies which platform and architecture of the index image to select when multiple variants are available. This is optional. Images are specified as `'<platform>/<arch>[/<variant>]'`. This does not apply to images referenced by the index. Valid values are `linux/amd64`, `linux/ppc64le`, `linux/s390x`, `linux/arm64`, and `.*`
`--manifests-only`
     Specifies the `--manifests-only` flag. This flag is optional. Generates only the manifests required for mirroring without actually mirroring the image content to a registry. This option can be useful for reviewing what will be mirrored, and lets you make any changes to the mapping list, if you require only a subset of packages. You can then use the `mapping.txt` file with the `oc image mirror` command to mirror the modified list of images in a later step. This flag is intended for only advanced selective mirroring of content from the catalog. 

```shell-session
src image has index label for database path: /database/index.db
using database path mapping: /database/index.db:/tmp/153048078
wrote database to /tmp/153048078
...
wrote mirroring manifests to manifests-redhat-operator-index-1614211642
```


where: 

`/tmp/153048078`
     Specifies the directory for the temporary `index.db` database generated by the command. 
`manifests-redhat-operator-index-1614211642`
    

Records the manifests directory name that is generated. This directory is referenced in subsequent procedures. 

Note

Red Hat Quay does not support nested repositories. As a result, running the `oc adm catalog mirror` command will fail with a `401` unauthorized error. As a workaround, you can use the `--max-components=2` option when running the `oc adm catalog mirror` command to disable the creation of nested repositories. For more information on this workaround, see the [Unauthorized error thrown while using catalog mirror command with Quay registry](https://access.redhat.com/solutions/5440741) Knowledgebase Solution. 




### 8.7.2.2. Mirroring catalog contents to airgapped registries

You can mirror catalog contents into airgapped registries. 

If your mirror registry is on a completely disconnected, or airgapped, host, take the following actions. 

**Procedure**

  1. Run the following command on your workstation with unrestricted network access to mirror the content to local files: 

```shell-session
$ oc adm catalog mirror \
    <index_image> \
    file:///local/index \
    -a ${REG_CREDS} \
    --insecure \
    --index-filter-by-os='<platform>/<arch>'
```


where: 

`<index image>`
     Specifies the index image for the catalog that you want to mirror. 
`<file:///local/index>`
     Specifies the content to mirror to local files in your current directory. 
`-a ${REG_CREDS}`
     Specifies the location of your registry credentials file. This is optional. 
`--insecure`
     Specifies the `--insecure` flag. This flag is optional. If you do not want to configure trust for the target registry, add the `--insecure` flag. 
`<platform>/<arch>`
     Specifies which platform and architecture of the index image to select when multiple variants are available. This is optional. Images are specified as `'<platform>/<arch>[/<variant>]'`. This does not apply to images referenced by the index. Valid values are `linux/amd64`, `linux/ppc64le`, `linux/s390x`, `linux/arm64`, and `.*`

```shell-session
...
info: Mirroring completed in 5.93s (5.915MB/s)
wrote mirroring manifests to manifests-my-index-1614985528

To upload local images to a registry, run:

	oc adm catalog mirror file://local/index/myrepo/my-index:v1 REGISTRY/REPOSITORY
```


     * Record the manifests directory name that is generated. This directory is referenced in subsequent procedures. 
     * Record the expanded `file://` path that is based on your provided index image. This path is referenced in a subsequent step. 

This command creates a `v2/` directory in your current directory. 

  2. Copy the `v2/` directory to removable media. 
  3. Physically remove the media and attach it to a host in the disconnected environment that has access to the mirror registry. 
  4. If your mirror registry requires authentication, run the following command on your host in the disconnected environment to log in to the registry: 

```shell-session
$ podman login <mirror_registry>
```


  5. Run the following command from the parent directory containing the `v2/` directory to upload the images from local files to the mirror registry: 

```shell-session
$ oc adm catalog mirror \
    file://local/index/<repository>/<index_image>:<tag> \
    <mirror_registry>:<port>[/<repository>] \
    -a ${REG_CREDS} \
    --insecure \
    --index-filter-by-os='<platform>/<arch>'
```


where: 

`file://`
     Specifies the `file://` path from the previous command output. 
`<mirror_registry>:<port>[/<repository>]`
     Specifies the fully qualified domain name (FQDN) for the target registry to mirror the Operator contents to. The mirror registry `<repository>` can be any existing repository, or namespace, on the registry, for example `olm-mirror` as outlined in the prerequisites. If there is an existing repository found during mirroring, the repository name is added to the resulting image name. If you do not want the image name to include the repository name, omit the `<repository>` value from this line, for example `<mirror_registry>:<port>`. 
`-a ${REG_CREDS}`
     Specifies the location of your registry credentials file. This is optional. 
`--insecure`
     Specifies the `--insecure` flag. This flag is optional. If you do not want to configure trust for the target registry, add the `--insecure` flag. 
`--index-filter-by-os='<platform>/<arch>'`
    

Specifies which platform and architecture of the index image to select when multiple variants are available. This is optional. Images are specified as `'<platform>/<arch>[/<variant>]'`. This does not apply to images referenced by the index. Valid values are `linux/amd64`, `linux/ppc64le`, `linux/s390x`, `linux/arm64`, and `.*`

Note

Red Hat Quay does not support nested repositories. As a result, running the `oc adm catalog mirror` command will fail with a `401` unauthorized error. As a workaround, you can use the `--max-components=2` option when running the `oc adm catalog mirror` command to disable the creation of nested repositories. For more information on this workaround, see the [Unauthorized error thrown while using catalog mirror command with Quay registry](https://access.redhat.com/solutions/5440741) Knowledgebase Solution. 

  6. Run the `oc adm catalog mirror` command again. Use the newly mirrored index image as the source and the same mirror registry target used in the previous step: 

```shell-session
$ oc adm catalog mirror \
    <mirror_registry>:<port>/<index_image> \
    <mirror_registry>:<port>[/<repository>] \
    --manifests-only \
    [-a ${REG_CREDS}] \
    [--insecure]
```


The `--manifests-only` flag is required for this step so that the command does not copy all of the mirrored content again. 

Important

This step is required because the image mappings in the `imageContentSourcePolicy.yaml` file generated during the previous step must be updated from local paths to valid mirror locations. Failure to do so will cause errors when you create the `ImageContentSourcePolicy` object in a later step. 

After you mirror the catalog, you can continue with the remainder of your cluster installation. After your cluster installation has finished successfully, you must specify the manifests directory from this procedure to create the `ImageContentSourcePolicy` and `CatalogSource` objects. These objects are required to enable installation of Operators from the software catalog. 




**Additional resources**

  * [Unauthorized error thrown while using catalog mirror command with Quay registry](https://access.redhat.com/solutions/5440741)



## 8.7.3. Generated manifests

After mirroring Operator catalog content to your mirror registry, a manifests directory is generated in your current directory. 

If you mirrored content to a registry on the same network, the directory name takes the following pattern: 

```plaintext
manifests-<index_image_name>-<random_number>
```


If you mirrored content to a registry on a disconnected host in the previous section, the directory name takes the following pattern: 

```plaintext
manifests-index/<repository>/<index_image_name>-<random_number>
```


Note

The manifests directory name is referenced in subsequent procedures. 

The manifests directory contains the following files, some of which might require further modification: 

  * The `catalogSource.yaml` file is a basic definition for a `CatalogSource` object that is pre-populated with your index image tag and other relevant metadata. This file can be used as is or modified to add the catalog source to your cluster. 

Important

If you mirrored the content to local files, you must modify your `catalogSource.yaml` file to remove any backslash (`/`) characters from the `metadata.name` field. Otherwise, when you attempt to create the object, it fails with an "invalid resource name" error. 

  * The `imageContentSourcePolicy.yaml` file defines an `ImageContentSourcePolicy` object that can configure nodes to translate between the image references stored in Operator manifests and the mirrored registry. 

Note

If your cluster uses an `ImageContentSourcePolicy` object to configure repository mirroring, you can use only global pull secrets for mirrored registries. You cannot add a pull secret to a project. 

  * The `mapping.txt` file contains all of the source images and where to map them in the target registry. This file is compatible with the `oc image mirror` command and can be used to further customize the mirroring configuration. 

Important

If you used the `--manifests-only` flag during the mirroring process and want to further trim the subset of packages to mirror, see the steps in the [Mirroring a package manifest format catalog image](https://docs.openshift.com/container-platform/4.7/operators/admin/olm-managing-custom-catalogs.html#olm-mirroring-package-manifest-catalog_olm-managing-custom-catalogs) procedure of the OpenShift Container Platform 4.7 documentation about modifying your `mapping.txt` file and using the file with the `oc image mirror` command. 




## 8.7.4. Postinstallation requirements

After mirroring the catalog and completing the cluster installation, you must create `ImageContentSourcePolicy` and `CatalogSource` objects from the manifests directory to enable installation of Operators from the software catalog. 

**Additional resources**

  * [Populating the software catalog from mirrored Operator catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#post-install-mirrored-catalogs_post-install-preparing-for-users)
  * [Updating or filtering a file-based catalog image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-filtering-fbc_olm-managing-custom-catalogs)
