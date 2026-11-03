# 6.1. Summarizing cluster specifications by using a cluster version object

To verify your cluster version, check update history, and confirm component status, query the `clusterversion` resource. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Query cluster version, availability, uptime, and general status: 

```shell-session
$ oc get clusterversion
```


**Example output**

```plaintext
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.13.8    True        False         8h      Cluster version is 4.13.8
```


  2. Obtain a detailed summary of cluster specifications, update availability, and update history: 

```shell-session
$ oc describe clusterversion
```


**Example output**

```plaintext
Name:         version
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  config.openshift.io/v1
Kind:         ClusterVersion
# ...
    Image:    quay.io/openshift-release-dev/ocp-release@sha256:a956488d295fe5a59c8663a4d9992b9b5d0950f510a7387dbbfb8d20fc5970ce
    URL:      https://access.redhat.com/errata/RHSA-2023:4456
    Version:  4.13.8
  History:
    Completion Time:    2023-08-17T13:20:21Z
    Image:              quay.io/openshift-release-dev/ocp-release@sha256:a956488d295fe5a59c8663a4d9992b9b5d0950f510a7387dbbfb8d20fc5970ce
    Started Time:       2023-08-17T12:59:45Z
    State:              Completed
    Verified:           false
    Version:            4.13.8
# ...
```
