# 24.3. Requesting CRI-O and Kubelet profiling data using the Node Observability Operator

Creating a Node Observability custom resource to collect CRI-O and Kubelet profiling data. 

## 24.3.1. Creating the Node Observability custom resource

You must create and run the `NodeObservability` custom resource (CR) before you run the profiling query. When you run the `NodeObservability` CR, it creates the necessary machine config and machine config pool CRs to enable the CRI-O profiling on the worker nodes matching the `nodeSelector`. 

Important

If CRI-O profiling is not enabled on the worker nodes, the `NodeObservabilityMachineConfig` resource gets created. Worker nodes matching the `nodeSelector` specified in `NodeObservability` CR restarts. This might take 10 or more minutes to complete. 

Note

Kubelet profiling is enabled by default. 

The CRI-O unix socket of the node is mounted on the agent pod, which allows the agent to communicate with CRI-O to run the pprof request. Similarly, the `kubelet-serving-ca` certificate chain is mounted on the agent pod, which allows secure communication between the agent and node’s kubelet endpoint. 

**Prerequisites**

  * You have installed the Node Observability Operator. 
  * You have installed the OpenShift CLI (oc). 
  * You have access to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Log in to the OpenShift Container Platform CLI by running the following command: 

```shell-session
$ oc login -u kubeadmin https://<HOSTNAME>:6443
```


  2. Switch back to the `node-observability-operator` namespace by running the following command: 

```shell-session
$ oc project node-observability-operator
```


  3. Create a CR file named `nodeobservability.yaml` that contains the following text: 

```yaml
    apiVersion: nodeobservability.olm.openshift.io/v1alpha2
    kind: NodeObservability
    metadata:
      name: cluster
    spec:
      nodeSelector:
        kubernetes.io/hostname: <node_hostname>
      type: crio-kubelet
```


where: 

`cluster`
     You must specify the name as `cluster` because there should be only one `NodeObservability` CR per cluster. 
`<node_hostname>`
     Specify the nodes on which the Node Observability agent must be deployed. 

  4. Run the `NodeObservability` CR: 

```shell-session
oc apply -f nodeobservability.yaml
```


**Example output**

```shell-session
nodeobservability.olm.openshift.io/cluster created
```


  5. Review the status of the `NodeObservability` CR by running the following command: 

```shell-session
$ oc get nob/cluster -o yaml | yq '.status.conditions'
```


**Example output**

```shell-session
conditions:
  conditions:
  - lastTransitionTime: "2022-07-05T07:33:54Z"
    message: 'DaemonSet node-observability-ds ready: true NodeObservabilityMachineConfig
      ready: true'
    reason: Ready
    status: "True"
    type: Ready
```


`NodeObservability` CR run is completed when the reason is `Ready` and the status is `True`. 




## 24.3.2. Running the profiling query

To run the profiling query, you must create a `NodeObservabilityRun` resource. The profiling query is a blocking operation that fetches CRI-O and Kubelet profiling data for a duration of 30 seconds. 

After the profiling query is complete, you must retrieve the profiling data inside the container file system `/run/node-observability` directory. The lifetime of data is bound to the agent pod through the `emptyDir` volume, so you can access the profiling data while the agent pod is in the `running` status. 

Important

You can request only one profiling query at any point of time. 

**Prerequisites**

  * You have installed the Node Observability Operator. 
  * You have created the `NodeObservability` custom resource (CR). 
  * You have access to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Create a `NodeObservabilityRun` resource file named `nodeobservabilityrun.yaml` that contains the following text: 

```yaml
apiVersion: nodeobservability.olm.openshift.io/v1alpha2
kind: NodeObservabilityRun
metadata:
  name: nodeobservabilityrun
spec:
  nodeObservabilityRef:
    name: cluster
```


  2. Trigger the profiling query by running the `NodeObservabilityRun` resource: 

```shell-session
$ oc apply -f nodeobservabilityrun.yaml
```


  3. Review the status of the `NodeObservabilityRun` by running the following command: 

```shell-session
$ oc get nodeobservabilityrun nodeobservabilityrun -o yaml  | yq '.status.conditions'
```


**Example output**

```shell-session
conditions:
- lastTransitionTime: "2022-07-07T14:57:34Z"
  message: Ready to start profiling
  reason: Ready
  status: "True"
  type: Ready
- lastTransitionTime: "2022-07-07T14:58:10Z"
  message: Profiling query done
  reason: Finished
  status: "True"
  type: Finished
```


The profiling query is complete once the status is `True` and type is `Finished`. 

  4. Retrieve the profiling data from the container’s `/run/node-observability` path by running the following bash script: 

```bash
for a in $(oc get nodeobservabilityrun nodeobservabilityrun -o yaml | yq .status.agents[].name); do
  echo "agent ${a}"
  mkdir -p "/tmp/${a}"
  for p in $(oc exec "${a}" -c node-observability-agent -- bash -c "ls /run/node-observability/*.pprof"); do
    f="$(basename ${p})"
    echo "copying ${f} to /tmp/${a}/${f}"
    oc exec "${a}" -c node-observability-agent -- cat "${p}" > "/tmp/${a}/${f}"
  done
done
```
