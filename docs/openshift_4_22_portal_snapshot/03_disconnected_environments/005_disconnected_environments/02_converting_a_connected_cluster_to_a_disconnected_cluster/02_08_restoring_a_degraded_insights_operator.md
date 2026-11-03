# 2.8. Restoring a degraded Insights Operator

Disconnecting the cluster from the network necessarily causes the cluster to lose the Internet connection. The Insights Operator becomes degraded because it requires access to Red Hat Lightspeed. 

For more information, see documentation on "Red Hat Lightspeed". 

Use the following procedure to recover from a degraded Insights Operator. 

**Procedure**

  1. Edit your `.dockerconfigjson` file to remove the `cloud.openshift.com` entry, for example: 

```shell-session
"cloud.openshift.com":{"auth":"<hash>","email":"user@example.com"}
```


  2. Save the file. 
  3. Update the cluster secret with the edited `.dockerconfigjson` file: 

```shell-session
$ oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson=./.dockerconfigjson
```


  4. Verify that the Insights Operator is no longer degraded: 

```shell-session
$ oc get co insights
```


**Example output**

```shell-session
NAME       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
insights   4.5.41    True        False         False      3d
```


**Additional resources**

  * [Red Hat Lightspeed](https://console.redhat.com)
