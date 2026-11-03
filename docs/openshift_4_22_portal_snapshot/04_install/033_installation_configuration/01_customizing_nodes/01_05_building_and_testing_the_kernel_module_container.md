# 1.5. Building and testing the kernel module container

Before deploying kernel modules to your OpenShift Container Platform cluster, you can test the process on a separate RHEL system. 

Before testing the process, gather the source code for the kernal module, the KVC framework, and the `kmod-via-containers` software. You can then build and test a module on a RHEL system. 

**Procedure**

  1. Register a RHEL 8 system: 

```shell-session
# subscription-manager register
```


  2. Attach a subscription to the RHEL 8 system: 

```shell-session
# subscription-manager attach --auto
```


  3. Install software that is required to build the software and container: 

```shell-session
# yum install podman make git -y
```


  4. Clone the `kmod-via-containers` repository. 

     1. Create a folder for the repository: 

```shell-session
$ mkdir kmods; cd kmods
```


     2. Clone the repository: 

```shell-session
$ git clone https://github.com/kmods-via-containers/kmods-via-containers
```


  5. Install a KVC framework instance on your RHEL 8 build host to test the module. This adds a `kmods-via-container` systemd service and loads it: 

     1. Change to the `kmod-via-containers` directory: 

```shell-session
$ cd kmods-via-containers/
```


     2. Install the KVC framework instance: 

```shell-session
$ sudo make install
```


     3. Reload the systemd manager configuration: 

```shell-session
$ sudo systemctl daemon-reload
```


  6. Get the kernel module source code. The source code might be used to build a third-party module that you do not have control over, but is supplied by others. You will need content similar to the content shown in the `kvc-simple-kmod` example that can be cloned to your system as follows: 

```shell-session
$ cd .. ; git clone https://github.com/kmods-via-containers/kvc-simple-kmod
```


  7. Edit the configuration file, `simple-kmod.conf` file, in this example, and change the name of the Dockerfile to `Dockerfile.rhel`: 

     1. Change to the `kvc-simple-kmod` directory: 

```shell-session
$ cd kvc-simple-kmod
```


     2. Rename the Dockerfile: 

```shell-session
$ cat simple-kmod.conf
```


**Example Dockerfile**

```shell-session
KMOD_CONTAINER_BUILD_CONTEXT="https://github.com/kmods-via-containers/kvc-simple-kmod.git"
KMOD_CONTAINER_BUILD_FILE=Dockerfile.rhel
KMOD_SOFTWARE_VERSION=dd1a7d4
KMOD_NAMES="simple-kmod simple-procfs-kmod"
```


  8. Create an instance of `kmods-via-containers@.service` for your kernel module, `simple-kmod` in this example: 

```shell-session
$ sudo make install
```


  9. Enable the `kmods-via-containers@.service` instance: 

```shell-session
$ sudo kmods-via-containers build simple-kmod $(uname -r)
```


  10. Enable and start the systemd service: 

```shell-session
$ sudo systemctl enable kmods-via-containers@simple-kmod.service --now
```


     1. Review the service status: 

```shell-session
$ sudo systemctl status kmods-via-containers@simple-kmod.service
```


**Example output**

```shell-session
● kmods-via-containers@simple-kmod.service - Kmods Via Containers - simple-kmod
   Loaded: loaded (/etc/systemd/system/kmods-via-containers@.service;
          enabled; vendor preset: disabled)
   Active: active (exited) since Sun 2020-01-12 23:49:49 EST; 5s ago...
```


  11. To confirm that the kernel modules are loaded, use the `lsmod` command to list the modules: 

```shell-session
$ lsmod | grep simple_
```


**Example output**

```shell-session
simple_procfs_kmod     16384  0
simple_kmod            16384  0
```


  12. Optional. Use other methods to check that the `simple-kmod` example is working. 

     * Look for a "Hello world" message in the kernel ring buffer with `dmesg`: 

```shell-session
$ dmesg | grep 'Hello world'
```


**Example output**

```shell-session
[ 6420.761332] Hello world from simple_kmod.
```


     * Check the value of `simple-procfs-kmod` in `/proc`: 

```shell-session
$ sudo cat /proc/simple-procfs-kmod
```


**Example output**

```shell-session
simple-procfs-kmod number = 0
```


     * Run the `spkut` command to get more information from the module: 

```shell-session
$ sudo spkut 44
```


**Example output**

```shell-session
KVC: wrapper simple-kmod for 4.22.0-147.3.1.el8_1.x86_64
Running userspace wrapper using the kernel module container...
+ podman run -i --rm --privileged
   simple-kmod-dd1a7d4:4.22.0-147.3.1.el8_1.x86_64 spkut 44
simple-procfs-kmod number = 0
simple-procfs-kmod number = 44
```


**Results**

After the system boots, the service checks if a new kernel is running. If there is a new kernel, the service builds a new version of the kernel module and then loads it. If the module is already built, it will just load it.
