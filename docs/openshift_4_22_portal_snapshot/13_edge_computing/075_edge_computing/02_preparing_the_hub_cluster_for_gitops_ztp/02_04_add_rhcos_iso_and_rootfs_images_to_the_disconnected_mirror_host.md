# 2.4. Add RHCOS ISO and RootFS images to the disconnected mirror host

Before you begin installing clusters in the disconnected environment with Red Hat Advanced Cluster Management (RHACM), you must first host Red Hat Enterprise Linux CoreOS (RHCOS) images for it to use. Use a disconnected mirror to host the RHCOS images. 

**Prerequisites**

  * Deploy and configure an HTTP server to host the RHCOS image resources on the network. You must be able to access the HTTP server from your computer, and from the machines that you create. 



Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. You require ISO and RootFS images to install RHCOS on the hosts. RHCOS QCOW2 images are not supported for this installation type. 

**Procedure**

  1. Log in to the mirror host. 
  2. Obtain the RHCOS ISO and RootFS images from [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/), for example: 

     1. Export the required image names and OpenShift Container Platform version as environment variables: 

```shell-session
$ export ISO_IMAGE_NAME=<iso_image_name>
```


```shell-session
$ export ROOTFS_IMAGE_NAME=<rootfs_image_name>
```


```shell-session
$ export OCP_VERSION=<ocp_version>
```


where: 

`<iso_image_name>`
     ISO image name, for example, `rhcos-4.22.1-x86_64-live.x86_64.iso`
`<rootfs_image_name>`
     RootFS image name, for example, `rhcos-4.22.1-x86_64-live-rootfs.x86_64.img`
`<ocp_version>`
     OpenShift Container Platform version, for example, `4.22.1`

     2. Download the required images: 

```shell-session
$ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/4.22/${OCP_VERSION}/${ISO_IMAGE_NAME} -O /var/www/html/${ISO_IMAGE_NAME}
```


```shell-session
$ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/4.22/${OCP_VERSION}/${ROOTFS_IMAGE_NAME} -O /var/www/html/${ROOTFS_IMAGE_NAME}
```


**Verification**

  * Verify that the images downloaded successfully and are being served on the disconnected mirror host, for example: 

```shell-session
$ wget http://$(hostname)/${ISO_IMAGE_NAME}
```


Example output: 

```shell-session
Saving to: rhcos-4.22.1-x86_64-live.x86_64.iso
rhcos-4.22.1-x86_64-live.x86_64.iso-  11%[====>    ]  10.01M  4.71MB/s
```


**Additional resources**

  * [Creating a mirror registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-creating-registry)
  * [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-installation-images)
