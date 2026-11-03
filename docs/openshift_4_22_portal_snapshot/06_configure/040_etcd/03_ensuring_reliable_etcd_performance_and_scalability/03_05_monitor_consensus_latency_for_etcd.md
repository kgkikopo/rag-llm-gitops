# 3.5. Monitor consensus latency for etcd

Use the `etcdctl` command-line interface (CLI) to check endpoint health and consensus latency on a running cluster. Regular monitoring helps you spot delays before they cause leader elections and Kubernetes API instability. 

By using the `etcdctl` CLI, you can monitor the latency for reaching consensus as experienced by etcd. You must identify one of the etcd pods and then retrieve the endpoint health. 

This procedure, which validates and monitors cluster health, can be run only on an active cluster. 

**Prerequisites**

  * During planning for cluster deployment, you completed the disk and network tests. 



**Procedure**

  1. Enter the following command: 

```shell-session
# oc get pods -n openshift-etcd -l app=etcd
```


**Example output**

```shell-session
NAME      READY   STATUS    RESTARTS   AGE
etcd-m0   4/4     Running   4          8h
etcd-m1   4/4     Running   4          8h
etcd-m2   4/4     Running   4          8h
```


  2. Enter the following command. To better understand the etcd latency for consensus, run this command on a precise watch cycle for a few minutes. Observe that the numbers remain below the ~66 ms threshold. The closer the consensus time is to 100 ms, the more likely the cluster experiences service-affecting events and instability. 

```shell-session
# oc exec -ti etcd-m0 -- etcdctl endpoint health -w table
```


**Example output**

```shell-session
+----------------------------+--------+-------------+-------+
|          ENDPOINT          | HEALTH |    TOOK     | ERROR |
+----------------------------+--------+-------------+-------+
| https://198.18.111.12:2379 |   true |  3.798349ms |       |
| https://198.18.111.14:2379 |   true |  7.389608ms |       |
| https://198.18.111.13:2379 |   true |  6.263117ms |       |
+----------------------------+--------+-------------+-------+
```


  3. Enter the following command: 

```shell-session
# oc exec -ti etcd-m0 -- watch -dp -c etcdctl endpoint health -w table
```


**Example output**

```shell-session
+----------------------------+--------+-------------+-------+
|          ENDPOINT          | HEALTH |    TOOK     | ERROR |
+----------------------------+--------+-------------+-------+
| https://198.18.111.12:2379 |   true |  9.533405ms |       |
| https://198.18.111.13:2379 |   true |  4.628054ms |       |
| https://198.18.111.14:2379 |   true |  5.803378ms |       |
+----------------------------+--------+-------------+-------+
```
