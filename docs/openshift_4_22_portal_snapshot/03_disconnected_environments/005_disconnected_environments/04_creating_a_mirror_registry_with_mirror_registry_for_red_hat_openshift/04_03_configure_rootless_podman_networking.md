# 4.3. Configure rootless Podman networking

To restore rootless Podman networking when the default `pasta` stack fails on OpenShift Container Platform mirror or install hosts, you can set the default rootless network back to `slirp4netns` in the `/etc/containers/containers.conf` file, or in the user’s `~/.config/containers/container.conf` file. 

You might need to configure rootless Podman networking after upgrading to RHEL 9.5 or Podman 5.0. In these versions, the default networking stack changed from `slirp4netns` to `pasta`. As a result, systems that previously operated without a default route might no longer be able to establish network connectivity and could display the following error: 

```shell-session
Error: pasta failed with exit code 1:
External interface not usable
```


**Prerequisites**

  * You have updated to RHEL 9.5 or Podman 5.0. 



**Procedure**

  1. Use your preferred IDE to modify the `/etc/containers/containers.conf` or `~/.config/containers/container.conf` file. 

     1. To modify the `/etc/containers/containers.conf` file, enter the following command: 

```shell-session
$ nano /etc/containers/containers.conf
```


     2. To modify the `~/.config/containers/container.conf` file, enter the following command: 

```shell-session
$ nano ~/.config/containers/container.conf
```


  2. Add, or update, the `[network]` section as in the following example: 

```plaintext
# ...
[network]
default_rootless_network_cmd = "slirp4netns"
# ...
```


  3. Restart the Podman system as the rootless user by entering the following command. Note that all containers must be stopped and restarted for the change to take effect. 

```shell-session
$ podman system migrate
```
