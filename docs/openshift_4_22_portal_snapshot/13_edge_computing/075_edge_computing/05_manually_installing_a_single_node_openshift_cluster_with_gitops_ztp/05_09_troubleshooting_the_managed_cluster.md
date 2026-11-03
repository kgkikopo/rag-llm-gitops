# 5.9. Troubleshooting the managed cluster

Use this procedure to diagnose any installation issues that might occur with the managed cluster. 

**Procedure**

  1. Check the status of the managed cluster: 

```shell-session
$ oc get managedcluster
```


**Example output**

```shell-session
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED   AVAILABLE   AGE
SNO-cluster     true                                   True     True      2d19h
```


If the status in the `AVAILABLE` column is `True`, the managed cluster is being managed by the hub. 

If the status in the `AVAILABLE` column is `Unknown`, the managed cluster is not being managed by the hub. Use the following steps to continue checking to get more information. 

  2. Check the `AgentClusterInstall` install status: 

```shell-session
$ oc get clusterdeployment -n <cluster_name>
```


**Example output**

```shell-session
NAME        PLATFORM            REGION   CLUSTERTYPE   INSTALLED    INFRAID    VERSION  POWERSTATE AGE
Sno0026    agent-baremetal                               false                          Initialized
2d14h
```


If the status in the `INSTALLED` column is `false`, the installation was unsuccessful. 

  3. If the installation failed, enter the following command to review the status of the `AgentClusterInstall` resource: 

```shell-session
$ oc describe agentclusterinstall -n <cluster_name> <cluster_name>
```


  4. Resolve the errors and reset the cluster: 

     1. Remove the cluster’s managed cluster resource: 

```shell-session
$ oc delete managedcluster <cluster_name>
```


     2. Remove the cluster’s namespace: 

```shell-session
$ oc delete namespace <cluster_name>
```


This deletes all of the namespace-scoped custom resources created for this cluster. You must wait for the `ManagedCluster` CR deletion to complete before proceeding. 

     3. Recreate the custom resources for the managed cluster.
