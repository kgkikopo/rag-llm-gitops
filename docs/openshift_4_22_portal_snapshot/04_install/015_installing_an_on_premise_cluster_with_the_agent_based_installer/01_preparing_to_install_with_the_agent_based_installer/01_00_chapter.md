# Chapter 1. Preparing to install with the Agent-based Installer

The Agent-based Installer provides the flexibility to boot your on-premise servers in any way that you choose. It combines the ease of use of the Assisted Installation service with the ability to run offline, including in air-gapped environments. 

The Agent-based Installer uses a subcommand of the OpenShift Container Platform installation program. It generates a bootable ISO image containing all of the information required to deploy an OpenShift Container Platform cluster, with an available release image. 

The configuration is in the same format as for the installer-provisioned infrastructure and user-provisioned infrastructure installation methods. The Agent-based Installer can also optionally generate or accept Zero Touch Provisioning (ZTP) custom resources. ZTP allows you to provision new edge sites with declarative configurations of bare-metal equipment. 

Note

To deploy clusters with virtualized control planes running on OpenShift Virtualization VMs, you can use KubeVirt Redfish to expose VMs as Redfish-compatible endpoints. For more information about using virtualized control planes, see "Using virtualized control planes". 

Table 1.1. Agent-based Installer supported architecturesCPU architecture| Connected installation| Disconnected installation  
---|---|---  
`64-bit x86` |  ✓  |  ✓   
`64-bit ARM` |  ✓  |  ✓   
`ppc64le` |  ✓  |  ✓   
`s390x` |  ✓  |  ✓   
Show more

**Additional resources**

  * [Understanding virtualized control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/virtualized_control_planes/#vcp-overview)

- [1.1. Understand Agent-based Installer](01_01_understand_agent_based_installer.md)
- [1.2. About FIPS compliance](01_02_about_fips_compliance.md)
- [1.3. Configure FIPS through the Agent-based Installer](01_03_configure_fips_through_the_agent_based_installer.md)
- [1.4. Host configuration](01_04_host_configuration.md)
- [1.5. About networking](01_05_about_networking.md)
- [1.6. Requirements for a cluster using the platform "none" option](01_06_requirements_for_a_cluster_using_the_platform_none_option.md)
- [1.7. About an arbiter node](01_07_about_an_arbiter_node.md)
- [1.8. Example: Bonds and VLAN interface node network configuration](01_08_example_bonds_and_vlan_interface_node_network_configuration.md)
- [1.9. Example: Bonds and SR-IOV dual-NIC node network configuration](01_09_example_bonds_and_sr_iov_dual_nic_node_network_configuration.md)
- [1.10. Sample install-config.yaml file for bare metal](01_10_sample_install_config_yaml_file_for_bare_metal.md)
- [1.11. Validation checks before agent ISO creation](01_11_validation_checks_before_agent_iso_creation.md)
- [1.12. Additional resources](01_12_additional_resources.md)
