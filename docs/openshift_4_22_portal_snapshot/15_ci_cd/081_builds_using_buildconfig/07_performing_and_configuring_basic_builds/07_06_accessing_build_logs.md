# 7.6. Accessing build logs

You can access build logs using the web console or the CLI. 

**Procedure**

  * To stream the logs using the build directly, enter the following command: 

```shell-session
$ oc describe build <build_name>
```


## 7.6.1. Accessing BuildConfig logs

You can access `BuildConfig` logs using the web console or the CLI. 

**Procedure**

  * To stream the logs of the latest build for a `BuildConfig`, enter the following command: 

```shell-session
$ oc logs -f bc/<buildconfig_name>
```


## 7.6.2. Accessing BuildConfig logs for a given version build

You can access logs for a given version build for a `BuildConfig` using the web console or the CLI. 

**Procedure**

  * To stream the logs for a given version build for a `BuildConfig`, enter the following command: 

```shell-session
$ oc logs --version=<number> bc/<buildconfig_name>
```


## 7.6.3. Enabling log verbosity

You can enable a more verbose output by passing the `BUILD_LOGLEVEL` environment variable as part of the `sourceStrategy` or `dockerStrategy` in a `BuildConfig`. 

Note

An administrator can set the default build verbosity for the entire OpenShift Container Platform instance by configuring `env/BUILD_LOGLEVEL`. This default can be overridden by specifying `BUILD_LOGLEVEL` in a given `BuildConfig`. You can specify a higher priority override on the command line for non-binary builds by passing `--build-loglevel` to `oc start-build`. 

Available log levels for source builds are as follows: 

Level 0  |  Produces output from containers running the `assemble` script and all encountered errors. This is the default.   
---|---  
Level 1  |  Produces basic information about the executed process.   
Level 2  |  Produces very detailed information about the executed process.   
Level 3  |  Produces very detailed information about the executed process, and a listing of the archive contents.   
Level 4  |  Currently produces the same information as level 3.   
Level 5  |  Produces everything mentioned on previous levels and additionally provides docker push messages.   
  
**Procedure**

  * To enable more verbose output, pass the `BUILD_LOGLEVEL` environment variable as part of the `sourceStrategy` or `dockerStrategy` in a `BuildConfig`: 

```yaml
sourceStrategy:
...
  env:
    - name: "BUILD_LOGLEVEL"
      value: "2" 
```


1

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/basic-build-operations#CO17-1)
    

Adjust this value to the desired log level.
