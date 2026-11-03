# 5.7. Creating the RHCOS image for restricted network installations

Download the Red Hat Enterprise Linux CoreOS (RHCOS) image to install OpenShift Container Platform on a restricted network Red Hat OpenStack Platform (RHOSP) environment. 

**Prerequisites**

  * Obtain the OpenShift Container Platform installation program. For a restricted network installation, the program is on your mirror registry host. 



**Procedure**

  1. Log in to the Red Hat Customer Portal’s [Product Downloads page](https://access.redhat.com/downloads/content/290). 
  2. Under **Version** , select the most recent release of OpenShift Container Platform 4.22 for RHEL 8. 

Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. 

  3. Download the **Red Hat Enterprise Linux CoreOS (RHCOS) - OpenStack Image (QCOW)** image. 
  4. Decompress the image. 

Note

You must decompress the image before the cluster can use it. The name of the downloaded file might not contain a compression extension, like `.gz` or `.tgz`. To find out if or how the file is compressed, in a command line, enter: 

```shell-session
$ file <name_of_downloaded_file>
```


  5. Upload the image that you decompressed to a location that is accessible from the bastion server, like Glance. For example: 

```plaintext
$ openstack image create --file rhcos-44.81.202003110027-0-openstack.x86_64.qcow2 --disk-format qcow2 rhcos-${RHCOS_VERSION}
```


Important

Depending on your RHOSP environment, you might be able to upload the image in either [`.raw` or `.qcow2` formats](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/15/html/instances_and_images_guide/index). If you use Ceph, you must use the `.raw` format. 

Warning

If the installation program finds multiple images with the same name, it chooses one of them at random. To avoid this behavior, create unique names for resources in RHOSP. 

The image is now available for a restricted installation. Note the image name or location for use in OpenShift Container Platform deployment.
