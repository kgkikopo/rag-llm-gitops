# 3.1. OpenShift Container Platform installation options

The OpenShift Container Platform installation program offers four methods for deploying a cluster. Each method has unique characteristics so that you can choose a method that meets your needs. 

The following list details these methods: 

  * **Interactive** : You can deploy a cluster with the web-based Assisted Installer. This is an ideal approach for clusters with networks connected to the internet. The Assisted Installer is the easiest way to install OpenShift Container Platform. Assisted Installer provides smart defaults and performs pre-flight validations before installing the cluster. Assisted Installer also provides a RESTful API for automation and advanced configuration scenarios. 
  * **Local Agent-based** : You can deploy a cluster locally with the Agent-based Installer for disconnected environments or restricted networks. The Local Agent-based installer provides many of the benefits of the Assisted Installer, but you must download and configure the Agent-based Installer first. Configuration is done with a command-line interface. This approach is ideal for disconnected environments. 

    * Additionally, you can deploy a cluster without an external registry, using self-contained installation media that also provides a simplified user interface similar to the Assisted Installer during on-premise installations. For more information, see "Installing a cluster without an external registry". 

  * **Automated** : You can deploy a cluster on installer-provisioned infrastructure. The installation program uses each cluster host’s baseboard management controller (BMC) for provisioning. You can deploy clusters in connected or disconnected environments. 
  * **Full control** : You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters in connected or disconnected environments. 



Each method deploys a cluster with the following characteristics: 

  * Highly available infrastructure with no single points of failure, which is available by default. 
  * Administrators can control what updates are applied and when. 



**Additional resources**

  * [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform)
  * [Agent-based Installer](https://console.redhat.com/openshift/install/metal/agent-based)
  * [Installing a cluster without an external registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#installing-ove)



## 3.1.1. The installation program

You can use the installation program to deploy each type of cluster. The installation program generates the main assets, such as Ignition config files for the bootstrap, control plane, and compute machines. 

You can start an OpenShift Container Platform cluster with these three machine configurations, provided you correctly configured the infrastructure. 

The OpenShift Container Platform installation program uses a set of targets and dependencies to manage cluster installations. The installation program has a set of targets that it must achieve, and each target has a set of dependencies. Because each target is only concerned with its own dependencies, the installation program can act to achieve multiple targets in parallel with the ultimate target being a running cluster. The installation program recognizes and uses existing components instead of running commands to create them again because the program meets the dependencies. 

**Figure 3.1. OpenShift Container Platform installation targets and dependencies**

![OpenShift Container Platform installation targets and dependencies](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Architecture-en-US/images/6527feee3673861daba1c8118bcfa1b6/targets-and-dependencies.png) ![OpenShift Container Platform installation targets and dependencies](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Architecture-en-US/images/6527feee3673861daba1c8118bcfa1b6/targets-and-dependencies.png)

## 3.1.2. Red Hat Enterprise Linux CoreOS (RHCOS)

Post-installation, each cluster machine uses Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. RHCOS is the immutable container host version of Red Hat Enterprise Linux (RHEL) and features a RHEL kernel with SELinux enabled by default. 

RHCOS includes the `kubelet`, which is the Kubernetes node agent, and the CRI-O container runtime, which is optimized for Kubernetes. 

Every control plane machine in an OpenShift Container Platform 4.22 cluster must use RHCOS, which includes a critical first-boot provisioning tool called Ignition. This tool enables the cluster to configure the machines. Operating system updates are delivered as a bootable container image, using OSTree as a backend, that is deployed across the cluster by the Machine Config Operator. Actual operating system changes are made in-place on each machine as an atomic operation by using `rpm-ostree`. Together, these technologies enable OpenShift Container Platform to manage the operating system like it manages any other application on the cluster, by in-place upgrades that keep the entire platform up to date. These in-place updates can reduce the burden on operations teams. 

If you use RHCOS as the operating system for all cluster machines, the cluster manages all aspects of its components and machines, including the operating system. Because of this, only the installation program and the Machine Config Operator can change machines. The installation program uses Ignition config files to set the exact state of each machine, and the Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation. 

## 3.1.3. Supported platforms for OpenShift Container Platform clusters

Review the platform support matrix to choose the installation method that meets your requirements. 

Table 3.1. Supported platformsPlatform| Installer-provisioned infrastructure [1]| User-provisioned infrastructure [2]| Agent-based Installer| Assisted Installer  
---|---|---|---|---  
**Amazon Web Services (AWS)** |  X  |  X  |  |   
**Bare metal** |  X  |  X  |  X  |  X   
**External** |  |  |  X  |  X   
**Google Cloud** |  X  |  X  |  |   
**IBM Cloud® Classic** |  X  |  |  |   
**IBM Cloud® Virtual Private Cloud (VPC)** |  X  |  |  |   
**IBM Power®** |  |  X  |  X  |  X   
**IBM Z® or IBM® LinuxONE** |  |  X  |  X  |  X   
**Microsoft Azure** |  X  |  X  |  |   
**Microsoft Azure Stack Hub** |  X  |  X  |  |   
**None** |  |  |  X  |  X   
**Nutanix** |  X  |  |  |  X   
**Oracle Cloud Infrastructure (OCI)** |  |  |  X  |  X   
**Red Hat OpenStack Platform (RHOSP)[3]** |  X  |  X  |  |   
**VMware vSphere** |  X  |  X  |  X  |  X   
Show more

The following list describes three different deployment pathways and their prerequisites: 

  * For installer-provisioned infrastructure: All machines, including the computer that you run the installation process on, must have direct internet access to pull images for platform containers and provide telemetry data to Red Hat. 

Important

After installation, the following changes are not supported: 

    * Mixing cloud provider platforms. 
    * Mixing cloud provider components. For example, using a persistent storage framework from another platform on the platform where you installed the cluster. 

  * For user-provisioned infrastructure: Depending on the supported cases for the platform, you can perform installations on user-provisioned infrastructure so that you can run machines with full internet access, place your cluster behind a proxy, or perform a disconnected installation. 

In a disconnected installation, you can download the images that are required to install a cluster, place them in a mirror registry, and use that data to install your cluster. While you require internet access to pull images for platform containers, with a disconnected installation on vSphere or bare-metal infrastructure, your cluster machines do not require direct internet access. 

  * For Red Hat OpenStack Platform (RHOSP): The latest OpenShift Container Platform release supports both the latest RHOSP long-life release and intermediate release. For complete RHOSP release compatibility, see "OpenShift Container Platform on RHOSP support matrix". See "OpenShift Container Platform 4.x Tested Integrations" for details about integration testing for different platforms. 



**Additional resources**

  * [OpenShift Container Platform on RHOSP support matrix](https://access.redhat.com/articles/4679401)
  * [OpenShift Container Platform 4.x Tested Integrations](https://access.redhat.com/articles/4128421)



## 3.1.4. Installation process

The OpenShift Container Platform installation program transforms a set of assets into a running cluster, using an installation process that varies depending on your installation method. 

Except for the Assisted Installer, when you install an OpenShift Container Platform cluster, you must download the installation program from the appropriate **Cluster Type** page on the OpenShift Cluster Manager Hybrid Cloud Console. This console manages: 

  * REST API for accounts. 
  * Registry tokens, which are the pull secrets that you use to obtain the required components. 
  * Cluster registration, which associates the cluster identity to your Red Hat account to facilitate the gathering of usage metrics. 



In OpenShift Container Platform 4.22, the installation program is a Go binary file that performs a series of file transformations on a set of assets. The way you interact with the installation program differs depending on your installation type. Consider the following installation use cases: 

  * To deploy a cluster with the Assisted Installer, you must configure the cluster settings by using the Assisted Installer. There is no installation program to download and configure. After you finish setting the cluster configuration, you download a discovery ISO and then boot cluster machines with that image. You can install clusters with the Assisted Installer on Nutanix, vSphere, and bare metal with full integration, and other platforms without integration. If you install on bare metal, you must provide all of the cluster infrastructure and resources, including the networking, load balancing, storage, and individual cluster machines. 
  * To deploy clusters with the Agent-based Installer, you can download the Agent-based Installer first. You can then configure the cluster and generate a discovery image. You boot cluster machines with the discovery image, which installs an agent that communicates with the installation program and handles the provisioning for you instead of you interacting with the installation program or setting up a provisioner machine yourself. You must provide all of the cluster infrastructure and resources, including the networking, load balancing, storage, and individual cluster machines. This approach is ideal for disconnected environments. 
  * For clusters with installer-provisioned infrastructure, you delegate the infrastructure bootstrapping and provisioning to the installation program instead of doing it yourself. The installation program creates all of the networking, machines, and operating systems that are required to support the cluster, except if you install on bare metal. If you install on bare metal, you must provide all of the cluster infrastructure and resources, including the bootstrap machine, networking, load balancing, storage, and individual cluster machines. 
  * If you provision and manage the infrastructure for your cluster, you must provide all of the cluster infrastructure and resources, including the bootstrap machine, networking, load balancing, storage, and individual cluster machines. 



The installation program uses three sets of files during installation: an installation configuration file that is named `install-config.yaml`, Kubernetes manifests, and Ignition config files for your machine types. 

Important

You can modify Kubernetes and the Ignition config files that control the underlying RHCOS operating system during installation. However, no validation is available to confirm the suitability of any modifications that you make to these objects. If you modify these objects, you might render your cluster non-functional. Because of this risk, modifying Kubernetes and Ignition config files is not supported unless you are following documented procedures or are instructed to do so by Red Hat support. 

The installation configuration file is transformed into Kubernetes manifests, and then the manifests are wrapped into Ignition config files. The installation program uses these Ignition config files to create the cluster. 

The installation configuration files are all pruned when you run the installation program, ensure you back up all the configuration files that you want to use again. 

Important

You cannot modify the parameters that you set during installation, but you can modify many cluster attributes after installation. 

The installation process with the Assisted Installer
    

Installation with the Assisted Installer involves creating a cluster configuration interactively by using the web-based user interface or the RESTful API. The Assisted Installer user interface prompts you for required values and provides reasonable default values for the remaining parameters, unless you change them in the user interface or with the API. The Assisted Installer generates a discovery image, which you download and use to boot the cluster machines. The image installs RHCOS and an agent, and the agent handles the provisioning for you. You can install OpenShift Container Platform with the Assisted Installer and full integration on Nutanix, vSphere, and bare metal. Additionally, you can install OpenShift Container Platform with the Assisted Installer on other platforms without integration. 

OpenShift Container Platform manages all aspects of the cluster, including the operating system itself. Each machine boots with a configuration that references resources hosted in the cluster that it joins. This configuration allows the cluster to manage itself as updates are applied. 

If possible, use the Assisted Installer feature to avoid having to download and configure the Agent-based Installer. 

The installation process with Agent-based infrastructure
    

Agent-based installation is similar to using the Assisted Installer, except that you must initially download and install the Agent-based Installer. An Agent-based installation is useful when you want the convenience of the Assisted Installer, but you need to install a cluster in a disconnected environment. 

If possible, use the Agent-based installation feature to avoid having to create a provisioner machine with a bootstrap VM, and then provision and maintain the cluster infrastructure. 

The installation process with installer-provisioned infrastructure
    

The default installation type uses installer-provisioned infrastructure. By default, the installation program acts as an installation wizard, prompting you for values that it cannot determine on its own and providing reasonable default values for the remaining parameters. You can also customize the installation process to support advanced infrastructure scenarios. The installation program provisions the underlying infrastructure for the cluster. 

You can install either a standard cluster or a customized cluster. With a standard cluster, you provide minimum details that are required to install the cluster. With a customized cluster, you can specify more details about the platform, such as the number of machines that the control plane uses, the type of virtual machine that the cluster deploys, or the CIDR range for the Kubernetes service network. 

If possible, use this feature to avoid having to provision and maintain the cluster infrastructure. In all other environments, you use the installation program to generate the assets that you require to provision your cluster infrastructure. 

With installer-provisioned infrastructure clusters, OpenShift Container Platform manages all aspects of the cluster, including the operating system itself. Each machine boots with a configuration that references resources hosted in the cluster that it joins. This configuration allows the cluster to manage itself as updates are applied. 

The installation process with user-provisioned infrastructure
    

You can also install OpenShift Container Platform on infrastructure that you provide. You use the installation program to generate the assets that you require to provision the cluster infrastructure, create the cluster infrastructure, and then deploy the cluster to the infrastructure that you provided. 

If you do not use infrastructure that the installation program provisioned, you must manage and maintain the cluster resources yourself. The following list details some of these self-managed resources: 

  * The underlying infrastructure for the control plane and compute machines that make up the cluster 
  * Load balancers 
  * Cluster networking, including the DNS records and required subnets 
  * Storage for the cluster infrastructure and applications 

If your cluster uses user-provisioned infrastructure, you have the option of adding RHEL compute machines to your cluster. 




**Additional resources**

  * [Recommended etcd practices](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#recommended-etcd-practices)
  * [Control plane node sizing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#master-node-sizing_recommended-control-plane-practices)
  * [Available cluster customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations)



## 3.1.5. Installation process details

When a cluster is provisioned, each machine in the cluster requires information about the cluster. OpenShift Container Platform uses a temporary bootstrap machine during initial configuration to provide the required information to the permanent control plane. 

The temporary bootstrap machine boots by using an Ignition config file that describes how to create the cluster. The bootstrap machine creates the control plane machines that make up the control plane. The control plane machines then create the compute machines, which are also known as worker machines. The following figure illustrates this process: 

**Figure 3.2. Creating the bootstrap, control plane, and compute machines**

![Creating bootstrap](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Architecture-en-US/images/9fb14e59171a618c486862da6b1ae17b/create-nodes.png) ![Creating bootstrap](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Architecture-en-US/images/9fb14e59171a618c486862da6b1ae17b/create-nodes.png)

Important

While planning to deploy your cluster, review the recommended practices for performance and scalability, particularly the requirements for input/output (I/O) latency for etcd storage and the requirements for the recommended control plane node sizing. For more information, see “Recommended etcd practices” and “Control plane node sizing”. 

After the cluster machines initialize, the bootstrap machine is destroyed. All clusters use the bootstrap process to initialize the cluster, but if you provision the infrastructure for your cluster, you must complete many of the steps manually. 

Important

  * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 
  * Consider using Ignition config files within 12 hours after they are generated, because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation. 



Bootstrapping a cluster involves the following steps: 

  1. The bootstrap machine boots and starts hosting the remote resources required for the control plane machines to boot. If you provision the infrastructure, this step requires manual intervention. 
  2. The bootstrap machine starts a single-node etcd cluster and a temporary Kubernetes control plane. 
  3. The control plane machines fetch the remote resources from the bootstrap machine and finish booting. If you provision the infrastructure, this step requires manual intervention. 
  4. The temporary control plane schedules the production control plane to the production control plane machines. 
  5. The Cluster Version Operator (CVO) comes online and installs the etcd Operator. The etcd Operator scales up etcd on all control plane nodes. 
  6. The temporary control plane shuts down and passes control to the production control plane. 
  7. The bootstrap machine injects OpenShift Container Platform components into the production control plane. 
  8. The installation program shuts down the bootstrap machine. If you provision the infrastructure, this step requires manual intervention. 
  9. The control plane sets up the compute nodes. 
  10. The control plane installs additional services in the form of a set of Operators. 



The result of this bootstrapping process is a running OpenShift Container Platform cluster. The cluster then downloads and configures remaining components needed for the day-to-day operations, including the creation of compute machines in supported environments. 

**Additional resources**

  * [Cluster Type](https://console.redhat.com/openshift/create)
  * [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform)
  * [Agent-based Installer](https://console.redhat.com/openshift/install/metal/agent-based)
