# 7.5. View DNS Operator logs

You can view DNS Operator logs to troubleshoot DNS issues, verify configuration changes, and monitor activity by using the by using the `oc logs` command. 

**Procedure**

  * View the logs of the DNS Operator by running the following command: 

```shell-session
$ oc logs -n openshift-dns-operator deployment/dns-operator -c dns-operator
```
