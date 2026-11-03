# 9.1. Available installation configuration parameters for IBM Power Virtual Server

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file. 

The following tables specify the required, optional, and IBM Power Virtual Server-specific installation configuration parameters that you can set as part of the installation process. 

Important

After installation, you cannot change these parameters in the `install-config.yaml` file. 

## 9.1.1. Required configuration parameters

Required installation configuration parameters are described in the following table: 

Table 9.1. Required parametersParameter| Description  
---|---  
`apiVersion:` |  The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String   
`baseDomain:` |  The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`.   
`metadata:` |  Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object   
`metadata: name:` |  The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`.   
`platform:` |  The configuration for the specific platform upon which to perform the installation: `aws`, `baremetal`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`. For additional information about `platform.<platform>` parameters, consult the table for your specific platform that follows.  **Value:** Object   
`pullSecret:` |  Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:** `{ "auths":{ "cloud.openshift.com":{ "auth":"b3Blb=", "email":"you@example.com" }, "quay.io":{ "auth":"b3Blb=", "email":"you@example.com" } } }`  
`platform: powervs: userID:` |  The UserID is the login for the user’s IBM Cloud® account.  **Value:** String. For example, `existing_user_id`.   
`platform: powervs: powervsResourceGroup:` |  The PowerVSResourceGroup is the resource group in which IBM Power® Virtual Server resources are created. If using an existing VPC, the existing VPC and subnets should be in this resource group.  **Value:** String. For example, `existing_resource_group`.   
`platform: powervs: region:` |  Specifies the IBM Cloud® region where the cluster is created.  **Value:** String. For example, `existing_region`.   
`platform: powervs: zone:` |  Specifies the IBM Cloud® colo region where the cluster is created.  **Value:** String. For example, `existing_zone`.   
Show more

## 9.1.2. Network configuration parameters

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults. 

Only IPv4 addresses are supported. 

Table 9.2. Network parametersParameter| Description  
---|---  
`networking:` |  The configuration for the cluster network.  **Value:** Object  Note You cannot change parameters specified by the `networking` object after installation.   
`networking: networkType:` |  The Red Hat OpenShift Networking network plugin to install.  **Value:** The default value is `OVNKubernetes`.   
`networking: clusterNetwork:` |  The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  `networking: clusterNetwork: - cidr: 10.128.0.0/14 hostPrefix: 23`  
`networking: clusterNetwork: cidr:` |  Required if you use `networking.clusterNetwork`. An IP address block.  An IPv4 network.   
`networking: clusterNetwork: hostPrefix:` |  The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  The default value is `23`.   
`networking: serviceNetwork:` |  The IP address block for services. The default value is `172.30.0.0/16`.  **Value:** An array with an IP address block in CIDR format. For example:  `networking: serviceNetwork: - 172.30.0.0/16`  
`networking: machineNetwork:` |  The IP address blocks for machines.  **Value:** An array of objects. For example:  `networking: machineNetwork: - cidr: 10.0.0.0/16`  
`networking: machineNetwork: cidr:` |  Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  **Value:** An IP network block in CIDR notation.  For example, `192.168.0.0/24`.  Note Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction: 

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
`compute: architecture:` |  Determines the instruction set architecture of the machines in the pool. Currently, heterogeneous clusters are not supported, so all pools must specify the same architecture. The valid value is the default: `ppc64le`.  **Value:** String   
`compute: hyperthreading:` |  Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled`  
`compute: smtLevel:` |  The SMTLevel specifies the level of SMT to set to the control plane and compute machines. Valid values are `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `off`, and `on`.  **Value:** String   
`compute: name:` |  Required if you use `compute`. The name of the machine pool.  **Value:** `worker`  
`compute: platform:` |  Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  Example usage, `compute.platform.powervs.sysType`.   
`compute: platform: powervs: sysType:` |  Defines the system type for the instance.  **Value:** The available system types depend on the zone you want to target. Supported values are `e980`, `s922`, `e1080`, or `s1022`.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`  
`compute: replicas:` |  The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`.   
`featureSet:` |  Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`.   
`controlPlane:` |  The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects.   
`controlPlane: architecture:` |  Determines the instruction set architecture of the machines in the pool. Currently, heterogeneous clusters are not supported, so all pools must specify the same architecture. The valid value is the default: `ppc64le`.  **Value:** String   
`controlPlane: hyperthreading:` |  Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on control plane machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled`  
`controlPlane: name:` |  Required if you use `controlPlane`. The name of the machine pool.  **Value:** `master`  
`controlPlane: platform:` |  Required if you use `controlPlane`. Use this parameter to specify the cloud provider that hosts the control plane machines. This parameter value must match the `compute.platform` parameter value.  Example usage, `controlPlane.platform.powervs.processors`.   
`controlPlane: platform: powervs: sysType:` |  Defines the system type for the instance.  **Value:** The available system types depend on the zone you want to target. Supported values are `e980`, `s922`, `e1080`, or `s1022`.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`  
`controlPlane: replicas:` |  The number of control plane machines to provision.  **Value:** Supported values are `3`, or `1` when deploying single-node OpenShift.   
`arbiter: name:` |  The OpenShift Container Platform cluster requires a name for arbiter nodes. For example, `arbiter`.   
`arbiter: replicas:` |  The `replicas` parameter sets the number of arbiter nodes for the OpenShift Container Platform cluster. You cannot set this field to a value that is greater than 1.   
`credentialsMode:` |  The Cloud Credential Operator (CCO) mode. If no mode is specified, the CCO dynamically tries to determine the capabilities of the provided credentials, with a preference for mint mode on the platforms where multiple modes are supported.  Note Not all CCO modes are supported for all cloud providers. For more information about CCO modes, see the "Managing cloud provider credentials" entry in the _Authentication and authorization_ content.  **Value:** `Mint`, `Passthrough`, `Manual` or an empty string (`""`).   
`imageContentSources:` |  Sources and repositories for the release-image content.  **Value:** Array of objects. Includes a `source` and, optionally, `mirrors`, as described in the following rows of this table.   
`imageContentSources: source:` |  Required if you use `imageContentSources`. Specify the repository that users refer to, for example, in image pull specifications.  **Value:** String   
`imageContentSources: mirrors:` |  Specify one or more repositories that might also contain the same images.  **Value:** Array of strings   
`osImageStream:` |  Specifies the image stream that will be used for all machines in the cluster. `osImageStream` is a Technology Preview feature. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.  **Value:** String. Valid values are `rhel-9` or `rhel-10`.   
`publish:` |  How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.  **Value:**`Internal` or `External`. The default value is `External`.  Setting this field to `Internal` is not supported on non-cloud platforms.   
`sshKey:` |  The SSH key to authenticate access to your cluster machines.  Note For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.  **Value:** For example, `sshKey: ssh-ed25519 AAAA..`.   
`platform: powervs: vpcRegion:` |  Specifies the IBM Cloud® region in which to create VPC resources.  **Value:** String. For example, `existing_vpc_region`.   
`platform: powervs: vpcSubnets:` |  Specifies existing subnets by name where cluster resources are created.  **Value:** String. For example, `powervs_region_example_subnet`.   
`platform: powervs: vpcName:` |  Specifies the IBM Cloud® name.  **Value:** String. For example, `existing_vpcName`.   
`platform: powervs: serviceInstanceGUID:` |  Specifies the ID of the Power IAAS instance created from the IBM Cloud® Catalog.  **Value:** String. For example, `existing_service_instance_GUID`.   
`platform: powervs: clusterOSImage:` |  Specifies a pre-created IBM Power® Virtual Server boot image that overrides the default image for cluster nodes.  **Value:** String. For example, `existing_cluster_os_image`.   
`platform: powervs: defaultMachinePlatform:` |  Specifies the default configuration used when installing on IBM Power® Virtual Server for machine pools that do not define their own platform configuration.  **Value:** String. For example, `existing_machine_platform`.   
`platform: powervs: memoryGiB:` |  Specifies the size of a virtual machine’s memory, in GB.  **Value:** The valid integer must be an integer number of GB that is at least `2` and no more than `64`, depending on the machine type.   
`platform: powervs: procType:` |  Defines the processor sharing model for the instance.  **Value:** The valid values are `Capped`, `Dedicated`, and `Shared`.   
`platform: powervs: processors:` |  Defines the processing units for the instance.  **Value:** The number of processors must be from `.5` to `32` cores. The processors must be in increments of `.25`.   
`platform: powervs: tgName:` |  Defines the name of an existing Transit Gateway.  **Value:** String. For example, `existing_tgName`.   
Show more
