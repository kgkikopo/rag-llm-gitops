# 5.3. Delete user-owned OAuth access tokens

You can use the following procedure to delete any user-owned OAuth tokens that are no longer needed. 

The `oc logout` command only invalidates the OAuth token for the active session. Deleting an OAuth access token logs out the user from all sessions that use the token. 

**Procedure**

  * Delete the user-owned OAuth access token: 

```shell-session
$ oc delete useroauthaccesstokens <token_name>
```


**Example output**

```shell-session
useroauthaccesstoken.oauth.openshift.io "<token_name>" deleted
```
