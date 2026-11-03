# 5.8. Monitoring the managed cluster installation status

Ensure that cluster provisioning was successful by checking the cluster status. 

**Prerequisites**

  * All of the custom resources have been configured and provisioned, and the `Agent` custom resource is created on the hub for the managed cluster. 



**Procedure**

  1. Check the status of the managed cluster: 

```shell-session
$ oc get managedcluster
```


`True` indicates the managed cluster is ready. 

  2. Check the agent status: 

```shell-session
$ oc get agent -n <cluster_name>
```


  3. Use the `describe` command to provide an in-depth description of the agent’s condition. Statuses to be aware of include `BackendError`, `InputError`, `ValidationsFailing`, `InstallationFailed`, and `AgentIsConnected`. These statuses are relevant to the `Agent` and `AgentClusterInstall` custom resources. 

```shell-session
$ oc describe agent -n <cluster_name>
```


  4. Check the cluster provisioning status: 

```shell-session
$ oc get agentclusterinstall -n <cluster_name>
```


  5. Use the `describe` command to provide an in-depth description of the cluster provisioning status: 

```shell-session
$ oc describe agentclusterinstall -n <cluster_name>
```


  6. Check the status of the managed cluster’s add-on services: 

```shell-session
$ oc get managedclusteraddon -n <cluster_name>
```


  7. Retrieve the authentication information of the `kubeconfig` file for the managed cluster: 

```shell-session
$ oc get secret -n <cluster_name> <cluster_name>-admin-kubeconfig -o jsonpath={.data.kubeconfig} | base64 -d > <directory>/<cluster_name>-kubeconfig
```
