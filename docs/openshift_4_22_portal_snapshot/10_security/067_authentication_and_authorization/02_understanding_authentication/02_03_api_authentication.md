# 2.3. API authentication

Requests to the OpenShift Container Platform API are authenticated using OAuth access tokens or X.509 client certificates, with invalid credentials rejected and anonymous requests assigned virtual user and group identities for authorization processing. 

OAuth access tokens
    

  * Obtained from the OpenShift Container Platform OAuth server using the `_< namespace_route>_/oauth/authorize` and `_< namespace_route>_/oauth/token` endpoints. 
  * Sent as an `Authorization: Bearer…​` header. 
  * Sent as a websocket subprotocol header in the form `base64url.bearer.authorization.k8s.io.<base64url-encoded-token>` for websocket requests. 



X.509 client certificates
    

  * Requires an HTTPS connection to the API server. 
  * Verified by the API server against a trusted certificate authority bundle. 
  * The API server creates and distributes certificates to controllers to authenticate themselves. 



Any request with an invalid access token or an invalid certificate is rejected by the authentication layer with a `401` error. 

If no access token or certificate is presented, the authentication layer assigns the `system:anonymous` virtual user and the `system:unauthenticated` virtual group to the request. This allows the authorization layer to determine which requests, if any, an anonymous user is allowed to make. 

## 2.3.1. OpenShift Container Platform OAuth server

The OpenShift Container Platform Control Plane includes a built-in OAuth server. Users obtain OAuth access tokens to authenticate themselves to the API. 

When a person requests a new OAuth token, the OAuth server uses the configured identity provider to determine the identity of the person making the request. 

It then determines what user that identity maps to, creates an access token for that user, and returns the token for use. 

## 2.3.2. OAuth token requests

OpenShift Container Platform automatically creates OAuth clients to handle token requests from different user agents, including browser-based and CLI tools. These clients interact with OAuth endpoints to authenticate users through interactive login flows or WWW-Authenticate challenges. 

The following OAuth clients are automatically created when starting the OpenShift Container Platform API: 

OAuth client| Usage  
---|---  
`openshift-browser-client` |  Requests tokens at `<namespace_route>/oauth/token/request` with a user-agent that can handle interactive logins. [1]  
`openshift-challenging-client` |  Requests tokens with a user-agent that can handle `WWW-Authenticate` challenges.   
Show more

  1. `<namespace_route>` refers to the namespace route. This is found by running the following command: 

```shell-session
$ oc get route oauth-openshift -n openshift-authentication -o json | jq .spec.host
```


All requests for OAuth tokens involve a request to `<namespace_route>/oauth/authorize`. Most authentication integrations place an authenticating proxy in front of this endpoint, or configure OpenShift Container Platform to validate credentials against a backing identity provider. Requests to `<namespace_route>/oauth/authorize` can come from user-agents that cannot display interactive login pages, such as the CLI. Therefore, OpenShift Container Platform supports authenticating using a `WWW-Authenticate` challenge in addition to interactive login flows. 

If an authenticating proxy is placed in front of the `<namespace_route>/oauth/authorize` endpoint, it sends unauthenticated, non-browser user-agents `WWW-Authenticate` challenges rather than displaying an interactive login page or redirecting to an interactive login flow. 

Note

To prevent cross-site request forgery (CSRF) attacks against browser clients, only send Basic authentication challenges with if a `X-CSRF-Token` header is on the request. Clients that expect to receive Basic `WWW-Authenticate` challenges must set this header to a non-empty value. 

If the authenticating proxy cannot support `WWW-Authenticate` challenges, or if OpenShift Container Platform is configured to use an identity provider that does not support WWW-Authenticate challenges, you must use a browser to manually obtain a token from `<namespace_route>/oauth/token/request`. 

### 2.3.2.1. API impersonation

You can configure API requests in OpenShift Container Platform to act as another user. Impersonation allows you to perform actions on behalf of another account without switching credentials. 

**Additional resources**

  * [User impersonation (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation)



### 2.3.2.2. Authentication metrics for Prometheus

You can use Prometheus metrics to monitor login activity and troubleshoot authentication failures. 

OpenShift Container Platform captures the following Prometheus metrics that track authentication attempts and outcomes for both the CLI and web console: 

  * `openshift_auth_basic_password_count` counts the number of `oc login` user name and password attempts. 
  * `openshift_auth_basic_password_count_result` counts the number of `oc login` user name and password attempts by result, `success` or `error`. 
  * `openshift_auth_form_password_count` counts the number of web console login attempts. 
  * `openshift_auth_form_password_count_result` counts the number of web console login attempts by result, `success` or `error`. 
  * `openshift_auth_password_total` counts the total number of `oc login` and web console login attempts.
