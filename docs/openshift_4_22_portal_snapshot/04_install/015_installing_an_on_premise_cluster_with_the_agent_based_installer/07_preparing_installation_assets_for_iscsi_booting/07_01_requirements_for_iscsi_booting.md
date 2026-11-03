# 7.1. Requirements for iSCSI booting

Several configurations are necessary to enable iSCSI booting when using the Agent-based Installer. 

The following configurations are required: 

  * Dynamic Host Configuration Protocol (DHCP) must be configured. Static networking is not supported. 
  * You must create an additional network for iSCSI that is separate from the machine network of the cluster. The machine network is rebooted during cluster installation and cannot be used for the iSCSI session. 
  * If the host on which you are booting the agent ISO image also has an installed disk, it might be necessary to specify the iSCSI disk name in the `rootDeviceHints` parameter to ensure that it is chosen as the boot disk for the final Red Hat Enterprise Linux CoreOS (RHCOS) image. You can also use a diskless environment for iSCSI booting, in which case you do not need to set the `rootDeviceHints` parameter. 



**Additional resources**

  * [DHCP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/preparing-to-install-with-agent-based-installer#agent-install-networking-DHCP_preparing-to-install-with-agent-based-installer "1.5.2. DHCP")
  * [About root device hints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/preparing-to-install-with-agent-based-installer#root-device-hints_preparing-to-install-with-agent-based-installer "1.4.2. About root device hints")
