# 2.1. Jenkins agent images

The OpenShift Container Platform Jenkins agent images are available on [Quay.io](https://quay.io) or [registry.redhat.io](https://registry.redhat.io). 

Jenkins images are available through the Red Hat Registry: 

```shell-session
$ docker pull registry.redhat.io/ocp-tools-4/jenkins-rhel8:<image_tag>
```


```shell-session
$ docker pull registry.redhat.io/ocp-tools-4/jenkins-agent-base-rhel8:<image_tag>
```


To use these images, you can either access them directly from [Quay.io](https://quay.io) or [registry.redhat.io](https://registry.redhat.io) or push them into your OpenShift Container Platform container image registry.
