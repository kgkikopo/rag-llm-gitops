# 20.2. Run LDAP sync

Review LDAP sync types before running group sync between your LDAP server and OpenShift Container Platform. Each type defines sync direction and scope so you select the command that matches your directory layout. 

After you have created a sync configuration file, you can begin to sync. OpenShift Container Platform allows administrators to perform several different sync types with the same server. 

## 20.2.1. Sync the LDAP server with OpenShift Container Platform

Sync all groups from your LDAP server with OpenShift Container Platform so you can mirror your complete LDAP group membership in the cluster. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `config.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync all groups from the LDAP server with OpenShift Container Platform by running the following command: 

```shell-session
$ oc adm groups sync --sync-config=config.yaml --confirm
```


Note

By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records. 




## 20.2.2. Sync OpenShift Container Platform groups with the LDAP server

Sync existing OpenShift Container Platform groups with your LDAP server so you can update membership for groups that already exist in the cluster. 

You can sync all groups already in OpenShift Container Platform that correspond to groups in the LDAP server specified in the configuration file. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `config.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * Sync OpenShift Container Platform groups with the LDAP server by running the following command: 

```shell-session
$ oc adm groups sync --type=openshift --sync-config=config.yaml --confirm
```


Note

By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records. 




## 20.2.3. Sync subgroups from the LDAP server with OpenShift Container Platform

Sync a subset of LDAP groups with OpenShift Container Platform so you can control which groups are synchronized using allowlist files, denylist files, or both. 

Note

You can use any combination of denylist files, allowlist files, or allowlist literals. Allowlist and denylist files must contain one unique group identifier per line, and you can include allowlist literals directly in the command itself. These guidelines apply to groups found on LDAP servers as well as groups already present in OpenShift Container Platform. 

**Prerequisites**

  * An LDAP sync configuration file exists. This procedure uses an example file named `config.yaml`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  * To sync groups using an allowlist file, run the following command: 

```shell-session
$ oc adm groups sync --whitelist=<allowlist_file> \
                   --sync-config=config.yaml      \
                   --confirm
```


  * To sync groups using a denylist file, run the following command: 

```shell-session
$ oc adm groups sync --blacklist=<denylist_file> \
                   --sync-config=config.yaml      \
                   --confirm
```


  * To sync a single group by the unique identifier of the group, run the following command: 

```shell-session
$ oc adm groups sync <group_unique_identifier>    \
                   --sync-config=config.yaml      \
                   --confirm
```


  * To sync a single group with both an allowlist and a denylist, run the following command: 

```shell-session
$ oc adm groups sync <group_unique_identifier>  \
                   --whitelist=<allowlist_file> \
                   --blacklist=<denylist_file> \
                   --sync-config=config.yaml    \
                   --confirm
```


  * To sync existing OpenShift Container Platform groups using an allowlist file, run the following command: 

```shell-session
$ oc adm groups sync --type=openshift           \
                   --whitelist=<allowlist_file> \
                   --sync-config=config.yaml    \
                   --confirm
```


Note

By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records.
