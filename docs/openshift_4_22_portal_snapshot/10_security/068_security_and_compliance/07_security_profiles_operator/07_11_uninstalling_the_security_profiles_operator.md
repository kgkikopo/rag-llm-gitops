# 7.11. Uninstalling the Security Profiles Operator

You can remove the Security Profiles Operator from your cluster by using the OpenShift Container Platform web console. 

## 7.11.1. Uninstall the Security Profiles Operator by using the web console

To remove the Security Profiles Operator, you must first delete the `seccomp` and SELinux profiles. After the profiles are removed, you can then remove the Operator and its namespace by deleting the **openshift-security-profiles** project. 

**Prerequisites**

  * You have access to the web console as a user with `cluster-admin` privileges. 
  * The Security Profiles Operator is installed. 



**Procedure**

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Delete all `seccomp` profiles, SELinux profiles, and webhook configurations. 
  3. Switch to the **Administration** **Ecosystem** **Installed Operators** page. 
  4. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) on the **Security Profiles Operator** entry. 
  5. Select **Uninstall Operator**. 
  6. Switch to the **Home** **Projects** page. 
  7. Search for `security profiles`. 
  8. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **openshift-security-profiles** project. 
  9. Select **Delete Project**. 

     1. Enter `openshift-security-profiles` in the dialog box. 
     2. Click **Delete**. 

  10. Delete the `MutatingWebhookConfiguration` object by running the following command: 

```shell-session
$ oc delete MutatingWebhookConfiguration spo-mutating-webhook-configuration
```
