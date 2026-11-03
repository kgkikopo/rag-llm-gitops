# 9.6. RHEL KVM on IBM Z host recommendations

To optimize Kernel-based Virtual Machine (KVM) performance on IBM Z, apply host recommendations. 

Optimizing a KVM virtual server environment strongly depends on the workloads of the virtual servers and on the available resources. The same action that enhances performance in one environment can have adverse effects in another. Finding the best balance for a particular setting can be a challenge and often involves experimentation. 

The following sections introduces some best practices when using OpenShift Container Platform with RHEL KVM on IBM Z® and IBM® LinuxONE environments. 

## 9.6.1. Use I/O threads for your virtual block devices

To make virtual block devices use I/O threads, you must configure one or more I/O threads for the virtual server and each virtual block device to use one of these I/O threads. 

The following example specifies `<iothreads>3</iothreads>` to configure three I/O threads, with consecutive decimal thread IDs 1, 2, and 3. The `iothread="2"` parameter specifies the driver element of the disk device to use the I/O thread with ID 2. 

**Sample I/O thread specification**

```plaintext
...
<domain>
 	<iothreads>3</iothreads>
  	 ...
    	<devices>
       ...
          <disk type="block" device="disk">
<driver ... iothread="2"/>
    </disk>
       ...
    	</devices>
   ...
</domain>
```


where: 

`iothreads`
     Specifies the number of I/O threads. 
`disk`
     Specifies the driver element of the disk device. 

Threads can increase the performance of I/O operations for disk devices, but they also use memory and CPU resources. You can configure multiple devices to use the same thread. The best mapping of threads to devices depends on the available resources and the workload. 

Start with a small number of I/O threads. Often, a single I/O thread for all disk devices is sufficient. Do not configure more threads than the number of virtual CPUs, and do not configure idle threads. 

You can use the `virsh iothreadadd` command to add I/O threads with specific thread IDs to a running virtual server. 

## 9.6.2. Avoid virtual SCSI devices

Configure virtual SCSI devices only if you need to address the device through SCSI-specific interfaces. Configure disk space as virtual block devices rather than virtual SCSI devices, regardless of the backing on the host. 

However, you might need SCSI-specific interfaces for: 

  * A logical unit number (LUN) for a SCSI-attached tape drive on the host. 
  * A DVD ISO file on the host file system that is mounted on a virtual DVD drive. 



## 9.6.3. Configure guest caching for disk

To ensure that the guest manages caching instead of the host, configure your disk devices. 

Ensure that the driver element of the disk device includes the `cache="none"` and `io="native"` parameters. 

**Example configuration**

```plaintext
<disk type="block" device="disk">
    <driver name="qemu" type="raw" cache="none" io="native" iothread="1"/>
...
</disk>
```


## 9.6.4. Exclude the memory balloon device

Unless you need a dynamic memory size, do not define a memory balloon device and ensure that libvirt does not create one for you. Include the `memballoon` parameter as a child of the devices element in your domain configuration file. 

**Procedure**

  * To disable the memory balloon driver, add the following configuration setting to your domain configuration file: 

```plaintext
<memballoon model="none"/>
```


## 9.6.5. Tune the CPU migration algorithm of the host scheduler

You can tune the CPU migration algorithm of the host scheduler to meet the demands of your production system. 

Important

Do not change the scheduler settings unless you are an expert who understands the implications. Do not apply changes to production systems without testing them and confirming that they have the intended effect. 

The `kernel.sched_migration_cost_ns` parameter specifies a time interval in nanoseconds. After the last execution of a task, the CPU cache is considered to have useful content until this interval expires. Increasing this interval results in fewer task migrations. The default value is `500000` ns. 

If the CPU idle time is higher than expected when there are runnable processes, try reducing this interval. If tasks bounce between CPUs or nodes too often, try increasing it. 

**Procedure**

  * To dynamically set the interval to `60000` ns, enter the following command: 

```shell-session
# sysctl kernel.sched_migration_cost_ns=60000
```


  * To persistently change the value to `60000` ns, add the following entry to `/etc/sysctl.conf`: 

```plaintext
kernel.sched_migration_cost_ns=60000
```


## 9.6.6. Disable the cpuset cgroup controller

You can disable the cpuset cgroup controller. Disabling the controller requires a restart of the libvirtd daemon. 

Note

This setting applies only to KVM hosts with cgroups version 1. To enable CPU hotplug on the host, disable the cgroup controller. 

**Procedure**

  1. Open `/etc/libvirt/qemu.conf` with an editor of your choice. 
  2. Go to the `cgroup_controllers` line. 
  3. Duplicate the entire line and remove the leading number sign (#) from the copy. 
  4. Remove the `cpuset` entry, as follows: 

```plaintext
cgroup_controllers = [ "cpu", "devices", "memory", "blkio", "cpuacct" ]
```


  5. For the new setting to take effect, you must restart the libvirtd daemon: 

     1. Stop all virtual machines. 
     2. Run the following command: 

```shell-session
# systemctl restart libvirtd
```


     3. Restart the virtual machines. 

This setting persists across host reboots. 




## 9.6.7. Tune the polling period for idle virtual CPUs

When a virtual CPU becomes idle, KVM polls for wakeup conditions for the virtual CPU before allocating the host resource. You can specify the time interval, during which polling takes place in sysfs at `/sys/module/kvm/parameters/halt_poll_ns`. 

During the specified time, polling reduces the wakeup latency for the virtual CPU at the expense of resource usage. Depending on the workload, a longer or shorter time for polling can be beneficial. The time interval is specified in nanoseconds. The default is `50000` ns. 

**Procedure**

  * To optimize for low CPU consumption, enter a small value or write `0` to disable polling: 

```shell-session
# echo 0 > /sys/module/kvm/parameters/halt_poll_ns
```


  * To optimize for low latency, for example for transactional workloads, enter a large value: 

```shell-session
# echo 80000 > /sys/module/kvm/parameters/halt_poll_ns
```


**Additional resources**

  * [Linux on IBM Z® Performance Tuning for KVM](https://www.ibm.com/docs/en/linux-on-systems?topic=v-kvm)
  * [Getting started with virtualization on IBM Z®](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_virtualization/getting-started-with-virtualization-in-rhel-8-on-ibm-z_configuring-and-managing-virtualization)
