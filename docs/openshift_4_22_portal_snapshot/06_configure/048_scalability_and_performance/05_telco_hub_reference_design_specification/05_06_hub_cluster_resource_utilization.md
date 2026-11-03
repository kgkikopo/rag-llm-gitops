# 5.6. Hub cluster resource utilization

Resource utilization was measured for deploying hub clusters in the following scenario: 

  * Under reference load managing 3500 single-node OpenShift clusters. 
  * 3-node compact cluster for management hub running on dual socket bare-metal servers. 
  * Network impairment of 50 ms round-trip latency, 100 Mbps bandwidth limit and 0.02% packet loss. 
  * Observability was not enabled. 
  * Only local storage was used. 



Table 5.1. Resource utilization valuesMetric| Peak Measurement  
---|---  
OpenShift Platform CPU  |  106 cores (52 cores peak per node)   
OpenShift Platform memory  |  504 G (168 G peak per node)   
Show more

**Additional resources**

  * [Comparison of hub cluster and managed cluster templates](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/governance/index#template-comparison-table)
