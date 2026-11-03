# Chapter 4. Audit logging for network security

The OVN-Kubernetes network plugin uses Open Virtual Network (OVN) access control lists (ACLs) to manage `AdminNetworkPolicy`, `BaselineAdminNetworkPolicy`, `NetworkPolicy`, and `EgressFirewall` objects. Audit logging exposes `Allow` and `Deny` ACL events for `NetworkPolicy`, `EgressFirewall` and `BaselineAdminNetworkPolicy` custom resources (CR). Logging also exposes `Allow`, `Deny`, and `Pass` ACL events for `AdminNetworkPolicy` (ANP) CR. 

Note

Audit logging is available for only the [OVN-Kubernetes network plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#about-ovn-kubernetes).

- [4.1. Audit configuration](04_01_audit_configuration.md)
- [4.2. Audit logging](04_02_audit_logging.md)
- [4.3. AdminNetworkPolicy audit logging](04_03_adminnetworkpolicy_audit_logging.md)
- [4.4. BaselineAdminNetworkPolicy audit logging](04_04_baselineadminnetworkpolicy_audit_logging.md)
- [4.5. Configure egress firewall and network policy auditing for a cluster](04_05_configure_egress_firewall_and_network_policy_auditing_for_a_cluster.md)
- [4.6. Enable egress firewall and network policy audit logging for a namespace](04_06_enable_egress_firewall_and_network_policy_audit_logging_for_a_namespace.md)
- [4.7. Disable egress firewall and network policy audit logging for a namespace](04_07_disable_egress_firewall_and_network_policy_audit_logging_for_a_namespace.md)
- [4.8. Additional resources](04_08_additional_resources.md)
