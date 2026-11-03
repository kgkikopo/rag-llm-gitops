# 22.4. Display resulting values of worker latency profile

You can run specific commands to display the values for the worker latency profile. You can then check the displayed values for information accuracy. 

**Procedure**

  1. Check the `default-not-ready-toleration-seconds` and `default-unreachable-toleration-seconds` fields output by the Kube API Server: 

```shell-session
$ oc get KubeAPIServer -o yaml | grep -A 1 default-
```


**Example output**

```shell-session
default-not-ready-toleration-seconds:
- "300"
default-unreachable-toleration-seconds:
- "300"
```


  2. Check the values of the `node-monitor-grace-period` field from the Kube Controller Manager: 

```shell-session
$ oc get KubeControllerManager -o yaml | grep -A 1 node-monitor
```


**Example output**

```shell-session
node-monitor-grace-period:
- 40s
```


  3. Check the `nodeStatusUpdateFrequency` value from the Kubelet by entering the following command. Set the directory `/host` as the root directory within the debug shell. By changing the root directory to `/host`, you can run binaries contained in the executable paths of the host. 

```shell-session
$ oc debug node/<compute_node_name>
```


```shell-session
$ chroot /host
```


```shell-session
# cat /etc/kubernetes/kubelet.conf|grep nodeStatusUpdateFrequency
```


**Example output**

```shell-session
“nodeStatusUpdateFrequency”: “10s”
```


These outputs validate the set of timing variables for the Worker Latency Profile.
