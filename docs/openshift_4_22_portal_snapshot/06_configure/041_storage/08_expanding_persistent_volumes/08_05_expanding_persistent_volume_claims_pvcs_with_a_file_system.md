# 8.5. Expanding persistent volume claims (PVCs) with a file system

To expand your storage capacity and meet growing data needs, you can resize existing volumes without recreating them. 

Expanding persistent volume claims (PVCs) based on volume types that need file system resizing, such as Google Cloud Platform (GCP) persistent disk (PD), AWS Elastic Block Storage (EBS), and Cinder, is a two-step process. First, expand the volume objects in the cloud provider. Second, expand the file system on the node. 

Expanding the file system on the node only happens when a new pod is started with the volume. 

**Prerequisites**

  * The controlling storage class has the `allowVolumeExpansion` field set to `true`. 

For more information, see section _Enabling volume expansion support_. 




**Procedure**

  * Edit the PVC and request a new size by editing `spec.resources.requests`. For example, the following expands the `ebs` PVC to 8 Gi: 

**Example PVC YAML file**

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: ebs
spec:
  storageClass: "storageClassWithFlagSet"
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
```


Where updating `spec.resources.requests` to a larger amount expands the PVC. 




**Verification**

After the cloud provider object has finished resizing, the PVC is set to `FileSystemResizePending`. 

  * Check the condition by running the following command: 

```shell-session
$ oc describe pvc <pvc_name>
```


**Next steps**

When the cloud provider object has finished resizing, the `PersistentVolume` object reflects the newly requested size in `PersistentVolume.Spec.Capacity`. You can now create or recreate a new pod from the PVC to finish the file system resizing. After the pod is running, the newly requested size is available and the `FileSystemResizePending` condition is removed from the PVC.
