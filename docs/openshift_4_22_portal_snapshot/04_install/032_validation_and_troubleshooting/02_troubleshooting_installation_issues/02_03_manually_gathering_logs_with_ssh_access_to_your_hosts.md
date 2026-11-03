# 2.3. Manually gathering logs with SSH access to your hosts

Manually gather logs in situations where `must-gather` or automated collection methods do not work. 

Important

By default, SSH access to the OpenShift Container Platform nodes is disabled on the Red Hat OpenStack Platform (RHOSP) based installations. 

**Prerequisites**

  * You must have SSH access to your hosts. 



**Procedure**

  1. Collect the `bootkube.service` service logs from the bootstrap host by entering the `journalctl` command: 

```shell-session
$ journalctl -b -f -u bootkube.service
```


  2. Collect the container logs of the bootstrap host by using the podman logs. Podman logs are shown as a loop to get all of the container logs from the host. 

```shell-session
$ for pod in $(sudo podman ps -a -q); do sudo podman logs $pod; done
```


  3. Alternatively, collect the container logs of the host by entering the `tail` command: 

```shell-session
# tail -f /var/lib/containers/storage/overlay-containers/*/userdata/ctr.log
```


  4. Collect the `kubelet.service` and `crio.service` service logs from the control plane and compute hosts using the `journalctl` command by running: 

```shell-session
$ journalctl -b -f -u kubelet.service -u crio.service
```


  5. Collect the control plane and compute host container logs by entering the `tail` command: 

```shell-session
$ sudo tail -f /var/log/containers/*
```
