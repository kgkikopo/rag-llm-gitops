# 13.7. Using the container image pre-cache feature

Single-node OpenShift clusters might have limited bandwidth to access the container image registry, which can cause a timeout before the updates are completed. 

Note

The time of the update is not set by TALM. You can apply the `ClusterGroupUpgrade` CR at the beginning of the update by manual application or by external automation. 

The container image pre-caching starts when the `preCaching` field is set to `true` in the `ClusterGroupUpgrade` CR. 

TALM uses the `PrecacheSpecValid` condition to report status information as follows: 

  * `true`

The pre-caching spec is valid and consistent. 

  * `false`

The pre-caching spec is incomplete. 




TALM uses the `PrecachingSucceeded` condition to report status information as follows: 

  * `true`

TALM has concluded the pre-caching process. If pre-caching fails for any cluster, the update fails for that cluster but proceeds for all other clusters. A message informs you if pre-caching has failed for any clusters. 

  * `false`

Pre-caching is still in progress for one or more clusters or has failed for all clusters. 




After a successful pre-caching process, you can start remediating policies. The remediation actions start when the `enable` field is set to `true`. If there is a pre-caching failure on a cluster, the upgrade fails for that cluster. The upgrade process continues for all other clusters that have a successful pre-cache. 

The pre-caching process can be in the following statuses: 

  * `NotStarted`

This is the initial state all clusters are automatically assigned to on the first reconciliation pass of the `ClusterGroupUpgrade` CR. In this state, TALM deletes any pre-caching namespace and hub view resources of spoke clusters that remain from previous incomplete updates. TALM then creates a new `ManagedClusterView` resource for the spoke pre-caching namespace to verify its deletion in the `PrecachePreparing` state. 

  * `PreparingToStart`

Cleaning up any remaining resources from previous incomplete updates is in progress. 

  * `Starting`

Pre-caching job prerequisites and the job are created. 

  * `Active`

The job is in "Active" state. 

  * `Succeeded`

The pre-cache job succeeded. 

  * `PrecacheTimeout`

The artifact pre-caching is partially done. 

  * `UnrecoverableError`

The job ends with a non-zero exit code. 




## 13.7.1. Using the container image pre-cache filter

The pre-cache feature typically downloads more images than a cluster needs for an update. You can control which pre-cache images are downloaded to a cluster. This decreases download time, and saves bandwidth and storage. 

You can see a list of all images to be downloaded using the following command: 

```shell-session
$ oc adm release info <ocp-version>
```


The following `ConfigMap` example shows how you can exclude images using the `excludePrecachePatterns` field. 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-group-upgrade-overrides
data:
  excludePrecachePatterns: |
    azure
    aws
    vsphere
    alibaba
```


TALM excludes all images with names that include any of the patterns listed here. 

## 13.7.2. Creating a ClusterGroupUpgrade CR with pre-caching

For single-node OpenShift, the pre-cache feature allows the required container images to be present on the spoke cluster before the update starts. 

Note

For pre-caching, TALM uses the `spec.remediationStrategy.timeout` value from the `ClusterGroupUpgrade` CR. You must set a `timeout` value that allows sufficient time for the pre-caching job to complete. When you enable the `ClusterGroupUpgrade` CR after pre-caching has completed, you can change the `timeout` value to a duration that is appropriate for the update. 

**Prerequisites**

  * Install the Topology Aware Lifecycle Manager (TALM). 
  * Provision one or more managed clusters. 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Save the contents of the `ClusterGroupUpgrade` CR with the `preCaching` field set to `true` in the `clustergroupupgrades-group-du.yaml` file: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: du-upgrade-4918
  namespace: ztp-group-du-sno
spec:
  preCaching: true
  clusters:
  - cnfdb1
  - cnfdb2
  enable: false
  managedPolicies:
  - du-upgrade-platform-upgrade
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
```


The `preCaching` field is set to `true`, which enables TALM to pull the container images before starting the update. 

  2. When you want to start pre-caching, apply the `ClusterGroupUpgrade` CR by running the following command: 

```shell-session
$ oc apply -f clustergroupupgrades-group-du.yaml
```


**Verification**

  1. Check if the `ClusterGroupUpgrade` CR exists in the hub cluster by running the following command: 

```shell-session
$ oc get cgu -A
```


Example output: 

```shell-session
NAMESPACE          NAME              AGE   STATE        DETAILS
ztp-group-du-sno   du-upgrade-4918   10s   InProgress   Precaching is required and not done
```


The CR is created. 

  2. Check the status of the pre-caching task by running the following command: 

```shell-session
$ oc get cgu -n ztp-group-du-sno du-upgrade-4918 -o jsonpath='{.status}'
```


Example output: 

```plaintext
{
  "conditions": [
    {
      "lastTransitionTime": "2022-01-27T19:07:24Z",
      "message": "Precaching is required and not done",
      "reason": "InProgress",
      "status": "False",
      "type": "PrecachingSucceeded"
    },
    {
      "lastTransitionTime": "2022-01-27T19:07:34Z",
      "message": "Pre-caching spec is valid and consistent",
      "reason": "PrecacheSpecIsWellFormed",
      "status": "True",
      "type": "PrecacheSpecValid"
    }
  ],
  "precaching": {
    "clusters": [
      "cnfdb1"
      "cnfdb2"
    ],
    "spec": {
      "platformImage": "image.example.io"},
    "status": {
      "cnfdb1": "Active"
      "cnfdb2": "Succeeded"}
    }
}
```


The output lists the identified clusters. The `platformImage` value in `status.precaching.spec` is derived by TALM from the `ClusterVersion` object in the managed policies. 

  3. Check the status of the pre-caching job by running the following command on the spoke cluster: 

```shell-session
$ oc get jobs,pods -n openshift-talo-pre-cache
```


Example output: 

```shell-session
NAME                  COMPLETIONS   DURATION   AGE
job.batch/pre-cache   0/1           3m10s      3m10s

NAME                     READY   STATUS    RESTARTS   AGE
pod/pre-cache--1-9bmlr   1/1     Running   0          3m10s
```


  4. Check the status of the `ClusterGroupUpgrade` CR by running the following command: 

```shell-session
$ oc get cgu -n ztp-group-du-sno du-upgrade-4918 -o jsonpath='{.status}'
```


Example output: 

```plaintext
"conditions": [
    {
      "lastTransitionTime": "2022-01-27T19:30:41Z",
      "message": "The ClusterGroupUpgrade CR has all clusters compliant with all the managed policies",
      "reason": "UpgradeCompleted",
      "status": "True",
      "type": "Ready"
    },
    {
      "lastTransitionTime": "2022-01-27T19:28:57Z",
      "message": "Precaching is completed",
      "reason": "PrecachingCompleted",
      "status": "True",
      "type": "PrecachingSucceeded"
    }
```


The pre-cache tasks are done.
