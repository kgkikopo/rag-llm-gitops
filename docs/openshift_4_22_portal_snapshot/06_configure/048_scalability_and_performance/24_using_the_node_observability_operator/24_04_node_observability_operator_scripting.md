# 24.4. Node Observability Operator scripting

Scripting allows you to run pre-configured bash scripts, using the current Node Observability Operator and Node Observability Agent. 

These scripts monitor key metrics like CPU load, memory pressure, and worker node issues. They also collect sar reports and custom performance metrics. 

## 24.4.1. Creating the Node Observability custom resource for scripting

You must create and run the `NodeObservability` custom resource (CR) before you run the scripting. When you run the `NodeObservability` CR, it enables the agent in scripting mode on the compute nodes matching the `nodeSelector` label. 

**Prerequisites**

  * You have installed the Node Observability Operator. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have access to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Log in to the OpenShift Container Platform cluster by running the following command: 

```shell-session
$ oc login -u kubeadmin https://<host_name>:6443
```


  2. Switch to the `node-observability-operator` namespace by running the following command: 

```shell-session
$ oc project node-observability-operator
```


  3. Create a file named `nodeobservability.yaml` that contains the following content: 

```yaml
    apiVersion: nodeobservability.olm.openshift.io/v1alpha2
    kind: NodeObservability
    metadata:
      name: cluster
    spec:
      nodeSelector:
        kubernetes.io/hostname: <node_hostname>
      type: scripting
```


where: 

`cluster`
     You must specify the name as `cluster` because there should be only one `NodeObservability` CR per cluster. 
`<node_hostname>`
     Specify the nodes on which the Node Observability agent must be deployed. 
`scripting`
     To deploy the agent in scripting mode, you must set the type to `scripting`. 

  4. Create the `NodeObservability` CR by running the following command: 

```shell-session
$ oc apply -f nodeobservability.yaml
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
    message: 'DaemonSet node-observability-ds ready: true NodeObservabilityScripting
      ready: true'
    reason: Ready
    status: "True"
    type: Ready
```


The `NodeObservability` CR run is completed when the `reason` is `Ready` and `status` is `"True"`. 




## 24.4.2. Configuring Node Observability Operator scripting

You can configure the Node Observability Operator to run pre-configured scripts for collecting metrics data from compute nodes. 

**Prerequisites**

  * You have installed the Node Observability Operator. 
  * You have created the `NodeObservability` custom resource (CR). 
  * You have access to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Create a file named `nodeobservabilityrun-script.yaml` that contains the following content: 

```yaml
apiVersion: nodeobservability.olm.openshift.io/v1alpha2
kind: NodeObservabilityRun
metadata:
  name: nodeobservabilityrun-script
  namespace: node-observability-operator
spec:
  nodeObservabilityRef:
    name: cluster
    type: scripting
```


Important

You can request only the following scripts: 

     * `metrics.sh`
     * `network-metrics.sh` (uses `monitor.sh`) 

  2. Trigger the scripting by creating the `NodeObservabilityRun` resource with the following command: 

```shell-session
$ oc apply -f nodeobservabilityrun-script.yaml
```


  3. Review the status of the `NodeObservabilityRun` scripting by running the following command: 

```shell-session
$ oc get nodeobservabilityrun nodeobservabilityrun-script -o yaml  | yq '.status.conditions'
```


**Example output**

```shell-session
Status:
  Agents:
    Ip:    10.128.2.252
    Name:  node-observability-agent-n2fpm
    Port:  8443
    Ip:    10.131.0.186
    Name:  node-observability-agent-wcc8p
    Port:  8443
  Conditions:
    Conditions:
      Last Transition Time:  2023-12-19T15:10:51Z
      Message:               Ready to start profiling
      Reason:                Ready
      Status:                True
      Type:                  Ready
      Last Transition Time:  2023-12-19T15:11:01Z
      Message:               Profiling query done
      Reason:                Finished
      Status:                True
      Type:                  Finished
  Finished Timestamp:        2023-12-19T15:11:01Z
  Start Timestamp:           2023-12-19T15:10:51Z
```


The scripting is complete once `Status` is `True` and `Type` is `Finished`. 

  4. Retrieve the scripting data from the root path of the container by running the following bash script: 

```bash
#!/bin/bash

RUN=$(oc get nodeobservabilityrun --no-headers | awk '{print $1}')

for a in $(oc get nodeobservabilityruns.nodeobservability.olm.openshift.io/${RUN} -o json | jq .status.agents[].name); do
  echo "agent ${a}"
  agent=$(echo ${a} | tr -d "\"\'\`")
  base_dir=$(oc exec "${agent}" -c node-observability-agent -- bash -c "ls -t | grep node-observability-agent" | head -1)
  echo "${base_dir}"
  mkdir -p "/tmp/${agent}"
  for p in $(oc exec "${agent}" -c node-observability-agent -- bash -c "ls ${base_dir}"); do
    f="/${base_dir}/${p}"
    echo "copying ${f} to /tmp/${agent}/${p}"
    oc exec "${agent}" -c node-observability-agent -- cat ${f} > "/tmp/${agent}/${p}"
  done
done
```
