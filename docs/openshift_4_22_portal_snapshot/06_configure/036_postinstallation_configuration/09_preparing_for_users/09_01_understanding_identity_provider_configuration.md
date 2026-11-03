# 9.1. Understanding identity provider configuration

The OpenShift Container Platform control plane includes a built-in OAuth server. Developers and administrators obtain OAuth access tokens to authenticate themselves to the API. 

As an administrator, you can configure OAuth to specify an identity provider after you install your cluster. 

## 9.1.1. Identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user. 

Note

OpenShift Container Platform usernames containing `/`, `:`, and `%` are not supported. 

## 9.1.2. Supported identity providers

You can configure the following types of identity providers: 

Identity provider| Description  
---|---  
[htpasswd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-htpasswd-identity-provider) |  Configure the `htpasswd` identity provider to validate user names and passwords against a flat file generated using [`htpasswd`](http://httpd.apache.org/docs/2.4/programs/htpasswd.html).   
[Keystone](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-keystone-identity-provider) |  Configure the `keystone` identity provider to integrate your OpenShift Container Platform cluster with Keystone to enable shared authentication with an OpenStack Keystone v3 server configured to store users in an internal database.   
[LDAP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-ldap-identity-provider) |  Configure the `ldap` identity provider to validate user names and passwords against an LDAPv3 server, using simple bind authentication.   
[Basic authentication](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-basic-authentication-identity-provider) |  Configure a `basic-authentication` identity provider for users to log in to OpenShift Container Platform with credentials validated against a remote identity provider. Basic authentication is a generic backend integration mechanism.   
[Request header](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-request-header-identity-provider) |  Configure a `request-header` identity provider to identify users from request header values, such as `X-Remote-User`. It is typically used in combination with an authenticating proxy, which sets the request header value.   
[GitHub or GitHub Enterprise](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-github-identity-provider) |  Configure a `github` identity provider to validate user names and passwords against GitHub or GitHub Enterprise’s OAuth authentication server.   
[GitLab](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-gitlab-identity-provider) |  Configure a `gitlab` identity provider to use [GitLab.com](https://gitlab.com/) or any other GitLab instance as an identity provider.   
[Google](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-google-identity-provider) |  Configure a `google` identity provider using [Google’s OpenID Connect integration](https://developers.google.com/identity/protocols/OpenIDConnect).   
[OpenID Connect](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-oidc-identity-provider) |  Configure an `oidc` identity provider to integrate with an OpenID Connect identity provider using an [Authorization Code Flow](http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth).   
Show more

Once an identity provider has been defined, you can [use RBAC to define and apply permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#authorization-overview_using-rbac). 

## 9.1.3. Identity provider parameters

The following parameters are common to all identity providers: 

Parameter| Description  
---|---  
`name` |  The provider name is prefixed to provider user names to form an identity name.   
`mappingMethod` |  Defines how new identities are mapped to users when they log in. Enter one of the following values: 

claim
     The default value. Provisions a user with the identity’s preferred user name. Fails if a user with that user name is already mapped to another identity. 
lookup
     Looks up an existing identity, user identity mapping, and user, but does not automatically provision users or identities. This allows cluster administrators to set up identities and users manually, or using an external process. Using this method requires you to manually provision users. 
add
     Provisions a user with the identity’s preferred user name. If a user with that user name already exists, the identity is mapped to the existing user, adding to any existing identity mappings for the user. Required when multiple identity providers are configured that identify the same set of users and map to the same user names.   
Show more

Note

When adding or changing identity providers, you can map identities from the new provider to existing users by setting the `mappingMethod` parameter to `add`. 

## 9.1.4. Sample identity provider CR

You can use a custom resource (CR) to see the parameters and default values that you use to configure an identity provider. 

The following example uses the htpasswd identity provider. 

**Sample identity provider CR**

```yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_identity_provider
    mappingMethod: claim
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret
```


where: 

`spec.identityProviders.name`
     Specifies the provider name, which is prefixed to provider user names to form an identity name. 
`spec.identityProviders.mappingMethod`
     Specifies how mappings are established between this provider’s identities and `User` objects. 
`spec.identityProviders.htpasswd.fileData.name`
     Specifies an existing secret containing a file generated using [`htpasswd`](http://httpd.apache.org/docs/2.4/programs/htpasswd.html).
