# 12.2. About the MachineHealthCheck custom resource

You control how a machine health check remediates unhealthy machines by using a `MachineHealthCheck` custom resource (CR) to configure health criteria, remediation limits, and startup timeouts for machines in a targeted pool. 

The `MachineHealthCheck` resource for all cloud-based installation types, and other than bare metal, resembles the following YAML file: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: example
  namespace: openshift-machine-api
spec:
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-machine-role: <role>
      machine.openshift.io/cluster-api-machine-type: <role>
      machine.openshift.io/cluster-api-machineset: <cluster_name>-<label>-<zone>
  unhealthyConditions:
  - type:    "Ready"
    timeout: "300s"
    status: "False"
  - type:    "Ready"
    timeout: "300s"
    status: "Unknown"
  maxUnhealthy: "40%"
  nodeStartupTimeout: "10m"
```


where: 

`metadata.name`
     Specifies the name of the machine health check to deploy. 
`spec.selector.matchLabels`
    

Specifies the machine pool and machine set to check by adding labels: 

  * `machine.openshift.io/cluster-api-machine-role`: Specifies a label for the machine pool that you want to check. 
  * `machine.openshift.io/cluster-api-machine-type`: Specifies a label for the machine pool that you want to check. 
  * `machine.openshift.io/cluster-api-machineset`: Specifies the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`. 



`spec.unhealthyConditions.timeout`
     Specifies the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine. 
`spec.maxUnhealthy`
     Specifies the amount of machines allowed to be concurrently remediated in the targeted pool. This can be set as a percentage or an integer. If the number of unhealthy machines exceeds the limit set by `maxUnhealthy`, remediation is not performed. 
`spec.nodeStartupTimeout`
     Specifies the timeout duration that a machine health check must wait for a node to join the cluster before a machine is determined to be unhealthy. 

Note

The `matchLabels` are examples only; you must map your machine groups based on your specific needs. 

## 12.2.1. About short-circuiting machine health check remediation

You can use machine health check short-circuiting to ensure that machine health checks remediate machines only when the cluster is healthy, by configuring the `maxUnhealthy` field in the `MachineHealthCheck` resource. 

If you define a value for the `maxUnhealthy` field, before remediating any machines, the `MachineHealthCheck` compares the value of `maxUnhealthy` with the number of machines within its target pool that it has determined to be unhealthy. Remediation is not performed if the number of unhealthy machines exceeds the `maxUnhealthy` limit. 

Important

If `maxUnhealthy` is not set, the value defaults to `100%` and the machines are remediated regardless of the state of the cluster. 

The appropriate `maxUnhealthy` value depends on the scale of the cluster you deploy and how many machines the `MachineHealthCheck` covers. For example, you can use the `maxUnhealthy` value to cover multiple compute machine sets across multiple availability zones so that if you lose an entire zone, your `maxUnhealthy` setting prevents further remediation within the cluster. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability. 

Important

If you configure a `MachineHealthCheck` resource for the control plane, set the value of `maxUnhealthy` to `1`. 

This configuration ensures that the machine health check takes no action when multiple control plane machines appear to be unhealthy. Multiple unhealthy control plane machines can indicate that the etcd cluster is degraded or that a scaling operation to replace a failed machine is in progress. 

If the etcd cluster is degraded, manual intervention might be required. If a scaling operation is in progress, the machine health check should allow it to finish. 

The `maxUnhealthy` field can be set as either an integer or percentage. There are different remediation implementations depending on the `maxUnhealthy` value. 

Setting maxUnhealthy by using an absolute value
    

If `maxUnhealthy` is set to `2`: 

  * Remediation will be performed if 2 or fewer nodes are unhealthy 
  * Remediation will not be performed if 3 or more nodes are unhealthy 



These values are independent of how many machines are being checked by the machine health check. 

Setting maxUnhealthy by using percentages
    

If `maxUnhealthy` is set to `40%` and there are 25 machines being checked: 

  * Remediation will be performed if 10 or fewer nodes are unhealthy 
  * Remediation will not be performed if 11 or more nodes are unhealthy 



If `maxUnhealthy` is set to `40%` and there are 6 machines being checked: 

  * Remediation will be performed if 2 or fewer nodes are unhealthy 
  * Remediation will not be performed if 3 or more nodes are unhealthy 



Note

The allowed number of machines is rounded down when the percentage of `maxUnhealthy` machines that are checked is not a whole number.
