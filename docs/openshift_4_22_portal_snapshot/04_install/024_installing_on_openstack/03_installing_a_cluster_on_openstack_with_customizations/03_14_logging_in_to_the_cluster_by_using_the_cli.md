# 3.14. Logging in to the cluster by using the CLI

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation. 

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation. 

**Prerequisites**

  * You deployed an OpenShift Container Platform cluster. 
  * You installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Export the `kubeadmin` credentials by running the following command: 

```shell-session
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
```


where: 

`<installation_directory>`
     Specifies the path to the directory that stores the installation files. 

  2. Verify you can run `oc` commands successfully using the exported configuration by running the following command: 

```shell-session
$ oc whoami
```


**Example output**

```shell-session
system:admin
```


**Next steps**

  * "Customize your cluster" 
  * "Remote health reporting" 



**Additional resources**

  * [Accessing the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#web-console)
