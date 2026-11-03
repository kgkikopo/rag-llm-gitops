# 7.7. Viewing the CoreDNS logs

You can view CoreDNS pod logs to troubleshoot DNS issues by using the `oc logs` command. 

**Procedure**

  * View the logs of a specific CoreDNS pod by entering the following command: 

```shell-session
$ oc -n openshift-dns logs -c dns <core_dns_pod_name>
```


  * Follow the logs of all CoreDNS pods by entering the following command: 

```shell-session
$ oc -n openshift-dns logs -c dns -l dns.operator.openshift.io/daemonset-dns=default -f --max-log-requests=<number> 
```


1

```shell-session

```


    * `<number>`: Specifies the number of DNS pods to stream logs from. The maximum is 6.
