# 6.22. Kubernetes API Server Operator

The Kubernetes API Server Operator manages and updates the Kubernetes API server deployed on top of OpenShift Container Platform. The Operator is based on the OpenShift Container Platform `library-go` framework and it is installed using the Cluster Version Operator (CVO). 

## 6.22.1. CRDs

  * `kubeapiservers.operator.openshift.io`

    * Scope: Cluster 
    * CR: `kubeapiserver`
    * Validation: Yes 




## 6.22.2. Configuration objects

```shell-session
$ oc edit kubeapiserver
```


**Additional resources**

  * [`openshift-kube-apiserver-operator`](https://github.com/openshift/cluster-kube-apiserver-operator)
