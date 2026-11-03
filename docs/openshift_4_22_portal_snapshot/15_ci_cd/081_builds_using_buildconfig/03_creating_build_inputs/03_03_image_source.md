# 3.3. Image source

You can add additional files to the build process with images. Input images are referenced in the same way the `From` and `To` image targets are defined. This means both container images and image stream tags can be referenced. In conjunction with the image, you must provide one or more path pairs to indicate the path of the files or directories to copy the image and the destination to place them in the build context. 

The source path can be any absolute path within the image specified. The destination must be a relative directory path. At build time, the image is loaded and the indicated files and directories are copied into the context directory of the build process. This is the same directory into which the source repository content is cloned. If the source path ends in `/.` then the content of the directory is copied, but the directory itself is not created at the destination. 

Image inputs are specified in the `source` definition of the `BuildConfig`: 

```yaml
source:
  git:
    uri: https://github.com/openshift/ruby-hello-world.git
    ref: "master"
  images: 
```


1

```yaml
  - from: 
```


2

```yaml
      kind: ImageStreamTag
      name: myinputimage:latest
      namespace: mynamespace
    paths: 
```


3

```yaml
    - destinationDir: injected/dir 
```


4

```yaml
      sourcePath: /usr/lib/somefile.jar 
```


5

```yaml
  - from:
      kind: ImageStreamTag
      name: myotherinputimage:latest
      namespace: myothernamespace
    pullSecret: mysecret 
```


6

```yaml
    paths:
    - destinationDir: injected/dir
      sourcePath: /usr/lib/somefile.jar
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO3-1)
    

An array of one or more input images and files. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO3-2)
    

A reference to the image containing the files to be copied. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO3-3)
    

An array of source/destination paths. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO3-4)
    

The directory relative to the build root where the build process can access the file. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO3-5)
    

The location of the file to be copied out of the referenced image. 

[6](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO3-6)
    

An optional secret provided if credentials are needed to access the input image. 

Note

By default, if your cluster uses an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object to configure repository mirroring, you must use a global pull secret for mirrored registries. You cannot add an image pull secret to a project. 

However, you can configure a cluster-wide `CRIOCredentialProviderConfig` object to enable project-scoped image pull secrets that you can use with mirrored repositories. For more information, see "Configuring project-scoped image pull secrets for mirrored registries". 

**Images that require pull secrets**

When using an input image that requires a pull secret, you can link the pull secret to the service account used by the build. By default, builds use the `builder` service account. The pull secret is automatically added to the build if the secret contains a credential that matches the repository hosting the input image. To link a pull secret to the service account used by the build, run: 

```shell-session
$ oc secrets link builder dockerhub
```


Note

This feature is not supported for builds using the custom strategy. 

**Images on mirrored registries that require pull secrets**

When using an input image from a mirrored registry, if you get a `build error: failed to pull image` message, you can resolve the error by using either of the following methods: 

  * Create an input secret that contains the authentication credentials for the builder image’s repository and all known mirrors. In this case, create a pull secret for credentials to the image registry and its mirrors. 
  * Use the input secret as the pull secret on the `BuildConfig` object. 



**Additional resources**

  * [Configuring project-scoped image pull secrets for mirrored registries](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#images-configuration-registry-mirror-project-secret_image-configuration)
