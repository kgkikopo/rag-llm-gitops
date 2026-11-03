# 6.3. Build custom builder image

You can use OpenShift Container Platform to build and push custom builder images to use in a custom strategy. 

**Prerequisites**

  * Define all the inputs that will go into creating your new custom builder image. 



**Procedure**

  1. Define a `BuildConfig` object that will build your custom builder image: 

```shell-session
$ oc new-build --binary --strategy=docker --name custom-builder-image
```


  2. From the directory in which you created your custom build image, run the build: 

```shell-session
$ oc start-build custom-builder-image --from-dir . -F
```


After the build completes, your new custom builder image is available in your project in an image stream tag that is named `custom-builder-image:latest`.
