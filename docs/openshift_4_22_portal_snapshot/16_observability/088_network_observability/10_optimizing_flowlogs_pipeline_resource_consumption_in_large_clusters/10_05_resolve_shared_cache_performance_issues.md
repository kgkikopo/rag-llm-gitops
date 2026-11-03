# 10.5. Resolve shared cache performance issues

Troubleshoot shared cache component failures by verifying pod health, reviewing system logs, and confirming leader election status to restore cluster performance. 

**Prerequisites**

  * You have installed the Network Observability Operator. 
  * You have access to the cluster as a user with the `cluster-admin` role. 
  * The shared cache architecture is enabled in your `FlowCollector` configuration. 



**Procedure**

  1. Check the status of the shared cache pods by running the following command: 

```shell-session
$ oc get pods -n netobserv -l app=flowlogs-pipeline-informers
```


**Example output**

```shell-session
NAME                             READY   STATUS    RESTARTS   AGE
flowlogs-pipeline-informers-7d9f8b5c4d-abc12   1/1     Running   0          5m
flowlogs-pipeline-informers-7d9f8b5c4d-xyz34   1/1     Running   0          5m
```


Ensure all pods show `Running` status. If pods are in `CrashLoopBackOff` or `Error` status, proceed to examine the logs. 

  2. Identify the current leader pod: 

```shell-session
$ oc logs -n netobserv -l app=flowlogs-pipeline-informers --tail=50 | grep -i "leader"
```


Look for log entries indicating leader election status. Ensure that only one pod reports itself as the active leader. 

  3. View detailed logs from the leader pod to diagnose issues: 

```shell-session
$ oc logs -n netobserv <flowlogs_pipeline_informers_pod_name>
```


Common issues to look for: 

     * **API server connection failures** : Error messages indicating inability to connect to the Kubernetes API server suggest network or RBAC permission issues. 
     * **gRPC communication errors** : Messages about failed connections on port `9402` indicate `flowlogs-pipeline` instances cannot reach the shared cache. 
     * **Leader election conflicts** : If multiple pods claim to be the leader, there might be a configuration issue with leader election. 

  4. Verify that `flowlogs-pipeline` instances are receiving cache updates: 

```shell-session
$ oc logs -n netobserv -l app=flowlogs-pipeline --tail=100 | grep -i "k8scache"
```


`flowlogs-pipeline` pods show successful connection messages to the shared cache on port `9402`. 

  5. Check the shared cache service: 

```shell-session
$ oc get svc -n netobserv flowlogs-pipeline-k8scache
```


Verify that the service exists and is routing to the correct pods. 

  6. If the shared cache is not functioning correctly, check for RBAC permission issues: 

```shell-session
$ oc describe clusterrolebinding netobserv-informers
```


The `ClusterRoleBinding` grants the `flowlogs-pipeline-informers` `ServiceAccount` the necessary permissions to watch Kubernetes resources. 




**Verification**

  1. After you resolve issues, complete the following verification steps: 

     * Confirm all shared cache pods are running and healthy. 
     * Verify that one pod shows as the active leader in the logs. 
     * Check that `flowlogs-pipeline` pods successfully connect to the shared cache. 
     * Monitor flow enrichment in the network observability console to ensure metadata is displayed correctly on network flows. 




**Additional resources**

  * [Kubernetes leader election and leases](https://kubernetes.io/docs/concepts/architecture/leases/)
