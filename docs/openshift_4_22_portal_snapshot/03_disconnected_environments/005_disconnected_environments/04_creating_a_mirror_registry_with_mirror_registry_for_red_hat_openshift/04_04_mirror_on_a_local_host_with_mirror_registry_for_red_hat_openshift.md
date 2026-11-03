# 4.4. Mirror on a local host with mirror registry for Red Hat OpenShift

You can install the _mirror registry for Red Hat OpenShift_ on a local host by using the `mirror-registry` installer tool. By doing so, users can create a local host registry running on port 443 for the purpose of storing a mirror of OpenShift Container Platform images. 

Note

Installing the _mirror registry for Red Hat OpenShift_ using the `mirror-registry` CLI tool makes several changes to your machine. After installation, a `$HOME/quay-install` directory is created, which has installation files, local storage, and the configuration bundle. Trusted SSH keys are generated in case the deployment target is the local host, and systemd files on the host machine are set up to ensure that container runtimes are persistent. Additionally, an initial user named `init` is created with an automatically generated password. All access credentials are printed at the end of the install routine. 

**Procedure**

  1. Download the `mirror-registry.tar.gz` package for the latest version of the _mirror registry for Red Hat OpenShift_ found on the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page. 
  2. Install the _mirror registry for Red Hat OpenShift_ on your local host with your current user account by using the `mirror-registry` tool. For a full list of available flags, see "mirror registry for Red Hat OpenShift flags". 

```shell-session
$ ./mirror-registry install \
  --quayHostname <host_example_com> \
  --quayRoot <example_directory_name>
```


  3. Use the username and password generated during installation to log in to the registry by running the following command: 

```shell-session
$ podman login -u init \
  -p <password> \
  <host_example_com>:8443> \
  --tls-verify=false
```


You can avoid running `--tls-verify=false` by configuring your system to trust the generated rootCA certificates. See "Securing Red Hat Quay" and "Configuring the system to trust the certificate authority" for more information. 

Note

You can also log in by accessing the UI at `https://<host.example.com>:8443` after installation. 

  4. You can mirror OpenShift Container Platform images after logging in. Depending on your needs, see either the "Mirroring the OpenShift Container Platform image repository" or the "Mirroring Operator catalogs for use with disconnected clusters" sections of this document. 

Note

If there are issues with images stored by the _mirror registry for Red Hat OpenShift_ due to storage layer problems, you can re-mirror the OpenShift Container Platform images, or reinstall mirror registry on more stable storage.
