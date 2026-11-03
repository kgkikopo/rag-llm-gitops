# 10.1. Available installation configuration parameters for IBM Cloud

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file. 

The following tables specify the required, optional, and IBM Cloud-specific installation configuration parameters that you can set as part of the installation process. 

Important

After installation, you cannot change these parameters in the `install-config.yaml` file. 

## 10.1.1. Required configuration parameters

Required installation configuration parameters are described in the following table: 

Table 10.1. Required parametersParameter| Description  
---|---  
`apiVersion:` |  The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String   
`baseDomain:` |  The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`.   
`metadata:` |  Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object   
`metadata: name:` |  The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`.   
`platform:` |  The configuration for the specific platform upon which to perform the installation: `aws`, `baremetal`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`. For additional information about `platform.<platform>` parameters, consult the table for your specific platform that follows.  **Value:** Object   
`pullSecret:` |  Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:** `{ "auths":{ "cloud.openshift.com":{ "auth":"b3Blb=", "email":"you@example.com" }, "quay.io":{ "auth":"b3Blb=", "email":"you@example.com" } } }`  
Show more

## 10.1.2. Network configuration parameters

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults. 

Only IPv4 addresses are supported. 

Table 10.2. Network parametersParameter| Description  
---|---  
`networking:` |  The configuration for the cluster network.  **Value:** Object  Note You cannot change parameters specified by the `networking` object after installation.   
`networking: networkType:` |  The Red Hat OpenShift Networking network plugin to install.  **Value:**`OVNKubernetes`. `OVNKubernetes` is a Container Network Interface (CNI) plugin for Linux networks and hybrid networks that contain both Linux and Windows servers. The default value is `OVNKubernetes`.   
`networking: clusterNetwork:` |  The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  `networking: clusterNetwork: - cidr: 10.128.0.0/14 hostPrefix: 23`  
`networking: clusterNetwork: cidr:` |  Required if you use `networking.clusterNetwork`. An IP address block.  An IPv4 network.   
`networking: clusterNetwork: hostPrefix:` |  The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  The default value is `23`.   
`networking: serviceNetwork:` |  The IP address block for services. The default value is `172.30.0.0/16`.  **Value:** An array with an IP address block in CIDR format. For example:  `networking: serviceNetwork: - 172.30.0.0/16`  
`networking: machineNetwork:` |  The IP address blocks for machines.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  `networking: machineNetwork: - cidr: 10.0.0.0/16`  
`networking: machineNetwork: cidr:` |  Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  If you are deploying the cluster to an existing Virtual Private Cloud (VPC), the CIDR must contain the subnets defined in `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`.  **Value:** An IP network block in CIDR notation.  For example, `10.0.0.0/16`.  Note Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction: 

  * If the installation program creates the VPC, do not specify an IPv6 entry in `networking.machineNetwork`. The installation program will assign an IPv6 address to the VPC. 
  * If you provide existing dual-stack subnets using the `platform.aws.vpc.subnets` parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets. 
  * In both cases, you must provide an IPv4 CIDR entry. 

  
`networking: ovnKubernetesConfig: ipv4: internalJoinSubnet:` |  Configures the IPv4 join subnet that is used internally by `ovn-kubernetes`. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.  **Value:** An IP network block in CIDR notation. The default value is `100.64.0.0/16`.   
Show more

## 10.1.3. Optional configuration parameters

Optional installation configuration parameters are described in the following table: 

Table 10.3. Optional parametersParameter| Description  
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
`publish:` |  How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.  **Value:**`Internal` or `External`. To deploy a private cluster that cannot be accessed from the internet, set the `publish` parameter to `Internal`. The default value is `External`.   
`sshKey:` |  The SSH key to authenticate access to your cluster machines.  Note For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.  **Value:** For example, `sshKey: ssh-ed25519 AAAA..`.   
Show more

## 10.1.4. Additional IBM Cloud configuration parameters

Additional IBM Cloud® configuration parameters are described in the following table: 

Table 10.4. Additional IBM Cloud(R) parametersParameter| Description  
---|---  
`controlPlane: platform: ibmcloud: bootVolume: encryptionKey:` |  An IBM® Key Protect for IBM Cloud® (Key Protect) root key that should be used to encrypt the root (boot) volume of only control plane machines.  **Value:** The Cloud Resource Name (CRN) of the root key.  The CRN must be enclosed in quotes ("").   
`compute: platform: ibmcloud: bootVolume: encryptionKey:` |  A Key Protect root key that should be used to encrypt the root (boot) volume of only compute machines.  **Value:** The CRN of the root key.  The CRN must be enclosed in quotes ("").   
`platform: ibmcloud: defaultMachinePlatform: bootvolume: encryptionKey:` |  A Key Protect root key that should be used to encrypt the root (boot) volume of all of the cluster’s machines.  When specified as part of the default machine configuration, all managed storage classes are updated with this key. Data volumes that are provisioned after the installation are also encrypted using this key.  **Value:** The CRN of the root key.  The CRN must be enclosed in quotes ("").   
`platform: ibmcloud: resourceGroupName:` |  The name of an existing resource group. By default, an installer-provisioned VPC and cluster resources are created and placed in this resource group. The installation program creates the resource group for the cluster if you do not specify these parameters.  If you are deploying the cluster into an existing VPC, the installation-program-provisioned cluster resources are placed in this resource group. The installation program creates the resource group for the cluster if you do not specify these parameters. The VPC resources that you have provisioned must exist in a resource group that you specify using the `networkResourceGroupName` parameter.  In either case, this resource group must only be used for a single cluster installation, as the cluster components assume ownership of all of the resources in the resource group. [1]  **Value:** String, for example `existing_resource_group`.   
`platform: ibmcloud: serviceEndpoints: - name: url:` |  A list of service endpoint names and URIs.  By default, the installation program and cluster components use public service endpoints to access the required IBM Cloud® services.  If network restrictions limit access to public service endpoints, you can specify an alternate service endpoint to override the default behavior.  You can specify only one alternate service endpoint for each of the following services: 

  * Cloud Object Storage 
  * DNS Services 
  * Global Search 
  * Global Tagging 
  * Identity Services 
  * Key Protect 
  * Resource Controller 
  * Resource Manager 
  * VPC 

**Value:** A valid service endpoint name and fully qualified URI.  Valid names include: 

  * `COS`
  * `DNSServices`
  * `GlobalServices`
  * `GlobalTagging`
  * `IAM`
  * `KeyProtect`
  * `ResourceController`
  * `ResourceManager`
  * `VPC`

  
`platform: ibmcloud: networkResourceGroupName:` |  The name of an existing resource group. This resource contains the existing VPC and subnets to which the cluster is deployed. This parameter is required when deploying the cluster to a VPC that you have provisioned.  **Value:** String, for example `existing_network_resource_group`.   
`platform: ibmcloud: dedicatedHosts: profile:` |  The new dedicated host to create. If you specify a value for `platform.ibmcloud.dedicatedHosts.name`, this parameter is not required.  **Value:** Valid IBM Cloud® dedicated host profile, such as `cx2-host-152x304`. [2]   
`platform: ibmcloud: dedicatedHosts: name:` |  An existing dedicated host. If you specify a value for `platform.ibmcloud.dedicatedHosts.profile`, this parameter is not required.  **Value:** String, for example `my-dedicated-host-name`.   
`platform: ibmcloud: type:` |  The instance type for all IBM Cloud® machines.  **Value:** Valid IBM Cloud® instance type, such as `bx2-8x32`. [2]   
`platform: ibmcloud: vpcName:` |  The name of the existing VPC that you want to deploy your cluster to.  **Value:** String.   
`platform: ibmcloud: controlPlaneSubnets:` |  The name(s) of the existing subnet(s) in your VPC that you want to deploy your control plane machines to. Specify a subnet for each availability zone.  **Value:** String array   
`platform: ibmcloud: computeSubnets:` |  The name(s) of the existing subnet(s) in your VPC that you want to deploy your compute machines to. Specify a subnet for each availability zone. Subnet IDs are not supported.  **Value:** String array   
Show more

  1. Whether you define an existing resource group, or if the installation program creates one, determines how the resource group is treated when the cluster is uninstalled. If you define a resource group, the installation program removes all of the installer-provisioned resources, but leaves the resource group alone; if a resource group is created as part of the installation, the installation program removes all of the installer-provisioned resources and the resource group. 
  2. To determine which profile best meets your needs, see [Instance Profiles](https://cloud.ibm.com/docs/vpc?topic=vpc-profiles&interface=ui) in the IBM® documentation.
