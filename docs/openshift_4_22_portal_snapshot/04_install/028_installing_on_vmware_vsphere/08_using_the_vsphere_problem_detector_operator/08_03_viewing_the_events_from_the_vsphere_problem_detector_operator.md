# 8.3. Viewing the events from the vSphere Problem Detector Operator

After the vSphere Problem Detector Operator runs and performs the configuration checks, the Operator creates events that you can view from the command-line interface (CLI) or from the OpenShift Container Platform web console. 

**Prerequisites**

  * The vSphere Problem Detector Operator ran checks on your cluster. 



**Procedure**

  * To view the events by using the CLI, run the following command: 

```shell-session
$ oc get event -n openshift-cluster-storage-operator \
    --sort-by={.metadata.creationTimestamp}
```


**Example output**

```shell-session
16m     Normal    Started             pod/vsphere-problem-detector-operator-xxxxx         Started container vsphere-problem-detector
16m     Normal    Created             pod/vsphere-problem-detector-operator-xxxxx         Created container vsphere-problem-detector
16m     Normal    LeaderElection      configmap/vsphere-problem-detector-lock    vsphere-problem-detector-operator-xxxxx became leader
```


  * To view the events by using the OpenShift Container Platform web console, navigate to **Home** **Events** and select `openshift-cluster-storage-operator` from the **Project** menu.
