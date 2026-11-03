# 20.1. Use the must-gather tool

Use the must-gather tool to collect diagnostic information about Network Observability Operator resources, including pod logs and configuration details, to assist in troubleshooting cluster issues. 

**Procedure**

  1. Navigate to the directory where you want to store the must-gather data. 
  2. Run the following command to collect cluster-wide must-gather resources: 

```shell-session
$ oc adm must-gather
 --image-stream=openshift/must-gather \
 --image=quay.io/netobserv/must-gather
```
