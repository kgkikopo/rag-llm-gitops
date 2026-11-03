# 1.2. About authentication in OpenShift Container Platform

To control access to an OpenShift Container Platform cluster, a cluster administrator can configure [user authentication](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/understanding-authentication "Chapter 2. Understanding authentication") and ensure only approved users access the cluster. 

To interact with an OpenShift Container Platform cluster, users must first authenticate to the OpenShift Container Platform API in some way. You can authenticate by providing an [OAuth access token or an X.509 client certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/understanding-authentication#rbac-api-authentication_understanding-authentication "2.3. API authentication") in your requests to the OpenShift Container Platform API. 

Note

If you do not present a valid access token or certificate, your request is unauthenticated and you receive an HTTP 401 error. 

An administrator can configure authentication through the following tasks: 

  * Configuring an identity provider: You can define any [supported identity provider in OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/understanding-identity-provider#supported-identity-providers_understanding-identity-provider "6.2. Supported identity providers") and add it to your cluster. 
  * [Configuring the internal OAuth server](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/configuring-internal-oauth "Chapter 3. Configuring the internal OAuth server"): The OpenShift Container Platform control plane includes a built-in OAuth server that determines the user’s identity from the configured identity provider and creates an access token. You can configure the token duration and inactivity timeout, and customize the internal OAuth server URL. 

Note

Users can [view and manage OAuth tokens owned by them](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-oauth-access-tokens "Chapter 5. Managing user-owned OAuth access tokens"). 

  * Registering an OAuth client: OpenShift Container Platform includes several [default OAuth clients](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/configuring-oauth-clients#oauth-default-clients_configuring-oauth-clients "4.1. Default OAuth clients"). You can [register and configure additional OAuth clients](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/configuring-oauth-clients#oauth-register-additional-client_configuring-oauth-clients "4.2. Register an additional OAuth client"). 

Note

When users send a request for an OAuth token, they must specify either a default or custom OAuth client that receives and uses the token. 

  * Managing cloud provider credentials using the [Cloud Credentials Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-cloud-provider-credentials#about-cloud-credential-operator "21.1. About the Cloud Credential Operator"): Cluster components use cloud provider credentials to get permissions required to perform cluster-related tasks. 
  * Impersonating a system admin user: You can grant cluster administrator permissions to a user by [impersonating a system admin user](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/impersonating-system-admin "Chapter 19. Impersonating the system:admin user").
