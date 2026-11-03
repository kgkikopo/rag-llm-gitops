# Chapter 4. Important changes to OpenShift Jenkins images

Important

Openshift Jenkins receives periodic updates from Jenkins LTS releases and associated plugins. These updates may include bug fixes, security vulnerability patches, and occasionally new features. However, Red Hat does not plan to introduce further enhancements or major changes to the functionality or contents of the OpenShift Jenkins container image, other than updates to its dependent plugins. 

Additionally, the following three Red Hat-maintained Jenkins plugins are now in maintenance mode. Only critical bug fixes will be addressed, and no new enhancements or feature development are planned. 

  * Jenkins Client Plugin 
  * Jenkins Login Plugin 
  * Jenkins Sync Plugin 



OpenShift Container Platform 4.11 moves the OpenShift Jenkins and OpenShift Agent Base images to the `ocp-tools-4` repository at `registry.redhat.io`. It also removes the OpenShift Jenkins Maven and NodeJS Agent images from its payload: 

  * OpenShift Container Platform 4.11 moves the OpenShift Jenkins and OpenShift Agent Base images to the `ocp-tools-4` repository at `registry.redhat.io` so that Red Hat can produce and update the images outside the OpenShift Container Platform lifecycle. Previously, these images were in the OpenShift Container Platform install payload and the `openshift4` repository at `registry.redhat.io`. 
  * OpenShift Container Platform 4.10 deprecated the OpenShift Jenkins Maven and NodeJS Agent images. OpenShift Container Platform 4.11 removes these images from its payload. Red Hat no longer produces these images, and they are not available from the `ocp-tools-4` repository at `registry.redhat.io`. Red Hat maintains the 4.10 and earlier versions of these images for any significant bug fixes or security CVEs, following the [OpenShift Container Platform lifecycle policy](https://access.redhat.com/support/policy/updates/openshift). 



These changes support the OpenShift Container Platform 4.10 recommendation to use [multiple container Pod Templates with the Jenkins Kubernetes Plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#images-other-jenkins-config-kubernetes_images-other-jenkins "1.6. Configuring the Jenkins Kubernetes plugin").

- [4.1. Relocation of OpenShift Jenkins images](04_01_relocation_of_openshift_jenkins_images.md)
- [4.2. Customizing the Jenkins image stream tag](04_02_customizing_the_jenkins_image_stream_tag.md)
- [4.3. About the OpenShift CLI tool in OpenShift Jenkins images](04_03_about_the_openshift_cli_tool_in_openshift_jenkins_images.md)
- [4.4. OpenShift Jenkins release compared to bundled oc client version table](04_04_openshift_jenkins_release_compared_to_bundled_oc_client_version_table.md)
- [4.5. Specifying a fixed oc client version for OpenShift Jenkins images](04_05_specifying_a_fixed_oc_client_version_for_openshift_jenkins_images.md)
- [4.6. Additional resources](04_06_additional_resources.md)
