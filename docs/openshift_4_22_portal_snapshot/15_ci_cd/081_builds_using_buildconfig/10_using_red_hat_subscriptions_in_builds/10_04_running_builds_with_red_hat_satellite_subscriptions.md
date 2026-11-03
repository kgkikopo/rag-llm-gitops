# 10.4. Running builds with Red Hat Satellite subscriptions

## 10.4.1. Adding Red Hat Satellite configurations to builds

Builds that use Red Hat Satellite to install content must provide appropriate configurations to obtain content from Satellite repositories. 

**Prerequisites**

  * You must provide or create a `yum`-compatible repository configuration file that downloads content from your Satellite instance. 

**Sample repository configuration**

```shell-session
[test-<name>]
name=test-<number>
baseurl = https://satellite.../content/dist/rhel/server/7/7Server/x86_64/os
enabled=1
gpgcheck=0
sslverify=0
sslclientkey = /etc/pki/entitlement/...-key.pem
sslclientcert = /etc/pki/entitlement/....pem
```


**Procedure**

  1. Create a `ConfigMap` object containing the Satellite repository configuration file by entering the following command: 

```shell-session
$ oc create configmap yum-repos-d --from-file /path/to/satellite.repo
```


  2. Add the Satellite repository configuration and entitlement key as a build volumes: 

```yaml
strategy:
  dockerStrategy:
    from:
      kind: ImageStreamTag
      name: ubi9:latest
    volumes:
    - name: yum-repos-d
      mounts:
      - destinationPath: /etc/yum.repos.d
      source:
        type: ConfigMap
        configMap:
          name: yum-repos-d
    - name: etc-pki-entitlement
      mounts:
      - destinationPath: /etc/pki/entitlement
      source:
        type: Secret
        secret:
          secretName: etc-pki-entitlement
```


## 10.4.2. Docker builds using Red Hat Satellite subscriptions

Docker strategy builds can use Red Hat Satellite repositories to install subscription content. 

**Prerequisites**

  * You have added the entitlement keys and Satellite repository configurations as build volumes. 



**Procedure**

  * Use the following example to create a `Dockerfile` for installing content with Satellite: 

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


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO28-1)
    

You must include the command to remove the `/etc/rhsm-host` directory and all its contents in your Dockerfile before executing any `yum` or `dnf` commands. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO28-2)
    

Contact your Satellite system administrator to find the correct repositories for the build’s installed packages. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO28-3)
    

You must restore the `/etc/rhsm-host` symbolic link to keep your image compatible with other Red Hat container images. 




**Additional resources**

  * [How to use builds with Red Hat Satellite subscriptions and which certificate to use](https://access.redhat.com/solutions/5847331)
