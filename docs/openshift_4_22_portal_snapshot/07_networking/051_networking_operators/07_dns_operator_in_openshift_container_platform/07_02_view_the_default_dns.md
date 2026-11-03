# 7.2. View the default DNS

View the default DNS resource and cluster DNS settings to verify the DNS configuration or troubleshoot DNS issues. 

Every new OpenShift Container Platform installation has a `dns.operator` named `default`. 

**Procedure**

  1. Use the `oc describe` command to view the default `dns`: 

```shell-session
$ oc describe dns.operator/default
```


**Example output**

```shell-session
Name:         default
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  operator.openshift.io/v1
Kind:         DNS
...
Status:
  Cluster Domain:  cluster.local
  Cluster IP:      172.30.0.10
...
```


where: 

`Status.Cluster Domain`
     Specifiecs the base DNS domain used to construct fully qualified pod and service domain names. 
`Status.Cluster IP`
     Specifies the address that pods query for name resolution. The IP is defined as the 10th address in the service CIDR range. 

  2. To find the service CIDR range, such as `172.30.0.0/16`, of your cluster, use the `oc get` command: 

```shell-session
$ oc get networks.config/cluster -o jsonpath='{$.status.serviceNetwork}'
```
