# 6.8. Import and work with images and image streams

To bring container images into your OpenShift Container Platform cluster and manage their references, you can import images from external registries and organize them by using image streams. By using this process, you can maintain a centralized registry of container images for your applications. 

The following sections describe how to import, and work with, image streams. 

## 6.8.1. Import images and image streams from private registries

To securely manage content from external sources, configure your image streams to import tag and image metadata from private registries requiring authentication. 

This procedure is essential if you change the registry that the Cluster Samples Operator uses for pulling content to something other than the default [registry.redhat.io](https://registry.redhat.io). 

Note

When importing from insecure or secure registries, the registry URL defined in the secret must include the `:80` port suffix or the secret is not used when attempting to import from the registry. 

**Procedure**

  1. You must create a `secret` object that is used to store your credentials by entering the following command: 

```shell-session
$ oc create secret generic <secret_name> --from-file=.dockerconfigjson=<file_absolute_path> --type=kubernetes.io/dockerconfigjson
```


  2. After the secret is configured, create the new image stream or enter the `oc import-image` command: 

```shell-session
$ oc import-image <imagestreamtag> --from=<image> --confirm
```


During the import process, OpenShift Container Platform picks up the secrets and provides them to the remote party. 




## 6.8.2. Working with manifest lists

To manage multi-architecture images in a manifest list, use the `--import-mode` flag with `oc import-image` or `oc tag`. Importing a single sub-manifest or all manifests provides fine-grained control over your image stream content. 

In some cases, users might want to use sub-manifests directly. When `oc adm prune images` is run, or the `CronJob` pruner runs, they cannot detect when a sub-manifest list is used. As a result, an administrator using `oc adm prune images`, or the `CronJob` pruner, might delete entire manifest lists, including sub-manifests. 

To avoid this limitation, you can use the manifest list by tag or by digest instead. 

**Procedure**

  * Create an image stream that includes multi-architecture images, and sets the import mode to `PreserveOriginal`, by entering the following command: 

```shell-session
$ oc import-image <multiarch-image-stream-tag>  --from=<registry>/<project_name>/<image-name> \
--import-mode='PreserveOriginal' --reference-policy=local --confirm
```


**Example output**

```shell-session
---
Arch:           <none>
Manifests:      linux/amd64     sha256:6e325b86566fafd3c4683a05a219c30c421fbccbf8d87ab9d20d4ec1131c3451
                linux/arm64     sha256:d8fad562ffa75b96212c4a6dc81faf327d67714ed85475bf642729703a2b5bf6
                linux/ppc64le   sha256:7b7e25338e40d8bdeb1b28e37fef5e64f0afd412530b257f5b02b30851f416e1
---
```


  * Alternatively, enter the following command to import an image with the `Legacy` import mode, which discards manifest lists and imports a single sub-manifest: 

```shell-session
$ oc import-image <multiarch-image-stream-tag>  --from=<registry>/<project_name>/<image-name> \
--import-mode='Legacy' --confirm
```


Note

The `--import-mode=` default value is `Legacy`. Excluding this value, or failing to specify either `Legacy` or `PreserveOriginal`, imports a single sub-manifest. An invalid import mode returns the following error: `error: valid ImportMode values are Legacy or PreserveOriginal`. 




### 6.8.2.1. Configure periodic importing of manifest lists

To maintain up-to-date image references for complex, multi-architecture images, configure periodic importing of manifest lists. To periodically re-import a manifest list, you can use the `--scheduled` flag, ensuring your image stream tracks the latest versions from external registries. 

**Procedure**

  * Set the image stream to periodically update the manifest list by entering the following command: 

```shell-session
$ oc import-image <multiarch-image-stream-tag>  --from=<registry>/<project_name>/<image-name> \
--import-mode='PreserveOriginal' --scheduled=true
```


### 6.8.2.2. Configure SSL/TLS when importing manifest lists

To control connection security and access policies for manifest lists sourced from external repositories, configure SSL/TLS settings during image importing. 

To configure SSL/TLS when importing a manifest list, you can use the `--insecure` flag to bypass standard certificate validation requirements if necessary. 

**Procedure**

  * Set `--insecure=true` so that importing a manifest list skips SSL/TLS verification. For example: 

```shell-session
$ oc import-image <multiarch-image-stream-tag> --from=<registry>/<project_name>/<image-name> \
--import-mode='PreserveOriginal' --insecure=true
```


## 6.8.3. Specify architecture for --import-mode

To control the architecture of your imported images and ensure proper deployment, use the `--import-mode=` flag. You can swap your imported image stream between multi-architecture and single architecture by excluding or including the `--import-mode=` flag as needed. 

**Procedure**

  * Run the following command to update your image stream from multi-architecture to single architecture by excluding the `--import-mode=` flag: 

```shell-session
$ oc import-image <multiarch-image-stream-tag> --from=<registry>/<project_name>/<image-name>
```


  * Run the following command to update your image stream from single-architecture to multi-architecture: 

```shell-session
$ oc import-image <multiarch_image_stream_tag>  --from=<registry>/<project_name>/<image_name> \
--import-mode='PreserveOriginal'
```


## 6.8.4. Configuration fields for --import-mode

To implement multi-architecture image management using the `--import-mode` flag, reference the necessary configuration fields. These fields define precise parameters for selecting and importing specific manifests into your OpenShift Container Platform cluster. 

The following table describes the options available for the `--import-mode=` flag: 

Parameter| Description  
---|---  
**Legacy** |  The default option for `--import-mode`. When specified, the manifest list is discarded, and a single sub-manifest is imported. The platform is chosen in the following order of priority: 

  1. Tag annotations 
  2. Control plane architecture 
  3. Linux/AMD64 
  4. The first manifest in the list 

  
**PreserveOriginal** |  When specified, the original manifest is preserved. For manifest lists, the manifest list and all of its sub-manifests are imported.   
Show more
