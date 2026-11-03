# 8.6. Recovering from failure when expanding volumes

If a resize request fails or remains in a pending state, you can try again by entering a different resize value in `.spec.resources.requests.storage` for the persistent volume claim (PVC). The new value must be larger than the original volume size. 

If entering another smaller resize value in `.spec.resources.requests.storage` for the PVC does not work, use the following procedure to recover. 

**Procedure**

  1. Mark the persistent volume (PV) that is bound to the PVC with the `Retain` reclaim policy. Change the `persistentVolumeReclaimPolicy` field to `Retain`. 
  2. Delete the PVC. 
  3. Manually edit the PV and delete the `claimRef` entry from the PV specification to ensure that the newly created PVC can bind to the PV marked `Retain`. This marks the PV as `Available`. 
  4. Recreate the PVC in a smaller size, or a size that can be allocated by the underlying storage provider. 
  5. Set the `volumeName` field of the PVC to the name of the PV. This binds the PVC to the provisioned PV only. 
  6. Restore the reclaim policy on the PV.
