# 3.5. Deploying the cluster

To deploy your OpenShift Container Platform cluster, you initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions the required infrastructure and completes the cluster setup. 

Important

You can run the `create cluster` command of the installation program only once, during initial installation. 

**Prerequisites**

  * You have configured an account with the cloud platform that hosts your cluster. 
  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 
  * You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions. 



**Procedure**

  1. Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations: 

     * The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables 
     * The `~/.gcp/osServiceAccount.json` file 
     * The `gcloud cli` default credentials 

  2. In the directory that contains the installation program, initialize the cluster deployment by running the following command: 

```shell-session
$ ./openshift-install create cluster --dir <installation_directory> \
    --log-level=info
```


where: 

     * `<installation_directory>`: Specifies the directory name to store the files that the installation program creates. 
     * `--log-level`: Specifies the log level. To view different installation details, specify `warn`, `debug`, or `error` instead of `info`. 

When specifying the directory: * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory. * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

  3. Provide values at the prompts: 

     1. Optional: Select an SSH key to use to access your cluster machines. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

     2. Select **gcp** as the platform to target. 
     3. If you have not configured the service account key for your Google Cloud account on your host, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file. 
     4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured. 
     5. Select the region to deploy the cluster to. 
     6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster. 
     7. Enter a descriptive name for your cluster. If you provide a name that is longer than 6 characters, only the first 6 characters will be used in the infrastructure ID that is generated from the cluster name. 
     8. Paste the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). 

  4. Optional: You can reduce the number of permissions for the service account that you used to install the cluster. 

     * If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role. 
     * If you included the `Service Account Key Admin` role, you can remove it. 




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
