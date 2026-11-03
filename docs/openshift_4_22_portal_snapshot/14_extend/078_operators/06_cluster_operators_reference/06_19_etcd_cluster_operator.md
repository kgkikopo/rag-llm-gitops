# 6.19. etcd cluster Operator

The etcd cluster Operator automates etcd cluster scaling, enables etcd monitoring and metrics, and simplifies disaster recovery procedures. 

## 6.19.1. CRDs

  * `etcds.operator.openshift.io`

    * Scope: Cluster 
    * CR: `etcd`
    * Validation: Yes 




## 6.19.2. Configuration objects

```shell-session
$ oc edit etcd cluster
```


**Additional resources**

  * [cluster-etcd-operator](https://github.com/openshift/cluster-etcd-operator/)
