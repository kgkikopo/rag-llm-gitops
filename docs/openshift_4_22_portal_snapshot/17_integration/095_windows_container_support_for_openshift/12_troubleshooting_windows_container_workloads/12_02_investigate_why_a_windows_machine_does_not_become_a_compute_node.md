# 12.2. Investigate why a Windows machine does not become a compute node

There are various reasons why a Windows Machine does not become a compute node. The best way to investigate this problem is to collect the Windows Machine Config Operator (WMCO) logs. 

**Prerequisites**

  * You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM). 
  * You have created a Windows compute machine set. 



**Procedure**

  * Run the following command to collect the WMCO logs: 

```shell-session
$ oc logs -f deployment/windows-machine-config-operator -n openshift-windows-machine-config-operator
```
