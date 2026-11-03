# 8.4. Viewing the logs from the vSphere Problem Detector Operator

After the vSphere Problem Detector Operator runs and performs the configuration checks, the Operator creates log records that you can view from the command-line interface (CLI) or from the OpenShift Container Platform web console. Log lines that indicate `passed` means that you do not need to perform any actions. 

The ideal output for a log line indicates `passed` or `0 problems`. If a log line indicates `failure` or 1 or more problems, see the information in the "Configuration checks run by the vSphere Problem Detector Operator" document. 

**Prerequisites**

  * The vSphere Problem Detector Operator ran checks on your cluster. 



**Procedure**

  * To view the logs by using the CLI, run the following command. A log line that shows `passed` in the output means that you must analyze the log output and resolve the issue. 

```shell-session
$ oc logs deployment/vsphere-problem-detector-operator \
    -n openshift-cluster-storage-operator
```


**Example output**

```shell-session
I0108 08:32:28.445696       1 operator.go:209] ClusterInfo passed
I0108 08:32:28.451029       1 datastore.go:57] CheckStorageClasses checked 1 storage classes, 0 problems found
I0108 08:32:28.451047       1 operator.go:209] CheckStorageClasses passed
I0108 08:32:28.452160       1 operator.go:209] CheckDefaultDatastore passed
I0108 08:32:28.480648       1 operator.go:271] CheckNodeDiskUUID:<host_name> passed
I0108 08:32:28.480685       1 operator.go:271] CheckNodeProviderID:<host_name> passed
```


  * To view the Operator logs with the OpenShift Container Platform web console, perform the following steps: 

    1. Navigate to **Workloads** **Pods**. 
    2. Select `openshift-cluster-storage-operator` from the **Projects** menu. 
    3. Click the link for the `vsphere-problem-detector-operator` pod. 
    4. Click the **Logs** tab on the **Pod details** page to view the logs.
