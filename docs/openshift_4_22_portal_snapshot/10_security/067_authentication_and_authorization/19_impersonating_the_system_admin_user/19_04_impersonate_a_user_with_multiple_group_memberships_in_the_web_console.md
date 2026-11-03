# 19.4. Impersonate a user with multiple group memberships in the web console

You can start user impersonation from multiple locations in the OpenShift Container Platform Console. Depending on where you start, you can impersonate a single user, a single group, or a user with one or more group memberships. 

**Prerequisites**

  * You must be logged in to the OpenShift Container Platform web console as a user with permission to impersonate other users. 
  * The user or group that you want to impersonate must already exist. 



Note

The impersonated user can belong to zero or more groups. 

**Procedure**

  1. From the **Overview** page in the OpenShift Container Platform console, click your user name and select **Impersonate User**. 
  2. In the **Username** field in the **Impersonate** dialog, enter the name of the user you want to impersonate. 
  3. Optional: In the **Groups** field, choose one or more groups that are associated with the user. 

The dialog displays a warning message explaining that impersonation applies the effective permissions of the specified user and any selected groups. 

  4. Click **Impersonate** to impersonate your selected user, groups, or both. 



Note

Selecting one group uses the existing single-group impersonation behavior. Selecting no groups uses regular single-user impersonation.
