# 6.7. Working with image streams

To organize and manage container images in OpenShift Container Platform, you can use image streams and image stream tags. By using image streams, you can track image versions and simplify deployments. 

Important

Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components. 

The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects. 

## 6.7.1. Get information about image streams

To efficiently manage and monitor your image streams in OpenShift Container Platform, you can get general information about the image stream and detailed information about all the tags it is pointing to, ensuring your deployed applications rely on the correct image versions. 

**Procedure**

  * To get general information about the image stream and detailed information about all the tags it is pointing to, enter the following command: 

```shell-session
$ oc describe is/<image-name>
```


For example: 

```shell-session
$ oc describe is/python
```


**Example output**

```shell-session
Name:			python
Namespace:		default
Created:		About a minute ago
Labels:			<none>
Annotations:		openshift.io/image.dockerRepositoryCheck=2017-10-02T17:05:11Z
Docker Pull Spec:	docker-registry.default.svc:5000/default/python
Image Lookup:		local=false
Unique Images:		1
Tags:			1

3.5
  tagged from centos/python-35-centos7

  * centos/python-35-centos7@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
      About a minute ago
```


  * To get all of the information available about a particular image stream tag, enter the following command: 

```shell-session
$ oc describe istag/<image-stream>:<tag-name>
```


For example: 

```shell-session
$ oc describe istag/python:latest
```


**Example output**

```shell-session
Image Name:	sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
Docker Image:	centos/python-35-centos7@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
Name:		sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
Created:	2 minutes ago
Image Size:	251.2 MB (first layer 2.898 MB, last binary layer 72.26 MB)
Image Created:	2 weeks ago
Author:		<none>
Arch:		amd64
Entrypoint:	container-entrypoint
Command:	/bin/sh -c $STI_SCRIPTS_PATH/usage
Working Dir:	/opt/app-root/src
User:		1001
Exposes Ports:	8080/tcp
Docker Labels:	build-date=20170801
```


Note

More information is output than shown. 

  * Enter the following command to discover which architecture or operating system that an image stream tag supports: 

```shell-session
$ oc get istag <image-stream-tag> -ojsonpath="{range .image.dockerImageManifests[*]}{.os}/{.architecture}{'\n'}{end}"
```


For example: 

```shell-session
$ oc get istag busybox:latest -ojsonpath="{range .image.dockerImageManifests[*]}{.os}/{.architecture}{'\n'}{end}"
```


**Example output**

```shell-session
linux/amd64
linux/arm
linux/arm64
linux/386
linux/mips64le
linux/ppc64le
linux/riscv64
linux/s390x
```


## 6.7.2. Add tags to an image stream

To accurately manage and track specific versions of your container images, add tags to your image streams within OpenShift Container Platform, This ensures reliable referencing and deployment throughout your environment. 

**Procedure**

  * Add a tag that points to one of the existing tags by using the `oc tag`command: 

```shell-session
$ oc tag <image-name:tag1> <image-name:tag2>
```


For example: 

```shell-session
$ oc tag python:3.5 python:latest
```


**Example output**

```shell-session
Tag python:latest set to python@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25.
```


  * Confirm the image stream has two tags, one, `3.5`, pointing at the external container image and another tag, `latest`, pointing to the same image because it was created based on the first tag. 

```shell-session
$ oc describe is/python
```


**Example output**

```shell-session
Name:			python
Namespace:		default
Created:		5 minutes ago
Labels:			<none>
Annotations:		openshift.io/image.dockerRepositoryCheck=2017-10-02T17:05:11Z
Docker Pull Spec:	docker-registry.default.svc:5000/default/python
Image Lookup:		local=false
Unique Images:		1
Tags:			2

latest
  tagged from python@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25

  * centos/python-35-centos7@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
      About a minute ago

3.5
  tagged from centos/python-35-centos7

  * centos/python-35-centos7@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
      5 minutes ago
```


## 6.7.3. Add tags for an external image

To enable OpenShift Container Platform resources to track and consume container images sourced from external registries, add tags to the corresponding image streams. This action integrates external image content securely into your cluster’s local image management system. 

**Procedure**

  * Add tags pointing to internal or external images, by using the `oc tag` command for all tag-related operations: 

```shell-session
$ oc tag <repository/image> <image-name:tag>
```


For example, this command maps the `docker.io/python:3.6.0` image to the `3.6` tag in the `python` image stream. 

```shell-session
$ oc tag docker.io/python:3.6.0 python:3.6
```


**Example output**

```shell-session
Tag python:3.6 set to docker.io/python:3.6.0.
```


If the external image is secured, you must create a secret with credentials for accessing that registry. 




## 6.7.4. Update image stream tags

To maintain flexibility and consistency in deployment definitions, update an image stream tag to reflect a different tag in OpenShift Container Platform. Specifically, you can update a tag to reflect another tag in an image stream, which is essential for managing image versions effectively. 

**Procedure**

  * Update a tag: 

```shell-session
$ oc tag <image-name:tag> <image-name:latest>
```


For example, the following updates the `latest` tag to reflect the `3.6` tag in an image stream: 

```shell-session
$ oc tag python:3.6 python:latest
```


**Example output**

```shell-session
Tag python:latest set to python@sha256:438208801c4806548460b27bd1fbcb7bb188273d13871ab43f.
```


## 6.7.5. Remove image stream tags

To maintain control over your image history and simplify management within OpenShift Container Platform, you can remove old tags from an image stream. This action helps ensure that your resources track only the current and necessary image references. 

**Procedure**

  * Remove old tags from an image stream: 

```shell-session
$ oc tag -d <image-name:tag>
```


For example: 

```shell-session
$ oc tag -d python:3.6
```


**Example output**

```shell-session
Deleted tag default/python:3.6
```


**Additional resources**

  * [Remove deprecated image stream tags from the Cluster Samples Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/images/configuring-samples-operator#images-samples-operator-deprecated-image-stream_configuring-samples-operator "2.6. Remove deprecated image stream tags from the Cluster Samples Operator")



## 6.7.6. Configure periodic importing of image stream tags

To maintain up-to-date image definitions from an external container image registry, configure periodic importing of image stream tags. This process allows you to quickly re-import images for critical security updates by using the `--scheduled` flag. 

**Procedure**

  1. Schedule importing images: 

```shell-session
$ oc tag <repository/image> <image-name:tag> --scheduled
```


For example: 

```shell-session
$ oc tag docker.io/python:3.6.0 python:3.6 --scheduled
```


**Example output**

```shell-session
Tag python:3.6 set to import docker.io/python:3.6.0 periodically.
```


This command causes OpenShift Container Platform to periodically update this particular image stream tag. This period is a cluster-wide setting set to 15 minutes by default. 

  2. Remove the periodic check, re-run above command but omit the `--scheduled` flag. This will reset its behavior to default. 

```shell-session
$ oc tag <repositiory/image> <image-name:tag>
```
