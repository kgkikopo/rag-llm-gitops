# 4.7. Assigning machine set resources to infrastructure nodes

Apply taints and tolerations to infrastructure nodes so user workloads are not scheduled inadvertently to those nodes. 

After creating an infrastructure machine set, the `worker` and `infra` roles are applied to new infra nodes. Nodes with the `infra` role are not counted toward the total number of subscriptions that are required to run the environment, even when the `worker` role is also applied. 

However, when an infra node is assigned the worker role, there is a chance that user workloads can get assigned inadvertently to the infra node. To avoid this, you can apply a taint to the infra node and tolerations for the pods that you want to control. 

## 4.7.1. Bind infrastructure node workloads using taints and tolerations

To avoid user workloads being inadvertently assigned to an infra node, you can apply a taint to the infra node and tolerations for the pods you want to control. After creating an infrastructure machine set, the `worker` and `infra` roles are applied to new infra nodes. 

Nodes with the `infra` role applied are not counted toward the total number of subscriptions that are required to run the environment, even when the `worker` role is also applied. If you have an infrastructure node that has the `infra` and `worker` roles assigned, you must configure the node so that user workloads are not assigned to it. 

Important

It is recommended that you preserve the dual `infra,worker` label that is created for infrastructure nodes and use taints and tolerations to manage nodes that user workloads are scheduled on. If you remove the `worker` label from the node, you must create a custom pool to manage it. A node with a label other than `master` or `worker` is not recognized by the MCO without a custom pool. Maintaining the `worker` label allows the node to be managed by the default worker machine config pool, if no custom pools that select the custom label exists. The `infra` label communicates to the cluster that it does not count toward the total number of subscriptions. 

**Prerequisites**

  * Configure additional `MachineSet` objects in your OpenShift Container Platform cluster. 



**Procedure**

  1. Add a taint to the infrastructure node to prevent scheduling user workloads on it: 

     1. Determine if the node has the taint by running the following command: 

```shell-session
$ oc describe nodes <node_name>
```


**Sample output**

```plaintext
oc describe node ci-ln-iyhx092-f76d1-nvdfm-worker-b-wln2l
Name:               ci-ln-iyhx092-f76d1-nvdfm-worker-b-wln2l
Roles:              worker
 ...
Taints:             node-role.kubernetes.io/infra=reserved:NoSchedule
 ...
```


This example shows that the node has a taint. You can proceed with adding a toleration to your pod in the next step. 

     2. If you have not configured a taint to prevent scheduling user workloads on it, configure a taint by running the following command: 

```shell-session
$ oc adm taint nodes <node_name> <key>=<value>:<effect>
```


For example: 

```shell-session
$ oc adm taint nodes node1 node-role.kubernetes.io/infra=reserved:NoSchedule
```


Tip

You can alternatively edit the pod specification to add the taint: 

```yaml
apiVersion: v1
kind: Node
metadata:
  name: node1
# ...
spec:
  taints:
    - key: node-role.kubernetes.io/infra
      value: reserved
      effect: NoSchedule
# ...
```


These examples place a taint on `node1` that has the `node-role.kubernetes.io/infra` key and the `NoSchedule` taint effect. Nodes with the `NoSchedule` effect schedule only pods that tolerate the taint, but allow existing pods to remain scheduled on the node. If you added a `NoSchedule` taint to the infrastructure node, any pods that are controlled by a daemon set on that node are marked as `misscheduled`. You must either delete the pods or add a toleration to the pods as shown in the Red Hat Knowledgebase solution [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171). Note that you cannot add a toleration to a daemon set object that is managed by an operator. 

Note

If a descheduler is used, pods violating node taints could be evicted from the cluster. 

  2. Add tolerations to the pods that you want to schedule on the infrastructure node, such as the router, registry, and monitoring workloads. Referencing the previous examples, add the following tolerations to the `Pod` object specification: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:

# ...
spec:
# ...
  tolerations:
    - key: <node_taint_key>
      value: <node_taint_value>
      effect: <taint_effect>
      operator: Equal
```


where: 

`<node_taint_key>`
     Specifies the key that you added to the taint on the node. 
`<node_taint_value>`
     Specifies the value of the key-value pair taint that you added to the node. 
`<taint_effect>`
     Specifies the effect that you added to the node. 
`Equal`
    

Specifies that a taint with a key matching `<node_taint_key>` is required to be present on the node. 

This toleration matches the taint created by the `oc adm taint` command. A pod with this toleration can be scheduled onto the infrastructure node. 

Note

Moving pods for an Operator installed via OLM to an infrastructure node is not always possible. The capability to move Operator pods depends on the configuration of each Operator. 

  3. Schedule the pod to the infrastructure node by using a scheduler. See the documentation for "Controlling pod placement using the scheduler" for details. 
  4. Remove any workloads that you do not want, or that do not belong, on the new infrastructure node. See the list of workloads supported for use on infrastructure nodes in "OpenShift Container Platform infrastructure components". 



**Additional resources**

  * [Controlling pod placement using the scheduler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-about)
