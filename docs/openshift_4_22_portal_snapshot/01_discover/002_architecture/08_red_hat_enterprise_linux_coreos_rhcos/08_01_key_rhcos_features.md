# 8.1. Key RHCOS features

Before you use Red Hat Enterprise Linux CoreOS (RHCOS), understand key features so that you can use RHCOS to meet your needs. 

The following list describes key features of the RHCOS operating system: 

  * **Based on RHEL** : The underlying operating system consists primarily of RHEL components. The same quality, security, and control measures that support RHEL also support RHCOS. For example, RHCOS software is in RPM packages, and each RHCOS system starts up with a RHEL kernel and a set of services that are managed by the systemd init system. 
  * **Controlled immutability** : Although it contains RHEL components, RHCOS is designed to be managed more tightly than a default RHEL installation. Management is performed remotely from the OpenShift Container Platform cluster. When you set up your RHCOS machines, you can modify only a few system settings. This controlled immutability allows OpenShift Container Platform to store the latest state of RHCOS systems in the cluster so it is always able to create additional machines and perform updates based on the latest RHCOS configurations. 
  * **CRI-O container runtime** : Although RHCOS contains features for running the OCI- and libcontainer-formatted containers that Docker requires, it incorporates the CRI-O container engine instead of the Docker container engine. By focusing on features needed by Kubernetes platforms, such as OpenShift Container Platform, CRI-O can offer specific compatibility with different Kubernetes versions. CRI-O also offers a smaller footprint and reduced attack surface than is possible with container engines that offer a larger feature set. Currently, CRI-O is the only engine available within OpenShift Container Platform clusters. 

CRI-O can use either the `crun` or `runC` container runtime to start and manage containers. `crun` is the default. For information about how to enable `runC`, see the documentation for creating a `ContainerRuntimeConfig` CR. 

  * **Set of container tools** : For tasks such as building, copying, and otherwise managing containers, RHCOS replaces the Docker CLI tool with a compatible set of container tools. The podman CLI tool supports many container runtime features, such as running, starting, stopping, listing, and removing containers and container images. The `skopeo` CLI tool can copy, authenticate, and sign images. You can use the `crictl` CLI tool to work with containers and pods from the CRI-O container engine. While direct use of these tools in RHCOS is discouraged, you can use them for debugging purposes. 
  * **rpm-ostree upgrades** : RHCOS features transactional upgrades using the `rpm-ostree` system. Updates are delivered by means of container images and are part of the OpenShift Container Platform update process. When deployed, the container image is pulled, extracted, and written to disk, then the boot loader is modified to boot into the new version. The machine reboots into the update in a rolling manner to ensure cluster capacity is minimally impacted. 
  * **bootupd firmware and boot loader updater** : Package managers and hybrid systems such as `rpm-ostree` do not update the firmware or the boot loader. With `bootupd`, RHCOS users have access to a cross-distribution, system-agnostic update tool that manages firmware and boot updates in UEFI and legacy BIOS boot modes that run on modern architectures, such as x86_64, ppc64le, and aarch64. 

For information about how to install `bootupd`, see the documentation for _Updating the bootloader using bootupd_. 

  * **Updated through the Machine Config Operator** : In OpenShift Container Platform, the Machine Config Operator handles operating system upgrades. Instead of upgrading individual packages, as is done with `yum` upgrades, `rpm-ostree` delivers upgrades of the OS as an atomic unit. The new OS deployment is staged during upgrades and goes into effect on the next reboot. If something goes wrong with the upgrade, a single rollback and reboot returns the system to the previous state. RHCOS upgrades in OpenShift Container Platform are performed during cluster updates. 



For RHCOS systems, the layout of the `rpm-ostree` file system has the following characteristics: 

  * `/usr` is where the operating system binaries and libraries are stored and is read-only. Red Hat does not support altering this. 
  * `/etc`, `/boot`, `/var` are writable on the system but only intended to be altered by the Machine Config Operator. 
  * `/var/lib/containers` is the graph storage location for storing container images. 



## 8.1.1. How to configure RHCOS

RHCOS is designed to deploy on an OpenShift Container Platform cluster with a minimal amount of configuration input. RHCOS systems are fully managed from the OpenShift Container Platform cluster. Directly changing an RHCOS machine is discouraged. 

The basic RHCOS configuration consists of the following components: 

  * Starting with a provisioned infrastructure, such as on AWS, or provisioning the infrastructure yourself. 
  * Supplying a few pieces of information, such as credentials and cluster name, in an `install-config.yaml` file when running `openshift-install`. 



Limited direct access to RHCOS machines cluster is available for debugging purposes. However, do not directly configure RHCOS systems. Instead, if you need to add or change features on your OpenShift Container Platform nodes, consider making changes in the following ways: 

  * **Kubernetes workload objects, such as DaemonSet and Deployment** : If you need to add services or other user-level features to your cluster, consider adding them as Kubernetes workload objects. Keep features outside node configurations. This approach reduces the risk of breaking the cluster during upgrades. 
  * **Day-2 customizations** : If possible, open a cluster without making any customizations to cluster nodes and make necessary node changes after the cluster is up. Those changes are easier to track later and less likely to break updates. Creating machine configs or modifying Operator custom resources are ways of making these customizations. 
  * **Day-1 customizations** : Some customizations must be implemented when the cluster first boots. Ways exist for modifying your cluster so changes are implemented on first boot. Implement day-1 customizations through Ignition configs during `openshift-install`. Alternatively, add boot options during user-provisioned ISO installs. 



Here are examples of customizations you could do on day 1: 

  * **Kernel arguments** : If particular kernel features or tuning is needed on nodes when the cluster first boots. 
  * **Disk encryption** : If your security needs require that the root file system on the nodes is encrypted, such as with FIPS support. 
  * **Kernel modules** : If a particular hardware device, such as a network card or video card, does not have a usable module available by default in the Linux kernel. 
  * **Chronyd** : If you want to provide specific clock settings to your nodes, such as the location of time servers. 



To accomplish these tasks, you can augment the `openshift-install` process to include additional objects such as `MachineConfig` objects. Those procedures that result in creating machine configs can be passed to the Machine Config Operator after the cluster is up. 

Note

The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 

Red Hat recommends that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation. 

## 8.1.2. How to deploy RHCOS

Differences between RHCOS installations for OpenShift Container Platform are based on if you are deploying on an installer-provisioned or user-provisioned infrastructure. 

The following list describes the differences between these infrastructure types: 

  * **Installer-provisioned infrastructure** : Some cloud environments offer preconfigured infrastructures so that you can start an OpenShift Container Platform cluster with minimal configuration. For these types of installations, you can supply Ignition configs that place content on each node so it is there when the cluster first boots. 
  * **User-provisioned infrastructure** : If you are provisioning your own infrastructure, you have more flexibility in how you add content to a RHCOS node. For example, you could add kernel arguments when you boot the RHCOS ISO installer to install each system. However, in most cases where configuration is required on the operating system itself, it is best to provide that configuration through an Ignition config. 



The Ignition facility runs only when the RHCOS system is first set up. After that, Ignition configs can be supplied later using the machine config. 

## 8.1.3. Ignition

Automate RHCOS disk provisioning on first boot using Ignition. Learn how Ignition reads configuration files to automatically partition disks, format filesystems, write essential files, and create user accounts during initial setup. 

On first boot, Ignition reads its configuration from the installation media or specified location. Ignition then applies the configuration. 

Whether you are installing your cluster or adding machines to it, Ignition always performs the initial configuration of the OpenShift Container Platform cluster machines. Most of the actual system setup happens on each machine itself. For each machine, Ignition takes the RHCOS image and boots the RHCOS kernel. Options on the kernel command line identify the type of deployment and the location of the Ignition-enabled initial RAM disk (initramfs). 

To create machines by using Ignition, you need Ignition config files. The OpenShift Container Platform installation program creates the Ignition config files that you need to deploy your cluster. These files are based on the information that you provide to the installation program directly or through an `install-config.yaml` file. 

The way that Ignition configures machines is similar to how tools like `cloud-init` or Linux Anaconda Kickstart configure systems, but with the following important differences: 

  * Ignition runs from an initial RAM disk that is separate from the system you are installing to. Because of that, Ignition can repartition disks, set up file systems, and perform other changes to the machine’s permanent file system. In contrast, cloud-init runs as part of the machine init system when the system boots. This makes foundational changes like disk partitioning more difficult. With cloud-init, difficulty exists to reconfigure the boot process while you are in the middle of the node boot process. 
  * Ignition is meant to initialize systems, not change existing systems. After a machine initializes and the kernel is running from the installed system, the Machine Config Operator from the OpenShift Container Platform cluster completes all future machine configuration. 
  * Instead of completing a defined set of actions, Ignition implements a declarative configuration. Ignition checks that all partitions, files, services, and other items are in place before the new machine starts. Ignition then makes the changes, like copying files to disk that are necessary for the new machine to meet the specified configuration. 
  * After Ignition finishes configuring a machine, the kernel keeps running but discards the initial RAM disk and pivots to the installed system on disk. All of the new system services and other features start without requiring a system reboot. 
  * Because Ignition confirms that all new machines meet the declared configuration, you cannot have a partially configured machine. If a machine setup fails, the initialization process does not finish, and Ignition does not start the new machine. Your cluster never contain partially configured machines. If Ignition cannot complete, the machine is not added to the cluster. You must add a new machine instead. This behavior prevents the difficult case of debugging a machine when the results of a failed configuration task are not known until something that depended on it fails at a later date. 
  * If there is a problem with an Ignition config that causes the setup of a machine to fail, Ignition does not try to use the same config to set up another machine. For example, a failure could result from an Ignition config made up of a parent and child config that both want to create the same file. A failure in such a case would prevent that Ignition config from being used again to set up on other machines until the problem is resolved. 
  * If you have multiple Ignition config files, you get a union of that set of configs. Because Ignition is declarative, conflicts between the configs could cause Ignition to fail to set up the machine. The order of information in those files does not matter. Ignition sorts and implements each setting in ways that make the most sense. For example, if a file needs a directory several levels deep, if another file needs a directory along that path, the later file is created first. Ignition sorts and creates all files, directories, and links by depth. 
  * Ignition can start with an empty disk and set up bare-metal systems from scratch by using PXE boot. This is a capability that cloud-init cannot do. In the bare metal case, the Ignition config is injected into the boot partition so that Ignition can find it and configure the system correctly. 



The Ignition process for an RHCOS machine in an OpenShift Container Platform cluster involves the following steps: 

  * The machine gets its Ignition config file. Control plane machines get their Ignition config files from the bootstrap machine, and worker machines get Ignition config files from a control plane machine. 
  * Ignition creates disk partitions, file systems, directories, and links on the machine. It supports RAID arrays but does not support LVM volumes. 
  * Ignition mounts the root of the permanent file system to the `/sysroot` directory in the initramfs and starts working in that `/sysroot` directory. 
  * Ignition configures all defined file systems and sets them up to mount appropriately at runtime. 
  * Ignition runs systemd temporary files to populate required files in the `/var` directory. 
  * Ignition runs the Ignition config files to set up users, systemd unit files, and other configuration files. 
  * Ignition unmounts all components in the permanent system that were mounted in the initramfs. 
  * Ignition starts up the init process of the new machine, which in turn starts up all other services on the machine that run during system boot. 



At the end of this process, the machine is ready to join the cluster and does not require a reboot. 

**Additional resources**

  * [cloud-init documentation](https://cloud-init.io/)
  * [Kickstart installations](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/installation_guide/index#chap-kickstart-installations)
