# 2.3. Monitoring ANP and BANP

To monitor and troubleshoot `AdminNetworkPolicy` and `BaselineAdminNetworkPolicy` resources in OpenShift Container Platform, you can use OVN-Kubernetes metrics that report resource counts, rules, and northbound database objects. 

## 2.3.1. Metrics for AdminNetworkPolicy

You can use OVN-Kubernetes metrics to monitor `AdminNetworkPolicy` and `BaselineAdminNetworkPolicy` resources. These metrics report policy and rule counts by direction and action, and northbound database objects that the policies create. 

Name| Description| Explanation  
---|---|---  
`ovnkube_controller_admin_network_policies` |  Not applicable  |  The total number of `AdminNetworkPolicy` resources in the cluster.   
`ovnkube_controller_baseline_admin_network_policies` |  Not applicable  |  The total number of `BaselineAdminNetworkPolicy` resources in the cluster. The value should be 0 or 1.   
`ovnkube_controller_admin_network_policies_rules` | 

  * `direction`: specifies either `Ingress` or `Egress`. 
  * `action`: specifies either `Pass`, `Allow`, or `Deny`. 

|  The total number of rules across all ANP policies in the cluster grouped by `direction` and `action`.   
`ovnkube_controller_baseline_admin_network_policies_rules` | 

  * `direction`: specifies either `Ingress` or `Egress`. 
  * `action`: specifies either `Allow` or `Deny`. 

|  The total number of rules across all BANP policies in the cluster grouped by `direction` and `action`.   
`ovnkube_controller_admin_network_policies_db_objects` |  `table_name`: specifies either `ACL` or `Address_Set` |  The total number of OVN Northbound database (nbdb) objects that are created by all the ANP in the cluster grouped by the `table_name`.   
`ovnkube_controller_baseline_admin_network_policies_db_objects` |  `table_name`: specifies either `ACL` or `Address_Set` |  The total number of OVN Northbound database (nbdb) objects that are created by all the BANP in the cluster grouped by the `table_name`.   
Show more
