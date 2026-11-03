# 1.5. Completing the installation

After the cluster is installed and initialized, the Assisted Installer indicates that the installation is finished. The Assisted Installer provides the console URL, the `kubeadmin` username and password, and the `kubeconfig` file. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Make a copy of the `kubeadmin` username and password. 
  2. Download the `kubeconfig` file and copy it to the auth directory under your working directory by running the following commands: 

```shell-session
$ mkdir -p <working_directory>/auth
```


```shell-session
$ cp kubeconfig <working_directory>/auth
```


Note

The `kubeconfig` file is available for download for 20 days after completing the installation. 

  3. Add the `kubeconfig` file to your environment by running the following command: 

```shell-session
$ export KUBECONFIG=<working_directory>/auth/kubeconfig
```


  4. Log in with the OpenShift CLI (`oc`) by running the following command: 

```shell-session
$ oc login -u kubeadmin -p <password>
```


Replace `<password>` with the password of the `kubeadmin` user. 

  5. Click the web console URL or click **Launch OpenShift Console** to open the console. 
  6. Enter the `kubeadmin` username and password. Follow the instructions in the OpenShift Container Platform console to configure an identity provider and configure alert receivers.
