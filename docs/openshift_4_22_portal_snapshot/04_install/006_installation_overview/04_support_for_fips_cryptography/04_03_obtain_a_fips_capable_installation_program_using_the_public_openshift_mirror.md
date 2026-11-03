# 4.3. Obtain a FIPS-capable installation program using the public OpenShift mirror

To install a OpenShift Container Platform cluster in FIPS mode, download the FIPS-capable installation binary from the public OpenShift mirror. 

After you obtain the binary, proceed with the cluster installation, replacing all instances of the `openshift-install` binary with `openshift-install-fips`. 

**Prerequisites**

  * You have access to the internet. 



**Procedure**

  1. Download the installation program from <https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.18/openshift-install-rhel9-amd64.tar.gz>. 
  2. Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ tar -xvf openshift-install-rhel9-amd64.tar.gz
```


  3. Proceed with cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.
