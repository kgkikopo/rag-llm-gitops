# 3.4. Gathering kubelet logs

**Procedure**

  * After the kubelet’s log level verbosity is configured properly, you can gather logs by running the following commands: 

```shell-session
$ oc adm node-logs --role master -u kubelet
```


```shell-session
$ oc adm node-logs --role worker -u kubelet
```


Alternatively, inside the node, run the following command: 

```shell-session
$ journalctl -b -f -u kubelet.service
```


  * To collect master container logs, run the following command: 

```shell-session
$ sudo tail -f /var/log/containers/*
```


  * To directly gather the logs of all nodes, run the following command: 

```shell-session
- for n in $(oc get node --no-headers | awk '{print $1}'); do oc adm node-logs $n | gzip > $n.log.gz; done
```
