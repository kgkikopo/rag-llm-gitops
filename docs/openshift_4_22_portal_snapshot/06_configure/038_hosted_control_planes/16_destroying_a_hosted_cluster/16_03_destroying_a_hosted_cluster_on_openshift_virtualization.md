# 16.3. Destroying a hosted cluster on OpenShift Virtualization

You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve. 

## 16.3.1. Destroying a hosted cluster on OpenShift Virtualization by using the CLI

You can use the command-line interface (CLI) to destroy a hosted cluster and its managed cluster resource on OpenShift Virtualization. 

**Procedure**

  1. Delete the managed cluster resource on multicluster engine Operator by running the following command: 

```shell-session
$ oc delete managedcluster <hosted_cluster_name>
```


  2. Delete the hosted cluster and its backend resources by running the following command: 

```shell-session
$ hcp destroy cluster kubevirt --name <hosted_cluster_name>
```
