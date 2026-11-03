# 1.1. Control plane backup and restore operations

As a cluster administrator, you might need to stop an OpenShift Container Platform cluster for a period and restart it later. 

Some reasons for restarting a cluster are that you need to perform maintenance on a cluster or want to reduce resource costs. In OpenShift Container Platform, you can perform a [graceful shutdown of a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/graceful-shutdown-cluster "Chapter 2. Shutting down the cluster gracefully") so that you can easily restart the cluster later. 

You must [back up etcd data](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/control-plane-backup-and-restore#backup-etcd "6.1. Backing up and restoring etcd data") before shutting down a cluster; etcd is the key-value store for OpenShift Container Platform, which persists the state of all resource objects. An etcd backup plays a crucial role in disaster recovery. In OpenShift Container Platform, you can also [replace an unhealthy etcd member](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/control-plane-backup-and-restore#replacing-unhealthy-etcd-member "6.3. Replacing an unhealthy etcd member"). 

When you want to get your cluster running again, [restart the cluster gracefully](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/graceful-restart-cluster "Chapter 3. Restarting the cluster gracefully"). 

Note

A cluster’s certificates expire one year after the installation date. You can shut down a cluster and expect it to restart gracefully while the certificates are still valid. Although the cluster automatically retrieves the expired control plane certificates, you must still [approve the certificate signing requests (CSRs)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/control-plane-backup-and-restore#dr-recovering-expired-certs "6.4.4. Recovering from expired control plane certificates"). 

You might run into several situations where OpenShift Container Platform does not work as expected, such as: 

  * You have a cluster that is not functional after the restart because of unexpected conditions, such as node failure or network connectivity issues. 
  * You have deleted something critical in the cluster by mistake. 
  * You have lost the majority of your control plane hosts, leading to etcd quorum loss. 



You can always recover from a disaster situation by [restoring your cluster to its previous state](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/control-plane-backup-and-restore#dr-restoring-cluster-state "6.4.3. Restoring to an earlier cluster state") using the saved etcd snapshots. 

**Additional resources**

  * [Quorum protection with machine lifecycle hooks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#machine-lifecycle-hook-deletion-etcd_deleting-machine)
