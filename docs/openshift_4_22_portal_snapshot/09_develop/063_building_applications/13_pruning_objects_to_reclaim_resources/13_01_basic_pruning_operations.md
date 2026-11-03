# 13.1. Basic pruning operations

Remove obsolete or unreferenced cluster objects to reclaim cluster storage and maintain optimal API server performance. 

The CLI groups prune operations under a common parent command: 

```shell-session
$ oc adm prune <object_type> <options>
```


This specifies: 

  * The `<object_type>` to perform the action on, such as `groups`, `builds`, `deployments`, or `images`. 
  * The `<options>` supported to prune that object type.
