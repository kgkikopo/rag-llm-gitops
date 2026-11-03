# 5.14. About toolbox

`toolbox` is a tool that starts a container on a Red Hat Enterprise Linux CoreOS (RHCOS) system. The tool is primarily used to start a container that includes the required binaries and plugins that are needed to run commands such as `sosreport`. 

The primary purpose for a `toolbox` container is to gather diagnostic information and to provide it to Red Hat Support. However, if additional diagnostic tools are required, you can add RPM packages or run an image that is an alternative to the standard support tools image. 

## 5.14.1. Installing packages to a toolbox container

By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel9/support-tools:latest` image. This image contains the most frequently used support tools. If you need to collect node-specific data that requires a support tool that is not part of the image, you can install additional packages. 

**Prerequisites**

  * You have accessed a node with the `oc debug node/<node_name>` command. 
  * You can access your system as a user with root privileges. 



**Procedure**

  1. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths: 

```shell-session
# chroot /host
```


  2. Start the toolbox container: 

```shell-session
# toolbox
```


  3. Install the additional package, such as `wget`: 

```shell-session
# dnf install -y <package_name>
```


## 5.14.2. Starting an alternative image with toolbox

By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel9/support-tools:latest` image. 

Note

You can start an alternative image by creating a `.toolboxrc` file and specifying the image to run. However, running an older version of the `support-tools` image, such as `registry.redhat.io/rhel8/support-tools:latest`, is not supported on OpenShift Container Platform 4.22. 

**Prerequisites**

  * You have accessed a node with the `oc debug node/<node_name>` command. 
  * You can access your system as a user with root privileges. 



**Procedure**

  1. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths: 

```shell-session
# chroot /host
```


  2. Optional: If you need to use an alternative image instead of the default image, create a `.toolboxrc` file in the home directory for the root user ID, and specify the image metadata: 

```plaintext
REGISTRY=quay.io
IMAGE=fedora/fedora:latest
TOOLBOX_NAME=toolbox-fedora-latest
```


where: 

`REGISTRY=quay.io`
     Optional: Specify an alternative container registry. 
`IMAGE=fedora/fedora:latest`
     Specify an alternative image to start. 
`TOOLBOX_NAME=toolbox-fedora-latest`
     Optional: Specify an alternative name for the toolbox container. 

  3. Start a toolbox container by entering the following command: 

```shell-session
# toolbox
```


Note

If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start…​`. To avoid issues with `sosreport` plugins, remove the running toolbox container with `podman rm toolbox-` and then spawn a new toolbox container.
