# 6.4. Use custom builder image

You can define a `BuildConfig` object that uses the custom strategy in conjunction with your custom builder image to execute your custom build logic. 

**Prerequisites**

  * Define all the required inputs for new custom builder image. 
  * Build your custom builder image. 



**Procedure**

  1. Create a file named `buildconfig.yaml`. This file defines the `BuildConfig` object that is created in your project and executed: 

```yaml
kind: BuildConfig
apiVersion: build.openshift.io/v1
metadata:
  name: sample-custom-build
  labels:
    name: sample-custom-build
  annotations:
    template.alpha.openshift.io/wait-for-ready: 'true'
spec:
  strategy:
    type: Custom
    customStrategy:
      forcePull: true
      from:
        kind: ImageStreamTag
        name: custom-builder-image:latest
        namespace: <yourproject> 
```


1

```yaml
  output:
    to:
      kind: ImageStreamTag
      name: sample-custom:latest
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/custom-builds-buildah#CO16-1)
    

Specify your project name. 

  2. Create the `BuildConfig` object by entering the following command: 

```shell-session
$ oc create -f buildconfig.yaml
```


  3. Create a file named `imagestream.yaml`. This file defines the image stream to which the build will push the image: 

```yaml
kind: ImageStream
apiVersion: image.openshift.io/v1
metadata:
  name: sample-custom
spec: {}
```


  4. Create the image stream by entering the following command: 

```shell-session
$ oc create -f imagestream.yaml
```


  5. Run your custom build by entering the following command: 

```shell-session
$ oc start-build sample-custom-build -F
```


When the build runs, it launches a pod running the custom builder image that was built earlier. The pod runs the `build.sh` logic that is defined as the entrypoint for the custom builder image. The `build.sh` logic invokes Buildah to build the `dockerfile.sample` that was embedded in the custom builder image, and then uses Buildah to push the new image to the `sample-custom image stream`.
