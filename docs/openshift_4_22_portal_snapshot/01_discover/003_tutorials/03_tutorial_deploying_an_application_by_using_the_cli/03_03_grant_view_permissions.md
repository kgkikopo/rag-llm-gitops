# 3.3. Grant view permissions

Configure the necessary permissions for the application to access the required cluster resources. 

OpenShift Container Platform automatically creates several service accounts in every project. The `default` service account takes responsibility for running the pods. OpenShift Container Platform uses and injects this service account into every pod that launches. 

By default, the `default` service account has limited permissions to interact with the OpenShift API. 

As a requirement of the application, you must assign the `view` role to the `default` service account to allow it to communicate with the OpenShift API to learn about pods, services, and resources within the project. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have `cluster-admin` or project-level `admin` privileges. 



**Procedure**

  * Add the `view` role to the `default` service account in the `user-getting-started` project by running the following command: 

```shell-session
$ oc adm policy add-role-to-user view -z default -n user-getting-started
```


Important

If you are using a different project, replace `user-getting-started` with the name of your project. 




**Additional resources**

  * [RBAC overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#authorization-overview_using-rbac)
  * [oc adm policy add-role-to-user](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-adm-policy-add-role-to-user)
