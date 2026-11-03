# 2.6. Reinstalling the OpenShift Container Platform cluster

If you are unable to debug and resolve issues in the failed OpenShift Container Platform installation, consider installing a new OpenShift Container Platform cluster. Before starting the installation process again, you must complete thorough cleanup. 

For a user-provisioned infrastructure installation, you must manually destroy the cluster and delete all associated resources. The following procedure is for an installer-provisioned infrastructure installation. 

**Procedure**

  1. Destroy the cluster and remove all the resources associated with the cluster, including the hidden installer state files in the installation directory: 

```shell-session
$ ./openshift-install destroy cluster --dir <installation_directory>
```


Where `<installation_directory>` is the directory you specified when you ran `./openshift-install create cluster`. This directory contains the OpenShift Container Platform definition files that the installation program creates. 

  2. Before reinstalling the cluster, delete the installation directory by running a command similar to the following command: 

```shell-session
$ rm -rf <installation_directory>
```


  3. Follow the procedure for installing a new OpenShift Container Platform cluster.
