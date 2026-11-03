# 3.2. Configuring the Cloud Credential Operator utility

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary. 

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment. 

**Prerequisites**

  * You have access to an OpenShift Container Platform account with cluster administrator access. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Set a variable for the OpenShift Container Platform release image by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
```


Note

Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool. 

  3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
```


For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid: 

     * `rhel8`: Specify this value for hosts that use RHEL 8. 
     * `rhel9`: Specify this value for hosts that use RHEL 9. 

Note

The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`. 

  4. Change the permissions to make `ccoctl` executable by running the following command: 

```shell-session
$ chmod 775 ccoctl
```


**Verification**

  * To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example: 

```shell-session
$ ./ccoctl
```


**Example output**

```shell-session
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
```


**Additional resources**

  * [Rotating API keys for IBM Cloud®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#refreshing-service-ids-ibm-cloud_changing-cloud-credentials-configuration)
