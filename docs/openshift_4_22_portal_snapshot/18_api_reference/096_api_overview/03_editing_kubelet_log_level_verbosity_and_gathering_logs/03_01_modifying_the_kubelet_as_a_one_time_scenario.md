# 3.1. Modifying the kubelet as a one-time scenario

To modify the kubelet in a one-time scenario without rebooting the node due to the change of `machine-config(spec":{"paused":false}})`, allowing you to modify the kubelet without affecting the service, follow this procedure. 

**Procedure**

  1. Connect to the node in debug mode: 

```shell-session
$ oc debug node/<node>
```


```shell-session
$ chroot /host
```


Alternatively, it is possible to SSH to the node and become root. 

  2. After access is established, check the default log level: 

```shell-session
$ systemctl cat kubelet
```


**Example output**

```shell-session
# /etc/systemd/system/kubelet.service.d/20-logging.conf
[Service]
Environment="KUBELET_LOG_LEVEL=2"
```


  3. Define the new verbosity required in a new `/etc/systemd/system/kubelet.service.d/30-logging.conf` file, which overrides `/etc/systemd/system/kubelet.service.d/20-logging.conf`. In this example, the verbosity is changed from `2` to `8`: 

```shell-session
$ echo -e "[Service]\nEnvironment=\"KUBELET_LOG_LEVEL=8\"" > /etc/systemd/system/kubelet.service.d/30-logging.conf
```


  4. Reload systemd and restart the service: 

```shell-session
$ systemctl daemon-reload
```


```shell-session
$ systemctl restart kubelet
```


  5. Gather the logs, and then revert the log level increase: 

```shell-session
$ rm -f /etc/systemd/system/kubelet.service.d/30-logging.conf
```


```shell-session
$ systemctl daemon-reload
```


```shell-session
$ systemctl restart kubelet
```
