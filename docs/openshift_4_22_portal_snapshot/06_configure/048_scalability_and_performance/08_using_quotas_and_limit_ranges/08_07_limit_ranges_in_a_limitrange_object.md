# 8.7. Limit ranges in a LimitRange object

To define compute resource constraints at the object level, create a `LimitRange` object. By creating this object, you can specify the exact amount of resources that an individual pod, container, image, image stream, or persistent volume claim can consume. 

All requests to create and modify resources are evaluated against each `LimitRange` object in the project. If the resource violates any of the enumerated constraints, the resource is rejected. If the resource does not set an explicit value, and if the constraint supports a default value, the default value is applied to the resource. 

For CPU and memory limits, if you specify a maximum value but do not specify a minimum limit, the resource can consume more CPU and memory resources than the maximum value. 

**Core limit range object definition**

```yaml
apiVersion: "v1"
kind: "LimitRange"
metadata:
  name: "core-resource-limits"
spec:
  limits:
    - type: "Pod"
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "200m"
        memory: "6Mi"
    - type: "Container"
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "100m"
        memory: "4Mi"
      default:
        cpu: "300m"
        memory: "200Mi"
      defaultRequest:
        cpu: "200m"
        memory: "100Mi"
      maxLimitRequestRatio:
        cpu: "10"
# ...
```


where: 

`metadata.name`
     Specifies the name of the limit range object. 
`max.cpu`
     Specifies the maximum amount of CPU that a pod can request on a node across all containers. 
`max.memory`
     Specifies the maximum amount of memory that a pod can request on a node across all containers. 
`min.cpu`
     Specifies the minimum amount of CPU that a pod can request on a node across all containers. If you do not set a `min` value or you set `min` to `0`, the result is no limit and the pod can consume more than the `max` CPU value. 
`min.memory`
     Specifies the minimum amount of memory that a pod can request on a node across all containers. If you do not set a `min` value or you set `min` to `0`, the result is no limit and the pod can consume more than the `max` memory value. 
`max.cpu`
     Specifies the maximum amount of CPU that a single container in a pod can request. 
`max.memory`
     Specifies the maximum amount of memory that a single container in a pod can request. 
`min.cpu`
     Specifies the minimum amount of CPU that a single container in a pod can request. If you do not set a `min` value or you set `min` to `0`, the result is no limit and the pod can consume more than the `max` CPU value. 
`max.memory`
     Specifies the minimum amount of memory that a single container in a pod can request. If you do not set a `min` value or you set `min` to `0`, the result is no limit and the pod can consume more than the `max` memory value. 
`default.cpu`
     Specifies the default CPU limit for a container if you do not specify a limit in the pod specification. 
`default.memory`
     Specifies the default memory limit for a container if you do not specify a limit in the pod specification. 
`defaultRequest.cpu`
     Specifies the default CPU request for a container if you do not specify a request in the pod specification. 
`defaultRequest.memory`
     Specifies the default memory request for a container if you do not specify a request in the pod specification. 
`maxLimitRequestRatio.cpu`
     Specifies the maximum limit-to-request ratio for a container. 

**OpenShift Container Platform Limit range object definition**

```yaml
apiVersion: "v1"
kind: "LimitRange"
metadata:
  name: "openshift-resource-limits"
spec:
  limits:
    - type: openshift.io/Image
      max:
        storage: 1Gi
    - type: openshift.io/ImageStream
      max:
        openshift.io/image-tags: 20
        openshift.io/images: 30
    - type: "Pod"
      max:
        cpu: "2"
        memory: "1Gi"
        ephemeral-storage: "1Gi"
      min:
        cpu: "1"
        memory: "1Gi"
# ...
```


where: 

`limits.max.storage`
     Specifies the maximum size of an image that can be pushed to an internal registry. 
`limits.max.openshift.io/image-tags`
     Specifies the maximum number of unique references counted from tag definitions in the `imagestream.spec.tags` resource. 
`limits.max.openshift.io/images`
     Specifies the maximum number of unique image identities, or digests, recorded in the `imagestream.status.tags` resource. 
`type.max.cpu`
     Specifies the maximum amount of CPU that a pod can request on a node across all containers. 
`type.max.memory`
     Specifies the maximum amount of memory that a pod can request on a node across all containers. 
`type.max.ephemeral-storage`
     Specifies the maximum amount of ephemeral storage that a pod can request on a node across all containers. 
`min.cpu`
     Specifies the minimum amount of CPU that a pod can request on a node across all containers. See the Supported Constraints table for important information. 
`min.memory`
     Specifies the minimum amount of memory that a pod can request on a node across all containers. If you do not set a `min` value or you set `min` to `0`, the result is no limit and the pod can consume more than the `max` memory value. 

You can specify both core and OpenShift Container Platform resources in one limit range object. 

## 8.7.1. Container limits

After you create the `LimitRange` object, you can specify the exact amount of resources that a container can consume. 

The following list shows resources that a container can consume: 

  * CPU 
  * Memory 



The following table shows the supported constraints for a container. If specified, the constraints must hold true for each container. 

Table 8.4. Supported constraintsConstraint| Behavior  
---|---  
`Min` |  `Min[<resource>]` less than or equal to `container.resources.requests[<resource>]` (required) less than or equal to `container/resources.limits[<resource>]` (optional)  If the configuration defines a `min` CPU, the request value must be greater than the CPU value. If you do not set a `min` value or you set `min` to `0`, the result is no limit and the pod can consume more of the resource than the `max` value.   
`Max` |  `container.resources.limits[<resource>]` (required) less than or equal to `Max[<resource>]` If the configuration defines a `max` CPU, you do not need to define a CPU request value. However, you must set a limit that satisfies the maximum CPU constraint that is specified in the limit range.   
`MaxLimitRequestRatio` |  `MaxLimitRequestRatio[<resource>]` less than or equal to (`container.resources.limits[<resource>]` / `container.resources.requests[<resource>]`)  If the limit range defines a `maxLimitRequestRatio` constraint, any new containers must have both a `request` and a `limit` value. Additionally, OpenShift Container Platform calculates a limit-to-request ratio by dividing the `limit` by the `request`. The result should be an integer greater than 1.  For example, if a container has `cpu: 500` in the `limit` value, and `cpu: 100` in the `request` value, the limit-to-request ratio for `cpu` is `5`. This ratio must be less than or equal to the `maxLimitRequestRatio`.   
Show more

The following list shows default resources that a container can consume: 

  * `Default[<resource>]`: Defaults `container.resources.limit[<resource>]` to specified value if none. 
  * `Default Requests[<resource>]`: Defaults `container.resources.requests[<resource>]` to specified value if none. 



## 8.7.2. Pod limits

After you create the `LimitRange` object, you can specify the exact amount of resources that a pod can consume. 

A pod can consume the following resources: 

  * CPU 
  * Memory 



The following table shows the supported constraints for a pod. Across all pods, the following behavior must hold true: 

Constraint| Enforced behavior  
---|---  
`Min` |  `Min[<resource>]` less than or equal to `container.resources.requests[<resource>]` (required) less than or equal to `container.resources.limits[<resource>]`. If you do not set a `min` value or you set `min` to `0`, the result is no limit and the pod can consume more of the resource than the `max` value.   
`Max` |  `container.resources.limits[<resource>]` (required) less than or equal to `Max[<resource>]`.   
`MaxLimitRequestRatio` |  `MaxLimitRequestRatio[<resource>]` less than or equal to (`container.resources.limits[<resource>]` / `container.resources.requests[<resource>]`).   
Show more

## 8.7.3. Image limits

After you create the `LimitRange` object, you can specify the exact amount of resources that an image can consume. 

An image can consume the following resources: 

  * Storage 
  * `openshift.io/Image`



The following table shows the supported constraints for an image. If specified, the constraints must hold true for each image. 

Table 8.5. Image limitsConstraint| Behavior  
---|---  
`Max` |  `image.dockerimagemetadata.size` less than or equal to `Max[<resource>]`  
Show more

Note

To prevent blobs that exceed the limit from being uploaded to the registry, you must configure the registry to enforce quota. The `REGISTRY_MIDDLEWARE_REPOSITORY_OPENSHIFT_ENFORCEQUOTA` environment variable must be set to `true`. By default, the environment variable is set to `true` for new deployments. 

## 8.7.4. Image stream limits

After you create the `LimitRange` object, you can specify the exact amount of resources that an image stream can consume. 

An image stream can consume the following resources: 

  * `openshift.io/image-tags`
  * `openshift.io/images`
  * `openshift.io/ImageStream`



The `openshift.io/image-tags` limit bounds unique references derived from tag definitions in the `imagestream.spec.tags` resource. A reference can be an `ImageStreamTag`, an `ImageStreamImage`, or a `DockerImage`. You can use the `oc tag` and `oc import-image` commands to create tags. Internal and external references are not distinguished, and each unique reference in the spec is counted once. Updates that would exceed the limit are rejected, including updates from pushes to the internal registry that add or change tag definitions. 

The `openshift.io/images` limit bounds unique image identities recorded in `imagestream.status.tags`. The name is equivalent to the digest for the image. It limits how many distinct images the stream can reference in status, including from registry pushes. Internal and external references are not distinguished. 

Important

Do not read `openshift.io/image-tags` and `openshift.io/images` as "tag names versus images per tag." The first limit is computed from the `ImageStream` `spec.tags` resource. The second is computed from the `imagestream.status.tags` resource. Both limits can cause image stream updates to fail when a push or other operation would exceed them. 

The following table shows the supported constraints for an image stream. If specified, the constraints must hold true for each image stream. 

Constraint| Behavior  
---|---  
`Max[openshift.io/image-tags]` |  `length( uniqueimagetags( imagestream.spec.tags ) )` less than or equal to `Max[openshift.io/image-tags]` `uniqueimagetags` returns unique references to images of given spec tags.   
`Max[openshift.io/images]` |  `length( uniqueimages( imagestream.status.tags ) )` less than or equal to `Max[openshift.io/images]` `uniqueimages` returns unique image names found in status tags. The name is equal to the digest for the image.   
Show more

## 8.7.5. PersistentVolumeClaim limits

After you create the `LimitRange` object, you can specify the exact amount of resources that a `PersistentVolumeClaim` resource can consume. 

A `PersistentVolumeClaim` resource can consume storage resources. 

The following table shows the supported constraints for a persistent volume claim. If specified, the constraints must hold true for each persistent volume claim. 

Table 8.6. PersistentVolumeClaim resource limitsConstraint| Enforced behavior  
---|---  
`Min` |  Min[<resource>] <= claim.spec.resources.requests[<resource>] (required)   
`Max` |  claim.spec.resources.requests[<resource>] (required) <= Max[<resource>]   
Show more

**Limit range object definition example**

```plaintext
{
  "apiVersion": "v1",
  "kind": "LimitRange",
  "metadata": {
    "name": "pvcs"
  },
  "spec": {
    "limits": [{
        "type": "PersistentVolumeClaim",
        "min": {
          "storage": "2Gi"
        },
        "max": {
          "storage": "50Gi"
        }
      }
    ]
  }
}
```


where: 

`metadata.name`
     Specifies the name of the limit range object. 
`limits.min.storage`
     Specifies the minimum amount of storage that can be requested in a persistent volume claim. 
`limits.max.storage`
     Specifies the maximum amount of storage that can be requested in a persistent volume claim.
