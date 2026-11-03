# 4.12. Troubleshooting mirror registry for Red Hat OpenShift

To assist in troubleshooting _mirror registry for Red Hat OpenShift_ , you can gather logs of systemd services installed by the mirror registry. 

The following services are installed: 

  * quay-app.service 
  * quay-redis.service 
  * quay-pod.service 



**Prerequisites**

  * You have installed _mirror registry for Red Hat OpenShift_. 



**Procedure**

  * If you installed _mirror registry for Red Hat OpenShift_ with root privileges, you can get the status information of its systemd services by entering the following command: 

```shell-session
$ sudo systemctl status <service>
```


  * If you installed _mirror registry for Red Hat OpenShift_ as a standard user, you can get the status information of its systemd services by entering the following command: 

```shell-session
$ systemctl --user status <service>
```
