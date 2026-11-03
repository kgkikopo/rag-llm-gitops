# 9.3. Assigning builds to specific nodes

Builds can be targeted to run on specific nodes by specifying labels in the `nodeSelector` field of a build configuration. The `nodeSelector` value is a set of key-value pairs that are matched to `Node` labels when scheduling the build pod. 

The `nodeSelector` value can also be controlled by cluster-wide default and override values. Defaults will only be applied if the build configuration does not define any key-value pairs for the `nodeSelector` and also does not define an explicitly empty map value of `nodeSelector:{}`. Override values will replace values in the build configuration on a key by key basis. 

Note

If the specified `NodeSelector` cannot be matched to a node with those labels, the build still stay in the `Pending` state indefinitely. 

**Procedure**

  * Assign builds to run on specific nodes by assigning labels in the `nodeSelector` field of the `BuildConfig`, for example: 

```yaml
apiVersion: "v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  nodeSelector:
```


1

```yaml
    key1: value1
    key2: value2
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/advanced-build-operations#CO24-1)
    

Builds associated with this build configuration will run only on nodes with the `key1=value2` and `key2=value2` labels.
