# 12.2. Verifying the configuration

The connection configuration process updates operator statuses and control plane nodes. It takes approximately an hour to complete. During the configuration process, the nodes reboot. Previously bound `PersistentVolumeClaims` objects might become disconnected. 

**Prerequisites**

  * You have saved the configuration settings in the **vSphere connection configuration** wizard. 



**Procedure**

  1. Check that the configuration process completed successfully: 

     1. In the OpenShift Container Platform Administrator perspective, navigate to **Home Overview**. 
     2. Under **Status** click **Operators**. Wait for all operator statuses to change from **Progressing** to **All succeeded**. A **Failed** status indicates that the configuration failed. 
     3. Under **Status** , click **Control Plane**. Wait for the response rate of all Control Pane components to return to 100%. A **Failed** control plane component indicates that the configuration failed. 

A failure indicates that at least one of the connection settings is incorrect. Change the settings in the **vSphere connection configuration** wizard and save the configuration again. 

  2. Check that you are able to bind `PersistentVolumeClaims` objects by performing the following steps: 

     1. Create a `StorageClass` object using the following YAML: 

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: vsphere-sc
provisioner: kubernetes.io/vsphere-volume
parameters:
 datastore: YOURVCENTERDATASTORE
 diskformat: thin
reclaimPolicy: Delete
volumeBindingMode: Immediate
```


     2. Create a `PersistentVolumeClaims` object using the following YAML: 

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
 name: test-pvc
 namespace: openshift-config
 annotations:
   volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
 finalizers:
   - kubernetes.io/pvc-protection
spec:
 accessModes:
   - ReadWriteOnce
 resources:
   requests:
    storage: 10Gi
 storageClassName: vsphere-sc
 volumeMode: Filesystem
```


If you are unable to create a `PersistentVolumeClaims` object, you can troubleshoot by navigating to **Storage** **PersistentVolumeClaims** in the **Administrator** perspective of the OpenShift Container Platform web console.
