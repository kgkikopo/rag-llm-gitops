# 15.3. Consume huge pages resources using the Downward API

To inject information about the huge pages resources consumed by a container, use the Downward API. 

You can inject the resource allocation as environment variables, a volume plugin, or both. Applications that you develop and run in the container can determine the resources that are available by reading the environment variables or files in the specified volumes. 

**Procedure**

  1. Create a `hugepages-volume-pod.yaml` file that is similar to the following example: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  generateName: hugepages-volume-
  labels:
    app: hugepages-example
spec:
  containers:
  - securityContext:
      capabilities:
        add: [ "IPC_LOCK" ]
    image: rhel7:latest
    command:
    - sleep
    - inf
    name: example
    volumeMounts:
    - mountPath: /dev/hugepages
      name: hugepage
    - mountPath: /etc/podinfo
      name: podinfo
    resources:
      limits:
        hugepages-1Gi: 2Gi
        memory: "1Gi"
        cpu: "1"
      requests:
        hugepages-1Gi: 2Gi
    env:
    - name: REQUESTS_HUGEPAGES_1GI
      valueFrom:
        resourceFieldRef:
          containerName: example
          resource: requests.hugepages-1Gi
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
  - name: podinfo
    downwardAPI:
      items:
        - path: "hugepages_1G_request"
          resourceFieldRef:
            containerName: example
            resource: requests.hugepages-1Gi
            divisor: 1Gi
```


where: 

`spec.containers.securityContext.env.name`
     Specifies what resource to read and use from `requests.hugepages-1Gi` and expose the value as the `REQUESTS_HUGEPAGES_1GI` environment variable. 
`spec.volumes.name.items.path`
     Specifies what resource to read and use from `requests.hugepages-1Gi` and expose the value as the file `/etc/podinfo/hugepages_1G_request`. 

  2. Create the pod from the `hugepages-volume-pod.yaml` file by entering the following command: 

```shell-session
$ oc create -f hugepages-volume-pod.yaml
```


**Verification**

  1. Check the value of the `REQUESTS_HUGEPAGES_1GI` environment variable: 

```shell-session
$ oc exec -it $(oc get pods -l app=hugepages-example -o jsonpath='{.items[0].metadata.name}') \
     -- env | grep REQUESTS_HUGEPAGES_1GI
```


**Example output**

```shell-session
REQUESTS_HUGEPAGES_1GI=2147483648
```


  2. Check the value of the `/etc/podinfo/hugepages_1G_request` file: 

```shell-session
$ oc exec -it $(oc get pods -l app=hugepages-example -o jsonpath='{.items[0].metadata.name}') \
     -- cat /etc/podinfo/hugepages_1G_request
```


**Example output**

```shell-session
2
```


**Additional resources**

  * [Allowing containers to consume Downward API objects](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-containers-downward-api)
