# 3.3. View the cluster capabilities

As a cluster administrator, you can view the capabilities by using the `clusterversion` resource status. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * To view the status of the cluster capabilities, run the following command: 

```shell-session
$ oc get clusterversion version -o jsonpath='{.spec.capabilities}{"\n"}{.status.capabilities}{"\n"}'
```


**Example output**

```shell-session
{"additionalEnabledCapabilities":["openshift-samples"],"baselineCapabilitySet":"None"}
{"enabledCapabilities":["openshift-samples"],"knownCapabilities":["CSISnapshot","Console","Insights","Storage","baremetal","marketplace","openshift-samples"]}
```
