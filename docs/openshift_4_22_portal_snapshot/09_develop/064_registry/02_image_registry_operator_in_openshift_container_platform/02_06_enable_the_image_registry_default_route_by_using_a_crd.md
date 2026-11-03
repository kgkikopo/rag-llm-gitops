# 2.6. Enable the Image Registry default route by using a CRD

In OpenShift Container Platform, the `Registry` Operator controls the OpenShift image registry feature by using the `configs.imageregistry.operator.openshift.io` CRD. Patch this CRD to automatically enable the Image Registry default route. 

**Procedure**

  * Patch the Image Registry Operator CRD: 

```shell-session
$ oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
```
