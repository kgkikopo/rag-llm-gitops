# 13.2. Pruning groups

Remove stale user group records from external identity providers by using the group pruner. Pruning orphaned groups keeps user management data accurate, ensures cluster security, and prevents unauthorized access permissions. 

To prune groups records from an external provider, administrators can run the following command: 

```shell-session
$ oc adm prune groups \
    --sync-config=path/to/sync/config [<options>]
```


Table 13.1. oc adm prune groups flagsOptions| Description  
---|---  
`--confirm` |  Indicate that pruning should occur, instead of performing a dry-run.   
`--blacklist` |  Path to the group blacklist file.   
`--whitelist` |  Path to the group whitelist file.   
`--sync-config` |  Path to the synchronization configuration file.   
Show more

**Procedure**

  1. To see the groups that the prune command deletes, run the following command: 

```shell-session
$ oc adm prune groups --sync-config=ldap-sync-config.yaml
```


  2. To perform the prune operation, add the `--confirm` flag: 

```shell-session
$ oc adm prune groups --sync-config=ldap-sync-config.yaml --confirm
```
