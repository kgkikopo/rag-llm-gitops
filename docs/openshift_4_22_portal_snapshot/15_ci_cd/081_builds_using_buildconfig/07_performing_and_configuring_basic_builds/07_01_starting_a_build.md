# 7.1. Starting a build

You can manually start a new build from an existing build configuration in your current project. 

**Procedure**

  * To start a build manually, enter the following command: 

```shell-session
$ oc start-build <buildconfig_name>
```


## 7.1.1. Re-running a build

You can manually re-run a build using the `--from-build` flag. 

**Procedure**

  * To manually re-run a build, enter the following command: 

```shell-session
$ oc start-build --from-build=<build_name>
```


## 7.1.2. Streaming build logs

You can specify the `--follow` flag to stream the build’s logs in `stdout`. 

**Procedure**

  * To manually stream a build’s logs in `stdout`, enter the following command: 

```shell-session
$ oc start-build <buildconfig_name> --follow
```


## 7.1.3. Setting environment variables when starting a build

You can specify the `--env` flag to set any desired environment variable for the build. 

**Procedure**

  * To specify a desired environment variable, enter the following command: 

```shell-session
$ oc start-build <buildconfig_name> --env=<key>=<value>
```


## 7.1.4. Starting a build with source

Rather than relying on a Git source pull or a Dockerfile for a build, you can also start a build by directly pushing your source, which could be the contents of a Git or SVN working directory, a set of pre-built binary artifacts you want to deploy, or a single file. This can be done by specifying one of the following options for the `start-build` command: 

Option| Description  
---|---  
`--from-dir=<directory>` |  Specifies a directory that will be archived and used as a binary input for the build.   
`--from-file=<file>` |  Specifies a single file that will be the only file in the build source. The file is placed in the root of an empty directory with the same file name as the original file provided.   
`--from-repo=<local_source_repo>` |  Specifies a path to a local repository to use as the binary input for a build. Add the `--commit` option to control which branch, tag, or commit is used for the build.   
Show more

When passing any of these options directly to the build, the contents are streamed to the build and override the current build source settings. 

Note

Builds triggered from binary input will not preserve the source on the server, so rebuilds triggered by base image changes will use the source specified in the build configuration. 

**Procedure**

  * To start a build from a source code repository and send the contents of a local Git repository as an archive from the tag `v2`, enter the following command: 

```shell-session
$ oc start-build hello-world --from-repo=../hello-world --commit=v2
```
