# 12.1. About machine health checks

You can use machine health checks to detect and remediate unhealthy machines automatically, limiting disruption to the targeted machine pool. 

Note

You can only apply a machine health check to machines that are managed by compute machine sets or control plane machine sets. 

To monitor machine health, create a resource to define the configuration for a controller. Set a condition to check, such as staying in the `NotReady` status for five minutes or displaying a permanent condition in the node-problem-detector, and a label for the set of machines to monitor. 

The controller that observes a `MachineHealthCheck` resource checks for the defined condition. If a machine fails the health check, the machine is automatically deleted and one is created to take its place. When a machine is deleted, you see a `machine deleted` event. 

To limit disruptive impact of the machine deletion, the controller drains and deletes only one node at a time. If there are more unhealthy machines than the `maxUnhealthy` threshold allows for in the targeted pool of machines, remediation stops and therefore enables manual intervention. 

Note

Consider the timeouts carefully, accounting for workloads and requirements. 

  * Long timeouts can result in long periods of downtime for the workload on the unhealthy machine. 
  * Too short timeouts can result in a remediation loop. For example, the timeout for checking the `NotReady` status must be long enough to allow the machine to complete the startup process. 



To stop the check, remove the resource. 

## 12.1.1. Limitations when deploying machine health checks

There are limitations to consider before deploying a machine health check: 

  * Only machines owned by a machine set are remediated by a machine health check. 
  * If the node for a machine is removed from the cluster, a machine health check considers the machine to be unhealthy and remediates it immediately. 
  * If the corresponding node for a machine does not join the cluster after the `nodeStartupTimeout`, the machine is remediated. 
  * A machine is remediated immediately if the `Machine` resource phase is `Failed`. 



**Additional resources**

  * [About listing all the nodes in a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-viewing-listing_nodes-nodes-viewing)
  * [Short-circuiting machine health check remediation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/deploying-machine-health-checks#machine-health-checks-short-circuiting_deploying-machine-health-checks "12.2.1. About short-circuiting machine health check remediation")
  * [About the Control Plane Machine Set Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-about "10.1. About control plane machine sets")
