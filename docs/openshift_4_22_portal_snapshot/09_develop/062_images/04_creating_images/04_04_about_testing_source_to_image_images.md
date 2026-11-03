# 4.4. About testing source-to-image images

Verify your Source-to-image (S2I) environment and resulting application images to ensure successful, reproducible container deployment within OpenShift Container Platform. 

As an S2I builder image author, you can test your S2I image locally and use the OpenShift Container Platform build system for automated testing and continuous integration. 

S2I requires the `assemble` and `run` scripts to be present to successfully run the S2I build. Providing the `save-artifacts` script reuses the build artifacts, and providing the `usage` script ensures that usage information is printed to console when someone runs the container image outside of the S2I. 

The goal of testing an S2I image is to make sure that all of these described commands work properly, even if the base container image has changed or the tooling used by the commands was updated. 

## 4.4.1. Understanding testing requirements

The standard location for the `test` script is `test/run`. This script is invoked by the OpenShift Container Platform S2I image builder and it could be a simple Bash script or a static Go binary. 

The `test/run` script performs the S2I build, so you must have the S2I binary available in your `$PATH`. If required, follow the S2I installation instructions in the _Additional resources_. 

S2I combines the application source code and builder image, so to test it you need a sample application source to verify that the source successfully transforms into a runnable container image. The sample application should be simple, but it should exercise the crucial steps of `assemble` and `run` scripts. 

## 4.4.2. Generating scripts and tools

The S2I tooling includes powerful generation tools to speed up the process of creating a new S2I image. The `s2i create` command produces all the necessary S2I scripts and testing tools along with the `Makefile`: 

```shell-session
$ s2i create <image_name> <destination_directory>
```


The generated `test/run` script must be adjusted to be useful, but it provides a good starting point to begin developing. 

Note

The `test/run` script produced by the `s2i create` command requires that the sample application sources are inside the `test/test-app` directory. 

## 4.4.3. Testing locally

The easiest way to run the S2I image tests locally is to use the generated `Makefile`. 

If you did not use the `s2i create` command, you can copy the following `Makefile` template and replace the `IMAGE_NAME` parameter with your image name. 

**Sample`Makefile`**

```plaintext
IMAGE_NAME = openshift/ruby-20-centos7
CONTAINER_ENGINE := $(shell command -v podman 2> /dev/null | echo docker)

build:
	${CONTAINER_ENGINE} build -t $(IMAGE_NAME) .

.PHONY: test
test:
	${CONTAINER_ENGINE} build -t $(IMAGE_NAME)-candidate .
	IMAGE_NAME=$(IMAGE_NAME)-candidate test/run
```


## 4.4.4. Basic testing workflow

The `test` script assumes you have already built the image you want to test. If required, first build the S2I image. Run one of the following commands: 

  * If you use Podman, run the following command: 

```shell-session
$ podman build -t <builder_image_name>
```


  * If you use Docker, run the following command: 

```shell-session
$ docker build -t <builder_image_name>
```


The following steps describe the default workflow to test S2I image builders: 

  1. Verify the `usage` script is working: 

     * If you use Podman, run the following command: 

```shell-session
$ podman run <builder_image_name> .
```


     * If you use Docker, run the following command: 

```shell-session
$ docker run <builder_image_name> .
```


  2. Build the image: 

```shell-session
$ s2i build file:///path-to-sample-app _<BUILDER_IMAGE_NAME>_ _<OUTPUT_APPLICATION_IMAGE_NAME>_
```


  3. Optional: if you support `save-artifacts`, run step 2 once again to verify that saving and restoring artifacts works properly. 
  4. Run the container: 

     * If you use Podman, run the following command: 

```shell-session
$ podman run <output_application_image_name>
```


     * If you use Docker, run the following command: 

```shell-session
$ docker run <output_application_image_name>
```


  5. Verify the container is running and the application is responding. 



Running these steps is generally enough to tell if the builder image is working as expected. 

## 4.4.5. Using OpenShift Container Platform for building the image

Once you have a `Dockerfile` and the other artifacts that make up your new S2I builder image, you can put them in a git repository and use OpenShift Container Platform to build and push the image. Define a Docker build that points to your repository. 

If your OpenShift Container Platform instance is hosted on a public IP address, the build can be triggered each time you push into your S2I builder image GitHub repository. 

You can also use the `ImageChangeTrigger` to trigger a rebuild of your applications that are based on the S2I builder image you updated.
