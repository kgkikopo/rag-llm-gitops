# 10.11. Create a cluster admin

To grant a user full administrative access to the cluster, you can bind the `cluster-admin` cluster role to that user. 

The `cluster-admin` role is required to perform administrator level tasks on the OpenShift Container Platform cluster, such as modifying cluster resources. 

**Prerequisites**

  * You must have created a user to define as the cluster admin. 



**Procedure**

  * Define the user as a cluster admin: 

```shell-session
$ oc adm policy add-cluster-role-to-user cluster-admin <user>
```
