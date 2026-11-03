# 2.4. Manually gathering logs without SSH access to your host(s)

Manually gather logs in situations where `must-gather` or automated collection methods do not work. 

If you do not have SSH access to your node, you can access the systems journal to investigate what is happening on your host. 

**Prerequisites**

  * Your OpenShift Container Platform installation must be complete. 
  * Your API service is still functional. 
  * You have system administrator privileges. 



**Procedure**

  1. Access `journald` unit logs under `/var/log` by running: 

```shell-session
$ oc adm node-logs --role=master -u kubelet
```


  2. Access host file paths under `/var/log` by running: 

```shell-session
$ oc adm node-logs --role=master --path=openshift-apiserver
```
