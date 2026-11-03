# 8.6. View Ingress Controller logs

You can view your Ingress Controller logs by using the `oc logs` command. 

**Procedure**

  * View your Ingress Controller logs: 

```shell-session
$ oc logs --namespace=openshift-ingress-operator deployments/ingress-operator -c <container_name>
```
