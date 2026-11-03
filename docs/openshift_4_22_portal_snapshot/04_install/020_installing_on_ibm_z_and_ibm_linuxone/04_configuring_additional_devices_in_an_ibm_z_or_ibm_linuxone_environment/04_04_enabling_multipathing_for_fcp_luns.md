# 4.4. Enabling multipathing for FCP LUNs

After installation, you can enable multipathing for Fibre Channel Protocol (FCP) logical unit numbers (LUNs) on IBM Z® or IBM® LinuxONE nodes. This configuration persists across node restarts, but you must redo the steps if you replace the node. 

Important

On IBM Z® and IBM® LinuxONE, you can enable multipathing only if you configured your cluster for it during installation. For more information, see "Installing RHCOS and starting the OpenShift Container Platform bootstrap process" in _Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE_. 

**Prerequisites**

  * You are logged in to the cluster as a user with administrative privileges. 
  * You have configured multiple paths to a LUN with either method explained above. 



**Procedure**

  1. Connect to the node via SSH by running the following command: 

```shell-session
$ ssh <user>@<node_ip_address>
```


You can also start a debug session to the node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  2. To enable multipathing, run the following command: 

```shell-session
$ sudo /sbin/mpathconf --enable
```


  3. To start the `multipathd` daemon, run the following command: 

```shell-session
$ sudo multipath
```


  4. Optional: To format your multipath device with fdisk, run the following command: 

```shell-session
$ sudo fdisk /dev/mapper/mpatha
```


**Verification**

  * To verify that the devices have been grouped, run the following command: 

```shell-session
$ sudo multipath -ll
```


For example: 

```shell-session
mpatha (20017380030290197) dm-1 IBM,2810XIV
   size=512G features='1 queue_if_no_path' hwhandler='1 alua' wp=rw
	-+- policy='service-time 0' prio=50 status=enabled
 	|- 1:0:0:6  sde 68:16  active ready running
 	|- 1:0:1:6  sdf 69:24  active ready running
 	|- 0:0:0:6  sdg  8:80  active ready running
 	`- 0:0:1:6  sdh 66:48  active ready running
```


**Additional resources**

  * [Install and configure the Local Storage Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-local-volume)
  * [Observing and updating the node network state and configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/kubernetes_nmstate/#k8s-nmstate-updating-node-network-config)
