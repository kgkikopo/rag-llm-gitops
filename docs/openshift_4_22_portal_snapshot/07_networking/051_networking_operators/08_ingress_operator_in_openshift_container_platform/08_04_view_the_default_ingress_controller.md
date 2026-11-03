# 8.4. View the default Ingress Controller

The Ingress Operator is a core feature of OpenShift Container Platform and is enabled out of the box. 

Every new OpenShift Container Platform installation has an `ingresscontroller` named default. It can be supplemented with additional Ingress Controllers. If the default `ingresscontroller` is deleted, the Ingress Operator will automatically recreate it within a minute. 

**Procedure**

  * View the default Ingress Controller: 

```shell-session
$ oc describe --namespace=openshift-ingress-operator ingresscontroller/default
```
