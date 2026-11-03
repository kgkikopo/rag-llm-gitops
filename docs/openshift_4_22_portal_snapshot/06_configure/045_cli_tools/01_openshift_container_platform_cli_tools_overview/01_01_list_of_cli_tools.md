# 1.1. List of CLI tools

Manage your OpenShift Container Platform cluster, applications, and Operators from the terminal by using primary command-line interface (CLI) tools. 

The following list details these primary CLI tools: 

  * OpenShift CLI (`oc`): This is the most commonly used CLI tool by OpenShift Container Platform users. Cluster administrators and developers can use it to perform end-to-end operations across OpenShift Container Platform from the terminal, including working directly with project source code using command scripts. 
  * Kubernetes CLI (`kubectl`): OpenShift Container Platform is conformant with Cloud Native Computing Foundation (CNCF) Kubernetes and fully supports `kubectl` as a client. The OpenShift CLI (`oc`) is a superset of `kubectl`, where both CLI tools are included in the OpenShift Container Platform clients download. You can use the standard `kubectl` commands against OpenShift Container Platform clusters without any compatibility issues. 
  * Helm CLI (`helm`): Helm is a package manager for Kubernetes. The `helm` CLI provides commands to install, upgrade, and manage Helm charts on a cluster. 
  * opm CLI: The `opm` CLI tool helps Operator developers and cluster administrators create and maintain catalogs of Operators. 
  * Knative CLI: The Knative (`kn`) CLI tool provides commands to interact with OpenShift Serverless components, such as Knative Serving and Eventing. 
  * Pipelines CLI (tkn): OpenShift Pipelines is a continuous integration and delivery (CI/CD) solution in OpenShift Container Platform, which internally uses Tekton. The `tkn` CLI tool provides commands to interact with OpenShift Pipelines. 



## 1.1.1. Additional resources

  * [OpenShift Container Platform CLI (`oc`)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/openshift-cli-oc#cli-getting-started "2.1. Getting started with the OpenShift CLI")
  * [Helm CLI (`helm`)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#installing-helm)
  * [`opm` CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/opm-cli#cli-opm-install "8.1. Installing the opm CLI")
  * [Knative CLI (`kn`)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/kn-cli-tools "Chapter 5. Knative CLI for use with OpenShift Serverless")
  * [OpenShift Pipelines CLI (`tkn`)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/pipelines-cli-tkn#installing-tkn "6.1. Installing tkn")
