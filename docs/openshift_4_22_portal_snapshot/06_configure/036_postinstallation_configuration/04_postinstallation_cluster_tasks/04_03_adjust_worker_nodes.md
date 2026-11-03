# 4.3. Adjust worker nodes

Resize worker nodes by creating new compute machine sets, scaling them up, and scaling down the original machine set before removal. 

If you incorrectly sized the worker nodes during deployment, adjust them by creating one or more new compute machine sets, scale them up, then scale the original compute machine set down before removing them. 

## 4.3.1. Understanding the difference between compute machine sets and the machine config pool

Compute machine sets and machine config pools control different aspects of node lifecycle in OpenShift Container Platform. Understanding how each object relates to scaling and upgrades helps you configure nodes correctly. 

`MachineSet` objects describe OpenShift Container Platform nodes with respect to the cloud or machine provider. 

The `MachineConfigPool` object allows `MachineConfigController` components to define and provide the status of machines in the context of upgrades. 

The `MachineConfigPool` object allows users to configure how upgrades are rolled out to the OpenShift Container Platform nodes in the machine config pool. 

The `NodeSelector` object can be replaced with a reference to the `MachineSet` object. 

## 4.3.2. Scale a compute machine set manually

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


## 4.3.3. The compute machine set deletion policy

Compute machine sets can be configured to use the `Random`, `Newest`, and `Oldest` deletion options. The default is `Random`, meaning that random machines are chosen and deleted when scaling compute machine sets down. 

The deletion policy can be set according to the use case by modifying the particular compute machine set as in the following example: 

```yaml
spec:
  deletePolicy: <delete_policy>
  replicas: <desired_replica_count>
```


Specific machines can also be prioritized for deletion by adding the annotation `machine.openshift.io/delete-machine=true` to the machine of interest, regardless of the deletion policy. 

Important

By default, the OpenShift Container Platform router pods are deployed on workers. Because the router is required to access some cluster resources, including the web console, do not scale the worker compute machine set to `0` unless you first relocate the router pods. 

Note

Custom compute machine sets can be used for use cases requiring that services run on specific nodes and that those services are ignored by the controller when the worker compute machine sets are scaling down. This prevents service disruption. 

## 4.3.4. Create default cluster-wide node selectors

You can use default cluster-wide node selectors on pods together with labels on nodes to constrain all pods created in a cluster to specific nodes. 

With cluster-wide node selectors, when you create a pod in that cluster, OpenShift Container Platform adds the default node selectors to the pod and schedules the pod on nodes with matching labels. 

You configure cluster-wide node selectors by editing the Scheduler Operator custom resource (CR). You add labels to a node, a compute machine set, or a machine config. Adding the label to the compute machine set ensures that if the node or machine goes down, new nodes have the label. Labels added to a node or machine config do not persist if the node or machine goes down. 

Note

You can add additional key/value pairs to a pod. But you cannot add a different value for a default key. 

The following procedure adds a default cluster-wide node selector. 

**Procedure**

  1. Edit the Scheduler Operator CR to add the default cluster-wide node selectors: 

```shell-session
$ oc edit scheduler cluster
```


**Example Scheduler Operator CR with a node selector**

```yaml
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
...
spec:
  defaultNodeSelector: type=user-node,region=east
  mastersSchedulable: false
```


where: 

`spec.defaultNodeSelector`
     Specifies a node selector with the appropriate `<key>:<value>` pairs. 

After making this change, wait for the pods in the `openshift-kube-apiserver` project to redeploy. This can take several minutes. The default cluster-wide node selector does not take effect until the pods redeploy. 

  2. Add labels to a node by using a compute machine set or editing the node directly: 

     * Use a compute machine set to add labels to nodes managed by the compute machine set when a node is created: 

       1. Run the following command to add labels to a `MachineSet` object: 

```shell-session
$ oc patch MachineSet <name> --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"<key>"="<value>","<key>"="<value>"}}]'  -n openshift-machine-api
```


Add a `<key>/<value>` pair for each label. 

For example: 

```shell-session
$ oc patch MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"type":"user-node","region":"east"}}]'  -n openshift-machine-api
```


Tip

You can alternatively apply the following YAML to add labels to a compute machine set: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  template:
    spec:
      metadata:
        labels:
          region: "east"
          type: "user-node"
```


       2. Verify that the labels are added to the `MachineSet` object by using the `oc edit` command: 

For example: 

```shell-session
$ oc edit MachineSet abc612-msrtw-worker-us-east-1c -n openshift-machine-api
```


**Example`MachineSet` object**

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
  ...
spec:
  ...
  template:
    metadata:
  ...
    spec:
      metadata:
        labels:
          region: east
          type: user-node
  ...
```


       3. Redeploy the nodes associated with that compute machine set by scaling down to `0` and scaling up the nodes: 

For example: 

```shell-session
$ oc scale --replicas=0 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
```


```shell-session
$ oc scale --replicas=1 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
```


       4. When the nodes are ready and available, verify that the label is added to the nodes by using the `oc get` command: 

```shell-session
$ oc get nodes -l <key>=<value>
```


For example: 

```shell-session
$ oc get nodes -l type=user-node
```


**Example output**

```shell-session
NAME                                       STATUS   ROLES    AGE   VERSION
ci-ln-l8nry52-f76d1-hl7m7-worker-c-vmqzp   Ready    worker   61s   v1.35.4
```


     * Add labels directly to a node: 

       1. Edit the `Node` object for the node: 

```shell-session
$ oc label nodes <name> <key>=<value>
```


For example, to label a node: 

```shell-session
$ oc label nodes ci-ln-l8nry52-f76d1-hl7m7-worker-b-tgq49 type=user-node region=east
```


Tip

You can alternatively apply the following YAML to add labels to a node: 

```yaml
kind: Node
apiVersion: v1
metadata:
  name: <node_name>
  labels:
    type: "user-node"
    region: "east"
```


       2. Verify that the labels are added to the node using the `oc get` command: 

```shell-session
$ oc get nodes -l <key>=<value>,<key>=<value>
```


For example: 

```shell-session
$ oc get nodes -l type=user-node,region=east
```


**Example output**

```shell-session
NAME                                       STATUS   ROLES    AGE   VERSION
ci-ln-l8nry52-f76d1-hl7m7-worker-b-tgq49   Ready    worker   17m   v1.35.4
```
