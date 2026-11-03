# 3.7. Configure Node Feature Discovery worker and controller pod scheduling

You can control where Node Feature Discovery (NFD) worker and controller pods are scheduled by configuring node selectors and tolerations in the `NodeFeatureDiscovery` custom resource. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 
  * You have installed the NFD Operator. 



Note

If you specify `workerNodeSelector` without the required `workerTolerations`, NFD worker pods are not scheduled on tainted nodes, even when the nodes match the configured node selector. 

**Procedure**

  1. Label the target node with the label you use in the `workerNodeSelector` field by entering the following command: 

```shell-session
$ oc label node <node_name> special-node=true
```


  2. Edit the `NodeFeatureDiscovery` custom resource by entering the following command: 

```shell-session
$ oc edit NodeFeatureDiscovery nfd-instance -n openshift-nfd
```


  3. Configure the scheduling options: 

```yaml
apiVersion: nfd.openshift.io/v1
kind: NodeFeatureDiscovery
metadata:
  name: nfd-instance
  namespace: openshift-nfd
spec:
  enableTaints: false
  instance: ""
  operand:
    imagePullPolicy: IfNotPresent
    servicePort: 12000
    workerNodeSelector:
      special-node: "true"
    workerTolerations:
      - key: "node-role.kubernetes.io/ai"
        operator: "Exists"
        effect: "NoSchedule"
      - key: "node-role.kubernetes.io/ai"
        operator: "Exists"
        effect: "NoExecute"
    masterTolerations:
      - key: "node-role.kubernetes.io/master"
        operator: "Exists"
        effect: "NoSchedule"
      - key: "node-role.kubernetes.io/control-plane"
        operator: "Exists"
        effect: "NoSchedule"
  prunerOnDelete: false
  topologyUpdater: false
```


where: 

`spec.operand.workerNodeSelector`
     Controls where the NFD worker DaemonSet is scheduled. Configure this field under `spec.operand`. 
`spec.operand.workerTolerations`
     Allows the NFD worker pods to tolerate taints applied to the selected nodes. Configure this field under `spec.operand`. 
`spec.operand.masterTolerations`
     Allows NFD controller pods to tolerate taints on control plane nodes. The tolerations must match the node taints for the controller pods to schedule successfully. 




**Verification**

  1. Verify that the NFD worker pods are scheduled on the expected nodes by entering the following command: 

```shell-session
$ oc get pods -n openshift-nfd -o wide
```


  2. Verify the node labels by entering the following command: 

```shell-session
$ oc get nodes --show-labels
```


  3. Verify the node taints by entering the following command: 

```shell-session
$ oc get node <node_name> -o jsonpath='{.spec.taints}'
```


After verification, NFD worker pods should appear on nodes with the `special-node=true` label, or with the label you configured in `workerNodeSelector`. Controller pods should remain `Running` in the `openshift-nfd` namespace.
