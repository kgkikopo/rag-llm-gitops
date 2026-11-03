# 4.12. etcd tasks

Back up etcd, enable or disable etcd encryption, or defragment etcd data. 

Note

If you deployed a bare-metal cluster, you can scale the cluster up to 5 nodes as part of your post-installation tasks. 

**Additional resources**

  * [Node scaling for etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#etcd-node-scaling_etcd-performance)



## 4.12.1. etcd encryption

You can encrypt sensitive resource data in etcd to provide an additional layer of protection if an etcd backup or storage data is exposed. 

By default, etcd data is not encrypted in OpenShift Container Platform. You can enable etcd encryption for your cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties. 

When you enable etcd encryption, the following OpenShift API server and Kubernetes API server resources are encrypted: 

  * Secrets 
  * Config maps 
  * Routes 
  * OAuth access tokens 
  * OAuth authorize tokens 



When you enable etcd encryption, encryption keys are created. You must have these keys to restore from an etcd backup. 

Note

etcd encryption only encrypts values, not keys. Resource types, namespaces, and object names are unencrypted. 

If etcd encryption is enabled during a backup, the `_static_kuberesources_ <datetimestamp>.tar.gz_` file contains the encryption keys for the etcd snapshot. For security reasons, store this file separately from the etcd snapshot. However, this file is required to restore a previous state of etcd from the respective etcd snapshot. 

## 4.12.2. Supported encryption types

OpenShift Container Platform supports AES-CBC and AES-GCM encryption types to protect etcd data at rest. 

The following encryption types are supported for encrypting etcd data in OpenShift Container Platform: 

AES-CBC
     Uses AES-CBC with PKCS#7 padding and a 32-byte key to perform the encryption. 
AES-GCM
     Uses AES-GCM with a random nonce and a 32-byte key to perform the encryption. 

The etcd encryption keys are rotated every 7 days. Up to 10 historical encryption keys are preserved after rotation to help decrypt older backups and provide an extra layer of data recovery safety. 

## 4.12.3. Enable etcd encryption

Enable etcd encryption to protect sensitive cluster resources such as secrets, config maps, routes, and OAuth tokens at rest. 

Warning

Do not back up etcd resources until the initial encryption process is completed. If the encryption process is not completed, the backup might be only partially encrypted. 

After you enable etcd encryption, several changes can occur: 

  * The etcd encryption might affect the memory consumption of a few resources. 
  * You might notice a transient effect on backup performance because the leader must serve the backup. 
  * A disk I/O can affect the node that receives the backup state. 



You can encrypt the etcd database in either AES-GCM or AES-CBC encryption. 

Note

To migrate your etcd database from one encryption type to the other, you can modify the API server’s `spec.encryption.type` field. Migration of the etcd data to the new encryption type occurs automatically. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Modify the `APIServer` object: 

```shell-session
$ oc edit apiserver
```


  2. Set the `spec.encryption.type` field to `aesgcm` or `aescbc`: 

```yaml
spec:
  encryption:
    type: aesgcm
```


     * The `aesgcm` value specifies AES-GCM encryption. Alternatively, set the `type` field to `aescbc` for AES-CBC encryption. 

  3. Save the file to apply the changes. 

The encryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of the etcd database. 




**Verification**

  * Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully encrypted: 

```shell-session
$ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `EncryptionCompleted` upon successful encryption: 

```shell-session
EncryptionCompleted
All resources encrypted: routes.route.openshift.io
```


If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again. 

  * Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully encrypted: 

```shell-session
$ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `EncryptionCompleted` upon successful encryption: 

```shell-session
EncryptionCompleted
All resources encrypted: secrets, configmaps
```


If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again. 

  * Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully encrypted: 

```shell-session
$ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `EncryptionCompleted` upon successful encryption: 

```shell-session
EncryptionCompleted
All resources encrypted: oauthaccesstokens.oauth.openshift.io, oauthauthorizetokens.oauth.openshift.io
```


If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again. 




## 4.12.4. Disable etcd encryption

Disable etcd encryption when you no longer need to encrypt sensitive cluster resources at rest. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Modify the `APIServer` object: 

```shell-session
$ oc edit apiserver
```


  2. Set the `encryption` field type to `identity`: 

```yaml
spec:
  encryption:
    type: identity
```


The `identity` value specifies that no encryption is performed. This is the default value. 

  3. Save the file to apply the changes. 

The decryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of your cluster. 




**Verification**

  * Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully decrypted: 

```shell-session
$ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `DecryptionCompleted` upon successful decryption: 

```shell-session
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
```


If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again. 

  * Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully decrypted: 

```shell-session
$ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `DecryptionCompleted` upon successful decryption: 

```shell-session
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
```


If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again. 

  * Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully decrypted: 

```shell-session
$ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `DecryptionCompleted` upon successful decryption: 

```shell-session
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
```


If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again. 




## 4.12.5. Backing up etcd data

You can back up etcd data by creating an etcd snapshot and saving the static pod resources on a control plane host. This backup preserves the cluster state and provides the resources required to restore etcd at a later time. 

Important

Only save a backup from a single control plane host. Do not take a backup from each control plane host in the cluster. 

For a Two-Node with Fencing (TNF) setup, follow the steps to back up etcd data on only one node in the cluster. The cluster restore process is driven by data from a single node, so you can perform the etcd backup steps on only one node. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have verified whether the cluster-wide proxy is enabled. 

Tip

You can check whether the proxy is enabled by reviewing the output of `oc get proxy cluster -o yaml`. The proxy is enabled if the `httpProxy`, `httpsProxy`, and `noProxy` fields have values set. 




**Procedure**

  1. Start a debug session as root for a control plane node: 

```shell-session
$ oc debug --as-root node/<node_name>
```


  2. Change your root directory to `/host` in the debug shell: 

```shell-session
sh-4.4# chroot /host
```


  3. If the cluster-wide proxy is enabled, export the `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY` environment variables by running the following commands: 

```shell-session
$ export HTTP_PROXY=http://<your_proxy.example.com>:8080
```


```shell-session
$ export HTTPS_PROXY=https://<your_proxy.example.com>:8080
```


```shell-session
$ export NO_PROXY=<example.com>
```


  4. Run the `cluster-backup.sh` script with the path to the directory where you want to save the backup: 

Tip

The `cluster-backup.sh` script is maintained as a component of the etcd Cluster Operator and is a wrapper around the `etcdctl snapshot save` command. 

```shell-session
sh-4.4# /usr/local/bin/cluster-backup.sh /home/core/assets/backup
```


**Example script output**

```shell-session
found latest kube-apiserver: /etc/kubernetes/static-pod-resources/kube-apiserver-pod-6
found latest kube-controller-manager: /etc/kubernetes/static-pod-resources/kube-controller-manager-pod-7
found latest kube-scheduler: /etc/kubernetes/static-pod-resources/kube-scheduler-pod-6
found latest etcd: /etc/kubernetes/static-pod-resources/etcd-pod-3
ede95fe6b88b87ba86a03c15e669fb4aa5bf0991c180d3c6895ce72eaade54a1
etcdctl version: 3.4.14
API version: 3.4
{"level":"info","ts":1624647639.0188997,"caller":"snapshot/v3_snapshot.go:119","msg":"created temporary db file","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db.part"}
{"level":"info","ts":"2021-06-25T19:00:39.030Z","caller":"clientv3/maintenance.go:200","msg":"opened snapshot stream; downloading"}
{"level":"info","ts":1624647639.0301006,"caller":"snapshot/v3_snapshot.go:127","msg":"fetching snapshot","endpoint":"https://10.0.0.5:2379"}
{"level":"info","ts":"2021-06-25T19:00:40.215Z","caller":"clientv3/maintenance.go:208","msg":"completed snapshot read; closing"}
{"level":"info","ts":1624647640.6032252,"caller":"snapshot/v3_snapshot.go:142","msg":"fetched snapshot","endpoint":"https://10.0.0.5:2379","size":"114 MB","took":1.584090459}
{"level":"info","ts":1624647640.6047094,"caller":"snapshot/v3_snapshot.go:152","msg":"saved","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db"}
Snapshot saved at /home/core/assets/backup/snapshot_2021-06-25_190035.db
{"hash":3866667823,"revision":31407,"totalKey":12828,"totalSize":114446336}
snapshot db and kube resources are successfully saved to /home/core/assets/backup
```


In this example, two files are created in the `/home/core/assets/backup/` directory on the control plane host: 

     * `snapshot_<datetimestamp>.db`: This file is the etcd snapshot. The `cluster-backup.sh` script confirms the validity of the snapshot. 
     * `static_kuberesources_<datetimestamp>.tar.gz`: This file contains the resources for the static pods. If etcd encryption is enabled, it also contains the encryption keys for the etcd snapshot. 

Note

If etcd encryption is enabled, store this second file separately from the etcd snapshot for security reasons. However, this file is required to restore from the etcd snapshot. 

The etcd encryption only encrypts values, not keys. This means that resource types, namespaces, and object names are not encrypted. 




## 4.12.6. Data defragmentation for etcd

To prevent etcd performance degradation and cluster-wide maintenance alarms on large clusters, monitor etcd database metrics and defragment the data store when the keyspace grows too large. 

For large and dense clusters, etcd can suffer from poor performance if the keyspace grows too large and exceeds the space quota. Periodically maintain and defragment etcd to free up space in the data store. Monitor Prometheus for etcd metrics and defragment it when required. Otherwise, etcd can raise a cluster-wide alarm that puts the cluster into a maintenance mode, which accepts only key reads and deletes. 

Monitor these key metrics: 

  * `etcd_server_quota_backend_bytes`, which is the current quota limit 
  * `etcd_mvcc_db_total_size_in_use_in_bytes`, which indicates the actual database usage after a history compaction 
  * `etcd_mvcc_db_total_size_in_bytes`, which shows the database size, including free space waiting for defragmentation 



Defragment etcd data to reclaim disk space after events that cause disk fragmentation, such as etcd history compaction. 

History compaction is performed automatically every five minutes and leaves gaps in the back-end database. This fragmented space is available for use by etcd, but is not available to the host file system. You must defragment etcd to make this space available to the host file system. 

Defragmentation occurs automatically, but you can also trigger it manually. 

## 4.12.7. Automatic defragmentation

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


## 4.12.8. Manually defragmenting etcd data

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


## 4.12.9. Restoring to an earlier cluster state for more than one node

To restore your OpenShift Container Platform cluster with more than one control plane node to an earlier state, use a saved etcd snapshot after quorum loss or critical data deletion. 

For a Two-Node with Fencing (TNF) setup, a single surviving node can continue to operate in degraded mode. Use a saved etcd backup to restore an earlier cluster state if only one node is operational, or when both nodes have failed and you need to restart the cluster from a known safe state. In both cases, perform the restore procedure on a single node. The peer node automatically synchronizes data with the restored node when it rejoins the cluster. 

Before you restore from backup on the recovery host, shut down etcd on enough control plane nodes so the remaining members cannot form a quorum: 

  * Shut down etcd on 2 hosts in a 3-node cluster. 
  * Shut down etcd on 3 hosts in a 4-node or 5-node cluster. 



If too few hosts are shut down, the other etcd members might still form a quorum and continue service while you restore. 

Note

If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in the control plane machine set troubleshooting topic for an etcd recovery procedure. For OpenShift Container Platform on a single node, follow the procedure to restore to an earlier cluster state for a single node. 

Important

When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform 4.22.2 cluster must use an etcd backup that was taken from 4.22.2. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file, like the one that was used during installation. 
  * You have a healthy control plane host to use as the recovery host. 
  * You have SSH access to control plane hosts. 
  * You have a backup directory containing both the `etcd` snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`. 
  * Control plane nodes are accessible or bootable. 



Important

For non-recovery control plane nodes, it is not required to establish SSH connectivity or to stop the static pods. You can delete and re-create other non-recovery, control plane machines, one by one. 

**Procedure**

  1. Select a control plane host to use as the recovery host. This is the host that you run the restore operation on. 
  2. Establish SSH connectivity to each of the control plane nodes, including the recovery host. 

`kube-apiserver` becomes inaccessible after the restore process starts, so you cannot access the control plane nodes. Establish SSH connectivity to each control plane host in a separate terminal. 

Important

If you do not complete this step, you cannot access the control plane hosts to complete the restore procedure, and you cannot recover your cluster from this state. 

  3. Using SSH, connect to each control plane node to disable etcd by running the following command: 

```shell-session
$ sudo -E /usr/local/bin/disable-etcd.sh
```


  4. Copy the etcd backup directory to the recovery control plane host. 

This procedure assumes that you copied the `backup` directory containing the etcd snapshot and the resources for the static pods to the `/home/core/` directory of your recovery control plane host. 

  5. Use SSH to connect to the recovery host. Restore the cluster from an earlier backup by running the following command: 

```shell-session
$ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd-backup-directory>
```


  6. Exit the SSH session. 
  7. When the API responds, turn off the etcd Operator quorum guard by running the following command: 

```shell-session
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
```


Important

For a TNF setup, do not: 

     * Change the etcd Operator quorum setting. 
     * Turn the etcd Operator quorum off. 
     * Turn the etcd Operator quorum back on. 

  8. Monitor the recovery progress of the control plane by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


Note

It can take up to 15 minutes for the control plane to recover. Wait for the control plane to recover before using the next step. 

  9. Enable the quorum guard by running the following command: 

```shell-session
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
```


**Troubleshooting**

If the etcd static pods do not roll out, you can manually force an etcd redeployment from the `cluster-etcd-operator` by running the following command: 

```shell-session
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$(date --rfc-3339=ns )"'"}}' --type=merge
```


**Additional resources**

  * [Recommended etcd practices](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#recommended-etcd-practices)
  * [Installing a user-provisioned cluster on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal)
  * [Replacing a bare-metal control plane node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#replacing-a-bare-metal-control-plane-node_bare-metal-expanding)



## 4.12.10. Issues and workarounds for restoring a persistent storage state

To restore workloads safely after an etcd snapshot restore, identify and resolve outdated persistent storage references, including volumes, credentials, attachments, and devices on your OpenShift Container Platform cluster. 

If your OpenShift Container Platform cluster uses persistent storage of any form, a state of the cluster is typically stored outside etcd. When you restore from an etcd backup, the status of the workloads in OpenShift Container Platform is also restored. However, if the etcd snapshot is old, the status might be invalid or outdated. 

Important

The contents of persistent volumes (PVs) are never part of the etcd snapshot. When you restore an OpenShift Container Platform cluster from an etcd snapshot, non-critical workloads might gain access to critical data, or vice-versa. 

The following are some example scenarios that produce an out-of-date status: 

  * MySQL database is running in a pod backed up by a PV object. Restoring OpenShift Container Platform from an etcd snapshot does not bring back the volume on the storage provider, and does not produce a running MySQL pod, despite the pod repeatedly attempting to start. You must manually restore this pod by restoring the volume on the storage provider, and then editing the PV to point to the new volume. 
  * Pod P1 is using volume A, which is attached to node X. If the etcd snapshot is taken while another pod uses the same volume on node Y, then when the etcd restore is performed, pod P1 might not be able to start correctly due to the volume still being attached to node Y. OpenShift Container Platform is not aware of the attachment, and does not automatically detach it. When this occurs, the volume must be manually detached from node Y so that the volume can attach on node X, and then pod P1 can start. 
  * Cloud provider or storage provider credentials were updated after the etcd snapshot was taken. This causes any CSI drivers or Operators that depend on those credentials to not work. You might have to manually update the credentials required by those drivers or Operators. 
  * A device is removed or renamed from OpenShift Container Platform nodes after the etcd snapshot is taken. The Local Storage Operator creates symlinks for each PV that it manages from `/dev/disk/by-id` or `/dev` directories. This situation might cause the local PVs to refer to devices that no longer exist. 

To fix this problem, an administrator must: 

    1. Manually remove the PVs with invalid devices. 
    2. Remove symlinks from respective nodes. 
    3. Delete `LocalVolume` or `LocalVolumeSet` objects. For more information, see "Deleting the Local Storage Operator resources".
