# 10.7. Create a local role

You can create a local role and bind it to a user to define custom permissions within a project. 

**Procedure**

  1. To create a local role for a project, run the following command: 

```shell-session
$ oc create role <name> --verb=<verb> --resource=<resource> -n <project>
```


In this command, specify: 

     * `<name>`, the local role’s name 
     * `<verb>`, a comma-separated list of the verbs to apply to the role 
     * `<resource>`, the resources that the role applies to 
     * `<project>`, the project name 

For example, to create a local role that allows a user to view pods in the `blue` project, run the following command: 

```shell-session
$ oc create role podview --verb=get --resource=pod -n blue
```


  2. To bind the new role to a user, run the following command: 

```shell-session
$ oc adm policy add-role-to-user podview user2 --role-namespace=blue -n blue
```
