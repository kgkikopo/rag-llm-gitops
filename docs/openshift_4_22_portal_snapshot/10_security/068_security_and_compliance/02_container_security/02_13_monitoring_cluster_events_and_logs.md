# 2.13. Monitoring cluster events and logs

Monitoring and auditing an OpenShift Container Platform cluster is an important part of safeguarding the cluster and its users against inappropriate usage. There are two main sources of cluster-level information that are useful for this purpose: events and logging. 

## 2.13.1. Watch cluster events

Cluster administrators are encouraged to familiarize themselves with the `Event` resource type and review the list of system events to determine which events are of interest. 

Events are associated with a namespace, either the namespace of the resource they are related to or, for cluster events, the `default` namespace. The default namespace holds relevant events for monitoring or auditing a cluster, such as node events and resource events related to infrastructure components. 

The master API and `oc` command do not provide parameters to scope a listing of events to only those related to nodes. A simple approach would be to use `grep`: 

```shell-session
$ oc get event -n default | grep Node
```


**Example output**

```shell-session
1h         20h         3         origin-node-1.example.local   Node      Normal    NodeHasDiskPressure   ...
```


A more flexible approach is to output the events in a form that other tools can process. For example, the following example uses the `jq` tool against JSON output to extract only `NodeHasDiskPressure` events: 

```shell-session
$ oc get events -n default -o json \
  | jq '.items[] | select(.involvedObject.kind == "Node" and .reason == "NodeHasDiskPressure")'
```


**Example output**

```shell-session
{
  "apiVersion": "v1",
  "count": 3,
  "involvedObject": {
    "kind": "Node",
    "name": "origin-node-1.example.local",
    "uid": "origin-node-1.example.local"
  },
  "kind": "Event",
  "reason": "NodeHasDiskPressure",
  ...
}
```


Events related to resource creation, modification, or deletion can also be good candidates for detecting misuse of the cluster. The following query, for example, can be used to look for excessive pulling of images: 

```shell-session
$ oc get events --all-namespaces -o json \
  | jq '[.items[] | select(.involvedObject.kind == "Pod" and .reason == "Pulling")] | length'
```


**Example output**

```shell-session
4
```


Note

When a namespace is deleted, its events are deleted as well. Events can also expire and are deleted to prevent filling up etcd storage. Events are not stored as a permanent record and frequent polling is necessary to capture statistics over time. 

## 2.13.2. Logging

Using the `oc log` command, you can view container logs, build configs and deployments in real time. Different users can have access different access to logs: 

  * Users who have access to a project are able to see the logs for that project by default. 
  * Users with admin roles can access all container logs. 



To save your logs for further audit and analysis, you can enable the `cluster-logging` add-on feature to collect, manage, and view system, container, and audit logs. You can deploy, manage, and upgrade OpenShift Logging through the OpenShift Elasticsearch Operator and Red Hat OpenShift Logging Operator. 

## 2.13.3. Audit logs

With _audit logs_ , you can follow a sequence of activities associated with how a user, administrator, or other OpenShift Container Platform component is behaving. API audit logging is done on each server. 

**Additional resources**

  * [List of system events](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-containers-events)
  * [Viewing audit logs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/audit-log-view "Chapter 14. Viewing audit logs")
