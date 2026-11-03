# 2.2. Pulling the Driver Toolkit container image

You can pull the `driver-toolkit` image from the Red Hat Ecosystem Catalog or extract its URL from the OpenShift Container Platform release payload by using the `oc adm` CLI. 

The `driver-toolkit` image is available from the [Container images section of the Red Hat Ecosystem Catalog](https://registry.redhat.io/) and in the OpenShift Container Platform release payload. The image corresponding to the most recent minor release of OpenShift Container Platform will be tagged with the version number in the catalog. The image URL for a specific release can be found using the `oc adm` CLI command. 

Instructions for pulling the `driver-toolkit` image from `registry.redhat.io` with `podman` or in OpenShift Container Platform can be found on the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/openshift4/driver-toolkit-rhel8/604009d6122bd89307e00865?container-tabs=gti). The driver-toolkit image for the latest minor release is tagged with the minor release version on `registry.redhat.io`, for example: `registry.redhat.io/openshift4/driver-toolkit-rhel8:v4.22`. 

**Prerequisites**

  * You obtained the image [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). 
  * You installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Use the `oc adm` command to extract the image URL of the `driver-toolkit` corresponding to a certain release: 

     * For an x86 image, the command is as follows: 

```shell-session
$ oc adm release info quay.io/openshift-release-dev/ocp-release:4.22.z-x86_64 --image-for=driver-toolkit
```


     * For an ARM image, the command is as follows: 

```shell-session
$ oc adm release info quay.io/openshift-release-dev/ocp-release:4.22.z-aarch64 --image-for=driver-toolkit
```


**Example output**

```shell-session
quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:b53883ca2bac5925857148c4a1abc300ced96c222498e3bc134fe7ce3a1dd404
```


  2. Obtain this image using a valid pull secret, such as the pull secret required to install OpenShift Container Platform: 

```shell-session
$ podman pull --authfile=path/to/pullsecret.json quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:<SHA>
```
