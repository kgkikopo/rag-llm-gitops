# 6.31. OpenShift Controller Manager Operator

The OpenShift Controller Manager Operator installs and maintains the `OpenShiftControllerManager` custom resource in a cluster. 

```shell-session
$ oc get clusteroperator openshift-controller-manager -o yaml
```


The custom resource definition (CRD) `openshiftcontrollermanagers.operator.openshift.io` can be viewed in a cluster with: 

```shell-session
$ oc get crd openshiftcontrollermanagers.operator.openshift.io -o yaml
```


**Additional resources**

  * [cluster-openshift-controller-manager-operator](https://github.com/openshift/cluster-openshift-controller-manager-operator)
