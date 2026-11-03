# 11.2. Restricting build strategies to users globally

You can allow a set of specific users to create builds with a particular strategy. 

**Procedure**

  * Assign the role that corresponds to the build strategy to a specific user. For example, to add the `system:build-strategy-docker` cluster role to the user `devuser`: 

```shell-session
$ oc adm policy add-cluster-role-to-user system:build-strategy-docker devuser
```


Warning

Granting a user access at the cluster level to the `builds/docker` subresource means that the user can create builds with the docker strategy in any project in which they can create builds.
