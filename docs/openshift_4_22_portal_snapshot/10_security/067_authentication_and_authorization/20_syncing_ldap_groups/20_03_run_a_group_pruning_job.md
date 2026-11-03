# 20.3. Run a group pruning job

Run a group pruning job to remove LDAP-synced groups from OpenShift Container Platform when they no longer exist on your LDAP server so you can keep cluster group records aligned with your directory. 

**Procedure**

  * Prune groups using a sync configuration file by running the following command: 

```shell-session
$ oc adm prune groups --sync-config=/path/to/ldap-sync-config.yaml --confirm
```


  * Prune groups using an allowlist file by running the following command: 

```shell-session
$ oc adm prune groups --whitelist=/path/to/whitelist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
```


  * Prune groups using a denylist file by running the following command: 

```shell-session
$ oc adm prune groups --blacklist=/path/to/blacklist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
```
