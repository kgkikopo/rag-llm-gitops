# 20.2. Configure network traffic menu entry in the OpenShift Container Platform console

Restore a missing network traffic menu entry in the **Observe** menu of the OpenShift Container Platform console by manually registering the console plugin in the `FlowCollector` resource and the console operator configuration. 

**Prerequisites**

  * You have installed OpenShift Container Platform version 4.10 or newer. 



**Procedure**

  1. Check if the `spec.consolePlugin.register` field is set to `true` by running the following command: 

```shell-session
$ oc -n netobserv get flowcollector cluster -o yaml
```


**Example output**

```plaintext
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  consolePlugin:
    register: false
```


  2. Optional: Add the `netobserv-plugin` plugin by manually editing the Console Operator config: 

```shell-session
$ oc edit console.operator.openshift.io cluster
```


**Example output**

```plaintext
...
spec:
  plugins:
  - netobserv-plugin
...
```


  3. Optional: Set the `spec.consolePlugin.register` field to `true` by running the following command: 

```shell-session
$ oc -n netobserv edit flowcollector cluster -o yaml
```


**Example output**

```plaintext
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  consolePlugin:
    register: true
```


  4. Ensure the status of console pods is `running` by running the following command: 

```shell-session
$ oc get pods -n openshift-console -l app=console
```


  5. Restart the console pods by running the following command: 

```shell-session
$ oc delete pods -n openshift-console -l app=console
```


  6. Clear your browser cache and history. 
  7. Check the status of network observability plugin pods by running the following command: 

```shell-session
$ oc get pods -n netobserv -l app=netobserv-plugin
```


**Example output**

```plaintext
NAME                                READY   STATUS    RESTARTS   AGE
netobserv-plugin-68c7bbb9bb-b69q6   1/1     Running   0          21s
```


  8. Check the logs of the network observability plugin pods by running the following command: 

```shell-session
$ oc logs -n netobserv -l app=netobserv-plugin
```


**Example output**

```shell-session
time="2022-12-13T12:06:49Z" level=info msg="Starting netobserv-console-plugin [build version: , build date: 2022-10-21 15:15] at log level info" module=main
time="2022-12-13T12:06:49Z" level=info msg="listening on https://:9001" module=server
```
