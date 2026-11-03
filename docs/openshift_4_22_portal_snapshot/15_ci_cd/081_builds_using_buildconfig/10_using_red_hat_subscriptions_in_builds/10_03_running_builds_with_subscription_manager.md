# 10.3. Running builds with Subscription Manager

## 10.3.1. Docker builds using Subscription Manager

Docker strategy builds can use `yum` or `dnf` to install additional Red Hat Enterprise Linux (RHEL) packages. 

**Prerequisites**

  * The entitlement keys must be added as build strategy volumes. 



**Procedure**

  * Use the following as an example Dockerfile to install content with the Subscription Manager: 

```plaintext
FROM registry.redhat.io/ubi9/ubi:latest
RUN rm -rf /etc/rhsm-host 
```


1

```plaintext
RUN yum --enablerepo=codeready-builder-for-rhel-9-x86_64-rpms install \ 
```


2

```plaintext
    nss_wrapper \
    uid_wrapper -y && \
    yum clean all -y
RUN ln -s /run/secrets/rhsm /etc/rhsm-host 
```


3

```plaintext

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO27-1)
    

You must include the command to remove the `/etc/rhsm-host` directory and all its contents in your Dockerfile before executing any `yum` or `dnf` commands. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO27-2)
    

Use the [Red Hat Package Browser](https://access.redhat.com/downloads/content/package-browser) to find the correct repositories for your installed packages. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO27-3)
    

You must restore the `/etc/rhsm-host` symbolic link to keep your image compatible with other Red Hat container images.
