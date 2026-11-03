# 8.4. Expanding local volumes

To expand your Local Storage Operator (LSO) storage capacity and meet growing data needs, update the storage request in your persistent volume (PV) and persistent volume claim (PVC). This increases capacity for existing volumes without recreating them. 

**Procedure**

  1. Expand the underlying devices. Ensure that appropriate capacity is available on these devices. 
  2. Update the corresponding PV objects to match the new device sizes by editing the `.spec.capacity` field of the PV. 
  3. For the storage class that is used for binding the PVC to PV, set the `allowVolumeExpansion` field to `true`. 
  4. For the PVC, set `.spec.resources.requests.storage` to match the new size. 



**Result**

Kubelet should automatically expand the underlying file system on the volume, if necessary, and update the status field of the PVC to reflect the new size.
