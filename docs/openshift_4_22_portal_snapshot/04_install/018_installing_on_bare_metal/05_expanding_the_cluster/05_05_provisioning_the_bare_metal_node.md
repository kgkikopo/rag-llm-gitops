# 5.5. Provisioning the bare-metal node

Scale the compute machine set to provision a new bare-metal node and add it as a worker to your cluster after the node is prepared and available. 

**Procedure**

  1. Ensure the `STATE` is `available` before provisioning the bare-metal node. 

```shell-session
$  oc -n openshift-machine-api get bmh openshift-worker-<num>
```


Replace `<num>` with the worker node number. 

```shell-session
NAME              STATE     ONLINE ERROR  AGE
openshift-worker  available true          34h
```


  2. Get a count of the number of worker nodes. 

```shell-session
$ oc get nodes
```


```shell-session
NAME                                                STATUS   ROLES           AGE     VERSION
openshift-master-1.openshift.example.com            Ready    master          30h     v1.35.4
openshift-master-2.openshift.example.com            Ready    master          30h     v1.35.4
openshift-master-3.openshift.example.com            Ready    master          30h     v1.35.4
openshift-worker-0.openshift.example.com            Ready    worker          30h     v1.35.4
openshift-worker-1.openshift.example.com            Ready    worker          30h     v1.35.4
```


  3. Get the compute machine set. 

```shell-session
$ oc get machinesets -n openshift-machine-api
```


```shell-session
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
...
openshift-worker-0.example.com      1         1         1       1           55m
openshift-worker-1.example.com      1         1         1       1           55m
```


  4. Increase the number of worker nodes by one. 

```shell-session
$ oc scale --replicas=<num> machineset <machineset> -n openshift-machine-api
```


Replace `<num>` with the new number of worker nodes. Replace `<machineset>` with the name of the compute machine set from the previous step. 

  5. Check the status of the bare-metal node. 

```shell-session
$ oc -n openshift-machine-api get bmh openshift-worker-<num>
```


Replace `<num>` with the worker node number. The STATE changes from `ready` to `provisioning`. 

```shell-session
NAME                    STATE             CONSUMER                          ONLINE   ERROR
openshift-worker-<num>  provisioning      openshift-worker-<num>-65tjz      true
```


The `provisioning` status remains until the OpenShift Container Platform cluster provisions the node. This can take 30 minutes or more. After the node is provisioned, the state will change to `provisioned`. 

```shell-session
NAME                    STATE             CONSUMER                          ONLINE   ERROR
openshift-worker-<num>  provisioned       openshift-worker-<num>-65tjz      true
```


  6. After provisioning completes, ensure the bare-metal node is ready. 

```shell-session
$ oc get nodes
```


```shell-session
NAME                                          STATUS   ROLES   AGE     VERSION
openshift-master-1.openshift.example.com      Ready    master  30h     v1.35.4
openshift-master-2.openshift.example.com      Ready    master  30h     v1.35.4
openshift-master-3.openshift.example.com      Ready    master  30h     v1.35.4
openshift-worker-0.openshift.example.com      Ready    worker  30h     v1.35.4
openshift-worker-1.openshift.example.com      Ready    worker  30h     v1.35.4
openshift-worker-<num>.openshift.example.com  Ready    worker  3m27s   v1.35.4
```


You can also check the kubelet. 

```shell-session
$ ssh openshift-worker-<num>
```


```shell-session
[kni@openshift-worker-<num>]$ journalctl -fu kubelet
```
