# 6.1. Cluster Network Operator

The Cluster Network Operator implements the `network` API from the `operator.openshift.io` API group. The Operator deploys the OVN-Kubernetes network plugin, or the network provider plugin that you selected during cluster installation, by using a daemon set. 

The Cluster Network Operator is deployed during installation as a Kubernetes `Deployment`. 

**Procedure**

  1. Run the following command to view the Deployment status: 

```shell-session
$ oc get -n openshift-network-operator deployment/network-operator
```


**Example output**

```shell-session
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
network-operator   1/1     1            1           56m
```


  2. Run the following command to view the state of the Cluster Network Operator: 

```shell-session
$ oc get clusteroperator/network
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
network   4.16.1     True        False         False      50m
```


The following fields provide information about the status of the operator: `AVAILABLE`, `PROGRESSING`, and `DEGRADED`. The `AVAILABLE` field is `True` when the Cluster Network Operator reports an available status condition.
