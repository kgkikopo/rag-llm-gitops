# 4.8. Monitor managed cluster installation progress

You can monitor managed cluster installation progress from the RHACM dashboard or from the command line after the Argo CD pipeline syncs the `ClusterInstance` CR to the hub cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 



**Procedure**

  1. Monitor the progress of cluster installation by running the following commands: 

     1. Export the cluster name: 

```shell-session
$ export CLUSTER=<clusterName>
```


     2. Query the `AgentClusterInstall` CR for the managed cluster: 

```shell-session
$ oc get agentclusterinstall -n $CLUSTER $CLUSTER -o jsonpath='{.status.conditions[?(@.type=="Completed")]}' | jq
```


     3. Get the installation events for the cluster: 

```shell-session
$ curl -sk $(oc get agentclusterinstall -n $CLUSTER $CLUSTER -o jsonpath='{.status.debugInfo.eventsURL}')  | jq '.[-2,-1]'
```
