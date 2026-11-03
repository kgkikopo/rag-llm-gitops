# 12.4. About power-based remediation of bare metal

You can configure and deploy a machine health check to detect and repair unhealthy bare-metal nodes, which is critical to ensuring the overall health of the cluster. 

Physically remediating a cluster can be challenging and any delay in putting the machine into a safe or an operational state increases the time the cluster remains in a degraded state, and the risk that subsequent failures might bring the cluster offline. Power-based remediation helps counter such challenges. 

Instead of reprovisioning the nodes, power-based remediation uses a power controller to power off an inoperable node. This type of remediation is also called power fencing. 

OpenShift Container Platform uses the `MachineHealthCheck` controller to detect faulty bare metal nodes. Power-based remediation is fast and reboots faulty nodes instead of removing them from the cluster. 

Power-based remediation provides the following capabilities: 

  * Allows the recovery of control plane nodes 
  * Reduces the risk of data loss in hyperconverged environments 
  * Reduces the downtime associated with recovering physical machines 



## 12.4.1. About machine health checks on bare metal

Machine deletion on bare metal cluster triggers reprovisioning of a bare metal host. Usually bare metal reprovisioning is a lengthy process, during which the cluster is missing compute resources and applications might be interrupted. 

There are two ways to change the default remediation process from machine deletion to host power-cycle: 

  1. Annotate the `MachineHealthCheck` resource with the `machine.openshift.io/remediation-strategy: external-baremetal` annotation. 
  2. Create a `Metal3RemediationTemplate` resource, and refer to it in the `spec.remediationTemplate` of the `MachineHealthCheck`. 



After using one of these methods, unhealthy machines are power-cycled by using Baseboard Management Controller (BMC) credentials. 

About the annotation-based remediation process
    

The annotation-based remediation process performs the following steps: 

  1. The MachineHealthCheck (MHC) controller detects that a node is unhealthy. 
  2. The MHC notifies the bare metal machine controller which requests to power-off the unhealthy node. 
  3. After the power is off, the node is deleted, which allows the cluster to reschedule the affected workload on other nodes. 
  4. The bare metal machine controller requests to power on the node. 
  5. After the node is up, the node re-registers itself with the cluster, resulting in the creation of a new node. 
  6. After the node is recreated, the bare metal machine controller restores the annotations and labels that existed on the unhealthy node before its deletion. 



Note

If the power operations did not complete, the bare metal machine controller triggers the reprovisioning of the unhealthy node unless this is a control plane node or a node that was provisioned externally. 

About the metal3-based remediation process
    

The metal3-based remediation process performs the following steps: 

  1. The MachineHealthCheck (MHC) controller detects that a node is unhealthy. 
  2. The MHC creates a metal3 remediation custom resource for the metal3 remediation controller, which requests to power-off the unhealthy node. 
  3. After the power is off, the node is deleted, which allows the cluster to reschedule the affected workload on other nodes. 
  4. The metal3 remediation controller requests to power on the node. 
  5. After the node is up, the node re-registers itself with the cluster, resulting in the creation of a new node. 
  6. After the node is recreated, the metal3 remediation controller restores the annotations and labels that existed on the unhealthy node before its deletion. 



Note

If the power operations did not complete, the metal3 remediation controller triggers the reprovisioning of the unhealthy node unless this is a control plane node or a node that was provisioned externally. 

## 12.4.2. Creating a MachineHealthCheck resource for bare metal

You control how a machine health check remediates unhealthy machines by using a `MachineHealthCheck` resource to configure health criteria, remediation limits, and startup timeouts for machines in a targeted pool. 

**Prerequisites**

  * The OpenShift Container Platform is installed using installer-provisioned infrastructure. 
  * Access to Baseboard Management Controller (BMC) credentials or BMC access to each node. 
  * Network access to the BMC interface of the unhealthy node. 
  * For a metal3-based remediation, a `Metal3RemediationTemplate` resource must exist. 

**Sample`Metal3RemediationTemplate` resource for bare metal, metal3-based remediation**

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: Metal3RemediationTemplate
metadata:
  name: metal3-remediation-template
  namespace: openshift-machine-api
spec:
  template:
    spec:
      strategy:
        type: Reboot
        retryLimit: 1
        timeout: 5m0s
```


**Procedure**

  1. Create a `healthcheck.yaml` file that contains the definition of your machine health check. 

**Sample`MachineHealthCheck` resource for bare metal, annotation-based remediation**

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: example
  namespace: openshift-machine-api
  annotations:
    machine.openshift.io/remediation-strategy: external-baremetal
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


where 

`metadata.name`
     Specify the name of the machine health check to deploy. 
`metadata.annotations`
    

Specify the required annotation for the annotation-based remediation process. 

Important

You must include the `machine.openshift.io/remediation-strategy: external-baremetal` annotation in the `annotations` section to enable annotation-based remediation. With this remediation strategy, unhealthy hosts are rebooted instead of removed from the cluster. 

`spec.selector.matchLabels`
    

Specify the machine pool and machine set to check by adding labels: 

     * `machine.openshift.io/cluster-api-machine-role`: Specify a label for the machine pool that you want to check. 
     * `machine.openshift.io/cluster-api-machine-type`: Specify a label for the machine pool that you want to check. 
     * `machine.openshift.io/cluster-api-machineset`: Specify the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`. 

`spec.unhealthyConditions.timeout`
     Specify the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine. 
`spec.maxUnhealthy`
     Specify the amount of machines allowed to be concurrently remediated in the targeted pool. This can be set as a percentage or an integer. If the number of unhealthy machines exceeds the limit set by `maxUnhealthy`, remediation is not performed. 
`spec.nodeStartupTimeout`
     Specify the timeout duration that a machine health check must wait for a node to join the cluster before a machine is determined to be unhealthy. 

**Sample`MachineHealthCheck` resource for bare metal, metal3-based remediation**

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
  remediationTemplate:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: Metal3RemediationTemplate
    name: metal3-remediation-template
    namespace: openshift-machine-api
  unhealthyConditions:
  - type:    "Ready"
    timeout: "300s"
```


where: 

`metadata.name`
     Specify the name of the machine health check to deploy. 
`spec.selector.matchLabels`
    

Specify the machine pool and machine set to check by adding labels: 

     * `machine.openshift.io/cluster-api-machine-role`: Specify a label for the machine pool that you want to check. 
     * `machine.openshift.io/cluster-api-machine-type`: Specify a label for the machine pool that you want to check. 
     * `machine.openshift.io/cluster-api-machineset`: Specify the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`. 

`spec.remediationTemplate`
    

Specify the metal3 remediation template to use. Provide the following information: 

     * `apiVersion`. Specify the API version as `infrastructure.cluster.x-k8s.io/v1beta1`. 
     * `kind`. Specify `Metal3RemediationTemplate`. 
     * `name`. Specify the name of the template. 
     * `namespace`. Specify the namespace of the template. 

`spec.unhealthyConditions.timeout`
     Specify the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine. 

Note

The `matchLabels` are examples only; you must map your machine groups based on your specific needs. 

  2. Apply the `healthcheck.yaml` file to your cluster using the following command: 

```shell-session
$ oc apply -f healthcheck.yaml
```


## 12.4.3. Troubleshooting issues with power-based remediation

To troubleshoot issues you are having with power-based remediation, check the connection to the Baseboard Management Controller (BMC). 

**Procedure**

  * Verify the following conditions: 

    * You have access to the BMC. 
    * The BMC is connected to the control plane node that is responsible for running the remediation task.
