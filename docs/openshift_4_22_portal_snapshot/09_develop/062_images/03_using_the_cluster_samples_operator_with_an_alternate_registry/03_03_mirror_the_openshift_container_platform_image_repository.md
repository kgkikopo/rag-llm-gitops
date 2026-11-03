# 3.3. Mirror the OpenShift Container Platform image repository

Mirror the OpenShift Container Platform image repository to your registry to use during cluster installation or upgrade. Complete the following steps on the mirror host. 

Important

The `oc adm release mirror` command is deprecated as of OpenShift Container Platform 4.22 and will be removed in a future release. 

As an alternative, use the oc-mirror plugin v2. 

**Prerequisites**

  * Your mirror host has access to the internet. 
  * You configured a mirror registry to use in your restricted network and can access the certificate and credentials that you configured. 
  * You downloaded the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and modified it to include authentication to your mirror repository. 
  * If you use self-signed certificates, you have specified a Subject Alternative Name in the certificates. 



**Procedure**

  1. Review the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290/) page to determine the version of OpenShift Container Platform that you want to install and determine the corresponding tag on the [Repository Tags](https://quay.io/repository/openshift-release-dev/ocp-release?tab=tags) page. 
  2. Set the following required environment variables: 

     1. Export the release version: 

```shell-session
$ OCP_RELEASE=<release_version>
```


For `<release_version>`, specify the tag that corresponds to the version of OpenShift Container Platform to install, such as `4.21.1`. 

     2. Export the local registry name and host port: 

```shell-session
$ LOCAL_REGISTRY='<local_registry_host_name>:<local_registry_host_port>'
```


For `<local_registry_host_name>`, specify the registry domain name for your mirror repository, and for `<local_registry_host_port>`, specify the port that it serves content on. 

     3. Export the local repository name: 

```shell-session
$ LOCAL_REPOSITORY='<local_repository_name>'
```


For `<local_repository_name>`, specify the name of the repository to create in your registry, such as `ocp4/openshift4`. 

     4. Export the name of the repository to mirror: 

```shell-session
$ PRODUCT_REPO='openshift-release-dev'
```


For a production release, you must specify `openshift-release-dev`. 

     5. Export the path to your registry pull secret: 

```shell-session
$ LOCAL_SECRET_JSON='<path_to_pull_secret>'
```


For `<path_to_pull_secret>`, specify the absolute path to and file name of the pull secret for your mirror registry that you created. 

     6. Export the release mirror: 

```shell-session
$ RELEASE_NAME="ocp-release"
```


For a production release, you must specify `ocp-release`. 

     7. Export the type of architecture for your cluster: 

```shell-session
$ ARCHITECTURE=<cluster_architecture>
```


Specify the architecture of the cluster, such as `x86_64`, `aarch64`, `s390x`, or `ppc64le`. 

     8. Export the path to the directory to host the mirrored images: 

```shell-session
$ REMOVABLE_MEDIA_PATH=<path>
```


Specify the full path, including the initial forward slash (/) character. 

  3. Mirror the version images to the mirror registry: 

     * If your mirror host does not have internet access, take the following actions: 

       1. Connect the removable media to a system that is connected to the internet. 
       2. Review the images and configuration manifests to mirror: 

```shell-session
$ oc adm release mirror -a ${LOCAL_SECRET_JSON}  \
     --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE} \
     --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} \
     --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE} --dry-run
```


       3. Record the entire `imageContentSources` section from the output of the previous command. The information about your mirrors is unique to your mirrored repository, and you must add the `imageContentSources` section to the `install-config.yaml` file during installation. 
       4. Mirror the images to a directory on the removable media: 

```shell-session
$ oc adm release mirror -a ${LOCAL_SECRET_JSON} --to-dir=${REMOVABLE_MEDIA_PATH}/mirror quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE}
```


       5. Take the media to the restricted network environment and upload the images to the local container registry. 

```shell-session
$ oc image mirror -a ${LOCAL_SECRET_JSON} --from-dir=${REMOVABLE_MEDIA_PATH}/mirror "file://openshift/release:${OCP_RELEASE}*" ${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}
```


For the `REMOVABLE_MEDIA_PATH` variable, you must use the same path that you specified when you mirrored the images. 

Important

Running the `oc image mirror` command might result in the following error: `error: unable to retrieve source image`. This error occurs when image indexes include references to images that no longer exist on the image registry. Image indexes might retain older references to allow users running those images an upgrade path to newer points on the upgrade graph. As a temporary workaround, you can use the `--skip-missing` option to bypass the error and continue downloading the image index. For more information, see [Service Mesh Operator mirroring failed](https://access.redhat.com/solutions/6975305). 

     * If the local container registry is connected to the mirror host, take the following actions: 

       1. Directly push the release images to the local registry by using following command: 

```shell-session
$ oc adm release mirror -a ${LOCAL_SECRET_JSON}  \
     --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE} \
     --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} \
     --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}
```


This command pulls the release information as a digest, and its output includes the `imageContentSources` data that you require when you install your cluster. 

       2. Record the entire `imageContentSources` section from the output of the previous command. The information about your mirrors is unique to your mirrored repository, and you must add the `imageContentSources` section to the `install-config.yaml` file during installation. 

Note

The image name gets patched to Quay.io during the mirroring process, and the Podman images will show Quay.io in the registry on the bootstrap virtual machine. 

  4. To create the installation program that is based on the content that you mirrored, extract it and pin it to the release: 

     * If your mirror host does not have internet access, run the following command: 

```shell-session
$ oc adm release extract -a ${LOCAL_SECRET_JSON} --icsp-file=<file> --command=openshift-install "${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}" \
--insecure=true
```


Optional: If you do not want to configure trust for the target registry, add the `--insecure=true` flag. 

     * If the local container registry is connected to the mirror host, run the following command: 

```shell-session
$ oc adm release extract -a ${LOCAL_SECRET_JSON} --command=openshift-install "${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}"
```


Important

To ensure that you use the correct images for the version of OpenShift Container Platform that you selected, you must extract the installation program from the mirrored content. 

You must perform this step on a machine with an active internet connection. 

  5. For clusters using installer-provisioned infrastructure, run the following command: 

```shell-session
$ openshift-install
```
