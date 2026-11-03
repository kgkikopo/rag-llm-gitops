# 16.1. Network observability deployment in specific nodes

Configure the `FlowCollector` resource using scheduling specifications, including `NodeSelector`, `Tolerations`, and `Affinity`, to control the deployment of network observability components on specific nodes. 

The `spec.agent.ebpf.advanced.scheduling`, `spec.processor.advanced.scheduling`, and `spec.consolePlugin.advanced.scheduling` specifications have the following configurable settings: 

  * `NodeSelector`
  * `Tolerations`
  * `Affinity`
  * `PriorityClassName`



**Sample`FlowCollector` resource for `spec.<component>.advanced.scheduling`**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
# ...
advanced:
  scheduling:
    tolerations:
    - key: "<taint key>"
      operator: "Equal"
      value: "<taint value>"
      effect: "<taint effect>"
      nodeSelector:
        <key>: <value>
      affinity:
        nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: name
              operator: In
              values:
              - app-worker-node
      priorityClassName: """
# ...
```


**Additional resources**

  * [Understanding taints and tolerations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-taints-tolerations-about_nodes-scheduler-taints-tolerations)
  * [Assign Pods to Nodes (Kubernetes documentation)](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
  * [Pod Priority and Preemption (Kubernetes documentation)](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)
