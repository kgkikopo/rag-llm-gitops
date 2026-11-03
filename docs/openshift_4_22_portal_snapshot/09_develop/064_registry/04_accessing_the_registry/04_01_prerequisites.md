# 4.1. Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role. 
  * You must have configured an identity provider (IDP). 
  * For pulling images, for example when using the `podman pull` command, the user must have the `registry-viewer` role. To add this role, run the following command: 

```shell-session
$ oc policy add-role-to-user registry-viewer <user_name>
```


  * For writing or pushing images, such as using `podman push` command, complete the following steps: 

    * Your account has the `registry-editor` role. To add this role, run the following command: 

```shell-session
$ oc policy add-role-to-user registry-editor <user_name>
```


    * Your cluster must have an existing project where the images can be pushed to.
