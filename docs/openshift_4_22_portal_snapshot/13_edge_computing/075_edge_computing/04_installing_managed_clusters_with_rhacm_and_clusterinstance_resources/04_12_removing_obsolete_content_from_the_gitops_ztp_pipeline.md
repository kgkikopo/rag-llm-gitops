# 4.12. Removing obsolete content from the GitOps ZTP pipeline

If a change to the `PolicyGenerator` or `PolicyGentemplate` configuration results in obsolete policies, for example, if you rename policies, use the following procedure to remove the obsolete policies. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 



**Procedure**

  1. Remove the affected `PolicyGenerator` or `PolicyGentemplate` files from the Git repository, commit and push to the remote repository. 
  2. Wait for the changes to synchronize through the application and the affected policies to be removed from the hub cluster. 
  3. Add the updated `PolicyGenerator` or `PolicyGentemplate` files back to the Git repository, and then commit and push to the remote repository. 

Note

Removing GitOps Zero Touch Provisioning (ZTP) policies from the Git repository, and as a result also removing them from the hub cluster, does not affect the configuration of the managed cluster. The policy and CRs managed by that policy remains in place on the managed cluster. 

  4. Optional: As an alternative, after making changes to `PolicyGenerator` or `PolicyGentemplate` CRs that result in obsolete policies, you can remove these policies from the hub cluster manually. You can delete policies from the RHACM console using the **Governance** tab or by running the following command: 

```shell-session
$ oc delete policy -n <namespace> <policy_name>
```
