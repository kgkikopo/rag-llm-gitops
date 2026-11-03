# 7.4. Deleting a BuildConfig

You can delete a `BuildConfig` using the following command. 

**Procedure**

  * To delete a `BuildConfig`, enter the following command: 

```shell-session
$ oc delete bc <BuildConfigName>
```


This also deletes all builds that were instantiated from this `BuildConfig`. 

  * To delete a `BuildConfig` and keep the builds instatiated from the `BuildConfig`, specify the `--cascade=false` flag when you enter the following command: 

```shell-session
$ oc delete --cascade=false bc <BuildConfigName>
```
