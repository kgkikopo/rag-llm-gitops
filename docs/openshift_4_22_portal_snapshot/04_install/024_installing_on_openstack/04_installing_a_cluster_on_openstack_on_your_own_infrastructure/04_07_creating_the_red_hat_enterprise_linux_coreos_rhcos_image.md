# 4.7. Creating the Red Hat Enterprise Linux CoreOS (RHCOS) image

The OpenShift Container Platform installation program requires that a Red Hat Enterprise Linux CoreOS (RHCOS) image be present in the Red Hat OpenStack Platform (RHOSP) cluster. Retrieve the latest RHCOS image, then upload it using the RHOSP CLI. 

**Prerequisites**

  * The RHOSP CLI is installed. 



**Procedure**

  1. Log in to the Red Hat Customer Portal’s [Product Downloads page](https://access.redhat.com/downloads/content/290). 
  2. Under **Version** , select the most recent release of OpenShift Container Platform 4.22 for Red Hat Enterprise Linux (RHEL) 8. 

Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. 

  3. Download the _Red Hat Enterprise Linux CoreOS (RHCOS) - OpenStack Image (QCOW)_. 
  4. Decompress the image. 

Note

You must decompress the RHOSP image before the cluster can use it. The name of the downloaded file might not contain a compression extension, like `.gz` or `.tgz`. To find out if or how the file is compressed, in a command line, enter: 

```shell-session
$ file <name_of_downloaded_file>
```


  5. From the image that you downloaded, create an image that is named `rhcos` in your cluster by using the RHOSP CLI: 

```shell-session
$ openstack image create --container-format=bare --disk-format=qcow2 --file rhcos-${RHCOS_VERSION}-openstack.qcow2 rhcos
```


Important

Depending on your RHOSP environment, you might be able to upload the image in either [`.raw` or `.qcow2` formats](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/15/html/instances_and_images_guide/index). If you use Ceph, you must use the `.raw` format. 

Warning

If the installation program finds multiple images with the same name, the program chooses one of them at random. To avoid this behavior, create unique names for resources in RHOSP. 

After you upload the image to RHOSP, the image is usable in the installation process.
