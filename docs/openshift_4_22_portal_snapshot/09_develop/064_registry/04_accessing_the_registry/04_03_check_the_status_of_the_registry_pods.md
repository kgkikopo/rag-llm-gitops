# 4.3. Check the status of the registry pods

As a cluster administrator, you can list the image registry pods running in the `openshift-image-registry` project and check their status. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * List the pods in the `openshift-image-registry` project and view their status. Example output provided for demonstrative purposes. 

```shell-session
$ oc get pods -n openshift-image-registry
```


```shell-session
NAME READY STATUS RESTARTS AGE
image-registry-79fb4469f6-llrln 1/1 Running 0 77m
node-ca-hjksc 1/1 Running 0 73m
node-ca-tftj6 1/1 Running 0 77m
node-ca-wb6ht 1/1 Running 0 77m
node-ca-zvt9q 1/1 Running 0 74m
```
