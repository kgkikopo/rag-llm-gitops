# 14.1. Disable multicast between pods

To disable multicast between pods in a project, you can remove the `k8s.ovn.org/multicast-enabled` annotation from the namespace by using the `oc annotate` command or a namespace manifest. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * You must log in to the cluster with a user that has the `cluster-admin` role. 



**Procedure**

  * Disable multicast by running the following command: 

```shell-session
$ oc annotate namespace <namespace> \
    k8s.ovn.org/multicast-enabled-
```


For `<namespace>`, specify the namespace for the project you want to disable multicast for. 

Tip

You can alternatively apply the following YAML to delete the annotation: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: <namespace>
  annotations:
    k8s.ovn.org/multicast-enabled: null
```
