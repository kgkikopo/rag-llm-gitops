# 5.8. Querying bootstrap node journal logs

If you experience bootstrap-related issues, you can gather `bootkube.service` `journald` unit logs and container logs from the bootstrap node. 

**Prerequisites**

  * You have SSH access to your bootstrap node. 
  * You have the fully qualified domain name of the bootstrap node. 



**Procedure**

  1. Query `bootkube.service` `journald` unit logs from a bootstrap node during OpenShift Container Platform installation. Replace `<bootstrap_fqdn>` with the bootstrap node’s fully qualified domain name: 

```shell-session
$ ssh core@<bootstrap_fqdn> journalctl -b -f -u bootkube.service
```


Note

The `bootkube.service` log on the bootstrap node outputs etcd `connection refused` errors, indicating that the bootstrap server is unable to connect to etcd on control plane nodes. After etcd has started on each control plane node and the nodes have joined the cluster, the errors should stop. 

  2. Collect logs from the bootstrap node containers using `podman` on the bootstrap node. Replace `<bootstrap_fqdn>` with the bootstrap node’s fully qualified domain name: 

```shell-session
$ ssh core@<bootstrap_fqdn> 'for pod in $(sudo podman ps -a -q); do sudo podman logs $pod; done'
```
