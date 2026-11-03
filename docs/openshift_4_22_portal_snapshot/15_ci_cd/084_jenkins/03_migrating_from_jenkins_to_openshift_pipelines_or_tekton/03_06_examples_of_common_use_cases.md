# 3.6. Examples of common use cases

Both Jenkins and OpenShift Pipelines offer capabilities for common CI/CD use cases, such as: 

  * Compiling, building, and deploying images using Apache Maven 
  * Extending the core capabilities by using plugins 
  * Reusing shareable libraries and custom scripts 



## 3.6.1. Running a Maven pipeline in Jenkins and OpenShift Pipelines

You can use Maven in both Jenkins and OpenShift Pipelines workflows for compiling, building, and deploying images. To map your existing Jenkins workflow to OpenShift Pipelines, consider the following examples: 

**Example: Compile and build an image and deploy it to OpenShift using Maven in Jenkins**

```plaintext
#!/usr/bin/groovy
node('maven') {
    stage 'Checkout'
    checkout scm

    stage 'Build'
    sh 'cd helloworld && mvn clean'
    sh 'cd helloworld && mvn compile'

    stage 'Run Unit Tests'
    sh 'cd helloworld && mvn test'

    stage 'Package'
    sh 'cd helloworld && mvn package'

    stage 'Archive artifact'
    sh 'mkdir -p artifacts/deployments && cp helloworld/target/*.war artifacts/deployments'
    archive 'helloworld/target/*.war'

    stage 'Create Image'
    sh 'oc login https://kubernetes.default -u admin -p admin --insecure-skip-tls-verify=true'
    sh 'oc new-project helloworldproject'
    sh 'oc project helloworldproject'
    sh 'oc process -f helloworld/jboss-eap70-binary-build.json | oc create -f -'
    sh 'oc start-build eap-helloworld-app --from-dir=artifacts/'

    stage 'Deploy'
    sh 'oc new-app helloworld/jboss-eap70-deploy.json' }
```


**Example: Compile and build an image and deploy it to OpenShift using Maven in OpenShift Pipelines.**

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: maven-pipeline
spec:
  workspaces:
    - name: shared-workspace
    - name: maven-settings
    - name: kubeconfig-dir
      optional: true
  params:
    - name: repo-url
    - name: revision
    - name: context-path
  tasks:
    - name: fetch-repo
      taskRef:
        name: git-clone
      workspaces:
        - name: output
          workspace: shared-workspace
      params:
        - name: url
          value: "$(params.repo-url)"
        - name: subdirectory
          value: ""
        - name: deleteExisting
          value: "true"
        - name: revision
          value: $(params.revision)
    - name: mvn-build
      taskRef:
        name: maven
      runAfter:
        - fetch-repo
      workspaces:
        - name: source
          workspace: shared-workspace
        - name: maven-settings
          workspace: maven-settings
      params:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["-DskipTests", "clean", "compile"]
    - name: mvn-tests
      taskRef:
        name: maven
      runAfter:
        - mvn-build
      workspaces:
        - name: source
          workspace: shared-workspace
        - name: maven-settings
          workspace: maven-settings
      params:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["test"]
    - name: mvn-package
      taskRef:
        name: maven
      runAfter:
        - mvn-tests
      workspaces:
        - name: source
          workspace: shared-workspace
        - name: maven-settings
          workspace: maven-settings
      params:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["package"]
    - name: create-image-and-deploy
      taskRef:
        name: openshift-client
      runAfter:
        - mvn-package
      workspaces:
        - name: manifest-dir
          workspace: shared-workspace
        - name: kubeconfig-dir
          workspace: kubeconfig-dir
      params:
        - name: SCRIPT
          value: |
            cd "$(params.context-path)"
            mkdir -p ./artifacts/deployments && cp ./target/*.war ./artifacts/deployments
            oc new-project helloworldproject
            oc project helloworldproject
            oc process -f jboss-eap70-binary-build.json | oc create -f -
            oc start-build eap-helloworld-app --from-dir=artifacts/
            oc new-app jboss-eap70-deploy.json
```


## 3.6.2. Extending the core capabilities of Jenkins and OpenShift Pipelines by using plugins

Jenkins has the advantage of a large ecosystem of numerous plugins developed over the years by its extensive user base. You can search and browse the plugins in the [Jenkins Plugin Index](https://plugins.jenkins.io/). 

OpenShift Pipelines also has many tasks developed and contributed by the community and enterprise users. A publicly available catalog of reusable OpenShift Pipelines tasks are available in the [Tekton Hub](https://hub.tekton.dev/). 

In addition, OpenShift Pipelines incorporates many of the plugins of the Jenkins ecosystem within its core capabilities. For example, authorization is a critical function in both Jenkins and OpenShift Pipelines. While Jenkins ensures authorization using the [Role-based Authorization Strategy](https://plugins.jenkins.io/role-strategy/) plugin, OpenShift Pipelines uses OpenShift’s built-in Role-based Access Control system. 

## 3.6.3. Sharing reusable code in Jenkins and OpenShift Pipelines

Jenkins [shared libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries/) provide reusable code for parts of Jenkins pipelines. The libraries are shared between [Jenkinsfiles](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/) to create highly modular pipelines without code repetition. 

Although there is no direct equivalent of Jenkins shared libraries in OpenShift Pipelines, you can achieve similar workflows by using tasks from the [Tekton Hub](https://hub.tekton.dev/) in combination with custom tasks and scripts.
