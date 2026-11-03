# 3.7. Data defragmentation for etcd

To prevent etcd performance degradation and cluster-wide maintenance alarms on large clusters, monitor etcd database metrics and defragment the data store when the keyspace grows too large. 

For large and dense clusters, etcd can suffer from poor performance if the keyspace grows too large and exceeds the space quota. Periodically maintain and defragment etcd to free up space in the data store. Monitor Prometheus for etcd metrics and defragment it when required. Otherwise, etcd can raise a cluster-wide alarm that puts the cluster into a maintenance mode, which accepts only key reads and deletes. 

Monitor these key metrics: 

  * `etcd_server_quota_backend_bytes`, which is the current quota limit 
  * `etcd_mvcc_db_total_size_in_use_in_bytes`, which indicates the actual database usage after a history compaction 
  * `etcd_mvcc_db_total_size_in_bytes`, which shows the database size, including free space waiting for defragmentation 



Defragment etcd data to reclaim disk space after events that cause disk fragmentation, such as etcd history compaction. 

History compaction is performed automatically every five minutes and leaves gaps in the back-end database. This fragmented space is available for use by etcd, but is not available to the host file system. You must defragment etcd to make this space available to the host file system. 

Defragmentation occurs automatically, but you can also trigger it manually. 

## 3.7.1. Automatic defragmentation

When etcd database growth affects performance, the etcd Operator can automatically defragment member disks based on cluster metrics. 

Note

Automatic defragmentation works well in most cases because the etcd Operator uses cluster metrics to choose the most efficient defragmentation approach. 

The etcd Operator automatically defragments disks. No manual intervention is needed. 

Verify that defragmentation succeeded by checking one of these logs: 

  * etcd logs 
  * cluster-etcd-operator pod 
  * operator status error log 



Warning

Automatic defragmentation can cause leader election failure in various OpenShift Container Platform core components, such as the Kubernetes controller manager, which triggers a restart of the failing component. The restart is harmless and either triggers failover to the next running instance or the component resumes work again after the restart. 

The following is example log output for successful defragmentation: 

```shell-session
etcd member has been defragmented: <member_name>, memberID: <member_id>
```


The following is example log output for unsuccessful defragmentation: 

```shell-session
failed defrag on member: <member_name>, memberID: <member_id>: <error_message>
```


## 3.7.2. Manually defragmenting etcd data

When automatic etcd defragmentation cannot reclaim enough space, manually defragment etcd on each member to restore disk availability and normal cluster operation. 

A Prometheus alert indicates when you need to use manual defragmentation. The alert is displayed in two cases: 

  * When etcd uses more than 50% of its available space for more than 10 minutes 
  * When etcd is actively using less than 50% of its total database size for more than 10 minutes 



You can also determine whether defragmentation is needed by checking the etcd database size in MB that will be freed by defragmentation with the PromQL expression: `(etcd_mvcc_db_total_size_in_bytes - etcd_mvcc_db_total_size_in_use_in_bytes)/1024/1024`

Warning

Defragmenting etcd is a blocking action. The etcd member does not respond until defragmentation is complete. For this reason, wait at least one minute between defragmentation actions on each of the pods to allow the cluster to recover. 

Follow this procedure to defragment etcd data on each etcd member. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Determine which etcd member is the leader, because the leader should be defragmented last. 

     1. Get the list of etcd pods: 

```shell-session
$ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
```


The following is example output: 

```shell-session
etcd-ip-10-0-159-225.example.redhat.com                3/3     Running     0          175m   10.0.159.225   ip-10-0-159-225.example.redhat.com   <none>           <none>
etcd-ip-10-0-191-37.example.redhat.com                 3/3     Running     0          173m   10.0.191.37    ip-10-0-191-37.example.redhat.com    <none>           <none>
etcd-ip-10-0-199-170.example.redhat.com                3/3     Running     0          176m   10.0.199.170   ip-10-0-199-170.example.redhat.com   <none>           <none>
```


     2. Choose a pod and run the following command to determine which etcd member is the leader: 

```shell-session
$ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com etcdctl endpoint status --cluster -w table
```


The following is example output: 

```shell-session
Defaulting container name to etcdctl.
Use 'oc describe pod/etcd-ip-10-0-159-225.example.redhat.com -n openshift-etcd' to see all of the containers in this pod.
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
| https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
| https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
```


Based on the `IS LEADER` column of this output, the `https://10.0.199.170:2379` endpoint is the leader. Matching this endpoint with the output of the previous step, the pod name of the leader is `etcd-ip-10-0-199-170.example.redhat.com`. 

  2. Defragment an etcd member. 

     1. Connect to the running etcd container, passing in the name of a pod that is _not_ the leader: 

```shell-session
$ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com
```


     2. Unset the `ETCDCTL_ENDPOINTS` environment variable: 

```shell-session
sh-4.4# unset ETCDCTL_ENDPOINTS
```


     3. Defragment the etcd member: 

```shell-session
sh-4.4# etcdctl --command-timeout=30s --endpoints=https://localhost:2379 defrag
```


The following is example output: 

```shell-session
Finished defragmenting etcd member[https://localhost:2379]
```


If a timeout error occurs, increase the value for `--command-timeout` until the command succeeds. 

     4. Verify that the database size was reduced: 

```shell-session
sh-4.4# etcdctl endpoint status -w table --cluster
```


The following is example output: 

```shell-session
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
| https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |   41 MB |     false |      false |         7 |      91624 |              91624 |        | 
```


1

```shell-session
| https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
```


This example shows that the database size for this etcd member is now 41 MB as opposed to the starting size of 104 MB. 

     5. Repeat these steps to connect to each of the other etcd members and defragment them. Always defragment the leader last. 

Wait at least one minute between defragmentation actions to allow the etcd pod to recover. Until the etcd pod recovers, the etcd member does not respond. 

  3. If any `NOSPACE` alarms were triggered due to the space quota being exceeded, clear them. 

     1. Check if there are any `NOSPACE` alarms: 

```shell-session
sh-4.4# etcdctl alarm list
```


The following is example output: 

```shell-session
memberID:12345678912345678912 alarm:NOSPACE
```


     2. Clear the alarms: 

```shell-session
sh-4.4# etcdctl alarm disarm
```
