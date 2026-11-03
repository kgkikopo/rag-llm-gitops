# 3.2. Create a project

Create a new project to contain all required resources and application components for the tutorial. 

A _project_ enables a community of users to organize and manage their content in isolation. Projects are OpenShift Container Platform extensions to Kubernetes namespaces. Projects have additional features that enable user self-provisioning. Each project has its own set of objects, policies, constraints, and service accounts. 

Cluster administrators can allow developers to create their own projects. In most cases, you automatically have access to your own projects. Administrators can grant access to other projects as needed. 

This procedure creates a new project called `user-getting-started`. You will use this project throughout the rest of this tutorial. 

Important

If you are using Developer Sandbox to complete this tutorial, skip this procedure. A project has already been created for you. 

**Prerequisites**

  * You have logged in to the OpenShift CLI (`oc`). 



**Procedure**

  * Create a project by running the following command: 

```shell-session
$ oc new-project user-getting-started
```


**Example output**

```shell-session
Now using project "user-getting-started" on server "https://openshift.example.com:6443".
...
```


**Additional resources**

  * [oc new-project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-new-project)
