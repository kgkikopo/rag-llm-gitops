# Chapter 2. Jenkins agent

OpenShift Container Platform provides a base image for use as a Jenkins agent. 

The Base image for Jenkins agents does the following: 

  * Pulls in both the required tools, headless Java, the Jenkins JNLP client, and the useful ones, including `git`, `tar`, `zip`, and `nss`, among others. 
  * Establishes the JNLP agent as the entry point. 
  * Includes the `oc` client tool for invoking command-line operations from within Jenkins jobs. 
  * Provides Dockerfiles for both Red Hat Enterprise Linux (RHEL) and `localdev` images. 



Important

Use a version of the agent image that is appropriate for your OpenShift Container Platform release version. Embedding an `oc` client version that is not compatible with the OpenShift Container Platform version can cause unexpected behavior. 

The OpenShift Container Platform Jenkins image also defines the following sample `java-builder` pod template to illustrate how you can use the agent image with the Jenkins Kubernetes plugin. 

The `java-builder` pod template employs two containers: 

  * A `jnlp` container that uses the OpenShift Container Platform Base agent image and handles the JNLP contract for starting and stopping Jenkins agents. 
  * A `java` container that uses the `java` OpenShift Container Platform Sample ImageStream, which contains the various Java binaries, including the Maven binary `mvn`, for building code.

- [2.1. Jenkins agent images](02_01_jenkins_agent_images.md)
- [2.2. Jenkins agent environment variables](02_02_jenkins_agent_environment_variables.md)
- [2.3. Jenkins agent memory requirements](02_03_jenkins_agent_memory_requirements.md)
- [2.4. Jenkins agent Gradle builds](02_04_jenkins_agent_gradle_builds.md)
- [2.5. Jenkins agent pod retention](02_05_jenkins_agent_pod_retention.md)
