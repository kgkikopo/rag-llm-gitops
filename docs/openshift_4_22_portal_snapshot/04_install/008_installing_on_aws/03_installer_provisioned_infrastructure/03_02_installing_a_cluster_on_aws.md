# 3.2. Installing a cluster on AWS

In OpenShift Container Platform version 4.22, you can install a cluster on Amazon Web Services (AWS) that uses the default configuration options. 

## 3.2.1. Prerequisites

Before you install a cluster on Amazon Web Services (AWS) that uses the default configuration options, you must meet several prerequisites. 

The following prerequisites must be met: 

  * You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes. 
  * You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing). 
  * You [configured an AWS account](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_aws/installing-aws-account "Chapter 2. Configuring an AWS account") to host the cluster. 

Important

If you have an AWS profile stored on your computer, it must not use a temporary session token that you generated while using a multi-factor authentication device. The cluster continues to use your current AWS credentials to create AWS resources for the entire life of the cluster, so you must use key-based, long-term credentials. To generate appropriate keys, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the AWS documentation. You can supply the keys when you run the installation program. 

  * If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to. 



## 3.2.2. Deploying the cluster

To deploy your OpenShift Container Platform cluster, you initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions the required infrastructure and completes the cluster setup. 

Important

You can run the `create cluster` command of the installation program only once, during initial installation. 

**Prerequisites**

  * You have configured an account with the cloud platform that hosts your cluster. 
  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 
  * You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions. 



**Procedure**

  1. In the directory that contains the installation program, initialize the cluster deployment by running the following command: 

```shell-session
$ ./openshift-install create cluster --dir <installation_directory> \
    --log-level=info
```


where: 

     * `<installation_directory>`: Specifies the directory name to store the files that the installation program creates. 
     * `--log-level`: Specifies the log level. To view different installation details, specify `warn`, `debug`, or `error` instead of `info`. 

When specifying the directory: * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory. * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

  2. Provide values at the prompts: 

     1. Optional: Select an SSH key to use to access your cluster machines. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

     2. Select **aws** as the platform to target. 
     3. If you do not have an Amazon Web Services (AWS) profile stored on your computer, enter the AWS access key ID and secret access key for the user that you configured to run the installation program. 

Note

The AWS access key ID and secret access key are stored in `~/.aws/credentials` in the home directory of the current user on the installation host. You are prompted for the credentials by the installation program if the credentials for the exported profile are not present in the file. Any credentials that you provide to the installation program are stored in the file. 

     4. Select the AWS region to deploy the cluster to. 
     5. Select the base domain for the Route 53 service that you configured for your cluster. 
     6. Enter a descriptive name for your cluster. 
     7. Paste the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). 

  3. Optional: Remove or disable the `AdministratorAccess` policy from the IAM account that you used to install the cluster. 

Note

The elevated permissions provided by the `AdministratorAccess` policy are required only during installation. 




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




**Additional resources**

  * [Configuration and credential file settings (AWS documentation)](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)



## 3.2.3. Logging in to the cluster by using the CLI

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



## 3.2.4. Logging in to the cluster by using the web console

To verify that your cluster deployed successfully and access its features, log in to the OpenShift Container Platform web console as the `kubeadmin` user. 

**Prerequisites**

  * You have access to the installation host. 
  * You completed a cluster installation and all cluster Operators are available. 



**Procedure**

  1. Obtain the password for the `kubeadmin` user from the `kubeadmin-password` file on the installation host: 

```shell-session
$ cat <installation_directory>/auth/kubeadmin-password
```


Note

Or, you can obtain the `kubeadmin` password from the `<installation_directory>/.openshift_install.log` log file on the installation host. 

  2. List the OpenShift Container Platform web console route: 

```shell-session
$ oc get routes -n openshift-console | grep 'console-openshift'
```


Note

Or, you can obtain the OpenShift Container Platform route from the `<installation_directory>/.openshift_install.log` log file on the installation host. 

**Example output**

```shell-session
console     console-openshift-console.apps.<cluster_name>.<base_domain>            console     https   reencrypt/Redirect   None
```


  3. Navigate to the route detailed in the output of the preceding command in a web browser and log in as the `kubeadmin` user. 



## 3.2.5. Additional resources

  * [Accessing the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#web-console)
  * [Validating an installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/validation_and_troubleshooting/#validating-an-installation)
  * [Available cluster customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations)
  * [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting)
  * [Removing cloud provider credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#manually-removing-cloud-creds_changing-cloud-credentials-configuration)
