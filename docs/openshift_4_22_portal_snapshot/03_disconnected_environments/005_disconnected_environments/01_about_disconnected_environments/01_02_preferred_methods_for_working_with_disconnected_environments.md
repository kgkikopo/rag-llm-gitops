# 1.2. Preferred methods for working with disconnected environments

You can choose between multiple options for most aspects of managing a cluster in a disconnected environment. For example, when mirroring images you can choose between using the oc-mirror OpenShift CLI (`oc`) plugin or using the `oc adm` command. 

However, some options provide a simpler and more convenient user experience for disconnected environments, and are the preferred method over their alternatives. 

Unless your organizational needs require you to choose another option, use the following methods for mirroring images, installing your cluster, and updating your cluster: 

  * Mirror your images using the oc-mirror plugin v2. For more information, see "Mirroring images for a disconnected installation by using the oc-mirror plugin v2". 
  * Install your cluster using the Agent-based Installer. For more information, see "Installing a cluster with customizations". 
  * Update your cluster using a local OpenShift Update Service instance. For more information, see "Updating a cluster in a disconnected environment using the OpenShift Update Service".
