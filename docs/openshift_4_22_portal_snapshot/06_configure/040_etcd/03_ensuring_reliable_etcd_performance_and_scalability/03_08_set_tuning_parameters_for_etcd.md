# 3.8. Set tuning parameters for etcd

Configure the control plane hardware speed setting for etcd to match your environment’s latency. 

You can set the control plane hardware speed to `"Standard"` or `"Slower"`, or use the default, which is `""`. 

The default setting allows the system to decide the speed to use. This value enables upgrades from versions where this feature does not exist, as the system can select values from previous versions. 

By selecting one of the other values, you are overriding the default. If you see many leader elections due to timeouts or missed heartbeats, and your system is set to `""` or `"Standard"`, set the hardware speed to `"Slower"`. This change makes the system more tolerant to the increased latency. 

**Procedure**

  1. Check to see what the current value is by entering the following command: 

```shell-session
$ oc describe etcd/cluster | grep "Control Plane Hardware Speed"
```


**Example output**

```shell-session
Control Plane Hardware Speed:  <VALUE>
```


Note

If the output is empty, the field has not been set and should be considered as the default (""). 

  2. Change the value by entering the following command. Replace `<value>` with one of the valid values: `""`, `"Standard"`, or `"Slower"`: 

```shell-session
$ oc patch etcd/cluster --type=merge -p '{"spec": {"controlPlaneHardwareSpeed": "<value>"}}'
```


The following table indicates the heartbeat interval and leader election timeout for each profile. These values are subject to change. 

Table 3.2. Heartbeat interval and leader election timeout by hardware speed profile Profile  |  ETCD_HEARTBEAT_INTERVAL  |  ETCD_LEADER_ELECTION_TIMEOUT   
---|---|---  
`""` |  Varies depending on platform  |  Varies depending on platform   
`Standard` |  100  |  1000   
`Slower` |  500  |  2500   
Show more

  3. Review the output: 

**Example output**

```shell-session
etcd.operator.openshift.io/cluster patched
```


If you enter any value besides the valid values, error output is displayed. For example, if you entered `"Faster"` as the value, the output is as follows: 

**Example output**

```shell-session
The Etcd "cluster" is invalid: spec.controlPlaneHardwareSpeed: Unsupported value: "Faster": supported values: "", "Standard", "Slower"
```


  4. Verify that the value was changed by entering the following command: 

```shell-session
$ oc describe etcd/cluster | grep "Control Plane Hardware Speed"
```


**Example output**

```shell-session
Control Plane Hardware Speed:  ""
```


  5. Wait for etcd pods to roll out: 

```shell-session
$ oc get pods -n openshift-etcd -w
```


The following output shows the expected entries for the `main-0` control plane node. Before you continue, wait until all control plane nodes show a status of `4/4 Running`. 

**Example output**

```shell-session
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Pending             0          0s
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Pending             0          0s
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     ContainerCreating   0          0s
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     ContainerCreating   0          1s
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           1/1     Running             0          2s
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          34s
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          36s
installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          36s
etcd-guard-ci-ln-qkgs94t-72292-9clnd-main-0            0/1     Running             0          26m
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Terminating         0          11m
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Terminating         0          11m
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Pending             0          0s
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Init:1/3            0          1s
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Init:2/3            0          2s
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     PodInitializing     0          3s
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  3/4     Running             0          4s
etcd-guard-ci-ln-qkgs94t-72292-9clnd-main-0            1/1     Running             0          26m
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  3/4     Running             0          20s
etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Running             0          20s
```


  6. Enter the following command to review to the values: 

```shell-session
$ oc describe -n openshift-etcd pod/<ETCD_PODNAME> | grep -e HEARTBEAT_INTERVAL -e ELECTION_TIMEOUT
```


Note

These values might not have changed from the default. 




**Additional resources**

  * [Understanding feature gates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cluster-enabling-features-about_nodes-cluster-enabling-features)
