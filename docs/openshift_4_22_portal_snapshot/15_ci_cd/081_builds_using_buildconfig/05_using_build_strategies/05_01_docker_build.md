# 5.1. Docker build

OpenShift Container Platform uses Buildah to build a container image from a Dockerfile. For more information on building container images with Dockerfiles, see [the Dockerfile reference documentation](https://docs.docker.com/engine/reference/builder/). 

Tip

If you set Docker build arguments by using the `buildArgs` array, see [Understand how ARG and FROM interact](https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact) in the Dockerfile reference documentation. 

## 5.1.1. Replacing the Dockerfile FROM image

You can replace the `FROM` instruction of the Dockerfile with the `from` parameters of the `BuildConfig` object. If the Dockerfile uses multi-stage builds, the image in the last `FROM` instruction will be replaced. 

**Procedure**

  * To replace the `FROM` instruction of the Dockerfile with the `from` parameters of the `BuildConfig` object, add the following settings to the `BuildConfig` object: 

```yaml
strategy:
  dockerStrategy:
    from:
      kind: "ImageStreamTag"
      name: "debian:latest"
```


## 5.1.2. Using Dockerfile path

By default, docker builds use a Dockerfile located at the root of the context specified in the `BuildConfig.spec.source.contextDir` field. 

The `dockerfilePath` field allows the build to use a different path to locate your Dockerfile, relative to the `BuildConfig.spec.source.contextDir` field. It can be a different file name than the default Dockerfile, such as `MyDockerfile`, or a path to a Dockerfile in a subdirectory, such as `dockerfiles/app1/Dockerfile`. 

**Procedure**

  * Set the `dockerfilePath` field for the build to use a different path to locate your Dockerfile: 

```yaml
strategy:
  dockerStrategy:
    dockerfilePath: dockerfiles/app1/Dockerfile
```


## 5.1.3. Using docker environment variables

To make environment variables available to the docker build process and resulting image, you can add environment variables to the `dockerStrategy` definition of the build configuration. 

The environment variables defined there are inserted as a single `ENV` Dockerfile instruction right after the `FROM` instruction, so that it can be referenced later on within the Dockerfile. 

The variables are defined during build and stay in the output image, therefore they will be present in any container that runs that image as well. 

For example, defining a custom HTTP proxy to be used during build and runtime: 

```yaml
dockerStrategy:
...
  env:
    - name: "HTTP_PROXY"
      value: "http://myproxy.net:5187/"
```


You can also manage environment variables defined in the build configuration with the `oc set env` command. 

## 5.1.4. Adding Docker build arguments

You can set [Docker build arguments](https://docs.docker.com/engine/reference/builder/#arg) using the `buildArgs` array. The build arguments are passed to Docker when a build is started. 

Tip

See [Understand how ARG and FROM interact](https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact) in the Dockerfile reference documentation. 

**Procedure**

  * To set Docker build arguments, add entries to the `buildArgs` array, which is located in the `dockerStrategy` definition of the `BuildConfig` object. For example: 

```yaml
dockerStrategy:
...
  buildArgs:
    - name: "version"
      value: "latest"
```


Note

Only the `name` and `value` fields are supported. Any settings on the `valueFrom` field are ignored. 




## 5.1.5. Squashing layers with docker builds

Docker builds normally create a layer representing each instruction in a Dockerfile. Setting the `imageOptimizationPolicy` to `SkipLayers` merges all instructions into a single layer on top of the base image. 

**Procedure**

  * Set the `imageOptimizationPolicy` to `SkipLayers`: 

```yaml
strategy:
  dockerStrategy:
    imageOptimizationPolicy: SkipLayers
```


## 5.1.6. Using build volumes

You can mount build volumes to give running builds access to information that you do not want to persist in the output container image. 

Build volumes provide sensitive information, such as repository credentials, that the build environment or configuration only needs at build time. Build volumes are different from build inputs, whose data can persist in the output container image. 

The mount points of build volumes, from which the running build reads data, are functionally similar to [pod volume mounts](https://kubernetes.io/docs/concepts/storage/volumes/). 

**Prerequisites**

  * You have added an input secret, config map, or both to a BuildConfig object. 



**Procedure**

  * In the `dockerStrategy` definition of the `BuildConfig` object, add any build volumes to the `volumes` array. For example: 

```yaml
spec:
  dockerStrategy:
    volumes:
      - name: secret-mvn
        mounts:
        - destinationPath: /opt/app-root/src/.ssh
        source:
          type: Secret
          secret:
            secretName: my-secret
      - name: settings-mvn
        mounts:
        - destinationPath: /opt/app-root/src/.m2
        source:
          type: ConfigMap
          configMap:
            name: my-config
      - name: my-csi-volume
        mounts:
        - destinationPath: /opt/app-root/src/some_path
        source:
          type: CSI
          csi:
            driver: csi.sharedresource.openshift.io
            readOnly: true
            volumeAttributes:
              attribute: value
```


where: 

`name`
     Specifies a unique name. 
`destinationPath`
     Specifies the absolute path of the mount point. It must not contain `..` or `:` and does not collide with the destination path generated by the builder. The `/opt/app-root/src` is the default home directory for many Red Hat S2I-enabled images. 
`type`
     Specifies the type of source, `ConfigMap`, `Secret`, or `CSI`. 
`secretName`
     Specifies the name of the source. 
`driver`
     Specifies the driver that provides the ephemeral CSI volume. 
`readOnly`
     Specifies that a read-only volume is provided. This value must be set to `true`. 
`volumeAttributes`
     (Optional) Specifies the volume attributes of the ephemeral CSI volume. Consult the CSI driver’s documentation for supported attribute keys and values. 




**Additional resources**

  * [Build inputs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#builds-define-build-inputs_creating-build-inputs "3.1. Build inputs")
  * [Input secrets and config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#builds-input-secrets-configmaps_creating-build-inputs "3.6. Input secrets and config maps")
