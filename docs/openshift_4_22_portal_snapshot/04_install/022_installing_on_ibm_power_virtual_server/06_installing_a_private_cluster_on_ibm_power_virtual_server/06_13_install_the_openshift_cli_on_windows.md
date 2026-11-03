# 6.13. Install the OpenShift CLI on Windows

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
