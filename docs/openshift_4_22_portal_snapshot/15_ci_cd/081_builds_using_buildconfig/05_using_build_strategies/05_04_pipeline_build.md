# 5.4. Pipeline build

Important

The Pipeline build strategy is deprecated in OpenShift Container Platform 4. Equivalent and improved functionality is present in the OpenShift Container Platform Pipelines based on Tekton. 

Jenkins images on OpenShift Container Platform are fully supported and users should follow Jenkins user documentation for defining their `jenkinsfile` in a job or store it in a Source Control Management system. 

The Pipeline build strategy allows developers to define a Jenkins pipeline for use by the Jenkins pipeline plugin. The build can be started, monitored, and managed by OpenShift Container Platform in the same way as any other build type. 

Pipeline workflows are defined in a `jenkinsfile`, either embedded directly in the build configuration, or supplied in a Git repository and referenced by the build configuration. 

## 5.4.1. Understanding OpenShift Container Platform pipelines

Important

The Pipeline build strategy is deprecated in OpenShift Container Platform 4. Equivalent and improved functionality is present in the OpenShift Container Platform Pipelines based on Tekton. 

Jenkins images on OpenShift Container Platform are fully supported and users should follow Jenkins user documentation for defining their `jenkinsfile` in a job or store it in a Source Control Management system. 

Pipelines give you control over building, deploying, and promoting your applications on OpenShift Container Platform. Using a combination of the Jenkins Pipeline build strategy, `jenkinsfiles`, and the OpenShift Container Platform Domain Specific Language (DSL) provided by the Jenkins Client Plugin, you can create advanced build, test, deploy, and promote pipelines for any scenario. 

**OpenShift Container Platform Jenkins Sync Plugin**

The OpenShift Container Platform Jenkins Sync Plugin keeps the build configuration and build objects in sync with Jenkins jobs and builds, and provides the following: 

  * Dynamic job and run creation in Jenkins. 
  * Dynamic creation of agent pod templates from image streams, image stream tags, or config maps. 
  * Injection of environment variables. 
  * Pipeline visualization in the OpenShift Container Platform web console. 
  * Integration with the Jenkins Git plugin, which passes commit information from OpenShift Container Platform builds to the Jenkins Git plugin. 
  * Synchronization of secrets into Jenkins credential entries. 



**OpenShift Container Platform Jenkins Client Plugin**

The OpenShift Container Platform Jenkins Client Plugin is a Jenkins plugin which aims to provide a readable, concise, comprehensive, and fluent Jenkins Pipeline syntax for rich interactions with the OpenShift Container Platform API Server. The plugin uses the OpenShift Container Platform command-line tool, `oc`, which must be available on the nodes executing the script. 

The Jenkins Client Plugin must be installed on your Jenkins master so the OpenShift Container Platform DSL will be available to use within the `jenkinsfile` for your application. This plugin is installed and enabled by default when using the OpenShift Container Platform Jenkins image. 

For OpenShift Container Platform Pipelines within your project, you will must use the Jenkins Pipeline Build Strategy. This strategy defaults to using a `jenkinsfile` at the root of your source repository, but also provides the following configuration options: 

  * An inline `jenkinsfile` field within your build configuration. 
  * A `jenkinsfilePath` field within your build configuration that references the location of the `jenkinsfile` to use relative to the source `contextDir`. 



Note

The optional `jenkinsfilePath` field specifies the name of the file to use, relative to the source `contextDir`. If `contextDir` is omitted, it defaults to the root of the repository. If `jenkinsfilePath` is omitted, it defaults to `jenkinsfile`. 

## 5.4.2. Providing the Jenkins file for pipeline builds

Important

The Pipeline build strategy is deprecated in OpenShift Container Platform 4. Equivalent and improved functionality is present in the OpenShift Container Platform Pipelines based on Tekton. 

Jenkins images on OpenShift Container Platform are fully supported and users should follow Jenkins user documentation for defining their `jenkinsfile` in a job or store it in a Source Control Management system. 

The `jenkinsfile` uses the standard groovy language syntax to allow fine grained control over the configuration, build, and deployment of your application. 

You can supply the `jenkinsfile` in one of the following ways: 

  * A file located within your source code repository. 
  * Embedded as part of your build configuration using the `jenkinsfile` field. 



When using the first option, the `jenkinsfile` must be included in your applications source code repository at one of the following locations: 

  * A file named `jenkinsfile` at the root of your repository. 
  * A file named `jenkinsfile` at the root of the source `contextDir` of your repository. 
  * A file name specified via the `jenkinsfilePath` field of the `JenkinsPipelineStrategy` section of your BuildConfig, which is relative to the source `contextDir` if supplied, otherwise it defaults to the root of the repository. 



The `jenkinsfile` is run on the Jenkins agent pod, which must have the OpenShift Container Platform client binaries available if you intend to use the OpenShift Container Platform DSL. 

**Procedure**

To provide the Jenkins file, you can either: 

  * Embed the Jenkins file in the build configuration. 
  * Include in the build configuration a reference to the Git repository that contains the Jenkins file. 



**Embedded Definition**

```yaml
kind: "BuildConfig"
apiVersion: "v1"
metadata:
  name: "sample-pipeline"
spec:
  strategy:
    jenkinsPipelineStrategy:
      jenkinsfile: |-
        node('agent') {
          stage 'build'
          openshiftBuild(buildConfig: 'ruby-sample-build', showBuildLogs: 'true')
          stage 'deploy'
          openshiftDeploy(deploymentConfig: 'frontend')
        }
```


**Reference to Git Repository**

```yaml
kind: "BuildConfig"
apiVersion: "v1"
metadata:
  name: "sample-pipeline"
spec:
  source:
    git:
      uri: "https://github.com/openshift/ruby-hello-world"
  strategy:
    jenkinsPipelineStrategy:
      jenkinsfilePath: some/repo/dir/filename 
```


1

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO14-1)
    

The optional `jenkinsfilePath` field specifies the name of the file to use, relative to the source `contextDir`. If `contextDir` is omitted, it defaults to the root of the repository. If `jenkinsfilePath` is omitted, it defaults to `jenkinsfile`. 

## 5.4.3. Using environment variables for pipeline builds

Important

The Pipeline build strategy is deprecated in OpenShift Container Platform 4. Equivalent and improved functionality is present in the OpenShift Container Platform Pipelines based on Tekton. 

Jenkins images on OpenShift Container Platform are fully supported and users should follow Jenkins user documentation for defining their `jenkinsfile` in a job or store it in a Source Control Management system. 

To make environment variables available to the Pipeline build process, you can add environment variables to the `jenkinsPipelineStrategy` definition of the build configuration. 

Once defined, the environment variables will be set as parameters for any Jenkins job associated with the build configuration. 

**Procedure**

  * To define environment variables to be used during build, edit the YAML file: 

```yaml
jenkinsPipelineStrategy:
...
  env:
    - name: "FOO"
      value: "BAR"
```


You can also manage environment variables defined in the build configuration with the `oc set env` command. 

### 5.4.3.1. Mapping between BuildConfig environment variables and Jenkins job parameters

When a Jenkins job is created or updated based on changes to a Pipeline strategy build configuration, any environment variables in the build configuration are mapped to Jenkins job parameters definitions, where the default values for the Jenkins job parameters definitions are the current values of the associated environment variables. 

After the Jenkins job’s initial creation, you can still add additional parameters to the job from the Jenkins console. The parameter names differ from the names of the environment variables in the build configuration. The parameters are honored when builds are started for those Jenkins jobs. 

How you start builds for the Jenkins job dictates how the parameters are set. 

  * If you start with `oc start-build`, the values of the environment variables in the build configuration are the parameters set for the corresponding job instance. Any changes you make to the parameters' default values from the Jenkins console are ignored. The build configuration values take precedence. 
  * If you start with `oc start-build -e`, the values for the environment variables specified in the `-e` option take precedence. 

    * If you specify an environment variable not listed in the build configuration, they will be added as a Jenkins job parameter definitions. 
    * Any changes you make from the Jenkins console to the parameters corresponding to the environment variables are ignored. The build configuration and what you specify with `oc start-build -e` takes precedence. 

  * If you start the Jenkins job with the Jenkins console, then you can control the setting of the parameters with the Jenkins console as part of starting a build for the job. 



Note

It is recommended that you specify in the build configuration all possible environment variables to be associated with job parameters. Doing so reduces disk I/O and improves performance during Jenkins processing. 

## 5.4.4. Pipeline build tutorial

Important

The Pipeline build strategy is deprecated in OpenShift Container Platform 4. Equivalent and improved functionality is present in the OpenShift Container Platform Pipelines based on Tekton. 

Jenkins images on OpenShift Container Platform are fully supported and users should follow Jenkins user documentation for defining their `jenkinsfile` in a job or store it in a Source Control Management system. 

This example demonstrates how to create an OpenShift Container Platform Pipeline that will build, deploy, and verify a `Node.js/MongoDB` application using the `nodejs-mongodb.json` template. 

**Procedure**

  1. Create the Jenkins master: 

```shell-session
  $ oc project <project_name>
```


Select the project that you want to use or create a new project with `oc new-project <project_name>`. 

```shell-session
  $ oc new-app jenkins-ephemeral 
```


1

```shell-session

```


If you want to use persistent storage, use `jenkins-persistent` instead. 

  2. Create a file named `nodejs-sample-pipeline.yaml` with the following content: 

Note

This creates a `BuildConfig` object that employs the Jenkins pipeline strategy to build, deploy, and scale the `Node.js/MongoDB` example application. 

```yaml
kind: "BuildConfig"
apiVersion: "v1"
metadata:
  name: "nodejs-sample-pipeline"
spec:
  strategy:
    jenkinsPipelineStrategy:
      jenkinsfile: <pipeline content from below>
    type: JenkinsPipeline
```


  3. After you create a `BuildConfig` object with a `jenkinsPipelineStrategy`, tell the pipeline what to do by using an inline `jenkinsfile`: 

Note

This example does not set up a Git repository for the application. 

The following `jenkinsfile` content is written in Groovy using the OpenShift Container Platform DSL. For this example, include inline content in the `BuildConfig` object using the YAML Literal Style, though including a `jenkinsfile` in your source repository is the preferred method. 

```plaintext
def templatePath = 'https://raw.githubusercontent.com/openshift/nodejs-ex/master/openshift/templates/nodejs-mongodb.json' 
```


1

```plaintext
def templateName = 'nodejs-mongodb-example' 
```


2

```plaintext
pipeline {
  agent {
    node {
      label 'nodejs' 
```


3

```plaintext
    }
  }
  options {
    timeout(time: 20, unit: 'MINUTES') 
```


4

```plaintext
  }
  stages {
    stage('preamble') {
        steps {
            script {
                openshift.withCluster() {
                    openshift.withProject() {
                        echo "Using project: ${openshift.project()}"
                    }
                }
            }
        }
    }
    stage('cleanup') {
      steps {
        script {
            openshift.withCluster() {
                openshift.withProject() {
                  openshift.selector("all", [ template : templateName ]).delete() 
```


5

```plaintext
                  if (openshift.selector("secrets", templateName).exists()) { 
```


6

```plaintext
                    openshift.selector("secrets", templateName).delete()
                  }
                }
            }
        }
      }
    }
    stage('create') {
      steps {
        script {
            openshift.withCluster() {
                openshift.withProject() {
                  openshift.newApp(templatePath) 
```


7

```plaintext
                }
            }
        }
      }
    }
    stage('build') {
      steps {
        script {
            openshift.withCluster() {
                openshift.withProject() {
                  def builds = openshift.selector("bc", templateName).related('builds')
                  timeout(5) { 
```


8

```plaintext
                    builds.untilEach(1) {
                      return (it.object().status.phase == "Complete")
                    }
                  }
                }
            }
        }
      }
    }
    stage('deploy') {
      steps {
        script {
            openshift.withCluster() {
                openshift.withProject() {
                  def rm = openshift.selector("dc", templateName).rollout()
                  timeout(5) { 
```


9

```plaintext
                    openshift.selector("dc", templateName).related('pods').untilEach(1) {
                      return (it.object().status.phase == "Running")
                    }
                  }
                }
            }
        }
      }
    }
    stage('tag') {
      steps {
        script {
            openshift.withCluster() {
                openshift.withProject() {
                  openshift.tag("${templateName}:latest", "${templateName}-staging:latest") 
```


10

```plaintext
                }
            }
        }
      }
    }
  }
}
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-2)
    

Path of the template to use. 

[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-1) [2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-3)
    

Name of the template that will be created. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-4)
    

Spin up a `node.js` agent pod on which to run this build. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-5)
    

Set a timeout of 20 minutes for this pipeline. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-6)
    

Delete everything with this template label. 

[6](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-7)
    

Delete any secrets with this template label. 

[7](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-8)
    

Create a new application from the `templatePath`. 

[8](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-9)
    

Wait up to five minutes for the build to complete. 

[9](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-10)
    

Wait up to five minutes for the deployment to complete. 

[10](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#CO15-11)
    

If everything else succeeded, tag the `$ {templateName}:latest` image as `$ {templateName}-staging:latest`. A pipeline build configuration for the staging environment can watch for the `$ {templateName}-staging:latest` image to change and then deploy it to the staging environment. 

Note

The previous example was written using the declarative pipeline style, but the older scripted pipeline style is also supported. 

  4. Create the Pipeline `BuildConfig` in your OpenShift Container Platform cluster: 

```shell-session
$ oc create -f nodejs-sample-pipeline.yaml
```


     1. If you do not want to create your own file, you can use the sample from the Origin repository by running: 

```shell-session
$ oc create -f https://raw.githubusercontent.com/openshift/origin/master/examples/jenkins/pipeline/nodejs-sample-pipeline.yaml
```


  5. Start the Pipeline: 

```shell-session
$ oc start-build nodejs-sample-pipeline
```


Note

Alternatively, you can start your pipeline with the OpenShift Container Platform web console by navigating to the Builds  Pipeline section and clicking **Start Pipeline** , or by visiting the Jenkins Console, navigating to the Pipeline that you created, and clicking **Build Now**. 

Once the pipeline is started, you should see the following actions performed within your project: 

     * A job instance is created on the Jenkins server. 
     * An agent pod is launched, if your pipeline requires one. 
     * The pipeline runs on the agent pod, or the master if no agent is required. 

       * Any previously created resources with the `template=nodejs-mongodb-example` label will be deleted. 
       * A new application, and all of its associated resources, will be created from the `nodejs-mongodb-example` template. 
       * A build will be started using the `nodejs-mongodb-example` `BuildConfig`. 

         * The pipeline will wait until the build has completed to trigger the next stage. 

       * A deployment will be started using the `nodejs-mongodb-example` deployment configuration. 

         * The pipeline will wait until the deployment has completed to trigger the next stage. 

       * If the build and deploy are successful, the `nodejs-mongodb-example:latest` image will be tagged as `nodejs-mongodb-example:stage`. 

     * The agent pod is deleted, if one was required for the pipeline. 

Note

The best way to visualize the pipeline execution is by viewing it in the OpenShift Container Platform web console. You can view your pipelines by logging in to the web console and navigating to Builds  Pipelines.
