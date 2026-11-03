# 15.1. About audit log policy profiles

To monitor activity and maintain compliance, you can apply audit log profiles that define the level of detail recorded for API server requests. While more comprehensive profiles provide request bodies for troubleshooting, they also increase resource overhead on the host system. 

Audit log profiles define how to log requests that come to the OpenShift API server, Kubernetes API server, OpenShift OAuth API server, and OpenShift OAuth server. 

OpenShift Container Platform provides the following predefined audit policy profiles: 

Profile| Description  
---|---  
`Default` |  Logs only metadata for read and write requests; does not log request bodies except for OAuth access token requests. This is the default policy.   
`WriteRequestBodies` |  In addition to logging metadata for all requests, logs request bodies for every write request to the API servers (`create`, `update`, `patch`, `delete`, `deletecollection`). This profile has more resource overhead than the `Default` profile. [1]  
`AllRequestBodies` |  In addition to logging metadata for all requests, logs request bodies for every read and write request to the API servers (`get`, `list`, `create`, `update`, `patch`). This profile has the most resource overhead. [1]  
`None` |  No requests are logged, including OAuth access token requests and OAuth authorize token requests. Custom rules are ignored when this profile is set.  Warning Do not disable audit logging by using the `None` profile unless you are fully aware of the risks of not logging data that can be beneficial when troubleshooting issues. If you disable audit logging and a support situation arises, you might need to enable audit logging and reproduce the issue to troubleshoot properly.   
Show more

  1. Sensitive resources, such as `Secret`, `Route`, and `OAuthClient` objects, are only logged at the metadata level. OpenShift OAuth server events are only logged at the metadata level. 



By default, OpenShift Container Platform uses the `Default` audit log profile. You can use another audit policy profile that also logs request bodies, but be aware of the increased resource usage such as CPU, memory, and I/O.
