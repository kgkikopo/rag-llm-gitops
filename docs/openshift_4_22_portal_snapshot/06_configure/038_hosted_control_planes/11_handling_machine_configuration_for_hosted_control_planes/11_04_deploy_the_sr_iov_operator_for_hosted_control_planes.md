# 11.4. Deploy the SR-IOV Operator for hosted control planes

After you configure and deploy your hosting service cluster, you can create a subscription to the SR-IOV Operator on a hosted cluster. The SR-IOV pod runs on worker machines rather than the control plane. 

**Prerequisites**

You must configure and deploy the hosted cluster on AWS. 

**Procedure**

  1. Create a namespace and an Operator group: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-sriov-network-operator
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: sriov-network-operators
  namespace: openshift-sriov-network-operator
spec:
  targetNamespaces:
  - openshift-sriov-network-operator
```


  2. Create a subscription to the SR-IOV Operator: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: sriov-network-operator-subsription
  namespace: openshift-sriov-network-operator
spec:
  channel: stable
  name: sriov-network-operator
  config:
    nodeSelector:
      node-role.kubernetes.io/worker: ""
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


**Verification**

  1. To verify that the SR-IOV Operator is ready, run the following command and view the resulting output: 

```shell-session
$ oc get csv -n openshift-sriov-network-operator
```


**Example output**

```shell-session
NAME                                         DISPLAY                   VERSION               REPLACES                                     PHASE
sriov-network-operator.4.22.0-202211021237   SR-IOV Network Operator   4.22.0-202211021237   sriov-network-operator.4.22.0-202210290517   Succeeded
```


  2. To verify that the SR-IOV pods are deployed, run the following command: 

```shell-session
$ oc get pods -n openshift-sriov-network-operator
```
