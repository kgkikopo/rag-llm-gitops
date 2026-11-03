# 5.3. Custom build

The custom build strategy allows developers to define a specific builder image responsible for the entire build process. Using your own builder image allows you to customize your build process. 

A custom builder image is a plain container image embedded with build process logic, for example for building RPMs or base images. 

Custom builds run with a high level of privilege and are not available to users by default. Only users who can be trusted with cluster administration permissions should be granted access to run custom builds. 

## 5.3.1. Using FROM image for custom builds

You can use the `customStrategy.from` section to indicate the image to use for the custom build. 

**Procedure**

  * Set the `customStrategy.from` section: 

```yaml
strategy:
  customStrategy:
    from:
      kind: "DockerImage"
      name: "openshift/sti-image-builder"
```


## 5.3.2. Using secrets in custom builds

In addition to secrets for source and images that can be added to all build types, custom strategies allow adding an arbitrary list of secrets to the builder pod. 

**Procedure**

  * To mount each secret at a specific location, edit the `secretSource` and `mountPath` fields of the `strategy` YAML file: 

```yaml
strategy:
  customStrategy:
    secrets:
      - secretSource: 
```


1

```yaml
          name: "secret1"
        mountPath: "/tmp/secret1" 
```


2

```yaml
      - secretSource:
          name: "secret2"
        mountPath: "/tmp/secret2"
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO13-1)
    

`secretSource` is a reference to a secret in the same namespace as the build. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO13-2)
    

`mountPath` is the path inside the custom builder where the secret should be mounted. 




## 5.3.3. Using environment variables for custom builds

To make environment variables available to the custom build process, you can add environment variables to the `customStrategy` definition of the build configuration. 

The environment variables defined there are passed to the pod that runs the custom build. 

**Procedure**

  1. Define a custom HTTP proxy to be used during build: 

```yaml
customStrategy:
...
  env:
    - name: "HTTP_PROXY"
      value: "http://myproxy.net:5187/"
```


  2. To manage environment variables defined in the build configuration, enter the following command: 

```shell-session
$ oc set env <enter_variables>
```


## 5.3.4. Using custom builder images

OpenShift Container Platform’s custom build strategy enables you to define a specific builder image responsible for the entire build process. When you need a build to produce individual artifacts such as packages, JARs, WARs, installable ZIPs, or base images, use a custom builder image using the custom build strategy. 

A custom builder image is a plain container image embedded with build process logic, which is used for building artifacts such as RPMs or base container images. 

Additionally, the custom builder allows implementing any extended build process, such as a CI/CD flow that runs unit or integration tests. 

### 5.3.4.1. Custom builder image

Upon invocation, a custom builder image receives the following environment variables with the information needed to proceed with the build: 

Table 5.2. Custom Builder Environment VariablesVariable Name| Description  
---|---  
`BUILD` |  The entire serialized JSON of the `Build` object definition. If you must use a specific API version for serialization, you can set the `buildAPIVersion` parameter in the custom strategy specification of the build configuration.   
`SOURCE_REPOSITORY` |  The URL of a Git repository with source to be built.   
`SOURCE_URI` |  Uses the same value as `SOURCE_REPOSITORY`. Either can be used.   
`SOURCE_CONTEXT_DIR` |  Specifies the subdirectory of the Git repository to be used when building. Only present if defined.   
`SOURCE_REF` |  The Git reference to be built.   
`ORIGIN_VERSION` |  The version of the OpenShift Container Platform master that created this build object.   
`OUTPUT_REGISTRY` |  The container image registry to push the image to.   
`OUTPUT_IMAGE` |  The container image tag name for the image being built.   
`PUSH_DOCKERCFG_PATH` |  The path to the container registry credentials for running a `podman push` operation.   
Show more

### 5.3.4.2. Custom builder workflow

Although custom builder image authors have flexibility in defining the build process, your builder image must adhere to the following required steps necessary for running a build inside of OpenShift Container Platform: 

  1. The `Build` object definition contains all the necessary information about input parameters for the build. 
  2. Run the build process. 
  3. If your build produces an image, push it to the output location of the build if it is defined. Other output locations can be passed with environment variables.
