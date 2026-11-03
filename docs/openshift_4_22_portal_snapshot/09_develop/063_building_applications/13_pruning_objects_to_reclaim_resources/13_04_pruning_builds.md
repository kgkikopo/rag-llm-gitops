# 13.4. Pruning builds

Prune obsolete build records and logs from your cluster to reclaim cluster storage and prevent API performance degradation. 

To prune builds that are no longer required by the system due to age and status, administrators can run the following command: 

```shell-session
$ oc adm prune builds [<options>]
```


Table 13.3. oc adm prune builds flagsOption| Description  
---|---  
`--confirm` |  Indicate that pruning should occur, instead of performing a dry-run.   
`--orphans` |  Prune all builds whose build configuration no longer exists, status is complete, failed, error, or canceled.   
`--keep-complete=<N>` |  Per build configuration, keep the last `N` builds whose status is complete. The default is `5`.   
`--keep-failed=<N>` |  Per build configuration, keep the last `N` builds whose status is failed, error, or canceled. The default is `1`.   
`--keep-younger-than=<duration>` |  Do not prune any object that is younger than `<duration>` relative to the current time. The default is `60m`.   
Show more

**Procedure**

  1. To see what a pruning operation would delete, run the following command: 

```shell-session
$ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m
```


  2. To actually perform the prune operation, add the `--confirm` flag: 

```shell-session
$ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m --confirm
```


Note

Developers can enable automatic build pruning by modifying their build configuration. 




**Additional resources**

  * [Performing advanced builds  Pruning builds](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_buildconfig/#builds-build-pruning_advanced-build-operations)
