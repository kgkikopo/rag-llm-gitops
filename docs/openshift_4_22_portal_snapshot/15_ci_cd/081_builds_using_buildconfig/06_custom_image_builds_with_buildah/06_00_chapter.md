# Chapter 6. Custom image builds with Buildah

With OpenShift Container Platform 4.22, a docker socket will not be present on the host nodes. This means the _mount docker socket_ option of a custom build is not guaranteed to provide an accessible docker socket for use within a custom build image. 

If you require this capability in order to build and push images, add the Buildah tool your custom build image and use it to build and push the image within your custom build logic. The following is an example of how to run custom builds with Buildah. 

Note

Using the custom build strategy requires permissions that normal users do not have by default because it allows the user to execute arbitrary code inside a privileged container running on the cluster. This level of access can be used to compromise the cluster and therefore should be granted only to users who are trusted with administrative privileges on the cluster.

- [6.1. Prerequisites](06_01_prerequisites.md)
- [6.2. Creating custom build artifacts](06_02_creating_custom_build_artifacts.md)
- [6.3. Build custom builder image](06_03_build_custom_builder_image.md)
- [6.4. Use custom builder image](06_04_use_custom_builder_image.md)
