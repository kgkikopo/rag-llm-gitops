# 4.1. Relocation of OpenShift Jenkins images

OpenShift Container Platform 4.11 makes significant changes to the location and availability of specific OpenShift Jenkins images. Additionally, you can configure when and how to update these images. 

**What stays the same with the OpenShift Jenkins images?**

  * The Cluster Samples Operator manages the `ImageStream` and `Template` objects for operating the OpenShift Jenkins images. 
  * By default, the Jenkins `DeploymentConfig` object from the Jenkins pod template triggers a redeployment when the Jenkins image changes. By default, this image is referenced by the `jenkins:2` image stream tag of Jenkins image stream in the `openshift` namespace in the `ImageStream` YAML file in the Samples Operator payload. 
  * If you upgrade from OpenShift Container Platform 4.10 and earlier to 4.11, the deprecated `maven` and `nodejs` pod templates are still in the default image configuration. 
  * If you upgrade from OpenShift Container Platform 4.10 and earlier to 4.11, the `jenkins-agent-maven` and `jenkins-agent-nodejs` image streams still exist in your cluster. To maintain these image streams, see the following section, "What happens with the `jenkins-agent-maven` and `jenkins-agent-nodejs` image streams in the `openshift` namespace?" 



**What changes in the support matrix of the OpenShift Jenkins image?**

Each new image in the `ocp-tools-4` repository in the `registry.redhat.io` registry supports multiple versions of OpenShift Container Platform. When Red Hat updates one of these new images, it is simultaneously available for all versions. This availability is ideal when Red Hat updates an image in response to a security advisory. Initially, this change applies to OpenShift Container Platform 4.11 and later. It is planned that this change will eventually apply to OpenShift Container Platform 4.9 and later. 

Previously, each Jenkins image supported only one version of OpenShift Container Platform and Red Hat might update those images sequentially over time. 

**What additions are there with the OpenShift Jenkins and Jenkins Agent Base ImageStream and ImageStreamTag objects?**

By moving from an in-payload image stream to an image stream that references non-payload images, OpenShift Container Platform can define additional image stream tags. Red Hat has created a series of new image stream tags to go along with the existing `"value": "jenkins:2"` and `"value": "image-registry.openshift-image-registry.svc:5000/openshift/jenkins-agent-base-rhel8:latest"` image stream tags present in OpenShift Container Platform 4.10 and earlier. These new image stream tags address some requests to improve how the Jenkins-related image streams are maintained. 

About the new image stream tags: 

`ocp-upgrade-redeploy`
     To update your Jenkins image when you upgrade OpenShift Container Platform, use this image stream tag in your Jenkins deployment configuration. This image stream tag corresponds to the existing `2` image stream tag of the `jenkins` image stream and the `latest` image stream tag of the `jenkins-agent-base-rhel8` image stream. It employs an image tag specific to only one SHA or image digest. When the `ocp-tools-4` image changes, such as for Jenkins security advisories, Red Hat Engineering updates the Cluster Samples Operator payload. 
`user-maintained-upgrade-redeploy`
     To manually redeploy Jenkins after you upgrade OpenShift Container Platform, use this image stream tag in your Jenkins deployment configuration. This image stream tag uses the least specific image version indicator available. When you redeploy Jenkins, run the following command: `$ oc import-image jenkins:user-maintained-upgrade-redeploy -n openshift`. When you issue this command, the OpenShift Container Platform `ImageStream` controller accesses the `registry.redhat.io` image registry and stores any updated images in the OpenShift image registry’s slot for that Jenkins `ImageStreamTag` object. Otherwise, if you do not run this command, your Jenkins deployment configuration does not trigger a redeployment. 
`scheduled-upgrade-redeploy`
     To automatically redeploy the latest version of the Jenkins image when it is released, use this image stream tag in your Jenkins deployment configuration. This image stream tag uses the periodic importing of image stream tags feature of the OpenShift Container Platform image stream controller, which checks for changes in the backing image. If the image changes, for example, due to a recent Jenkins security advisory, OpenShift Container Platform triggers a redeployment of your Jenkins deployment configuration. See "Configuring periodic importing of image stream tags" in the following "Additional resources." 

**What happens with the`jenkins-agent-maven` and `jenkins-agent-nodejs` image streams in the `openshift` namespace?**

The OpenShift Jenkins Maven and NodeJS Agent images for OpenShift Container Platform were deprecated in 4.10, and are removed from the OpenShift Container Platform install payload in 4.11. They do not have alternatives defined in the `ocp-tools-4` repository. However, you can work around this by using the sidecar pattern described in the "Jenkins agent" topic mentioned in the following "Additional resources" section. 

However, the Cluster Samples Operator does not delete the `jenkins-agent-maven` and `jenkins-agent-nodejs` image streams created by prior releases, which point to the tags of the respective OpenShift Container Platform payload images on `registry.redhat.io`. Therefore, you can pull updates to these images by running the following commands: 

```shell-session
$ oc import-image jenkins-agent-nodejs -n openshift
```


```shell-session
$ oc import-image jenkins-agent-maven -n openshift
```


**What OpenShift Container Platform architectures and versions does OpenShift Jenkins support?**

Jenkins supports the following architectures across OpenShift Container Platform releases: 

  * `amd64`
  * `arm64`
  * `ppc64le`
  * `s390x`



However, for OpenShift Container Platform Extended Update Support (EUS) releases, only the `amd64` architecture is officially supported. As a result, OpenShift Jenkins images are shipped exclusively for `amd64` on these releases. This is because the OpenShift Container Platform platform itself supports only the `amd64` architecture for EUS releases. For more information, see [Support Matrix for OpenShift Jenkins releases](https://access.redhat.com/articles/7115356). 

**When Red Hat updates Jenkins container images, are they available for all OpenShift Container Platform versions simultaneously?**

Yes, Jenkins container images are updated on a quarterly basis, and the updates are made available for all supported Jenkins images across all supported OpenShift Container Platform releases. 

**How long are the released Jenkins images supported?**

Red Hat supports only the latest Long-Term Support (LTS) version of the Jenkins core, as provided in our latest container images. We do not support multiple core versions. Our policy is to align with the latest Jenkins LTS version released by the upstream community. 

**Does the Jenkins release align with OpenShift Container Platform versions?**

Yes. Our goal is to maintain platform alignment. This means that Jenkins controller and agent images are built and tested for each supported OpenShift Container Platform releases. 

**Are Jenkins release timelines aligned with OpenShift Container Platform release cycles?**

Jenkins is no longer part of the OpenShift Container Platform core payload. Releases are managed separately. However, our intent is to publish updated OpenShift Jenkins images for newly released OpenShift Container Platform releases within a few weeks of the OpenShift Container Platform GA release. 

**Does Red Hat follow the upstream Jenkins lifecycle and LTS versions?**

Yes. We align with the Jenkins upstream lifecycle and follow the LTS version. Red Hat typically ships OpenShift Jenkins image updates quarterly unless a critical fix requires an out-of-cycle release. 

To verify the current Jenkins LTS version: - Navigate to the Jenkins Catalog  Packages section - Search for “Jenkins” - The result will show two packages, one of which is the Jenkins LTS package. 

**What is not supported?**

  * Jenkins versions older than the current OpenShift Jenkins LTS are not supported. 
  * Running OpenShift Jenkins and jenkins-agent-base outside of OpenShift Container Platform is not supported. 
  * Multiple core versions of Jenkins are not supported. Plugins bundled with our OpenShift Jenkins images follow the same versioning across all supported OpenShift Container Platform releases.
