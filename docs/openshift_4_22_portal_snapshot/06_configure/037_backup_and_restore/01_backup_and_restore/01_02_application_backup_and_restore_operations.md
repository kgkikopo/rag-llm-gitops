# 1.2. Application backup and restore operations

As a cluster administrator, you can back up and restore applications running on OpenShift Container Platform by using the OpenShift API for Data Protection (OADP). 

OADP backs up and restores Kubernetes resources and internal images, at the granularity of a namespace, by using the version of Velero that is appropriate for the version of OADP you install, according to the table in [OADP-Velero-OpenShift Container Platform version relationship](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#velero-oadp-version-relationship_oadp-cli-tool "5.29.2.1.1. OADP-Velero-OpenShift Container Platform version relationship"). OADP backs up and restores persistent volumes (PVs) by using snapshots or Restic. For details, see [OADP features](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-features_oadp-features-plugins "5.4.1. OADP features"). 

## 1.2.1. OADP requirements

OADP has the following requirements: 

  * You must be logged in as a user with a `cluster-admin` role. 
  * You must have object storage for storing backups, such as one of the following storage types: 

    * OpenShift Data Foundation 
    * Amazon Web Services 
    * Microsoft Azure 
    * Google Cloud 
    * S3-compatible object storage 
    * IBM Cloud® Object Storage S3 




Note

If you want to use CSI backup on OCP 4.11 and later, install OADP 1.1._x_. 

OADP 1.0._x_ does not support CSI backup on OCP 4.11 and later. OADP 1.0._x_ includes Velero 1.7._x_ and expects the API group `snapshot.storage.k8s.io/v1beta1`, which is not present on OCP 4.11 and later. 

  * To back up PVs with snapshots, you must have cloud storage that has a native snapshot API or supports Container Storage Interface (CSI) snapshots, such as the following providers: 

    * Amazon Web Services 
    * Microsoft Azure 
    * Google Cloud 
    * CSI snapshot-enabled cloud storage, such as Ceph RBD or Ceph FS 




Note

If you do not want to back up PVs by using snapshots, you can use [Restic](https://restic.net/), which is installed by the OADP Operator by default. 

## 1.2.2. Backing up and restoring applications

You back up applications by creating a `Backup` custom resource (CR). See [Creating a Backup CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#backing-up-applications "5.18.1. Backing up applications"). You can configure the following backup options: 

  * [Creating backup hooks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#backing-up-applications "5.18.1. Backing up applications") to run commands before or after the backup operation 
  * [Scheduling backups](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#backing-up-applications "5.18.1. Backing up applications")
  * [Backing up applications with File System Backup: Kopia or Restic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#backing-up-applications "5.18.1. Backing up applications")
  * You restore application backups by creating a `Restore` (CR). See [Creating a Restore CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-creating-restore-cr_restoring-applications "5.19.1.2. Create a Restore CR"). 
  * You can configure [restore hooks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-creating-restore-hooks_restoring-applications "5.19.1.3. Create restore hooks") to run commands in init containers or in the application container during the restore operation.
