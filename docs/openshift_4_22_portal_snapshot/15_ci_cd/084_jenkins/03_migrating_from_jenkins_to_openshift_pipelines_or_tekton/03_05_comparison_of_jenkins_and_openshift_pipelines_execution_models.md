# 3.5. Comparison of Jenkins and OpenShift Pipelines execution models

Jenkins and OpenShift Pipelines offer similar functions but are different in architecture and execution. 

Table 3.2. Comparison of execution models in Jenkins and OpenShift PipelinesJenkins| OpenShift Pipelines  
---|---  
Jenkins has a controller node. Jenkins runs pipelines and steps centrally, or orchestrates jobs running in other nodes.  |  OpenShift Pipelines is serverless and distributed, and there is no central dependency for execution.   
Containers are launched by the Jenkins controller node through the pipeline.  |  OpenShift Pipelines adopts a 'container-first' approach, where every step runs as a container in a pod (equivalent to nodes in Jenkins).   
Extensibility is achieved by using plugins.  |  Extensibility is achieved by using tasks in Tekton Hub or by creating custom tasks and scripts.   
Show more
