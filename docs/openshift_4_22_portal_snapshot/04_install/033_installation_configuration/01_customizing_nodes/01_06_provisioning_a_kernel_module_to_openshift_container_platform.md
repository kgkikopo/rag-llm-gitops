# 1.6. Provisioning a kernel module to OpenShift Container Platform

Depending on whether or not you must have the kernel module in place when OpenShift Container Platform cluster first boots, you can set up the kernel modules to be deployed in one of two ways. 

These two ways are listed as follows: 

  * Provision kernel modules at cluster install time (day-1): You can create the content as a `MachineConfig` object and provide it to `openshift-install` by including it with a set of manifest files. 
  * Provision kernel modules via Machine Config Operator (day-2): Deploy the kernel module software by using the Machine Config Operator (MCO) after the cluster is running. 



Regardless of the provisioning method, each node must be able to obtain the kernel packages and related software packages when a new kernel is detected. You can configure each node to obtain this content in one of the following ways: 

  * Provide RHEL entitlements to each node. 
  * Copy RHEL entitlements from the `/etc/pki/entitlement` directory on an existing RHEL host to the same location as the other files. These other files were provided when you built your Ignition config. when you build your Ignition config. 
  * Add pointers to a `yum` repository containing the kernel and other packages in the Docker file. The pointer must include new kernel packages as they are needed to match newly installed kernels. 



## 1.6.1. Provisioning kernel modules by using a MachineConfig object

Package kernel module software with a `MachineConfig` object to deliver that software to compute or control plane nodes at installation time or through the Machine Config Operator (MCO). 

**Procedure**

  1. Register a RHEL 8 system: 

```shell-session
# subscription-manager register
```


  2. Attach a subscription to the RHEL 8 system: 

```shell-session
# subscription-manager attach --auto
```


  3. Install software needed to build the software: 

```shell-session
# yum install podman make git -y
```


  4. Create a directory to host the kernel module and tooling: 

```shell-session
$ mkdir kmods; cd kmods
```


  5. Get the `kmods-via-containers` software: 

     1. Clone the `kmods-via-containers` repository: 

```shell-session
$ git clone https://github.com/kmods-via-containers/kmods-via-containers
```


     2. Clone the `kvc-simple-kmod` repository: 

```shell-session
$ git clone https://github.com/kmods-via-containers/kvc-simple-kmod
```


  6. Get your module software. In this example, `kvc-simple-kmod` is used. 
  7. Create a fakeroot directory and populate it with files that you want to deliver through Ignition, using the repositories cloned earlier: 

     1. Create the directory: 

```shell-session
$ FAKEROOT=$(mktemp -d)
```


     2. Change to the `kmod-via-containers` directory: 

```shell-session
$ cd kmods-via-containers
```


     3. Install the KVC framework instance: 

```shell-session
$ make install DESTDIR=${FAKEROOT}/usr/local CONFDIR=${FAKEROOT}/etc/
```


     4. Change to the `kvc-simple-kmod` directory: 

```shell-session
$ cd ../kvc-simple-kmod
```


     5. Create the instance: 

```shell-session
$ make install DESTDIR=${FAKEROOT}/usr/local CONFDIR=${FAKEROOT}/etc/
```


  8. Clone the fakeroot directory, replacing any symbolic links with copies of their targets, by running the following command: 

```shell-session
$ cd .. && rm -rf kmod-tree && cp -Lpr ${FAKEROOT} kmod-tree
```


  9. Create a Butane config file, `99-simple-kmod.bu`, that embeds the kernel module tree and enables the systemd service. 

Note

See "Creating machine configs with Butane" for information about Butane. 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 99-simple-kmod
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  trees:
    - local: kmod-tree
systemd:
  units:
    - name: kmods-via-containers@simple-kmod.service
      enabled: true
```


`metadata.labels.machineconfiguration.openshift.io/role`: Specifies the node role. To deploy on control plane nodes, change `worker` to `master`. To deploy on both control plane and compute nodes, perform the remainder of these instructions once for each node type. 

  10. Use Butane to generate a machine config YAML file, `99-simple-kmod.yaml`, containing the files and configuration to be delivered: 

```shell-session
$ butane 99-simple-kmod.bu --files-dir . -o 99-simple-kmod.yaml
```


  11. If the cluster is not up yet, generate manifest files and add this file to the `openshift` directory. If the cluster is already running, apply the file as follows: 

```shell-session
$ oc create -f 99-simple-kmod.yaml
```


Your nodes will start the `kmods-via-containers@simple-kmod.service` service and the kernel modules will be loaded. 

  12. To confirm that the kernel modules are loaded, list the modules by running the following command: 

```shell-session
$ lsmod | grep simple_
```


**Example output**

```shell-session
simple_procfs_kmod     16384  0
simple_kmod            16384  0
```


Note

You can log in to a node running the `oc debug node/<openshift-node>`command and then the `chroot /host` command. 




**Additional resources**

  * [kmods-via-containers (GitHub)](https://github.com/kmods-via-containers/kmods-via-containers)
