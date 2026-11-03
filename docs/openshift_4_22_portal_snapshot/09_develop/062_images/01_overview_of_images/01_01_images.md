# 1.1. Images

Container images are binaries that include all requirements for running a single container. You can use images to package applications and deploy them consistently across multiple containers and hosts in OpenShift Container Platform. 

Containers only have access to resources defined in the image unless you give the container additional access when creating it. By deploying the same image in multiple containers across multiple hosts and load balancing between them, OpenShift Container Platform can provide redundancy and horizontal scaling for a service packaged into an image. 

You can use the podman or `docker` CLI directly to build images, but OpenShift Container Platform also supplies builder images that assist with creating new images by adding your code or configuration to existing images. 

Because applications develop over time, a single image name can actually refer to many different versions of the same image. Each different image is referred to uniquely by its hash, a long hexadecimal number such as `fd44297e2ddb050ec4f…​`, which is usually shortened to 12 characters, such as `fd44297e2ddb`.
