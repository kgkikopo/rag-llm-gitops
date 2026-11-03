# 15.5. Disable transparent huge pages

If your application can handle huge pages on its own, you can disable transparent huge pages (THP) to optimally handle huge pages for all types of workloads and avoid the performance regressions that THP can cause. 

Disabling THP prevents them from attempting to automate most aspects of creating, managing, and using huge pages. You can disable THP by using the Node Tuning Operator (NTO). 

**Procedure**

  1. Create a file with the following content and name it `thp-disable-tuned.yaml`: 

```yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: thp-workers-profile
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Custom tuned profile for OpenShift to turn off THP on worker nodes
      include=openshift-node

      [vm]
      transparent_hugepages=never
    name: openshift-thp-never-worker

  recommend:
  - match:
    - label: node-role.kubernetes.io/worker
    priority: 25
    profile: openshift-thp-never-worker
# ...
```


  2. Create the Tuned object by entering the following command: 

```shell-session
$ oc create -f thp-disable-tuned.yaml
```


  3. Check the list of active profiles by entering the following command:: 

```shell-session
$ oc get profile -n openshift-cluster-node-tuning-operator
```


**Verification**

  * Log in to one of the nodes and do a regular THP check to verify if the nodes applied the profile successfully: 

```shell-session
$ cat /sys/kernel/mm/transparent_hugepage/enabled
```


**Example output**

```shell-session
always madvise [never]
```
