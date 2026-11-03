# 4.2. Mirror registry for Red Hat OpenShift introduction

For disconnected deployments of OpenShift Container Platform, a container registry is required to carry out the installation of the clusters. 

To run a production-grade registry service on such a cluster, you must create a separate registry deployment to install the first cluster. The _mirror registry for Red Hat OpenShift_ addresses this need and is included in every OpenShift Container Platform subscription. It is available for download on the "OpenShift console Downloads" page. 

The _mirror registry for Red Hat OpenShift_ allows users to install a small-scale version of Red Hat Quay and its required components by using the `mirror-registry` command-line interface (CLI) tool. The _mirror registry for Red Hat OpenShift_ is deployed automatically with pre-configured local storage and a local database. It also includes auto-generated user credentials and access permissions with a single set of inputs and no additional configuration choices to get started. 

The _mirror registry for Red Hat OpenShift_ provides a pre-determined network configuration and reports deployed component credentials and access URLs upon success. A limited set of optional configuration inputs such as fully qualified domain name (FQDN) services, superuser name and password, and custom TLS certificates are also provided. This provides users with a container registry so that they can easily create an offline mirror of all OpenShift Container Platform release content when running OpenShift Container Platform in restricted network environments. 

Use of the _mirror registry for Red Hat OpenShift_ is optional if another container registry is already available in the install environment. 

## 4.2.1. Mirror registry for Red Hat OpenShift limitations

The following limitations apply to the _mirror registry for Red Hat OpenShift_ : 

  * The _mirror registry for Red Hat OpenShift_ is not a highly-available registry and only local file system storage is supported. It is not intended to replace Red Hat Quay or the internal image registry for OpenShift Container Platform. 
  * The _mirror registry for Red Hat OpenShift_ is not intended to be a substitute for a production deployment of Red Hat Quay. 
  * The _mirror registry for Red Hat OpenShift_ is only supported for hosting images that are required to install a disconnected OpenShift Container Platform cluster, such as Release images or Red Hat Operator images. It uses local storage on your Red Hat Enterprise Linux (RHEL) machine, and storage supported by RHEL is supported by the _mirror registry for Red Hat OpenShift_. 

Note

Because the _mirror registry for Red Hat OpenShift_ uses local storage, you should remain aware of the storage usage consumed when mirroring images and use Red Hat Quay’s garbage collection feature to mitigate potential issues. For more information about this feature, see "Red Hat Quay garbage collection". 

  * Support for Red Hat product images that are pushed to the _mirror registry for Red Hat OpenShift_ for bootstrapping purposes are covered by valid subscriptions for each respective product. For a list of exceptions to further enable the bootstrap experience, see "Self-managed Red Hat OpenShift sizing and subscription guide". 
  * Content built by customers should not be hosted by the _mirror registry for Red Hat OpenShift_. 
  * Using the _mirror registry for Red Hat OpenShift_ with more than one cluster is discouraged because multiple clusters can create a single point of failure when updating your cluster fleet. Instead, use the _mirror registry for Red Hat OpenShift_ to install a cluster that can host a production-grade, highly-available registry such as Red Hat Quay, which can serve OpenShift Container Platform content to other clusters. 



**Additional resources**

  * [OpenShift console Downloads](https://console.redhat.com/openshift/downloads#tool-mirror-registry)
  * [Self-managed Red Hat OpenShift sizing and subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-sizing-subscription-guide)
