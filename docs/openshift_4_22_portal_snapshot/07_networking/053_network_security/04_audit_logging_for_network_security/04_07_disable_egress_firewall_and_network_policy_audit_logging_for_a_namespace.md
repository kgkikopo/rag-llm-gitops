# 4.7. Disable egress firewall and network policy audit logging for a namespace

To disable egress firewall and network policy audit logging for a namespace in OpenShift Container Platform, you can remove the `k8s.ovn.org/acl-logging` annotation with the `oc annotate` command. You can also apply a namespace YAML file that sets the annotation to `null`. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in to the cluster with a user with `cluster-admin` privileges. 



**Procedure**

  * To disable audit logging for a namespace, enter the following command: 

```shell-session
$ oc annotate --overwrite namespace <namespace> k8s.ovn.org/acl-logging-
```


where: 

`<namespace>`
     Specifies the name of the namespace. 

Tip

You can also apply the following YAML to disable audit logging: 

```yaml
kind: Namespace
apiVersion: v1
metadata:
  name: <namespace>
  annotations:
    k8s.ovn.org/acl-logging: null
```


Successful output lists the audit logging name and the `annotated` status.
