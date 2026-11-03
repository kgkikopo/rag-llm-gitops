# 7.3. Enable the Network Observability Operator FlowCollectorSlice

Enabling the `FlowCollectorSlice` feature in the `FlowCollector` resource allows cluster administrators to delegate flow collection and data enrichment management to specific namespaces. 

Before project administrators can manage their own settings, a cluster administrator must enable the `FlowCollector` custom resource to watch for the `FlowCollectorSlice` custom resource. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * A `FlowCollector` custom resource exists in the cluster. 
  * You have `cluster-admin` privileges. 



**Procedure**

  1. Edit the `FlowCollector` custom resource by running the following command: 

```shell-session
$ oc edit flowcollector cluster
```


  2. Configure the `spec.processor.slicesConfig` field to define which namespaces are permitted to use slices: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    slicesConfig:
      enable: true
      collectionMode: AllowList
      namespacesAllowList:
       - /openshift-.*|netobserv.*/
```


where: 

`spec.processor.sliceConfig.enable`
     Specifies if the `FlowCollectorSlice` feature is enabled. If not, all resources of kind `FlowCollectorSlice` are ignored. 
`spec.processor.sliceConfig.collectionMode`
     Specifies how the `FlowCollectorSlice` custom resources impacts the flow collection process. When set to `AlwaysCollect`, all flows are collected regardless of the presence of `FlowCollectorSlice`. When set to `AllowList`, only the flows related to namespaces where a `FlowCollectorSlice` resource is present, or configured via the global `namespacesAllowList`, are collected. 
`spec.processor.sliceConfig.namespacesAllowList`
    

Specifies a list of namespaces for which flows are always collected, regardless of the presence of `FlowCollectorSlice` in those namespaces. 

Note

The `namespacesAllowList` field supports regular expressions, such as `/openshift-.*/` to capture multiple namespaces, or strict equality, such as `netobserv`, to match a specific namespace. 

  3. Save the changes and exit the editor. 



**Verification**

  * Verify that only network flows from the `netobserv` namespace and namespaces starting with `openshift-` are displayed in the **Network Traffic** page of the web console. 



## 7.3.1. Disable the Network Observability Operator FlowCollectorSlice

Disable slice-based filtering in the Network Observability Operator to resume global flow collection while preserving existing `FlowCollectorSlice` resources. 

**Procedure**

  1. Edit the `FlowCollector` resource by running the following command: 

```shell-session
$ oc edit flowcollector cluster
```


  2. Set the `spec.processor.slicesConfig.collectionMode` field to `AlwaysCollect`: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    slicesConfig:
      enable: true
      collectionMode: AlwaysCollect
      ...
```


  3. Save the changes. 

Flow collection resumes for all traffic, and existing `FlowCollectorSlice` resources remain available for future use.
