# 8.12. Deploying the cluster

To deploy your OpenShift Container Platform cluster, you initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions the required infrastructure and completes the cluster setup. 

Important

You can run the `create cluster` command of the installation program only once, during initial installation. 

**Prerequisites**

  * You have configured an account with the cloud platform that hosts your cluster. 
  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 

If the Red Hat Enterprise Linux CoreOS (RHCOS) image is available locally, the host running the installation program does not require internet access. 

  * You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions. 



**Procedure**

  1. Export the `OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE` variable to specify the location of the Red Hat Enterprise Linux CoreOS (RHCOS) image by running the following command: 

```shell-session
$ export OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE="<path_to_image>/rhcos-<image_version>-ibmcloud.x86_64.qcow2.gz"
```


  2. In the directory that contains the installation program, initialize the cluster deployment by running the following command: 

```shell-session
$ ./openshift-install create cluster --dir <installation_directory> \
    --log-level=info
```


where: 

     * `<installation_directory>`: Specifies the location of your customized `./install-config.yaml` file. 
     * `--log-level`: Specifies the log level. To view different installation details, specify `warn`, `debug`, or `error` instead of `info`. 




**Verification**

When the cluster deployment completes successfully: 

  * The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user. 
  * Credential information also outputs to `<installation_directory>/.openshift_install.log`. 

Important

Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster. 

The following example shows the expected output: 

```shell-session
...
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
INFO Login to the console with user: "kubeadmin", and password: "password"
INFO Time elapsed: 36m22s
```


Important

    * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 
    * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
