# 3.4. Enable the cluster capabilities by setting baseline capability set

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `baselineCapabilitySet` configuration parameter. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * To set the `baselineCapabilitySet` configuration parameter, run the following command: 

```shell-session
$ oc patch clusterversion version --type merge -p '{"spec":{"capabilities":{"baselineCapabilitySet":"vCurrent"}}}'
```


For `baselineCapabilitySet` you can specify `vCurrent`, `v4.22`, or `None`.
