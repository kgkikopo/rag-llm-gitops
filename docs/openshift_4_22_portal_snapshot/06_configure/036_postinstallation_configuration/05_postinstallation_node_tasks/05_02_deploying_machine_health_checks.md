# 5.2. Deploying machine health checks

Understand and deploy machine health checks to detect and remediate unhealthy machines in your cluster. 

## 5.2.1. About machine health checks

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

### 5.2.1.1. Limitations when deploying machine health checks

There are limitations to consider before deploying a machine health check: 

  * Only machines owned by a machine set are remediated by a machine health check. 
  * If the node for a machine is removed from the cluster, a machine health check considers the machine to be unhealthy and remediates it immediately. 
  * If the corresponding node for a machine does not join the cluster after the `nodeStartupTimeout`, the machine is remediated. 
  * A machine is remediated immediately if the `Machine` resource phase is `Failed`. 



**Additional resources**

  * [About control plane machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#cpmso-about)



## 5.2.2. About the MachineHealthCheck custom resource

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

## 5.2.3. About short-circuiting machine health check remediation

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

## 5.2.4. Creating a machine health check resource

You can create a `MachineHealthCheck` resource to monitor and automatically remediate unhealthy machines in a machine set. 

Note

You can only apply a machine health check to machines that are managed by compute machine sets or control plane machine sets. 

**Prerequisites**

  * Install the `oc` command-line interface. 



**Procedure**

  1. Create a `healthcheck.yml` file that contains the definition of your machine health check. 
  2. Apply the `healthcheck.yml` file to your cluster: 

```shell-session
$ oc apply -f healthcheck.yml
```


## 5.2.5. Scale a compute machine set manually

To add or remove an instance of a machine in a compute machine set, you can manually scale the compute machine set. 

This guidance is relevant to fully automated, installer-provisioned infrastructure installations. Customized, user-provisioned infrastructure installations do not have compute machine sets. 

**Prerequisites**

  * Install an OpenShift Container Platform cluster and the `oc` command line. 
  * Log in to `oc` as a user with `cluster-admin` permission. 



**Procedure**

  1. View the compute machine sets that are in the cluster by running the following command: 

```shell-session
$ oc get machinesets.machine.openshift.io -n openshift-machine-api
```


The compute machine sets are listed in the form of `<clusterid>-worker-<aws-region-az>`. 

  2. View the compute machines that are in the cluster by running the following command: 

```shell-session
$ oc get machines.machine.openshift.io -n openshift-machine-api
```


  3. Set the annotation on the compute machine that you want to delete by running the following command: 

```shell-session
$ oc annotate machines.machine.openshift.io/<machine_name> -n openshift-machine-api machine.openshift.io/delete-machine="true"
```


  4. Scale the compute machine set by running one of the following commands: 

```shell-session
$ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
```


Or: 

```shell-session
$ oc edit machinesets.machine.openshift.io <machineset> -n openshift-machine-api
```


Tip

You can alternatively apply the following YAML to scale the compute machine set: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  replicas: 2
```


You can scale the compute machine set up or down. It takes several minutes for the new machines to be available. 

Important

By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine. 

You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine. 




**Verification**

  * Verify the deletion of the intended machine by running the following command: 

```shell-session
$ oc get machines.machine.openshift.io
```


## 5.2.6. Understanding the difference between compute machine sets and the machine config pool

Compute machine sets and machine config pools control different aspects of node lifecycle in OpenShift Container Platform. Understanding how each object relates to scaling and upgrades helps you configure nodes correctly. 

`MachineSet` objects describe OpenShift Container Platform nodes with respect to the cloud or machine provider. 

The `MachineConfigPool` object allows `MachineConfigController` components to define and provide the status of machines in the context of upgrades. 

The `MachineConfigPool` object allows users to configure how upgrades are rolled out to the OpenShift Container Platform nodes in the machine config pool. 

The `NodeSelector` object can be replaced with a reference to the `MachineSet` object.
