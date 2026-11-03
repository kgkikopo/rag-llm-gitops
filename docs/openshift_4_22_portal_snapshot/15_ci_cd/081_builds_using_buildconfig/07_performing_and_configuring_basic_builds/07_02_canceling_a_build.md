# 7.2. Canceling a build

You can cancel a build using the web console, or with the following CLI command. 

**Procedure**

  * To manually cancel a build, enter the following command: 

```shell-session
$ oc cancel-build <build_name>
```


## 7.2.1. Canceling multiple builds

You can cancel multiple builds with the following CLI command. 

**Procedure**

  * To manually cancel multiple builds, enter the following command: 

```shell-session
$ oc cancel-build <build1_name> <build2_name> <build3_name>
```


## 7.2.2. Canceling all builds

You can cancel all builds from the build configuration with the following CLI command. 

**Procedure**

  * To cancel all builds, enter the following command: 

```shell-session
$ oc cancel-build bc/<buildconfig_name>
```


## 7.2.3. Canceling all builds in a given state

You can cancel all builds in a given state, such as `new` or `pending`, while ignoring the builds in other states. 

**Procedure**

  * To cancel all in a given state, enter the following command: 

```shell-session
$ oc cancel-build bc/<buildconfig_name>
```
