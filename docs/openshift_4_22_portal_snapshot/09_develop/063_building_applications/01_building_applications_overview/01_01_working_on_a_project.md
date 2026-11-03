# 1.1. Working on a project

Manage the complete lifecycle of isolated projects, from initial provisioning to user access control, to securely organize applications across your cluster. 

After you create the project, you can grant or revoke access to a project and manage cluster roles for the users. You can also edit the project configuration resource while creating a project template that is used for automatic provisioning of new projects. 

Using the CLI, you can create a project as a different user by impersonating a request to the OpenShift Container Platform API. When you make a request to create a new project, the OpenShift Container Platform uses an endpoint to provision the project according to a customizable template. As a cluster administrator, you can choose to prevent an authenticated user group from self-provisioning new projects.
