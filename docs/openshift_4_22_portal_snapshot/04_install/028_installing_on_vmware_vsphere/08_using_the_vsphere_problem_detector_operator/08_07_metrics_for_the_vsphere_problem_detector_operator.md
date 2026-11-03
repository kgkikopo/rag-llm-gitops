# 8.7. Metrics for the vSphere Problem Detector Operator

The vSphere Problem Detector Operator exposes the following metrics for use by the OpenShift Container Platform monitoring stack. 

Table 8.3. Metrics exposed by the vSphere Problem Detector OperatorName| Description  
---|---  
`vsphere_cluster_check_total` |  Cumulative number of cluster-level checks that the vSphere Problem Detector Operator performed. This count includes both successes and failures.   
`vsphere_cluster_check_errors` |  Number of failed cluster-level checks that the vSphere Problem Detector Operator performed. For example, a value of `1` indicates that one cluster-level check failed.   
`vsphere_esxi_version_total` |  Counts the number of ESXi hosts with a specific version. Note that if a host runs more than one node, the vSphere Problem Detector Operator counts the host only once.   
`vsphere_node_check_total` |  Cumulative number of node-level checks that the vSphere Problem Detector Operator performed. This count includes both successes and failures.   
`vsphere_node_check_errors` |  Counts the number of failed node-level checks that the vSphere Problem Detector Operator performed. For example, a value of `1` indicates that one node-level check failed.   
`vsphere_node_hw_version_total` |  Number of vSphere nodes with a specific hardware version.   
`vsphere_vcenter_info` |  Information about the vSphere vCenter Server.   
Show more
