# 5.8. Install the OpenShift CLI on macOS

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
