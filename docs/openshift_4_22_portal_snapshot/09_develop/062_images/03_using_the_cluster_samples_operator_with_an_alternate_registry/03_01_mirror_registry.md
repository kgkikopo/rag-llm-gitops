# 3.1. Mirror registry

You must have access to the internet to obtain the necessary container images. Using an alternative registry means that you place the mirror registry on a mirror host that has access to both your network and the internet. 

You can mirror the images that are required for OpenShift Container Platform installation and subsequent product updates to a container mirror registry such as Red Hat Quay, JFrog Artifactory, Sonatype Nexus Repository, or Harbor. If you do not have access to a large-scale container registry, you can use the _mirror registry for Red Hat OpenShift_ , a small-scale container registry included with OpenShift Container Platform subscriptions. 

You can use any container registry that supports Docker v2-2, such as Red Hat Quay, the _mirror registry for Red Hat OpenShift_ , Artifactory, Sonatype Nexus Repository, or Harbor. Regardless of your chosen registry, the procedure to mirror content from Red Hat hosted sites on the internet to an isolated image registry is the same. After you mirror the content, you configure each cluster to retrieve this content from your mirror registry. 

Important

The OpenShift image registry cannot be used as the target registry because it does not support pushing without a tag, which is required during the mirroring process. 

If choosing a container registry that is not the _mirror registry for Red Hat OpenShift_ , it must be reachable by every machine in the clusters that you provision. If the registry is unreachable, installation, updating, or normal operations such as workload relocation might fail. For that reason, you must run mirror registries in a highly available way, and the mirror registries must at least match the production availability of your OpenShift Container Platform clusters. 

When you populate your mirror registry with OpenShift Container Platform images, you can follow two scenarios. If you have a host that can access both the internet and your mirror registry, but not your cluster nodes, you can directly mirror the content from that machine. This process is referred to as _connected mirroring_. If you have no such host, you must mirror the images to a file system and then bring that host or removable media into your restricted environment. This process is referred to as _disconnected mirroring_. 

For mirrored registries, to view the source of pulled images, you must review the `Trying to access` log entry in the CRI-O logs. Other methods to view the image pull source, such as using the `crictl images` command on a node, show the non-mirrored image name, even though the image is pulled from the mirrored location. 

Note

Red Hat does not test third party registries with OpenShift Container Platform. 

## 3.1.1. Install the OpenShift CLI on Linux

To manage your cluster and deploy applications from the command line on Linux, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red Customer Portal. 

Important

If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform. 

Download and install the new version of `oc`. 

**Procedure**

  1. Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal. 
  2. Select the architecture from the **Product Variant** list. 
  3. Select the appropriate version from the **Version** list. 
  4. Click **Download Now** next to the **OpenShift v4.22 Linux Clients** entry and save the file. 
  5. Unpack the archive: 

```shell-session
$ tar xvf <file>
```


  6. Place the `oc` binary in a directory that is on your `PATH`. 

To check your `PATH`, run the following command: 

```shell-session
$ echo $PATH
```


**Verification**

  * After you install the OpenShift CLI, it is available using the `oc` command: 

```shell-session
$ oc <command>
```


## 3.1.2. Install the OpenShift CLI on Windows

To manage your cluster and deploy applications from the command line on Windows, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red Customer Portal. 

Important

If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform. 

Download and install the new version of `oc`. 

**Procedure**

  1. Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal. 
  2. Select the appropriate version from the **Version** list. 
  3. Click **Download Now** next to the **OpenShift v4.22 Windows Client** entry and save the file. 
  4. Extract the archive with a ZIP program. 
  5. Move the `oc` binary to a directory that is on your `PATH` variable. 

To check your `PATH` variable, open the Command Prompt and run the following command: 

```shell-session
C:\> path
```


**Verification**

  * After you install the OpenShift CLI, it is available using the `oc` command: 

```shell-session
C:\> oc <command>
```


## 3.1.3. Install the OpenShift CLI on macOS

To manage your cluster and deploy applications from the command line on macOS, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red Customer Portal. 

Important

If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform. 

Download and install the new version of `oc`. 

**Procedure**

  1. Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal. 
  2. Select the architecture from the **Product Variant** list. 
  3. Select the appropriate version from the **Version** list. 
  4. Click **Download Now** next to the **OpenShift v4.22 macOS Clients** entry and save the file. 

Note

For macOS arm64, choose the **OpenShift v4.22 macOS arm64 Client** entry. 

  5. Extract the archive. 
  6. Move the `oc` binary to a directory on your `PATH` variable. 

To check your `PATH` variable, open a terminal and run the following command: 

```shell-session
$ echo $PATH
```


**Verification**

  * Verify your installation by using an `oc` command: 

```shell-session
$ oc <command>
```
