# 1.1. OpenShift Builds

OpenShift Builds provides you the following options to configure and run a build: 

  * Builds using Shipwright is an extensible build framework based on the Shipwright project. You can use it to build container images on a cluster. You can build container images from source code and Dockerfile by using image build tools, such as Source-to-Image (S2I) and Buildah. 

For more information, see [builds for Red Hat OpenShift](https://docs.redhat.com/en/documentation/builds_for_red_hat_openshift). 

  * Builds using `BuildConfig` objects is a declarative build process to create cloud-native apps. You can define the build process in a YAML file that you use to create a `BuildConfig` object. This definition includes attributes such as build triggers, input parameters, and source code. When deployed, the `BuildConfig` object builds a runnable image and pushes the image to a container image registry. With the `BuildConfig` object, you can create a Docker, Source-to-image (S2I), or custom build. 

For more information, see [Understanding image builds](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_buildconfig/#understanding-image-builds).
