# 2.6. Additional installation configuration parameters

Some parameters, such as the cluster domain name, are required in the `install-config.yaml` file when installing a cluster on bare metal. Others, such as the provisioning network CIDR, are optional. 

Table 2.1. Required parametersParameters| Default| Description  
---|---|---  
`baseDomain` |  |  The domain name for the cluster. For example, `example.com`.   
`bootMode` |  `UEFI` |  The boot mode for a node. Options are `legacy`, `UEFI`, and `UEFISecureBoot`. If `bootMode` is not set, Ironic sets it while inspecting the node.  Note For hardware that implements `BootMode` read-only, such as HP or Cisco, do not leave this parameter blank. You must manually set the system to UEFI mode before installation and explicitly set this parameter to UEFI.   
`platform: baremetal: bootstrapExternalStaticDNS` |  |  The static network DNS of the bootstrap node. You must set this value when deploying a cluster with static IP addresses when there is no Dynamic Host Configuration Protocol (DHCP) server on the bare-metal network. If you do not set this value, the installation program will use the value from `bootstrapExternalStaticGateway`, which causes problems when the IP address values of the gateway and DNS are different.   
`platform: baremetal: bootstrapExternalStaticIP` |  |  The static IP address for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare metal network.   
`platform: baremetal: bootstrapExternalStaticGateway` |  |  The static IP address of the gateway for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare metal network.   
`sshKey` |  |  The `sshKey` parameter sets the key in the `~/.ssh/id_rsa.pub` file required to access the control plane nodes and compute nodes. Typically, this key is from the `provisioner` node.   
`pullSecret` |  |  The `pullSecret` parameter sets a copy of the pull secret downloaded from the [Install OpenShift on Bare Metal](https://console.redhat.com/openshift/install/metal/user-provisioned) page when preparing the provisioner node.   
`metadata: name:` |  |  The OpenShift Container Platform cluster name. For example, `openshift`.   
`networking: machineNetwork: - cidr:` |  |  The public CIDR (Classless Inter-Domain Routing) of the external network. For example, `10.0.0.0/24`.   
`compute: - name: worker` |  |  The OpenShift Container Platform cluster requires a name for each compute node even if there are zero nodes.   
`compute: replicas: 2` |  |  Replicas sets the number of compute nodes in the OpenShift Container Platform cluster.   
`controlPlane: name: master` |  |  The OpenShift Container Platform cluster requires a name for control plane nodes.   
`controlPlane: replicas: 3` |  |  Replicas sets the number of control plane nodes included as part of the OpenShift Container Platform cluster.   
`provisioningNetworkInterface` |  |  The name of the network interface on nodes connected to the provisioning network. For OpenShift Container Platform 4.9 and later releases, use the `bootMACAddress` parameter to enable Ironic to identify the IP address of the NIC instead of using the `provisioningNetworkInterface` parameter to identify the name of the NIC.   
`defaultMachinePlatform` |  |  The default configuration used for machine pools without a platform configuration.   
`apiVIPs` |  |  (Optional) The virtual IP address for Kubernetes API communication.  You must either provide this setting in the `install-config.yaml` file as a reserved IP from the `MachineNetwork` parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the `apiVIPs` configuration setting in the `install-config.yaml` file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses `api.<cluster_name>.<base_domain>` to derive the IP address from the DNS.  Note Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the `apiVIP` parameter. From OpenShift Container Platform 4.12 or later, the `apiVIP` parameter is deprecated. Instead, use a list format for the `apiVIPs` parameter to specify an IPv4 address, an IPv6 address or both IP address formats.   
`bmcCACert` |  |  `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses when using self-signed certificates with `disableCertificateVerification` set to `False`.   
`ingressVIPs` |  |  (Optional) The virtual IP address for ingress traffic.  You must either provide this setting in the `install-config.yaml` file as a reserved IP from the `MachineNetwork` parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the `ingressVIPs` configuration setting in the `install-config.yaml` file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses `test.apps.<cluster_name>.<base_domain>` to derive the IP address from the DNS.  Note Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the `ingressVIP` parameter. In OpenShift Container Platform 4.12 and later, the `ingressVIP` parameter is deprecated. Instead, use a list format for the `ingressVIPs` parameter to specify an IPv4 addresses, an IPv6 addresses or both IP address formats.   
Show more

Table 2.2. Optional ParametersParameters| Default| Description  
---|---|---  
`platform: baremetal: additionalNTPServers: - <ip_address_or_domain_name>` |  |  An optional list of additional NTP servers to add to each host. You can use an IP address or a domain name to specify each NTP server. Additional NTP servers are user-defined NTP servers that enable preinstallation clock synchronization when the cluster host clocks are out of synchronization.   
`provisioningDHCPRange` |  `172.22.0.10,172.22.0.100` |  Defines the IP range for nodes on the provisioning network.   
`provisioningNetworkCIDR` |  `172.22.0.0/24` |  The CIDR for the network to use for provisioning. When not using the default address range on the provisioning network, you must set this configuration parameter.   
`clusterProvisioningIP` |  The third IP address of the `provisioningNetworkCIDR`.  |  The IP address within the cluster where the provisioning services run. Defaults to the third IP address of the provisioning subnet. For example, `172.22.0.3`.   
`bootstrapProvisioningIP` |  The second IP address of the `provisioningNetworkCIDR`.  |  The IP address on the bootstrap VM where the provisioning services run while the installation program is deploying the control plane nodes. Defaults to the second IP address of the provisioning subnet. For example, `172.22.0.2` or `2620:52:0:1307::2`.   
`externalBridge` |  `baremetal` |  The name of the bare metal bridge of the hypervisor attached to the bare metal network.   
`provisioningBridge` |  `provisioning` |  The name of the provisioning bridge on the `provisioner` host attached to the provisioning network.   
`architecture` |  |  Defines the host architecture for your cluster. Valid values are `amd64` or `arm64`.   
`defaultMachinePlatform` |  |  The default configuration used for machine pools without a platform configuration.   
`bootstrapOSImage` |  |  A URL to override the default operating system image for the bootstrap node. The URL must contain a SHA-256 hash of the image. For example: `[https://mirror.openshift.com/rhcos-<version>-qemu.qcow2.gz?sha256=<uncompressed_sha256>](https://mirror.openshift.com/rhcos-<version>-qemu.qcow2.gz?sha256=<uncompressed_sha256>)`.   
`provisioningNetwork` |  |  The `provisioningNetwork` parameter determines whether the cluster uses the provisioning network. If it does, the parameter also determines if the cluster manages the network.  `Disabled`: Set this parameter to `Disabled` to disable the requirement for a provisioning network. When set to `Disabled`, you must only use virtual media based provisioning, or install the cluster by using the Assisted Installer. If `Disabled` and using power management, BMCs must be accessible from the bare metal network. If `Disabled`, you must provide two IP addresses on the bare metal network for the provisioning services to use.  `Managed`: Set this parameter to `Managed`, which is the default, to fully manage the provisioning network, including DHCP, TFTP, and so on.  `Unmanaged`: Set this parameter to `Unmanaged` to enable the provisioning network but take care of manual configuration of DHCP. Virtual media provisioning is recommended but PXE is still available if required.   
`httpProxy` |  |  Set this parameter to the appropriate HTTP proxy used within your environment.   
`httpsProxy` |  |  Set this parameter to the appropriate HTTPS proxy used within your environment.   
`noProxy` |  |  Set this parameter to the appropriate list of exclusions for proxy usage within your environment.   
Show more

## 2.6.1. Hosts

The `hosts` parameter is a list of separate bare metal assets used to build the cluster. 

Table 2.3. HostsName| Default| Description  
---|---|---  
`name` |  |  The name of the `BareMetalHost` resource to associate with the details. For example, `openshift-master-0`.   
`role` |  |  The role of the bare metal node. Either `master` (control plane node) or `worker` (compute node).   
`bmc` |  |  Connection details for the baseboard management controller. See the BMC addressing section for additional details.   
`bmc: address:` |  |  The protocol and address of the BMC as a URL.   
`bmc: username:` |  |  The username of the BMC.   
`bmc: password:` |  |  The password of the BMC.   
`bmc: disableCertificateVerification:` |  `False` |  `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses. For OpenShift Container Platform 4.16 and earlier, the value should be `True` when using a self-signed certificate. OpenShift Container Platform supports self-signed certificates with certificate verification when used with the `bmcVerifyCA` parameter.   
`platform: baremetal: bmcVerifyCA:` |  |  A local or self-signed CA certificate that the installation program will use to secure communication with the BMC. If you specify your own CA certificate, ensure that `disableCertificateVerification` is set to `False` so that the user-provided CA certificate is validated.   
`bootMACAddress` |  |  The MAC address of the NIC that the host uses for the provisioning network. Ironic retrieves the IP address by using the `bootMACAddress` parameter. Then, it binds to the host.  Note You must provide a valid MAC address from the host if you disabled the provisioning network.   
`networkConfig` |  |  Set this optional parameter to configure the network interface of a host. See "(Optional) Configuring host network interfaces" for additional details.   
Show more
