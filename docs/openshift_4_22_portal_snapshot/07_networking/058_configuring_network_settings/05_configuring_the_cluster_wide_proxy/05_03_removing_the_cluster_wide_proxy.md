# 5.3. Removing the cluster-wide proxy

The `cluster` Proxy object cannot be deleted. To remove the cluster-wide proxy configuration from your OpenShift Container Platform cluster, you can remove all spec fields from the `Proxy` object by using the `oc edit` command. 

**Prerequisites**

  * Cluster administrator permissions 
  * OpenShift Container Platform `oc` CLI tool installed 



**Procedure**

  1. Use the `oc edit` command to modify the proxy: 

```shell-session
$ oc edit proxy/cluster
```


  2. Remove all `spec` fields from the Proxy object. For example: 

```yaml
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
spec: {}
```


  3. Save the file to apply the changes.
