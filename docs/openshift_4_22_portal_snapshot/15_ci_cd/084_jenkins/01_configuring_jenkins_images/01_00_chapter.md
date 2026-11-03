# Chapter 1. Configuring Jenkins images

OpenShift Container Platform provides a container image for running Jenkins. This image provides a Jenkins server instance, which can be used to set up a basic flow for continuous testing, integration, and delivery. 

The image is based on the Red Hat Universal Base Images (UBI). 

OpenShift Container Platform follows the [LTS](https://jenkins.io/changelog-stable/) release of Jenkins. OpenShift Container Platform provides an image that contains Jenkins 2.x. 

The OpenShift Container Platform Jenkins images are available on [Quay.io](https://quay.io) or [registry.redhat.io](https://registry.redhat.io). 

For example: 

```shell-session
$ podman pull registry.redhat.io/ocp-tools-4/jenkins-rhel8:<image_tag>
```


To use these images, you can either access them directly from these registries or push them into your OpenShift Container Platform container image registry. Additionally, you can create an image stream that points to the image, either in your container image registry or at the external location. Your OpenShift Container Platform resources can then reference the image stream. 

But for convenience, OpenShift Container Platform provides image streams in the `openshift` namespace for the core Jenkins image as well as the example Agent images provided for OpenShift Container Platform integration with Jenkins.

- [1.1. Configuration and customization](01_01_configuration_and_customization.md)
- [1.2. Jenkins environment variables](01_02_jenkins_environment_variables.md)
- [1.3. Providing Jenkins cross project access](01_03_providing_jenkins_cross_project_access.md)
- [1.4. Jenkins cross volume mount points](01_04_jenkins_cross_volume_mount_points.md)
- [1.5. Customizing the Jenkins image through source-to-image](01_05_customizing_the_jenkins_image_through_source_to_image.md)
- [1.6. Configuring the Jenkins Kubernetes plugin](01_06_configuring_the_jenkins_kubernetes_plugin.md)
- [1.7. Jenkins permissions](01_07_jenkins_permissions.md)
- [1.8. Creating a Jenkins service from a template](01_08_creating_a_jenkins_service_from_a_template.md)
- [1.9. Using the Jenkins Kubernetes plugin](01_09_using_the_jenkins_kubernetes_plugin.md)
- [1.10. Jenkins memory requirements](01_10_jenkins_memory_requirements.md)
- [1.11. Additional resources](01_11_additional_resources.md)
