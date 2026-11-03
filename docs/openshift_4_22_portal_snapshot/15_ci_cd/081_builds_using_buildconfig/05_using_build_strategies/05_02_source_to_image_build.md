# 5.2. Source-to-image build

Source-to-image (S2I) is a tool for building reproducible container images. It produces ready-to-run images by injecting application source into a container image and assembling a new image. 

The new image incorporates the base image, the builder, and built source and is ready to use with the `buildah run` command. S2I supports incremental builds, which re-use previously downloaded dependencies, previously built artifacts, and so on. 

## 5.2.1. Perform source-to-image incremental builds

Source-to-image (S2I) can perform incremental builds, which means it reuses artifacts from previously-built images. 

See S2I Requirements for information on how to create a builder image supporting incremental builds. 

**Procedure**

  * To create an incremental build, create a with the following modification to the strategy definition: 

```yaml
strategy:
  sourceStrategy:
    from:
      kind: "ImageStreamTag"
      name: "incremental-image:latest"
    incremental: true
```


where: 

`strategy.sourceStrategy.from.name`
     Specifies an image that supports incremental builds. Consult the documentation of the builder image to determine if it supports this behavior. 
`strategy.sourceStrategy.incremental`
     Specifies whether an incremental build is attempted. If the builder image does not support incremental builds, the build will still succeed, but you will get a log message stating the incremental build was not successful because of a missing `save-artifacts` script. 




## 5.2.2. Override source-to-image builder image scripts

You can override the `assemble`, `run`, and `save-artifacts` source-to-image (S2I) scripts provided by the builder image. 

**Procedure**

  * To override the `assemble`, `run`, and `save-artifacts` S2I scripts provided by the builder image, complete one of the following actions: 

    * Provide an `assemble`, `run`, or `save-artifacts` script in the `.s2i/bin` directory of your application source repository. 
    * Provide a URL of a directory containing the scripts as part of the strategy definition in the `BuildConfig` object. For example: 

```yaml
strategy:
  sourceStrategy:
    from:
      kind: "ImageStreamTag"
      name: "builder-image:latest"
    scripts: "http://somehost.com/scripts_directory"
```


The build process appends `run`, `assemble`, and `save-artifacts` to the path. If any or all scripts with these names exist, the build process uses these scripts in place of scripts with the same name that are provided in the image. 

Note

Files located at the `scripts` URL take precedence over files located in `.s2i/bin` of the source repository. 




## 5.2.3. Source-to-image environment variables

There are two ways to make environment variables available to the source build process and resulting image: environment files and `BuildConfig` environment values. The variables that you provide using either method will be present during the build process and in the output image. 

### 5.2.3.1. Use source-to-image environment files

Source build enables you to set environment values, one per line, inside your application, by specifying them in a `.s2i/environment` file in the source repository. The environment variables specified in this file are present during the build process and in the output image. 

If you provide a `.s2i/environment` file in your source repository, source-to-image (S2I) reads this file during the build. This allows customization of the build behavior as the `assemble` script may use these variables. The complete list of supported environment variables is available in the using images section for each image. 

**Procedure**

  1. To disable assets compilation for your Rails application during the build, add the following line to the `.s2i/environment` file: 

```plaintext
DISABLE_ASSET_COMPILATION=true
```


  2. In addition to builds, the specified environment variables are also available in the running application itself. To start the Rails application in `development` mode instead of `production` mode, add the following line to the `.s2i/environment` file: 

```plaintext
RAILS_ENV=development
```


### 5.2.3.2. Using source-to-image build configuration environment

You can add environment variables to the `sourceStrategy` definition of the build configuration. The environment variables defined there are visible during the `assemble` script execution and will be defined in the output image, making them also available to the `run` script and application code. 

**Procedure**

  * For example, to disable assets compilation for your Rails application: 

```yaml
sourceStrategy:
...
  env:
    - name: "DISABLE_ASSET_COMPILATION"
      value: "true"
```


**Additional resources**

  * The build environment section provides more advanced instructions. 
  * You can also manage environment variables defined in the build configuration with the `oc set env` command. 



## 5.2.4. Ignore source-to-image source files

Source-to-image (S2I) supports a `.s2iignore` file, which contains a list of file patterns that should be ignored. Files in the build working directory, as provided by the various input sources, that match a pattern found in the `.s2iignore` file will not be made available to the `assemble` script. 

## 5.2.5. Create images from source code with source-to-image

Source-to-image (S2I) is a framework that makes it easy to write images that take application source code as an input and produce a new image that runs the assembled application as output. 

The main advantage of using S2I for building reproducible container images is the ease of use for developers. As a builder image author, you must understand two basic concepts in order for your images to provide the best S2I performance, the build process and S2I scripts. 

### 5.2.5.1. Understand the source-to-image build process

Leverage the Source-to-image (S2I) process in OpenShift Container Platform to seamlessly transform application source code into ready-to-run, reproducible container images. 

The build process consists of the following three fundamental elements, which are combined into a final container image: 

  * Sources 
  * S2I scripts 
  * Builder image 



S2I generates a Dockerfile with the builder image as the first `FROM` instruction. The Dockerfile generated by S2I is then passed to Buildah. 

### 5.2.5.2. How to write source-to-image scripts

Define mandatory Source-to-image (S2I) scripts, such as `assemble` and `run` to enable OpenShift Container Platform to build, customize, and execute highly reproducible container images. 

You can write S2I scripts in any programming language, as long as the scripts are executable inside the builder image. S2I supports multiple options providing `assemble`/`run`/`save-artifacts` scripts. All of these locations are checked on each build in the following order: 

  1. A script specified in the build configuration. 
  2. A script found in the application source `.s2i/bin` directory. 
  3. A script found at the default image URL with the `io.openshift.s2i.scripts-url` label. 



Both the `io.openshift.s2i.scripts-url` label specified in the image and the script specified in a build configuration can take one of the following forms: 

  * `image:///path_to_scripts_dir`: absolute path inside the image to a directory where the S2I scripts are located. 
  * `file:///path_to_scripts_dir`: relative or absolute path to a directory on the host where the S2I scripts are located. 
  * `http(s)://path_to_scripts_dir`: URL to a directory where the S2I scripts are located. 



Table 5.1. S2I scriptsScript| Description  
---|---  
`assemble` |  The `assemble` script builds the application artifacts from a source and places them into appropriate directories inside the image. This script is required. The workflow for this script is: 

  1. Optional: Restore build artifacts. If you want to support incremental builds, make sure to define `save-artifacts` as well. 
  2. Place the application source in the desired location. 
  3. Build the application artifacts. 
  4. Install the artifacts into locations appropriate for them to run. 

  
`run` |  The `run` script executes your application. This script is required.   
`save-artifacts` |  The `save-artifacts` script gathers all dependencies that can speed up the build processes that follow. This script is optional. For example: 

  * For Ruby, `gems` installed by Bundler. 
  * For Java, `.m2` contents. 

These dependencies are gathered into a `tar` file and streamed to the standard output.   
`usage` |  The `usage` script allows you to inform the user how to properly use your image. This script is optional.   
`test/run` |  The `test/run` script allows you to create a process to check if the image is working correctly. This script is optional. The proposed flow of that process is: 

  1. Build the image. 
  2. Run the image to verify the `usage` script. 
  3. Run `s2i build` to verify the `assemble` script. 
  4. Optional: Run `s2i build` again to verify the `save-artifacts` and `assemble` scripts save and restore artifacts functionality. 
  5. Run the image to verify the test application is working. 

Note The suggested location to put the test application built by your `test/run` script is the `test/test-app` directory in your image repository.   
Show more

**Example S2I scripts**

The following example S2I scripts are written in Bash. Each example assumes its `tar` contents are unpacked into the `/tmp/s2i` directory. 

**`assemble` script:**

```bash
#!/bin/bash

# restore build artifacts
if [ "$(ls /tmp/s2i/artifacts/ 2>/dev/null)" ]; then
    mv /tmp/s2i/artifacts/* $HOME/.
fi

# move the application source
mv /tmp/s2i/src $HOME/src

# build application artifacts
pushd ${HOME}
make all

# install the artifacts
make install
popd
```


**`run` script:**

```bash
#!/bin/bash

# run the application
/opt/application/run.sh
```


**`save-artifacts` script:**

```bash
#!/bin/bash

pushd ${HOME}
if [ -d deps ]; then
    # all deps contents to tar stream
    tar cf - deps
fi
popd
```


**`usage` script:**

```bash
#!/bin/bash

# inform the user how to use the image
cat <<EOF
This is a S2I sample builder image, to use it, install
https://github.com/openshift/source-to-image
EOF
```


**Additional resources**

  * [S2I Image Creation Tutorial](https://blog.openshift.com/create-s2i-builder-image/)



## 5.2.6. Using build volumes

You can mount build volumes to give running builds access to information that you do not want to persist in the output container image. 

Build volumes provide sensitive information, such as repository credentials, that the build environment or configuration only needs at build time. Build volumes are different from build inputs, whose data can persist in the output container image. 

The mount points of build volumes, from which the running build reads data, are functionally similar to [pod volume mounts](https://kubernetes.io/docs/concepts/storage/volumes/). 

**Prerequisites**

  * You have added an input secret, config map, or both to a BuildConfig object. 



**Procedure**

  * In the `sourceStrategy` definition of the `BuildConfig` object, add any build volumes to the `volumes` array. For example: 

```yaml
spec:
  sourceStrategy:
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
     Specifies the type of source: `ConfigMap`, `Secret`, or `CSI`. 
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
