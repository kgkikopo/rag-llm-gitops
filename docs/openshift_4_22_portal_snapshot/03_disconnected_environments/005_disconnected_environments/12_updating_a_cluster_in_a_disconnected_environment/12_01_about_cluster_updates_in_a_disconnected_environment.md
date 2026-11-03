# 12.1. About cluster updates in a disconnected environment

You can update a OpenShift Container Platform cluster in a disconnected environment where the cluster nodes cannot access the internet or where you want to manage update recommendations and release images locally for policy or performance purposes. 

## 12.1.1. Mirroring OpenShift Container Platform images

You can mirror OpenShift Container Platform images to a local container image registry to provide your disconnected cluster with the resources necessary for targeted updates. A single container image registry is sufficient to host mirrored images for several clusters in the disconnected network. 

For more information about mirroring images onto a repository in your disconnected cluster, see the "Mirroring OpenShift Container Platform images" section. 

**Additional resources**

  * [Mirroring OpenShift Container Platform images](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/updating-a-cluster-in-a-disconnected-environment#mirroring-ocp-image-repository "12.2. Mirroring OpenShift Container Platform images")



## 12.1.2. Performing a cluster update in a disconnected environment

You can keep your disconnected OpenShift Container Platform environment up to date by performing a cluster update. This process can be managed locally either with or without the OpenShift Update Service (OSUS). 

For more information about performing a cluster update in a disconnected environment with OSUS, see the "Updating a cluster in a disconnected environment using the OpenShift Update Service" section. 

For more information about performing a cluster update in a disconnected environment without OSUS, see the "Updating a cluster in a disconnected environment without the OpenShift Update Service" section. 

**Additional resources**

  * [Updating a cluster in a disconnected environment using the OpenShift Update Service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/updating-a-cluster-in-a-disconnected-environment#updating-disconnected-cluster-osus "12.3. Updating a cluster in a disconnected environment using the OpenShift Update Service")
  * [Updating a cluster in a disconnected environment without the OpenShift Update Service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/updating-a-cluster-in-a-disconnected-environment#updating-disconnected-cluster "12.4. Updating a cluster in a disconnected environment without the OpenShift Update Service")



## 12.1.3. Uninstall the OpenShift Update Service from a cluster

You can uninstall a local copy of the OpenShift Update Service (OSUS) from your OpenShift Container Platform cluster when you no longer need to manage updates locally: 

For more information about uninstalling the OpenShift Update Service from a cluster, see the "Uninstalling the OpenShift Update Service from a cluster" section. 

**Additional resources**

  * [Uninstalling the OpenShift Update Service from a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/updating-a-cluster-in-a-disconnected-environment#uninstalling-osus "12.5. Uninstalling the OpenShift Update Service from a cluster")
