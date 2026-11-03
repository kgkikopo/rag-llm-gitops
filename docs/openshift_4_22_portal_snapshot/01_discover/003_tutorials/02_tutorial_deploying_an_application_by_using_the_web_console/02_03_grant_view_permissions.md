# 2.3. Grant view permissions

Configure the necessary permissions for the application to access the required cluster resources. 

OpenShift Container Platform automatically creates several service accounts in every project. The `default` service account takes responsibility for running the pods. OpenShift Container Platform uses and injects this service account into every pod that launches. 

By default, the `default` service account has limited permissions to interact with the OpenShift API. 

As a requirement of the application, you must assign the `view` role to the `default` service account to allow it to communicate with the OpenShift API to learn about pods, services, and resources within the project. 

**Prerequisites**

  * You have `cluster-admin` or project-level `admin` privileges. 



**Procedure**

  1. Navigate to **User Management** **RoleBindings**. 
  2. Click **Create binding**. 
  3. In the **Name** field, enter `sa-user-account`. 
  4. In the **Namespace** field, search for and select `user-getting-started`. 

Important

If you are using a different project, select the name of your project. 

  5. In the **Role name** field, search for and select `view`. 
  6. Under **Subject** , select `ServiceAccount`. 
  7. In the **Subject namespace** field, search for and select `user-getting-started`. 

Important

If you are using a different project, select the name of your project. 

  8. In the **Subject name** field, enter `default`. 
  9. Click **Create**. 



**Additional resources**

  * [RBAC overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#authorization-overview_using-rbac)
