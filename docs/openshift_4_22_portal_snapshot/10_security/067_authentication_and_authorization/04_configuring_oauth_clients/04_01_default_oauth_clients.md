# 4.1. Default OAuth clients

OpenShift Container Platform automatically creates OAuth clients for browser-based logins, CLI authentication, and challenge-based authentication when the API starts. 

The following OAuth clients are created: 

OAuth client| Usage  
---|---  
`openshift-browser-client` |  Requests tokens at `<namespace_route>/oauth/token/request` with a user-agent that can handle interactive logins.   
`openshift-challenging-client` |  Requests tokens with a user-agent that can handle `WWW-Authenticate` challenges.   
`openshift-cli-client` |  Requests tokens by using a local HTTP server fetching an authorization code grant.   
Show more

where: 

`<namespace_route>`
    

Specifies the namespace route. Find this value by running the following command: 

```shell-session
$ oc get route oauth-openshift -n openshift-authentication -o json | jq .spec.host
```
