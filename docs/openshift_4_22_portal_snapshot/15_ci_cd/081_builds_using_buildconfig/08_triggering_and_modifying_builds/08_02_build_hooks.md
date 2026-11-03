# 8.2. Build hooks

Build hooks allow behavior to be injected into the build process. 

The `postCommit` field of a `BuildConfig` object runs commands inside a temporary container that is running the build output image. The hook is run immediately after the last layer of the image has been committed and before the image is pushed to a registry. 

The current working directory is set to the image’s `WORKDIR`, which is the default working directory of the container image. For most images, this is where the source code is located. 

The hook fails if the script or command returns a non-zero exit code or if starting the temporary container fails. When the hook fails it marks the build as failed and the image is not pushed to a registry. The reason for failing can be inspected by looking at the build logs. 

Build hooks can be used to run unit tests to verify the image before the build is marked complete and the image is made available in a registry. If all tests pass and the test runner returns with exit code `0`, the build is marked successful. In case of any test failure, the build is marked as failed. In all cases, the build log contains the output of the test runner, which can be used to identify failed tests. 

The `postCommit` hook is not only limited to running tests, but can be used for other commands as well. Since it runs in a temporary container, changes made by the hook do not persist, meaning that running the hook cannot affect the final image. This behavior allows for, among other uses, the installation and usage of test dependencies that are automatically discarded and are not present in the final image. 

## 8.2.1. Configuring post commit build hooks

There are different ways to configure the post-build hook. All forms in the following examples are equivalent and run `bundle exec rake test --verbose`. 

**Procedure**

  * Use one of the following options to configure post-build hooks: 

Option| Description  
---|---  
Shell script  |  `postCommit: script: "bundle exec rake test --verbose"` The `script` value is a shell script to be run with `/bin/sh -ic`. Use this option when a shell script is appropriate to execute the build hook. For example, for running unit tests as above. To control the image entry point or if the image does not have `/bin/sh`, use `command`, or `args`, or both.  Note The additional `-i` flag was introduced to improve the experience working with CentOS and RHEL images, and may be removed in a future release.   
Command as the image entry point  |  `postCommit: command: ["/bin/bash", "-c", "bundle exec rake test --verbose"]` In this form, `command` is the command to run, which overrides the image entry point in the exec form, as documented in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#entrypoint). This is needed if the image does not have `/bin/sh`, or if you do not want to use a shell. In all other cases, using `script` might be more convenient.   
Command with arguments  |  `postCommit: command: ["bundle", "exec", "rake", "test"] args: ["--verbose"]` This form is equivalent to appending the arguments to `command`.   
Show more




Note

Providing both `script` and `command` simultaneously creates an invalid build hook. 

## 8.2.2. Using the CLI to set post commit build hooks

The `oc set build-hook` command can be used to set the build hook for a build configuration. 

**Procedure**

  1. Complete one of the following actions: 

     * To set a command as the post-commit build hook, enter the following command: 

```shell-session
$ oc set build-hook bc/mybc \
    --post-commit \
    --command \
    -- bundle exec rake test --verbose
```


     * To set a script as the post-commit build hook, enter the following command: 

```shell-session
$ oc set build-hook bc/mybc --post-commit --script="bundle exec rake test --verbose"
```
