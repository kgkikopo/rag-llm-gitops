# 1.2. Integrated OpenShift image registry

OpenShift Container Platform provides a built-in container image registry that runs as a standard workload on the cluster. An infrastructure Operator configures and manages the registry on top of existing cluster infrastructure. 

You can scale the registry up or down like any other cluster workload and the registry does not require specific infrastructure provisioning. The registry also integrates into the cluster user authentication and authorization system, which means that defining user permissions on image resources controls access to create and retrieve images. 

The registry is typically used as a publication target for images built on the cluster and as a source of images for workloads running on the cluster. When you push a new image to the registry, a notification gets sent to the cluster of the new image so that other components can react to and consume the updated image. 

Image data is stored in two locations. The actual image data is stored in a configurable storage location, such as cloud storage or a filesystem volume. The image metadata, which is exposed by the standard cluster APIs and is used to perform access control, is stored as standard API resources, specifically images and image streams. 

**Additional resources**

  * [Image Registry Operator in OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-operator "Chapter 2. Image Registry Operator in OpenShift Container Platform")
