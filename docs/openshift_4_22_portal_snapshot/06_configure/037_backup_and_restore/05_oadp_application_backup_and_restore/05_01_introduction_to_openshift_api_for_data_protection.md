# 5.1. Introduction to OpenShift API for Data Protection

Use OpenShift API for Data Protection (OADP) to safeguard applications, application-related cluster resources, persistent volumes, and internal images on OpenShift Container Platform. OADP backs up containerized applications and virtual machines (VMs). This helps you ensure disaster recovery. 

However, OADP does not serve as a disaster recovery solution for `etcd` or OpenShift Operators. 

Important

OADP support is applicable to customer workload namespaces and cluster scope resources. 

Full cluster `backup` and `restore` are not supported. 

## 5.1.1. OpenShift API for Data Protection APIs

OADP provides APIs that enable multiple approaches to customizing backups and preventing the inclusion of unnecessary or inappropriate resources. 

OADP provides the following APIs. See the _Additional resources_ section for more details. 

  * `Backup`
  * `Restore`
  * `Schedule`
  * `BackupStorageLocation`
  * `VolumeSnapshotLocation`



### 5.1.1.1. Support for OpenShift API for Data Protection

Review the OADP support matrix for version compatibility with OpenShift Container Platform releases and lifecycle policy information, including Extended Update Support (EUS) options. 

Table 5.1. Supported versions of OADPVersion| OpenShift Container Platform version| General availability| Full support ends| Maintenance ends| Extended Update Support (EUS)| Extended Update Support Term 2 (EUS Term 2)  
---|---|---|---|---|---|---  
1.6  | 

  * 4.22 

|  09 Jun 2026  |  Release of 1.7  |  Release of 1.8  |  30 Jun 2028  |  30 Jun 2029   
1.5  | 

  * 4.19 
  * 4.20 
  * 4.21 

|  17 June 2025  |  Release of 1.6  |  Release of 1.7  |  30 Jun 2028  EUS must be on OpenShift Container Platform 4.21  |  30 Jun 2029  EUS Term 2 must be on OpenShift Container Platform 4.21   
1.4  | 

  * 4.14 
  * 4.15 
  * 4.16 
  * 4.17 
  * 4.18 

|  10 Jul 2024  |  Release of 1.5  |  Release of 1.6  |  27 Jun 2026  EUS must be on OpenShift Container Platform 4.16  |  27 Jun 2027  EUS Term 2 must be on OpenShift Container Platform 4.16   
1.3  | 

  * 4.12 
  * 4.13 
  * 4.14 
  * 4.15 

|  29 Nov 2023  |  10 Jul 2024  |  Release of 1.5  |  31 Oct 2025  EUS must be on OpenShift Container Platform 4.14  |  31 Oct 2026  EUS Term 2 must be on OpenShift Container Platform 4.14   
Show more

#### 5.1.1.1.1. Unsupported versions of the OADP Operator

Table 5.2. Previous versions of the OADP Operator which are no longer supportedVersion| General availability| Full support ended| Maintenance ended  
---|---|---|---  
1.2  |  14 Jun 2023  |  29 Nov 2023  |  10 Jul 2024   
1.1  |  01 Sep 2022  |  14 Jun 2023  |  29 Nov 2023   
1.0  |  09 Feb 2022  |  01 Sep 2022  |  14 Jun 2023   
Show more

For more details about EUS, see [Extended Update Support](https://access.redhat.com/support/policy/updates/openshift#eus). 

For more details about EUS Term 2, see [Extended Update Support Term 2](https://access.redhat.com/support/policy/updates/openshift#eust2). 

**Additional resources**

  * [Backup](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#backing-up-applications "5.18.1. Backing up applications")
  * [Restore](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#restoring-applications "5.19.1. Restoring applications")
  * [Schedule](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-scheduling-backups-doc "5.18.8. Scheduling backups using Schedule CR")
  * [BackupStorageLocation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-about-backup-snapshot-locations_installing-oadp-aws "5.7.1.3. About backup and snapshot locations and their secrets")
  * [VolumeSnapshotLocation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-backing-up-pvs-csi-doc "5.18.5. Backing up persistent volumes with CSI snapshots")
  * [Backing up etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/control-plane-backup-and-restore#backup-etcd "6.1. Backing up and restoring etcd data")
