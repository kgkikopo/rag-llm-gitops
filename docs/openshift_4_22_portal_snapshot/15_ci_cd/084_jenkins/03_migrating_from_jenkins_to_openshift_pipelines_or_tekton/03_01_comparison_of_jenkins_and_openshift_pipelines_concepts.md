# 3.1. Comparison of Jenkins and OpenShift Pipelines concepts

You can review and compare the following equivalent terms used in Jenkins and OpenShift Pipelines. 

## 3.1.1. Jenkins terminology

Jenkins offers declarative and scripted pipelines that are extensible using shared libraries and plugins. Some basic terms in Jenkins are as follows: 

  * **Pipeline** : Automates the entire process of building, testing, and deploying applications by using [Groovy](https://groovy-lang.org/) syntax. 
  * **Node** : A machine capable of either orchestrating or executing a scripted pipeline. 
  * **Stage** : A conceptually distinct subset of tasks performed in a pipeline. Plugins or user interfaces often use this block to display the status or progress of tasks. 
  * **Step** : A single task that specifies the exact action to be taken, either by using a command or a script. 



## 3.1.2. OpenShift Pipelines terminology

OpenShift Pipelines uses [YAML](https://yaml.org/) syntax for declarative pipelines and consists of tasks. Some basic terms in OpenShift Pipelines are as follows: 

  * **Pipeline** : A set of tasks in a series, in parallel, or both. 
  * **Task** : A sequence of steps as commands, binaries, or scripts. 
  * **PipelineRun** : Execution of a pipeline with one or more tasks. 
  * **TaskRun** : Execution of a task with one or more steps. 

Note

You can initiate a PipelineRun or a TaskRun with a set of inputs such as parameters and workspaces, and the execution results in a set of outputs and artifacts. 

  * **Workspace** : In OpenShift Pipelines, workspaces are conceptual blocks that serve the following purposes: 

    * Storage of inputs, outputs, and build artifacts. 
    * Common space to share data among tasks. 
    * Mount points for credentials held in secrets, configurations held in config maps, and common tools shared by an organization. 

Note

In Jenkins, there is no direct equivalent of OpenShift Pipelines workspaces. You can think of the control node as a workspace, as it stores the cloned code repository, build history, and artifacts. When a job is assigned to a different node, the cloned code and the generated artifacts are stored in that node, but the control node maintains the build history. 




## 3.1.3. Mapping of concepts

The building blocks of Jenkins and OpenShift Pipelines are not equivalent, and a specific comparison does not provide a technically accurate mapping. The following terms and concepts in Jenkins and OpenShift Pipelines correlate in general: 

Table 3.1. Jenkins and OpenShift Pipelines - basic comparisonJenkins| OpenShift Pipelines  
---|---  
Pipeline  |  Pipeline and PipelineRun   
Stage  |  Task   
Step  |  A step in a task   
Show more
