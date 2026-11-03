# 11.3. Restricting build strategies to a user within a project

Similar to granting the build strategy role to a user globally, you can allow a set of specific users within a project to create builds with a particular strategy. 

**Procedure**

  * Assign the role that corresponds to the build strategy to a specific user within a project. For example, to add the `system:build-strategy-docker` role within the project `devproject` to the user `devuser`: 

```shell-session
$ oc adm policy add-role-to-user system:build-strategy-docker devuser -n devproject
```
