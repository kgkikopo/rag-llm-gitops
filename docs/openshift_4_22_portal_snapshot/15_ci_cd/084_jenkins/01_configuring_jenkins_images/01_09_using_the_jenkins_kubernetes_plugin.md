# 1.9. Using the Jenkins Kubernetes plugin

In the following example, the `openshift-jee-sample` `BuildConfig` object causes a Jenkins Maven agent pod to be dynamically provisioned. The pod clones some Java source code, builds a WAR file, and causes a second `BuildConfig`, `openshift-jee-sample-docker` to run. The second `BuildConfig` layers the new WAR file into a container image. 

Important

OpenShift Container Platform 4.11 removed the OpenShift Jenkins Maven and NodeJS Agent images from its payload. Red Hat no longer produces these images, and they are not available from the `ocp-tools-4` repository at `registry.redhat.io`. Red Hat maintains the 4.10 and earlier versions of these images for any significant bug fixes or security CVEs, following the [OpenShift Container Platform lifecycle policy](https://access.redhat.com/support/policy/updates/openshift). 

For more information, see the "Important changes to OpenShift Jenkins images" link in the following "Additional resources" section. 

**Sample`BuildConfig` that uses the Jenkins Kubernetes plugin**

```yaml
kind: List
apiVersion: v1
items:
- kind: ImageStream
  apiVersion: image.openshift.io/v1
  metadata:
    name: openshift-jee-sample
- kind: BuildConfig
  apiVersion: build.openshift.io/v1
  metadata:
    name: openshift-jee-sample-docker
  spec:
    strategy:
      type: Docker
    source:
      type: Docker
      dockerfile: |-
        FROM openshift/wildfly-101-centos7:latest
        COPY ROOT.war /wildfly/standalone/deployments/ROOT.war
        CMD $STI_SCRIPTS_PATH/run
      binary:
        asFile: ROOT.war
    output:
      to:
        kind: ImageStreamTag
        name: openshift-jee-sample:latest
- kind: BuildConfig
  apiVersion: build.openshift.io/v1
  metadata:
    name: openshift-jee-sample
  spec:
    strategy:
      type: JenkinsPipeline
      jenkinsPipelineStrategy:
        jenkinsfile: |-
          node("maven") {
            sh "git clone https://github.com/openshift/openshift-jee-sample.git ."
            sh "mvn -B -Popenshift package"
            sh "oc start-build -F openshift-jee-sample-docker --from-file=target/ROOT.war"
          }
    triggers:
    - type: ConfigChange
```


It is also possible to override the specification of the dynamically created Jenkins agent pod. The following is a modification to the preceding example, which overrides the container memory and specifies an environment variable. 

**Sample`BuildConfig` that uses the Jenkins Kubernetes plugin, specifying memory limit and environment variable**

```yaml
kind: BuildConfig
apiVersion: build.openshift.io/v1
metadata:
  name: openshift-jee-sample
spec:
  strategy:
    type: JenkinsPipeline
    jenkinsPipelineStrategy:
      jenkinsfile: |-
        podTemplate(label: "mypod", 
```


1

```yaml
                    cloud: "openshift", 
```


2

```yaml
                    inheritFrom: "maven", 
```


3

```yaml
                    containers: [
            containerTemplate(name: "jnlp", 
```


4

```yaml
                              image: "openshift/jenkins-agent-maven-35-centos7:v3.10", 
```


5

```yaml
                              resourceRequestMemory: "512Mi", 
```


6

```yaml
                              resourceLimitMemory: "512Mi", 
```


7

```yaml
                              envVars: [
              envVar(key: "CONTAINER_HEAP_PERCENT", value: "0.25") 
```


8

```yaml
            ])
          ]) {
          node("mypod") { 
```


9

```yaml
            sh "git clone https://github.com/openshift/openshift-jee-sample.git ."
            sh "mvn -B -Popenshift package"
            sh "oc start-build -F openshift-jee-sample-docker --from-file=target/ROOT.war"
          }
        }
  triggers:
  - type: ConfigChange
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-1)
    

A new pod template called `mypod` is defined dynamically. The new pod template name is referenced in the node stanza. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-2)
    

The `cloud` value must be set to `openshift`. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-3)
    

The new pod template can inherit its configuration from an existing pod template. In this case, inherited from the Maven pod template that is pre-defined by OpenShift Container Platform. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-4)
    

This example overrides values in the pre-existing container, and must be specified by name. All Jenkins agent images shipped with OpenShift Container Platform use the Container name `jnlp`. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-5)
    

Specify the container image name again. This is a known issue. 

[6](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-6)
    

A memory request of `512 Mi` is specified. 

[7](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-7)
    

A memory limit of `512 Mi` is specified. 

[8](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-8)
    

An environment variable `CONTAINER_HEAP_PERCENT`, with value `0.25`, is specified. 

[9](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/images-other-jenkins#CO2-9)
    

The node stanza references the name of the defined pod template. 

By default, the pod is deleted when the build completes. This behavior can be modified with the plugin or within a pipeline Jenkinsfile. 

Upstream Jenkins has more recently introduced a YAML declarative format for defining a `podTemplate` pipeline DSL in-line with your pipelines. An example of this format, using the sample `java-builder` pod template that is defined in the OpenShift Container Platform Jenkins image: 

```yaml
def nodeLabel = 'java-buidler'

pipeline {
  agent {
    kubernetes {
      cloud 'openshift'
      label nodeLabel
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    worker: ${nodeLabel}
spec:
  containers:
  - name: jnlp
    image: image-registry.openshift-image-registry.svc:5000/openshift/jenkins-agent-base-rhel8:latest
    args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
  - name: java
    image: image-registry.openshift-image-registry.svc:5000/openshift/java:latest
    command:
    - cat
    tty: true
"""
    }
  }

  options {
    timeout(time: 20, unit: 'MINUTES')
  }

  stages {
    stage('Build App') {
      steps {
        container("java") {
          sh "mvn --version"
        }
     }
    }
  }
}
```


**Additional resources**

  * [Important changes to OpenShift Jenkins images](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/jenkins/important-changes-to-openshift-jenkins-images "Chapter 4. Important changes to OpenShift Jenkins images")
