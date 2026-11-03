# 6.5. View Cluster Network Operator logs

You can view Cluster Network Operator logs by using the `oc logs` command. 

**Procedure**

  * Run the following command to view the logs of the Cluster Network Operator: 

```shell-session
$ oc logs --namespace=openshift-network-operator deployment/network-operator
```
