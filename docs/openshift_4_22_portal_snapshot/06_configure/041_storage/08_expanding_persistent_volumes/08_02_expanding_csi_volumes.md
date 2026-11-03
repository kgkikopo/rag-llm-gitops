# 8.2. Expanding CSI volumes

You can use the Container Storage Interface (CSI) to expand storage volumes after they have already been created. 

Important

Shrinking persistent volumes (PVs) is _not_ supported. 

**Prerequisites**

  * The underlying CSI driver supports resize. 

For information about which CSI drivers support resizing, see under the _Additional resources_ section "CSI drivers supported by OpenShift Container Platform". 

  * Dynamic provisioning is used. 
  * The controlling `StorageClass` object has `allowVolumeExpansion` set to `true`. 

For more information, see section _Enabling volume expansion support_. 




**Procedure**

  * For the persistent volume claim (PVC), set `.spec.resources.requests.storage` to the desired new size. 



**Verification**

  * To confirm that the resize is finished, look at the `status.conditions` field of the PVC . OpenShift Container Platform adds the `Resizing` condition to the PVC during expansion, which is removed after expansion completes.
