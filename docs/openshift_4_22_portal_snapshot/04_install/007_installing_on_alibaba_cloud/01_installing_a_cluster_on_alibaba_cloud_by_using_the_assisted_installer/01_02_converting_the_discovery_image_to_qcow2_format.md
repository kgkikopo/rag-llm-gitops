# 1.2. Converting the discovery image to QCOW2 format

Convert the generated ISO to `QCOW2` format before importing it into Alibaba Cloud. 

**Prerequisites**

  * You have created a cluster and downloaded the discovery image in the Assisted Installer. 
  * You have access to a Linux machine that is outside the cluster, such as your desktop machine. 



**Procedure**

  1. Open the command-line interface on the Linux machine. 
  2. Verify that the system has virtualization flags enabled by running the following command: 

```shell-session
$ grep -e lm -e svm -e vmx /proc/cpuinfo
```


  3. Install the `qemu-img` package on a RHEL or Fedora machine by running the following command: 

```shell-session
$ sudo dnf install -y qemu-img
```


Note

If your system uses the `APT` package manager, install the package using the name `qemu-utils` instead. 

  4. Convert the image to `QCOW2` by running the following command: 

```shell-session
$ qemu-img convert -O qcow2 ${CLUSTER_NAME}.iso ${CLUSTER_NAME}.qcow2
```
