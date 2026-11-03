# 4.13. Pod disruption budgets

Understand and configure pod disruption budgets to control voluntary disruptions during cluster operations. 

## 4.13.1. Understand how to use pod disruption budgets to specify the number of pods that must be up

To ensure pod availability during voluntary disruptions such as node maintenance or cluster updates, you can use pod disruption budgets to define safety constraints for your applications. 

A `PodDisruptionBudget` is an API object that specifies the minimum number or percentage of replicas that must be up at a time. Setting these in projects can be helpful during node maintenance (such as scaling a cluster down or a cluster upgrade) and is only honored on voluntary evictions (not on node failures). 

A `PodDisruptionBudget` object’s configuration consists of the following key parts: 

  * A label selector, which is a label query over a set of pods. 
  * An availability level, which specifies the minimum number of pods that must be available simultaneously, either: 

    * `minAvailable` is the number of pods must always be available, even during a disruption. 
    * `maxUnavailable` is the number of pods can be unavailable during a disruption. 




Note

`Available` refers to the number of pods that has condition `Ready=True`. `Ready=True` refers to the pod that is able to serve requests and should be added to the load balancing pools of all matching services. 

A `maxUnavailable` of `0%` or `0` or a `minAvailable` of `100%` or equal to the number of replicas is permitted but can block nodes from being drained. 

Warning

The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool. 

You can check for pod disruption budgets across all projects with the following: 

```shell-session
$ oc get poddisruptionbudget --all-namespaces
```


Note

The following example contains some values that are specific to OpenShift Container Platform on AWS. 

**Example output**

```shell-session
NAMESPACE                              NAME                                    MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
openshift-apiserver                    openshift-apiserver-pdb                 N/A             1                 1                     121m
openshift-cloud-controller-manager     aws-cloud-controller-manager            1               N/A               1                     125m
openshift-cloud-credential-operator    pod-identity-webhook                    1               N/A               1                     117m
openshift-cluster-csi-drivers          aws-ebs-csi-driver-controller-pdb       N/A             1                 1                     121m
openshift-cluster-storage-operator     csi-snapshot-controller-pdb             N/A             1                 1                     122m
openshift-cluster-storage-operator     csi-snapshot-webhook-pdb                N/A             1                 1                     122m
openshift-console                      console                                 N/A             1                 1                     116m
#...
```


The `PodDisruptionBudget` is considered healthy when there are at least `minAvailable` pods running in the system. Every pod above that limit can be evicted. 

Note

Depending on your pod priority and preemption settings, lower-priority pods might be removed despite their pod disruption budget requirements. 

## 4.13.2. Specify the number of pods that must be up with pod disruption budgets

You can use a `PodDisruptionBudget` object to specify the minimum number or percentage of replicas that must be up at a time. This ensures pod availability during voluntary disruptions such as node maintenance or cluster updates. 

The following procedure shows how to configure a pod disruption budget. 

**Procedure**

  1. Create a YAML file with the an object definition similar to the following: 

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      name: my-pod
```


where: 

`apiVersion`
     Specifies the `policy/v1` API group. 
`spec.minAvailable`
     Specifies the minimum number of pods that must be available simultaneously. This can be either an integer or a string specifying a percentage, for example, `20%`. 
`spec.selector`
     Specifies a label query over a set of resources. The result of `matchLabels` and `matchExpressions` are logically conjoined. Leave this parameter blank, for example `selector {}`, to select all pods in the project. 

Or: 

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  maxUnavailable: 25%
  selector:
    matchLabels:
      name: my-pod
```


where: 

`apiVersion`
     Specifies the `policy/v1` API group. 
`spec.maxUnavailable`
     Specifies the maximum number of pods that can be unavailable simultaneously. This can be either an integer or a string specifying a percentage, for example, `20%`. 
`spec.selector`
     Specifies a label query over a set of resources. The result of `matchLabels` and `matchExpressions` are logically conjoined. Leave this parameter blank, for example `selector {}`, to select all pods in the project. 

  2. Run the following command to add the object to project: 

```shell-session
$ oc create -f </path/to/file> -n <project_name>
```


## 4.13.3. Specify the eviction policy for unhealthy pods

When you use pod disruption budgets (PDBs) to specify how many pods must be available simultaneously, you can also define the criteria for how unhealthy pods are considered for eviction. The eviction policy determines which pods the cluster can evict. 

You can choose one of the following policies: 

IfHealthyBudget
     Running pods that are not yet healthy can be evicted only if the guarded application is not disrupted. 
AlwaysAllow
    

Running pods that are not yet healthy can be evicted regardless of whether the criteria in the pod disruption budget is met. This policy can help evict malfunctioning applications, such as ones with pods stuck in the `CrashLoopBackOff` state or failing to report the `Ready` status. 

Note

It is recommended to set the `unhealthyPodEvictionPolicy` field to `AlwaysAllow` in the `PodDisruptionBudget` object to support the eviction of misbehaving applications during a node drain. The default behavior is to wait for the application pods to become healthy before the drain can proceed. 

**Procedure**

  1. Create a YAML file that defines a `PodDisruptionBudget` object and specify the unhealthy pod eviction policy: 

**Example`pod-disruption-budget.yaml` file**

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      name: my-pod
  unhealthyPodEvictionPolicy: AlwaysAllow
```


where: 

`spec.unhealthyPodEvictionPolicy`
     Specifies the unhealthy pod eviction policy, either `IfHealthyBudget` or `AlwaysAllow`. The default is `IfHealthyBudget` when the `unhealthyPodEvictionPolicy` field is empty. 

  2. Create the `PodDisruptionBudget` object by running the following command: 

```shell-session
$ oc create -f pod-disruption-budget.yaml
```


With a PDB that has the `AlwaysAllow` unhealthy pod eviction policy set, you can now drain nodes and evict the pods for a malfunctioning application guarded by this PDB. 




**Additional resources**

  * [Enabling features using feature gates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cluster-enabling-features)
  * [Unhealthy Pod Eviction Policy in the Kubernetes documentation](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#unhealthy-pod-eviction-policy)
