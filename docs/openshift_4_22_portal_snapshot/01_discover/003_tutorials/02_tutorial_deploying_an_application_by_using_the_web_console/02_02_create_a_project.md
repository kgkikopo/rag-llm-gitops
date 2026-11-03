# 2.2. Create a project

Create a new project to contain all required resources and application components for the tutorial. 

A _project_ enables a community of users to organize and manage their content in isolation. Projects are OpenShift Container Platform extensions to Kubernetes namespaces. Projects have additional features that enable user self-provisioning. Each project has its own set of objects, policies, constraints, and service accounts. 

Cluster administrators can allow developers to create their own projects. In most cases, you automatically have access to your own projects. Administrators can grant access to other projects as needed. 

This procedure creates a new project called `user-getting-started`. You will use this project throughout the rest of this tutorial. 

Important

If you are using Developer Sandbox to complete this tutorial, skip this procedure. A project has already been created for you. 

**Prerequisites**

  * You have logged in to the OpenShift Container Platform web console. 



**Procedure**

  1. Navigate to **Home** **Projects**. 
  2. Click **Create Project**. 
  3. In the **Name** field, enter `user-getting-started`. 
  4. Click **Create**. 



**Additional resources**

  * [Viewing a project by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#viewing-a-project-using-the-web-console_projects)
