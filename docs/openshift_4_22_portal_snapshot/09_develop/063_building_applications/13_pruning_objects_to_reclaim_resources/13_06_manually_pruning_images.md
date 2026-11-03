# 13.6. Manually pruning images

Manually remove orphaned image data from your integrated OpenShift image registry to reclaim storage capacity and prevent node disk exhaustion. 

The pruning custom resource enables automatic image pruning for the images from the OpenShift image registry. Administrators can manually prune images with the `oc adm prune images <image_prune_option>` command. 

For example: 

```shell-session
$ oc adm prune images <image_prune_option>
```


For more information about available pruning options, see "Manual image pruning command options". 

This command removes images that are no longer required by the system. 

Depending on your needs, you can prune images based on their age and tag history, or prune images that cause a project to exceed its defined storage limits. 

## 13.6.1. Image pruning considerations

Review soft-delete conditions and registry caching behaviors before pruning images to prevent metadata corruption and protect active container deployment layers. 

  * Pruning with the `--namespace` flag does not remove images. It only removes image streams, because images are cluster-scoped resources. Limiting pruning to a particular namespace makes it impossible to calculate current usage. 
  * By default, the integrated registry caches metadata of blobs to reduce the number of requests to storage, and to increase request-processing speed. Pruning does not update the integrated registry cache. Images that still contain pruned layers after pruning will be broken because the pruned layers that have metadata in the cache will not be pushed. Therefore, you must redeploy the registry to clear the cache after pruning: 

```shell-session
$ oc rollout restart deployment/image-registry -n openshift-image-registry
```


  * If the integrated registry uses a Redis cache, you must clean the database manually. 
  * If redeploying the registry after pruning is not an option, then you must permanently disable the cache. 
  * `oc adm prune images` operations require a route for your registry. Registry routes are not created by default. 



## 13.6.2. Image pruning limitations

Review image layer removal rules and external registry limitations before running prune operations to predict layer deletion and avoid unpruned image streams. 

  * Pruning images from external registries is unsupported. 
  * When an image is pruned, all references to the image are removed from all image streams that contain the image in `status.tags`. 
  * Image layers that are no longer referenced by any images are removed. 



## 13.6.3. Image prune conditions

Review the prerequisites, dependency checks, and soft-delete conditions required before removing registry images to safely prune image layers without breaking active pod deployments. 

OpenShift Container Platform supports two methodologies for pruning images: 

  1. Pruning by age and tag 
  2. Pruning by size limit 



These methodologies are mutually exclusive. You must choose whether to prune by age and tag, or by size limit. Regardless of the method that you choose, the image pruner checks to ensure that images in use are not removed. 

An image is only pruned if it meets the primary condition **and** is not actively referenced by a system component. 

Image pruning by age and tag
    

Pruning an image by age and tag is the default pruning strategy. It identifies images for removal by using the `--keep-younger-than` and `--keep-tag-revisions` flags. To prune an image by age and tag, the image must be older than the `--keep-younger-than` threshold, not one of the most recent tag revisions, and cannot be in use by an active workload. 

For an image to be pruned by age and tag, **all** of the following conditions must be met: 

  1. The image is managed by OpenShift Container Platform or has the `openshift.io/image.managed` annotation. 
  2. The image is older than the time specified by the `--keep-younger-than` flag. 
  3. The image is not one of the most recent images for its tag, as specified by the `--keep-tag-revisions` flag. 
  4. The image is **not** currently referenced by any of the following active or recent API objects: 

     * Pods or image streams created more recently than the `--keep-younger-than` duration. 
     * Running or pending pods 
     * Deployments, replication controllers, replica sets, or stateful sets. 
     * Builds, build configurations, jobs, or cronjobs. 

An image is only removed if it is old, not a recent tag revision, and is confirmed to have no active references by system components. 




Image pruning by size limit
    

Pruning an image by size limit uses the `--prune-over-size-limit` flag. This method is used to bring a project back under its defined image storage limit. 

Note

The `--prune-over-size-limit` flag cannot be combined with the `--keep-tag-revisions` flag nor the `--keep-younger-than` flags. Doing so returns information that this operation is not allowed. 

For an image to be pruned using this method, all of the following conditions must be true: 

  1. The image is part of a project that is currently exceeding its smallest defined size limit. 
  2. The image is selected by the pruner as a candidate for deletion to reduce the total size. 
  3. The image is not currently referenced by any of the following active API objects: 

     * Pods that are in a `running` or `pending` state. 
     * Deployments, replication controllers, replica sets, or stateful sets. 
     * Builds, build configurations, jobs, or cronjobs. 

With this method, the primary trigger is the project’s size, but the safety check to ensure that the image is not actively in use is still performed. 




## 13.6.4. Run image prune operations

Securely remove unused container images from your registry to reclaim the cluster disk space and prevent registry storage exhaustion. 

**Prerequisites**

  * You must be logged into the CLI with an access token. 
  * You must have the `system:image-pruner` cluster role or greater (for example, `cluster-admin`). 
  * The image registry must be exposed. 
  * You have reviewed the "Considerations when manually pruning images" section of this document. 



**Procedure**

  1. Optional: To preview which images would be pruned, enter the following command. This command prints a list of the images, image streams, and pods that would be removed. Note that nothing is deleted until you add the `--confirm` flag. 

```shell-session
$ oc adm prune images <image_prune_option_one> <image_prune_option_two>
```


For more information about available pruning options, see "Manual image pruning command options". 

  2. Review the output to confirm the list of images, image streams, and pods to be removed. 
  3. Run the `oc adm prune images` command with the appropriate options for your cluster. Add the `--confirm` flag to confirm deletion. For example: 

```shell-session
$ oc adm prune images <image_prune_option_one> <image_prune_option_two> --confirm
```


## 13.6.5. Use secure or insecure connections

Configure secure or insecure flags when pruning images to communicate with image registries. Setting custom CA certificates or bypassing HTTPS verification prevents connection failures during pruning. 

The secure connection is the preferred and recommended approach. It is done over HTTPS protocol with a mandatory certificate verification. The `prune` command always attempts to use it if possible. If it is not possible, in some cases it can fall-back to insecure connection, which is dangerous. In this case, either certificate verification is skipped or plain HTTP protocol is used. 

The fall-back to insecure connection is allowed in the following cases unless `--certificate-authority` is specified: 

  1. The `prune` command is run with the `--force-insecure` option. 
  2. The provided `registry-url` is prefixed with the `http://` scheme. 
  3. The provided `registry-url` is a local-link address or `localhost`. 
  4. The configuration of the current user allows for an insecure connection. This can be caused by the user either logging in using `--insecure-skip-tls-verify` or choosing the insecure connection when prompted. 



Important

If the registry is secured by a certificate authority different from the one used by OpenShift Container Platform, it must be specified using the `--certificate-authority` flag. Otherwise, the `prune` command fails with an error. 

## 13.6.6. Image pruning CLI options

Review the CLI options for the `oc adm prune images` command to configure flags for age thresholds, tag references, and registry endpoints. 

The following table describes the options you can use with the `oc adm prune images <image_prune_option>` command. 

Table 13.4. Manual image pruning command optionsOption| Description  
---|---  
`--all` |  Include images that were not pushed to the registry, but have been mirrored by pullthrough. This is on by default. To limit the pruning to images that were pushed to the integrated registry, pass `--all=false`.   
`--certificate-authority` |  The path to a certificate authority file to use when communicating with the OpenShift Container Platform-managed registries. Defaults to the certificate authority data from the current user’s configuration file. If provided, a secure connection is initiated.   
`--confirm` |  Indicate that pruning should occur, instead of performing a test-run. This requires a valid route to the integrated container image registry. If this command is run outside of the cluster network, the route must be provided using `--registry-url`.   
`--force-insecure` |  Use caution with this option. Allow an insecure connection to the container registry that is hosted via HTTP or has an invalid HTTPS certificate.   
`--keep-tag-revisions=<N>` |  For each imagestream, keep up to at most `N` image revisions per tag (default `3`).   
`--keep-younger-than=<duration>` |  Do not prune any image that is younger than `<duration>` relative to the current time. Alternately, do not prune any image that is referenced by any other object that is younger than `<duration>` relative to the current time (default `60m`).   
`--prune-over-size-limit` |  Prune each image that exceeds the smallest limit defined in the same project. This flag cannot be combined with `--keep-tag-revisions` nor `--keep-younger-than`.   
`--registry-url` |  The address to use when contacting the registry. The command attempts to use a cluster-internal URL determined from managed images and image streams. In case it fails (the registry cannot be resolved or reached), an alternative route that works needs to be provided using this flag. The registry hostname can be prefixed by `https://` or `http://`, which enforces particular connection protocol.   
`--prune-registry` |  In conjunction with the conditions stipulated by the other options, this option controls whether the data in the registry corresponding to the OpenShift Container Platform image API object is pruned. By default, image pruning processes both the image API objects and corresponding data in the registry.  This option is useful when you are only concerned with removing etcd content, to reduce the number of image objects but are not concerned with cleaning up registry storage, or if you intend to do that separately by hard pruning the registry during an appropriate maintenance window for the registry.   
Show more

Additional information about the `--prune-registry` flag
    

You can separate the removal of OpenShift Container Platform image API objects from the removal of image data in the registry by passing in the `--prune-registry=false` flag. For example, the following command prunes only the API objects, leaving the registry storage untouched: 

```shell-session
$ oc adm prune images --keep-tag-revisions=3 --keep-younger-than=60m --confirm --prune-registry=false
```


Then, you can perform a hard prune of the registry to remove the associated image data. This approach can narrow the timing window for race conditions compared to pruning both in a single command. 

However, timing windows are not completely eliminated. For example, a pod might still be created that references an image while that image is being identified for pruning. You should track any API objects created during pruning to ensure that they do not reference deleted content. 

Re-running the pruning without the `--prune-registry` option, or with `--prune-registry=true`, does not remove the associated registry storage for images previously pruned with `--prune-registry=false`. Those images can only be removed from registry storage by performing a hard prune of the registry. For more information, see "Hard pruning the registry". 

## 13.6.7. Image pruning issues

Identify the image pruning issues in your cluster to diagnose unpruned images, manage tag revision thresholds, and fix connection or certificate authority errors between the CLI client and registry. 

Images not being pruned
    

If your images keep accumulating and the `prune` command removes just a small portion of what you expect, ensure that you understand the image prune conditions that must apply for an image to be considered a candidate for pruning. 

Ensure that images you want removed occur at higher positions in each tag history than your chosen tag revisions threshold. For example, consider an old and obsolete image named `sha256:abz`. By running the following command in your namespace, where the image is tagged, the image is tagged three times in a single image stream named `myapp`: 

```shell-session
$ oc get is -n <namespace> -o go-template='{{range $isi, $is := .items}}{{range $ti, $tag := $is.status.tags}}'\
'{{range $ii, $item := $tag.items}}{{if eq $item.image "sha256:<hash>"}}{{$is.metadata.name}}:{{$tag.tag}} at position {{$ii}} out of {{len $tag.items}}\n'\
'{{end}}{{end}}{{end}}{{end}}'
```


**Example output**

```shell-session
myapp:v2 at position 4 out of 5
myapp:v2.1 at position 2 out of 2
myapp:v2.1-may-2016 at position 0 out of 1
```


When default options are used, the image is never pruned because it occurs at position `0` in a history of `myapp:v2.1-may-2016` tag. For an image to be considered for pruning, the administrator must either: 

  * Specify `--keep-tag-revisions=0` with the `oc adm prune images` command. 

Warning

This action removes all the tags from all the namespaces with underlying images, unless they are younger or they are referenced by objects younger than the specified threshold. 

  * Delete all the `istags` where the position is below the revision threshold, which means `myapp:v2.1` and `myapp:v2.1-may-2016`. 
  * Move the image further in the history, either by running new builds pushing to the same `istag`, or by tagging other image. This is not always desirable for old release tags. 

Tags having a date or time of a particular image’s build in their names should be avoided, unless the image must be preserved for an undefined amount of time. Such tags tend to have just one image in their history, which prevents them from ever being pruned. 




Secure connection to an insecure registry
    

If you see a message similar to the following in the output of the `oc adm prune images` command, then your registry is not secured and the `oc adm prune images` client attempts to use a secure connection: 

```shell-session
error: error communicating with registry: Get https://172.30.30.30:5000/healthz: http: server gave HTTP response to HTTPS client
```


  * The recommended solution is to secure the registry. Otherwise, you can force the client to use an insecure connection by appending `--force-insecure` to the command; however, this is not recommended. 



Insecure connection to a secured registry
    

If you see one of the following errors in the output of the `oc adm prune images` command, it means that your registry is secured using a certificate signed by a certificate authority other than the one used by `oc adm prune images` client for connection verification: 

```shell-session
error: error communicating with registry: Get http://172.30.30.30:5000/healthz: malformed HTTP response "\x15\x03\x01\x00\x02\x02"
error: error communicating with registry: [Get https://172.30.30.30:5000/healthz: x509: certificate signed by unknown authority, Get http://172.30.30.30:5000/healthz: malformed HTTP response "\x15\x03\x01\x00\x02\x02"]
```


By default, the certificate authority data stored in the user’s configuration files is used; the same is true for communication with the control plane API. 

Use the `--certificate-authority` option to provide the right certificate authority for the container image registry server. 

Wrong certificate authority
    

The following error means that the certificate authority used to sign the certificate of the secured container image registry is different from the authority used by the client: 

```shell-session
error: error communicating with registry: Get https://172.30.30.30:5000/: x509: certificate signed by unknown authority
```


Make sure to provide the right one with the flag `--certificate-authority`. 

As a workaround, the `--force-insecure` flag can be added instead. However, this is not recommended. 

**Additional resources**

  * [Accessing the registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/registry/#accessing-the-registry)
  * [Exposing the registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/registry/#securing-exposing-registry)
  * [Image Registry Operator in OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/registry/#configuring-registry-operator)
