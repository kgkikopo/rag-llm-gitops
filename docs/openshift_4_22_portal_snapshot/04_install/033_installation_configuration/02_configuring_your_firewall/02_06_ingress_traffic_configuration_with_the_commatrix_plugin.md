# 2.6. Ingress traffic configuration with the commatrix plugin

You can use the `commatrix` plugin to generate `nftables` rules that configure the firewall on cluster nodes to permit only the ingress traffic defined in the communication matrix. 

`nftables` is the packet filtering framework in the Linux kernel that replaces `iptables`. OpenShift Container Platform cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) use `nftables` for packet filtering. The `commatrix` plugin generates `nftables` rules and packages them as `MachineConfig` resources that the Machine Config Operator applies to your nodes. 

When you generate firewall rules with the `commatrix` plugin in Butane format, the plugin also generates a `NodeDisruptionPolicy` patch. This patch enables the Machine Config Operator to apply `nftables` rule updates without triggering a full node reboot, minimizing disruption to running workloads. 

Important

When operators or components are installed, enabled, uninstalled, or disabled, you must regenerate the firewall rules to reflect the new configuration. Failure to regenerate and apply firewall rules in this scenario might have the following consequences: 

  * Unnecessary ports might remain open, which increases the attack surface of your cluster. 
  * Services might fail to function correctly if required ports remain blocked by outdated firewall rules. 



**Additional resources**

  * [Minimizing node disruption with MachineConfig changes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-config-node-disruption)
