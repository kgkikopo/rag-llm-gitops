# 6.6. Manually provisioning a user when using the lookup mapping method

You can manually provision users when the `lookup` mapping method is enabled. The `lookup` method disables automatic identity-to-user mapping during login, requiring manual provisioning of each user after configuring the identity provider. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create an OpenShift Container Platform user: 

```shell-session
$ oc create user <username>
```


  2. Create an OpenShift Container Platform identity: 

```shell-session
$ oc create identity <identity_provider>:<identity_provider_user_id>
```


Where `<identity_provider_user_id>` is a name that uniquely represents the user in the identity provider. 

  3. Create a user identity mapping for the created user and identity: 

```shell-session
$ oc create useridentitymapping <identity_provider>:<identity_provider_user_id> <username>
```


**Additional resources**

  * [How to create user, identity and map user and identity in LDAP authentication for `mappingMethod` as `lookup` inside the OAuth manifest](https://access.redhat.com/solutions/6006921)
  * [How to create user, identity and map user and identity in OIDC authentication for `mappingMethod` as `lookup`](https://access.redhat.com/solutions/7072510)
