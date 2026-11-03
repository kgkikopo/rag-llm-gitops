# 4.5. Specifying a fixed oc client version for OpenShift Jenkins images

You can ensure that your Jenkins pipeline uses your specified `oc` client version with the Jenkins container image by configuring the version you require. 

**Procedure**

  * Define the `oc` tool version explicitly in the pipeline configuration to use a specific OpenShift client version in a Jenkins pipeline as shown in the following example: 



**Example pipeline configuration:**

```shell-session
pipeline {
    agent any

    tools {
        oc 'oc-4.22'
    }

    stages {
        stage('Version') {
            steps {
                sh 'oc version'
            }
        }
    }
}
```
