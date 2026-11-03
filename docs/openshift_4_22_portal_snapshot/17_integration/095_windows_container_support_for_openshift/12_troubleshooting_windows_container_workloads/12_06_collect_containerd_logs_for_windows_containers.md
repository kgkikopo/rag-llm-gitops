# 12.6. Collect containerd logs for Windows containers

The Windows containerd container service does not stream log data to stdout, but instead, it streams log data to the Windows event log. You can view the containerd event logs to investigate issues you think might be caused by the Windows containerd container service. 

**Prerequisites**

  * You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM). 
  * You have created a Windows compute machine set. 



**Procedure**

  * View the containerd logs by running the following command: 

```shell-session
$ oc adm node-logs -l kubernetes.io/os=windows --path=containerd
```
