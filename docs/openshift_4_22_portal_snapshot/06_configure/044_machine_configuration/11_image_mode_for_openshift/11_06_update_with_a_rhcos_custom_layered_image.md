# 11.6. Update with a RHCOS custom layered image

When you configure image mode for OpenShift, OpenShift Container Platform no longer automatically updates the node pool that uses the custom layered image. You become responsible to manually update your nodes as appropriate. 

Updating a node with a custom layered image is not required. However, if that node gets too far behind the current OpenShift Container Platform version, you could experience unexpected results. 

To update a node that uses a custom layered image, follow these general steps: 

  1. The cluster automatically upgrades to version x.y.z+1, except for the nodes that use the custom layered image. 
  2. You could then create a new Containerfile that references the updated OpenShift Container Platform image and the RPM that you had previously applied. 
  3. Create a new machine config that points to the updated custom layered image.
