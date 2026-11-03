# 7.8. Setting the CoreDNS Operator log level

You can configure the Operator log level to quickly track down OpenShift DNS issues. 

The valid values for `operatorLogLevel` are `Normal`, `Debug`, and `Trace`. `Trace` has the most detailed information. The default `operatorlogLevel` is `Normal`. There are seven logging levels for Operator issues: Trace, Debug, Info, Warning, Error, Unrecoverable, and Panic. After the logging level is set, log entries with that severity or anything above it will be logged. 

  * `operatorLogLevel: "Normal"` sets `logrus.SetLogLevel("Info")`. 
  * `operatorLogLevel: "Debug"` sets `logrus.SetLogLevel("Debug")`. 
  * `operatorLogLevel: "Trace"` sets `logrus.SetLogLevel("Trace")`. 



**Procedure**

  * To set `operatorLogLevel` to `Debug`, enter the following command: 

```shell-session
$ oc patch dnses.operator.openshift.io/default -p '{"spec":{"operatorLogLevel":"Debug"}}' --type=merge
```


  * To set `operatorLogLevel` to `Trace`, enter the following command: 

```shell-session
$ oc patch dnses.operator.openshift.io/default -p '{"spec":{"operatorLogLevel":"Trace"}}' --type=merge
```


**Verification**

  1. To review the resulting change, enter the following command: 

```shell-session
$ oc get dnses.operator -A -oyaml
```


You should see two log level entries. The `operatorLogLevel` applies to OpenShift DNS Operator issues, and the `logLevel` applies to the daemonset of CoreDNS pods: 

```yaml
 logLevel: Trace
 operatorLogLevel: Debug
```


  2. To review the logs for the daemonset, enter the following command: 

```shell-session
$ oc logs -n openshift-dns ds/dns-default
```
