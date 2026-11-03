# 8.3. Preparing your mirror host

Before you begin mirroring images, you must prepare the host to retrieve content and push it to the remote location. 

## 8.3.1. Install the OpenShift CLI on Linux

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


## 8.3.2. Install the OpenShift CLI on Windows

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


## 8.3.3. Install the OpenShift CLI on macOS

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
