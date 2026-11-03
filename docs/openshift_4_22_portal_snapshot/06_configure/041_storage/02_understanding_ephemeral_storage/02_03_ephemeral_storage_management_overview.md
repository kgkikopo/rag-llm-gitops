# 2.3. Ephemeral storage management overview

Cluster administrators can manage ephemeral storage within a project by setting quotas that define limit ranges and request counts for all pods in a non-terminal state. Developers can also set requests and limits on this resource at the pod and container level. 

You can manage local ephemeral storage by specifying requests and limits. Each container in a pod can specify the following: 

  * `spec.containers[].resources.limits.ephemeral-storage`
  * `spec.containers[].resources.requests.ephemeral-storage`



## 2.3.1. Ephemeral storage management limits and requests

Express ephemeral storage limits and requests using byte quantities with suffixes like G, M, K or power-of-two equivalents Gi, Mi, Ki. Pod-level limits aggregate all container limits plus `emptyDir` volumes, enabling proper scheduling and preventing pods from exhausting node storage. 

Limits and requests for ephemeral storage are measured in byte quantities. You can express storage as a plain integer or as a fixed-point number by using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. For example, the following quantities all represent approximately the same value: 128974848, 129e6, 129M, and 123Mi. Pod-level limits aggregate all container limits plus `emptyDir` volumes, enabling proper scheduling and preventing pods from exhausting node storage. 

Important

The suffixes for each byte quantity are case-sensitive. Be sure to use the correct case. Use the case-sensitive "M", such as used in "400M", to set the request at 400 megabytes. Use the case-sensitive "400Mi" to request 400 mebibytes. If you specify "400m" of ephemeral storage, the storage request is only 0.4 bytes. 

The following example configuration file shows a pod with two containers: 

  * Each container requests 2GiB of local ephemeral storage. 
  * Each container has a limit of 4GiB of local ephemeral storage. 
  * At the pod level, kubelet works out an overall pod storage limit by adding up the limits of all the containers in that pod. 

    * In this case, the total storage usage at the pod level is the sum of the disk usage from all containers plus the `emptyDir` volumes of a pod. 
    * Therefore, the pod has a request of 4GiB of local ephemeral storage, and a limit of 8GiB of local ephemeral storage. 




**Example ephemeral storage configuration with quotas and limits**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      requests:
        ephemeral-storage: "2Gi"
      limits:
        ephemeral-storage: "4Gi"
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    resources:
      requests:
        ephemeral-storage: "2Gi"
      limits:
        ephemeral-storage: "4Gi"
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  volumes:
    - name: ephemeral
      emptyDir: {}
```


  * `spec.containers.name.resources.requests.ephemeral-storage`: Specifies the container request for local ephemeral storage. 
  * `spec.containers.name.resources.limits.ephemeral-storage`: Specifies the container limit for local ephemeral storage. 



**Additional resources**

  * [Resources managed by quotas](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#quotas-setting-per-project_quotas-setting-per-project)



## 2.3.2. Ephemeral storage management configuration affects pod scheduling and eviction

Configure ephemeral storage requests and limits in the pod spec to control how the scheduler places pods on nodes and when kubelet evicts pods that exceed their allocated storage. 

  * First, the scheduler ensures that the sum of the resource requests of the scheduled containers is less than the capacity of the node. In this case, the pod can be assigned to a node only if the node’s available ephemeral storage (allocatable resource) is more than 4GiB. 
  * Second, at the container level, because the first container sets a resource limit, kubelet eviction manager measures the disk usage of this container and evicts the pod if the storage usage of the container exceeds its limit (4GiB). The kubelet eviction manager also marks the pod for eviction if the total usage exceeds the overall pod storage limit (8GiB).
