# 6.3. OpenShift Pipelines tkn reference

This section lists the basic `tkn` CLI commands. 

## 6.3.1. Basic syntax

`tkn [command or options] [arguments…​]`

## 6.3.2. Global options

`--help, -h`

## 6.3.3. Utility commands

### 6.3.3.1. tkn

Parent command for `tkn` CLI. 

**Example: Display all options**

```shell-session
$ tkn
```


### 6.3.3.2. completion [shell]

Print shell completion code which must be evaluated to provide interactive completion. Supported shells are `bash` and `zsh`. 

**Example: Completion code for`bash` shell**

```shell-session
$ tkn completion bash
```


### 6.3.3.3. version

Print version information of the `tkn` CLI. 

**Example: Check the`tkn` version**

```shell-session
$ tkn version
```


## 6.3.4. Pipelines management commands

### 6.3.4.1. pipeline

Manage pipelines. 

**Example: Display help**

```shell-session
$ tkn pipeline --help
```


### 6.3.4.2. pipeline delete

Delete a pipeline. 

**Example: Delete the`mypipeline` pipeline from a namespace**

```shell-session
$ tkn pipeline delete mypipeline -n myspace
```


### 6.3.4.3. pipeline describe

Describe a pipeline. 

**Example: Describe the`mypipeline` pipeline**

```shell-session
$ tkn pipeline describe mypipeline
```


### 6.3.4.4. pipeline list

Display a list of pipelines. 

**Example: Display a list of pipelines**

```shell-session
$ tkn pipeline list
```


### 6.3.4.5. pipeline logs

Display the logs for a specific pipeline. 

**Example: Stream the live logs for the`mypipeline` pipeline**

```shell-session
$ tkn pipeline logs -f mypipeline
```


### 6.3.4.6. pipeline start

Start a pipeline. 

**Example: Start the`mypipeline` pipeline**

```shell-session
$ tkn pipeline start mypipeline
```


## 6.3.5. Pipeline run commands

### 6.3.5.1. pipelinerun

Manage pipeline runs. 

**Example: Display help**

```shell-session
$ tkn pipelinerun -h
```


### 6.3.5.2. pipelinerun cancel

Cancel a pipeline run. 

**Example: Cancel the`mypipelinerun` pipeline run from a namespace**

```shell-session
$ tkn pipelinerun cancel mypipelinerun -n myspace
```


### 6.3.5.3. pipelinerun delete

Delete a pipeline run. 

**Example: Delete pipeline runs from a namespace**

```shell-session
$ tkn pipelinerun delete mypipelinerun1 mypipelinerun2 -n myspace
```


**Example: Delete all pipeline runs from a namespace, except the five most recently executed pipeline runs**

```shell-session
$ tkn pipelinerun delete -n myspace --keep 5 
```


1

```shell-session

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/pipelines-cli-tkn#CO1-2) [1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/pipelines-cli-tkn#CO1-7)
    

Replace `5` with the number of most recently executed pipeline runs you want to retain. 

**Example: Delete all pipelines**

```shell-session
$ tkn pipelinerun delete --all
```


Note

Starting with Red Hat OpenShift Pipelines 1.6, the `tkn pipelinerun delete --all` command does not delete any resources that are in the running state. 

### 6.3.5.4. pipelinerun describe

Describe a pipeline run. 

**Example: Describe the`mypipelinerun` pipeline run in a namespace**

```shell-session
$ tkn pipelinerun describe mypipelinerun -n myspace
```


### 6.3.5.5. pipelinerun list

List pipeline runs. 

**Example: Display a list of pipeline runs in a namespace**

```shell-session
$ tkn pipelinerun list -n myspace
```


### 6.3.5.6. pipelinerun logs

Display the logs of a pipeline run. 

**Example: Display the logs of the`mypipelinerun` pipeline run with all tasks and steps in a namespace**

```shell-session
$ tkn pipelinerun logs mypipelinerun -a -n myspace
```


## 6.3.6. Task management commands

### 6.3.6.1. task

Manage tasks. 

**Example: Display help**

```shell-session
$ tkn task -h
```


### 6.3.6.2. task delete

Delete a task. 

**Example: Delete`mytask1` and `mytask2` tasks from a namespace**

```shell-session
$ tkn task delete mytask1 mytask2 -n myspace
```


### 6.3.6.3. task describe

Describe a task. 

**Example: Describe the`mytask` task in a namespace**

```shell-session
$ tkn task describe mytask -n myspace
```


### 6.3.6.4. task list

List tasks. 

**Example: List all the tasks in a namespace**

```shell-session
$ tkn task list -n myspace
```


### 6.3.6.5. task logs

Display task logs. 

**Example: Display logs for the`mytaskrun` task run of the `mytask` task**

```shell-session
$ tkn task logs mytask mytaskrun -n myspace
```


### 6.3.6.6. task start

Start a task. 

**Example: Start the`mytask` task in a namespace**

```shell-session
$ tkn task start mytask -s <ServiceAccountName> -n myspace
```


## 6.3.7. Task run commands

### 6.3.7.1. taskrun

Manage task runs. 

**Example: Display help**

```shell-session
$ tkn taskrun -h
```


### 6.3.7.2. taskrun cancel

Cancel a task run. 

**Example: Cancel the`mytaskrun` task run from a namespace**

```shell-session
$ tkn taskrun cancel mytaskrun -n myspace
```


### 6.3.7.3. taskrun delete

Delete a TaskRun. 

**Example: Delete the`mytaskrun1` and `mytaskrun2` task runs from a namespace**

```shell-session
$ tkn taskrun delete mytaskrun1 mytaskrun2 -n myspace
```


**Example: Delete all but the five most recently executed task runs from a namespace**

```shell-session
$ tkn taskrun delete -n myspace --keep 5 
```


1

```shell-session

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/pipelines-cli-tkn#CO2-1)
    

Replace `5` with the number of most recently executed task runs you want to retain. 

### 6.3.7.4. taskrun describe

Describe a task run. 

**Example: Describe the`mytaskrun` task run in a namespace**

```shell-session
$ tkn taskrun describe mytaskrun -n myspace
```


### 6.3.7.5. taskrun list

List task runs. 

**Example: List all the task runs in a namespace**

```shell-session
$ tkn taskrun list -n myspace
```


### 6.3.7.6. taskrun logs

Display task run logs. 

**Example: Display live logs for the`mytaskrun` task run in a namespace**

```shell-session
$ tkn taskrun logs -f mytaskrun -n myspace
```


## 6.3.8. Condition management commands

### 6.3.8.1. condition

Manage Conditions. 

**Example: Display help**

```shell-session
$ tkn condition --help
```


### 6.3.8.2. condition delete

Delete a Condition. 

**Example: Delete the`mycondition1` Condition from a namespace**

```shell-session
$ tkn condition delete mycondition1 -n myspace
```


### 6.3.8.3. condition describe

Describe a Condition. 

**Example: Describe the`mycondition1` Condition in a namespace**

```shell-session
$ tkn condition describe mycondition1 -n myspace
```


### 6.3.8.4. condition list

List Conditions. 

**Example: List Conditions in a namespace**

```shell-session
$ tkn condition list -n myspace
```


## 6.3.9. Pipeline Resource management commands

### 6.3.9.1. resource

Manage Pipeline Resources. 

**Example: Display help**

```shell-session
$ tkn resource -h
```


### 6.3.9.2. resource create

Create a Pipeline Resource. 

**Example: Create a Pipeline Resource in a namespace**

```shell-session
$ tkn resource create -n myspace
```


This is an interactive command that asks for input on the name of the Resource, type of the Resource, and the values based on the type of the Resource. 

### 6.3.9.3. resource delete

Delete a Pipeline Resource. 

**Example: Delete the`myresource` Pipeline Resource from a namespace**

```shell-session
$ tkn resource delete myresource -n myspace
```


### 6.3.9.4. resource describe

Describe a Pipeline Resource. 

**Example: Describe the`myresource` Pipeline Resource**

```shell-session
$ tkn resource describe myresource -n myspace
```


### 6.3.9.5. resource list

List Pipeline Resources. 

**Example: List all Pipeline Resources in a namespace**

```shell-session
$ tkn resource list -n myspace
```


## 6.3.10. ClusterTask management commands

Important

In Red Hat OpenShift Pipelines 1.10, ClusterTask functionality of the `tkn` command-line utility is deprecated and is planned to be removed in a future release. 

### 6.3.10.1. clustertask

Manage ClusterTasks. 

**Example: Display help**

```shell-session
$ tkn clustertask --help
```


### 6.3.10.2. clustertask delete

Delete a ClusterTask resource in a cluster. 

**Example: Delete`mytask1` and `mytask2` ClusterTasks**

```shell-session
$ tkn clustertask delete mytask1 mytask2
```


### 6.3.10.3. clustertask describe

Describe a ClusterTask. 

**Example: Describe the`mytask` ClusterTask**

```shell-session
$ tkn clustertask describe mytask1
```


### 6.3.10.4. clustertask list

List ClusterTasks. 

**Example: List ClusterTasks**

```shell-session
$ tkn clustertask list
```


### 6.3.10.5. clustertask start

Start ClusterTasks. 

**Example: Start the`mytask` ClusterTask**

```shell-session
$ tkn clustertask start mytask
```


## 6.3.11. Trigger management commands

### 6.3.11.1. eventlistener

Manage EventListeners. 

**Example: Display help**

```shell-session
$ tkn eventlistener -h
```


### 6.3.11.2. eventlistener delete

Delete an EventListener. 

**Example: Delete`mylistener1` and `mylistener2` EventListeners in a namespace**

```shell-session
$ tkn eventlistener delete mylistener1 mylistener2 -n myspace
```


### 6.3.11.3. eventlistener describe

Describe an EventListener. 

**Example: Describe the`mylistener` EventListener in a namespace**

```shell-session
$ tkn eventlistener describe mylistener -n myspace
```


### 6.3.11.4. eventlistener list

List EventListeners. 

**Example: List all the EventListeners in a namespace**

```shell-session
$ tkn eventlistener list -n myspace
```


### 6.3.11.5. eventlistener logs

Display logs of an EventListener. 

**Example: Display the logs of the`mylistener` EventListener in a namespace**

```shell-session
$ tkn eventlistener logs mylistener -n myspace
```


### 6.3.11.6. triggerbinding

Manage TriggerBindings. 

**Example: Display TriggerBindings help**

```shell-session
$ tkn triggerbinding -h
```


### 6.3.11.7. triggerbinding delete

Delete a TriggerBinding. 

**Example: Delete`mybinding1` and `mybinding2` TriggerBindings in a namespace**

```shell-session
$ tkn triggerbinding delete mybinding1 mybinding2 -n myspace
```


### 6.3.11.8. triggerbinding describe

Describe a TriggerBinding. 

**Example: Describe the`mybinding` TriggerBinding in a namespace**

```shell-session
$ tkn triggerbinding describe mybinding -n myspace
```


### 6.3.11.9. triggerbinding list

List TriggerBindings. 

**Example: List all the TriggerBindings in a namespace**

```shell-session
$ tkn triggerbinding list -n myspace
```


### 6.3.11.10. triggertemplate

Manage TriggerTemplates. 

**Example: Display TriggerTemplate help**

```shell-session
$ tkn triggertemplate -h
```


### 6.3.11.11. triggertemplate delete

Delete a TriggerTemplate. 

**Example: Delete`mytemplate1` and `mytemplate2` TriggerTemplates in a namespace**

```shell-session
$ tkn triggertemplate delete mytemplate1 mytemplate2 -n `myspace`
```


### 6.3.11.12. triggertemplate describe

Describe a TriggerTemplate. 

**Example: Describe the`mytemplate` TriggerTemplate in a namespace**

```shell-session
$ tkn triggertemplate describe mytemplate -n `myspace`
```


### 6.3.11.13. triggertemplate list

List TriggerTemplates. 

**Example: List all the TriggerTemplates in a namespace**

```shell-session
$ tkn triggertemplate list -n myspace
```


### 6.3.11.14. clustertriggerbinding

Manage ClusterTriggerBindings. 

**Example: Display ClusterTriggerBindings help**

```shell-session
$ tkn clustertriggerbinding -h
```


### 6.3.11.15. clustertriggerbinding delete

Delete a ClusterTriggerBinding. 

**Example: Delete`myclusterbinding1` and `myclusterbinding2` ClusterTriggerBindings**

```shell-session
$ tkn clustertriggerbinding delete myclusterbinding1 myclusterbinding2
```


### 6.3.11.16. clustertriggerbinding describe

Describe a ClusterTriggerBinding. 

**Example: Describe the`myclusterbinding` ClusterTriggerBinding**

```shell-session
$ tkn clustertriggerbinding describe myclusterbinding
```


### 6.3.11.17. clustertriggerbinding list

List ClusterTriggerBindings. 

**Example: List all ClusterTriggerBindings**

```shell-session
$ tkn clustertriggerbinding list
```


## 6.3.12. Hub interaction commands

Interact with Tekton Hub for resources such as tasks and pipelines. 

### 6.3.12.1. hub

Interact with hub. 

**Example: Display help**

```shell-session
$ tkn hub -h
```


**Example: Interact with a hub API server**

```shell-session
$ tkn hub --api-server https://api.hub.tekton.dev
```


Note

For each example, to get the corresponding sub-commands and flags, run `tkn hub <command> --help`. 

### 6.3.12.2. hub downgrade

Downgrade an installed resource. 

**Example: Downgrade the`mytask` task in the `mynamespace` namespace to its older version**

```shell-session
$ tkn hub downgrade task mytask --to version -n mynamespace
```


### 6.3.12.3. hub get

Get a resource manifest by its name, kind, catalog, and version. 

**Example: Get the manifest for a specific version of the`myresource` pipeline or task from the `tekton` catalog**

```shell-session
$ tkn hub get [pipeline | task] myresource --from tekton --version version
```


### 6.3.12.4. hub info

Display information about a resource by its name, kind, catalog, and version. 

**Example: Display information about a specific version of the`mytask` task from the `tekton` catalog**

```shell-session
$ tkn hub info task mytask --from tekton --version version
```


### 6.3.12.5. hub install

Install a resource from a catalog by its kind, name, and version. 

**Example: Install a specific version of the`mytask` task from the `tekton` catalog in the `mynamespace` namespace**

```shell-session
$ tkn hub install task mytask --from tekton --version version -n mynamespace
```


### 6.3.12.6. hub reinstall

Reinstall a resource by its kind and name. 

**Example: Reinstall a specific version of the`mytask` task from the `tekton` catalog in the `mynamespace` namespace**

```shell-session
$ tkn hub reinstall task mytask --from tekton --version version -n mynamespace
```


### 6.3.12.7. hub search

Search a resource by a combination of name, kind, and tags. 

**Example: Search a resource with a tag`cli`**

```shell-session
$ tkn hub search --tags cli
```


### 6.3.12.8. hub upgrade

Upgrade an installed resource. 

**Example: Upgrade the installed`mytask` task in the `mynamespace` namespace to a new version**

```shell-session
$ tkn hub upgrade task mytask --to version -n mynamespace
```
