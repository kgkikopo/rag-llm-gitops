# 11.14. Configuring log levels for cert-manager and the cert-manager Operator for Red Hat OpenShift

To troubleshoot issues with the cert-manager components and the cert-manager Operator for Red Hat OpenShift, you can configure the log level verbosity. 

Note

To use different log levels for different cert-manager components, see _Customizing cert-manager Operator API fields_. 

## 11.14.1. Setting a log level for cert-manager

To troubleshoot issues and control log volume, configure the log level for the cert-manager Operator for Red Hat OpenShift. You can set specific verbosity levels to capture the necessary details for debugging or to reduce noise in your cluster logs. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have installed version 1.11.1 or later of the cert-manager Operator for Red Hat OpenShift. 



**Procedure**

  1. Edit the `CertManager` resource by running the following command: 

```shell-session
$ oc edit certmanager.operator cluster
```


  2. Set the log level value by editing the `spec.logLevel` section: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
...
spec:
  logLevel: <log_level>
```


The `CertManager` resource supports the following `logLevel` values: 

`Normal`
     Audits logs and records common operations. The default setting. Use this level when there are no issues. 
`Debug`
     Provides verbose logs. Use this level to troubleshoot minor issues. 
`Trace`
     Provides highly verbose logs. Use this level to troubleshoot major issues. 
`TraceAll`
    

Provides maximum log detail. Use this level to troubleshoot serious issues. 

Note

`TraceAll` generates huge amount of logs. After setting `logLevel` to `TraceAll`, you might experience performance issues. 

  3. Save your changes and quit the text editor to apply your changes. 

After applying the changes, the verbosity level for the cert-manager components controller, CA injector, and webhook is updated. 




## 11.14.2. Setting a log level for the cert-manager Operator for Red Hat OpenShift

To troubleshoot issues and control log volume, set the log level for the cert-manager Operator for Red Hat OpenShift. You can configure the verbosity of the Operator log messages to capture the specific details required for your environment. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have installed version 1.11.1 or later of the cert-manager Operator for Red Hat OpenShift. 



**Procedure**

  * Update the subscription object for cert-manager Operator for Red Hat OpenShift to provide the verbosity level for the operator logs by running the following command: 

```shell-session
$ oc -n cert-manager-operator patch subscription openshift-cert-manager-operator --type='merge' -p '{"spec":{"config":{"env":[{"name":"OPERATOR_LOG_LEVEL","value":"v"}]}}}'
```


Replace `v` with the desired log level number. The valid values for `v` can range from `1`to `10`. The default value is `2`. 




**Verification**

  1. The cert-manager Operator pod is redeployed. Verify that the log level of the cert-manager Operator for Red Hat OpenShift is updated by running the following command: 

```shell-session
$ oc set env deploy/cert-manager-operator-controller-manager -n cert-manager-operator --list | grep -e OPERATOR_LOG_LEVEL -e container
```


**Example output**

```shell-session
# deployments/cert-manager-operator-controller-manager, container kube-rbac-proxy
OPERATOR_LOG_LEVEL=9
# deployments/cert-manager-operator-controller-manager, container cert-manager-operator
OPERATOR_LOG_LEVEL=9
```


  2. Verify that the log level of the cert-manager Operator for Red Hat OpenShift is updated by running the `oc logs` command: 

```shell-session
$ oc logs deploy/cert-manager-operator-controller-manager -n cert-manager-operator
```


## 11.14.3. Additional resources

  * [Customizing cert-manager Operator API fields](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/cert-manager-operator-for-red-hat-openshift#cert-manager-customizing-api-fields "11.5. Customizing the cert-manager Operator by using the CertManager custom resource")
