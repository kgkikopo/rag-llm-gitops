# 31.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  RouteSpec describes the hostname or path the route exposes, any security information, and one to four backends (services) the route points to. Requests are distributed among the backends depending on the weights assigned to each backend. When using roundrobin scheduling the portion of requests that go to each backend is the backend weight divided by the sum of all of the backend weights. When the backend has more than one endpoint the requests that end up on the backend are roundrobin distributed among the endpoints. Weights are between 0 and 256 with default 100. Weight 0 causes no requests to the backend. If all weights are zero the route will be considered to have no backends and return a standard 503 response.  The `tls` field is optional and allows specific certificates or behavior for the route. Routers typically configure a default certificate on a wildcard domain to terminate routes without explicit certificates, but custom hostnames usually must choose passthrough (send traffic directly to the backend via the TLS Server-Name- Indication field) or provide a certificate.   
`status` |  `object` |  RouteStatus provides relevant info about the status of a route, including which routers acknowledge it.   
Show more

## 31.1.1. .spec

Description
    

RouteSpec describes the hostname or path the route exposes, any security information, and one to four backends (services) the route points to. Requests are distributed among the backends depending on the weights assigned to each backend. When using roundrobin scheduling the portion of requests that go to each backend is the backend weight divided by the sum of all of the backend weights. When the backend has more than one endpoint the requests that end up on the backend are roundrobin distributed among the endpoints. Weights are between 0 and 256 with default 100. Weight 0 causes no requests to the backend. If all weights are zero the route will be considered to have no backends and return a standard 503 response. 

The `tls` field is optional and allows specific certificates or behavior for the route. Routers typically configure a default certificate on a wildcard domain to terminate routes without explicit certificates, but custom hostnames usually must choose passthrough (send traffic directly to the backend via the TLS Server-Name- Indication field) or provide a certificate. 

Type
     `object`
Required
    

  * `to`



Property| Type| Description  
---|---|---  
`alternateBackends` |  `array` |  alternateBackends allows up to 3 additional backends to be assigned to the route. Only the Service kind is allowed, and it will be defaulted to Service. Use the weight field in RouteTargetReference object to specify relative preference.   
`alternateBackends[]` |  `object` |  RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others.   
`host` |  `string` |  host is an alias/DNS that points to the service. Optional. If not specified a route name will typically be automatically chosen. Must follow DNS952 subdomain conventions.   
`httpHeaders` |  `object` |  RouteHTTPHeaders defines policy for HTTP headers.   
`path` |  `string` |  path that the router watches for, to route traffic for to the service. Optional   
`port` |  `object` |  RoutePort defines a port mapping from a router to an endpoint in the service endpoints.   
`subdomain` |  `string` |  subdomain is a DNS subdomain that is requested within the ingress controller’s domain (as a subdomain). If host is set this field is ignored. An ingress controller may choose to ignore this suggested name, in which case the controller will report the assigned name in the status.ingress array or refuse to admit the route. If this value is set and the server does not support this field host will be populated automatically. Otherwise host is left empty. The field may have multiple parts separated by a dot, but not all ingress controllers may honor the request. This field may not be changed after creation except by a user with the update routes/custom-host permission.  Example: subdomain `frontend` automatically receives the router subdomain `apps.mycluster.com` to have a full hostname `frontend.apps.mycluster.com`.   
`tls` |  `object` |  TLSConfig defines config used to secure a route and provide termination   
`to` |  `object` |  RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others.   
`wildcardPolicy` |  `string` |  Wildcard policy if any for the route. Currently only 'Subdomain' or 'None' is allowed.   
Show more

## 31.1.2. .spec.alternateBackends

Description
     alternateBackends allows up to 3 additional backends to be assigned to the route. Only the Service kind is allowed, and it will be defaulted to Service. Use the weight field in RouteTargetReference object to specify relative preference. 
Type
     `array`

## 31.1.3. .spec.alternateBackends[]

Description
     RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`kind` |  `string` |  The kind of target that the route is referring to. Currently, only 'Service' is allowed   
`name` |  `string` |  name of the service/target that is being referred to. e.g. name of the service   
`weight` |  `integer` |  weight as an integer between 0 and 256, default 100, that specifies the target’s relative weight against other target reference objects. 0 suppresses requests to this backend.   
Show more

## 31.1.4. .spec.httpHeaders

Description
     RouteHTTPHeaders defines policy for HTTP headers. 
Type
     `object`

Property| Type| Description  
---|---|---  
`actions` |  `object` |  RouteHTTPHeaderActions defines configuration for actions on HTTP request and response headers.   
Show more

## 31.1.5. .spec.httpHeaders.actions

Description
     RouteHTTPHeaderActions defines configuration for actions on HTTP request and response headers. 
Type
     `object`

Property| Type| Description  
---|---|---  
`request` |  `array` |  request is a list of HTTP request headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the request headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Currently, actions may define to either `Set` or `Delete` headers values. Route actions will be executed after IngressController actions for request headers. Actions are applied in sequence as defined in this list. A maximum of 20 request header actions may be configured. You can use this field to specify HTTP request headers that should be set or deleted when forwarding connections from the client to your application. Sample fetchers allowed are "req.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%[req.hdr(X-target),lower]", "%{+Q}[ssl_c_der,base64]". Any request header configuration applied directly via a Route resource using this API will override header configuration for a header of the same name applied via spec.httpHeaders.actions on the IngressController or route annotation. Note: This field cannot be used if your route uses TLS passthrough.   
`request[]` |  `object` |  RouteHTTPHeader specifies configuration for setting or deleting an HTTP header.   
`response` |  `array` |  response is a list of HTTP response headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the response headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Route actions will be executed before IngressController actions for response headers. Actions are applied in sequence as defined in this list. A maximum of 20 response header actions may be configured. You can use this field to specify HTTP response headers that should be set or deleted when forwarding responses from your application to the client. Sample fetchers allowed are "res.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%[res.hdr(X-target),lower]", "%{+Q}[ssl_c_der,base64]". Note: This field cannot be used if your route uses TLS passthrough.   
`response[]` |  `object` |  RouteHTTPHeader specifies configuration for setting or deleting an HTTP header.   
Show more

## 31.1.6. .spec.httpHeaders.actions.request

Description
     request is a list of HTTP request headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the request headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Currently, actions may define to either `Set` or `Delete` headers values. Route actions will be executed after IngressController actions for request headers. Actions are applied in sequence as defined in this list. A maximum of 20 request header actions may be configured. You can use this field to specify HTTP request headers that should be set or deleted when forwarding connections from the client to your application. Sample fetchers allowed are "req.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%[req.hdr(X-target),lower]", "%{+Q}[ssl_c_der,base64]". Any request header configuration applied directly via a Route resource using this API will override header configuration for a header of the same name applied via spec.httpHeaders.actions on the IngressController or route annotation. Note: This field cannot be used if your route uses TLS passthrough. 
Type
     `array`

## 31.1.7. .spec.httpHeaders.actions.request[]

Description
     RouteHTTPHeader specifies configuration for setting or deleting an HTTP header. 
Type
     `object`
Required
    

  * `name`
  * `action`



Property| Type| Description  
---|---|---  
`action` |  `object` |  RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header.   
`name` |  `string` |  name specifies the name of a header on which to perform an action. Its value must be a valid HTTP header name as defined in RFC 2616 section 4.2. The name must consist only of alphanumeric and the following special characters, "-!#$%&'*+.^_`". The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Cookie, Set-Cookie. It must be no more than 255 characters in length. Header name must be unique.   
Show more

## 31.1.8. .spec.httpHeaders.actions.request[].action

Description
     RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`set` |  `object` |  RouteSetHTTPHeader specifies what value needs to be set on an HTTP header.   
`type` |  `string` |  type defines the type of the action to be applied on the header. Possible values are Set or Delete. Set allows you to set HTTP request and response headers. Delete allows you to delete HTTP request and response headers.   
Show more

## 31.1.9. .spec.httpHeaders.actions.request[].action.set

Description
     RouteSetHTTPHeader specifies what value needs to be set on an HTTP header. 
Type
     `object`
Required
    

  * `value`



Property| Type| Description  
---|---|---  
`value` |  `string` |  value specifies a header value. Dynamic values can be added. The value will be interpreted as an HAProxy format string as defined in <http://cbonte.github.io/haproxy-dconv/2.6/configuration.html#8.2.6> and may use HAProxy’s %[] syntax and otherwise must be a valid HTTP header value as defined in <https://datatracker.ietf.org/doc/html/rfc7230#section-3.2>. The value of this field must be no more than 16384 characters in length. Note that the total size of all net added headers **after** interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController.   
Show more

## 31.1.10. .spec.httpHeaders.actions.response

Description
     response is a list of HTTP response headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the response headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Route actions will be executed before IngressController actions for response headers. Actions are applied in sequence as defined in this list. A maximum of 20 response header actions may be configured. You can use this field to specify HTTP response headers that should be set or deleted when forwarding responses from your application to the client. Sample fetchers allowed are "res.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%[res.hdr(X-target),lower]", "%{+Q}[ssl_c_der,base64]". Note: This field cannot be used if your route uses TLS passthrough. 
Type
     `array`

## 31.1.11. .spec.httpHeaders.actions.response[]

Description
     RouteHTTPHeader specifies configuration for setting or deleting an HTTP header. 
Type
     `object`
Required
    

  * `name`
  * `action`



Property| Type| Description  
---|---|---  
`action` |  `object` |  RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header.   
`name` |  `string` |  name specifies the name of a header on which to perform an action. Its value must be a valid HTTP header name as defined in RFC 2616 section 4.2. The name must consist only of alphanumeric and the following special characters, "-!#$%&'*+.^_`". The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Cookie, Set-Cookie. It must be no more than 255 characters in length. Header name must be unique.   
Show more

## 31.1.12. .spec.httpHeaders.actions.response[].action

Description
     RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`set` |  `object` |  RouteSetHTTPHeader specifies what value needs to be set on an HTTP header.   
`type` |  `string` |  type defines the type of the action to be applied on the header. Possible values are Set or Delete. Set allows you to set HTTP request and response headers. Delete allows you to delete HTTP request and response headers.   
Show more

## 31.1.13. .spec.httpHeaders.actions.response[].action.set

Description
     RouteSetHTTPHeader specifies what value needs to be set on an HTTP header. 
Type
     `object`
Required
    

  * `value`



Property| Type| Description  
---|---|---  
`value` |  `string` |  value specifies a header value. Dynamic values can be added. The value will be interpreted as an HAProxy format string as defined in <http://cbonte.github.io/haproxy-dconv/2.6/configuration.html#8.2.6> and may use HAProxy’s %[] syntax and otherwise must be a valid HTTP header value as defined in <https://datatracker.ietf.org/doc/html/rfc7230#section-3.2>. The value of this field must be no more than 16384 characters in length. Note that the total size of all net added headers **after** interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController.   
Show more

## 31.1.14. .spec.port

Description
     RoutePort defines a port mapping from a router to an endpoint in the service endpoints. 
Type
     `object`
Required
    

  * `targetPort`



Property| Type| Description  
---|---|---  
`targetPort` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  The target port on pods selected by the service this route points to. If this is a string, it will be looked up as a named port in the target endpoints port list. Required   
Show more

## 31.1.15. .spec.tls

Description
     TLSConfig defines config used to secure a route and provide termination 
Type
     `object`
Required
    

  * `termination`



Property| Type| Description  
---|---|---  
`caCertificate` |  `string` |  caCertificate provides the cert authority certificate contents   
`certificate` |  `string` |  certificate provides certificate contents. This should be a single serving certificate, not a certificate chain. Do not include a CA certificate.   
`destinationCACertificate` |  `string` |  destinationCACertificate provides the contents of the ca certificate of the final destination. When using reencrypt termination this file should be provided in order to have routers use it for health checks on the secure connection. If this field is not specified, the router may provide its own destination CA and perform hostname validation using the short service name (service.namespace.svc), which allows infrastructure generated certificates to automatically verify.   
`externalCertificate` |  `object` |  LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.   
`insecureEdgeTerminationPolicy` |  `string` |  insecureEdgeTerminationPolicy indicates the desired behavior for insecure connections to a route. While each router may make its own decisions on which ports to expose, this is normally port 80.  If a route does not specify insecureEdgeTerminationPolicy, then the default behavior is "None".  * Allow - traffic is sent to the server on the insecure port (edge/reencrypt terminations only).  * None - no traffic is allowed on the insecure port (default).  * Redirect - clients are redirected to the secure port.   
`key` |  `string` |  key provides key file contents   
`termination` |  `string` |  termination indicates the TLS termination type.  * edge - TLS termination is done by the router and http is used to communicate with the backend (default)  * passthrough - Traffic is sent straight to the destination without the router providing TLS termination  * reencrypt - TLS termination is done by the router and https is used to communicate with the backend  Note: passthrough termination is incompatible with httpHeader actions   
Show more

## 31.1.16. .spec.tls.externalCertificate

Description
     LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 31.1.17. .spec.to

Description
     RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`kind` |  `string` |  The kind of target that the route is referring to. Currently, only 'Service' is allowed   
`name` |  `string` |  name of the service/target that is being referred to. e.g. name of the service   
`weight` |  `integer` |  weight as an integer between 0 and 256, default 100, that specifies the target’s relative weight against other target reference objects. 0 suppresses requests to this backend.   
Show more

## 31.1.18. .status

Description
     RouteStatus provides relevant info about the status of a route, including which routers acknowledge it. 
Type
     `object`

Property| Type| Description  
---|---|---  
`ingress` |  `array` |  ingress describes the places where the route may be exposed. The list of ingress points may contain duplicate Host or RouterName values. Routes are considered live once they are `Ready`  
`ingress[]` |  `object` |  RouteIngress holds information about the places where a route is exposed.   
Show more

## 31.1.19. .status.ingress

Description
     ingress describes the places where the route may be exposed. The list of ingress points may contain duplicate Host or RouterName values. Routes are considered live once they are `Ready`
Type
     `array`

## 31.1.20. .status.ingress[]

Description
     RouteIngress holds information about the places where a route is exposed. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is the state of the route, may be empty.   
`conditions[]` |  `object` |  RouteIngressCondition contains details for the current condition of this route on a particular router.   
`host` |  `string` |  host is the host string under which the route is exposed; this value is required   
`routerCanonicalHostname` |  `string` |  CanonicalHostname is the external host name for the router that can be used as a CNAME for the host requested for this route. This value is optional and may not be set in all cases.   
`routerName` |  `string` |  Name is a name chosen by the router to identify itself; this value is required   
`wildcardPolicy` |  `string` |  Wildcard policy is the wildcard policy that was allowed where this route is exposed.   
Show more

## 31.1.21. .status.ingress[].conditions

Description
     conditions is the state of the route, may be empty. 
Type
     `array`

## 31.1.22. .status.ingress[].conditions[]

Description
     RouteIngressCondition contains details for the current condition of this route on a particular router. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  RFC 3339 date and time when this condition last transitioned   
`message` |  `string` |  Human readable message indicating details about last transition.   
`reason` |  `string` |  (brief) reason for the condition’s last transition, and is usually a machine and human readable constant   
`status` |  `string` |  status is the status of the condition. Can be True, False, Unknown.   
`type` |  `string` |  type is the type of the condition. Currently only Admitted or UnservableInFutureVersions.   
Show more
