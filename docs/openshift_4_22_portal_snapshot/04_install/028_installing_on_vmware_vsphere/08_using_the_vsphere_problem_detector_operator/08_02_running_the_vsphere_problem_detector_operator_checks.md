# 8.2. Running the vSphere Problem Detector Operator checks

You can override the schedule for running the vSphere Problem Detector Operator checks and run the checks immediately. 

The vSphere Problem Detector Operator automatically runs the checks every hour. After the Operator starts, the Operator runs the checks immediately. After the Cluster Storage Operator starts and determines that a cluster runs on VMware vSphere, the Cluster Storage Operator starts the vSphere Problem Detector Operator. To run the checks immediately, you can scale the vSphere Problem Detector Operator to `0` and back to `1` so that the Cluster Storage Operator restarts the vSphere Problem Detector Operator. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Scale the Operator to `0`: 

```shell-session
$ oc scale deployment/vsphere-problem-detector-operator --replicas=0 \
    -n openshift-cluster-storage-operator
```


**Verification**

  * Verify that the pods have restarted by running the following command: 

```shell-session
$ oc -n openshift-cluster-storage-operator get pod -l name=vsphere-problem-detector-operator -w
```


**Example output**

```shell-session
NAME                                                 READY   STATUS    RESTARTS   AGE
vsphere-problem-detector-operator-77486bd645-9ntpb   1/1     Running   0          11s
```


The `AGE` field must indicate that the pod restarted. 




**Next steps**

  * Viewing the events from the vSphere Problem Detector Operator 
  * Viewing the logs from the vSphere Problem Detector Operator
