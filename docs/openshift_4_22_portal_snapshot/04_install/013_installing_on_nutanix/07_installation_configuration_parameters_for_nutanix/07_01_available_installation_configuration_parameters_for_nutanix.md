# 7.1. Available installation configuration parameters for Nutanix

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file. 

The following tables specify the required, optional, and Nutanix-specific installation configuration parameters that you can set as part of the installation process. 

Important

After installation, you cannot change these parameters in the `install-config.yaml` file. 

## 7.1.1. Required configuration parameters

Required installation configuration parameters are described in the following table: 

Table 7.1. Required parametersParameter| Description  
---|---  
`apiVersion:` |  The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String   
`baseDomain:` |  The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`.   
`metadata:` |  Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object   
`metadata: name:` |  The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`.  **Value:** String of lowercase letters and hyphens (`-`), such as `dev`.   
`platform:` |  The configuration for the specific platform upon which to perform the installation: `aws`, `baremetal`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`. For additional information about `platform.<platform>` parameters, consult the table for your specific platform that follows.  **Value:** Object   
`pullSecret:` |  Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:** `{ "auths":{ "cloud.openshift.com":{ "auth":"b3Blb=", "email":"you@example.com" }, "quay.io":{ "auth":"b3Blb=", "email":"you@example.com" } } }`  
Show more

## 7.1.2. Network configuration parameters

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults. 

Only IPv4 addresses are supported. 

Table 7.2. Network parametersParameter| Description  
---|---  
`networking:` |  The configuration for the cluster network.  **Value:** Object  Note You cannot change parameters specified by the `networking` object after installation.   
`networking: networkType:` |  The Red Hat OpenShift Networking network plugin to install.  **Value:**`OVNKubernetes`. `OVNKubernetes` is a Container Network Interface (CNI) plugin for Linux networks and hybrid networks that contain both Linux and Windows servers. The default value is `OVNKubernetes`.   
`networking: clusterNetwork:` |  The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  `networking: clusterNetwork: - cidr: 10.128.0.0/14 hostPrefix: 23`  
`networking: clusterNetwork: cidr:` |  Required if you use `networking.clusterNetwork`. An IP address block.  An IPv4 network.   
`networking: clusterNetwork: hostPrefix:` |  The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  The default value is `23`.   
`networking: serviceNetwork:` |  The IP address block for services. The default value is `172.30.0.0/16`.  **Value:** An array with an IP address block in CIDR format. For example:  `networking: serviceNetwork: - 172.30.0.0/16`  
`networking: machineNetwork:` |  The IP address blocks for machines.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  `networking: machineNetwork: - cidr: 10.0.0.0/16`  
`networking: machineNetwork: cidr:` |  Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  **Value:** An IP network block in CIDR notation.  For example, `10.0.0.0/16`.  Note Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction: 

  * If the installation program creates the VPC, do not specify an IPv6 entry in `networking.machineNetwork`. The installation program will assign an IPv6 address to the VPC. 
  * If you provide existing dual-stack subnets using the `platform.aws.vpc.subnets` parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets. 
  * In both cases, you must provide an IPv4 CIDR entry. 

  
`networking: ovnKubernetesConfig: ipv4: internalJoinSubnet:` |  Configures the IPv4 join subnet that is used internally by `ovn-kubernetes`. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.  **Value:** An IP network block in CIDR notation. The default value is `100.64.0.0/16`.   
Show more

## 7.1.3. Optional configuration parameters

Optional installation configuration parameters are described in the following table: 

Table 7.3. Optional parametersParameter| Description  
---|---  
`additionalTrustBundle:` |  A PEM-encoded X.509 certificate bundle that is added to the nodes' trusted certificate store. This trust bundle might also be used when a proxy has been configured.  **Value:** String   
`capabilities:` |  Controls the installation of optional core cluster components. You can reduce the footprint of your OpenShift Container Platform cluster by disabling optional components. For more information, see the "Cluster capabilities" page in _Installing_.  **Value:** String array   
`capabilities: baselineCapabilitySet:` |  Selects an initial set of optional capabilities to enable. Valid values are `None`, `v4.11`, `v4.12` and `vCurrent`. The default value is `vCurrent`.  **Value:** String   
`capabilities: additionalEnabledCapabilities:` |  Extends the set of optional capabilities beyond what you specify in `baselineCapabilitySet`. You can specify multiple capabilities in this parameter.  **Value:** String array   
`cpuPartitioningMode:` |  Enables workload partitioning, which isolates OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved set of CPUs. You can only enable workload partitioning during installation. You cannot disable it after installation. While this field enables workload partitioning, it does not configure workloads to use specific CPUs. For more information, see the _Workload partitioning_ page in the _Scalability and Performance_ section.  **Value:** `None` or `AllNodes`. `None` is the default value.   
`compute:` |  The configuration for the machines that comprise the compute nodes.  **Value:** Array of `MachinePool` objects.   
`compute: architecture:` |  Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64` (the default).  **Value:** String   
`compute: hyperthreading:` |  Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled`  
`compute: name:` |  Required if you use `compute`. The name of the machine pool.  **Value:** `worker`  
`compute: platform:` |  Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`  
`compute: replicas:` |  The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`.   
`featureSet:` |  Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`.   
`controlPlane:` |  The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects.   
`controlPlane: architecture:` |  Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64` (the default).  **Value:** String   
`controlPlane: hyperthreading:` |  Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on control plane machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled`  
`controlPlane: name:` |  Required if you use `controlPlane`. The name of the machine pool.  **Value:** `master`  
`controlPlane: platform:` |  Required if you use `controlPlane`. Use this parameter to specify the cloud provider that hosts the control plane machines. This parameter value must match the `compute.platform` parameter value.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`  
`controlPlane: replicas:` |  The number of control plane machines to provision.  **Value:** Supported values are `3`, or `1` when deploying single-node OpenShift.   
`arbiter: name:` |  The OpenShift Container Platform cluster requires a name for arbiter nodes. For example, `arbiter`.   
`arbiter: replicas:` |  The `replicas` parameter sets the number of arbiter nodes for the OpenShift Container Platform cluster. You cannot set this field to a value that is greater than 1.   
`credentialsMode:` |  The Cloud Credential Operator (CCO) mode. If no mode is specified, the CCO dynamically tries to determine the capabilities of the provided credentials, with a preference for mint mode on the platforms where multiple modes are supported.  Note Not all CCO modes are supported for all cloud providers. For more information about CCO modes, see the "Managing cloud provider credentials" entry in the _Authentication and authorization_ content.  **Value:** `Mint`, `Passthrough`, `Manual` or an empty string (`""`).   
`fips:` |  Enable or disable FIPS mode. The default is `false` (disabled). If you enable FIPS mode, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that RHCOS provides instead.  Important To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).  When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.  Important If you are using Azure File storage, you cannot enable FIPS mode.  **Value:** `false` or `true`  
`endpoint: name: <endpoint_name> clusterUseOnly: `true` or `false`` |  The `name` parameter contains the name of the Private Service Connect (PSC) endpoints.  Important When `clusterUseOnly` is `false`, its default setting, you must run the installation program from a bastion host that is within the same VPC where you want to deploy the cluster.  When you want the installation program to use the public API endpoints and cluster Operators to use the API endpoint overrides, set `clusterUseOnly` to `true`. When you want both the installation program and the cluster Operators to use the API endpoint overrides, for example if you are running the installation program from a bastion host that is within the same VPC where you want to deploy the cluster, set `clusterUseOnly` to `false` . The parameter is optional and defaults to `false`.  **Value:** String or boolean   
`imageContentSources:` |  Sources and repositories for the release-image content.  **Value:** Array of objects. Includes a `source` and, optionally, `mirrors`, as described in the following rows of this table.   
`imageContentSources: source:` |  Required if you use `imageContentSources`. Specify the repository that users refer to, for example, in image pull specifications.  **Value:** String   
`imageContentSources: mirrors:` |  Specify one or more repositories that might also contain the same images.  **Value:** Array of strings   
`osImageStream:` |  Specifies the image stream that will be used for all machines in the cluster. `osImageStream` is a Technology Preview feature. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.  **Value:** String. Valid values are `rhel-9` or `rhel-10`.   
`publish:` |  How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.  **Value:**`Internal` or `External`. The default value is `External`.  Setting this field to `Internal` is not supported on non-cloud platforms.   
`sshKey:` |  The SSH key to authenticate access to your cluster machines.  Note For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.  **Value:** For example, `sshKey: ssh-ed25519 AAAA..`.   
Show more

## 7.1.4. Additional Nutanix configuration parameters

Additional Nutanix configuration parameters are described in the following table: 

Table 7.4. Additional Nutanix cluster parametersParameter| Description  
---|---  
`compute: platform: nutanix: categories: key:` |  The name of a prism category key to apply to compute VMs. This parameter must be accompanied by the `value` parameter, and both `key` and `value` parameters must exist in Prism Central. For more information on categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html).  **Value:** String   
`compute: platform: nutanix: categories: value:` |  The value of a prism category key-value pair to apply to compute VMs. This parameter must be accompanied by the `key` parameter, and both `key` and `value` parameters must exist in Prism Central.  **Value:** String   
`compute: platform: nutanix: failureDomains:` |  The failure domains that apply to only compute machines.  Failure domains are specified in `platform.nutanix.failureDomains`.  **Value:** List.  The name of one or more failures domains.   
`compute: platform: nutanix: gpus: type:` |  The type of identifier used to attach a GPU to a compute machine. Valid values are "Name" or "DeviceID".  **Value:** String   
`compute: platform: nutanix: gpus: name:` |  The name of the GPU device to attach to a compute machine. This parameter is required if the GPU `type` is "Name".  **Value:** String   
`compute: platform: nutanix: gpus: deviceID:` |  The device identifier of the GPU device to attach to a compute machine. This information is available in Prism Central. This parameter is required if the GPU `type` is "DeviceID".  **Value:** Integer   
`compute: platform: nutanix: project: type:` |  The type of identifier you use to select a project for compute VMs. Projects define logical groups of user roles for managing permissions, networks, and other parameters. For more information on projects, see [Projects Overview](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_9:ssp-app-mgmt-project-env-c.html).  **Value:** `name` or `uuid`  
`compute: platform: nutanix: project: name: or uuid:` |  The name or UUID of a project with which compute VMs are associated. This parameter must be accompanied by the `type` parameter.  **Value:** String   
`compute: platform: nutanix: bootType:` |  The boot type that the compute machines use. You must use the `Legacy` boot type in OpenShift Container Platform 4.22. For more information on boot types, see [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK).  **Value:** `Legacy`, `SecureBoot` or `UEFI`. The default is `Legacy`.   
`compute: platform: nutanix: dataDisks: dataSourceImage: name:` |  Optional. The name of the data source image for the virtual machine disk in Prism Central.  **Value:** String   
`compute: platform: nutanix: dataDisks: dataSourceImage: referenceName:` |  Optional. The reference name of the data source image in the failure domain. If you use this parameter, you must configure a matching `dataSourceImage` with the same `referenceName` in each failure domain that the compute nodes occupy. For more information about configuring failure domains, see _Configuring failure domains_ in the _Installing a cluster on Nutanix_ page.  **Value:** String   
`compute: platform: nutanix: dataDisks: dataSourceImage: uuid:` |  The UUID of the data source image in Prism Central. This value is required.  **Value:** String   
`compute: platform: nutanix: dataDisks: deviceProperties: adapterType:` |  The adapter type of the disk address. If the disk type is "Disk", valid values are "SCSI", "IDE", "PCI", "SATA" or "SPAPR". If the disk type is "CDRom", valid values are "IDE" or "SATA".  **Value:** String   
`compute: platform: nutanix: dataDisks: deviceProperties: deviceIndex:` |  The index of the disk address. Valid values are non-negative integers including `0`. The device index for disks that share the same adapter type should start at 0 and increase consecutively. The default value is `0`. For each virtual machine, the `Disk.SCSI.0` and `CDRom.IDE.0` indices are reserved. If you use the `Disk.SCSI` or `CDRom.IDE` disk and adapter types, the `deviceIndex` should start at `1`.  **Value:** Non-negative integer, including `0`.   
`compute: platform: nutanix: dataDisks: deviceProperties: deviceType:` |  The disk device type. Valid values are "Disk" and "CDRom".  **Value:** String   
`compute: platform: nutanix: dataDisks: diskSize:` |  The size of the disk to attach to the virtual machine. The minimum size is 1Gb.  **Value:** Quantity format, such as 100G or 100Gi. For more information on this format, see link:https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Format.   
`compute: platform: nutanix: dataDisks: storageConfig: diskMode:` |  The disk mode. Valid values are `Standard` or `Flash`, and the default is `Standard`.  **Value:** String   
`compute: platform: nutanix: dataDisks: storageConfig: storageContainer: name:` |  Optional. The name of the storage container object used by the virtual machine disk in Prism Central.  **Value:** String   
`compute: platform: nutanix: dataDisks: storageConfig: storageContainer: referenceName:` |  Optional. The reference name of the storage container in the failure domain. If you use this, you must configure a matching `storageContainer` with the same `referenceName` in each failure domain the compute nodes occupy. For more information about configuring failure domains, see _Configuring failure domains_ in the _Installing a cluster on Nutanix_ page.  **Value:** String   
`compute: platform: nutanix: dataDisks: storageConfig: storageContainer: uuid:` |  The UUID of the storage container in Prism Central.  **Value:** String   
`controlPlane: platform: nutanix: categories: key:` |  The name of a prism category key to apply to control plane VMs. This parameter must be accompanied by the `value` parameter, and both `key` and `value` parameters must exist in Prism Central. For more information on categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html).  **Value:** String   
`controlPlane: platform: nutanix: categories: value:` |  The value of a prism category key-value pair to apply to control plane VMs. This parameter must be accompanied by the `key` parameter, and both `key` and `value` parameters must exist in Prism Central.  **Value:** String   
`controlPlane: platform: nutanix: failureDomains:` |  The failure domains that apply to only control plane machines.  Failure domains are specified in `platform.nutanix.failureDomains`.  **Value:** List.  The name of one or more failures domains.   
`controlPlane: platform: nutanix: project: type:` |  The type of identifier you use to select a project for control plane VMs. Projects define logical groups of user roles for managing permissions, networks, and other parameters. For more information on projects, see [Projects Overview](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_9:ssp-app-mgmt-project-env-c.html).  **Value:** `name` or `uuid`  
`controlPlane: platform: nutanix: project: name: or uuid:` |  The name or UUID of a project with which control plane VMs are associated. This parameter must be accompanied by the `type` parameter.  **Value:** String   
`platform: nutanix: defaultMachinePlatform: categories: key:` |  The name of a prism category key to apply to all VMs. This parameter must be accompanied by the `value` parameter, and both `key` and `value` parameters must exist in Prism Central. For more information on categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html).  **Value:** String   
`platform: nutanix: defaultMachinePlatform: categories: value:` |  The value of a prism category key-value pair to apply to all VMs. This parameter must be accompanied by the `key` parameter, and both `key` and `value` parameters must exist in Prism Central.  **Value:** String   
`platform: nutanix: defaultMachinePlatform: failureDomains:` |  The failure domains that apply to both control plane and compute machines.  Failure domains are specified in `platform.nutanix.failureDomains`.  **Value:** List.  The name of one or more failures domains.   
`platform: nutanix: defaultMachinePlatform: project: type:` |  The type of identifier you use to select a project for all VMs. Projects define logical groups of user roles for managing permissions, networks, and other parameters. For more information on projects, see [Projects Overview](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_9:ssp-app-mgmt-project-env-c.html).  **Value:** `name` or `uuid`.   
`platform: nutanix: defaultMachinePlatform: project: name: or uuid:` |  The name or UUID of a project with which all VMs are associated. This parameter must be accompanied by the `type` parameter.  **Value:** String   
`platform: nutanix: defaultMachinePlatform: bootType:` |  The boot type for all machines. You must use the `Legacy` boot type in OpenShift Container Platform 4.22. For more information on boot types, see [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK).  **Value:** `Legacy`, `SecureBoot` or `UEFI`. The default is `Legacy`.   
`platform: nutanix: apiVIP:` |  The virtual IP (VIP) address that you configured for control plane API access.  **Value:** IP address   
`platform: nutanix: failureDomains: - name: prismElement: name: uuid: subnetUUIDs: -` |  By default, the installation program installs cluster machines to a single Prism Element instance. A maximum of 32 subnets for each failure domain (Prism Element) in an OpenShift Container Platform cluster is supported. All `subnetUUID` values must be unique. You can specify additional Prism Element instances for fault tolerance, and then apply them to: 

  * The cluster’s default machine configuration 
  * Only control plane or compute machine pools 

**Value:** A list of configured failure domains.  For more information on usage, see "Configuring a failure domain" in "Installing a cluster on Nutanix".   
`platform: nutanix: ingressVIP:` |  The virtual IP (VIP) address that you configured for cluster ingress.  **Value:** IP address   
`platform: nutanix: prismCentral: endpoint: address:` |  The Prism Central domain name or IP address.  **Value:** String   
`platform: nutanix: prismCentral: endpoint: port:` |  The port that is used to log into Prism Central.  **Value:** String   
`platform: nutanix: prismCentral: password:` |  The password for the Prism Central user name.  **Value:** String   
`platform: nutanix: preloadedOSImageName:` |  Instead of creating and uploading a RHCOS image object for each OpenShift Container Platform cluster, this parameter uses the named, preloaded RHCOS image object from the Prism Elements to which the OpenShift Container Platform cluster is deployed.  **Value:** String   
`platform: nutanix: prismCentral: username:` |  The user name that is used to log into Prism Central.  **Value:** String   
`platform: nutanix: prismElements: endpoint: address:` |  The Prism Element domain name or IP address. [1]  **Value:** String   
`platform: nutanix: prismElements: endpoint: port:` |  The port that is used to log into Prism Element.  **Value:** String   
`platform: nutanix: prismElements: uuid:` |  The universally unique identifier (UUID) for Prism Element.  **Value:** String   
`platform: nutanix: subnetUUIDs:` |  The UUID of the Prism Element network that contains the virtual IP addresses and DNS records that you configured. [2]  **Value:** String   
`platform: nutanix: clusterOSImage:` |  Optional: By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image. If Prism Central does not have internet access, you can override the default behavior by hosting the RHCOS image on any HTTP server and pointing the installation program to the image.  **Value:** An HTTP or HTTPS URL, optionally with a SHA-256 checksum. For example, http://example.com/images/rhcos-47.83.202103221318-0-nutanix.x86_64.qcow2   
Show more

  1. The `prismElements` section holds a list of Prism Elements (clusters). A Prism Element encompasses all of the Nutanix resources, for example virtual machines and subnets, that are used to host the OpenShift Container Platform cluster. 
  2. A maximum of 32 subnets for each Prism Element in an OpenShift Container Platform cluster is supported. All `subnetUUID` values must be unique.
