# 2.5. Access the Cluster Samples Operator configuration

You can configure the Cluster Samples Operator by editing the file with the provided parameters. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 



**Procedure**

  * Access the Cluster Samples Operator configuration by running the following command: 

```shell-session
$ oc edit configs.samples.operator.openshift.io/cluster
```


The Cluster Samples Operator configuration resembles the following example: 

```yaml
apiVersion: samples.operator.openshift.io/v1
kind: Config
# ...
```
