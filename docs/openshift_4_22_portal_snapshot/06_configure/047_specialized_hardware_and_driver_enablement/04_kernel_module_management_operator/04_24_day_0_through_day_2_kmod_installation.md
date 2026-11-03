# 4.24. Day 0 through Day 2 kmod installation

You can install some kernel modules (kmods) during Day 0 through Day 2 operations without Kernel Module Management (KMM). You can use these stages to plan kmod transitions to KMM. 

Use the following criteria to determine suitable kmod installations. 

Day 0
    

The most basic kmods that are required for a node to become `Ready` in the cluster. Examples of these types of kmods include: 

  * A storage driver that is required to mount the rootFS as part of the boot process 
  * A network driver that is required for the machine to access `machine-config-server` on the bootstrap node to pull the ignition and join the cluster 



Day 1
    

Kmods that are not required for a node to become `Ready` in the cluster but cannot be unloaded when the node is `Ready`. 

An example of this type of kmod is an out-of-tree (OOT) network driver that replaces an outdated in-tree driver to exploit the full potential of the NIC while `NetworkManager` depends on it. When the node is `Ready`, you cannot unload the driver because of the `NetworkManager` dependency. 

Day 2
    

Kmods that can be dynamically loaded to the kernel or removed from it without interfering with the cluster infrastructure, for example, connectivity. 

Examples of these types of kmods include: 

  * GPU operators 
  * Secondary network adapters 
  * field-programmable gate arrays (FPGAs) 



## 4.24.1. Layering background

Layering applies Day 0 kernel modules through the Machine Config Operator (MCO) on OpenShift Container Platform, so cluster upgrades do not trigger node upgrades for those modules. You recompile the driver only when you add new features, because the node operating system stays the same. 

## 4.24.2. Lifecycle management

KMM lifecycle management on OpenShift Container Platform lets you upgrade kmods from Day 0 through Day 2 without rebooting nodes when the driver supports it. 

Note

This will not work if the upgrade requires a node reboot, for example, when rebuilding `initramfs` files is needed. 

Use one of the following options for lifecycle management. 

### 4.24.2.1. Treat the kmod as an in-tree driver

Use this method when you want to upgrade the kmods. In this case, treat the kmod as an in-tree driver and create a `Module` in the cluster with the `inTreeRemoval` field to unload the old version of the driver. 

Note the following characteristics of treating the kmod as an in-tree driver: 

  * Downtime might occur as KMM tries to unload and load the kmod on all the selected nodes simultaneously. 
  * This works if removing the driver makes the node lose connectivity because KMM uses a single pod to unload and load the driver. 



### 4.24.2.2. Use ordered upgrade

You can use ordered upgrade (ordered_upgrade.md) to create a versioned `Module` in the cluster representing the kmods with no effect, because the kmods are already loaded. 

Note the following characteristics of using ordered upgrade: 

  * There is no cluster downtime because you control the pace of the upgrade and how many nodes are upgraded at the same time; therefore, an upgrade with no downtime is possible. 
  * This method will not work if unloading the driver results in losing connection to the node, because KMM creates two different worker pods for unloading and another for loading. These pods will not be scheduled.
