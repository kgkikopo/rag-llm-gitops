# 10.1. Create and assign RBAC roles to users

You can use role-based access control to configure whether users and groups can perform specific actions on cluster or project resources by evaluating roles, rules, and bindings. 

Role-based access control (RBAC) objects determine whether a user is allowed to perform a given action within a project. 

Cluster administrators can use the cluster roles and bindings to control who has various access levels to the OpenShift Container Platform platform itself and all projects. 

Developers can use local roles and bindings to control who has access to their projects. Note that authorization is a separate step from authentication, which is more about determining the identity of who is taking the action. 

Authorization is managed using: 

Authorization object| Description  
---|---  
Rules  |  Sets of permitted verbs on a set of objects. For example, whether a user or service account can `create` pods.   
Roles  |  Collections of rules. You can associate, or bind, users and groups to multiple roles.   
Bindings  |  Associations between users and/or groups with a role.   
Show more

There are two levels of RBAC roles and bindings that control authorization: 

RBAC level| Description  
---|---  
Cluster RBAC  |  Roles and bindings that are applicable across all projects. _Cluster roles_ exist cluster-wide, and _cluster role bindings_ can reference only cluster roles.   
Local RBAC  |  Roles and bindings that are scoped to a given project. While _local roles_ exist only in a single project, local role bindings can reference _both_ cluster and local roles.   
Show more

A cluster role binding is a binding that exists at the cluster level. A role binding exists at the project level. The cluster role _view_ must be bound to a user using a local role binding for that user to view the project. Create local roles only if a cluster role does not provide the set of permissions needed for a particular situation. 

This two-level hierarchy allows reuse across multiple projects through the cluster roles while allowing customization inside of individual projects through local roles. 

During evaluation, both the cluster role bindings and the local role bindings are used. For example: 

  1. Cluster-wide "allow" rules are checked. 
  2. Locally-bound "allow" rules are checked. 
  3. Deny by default. 



## 10.1.1. Default cluster roles

OpenShift Container Platform includes a set of default cluster roles that you can bind to users and groups cluster-wide or locally. 

Important

It is not recommended to manually modify the default cluster roles. Modifications to these system roles can prevent a cluster from functioning properly. 

Default cluster role| Description  
---|---  
`admin` |  A project manager. If used in a local binding, an `admin` has rights to view any resource in the project and modify any resource in the project except for quota.   
`basic-user` |  A user that can get basic information about projects and users.   
`cluster-admin` |  A super-user that can perform any action in any project. When bound to a user with a local binding, they have full control over quota and every action on every resource in the project.   
`cluster-status` |  A user that can get basic cluster status information.   
`cluster-reader` |  A user that can get or view most of the objects but cannot modify them.   
`edit` |  A user that can modify most objects in a project but does not have the power to view or modify roles or bindings.   
`self-provisioner` |  A user that can create their own projects.   
`view` |  A user who cannot make any modifications, but can see most objects in a project. They cannot view or modify roles or bindings.   
Show more

Be mindful of the difference between local and cluster bindings. For example, if you bind the `cluster-admin` role to a user by using a local role binding, it might appear that this user has the privileges of a cluster administrator. This is not the case. Binding the `cluster-admin` to a user in a project grants super administrator privileges for only that project to the user. That user has the permissions of the cluster role `admin`, plus a few additional permissions like the ability to edit rate limits, for that project. This binding can be confusing via the web console UI, which does not list cluster role bindings that are bound to true cluster administrators. However, it does list local role bindings that you can use to locally bind `cluster-admin`. 

The relationships between cluster roles, local roles, cluster role bindings, local role bindings, users, groups and service accounts are illustrated below. 

![OpenShift Container Platform RBAC](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/fad3132dbc5f65494508926853094025/rbac.png) ![OpenShift Container Platform RBAC](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/fad3132dbc5f65494508926853094025/rbac.png)

Warning

The `get pods/exec`, `get pods/*`, and `get *` rules grant execution privileges when they are applied to a role. Apply the principle of least privilege and assign only the minimal RBAC rights required for users and agents. For more information, see "RBAC rules allow execution privileges". 

## 10.1.2. Evaluating authorization

OpenShift Container Platform evaluates authorization by using: 

Identity
     The user name and list of groups that the user belongs to. 
Action
    

The action you perform. In most cases, this consists of: 

  * **Project** : The project you access. A project is a Kubernetes namespace with additional annotations that allows a community of users to organize and manage their content in isolation from other communities. 
  * **Verb** : The action itself: `get`, `list`, `create`, `update`, `delete`, `deletecollection`, or `watch`. 
  * **Resource name** : The API endpoint that you access. 



Bindings
     The full list of bindings, the associations between users or groups with a role. 

OpenShift Container Platform evaluates authorization by using the following steps: 

  1. The identity and the project-scoped action is used to find all bindings that apply to the user or their groups. 
  2. Bindings are used to locate all the roles that apply. 
  3. Roles are used to find all the rules that apply. 
  4. The action is checked against each rule to find a match. 
  5. If no matching rule is found, the action is then denied by default. 



Tip

Remember that users and groups can be associated with, or bound to, multiple roles at the same time. 

Project administrators can use the CLI to view local roles and bindings, including a matrix of the verbs and resources each are associated with. 

Important

The cluster role bound to the project administrator is limited in a project through a local binding. It is not bound cluster-wide like the cluster roles granted to the **cluster-admin** or **system:admin**. 

Cluster roles are roles defined at the cluster level but can be bound either at the cluster level or at the project level. 

## 10.1.3. Cluster role aggregation

The default admin, edit, view, and cluster-reader cluster roles support cluster role aggregation, where the cluster rules for each role are dynamically updated as new rules are created. This feature is relevant only if you extend the Kubernetes API by creating custom resources. 

**Additional resources**

  * [RBAC rules allow execution privileges](https://access.redhat.com/solutions/6989997)
  * [Aggregated ClusterRoles (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles)
