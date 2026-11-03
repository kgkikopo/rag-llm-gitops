# 9.5. Pruning builds

By default, builds that have completed their lifecycle are persisted indefinitely. You can limit the number of previous builds that are retained. 

**Procedure**

  1. Limit the number of previous builds that are retained by supplying a positive integer value for `successfulBuildsHistoryLimit` or `failedBuildsHistoryLimit` in your `BuildConfig`, for example: 

```yaml
apiVersion: "v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  successfulBuildsHistoryLimit: 2 
```


1

```yaml
  failedBuildsHistoryLimit: 2 
```


2

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/advanced-build-operations#CO26-1)
    

`successfulBuildsHistoryLimit` will retain up to two builds with a status of `completed`. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/advanced-build-operations#CO26-2)
    

`failedBuildsHistoryLimit` will retain up to two builds with a status of `failed`, `canceled`, or `error`. 

  2. Trigger build pruning by one of the following actions: 

     * Updating a build configuration. 
     * Waiting for a build to complete its lifecycle. 




Builds are sorted by their creation timestamp with the oldest builds being pruned first. 

Note

Administrators can manually prune builds using the 'oc adm' object pruning command.
