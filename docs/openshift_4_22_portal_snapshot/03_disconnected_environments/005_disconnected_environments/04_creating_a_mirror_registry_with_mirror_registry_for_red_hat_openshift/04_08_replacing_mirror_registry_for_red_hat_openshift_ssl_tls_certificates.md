# 4.8. Replacing mirror registry for Red Hat OpenShift SSL/TLS certificates

In some cases, you might want to update your SSL/TLS certificates for the _mirror registry for Red Hat OpenShift_. 

Use the following procedure to replace SSL/TLS certificates for the _mirror registry for Red Hat OpenShift_ in the following scenarios: 

  * If you are replacing the current _mirror registry for Red Hat OpenShift_ certificate. 
  * If you are using the same certificate as the previous _mirror registry for Red Hat OpenShift_ installation. 
  * If you are periodically updating the _mirror registry for Red Hat OpenShift_ certificate. 



**Prerequisites**

  * You have downloaded and installed the `./mirror-registry` binary from the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page. 



**Procedure**

  1. Enter the following command to install the _mirror registry for Red Hat OpenShift_ : 

```shell-session
$ ./mirror-registry install \
--quayHostname <host_example_com> \
--quayRoot <example_directory_name>
```


This installs the _mirror registry for Red Hat OpenShift_ to the `$HOME/quay-install` directory. 

  2. Prepare a new certificate authority (CA) bundle and generate new `ssl.key` and `ssl.crt` key files. For more information, see [Configuring SSL and TLS for Red Hat Quay](https://docs.redhat.com/en/documentation/red_hat_quay/3.15/html-single/securing_red_hat_quay/index#ssl-tls-quay-overview). 
  3. Assign `/$HOME/quay-install` an environment variable, for example, `QUAY`, by entering the following command: 

```shell-session
$ export QUAY=/$HOME/quay-install
```


  4. Copy the new `ssl.crt` file to the `/$HOME/quay-install` directory by entering the following command: 

```shell-session
$ cp ~/ssl.crt $QUAY/quay-config
```


  5. Copy the new `ssl.key` file to the `/$HOME/quay-install` directory by entering the following command: 

```shell-session
$ cp ~/ssl.key $QUAY/quay-config
```


  6. Restart the `quay-app` application pod by entering the following command: 

```shell-session
$ systemctl --user restart quay-app
```
