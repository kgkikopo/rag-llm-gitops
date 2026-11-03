# 6.2. Migrating to oc-mirror plugin v2

To migrate from oc-mirror plugin v1 to v2, you must manually update the `ImageSetConfiguration` file, modify mirroring commands, and clean up v1 artifacts. 

**Procedure**

  1. Modify the API version and remove deprecated fields in your `ImageSetConfiguration`. 

**Example`ImageSetConfiguration` file with oc-mirror plugin v1 configuration**

```yaml
kind: ImageSetConfiguration
apiVersion: mirror.openshift.io/v1alpha2
mirror:
  platform:
    channels:
      - name: stable-4.17
    graph: true
  helm:
    repositories:
      - name: sbo
        url: https://redhat-developer.github.io/service-binding-operator-helm-chart/
  additionalImages:
    - name: registry.redhat.io/ubi8/ubi:latest
    - name: quay.io/openshifttest/hello-openshift@sha256:example_hash
  operators:
    - catalog: oci:///test/redhat-operator-index
      packages:
        - name: aws-load-balancer-operator
storageConfig:  # REMOVE this field in v2
  local:
    path: /var/lib/oc-mirror
```


**Example`ImageSetConfiguration` file with oc-mirror plugin v2 configuration**

```yaml
kind: ImageSetConfiguration
apiVersion: mirror.openshift.io/v2alpha1
mirror:
  platform:
    channels:
      - name: stable-4.17
    graph: true
  helm:
    repositories:
      - name: sbo
        url: https://redhat-developer.github.io/service-binding-operator-helm-chart/
  additionalImages:
    - name: registry.redhat.io/ubi8/ubi:latest
    - name: quay.io/openshifttest/hello-openshift@sha256:example_hash
  operators:
    - catalog: oci:///test/redhat-operator-index
      packages:
        - name: aws-load-balancer-operator
```


Note

When migrating from oc-mirror plugin v1 to v2, you must use explicit registry hostnames for all images listed under `additionalImages`. Otherwise, images are mirrored to incorrect target paths. 

  2. Check the `cluster-resources` directory inside the working directory for IDMS, ITMS, `CatalogSource`, and `ClusterCatalog` resources by running the following command: 

```shell-session
$ ls <v2_workspace>/working-dir/cluster-resources/
```


  3. Once the migration is complete, verify that mirrored images and catalogs are available: 

     * Ensure that no errors or warnings occurred during mirroring. 
     * Ensure that no error file was generated (`working-dir/logs/mirroring_errors_YYYYMMdd_HHmmss.txt`). 

  4. Verify that mirrored images and catalogs are available using the following the commands: 

```shell-session
$ oc get catalogsource -n openshift-marketplace
```


```shell-session
$ oc get imagedigestmirrorset,imagetagmirrorset
```


For more information, refer to "Mirroring images for a disconnected installation using oc-mirror plugin v2". 

  5. Optional: Remove images mirrored using oc-mirror plugin v1: 

     1. Mirror the images using oc-mirror plugin v1. 
     2. Update the API version in the `ImageSetConfiguration` file from `v1alpha2` (v1) to `v2alpha1` (v2), then run the following command: 

```shell-session
$ oc-mirror -c isc.yaml file://some-dir --v2
```


Note

`storageConfig` is not a valid field in the `ImageSetConfiguration` and `DeleteImageSetConfiguration` files. Remove this field when updating to oc-mirror plugin v2. 

     3. Generate a delete manifest and delete v1 images by running the following command: 

```shell-session
$ oc-mirror delete --config=delete-isc.yaml --generate --delete-v1-images --workspace file://some-dir docker://registry.example:5000  --v2
```


Important

oc-mirror plugin v2 does not automatically prune the destination registry, unlike oc-mirror plugin v1. To clean up images that are no longer needed, use the delete functionality in v2 with the `--delete-v1-images` command flag. 

Once all images mirrored with oc-mirror plugin v1 are removed, you no longer need to use this flag. If you need to delete images mirrored with oc-mirror plugin v2, do not set `--delete-v1-images`. 

For more information about deleting images, see "Deletion of images from your disconnected environment". 

     4. Delete images based on the generated manifest by running the following command: 

```shell-session
$ oc-mirror delete --delete-yaml-file some-dir/working-dir/delete/delete-images.yaml docker://registry.example:5000 --v2
```
