# 3.6. Block volume support

Raw block volumes are filesystem-free storage that applications access directly for improved performance. Specify `volumeMode: Block` in persistent volumes and claims, and configure privileged containers. Storage provider support varies: static only, dynamic only, both, or none. 

Important

Pods using raw block volumes must be configured to allow privileged containers. 

The following table displays which volume plugins support block volumes. 

Table 3.4. Block volume supportVolume Plugin| Manually provisioned| Dynamically provisioned| Fully supported  
---|---|---|---  
Amazon Elastic Block Store (Amazon EBS)  |  ✅  |  ✅  |  ✅   
Amazon Elastic File Storage (Amazon EFS)  |  |  |   
Azure Disk  |  ✅  |  ✅  |  ✅   
Azure File  |  |  |   
Cinder  |  ✅  |  ✅  |  ✅   
Fibre Channel  |  ✅  |  |  ✅   
GCP  |  ✅  |  ✅  |  ✅   
HostPath  |  |  |   
IBM Cloud Block Storage volume  |  ✅  |  ✅  |  ✅   
iSCSI  |  ✅  |  |  ✅   
Local volume  |  ✅  |  |  ✅   
LVM Storage  |  ✅  |  ✅  |  ✅   
NFS  |  |  |   
Red Hat OpenShift Data Foundation  |  ✅  |  ✅  |  ✅   
CIFS/SMB  |  |  |   
VMware vSphere  |  ✅  |  ✅  |  ✅   
Show more

Important

Using any of the block volumes that can be provisioned manually, but are not provided as fully supported, is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

## 3.6.1. Block volume examples

Raw block volume examples demonstrate configurations for applications requiring direct access to block storage devices without a filesystem. This approach is commonly used by databases and other applications that need low-level storage control, bypassing traditional filesystem layers. 

The examples show how to configure three essential components for block volume storage: 

  * `PersistentVolume` (PV) with `volumeMode`: `Block` to define the raw block storage resource. 
  * `PersistentVolumeClaim` (PVC) that requests block storage by setting `volumeMode`: `Block`. 
  * Pod specification that mounts the block device by using `volumeDevices` and `devicePath` instead of the typical `volumeMounts` and `mountPath` used for filesystem volumes. 



The following reference tables show the accepted values for `volumeMode` (Filesystem is the default, Block must be explicitly set) and the binding scenarios between PVs and PVCs. Understanding these binding rules is critical. PVs and PVCs must both specify `volumeMode`: `Block` to bind successfully. Mismatched volume modes, such as a Block PV with a Filesystem PVC, prevent binding, which can cause pod scheduling failures. 

**PV example**

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: block-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  persistentVolumeReclaimPolicy: Retain
  fc:
    targetWWNs: ["50060e801049cfd1"]
    lun: 0
    readOnly: false
```


`spec.volumeMode` must be set to `Block` to indicate that this PV is a raw block volume. 

**PVC example**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: block-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  resources:
    requests:
      storage: 10Gi
```


`spec.volumeMode` must be set to `Block` to indicate that a raw block PVC is requested. 

**Pod specification example**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-block-volume
spec:
  containers:
    - name: fc-container
      image: fedora:26
      command: ["/bin/sh", "-c"]
      args: [ "tail -f /dev/null" ]
      volumeDevices:
        - name: data
          devicePath: /dev/xvda
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: block-pvc
```


  * `spec.container.volumeDevices`: Instead of `volumeMounts`, this parameter is used for block devices. Only `PersistentVolumeClaim` sources can be used with raw block volumes. 
  * `spec.container.volumeDevices.devicePath`: Instead of `mountPath`, this parameter represents the path to the physical device where the raw block is mapped to the system. 
  * `spec.volumes.persistentVolumeClaim.claimName`: The volume source must be of type `persistentVolumeClaim` and must match the name of the PVC as expected. 



Table 3.5. Accepted values for volumeModeValue| Default  
---|---  
Filesystem  |  Yes   
Block  |  No   
Show more

Table 3.6. Binding scenarios for block volumesPV `volumeMode`| PVC `volumeMode`| Binding result  
---|---|---  
Filesystem  |  Filesystem  |  Bind   
Unspecified  |  Unspecified  |  Bind   
Filesystem  |  Unspecified  |  Bind   
Unspecified  |  Filesystem  |  Bind   
Block  |  Block  |  Bind   
Unspecified  |  Block  |  No Bind   
Block  |  Unspecified  |  No Bind   
Filesystem  |  Block  |  No Bind   
Block  |  Filesystem  |  No Bind   
Show more

Important

Unspecified values result in the default value of `Filesystem`.
