# 5.4. Verifying the cluster-wide proxy configuration

To verify that your cluster-wide proxy configuration is working correctly in OpenShift Container Platform, you can check the `Proxy` object status, review Machine Config Operator logs, and confirm that system components are routing external requests through the proxy. 

**Prerequisites**

  * You have cluster administrator permissions. 
  * You have the OpenShift Container Platform `oc` CLI tool installed. 



**Procedure**

  1. Check the proxy configuration status using the `oc` command: 

```shell-session
$ oc get proxy/cluster -o yaml
```


  2. Verify the proxy fields in the output to ensure they match your configuration. Specifically, check the `spec.httpProxy`, `spec.httpsProxy`, `spec.noProxy`, and `spec.trustedCA` fields. 
  3. Inspect the status of the `Proxy` object: 

```shell-session
$ oc get proxy/cluster -o jsonpath='{.status}'
```


**Example output**

```shell-session
{
status:
    httpProxy: http://user:xxx@xxxx:3128
    httpsProxy: http://user:xxx@xxxx:3128
    noProxy: .cluster.local,.svc,10.0.0.0/16,10.128.0.0/14,127.0.0.1,169.254.169.254,172.30.0.0/16,localhost,test.no-proxy.com
}
```


  4. Check the logs of the Machine Config Operator (MCO) to ensure that the configuration changes were applied successfully: 

```shell-session
$ oc logs -n openshift-machine-config-operator $(oc get pods -n openshift-machine-config-operator -l k8s-app=machine-config-operator -o name)
```


  5. Look for messages that indicate the proxy settings were applied and the nodes were rebooted if necessary. 
  6. Verify that system components are using the proxy by checking the logs of a component that makes external requests, such as the Cluster Version Operator (CVO): 

```shell-session
$ oc logs -n openshift-cluster-version $(oc get pods -n openshift-cluster-version -l k8s-app=machine-config-operator -o name)
```


  7. Look for log entries that show that external requests have been routed through the proxy.
