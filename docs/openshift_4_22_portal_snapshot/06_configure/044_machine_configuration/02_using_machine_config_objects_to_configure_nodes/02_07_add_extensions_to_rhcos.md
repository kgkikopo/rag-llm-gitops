# 2.7. Add extensions to RHCOS

You can add software packages to Red Hat Enterprise Linux CoreOS (RHCOS) systems by using extension packages to add a minimal set of features to specific nodes. 

RHCOS is a minimal container-oriented op-system-base-full operating system, designed to provide a common set of capabilities to OpenShift Container Platform clusters across all platforms. Although adding software packages to RHCOS systems is generally discouraged, you can add any of the following extensions to extend RHCOS: 

  * **usbguard** : The `usbguard` extension protects RHCOS systems from attacks by intrusive USB devices. For `usbguard`, you must create additional `MachineConfig` objects to start and enable the services as described in the following procedure. For more information, see [USBGuard](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/security_hardening/index#usbguard_protecting-systems-against-intrusive-usb-devices). 
  * **kerberos** : The `kerberos` extension provides a mechanism that allows both users and machines to identify themselves to the network to receive defined, limited access to the areas and services that an administrator has configured. For more information, see [Using Kerberos](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/using_kerberos), including how to set up a Kerberos client and mount a Kerberized NFS share. 
  * **sandboxed-containers** : The `sandboxed-containers` extension contains RPMs for Kata, QEMU, and its dependencies. For more information, see [OpenShift Sandboxed Containers](https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/latest). 
  * **ipsec** : The `ipsec` extension contains RPMs for libreswan and NetworkManager-libreswan. 
  * **wasm** : The `wasm` extension enables Developer Preview functionality in OpenShift Container Platform for users who want to use WASM-supported workloads. 
  * **sysstat** : Adding the `sysstat` extension provides additional performance monitoring for OpenShift Container Platform nodes, including the system activity reporter (`sar`) command for collecting and reporting information. 
  * **kernel-devel** : The `kernel-devel` extension provides kernel headers and makefiles sufficient to build modules against the kernel package. 



The following procedure describes how to use a machine config to add one or more extensions to your RHCOS nodes. 

**Prerequisites**

  * Have a running OpenShift Container Platform cluster (version 4.6 or later). 
  * Log in to the cluster as a user with administrative privileges. 



**Procedure**

  1. Create a Butane configuration file named `80-worker-usbguard.bu` to add the extension, manage the configuration files, and enable the service. 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 80-worker-usbguard
  labels:
    machineconfiguration.openshift.io/role: worker
extensions:
  - usbguard
storage:
  files:
    - path: /etc/usbguard/usbguard-daemon.conf
      mode: 0600
      overwrite: true
      contents:
        inline: |
          RuleFile=/etc/usbguard/rules.conf
          PresentDevicePolicy=apply-policy
          IPCAllowedGroups=wheel
    - path: /etc/usbguard/rules.conf
      mode: 0600
      overwrite: false
      contents:
        inline: |
          allow id 1d6b:0002 serial "0000:00:14.0" name "EHCI Host Controller"
systemd:
  units:
    - name: usbguard.service
      enabled: true
```


  2. Convert the Butane configuration into a `MachineConfig` manifest by entering the following command: 

```shell-session
$ butane 80-worker-usbguard.bu -o 80-worker-usbguard.yaml
```


  3. Apply the `MachineConfig` to the cluster by entering the following command: 

```shell-session
$ oc apply -f 80-worker-usbguard.yaml
```


This sets all compute nodes to install the `usbguard` RPM package, write the required configuration files, and enable the systemd daemon within a single node rollout cycle. 




**Verification**

  1. Check that the new machine config was successfully created by entering the following command: 

```shell-session
$ oc get machineconfig 80-worker-usbguard
```


**Example output**

```shell-session
NAME                GENERATEDBYCONTROLLER IGNITIONVERSION AGE
80-worker-usbguard                        3.5.0           57s
```


  2. Check that the machine config is now applied and that the nodes are not in a degraded state. This operation might take a few minutes. The worker pool will show the updates in progress, as each machine successfully has the new machine config applied: 

```shell-session
$ oc get machineconfigpool
```


**Example output**

```shell-session
NAME   CONFIG             UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE
master rendered-master-35 True    False    False    3            3                 3                   0                    34m
worker rendered-worker-d8 False   True     False    3            1                 1                   0                    34m
```


  3. After the pool reports `UPDATED` as `True`, verify that the extension package was installed and that the service is running normally by debugging a compute node. You can complete these tasks by running the following commands: 

```shell-session
$ oc get node | grep worker
```


**Example output**

```shell-session
NAME                                        STATUS  ROLES    AGE   VERSION
ip-10-0-169-2.us-east-2.compute.internal    Ready   worker   102m  v1.35.4
```


```shell-session
$ oc debug node/ip-10-0-169-2.us-east-2.compute.internal
```


**Example output**

```shell-session
...
To use host binaries, run `chroot /host`
sh-4.4# chroot /host
sh-4.4# rpm -q usbguard
usbguard-0.7.4-4.el8.x86_64.rpm
...
sh-4.4# systemctl status usbguard.service
usbguard.service - USBGuard daemon
        Loaded: loaded (/usr/lib/systemd/system/usbguard.service; enabled; preset: disabled)
        Active: active (running)
```
