# 5.4. Obtaining the installation program

Before you install OpenShift Container Platform, download the installation file on the host you are using for installation, so that installation assets exist for deployment in your environment. 

**Prerequisites**

  * You have a computer that runs Linux or macOS, with 500 MB of local disk space. 



**Procedure**

  1. Go to the [Cluster Type](https://console.redhat.com/openshift/install) page on the Red Hat Hybrid Cloud Console. If you have a Red Hat account, log in with your credentials. If you do not, create an account. 

Tip

You can also [download the binaries for a specific OpenShift Container Platform release](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/). 

  2. Select your infrastructure provider from the **Run it yourself** section of the page. 
  3. Select your host operating system and architecture from the dropdown menus under **OpenShift Installer** and click **Download Installer**. 
  4. Place the downloaded file in the directory where you want to store the installation configuration files. 

Important

     * The installation program creates several files on the computer that you use to install your cluster. You must keep the installation program and the files that the installation program creates after you finish installing the cluster. Both of the files are required to delete the cluster. 
     * Deleting the files created by the installation program does not remove your cluster, even if the cluster failed during installation. To remove your cluster, complete the OpenShift Container Platform uninstallation procedures for your specific cloud provider. 

  5. Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ tar -xvf openshift-install-linux.tar.gz
```


  6. Download your installation [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components. 

Tip

Alternatively, you can retrieve the installation program from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/290/), where you can specify a version of the installation program to download. However, you must have an active subscription to access this page.
