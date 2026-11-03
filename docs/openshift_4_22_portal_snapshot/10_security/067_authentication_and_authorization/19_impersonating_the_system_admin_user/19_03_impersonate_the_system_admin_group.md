# 19.3. Impersonate the system:admin group

To impersonate a user who has cluster administration privileges through group membership, you must specify both the user and the associated groups in the impersonation command. 

**Procedure**

  * To grant a user permission to impersonate a `system:admin` by impersonating the associated cluster administration groups, run the following command: 

```shell-session
$ oc create clusterrolebinding <any_valid_name> --clusterrole=sudoer --as=<user> \
--as-group=<group1> --as-group=<group2>
```
