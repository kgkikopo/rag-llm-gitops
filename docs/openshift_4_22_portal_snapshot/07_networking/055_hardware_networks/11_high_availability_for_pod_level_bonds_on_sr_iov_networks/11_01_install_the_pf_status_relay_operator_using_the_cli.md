# 11.1. Install the PF Status Relay Operator using the CLI

Install the PF Status Relay Operator to enable OpenShift Container Platform to use Link Aggregation Control Protocol (LACP) as an active health check on physical functions. 

**Prerequisites**

  * You configured LACP on your upstream switch. 
  * You configured pod-level bonding for your SR-IOV networks. 
  * You installed the OpenShift CLI (`oc`). 
  * You have cluster-admin privileges. 



**Procedure**

  1. Create the `openshift-pf-status-relay-operator` namespace by entering the following command: 

```bash
$ cat << EOF| oc create -f -
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-pf-status-relay-operator
  annotations:
    workload.openshift.io/allowed: management
EOF
```


  2. Create an `OperatorGroup` custom resource (CR) by entering the following command: 

```bash
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: pf-status-relay-operators
  namespace: openshift-pf-status-relay-operator
spec:
  targetNamespaces:
  - openshift-pf-status-relay-operator
EOF
```


  3. Create a `Subscription` CR for the PF Status Relay Operator by entering the following command: 

```bash
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: pf-status-relay-operator-subscription
  namespace: openshift-pf-status-relay-operator
spec:
  channel: stable
  name: pf-status-relay-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
```


**Verification**

  * To verify that the Operator is installed, enter the following command and then check that output shows `Succeeded` for the Operator: 

```bash
$ oc get csv -n openshift-pf-status-relay-operator -o custom-columns=Name:.metadata.name,Phase:.status.phase
```
