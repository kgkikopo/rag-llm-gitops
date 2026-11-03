# 10.2. Source-to-image

To create containerized applications in OpenShift Container Platform without manually configuring runtime environments, you can use Source-to-Image (S2I) images. S2I images are runtime base images for languages such as Node.js, Python, and Java that you can insert your code into. You can use Red Hat Software Collections images as a foundation for applications that rely on specific runtime environments, and access S2I images through the Cluster Samples Operator. 

## 10.2.1. Access S2I builder images in the OpenShift Container Platform Developer Console

You can access S2I builder images through the Developer Console in the web console. You need these images to build containerized applications from your source code. 

**Procedure**

  1. Log in to the OpenShift Container Platform web console using your login credentials. The default view for the OpenShift Container Platform web console is the **Administrator** perspective. 
  2. Use the perspective switcher to switch to the **Developer** perspective. 
  3. In the **+Add** view, use the **Project** drop-down list to select an existing project or create a new project. 
  4. Click **All services** in the **Developer Catalog** tile. 
  5. Click **Builder Images** under **Type** to see the available S2I images. 



## 10.2.2. Source-to-image build process overview

Source-to-image (S2I) is a build process in OpenShift Container Platform that injects your source code into a container image. S2I automates the creation of ready-to-run container images from your application source code without manual configuration. 

S2I performs the following steps: 

  1. Runs the `FROM <builder image>` command 
  2. Copies the source code to a defined location in the builder image 
  3. Runs the assemble script in the builder image 
  4. Sets the run script in the builder image as the default command 



Buildah then creates the container image. 

## 10.2.3. Additional resources

  * [Red Hat Software Collections container images](https://access.redhat.com/documentation/en-us/red_hat_software_collections/3/html-single/using_red_hat_software_collections_container_images/index)
  * [Introduction to source-to-image for OpenShift with Red Hat build of OpenJDK](https://docs.redhat.com/en/documentation/red_hat_build_of_openjdk/11/html/using_source-to-image_for_openshift_with_red_hat_build_of_openjdk_11/openjdk-overview-s2i-openshift)
  * [Configuring the Cluster Samples Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/images/configuring-samples-operator "Chapter 2. Configuring the Cluster Samples Operator")
  * [Using build strategies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_buildconfig/#builds-strategy-s2i-build_build-strategies)
  * [Troubleshooting the Source-to-Image process](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#troubleshooting-s2i)
  * [Creating images from source code with source-to-image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/images/creating-images#images-create-s2i_create-images "4.3. Create images from source code with source-to-image")
  * [About testing source-to-image images](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/images/creating-images#images-test-s2i_create-images "4.4. About testing source-to-image images")
