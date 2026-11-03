# 10.2. Configure the OAuth server for a hosted cluster by using the web console

You can configure the internal OAuth server for your hosted cluster by using the OpenShift Container Platform web console. 

You can configure OAuth for the following supported identity providers: 

  * `oidc`
  * `htpasswd`
  * `keystone`
  * `ldap`
  * `basic-authentication`
  * `request-header`
  * `github`
  * `gitlab`
  * `google`



Adding any identity provider in the OAuth configuration removes the default `kubeadmin` user provider. 

Note

When you configure identity providers, you must configure at least one `NodePool` replica in your hosted cluster in advance. Traffic for DNS resolution is sent through the worker nodes. You do not need to configure the `NodePool` replicas in advance for the `htpasswd` and `request-header` identity providers. 

**Prerequisites**

  * You logged in as a user with `cluster-admin` privileges. 
  * You created your hosted cluster. 



**Procedure**

  1. Go to **Home** **API Explorer**. 
  2. Use the **Filter by kind** box to search for your `HostedCluster` resource. 
  3. Click the `HostedCluster` resource that you want to edit. 
  4. Click the **Instances** tab. 
  5. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hosted_control_planes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to your hosted cluster name entry and click **Edit HostedCluster**. 
  6. Add the OAuth configuration in the YAML file: 

```yaml
apiVersion: hypershift.openshift.io/v1alpha1
kind: HostedCluster
metadata:
  #...
spec:
  configuration:
    oauth:
      identityProviders:
      - openID:
          claims:
            email:
              - <email_address>
            name:
              - <display_name>
            preferredUsername:
              - <preferred_username>
          clientID: <client_id>
          clientSecret:
            name: <client_id_secret_name>
          issuer: https://example.com/identity
        mappingMethod: lookup
        name: IAM
        type: OpenID
```


     * `spec.configuration.oauth.identityProviders.openID` specifies the provider name that is prefixed to the value of the identity claim to form an identity name. The provider name is also used to build the redirect URL. 
     * `spec.configuration.oauth.identityProviders.openID.claims.email` defines a list of attributes to use as the email address. 
     * `spec.configuration.oauth.identityProviders.openID.claims.name` defines a list of attributes to use as a display name. 
     * `spec.configuration.oauth.identityProviders.openID.claims.preferredUsername` defines a list of attributes to use as a preferred user name. 
     * `spec.configuration.oauth.identityProviders.openID.clientID` defines the ID of a client registered with the OpenID provider. You must allow the client to redirect to the `https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>` URL. 
     * `spec.configuration.oauth.identityProviders.openID.clientSecret.name` defines a secret of a client registered with the OpenID provider. 
     * `spec.configuration.oauth.identityProviders.openID.issuer` specifies the Issuer Identifier described in the OpenID spec. You must use `https` without query or fragment component. For more information, see "Issuer Identifier". 
     * `spec.configuration.oauth.identityProviders.mappingMethod` defines a mapping method that controls how mappings are established between identities of this provider and `User` objects. 

  7. Click **Save**.
