# 2.8. Creating the OpenShift Container Platform manifests

Create manifest files to begin customizing your cluster installation. 

**Procedure**

  * Create the OpenShift Container Platform manifests by running the following command: 

```shell-session
$ ./openshift-baremetal-install --dir ~/clusterconfigs create manifests
```


**Example output**

```shell-session
INFO Consuming Install Config from target directory
WARNING Making control-plane schedulable by setting MastersSchedulable to true for Scheduler cluster settings
WARNING Discarding the OpenShift Manifest that was provided in the target directory because its dependencies are dirty and it needs to be regenerated
```
