# 9.1. Available installation configuration parameters

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file. 

The following tables specify the required and optional installation configuration parameters that you can set as part of the Agent-based installation process. 

These values are specified in the `install-config.yaml` file. 

Important

These settings are used for installation only, and cannot be changed after installation. 

## 9.1.1. Required configuration parameters

Required installation configuration parameters are described in the following table: 

Table 9.1. Required parametersParameter| Description  
---|---  
`apiVersion:` |  The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String   
`baseDomain:` |  The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`.   
`metadata:` |  Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object   
`metadata: name:` |  The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`. The cluster name is set to `agent-cluster` when you do not provide the `metadata.name` parameter through either the `install-config.yaml` or `agent-config.yaml` files. For example, installations that only use ZTP manifests do not provide the `metadata.name` parameter.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`.   
`platform:` |  The configuration for the specific platform upon which to perform the installation: `baremetal`, `external`, `none`, `vsphere`, or `nutanix`.  **Value:** Object   
`pullSecret:` |  Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:** `{ "auths":{ "cloud.openshift.com":{ "auth":"b3Blb=", "email":"you@example.com" }, "quay.io":{ "auth":"b3Blb=", "email":"you@example.com" } } }`  
Show more

## 9.1.2. Network configuration parameters

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults. 

Consider the following information before you configure network parameters for your cluster: 

  * If you use the Red Hat OpenShift Networking OVN-Kubernetes network plugin, both IPv4 and IPv6 address families are supported. 
  * If you deployed nodes in an OpenShift Container Platform cluster with a network that supports both IPv4 and non-link-local IPv6 addresses, configure your cluster to use a dual-stack network. 

    * For clusters configured for dual-stack networking, both IPv4 and IPv6 traffic must use the same network interface as the default gateway. This ensures that in a multiple network interface controller (NIC) environment, a cluster can detect what NIC to use based on the available network interface. For more information, see "OVN-Kubernetes IPv6 and dual-stack limitations" in _About the OVN-Kubernetes network plugin_. 
    * To prevent network connectivity issues, do not install a single-stack IPv4 cluster on a host that supports dual-stack networking. 




If you configure your cluster to use both IP address families, review the following requirements: 

  * Both IP families must use the same network interface for the default gateway. 
  * Both IP families must have the default gateway. 
  * You must specify IPv4 and IPv6 addresses in the same order for all network configuration parameters. For example, in the following configuration, IPv4 addresses are listed before IPv6 addresses: 

```yaml
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  - cidr: fd00:10:128::/56
    hostPrefix: 64
  serviceNetwork:
  - 172.30.0.0/16
  - fd00:172:16::/112
```


If you are installing your cluster on AWS, the order of address families must match the `platform.aws.ipFamily` parameter. For example, if you specified the `DualStackIPv6Primary` parameter, you must list the IPv6 address first. 




Table 9.2. Network parametersParameter| Description  
---|---  
`networking:` |  The configuration for the cluster network.  **Value:** Object  Note You cannot change parameters specified by the `networking` object after installation.   
`networking: networkType:` |  The Red Hat OpenShift Networking network plugin to install.  **Value:**`OVNKubernetes`. `OVNKubernetes` is a Container Network Interface (CNI) plugin for Linux networks and hybrid networks that contain both Linux and Windows servers. The default value is `OVNKubernetes`.   
`networking: clusterNetwork:` |  The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  `networking: clusterNetwork: - cidr: 10.128.0.0/14 hostPrefix: 23 - cidr: fd01::/48 hostPrefix: 64`  
`networking: clusterNetwork: cidr:` |  Required if you use `networking.clusterNetwork`. An IP address block.  If you use the OVN-Kubernetes network plugin, you can specify IPv4 and IPv6 networks.  **Value:** An IP address block in Classless Inter-Domain Routing (CIDR) notation. The prefix length for an IPv4 block is between `0` and `32`. The prefix length for an IPv6 block is between `0` and `128`. For example, `10.128.0.0/14` or `fd01::/48`.   
`networking: clusterNetwork: hostPrefix:` |  The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  For an IPv4 network the default value is `23`. For an IPv6 network `hostPrefix` must be set to `64`, which is the default value.   
`networking: serviceNetwork:` |  The IP address block for services. The default value is `172.30.0.0/16`.  If you use the OVN-Kubernetes network plugin, you can specify an IP address block for both of the IPv4 and IPv6 address families.  **Value:** An array with an IP address block in CIDR format. For example:  `networking: serviceNetwork: - 172.30.0.0/16 - fd02::/112`  
`networking: machineNetwork:` |  The IP address blocks for machines.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  `networking: machineNetwork: - cidr: 10.0.0.0/16`  
`networking: machineNetwork: cidr:` |  Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  **Value:** An IP network block in CIDR notation.  For example, `10.0.0.0/16` or `fd00::/48`.  Note Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction: 

  * If the installation program creates the VPC, do not specify an IPv6 entry in `networking.machineNetwork`. The installation program will assign an IPv6 address to the VPC. 
  * If you provide existing dual-stack subnets using the `platform.aws.vpc.subnets` parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets. 
  * In both cases, you must provide an IPv4 CIDR entry. 

  
`networking: ovnKubernetesConfig: ipv4: internalJoinSubnet:` |  Configures the IPv4 join subnet that is used internally by `ovn-kubernetes`. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.  **Value:** An IP network block in CIDR notation. The default value is `100.64.0.0/16`.   
Show more

## 9.1.3. Optional configuration parameters

Optional installation configuration parameters are described in the following table: 

Table 9.3. Optional parametersParameter| Description  
---|---  
`additionalTrustBundle:` |  A PEM-encoded X.509 certificate bundle that is added to the nodes' trusted certificate store. This trust bundle might also be used when a proxy has been configured.  **Value:** String   
`capabilities:` |  Controls the installation of optional core cluster components. You can reduce the footprint of your OpenShift Container Platform cluster by disabling optional components. For more information, see the "Cluster capabilities" page in _Installing_.  **Value:** String array   
`capabilities: baselineCapabilitySet:` |  Selects an initial set of optional capabilities to enable. Valid values are `None`, `v4.11`, `v4.12` and `vCurrent`. The default value is `vCurrent`.  **Value:** String   
`capabilities: additionalEnabledCapabilities:` |  Extends the set of optional capabilities beyond what you specify in `baselineCapabilitySet`. You can specify multiple capabilities in this parameter.  **Value:** String array   
`cpuPartitioningMode:` |  Enables workload partitioning, which isolates OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved set of CPUs. You can only enable workload partitioning during installation. You cannot disable it after installation. While this field enables workload partitioning, it does not configure workloads to use specific CPUs. For more information, see the _Workload partitioning_ page in the _Scalability and Performance_ section.  **Value:** `None` or `AllNodes`. `None` is the default value.   
`compute:` |  The configuration for the machines that comprise the compute nodes.  **Value:** Array of `MachinePool` objects.   
`compute: architecture:` |  Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.  **Value:** String   
`compute: hyperthreading:` |  Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled`  
`compute: name:` |  Required if you use `compute`. The name of the machine pool.  **Value:** `worker`  
`compute: platform:` |  Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  **Value:**`baremetal`, `vsphere`, or `{}`  
`compute: replicas:` |  The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`.   
`featureSet:` |  Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`.   
`controlPlane:` |  The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects.   
`controlPlane: architecture:` |  Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.  **Value:** String   
`controlPlane: hyperthreading:` |  Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on control plane machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled`  
`controlPlane: name:` |  Required if you use `controlPlane`. The name of the machine pool.  **Value:** `master`  
`controlPlane: platform:` |  Required if you use `controlPlane`. Use this parameter to specify the cloud provider that hosts the control plane machines. This parameter value must match the `compute.platform` parameter value.  **Value:**`baremetal`, `vsphere`, or `{}`  
`controlPlane: replicas:` |  The number of control plane machines to provision.  **Value:** Supported values are `3`, `4`, `5`, or `1` when deploying single-node OpenShift.   
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

## 9.1.4. Additional bare metal configuration parameters for the Agent-based Installer

Additional bare metal installation configuration parameters for the Agent-based Installer are described in the following table: 

Note

These fields are not used during the initial provisioning of the cluster, but they are available to use once the cluster has been installed. Configuring these fields at install time eliminates the need to set them as a Day 2 operation. 

Table 9.4. Additional bare metal parametersParameter| Description  
---|---  
`platform: baremetal: clusterProvisioningIP:` |  The IP address within the cluster where the provisioning services run. Defaults to the third IP address of the provisioning subnet. For example, `172.22.0.3` or `2620:52:0:1307::3`.  **Value:** IPv4 or IPv6 address.   
`platform: baremetal: provisioningNetwork:` |  The `provisioningNetwork` configuration setting determines whether the cluster uses the provisioning network. If it does, the configuration setting also determines if the cluster manages the network.  `Managed`: Default. Set this parameter to `Managed` to fully manage the provisioning network, including DHCP, TFTP, and so on.  `Disabled`: Set this parameter to `Disabled` to disable the requirement for a provisioning network. When set to `Disabled`, you can use only virtual media based provisioning on Day 2. If `Disabled` and using power management, BMCs must be accessible from the bare-metal network. If Disabled, you must provide two IP addresses on the bare-metal network that are used for the provisioning services.  **Value:** `Managed` or `Disabled`.   
`platform: baremetal: provisioningMACAddress:` |  The MAC address within the cluster where provisioning services run.  **Value:** MAC address.   
`platform: baremetal: provisioningNetworkCIDR:` |  The CIDR for the network to use for provisioning. This option is required when not using the default address range on the provisioning network.  **Value:** Valid CIDR, for example `10.0.0.0/16`.   
`platform: baremetal: provisioningNetworkInterface:` |  The name of the network interface on nodes connected to the provisioning network. Use the `bootMACAddress` configuration setting to enable Ironic to identify the IP address of the NIC instead of using the `provisioningNetworkInterface` configuration setting to identify the name of the NIC.  **Value:** String.   
`platform: baremetal: provisioningDHCPRange:` |  Defines the IP range for nodes on the provisioning network, for example `172.22.0.10,172.22.0.254`.  **Value:** IP address range.   
`platform: baremetal: hosts:` |  Configuration for bare metal hosts.  **Value:** Array of host configuration objects.   
`platform: baremetal: hosts: name:` |  The name of the host.  **Value:** String.   
`platform: baremetal: hosts: bootMACAddress:` |  The MAC address of the NIC used for provisioning the host.  **Value:** MAC address.   
`platform: baremetal: hosts: bmc:` |  Configuration for the host to connect to the baseboard management controller (BMC).  **Value:** Dictionary of BMC configuration objects.   
`platform: baremetal: hosts: bmc: username:` |  The username for the BMC.  **Value:** String.   
`platform: baremetal: hosts: bmc: password:` |  Password for the BMC.  **Value:** String.   
`platform: baremetal: hosts: bmc: address:` |  The URL for communicating with the host’s BMC controller. The address configuration setting specifies the protocol. For example, `redfish+http://10.10.10.1:8000/redfish/v1/Systems/1234` enables Redfish. For more information, see "BMC addressing" in the "Deploying installer-provisioned clusters on bare metal" section.  **Value:** URL.   
`platform: baremetal: hosts: bmc: disableCertificateVerification:` |  `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses. The value should be `True` when using a self-signed certificate for BMC addresses.  **Value:** Boolean.   
Show more

## 9.1.5. Additional VMware vSphere configuration parameters

Additional VMware vSphere configuration parameters are described in the following table: 

Table 9.5. Additional VMware vSphere cluster parametersParameter| Description  
---|---  
`platform: vsphere:` |  Describes your account on the cloud platform that hosts your cluster. You can use the parameter to customize the platform. If you provide additional configuration settings for compute and control plane machines in the machine pool, the parameter is not required.  **Value:** A dictionary of vSphere configuration objects   
`platform: vsphere: failureDomains:` |  Establishes the relationships between a region and zone. You define a failure domain by using vCenter objects, such as a `datastore` object. A failure domain defines the vCenter location for OpenShift Container Platform cluster nodes.  **Value:** An array of failure domain configuration objects.   
`platform: vsphere: failureDomains: name:` |  The name of the failure domain.  **Value:** String   
`platform: vsphere: failureDomains: region:` |  If you define multiple failure domains for your cluster, you must attach the tag to each vCenter data center. To define a region, use a tag from the `openshift-region` tag category. For a single vSphere data center environment, you do not need to attach a tag, but you must enter an alphanumeric value, such as `datacenter`, for the parameter. If you want to base your failure domains on host groups, attach these tags to your vSphere clusters instead of your data centers.  **Value:** String   
`platform: vsphere: failureDomains: regionType:` |  Specifies the `ComputeCluster` region type to enable host groups.  **Value:** String   
`platform: vsphere: failureDomains: server:` |  Specifies the fully-qualified hostname or IP address of the VMware vCenter server, so that a client can access failure domain resources. You must apply the `server` role to the vSphere vCenter server location.  **Value:** String   
`platform: vsphere: failureDomains: zone:` |  If you define multiple failure domains for your cluster, you must attach a tag to each vCenter cluster. To define a zone, use a tag from the `openshift-zone` tag category. For a single vSphere data center environment, you do not need to attach a tag, but you must enter an alphanumeric value, such as `cluster`, for the parameter. If you want to base your failure domains on host groups, define zones that correspond to your host groups instead of your clusters. Use these tags to associate each ESXi host with its host group.  **Value:** String   
`platform: vsphere: failureDomains: zoneType:` |  Specifies the `HostGroup` zone type to enable host groups.  **Value:** String   
`platform: vsphere: failureDomains: topology: computeCluster:` |  The path to the vSphere compute cluster.  **Value:** String   
`platform: vsphere: failureDomains: topology: datacenter:` |  Lists and defines the data centers where OpenShift Container Platform virtual machines (VMs) operate. The list of data centers must match the list of data centers specified in the `vcenters` field.  **Value:** String   
`platform: vsphere: failureDomains: topology: datastore:` |  The path to the vSphere datastore that holds virtual machine files, templates, and ISO images.  Important You can specify the path of any datastore that exists in a datastore cluster. By default, Storage vMotion is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable Storage vMotion to avoid data loss issues for your OpenShift Container Platform cluster.  If you must specify VMs across multiple datastores, use a `datastore` object to specify a failure domain in your cluster’s `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".  **Value:** String   
`platform: vsphere: failureDomains: topology: folder:` |  Optional: The absolute path of an existing folder where the user creates the virtual machines, for example, `/<data_center_name>/vm/<folder_name>/<subfolder_name>`.  **Value:** String   
`platform: vsphere: failureDomains: topology: hostGroup:` |  Specifies the vSphere host group to associate with the failure domain.  **Value:** String   
`platform: vsphere: failureDomains: topology: networks:` |  Lists any network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.  **Value:** String   
`platform: vsphere: failureDomains: topology: resourcePool:` |  Optional: The absolute path of an existing resource pool where the installation program creates the virtual machines, for example, `/<data_center_name>/host/<cluster_name>/Resources/<resource_pool_name>/<optional_nested_resource_pool_name>`.  **Value:** String   
`platform: vsphere: failureDomains: topology: tagIDs:` |  Optional: Specifies the ID of the tag to be associated by the installation program. Each VM created by OpenShift Container Platform is assigned a unique tag that is specific to the cluster. The assigned tag enables the installation program to identify and remove the associated VMs when a cluster is decommissioned. You can list up to ten additional tag IDs to be attached to the VMs provisioned by the installation program. For more information about determining the tag ID, see the [vSphere Tags and Attributes documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html).  **Value:** String, for example `urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL`.   
`platform: vsphere: failureDomains: topology: template:` |  Specifies the absolute path to a pre-existing Red Hat Enterprise Linux CoreOS (RHCOS) image template or virtual machine. The installation program can use the image template or virtual machine to quickly install RHCOS on vSphere hosts. Consider using this parameter as an alternative to uploading an RHCOS image on vSphere hosts. This parameter is available for use only on installer-provisioned infrastructure.  **Value:** String   
`platform: vsphere: vcenters:` |  Configures the connection details so that services can communicate with a vCenter server.  **Value:** An array of vCenter configuration objects.   
`platform: vsphere: vcenters: datacenters:` |  Lists and defines the data centers where OpenShift Container Platform virtual machines (VMs) operate. The list of data centers must match the list of data centers specified in the `failureDomains` field.  **Value:** String   
`platform: vsphere: vcenters: password:` |  The password associated with the vSphere user.  **Value:** String   
`platform: vsphere: vcenters: port:` |  The port number used to communicate with the vCenter server.  **Value:** Integer   
`platform: vsphere: vcenters: server:` |  The fully qualified host name (FQHN) or IP address of the vCenter server.  **Value:** String   
`platform: vsphere: vcenters: user:` |  The username associated with the vSphere user.  **Value:** String   
Show more

## 9.1.6. Deprecated VMware vSphere configuration parameters

In OpenShift Container Platform 4.13, the following vSphere configuration parameters are deprecated. You can continue to use these parameters, but the installation program does not automatically specify these parameters in the `install-config.yaml` file. 

The following table lists each deprecated vSphere configuration parameter: 

Table 9.6. Deprecated VMware vSphere cluster parametersParameter| Description  
---|---  
`platform: vsphere: cluster:` |  The vCenter cluster to install the OpenShift Container Platform cluster in.  **Value:** String   
`platform: vsphere: datacenter:` |  Defines the data center where OpenShift Container Platform virtual machines (VMs) operate.  **Value:** String   
`platform: vsphere: defaultDatastore:` |  The name of the default datastore to use for provisioning volumes.  **Value:** String   
`platform: vsphere: folder:` |  Optional: The absolute path of an existing folder where the installation program creates the virtual machines. If you do not provide this value, the installation program creates a folder that is named with the infrastructure ID in the data center virtual machine folder.  **Value:** String, for example, `/<data_center_name>/vm/<folder_name>/<subfolder_name>`.   
`platform: vsphere: password:` |  The password for the vCenter user name.  **Value:** String   
`platform: vsphere: resourcePool:` |  Optional: The absolute path of an existing resource pool where the installation program creates the virtual machines. If you do not specify a value, the installation program installs the resources in the root of the cluster under `/<data_center_name>/host/<cluster_name>/Resources`.  **Value:** String, for example, `/<data_center_name>/host/<cluster_name>/Resources/<resource_pool_name>/<optional_nested_resource_pool_name>`.   
`platform: vsphere: username:` |  The user name to use to connect to the vCenter instance with. This user must have at least the roles and privileges that are required for [static or dynamic persistent volume provisioning](https://github.com/vmware-archive/vsphere-storage-for-kubernetes/blob/master/documentation/vcp-roles.md) in vSphere.  **Value:** String   
`platform: vsphere: vCenter:` |  The fully-qualified hostname or IP address of a vCenter server.  **Value:** String   
Show more

**Additional resources**

  * [BMC addressing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bmc-addressing_ipi-install-installation-workflow)
  * [Configuring regions and zones for a VMware vCenter](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#configuring-vsphere-regions-zones_installing-vsphere-installer-provisioned-customizations)
  * [Required vCenter account privileges](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installation-vsphere-installer-infra-requirements-account_ipi-vsphere-installation-reqs)
