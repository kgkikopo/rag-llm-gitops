# 9.1. Setting build resources

By default, builds are completed by pods using unbound resources, such as memory and CPU. These resources can be limited. 

**Procedure**

You can limit resource use in two ways: 

  * Limit resource use by specifying resource limits in the default container limits of a project. 
  * Limit resource use by specifying resource limits as part of the build configuration. 

    * In the following example, each of the `resources`, `cpu`, and `memory` parameters are optional: 

```yaml
apiVersion: "v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  resources:
    limits:
      cpu: "100m" 
```


1

```yaml
      memory: "256Mi" 
```


2

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/advanced-build-operations#CO22-1)
    

`cpu` is in CPU units: `100m` represents 0.1 CPU units (100 * 1e-3). 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/advanced-build-operations#CO22-2)
    

`memory` is in bytes: `256Mi` represents 268435456 bytes (256 * 2 ^ 20). 

However, if a quota has been defined for your project, one of the following two items is required: 

      * A `resources` section set with an explicit `requests`: 

```yaml
resources:
  requests: 
```


1

```yaml
    cpu: "100m"
    memory: "256Mi"
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/advanced-build-operations#CO23-1)
    

The `requests` object contains the list of resources that correspond to the list of resources in the quota. 

      * A limit range defined in your project, where the defaults from the `LimitRange` object apply to pods created during the build process. 

Otherwise, build pod creation will fail, citing a failure to satisfy quota.
