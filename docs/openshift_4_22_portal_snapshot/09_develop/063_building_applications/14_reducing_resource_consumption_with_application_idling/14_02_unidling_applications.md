# 14.2. Unidling applications

Restore normal application operations by scaling up the replicas when network traffic is directed back to the idled resources. 

Application services become active again when they receive network traffic and are scaled back up to their previous state. This includes both traffic to the services and traffic passing through routes. Applications can also be manually unidled by scaling up the resources. 

**Procedure**

  * To scale up a DeploymentConfig, run: 

```shell-session
$ oc scale --replicas=1 dc <dc_name>
```


Note

Automatic unidling by a router is currently only supported by the default HAProxy router.
