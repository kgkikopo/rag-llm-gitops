# 6.10. Uninstalling the File Integrity Operator

You can remove the File Integrity Operator from your cluster by using the OpenShift Container Platform web console. 

## 6.10.1. Uninstall the File Integrity Operator using the web console

To remove the File Integrity Operator, you must first delete the `FileIntegrity` objects in all namespaces. After the objects are removed, you can then remove the Operator and its namespace. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster that uses an account with `cluster-admin` permissions. 
  * The File Integrity Operator is installed. 



**Procedure**

  1. Navigate to the **Ecosystem** **Installed Operators** **File Integrity Operator** page. 
  2. From the **File Integrity** tab, ensure the **Show operands in: All namespaces** default option is selected to list all `FileIntegrity` objects in all namespaces. 
  3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) for a `FileIntegrity` object. 
  4. Select **Delete FileIntegrity**. 
  5. Repeat the previous two steps until no `FileIntegrity` objects remain. 
  6. Go to the **Administration** **Ecosystem** **Installed Operators** page. 
  7. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) on the **File Integrity Operator** entry. 
  8. Select **Uninstall Operator**. 
  9. Go to the **Home** **Projects** page. 
  10. Search for `openshift-file-integrity`. 
  11. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) for the **openshift-file-integrity** project entry. 
  12. Select **Delete Project**. A **Delete Project** dialog box opens on the web console. 



**Verification**

  * Type `openshift-file-integrity` in the **Delete Project** dialog box. 
  * Click the **Delete** button.
