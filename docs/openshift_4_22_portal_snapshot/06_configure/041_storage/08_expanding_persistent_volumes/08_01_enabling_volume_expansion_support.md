# 8.1. Enabling volume expansion support

To enable volume expansion, the `StorageClass` object must have the `allowVolumeExpansion` field set to `true`. This prerequisite configuration allows persistent volume claims (PVCs) to be expanded after creation as your storage needs grow. 

**Procedure**

  * Edit the `StorageClass` object and add the `allowVolumeExpansion` attribute by running the following command: 

```shell-session
$ oc edit storageclass <storage_class_name>
```


Enter the name of storage class in `<storage_class_name>`. 

The following example shows adding this line at the bottom of the storage class configuration. 

**Example storage class YAML file with`allowVolumeExpansion` field set to `true`**

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
...
parameters:
  type: gp2
reclaimPolicy: Delete
allowVolumeExpansion: true
```


    * `parameters.allowVolumeExpansion`: Setting this field to `true` allows persistent volume claims (PVCs) to be expanded after creation.
