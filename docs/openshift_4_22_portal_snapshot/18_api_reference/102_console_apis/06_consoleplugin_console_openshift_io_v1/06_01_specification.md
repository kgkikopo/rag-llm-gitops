# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec contains the desired configuration for the console plugin.   
Show more

## 6.1.1. .spec

Description
     spec contains the desired configuration for the console plugin. 
Type
     `object`
Required
    

  * `backend`
  * `displayName`



Property| Type| Description  
---|---|---  
`backend` |  `object` |  backend holds the configuration of backend which is serving console’s plugin .   
`contentSecurityPolicy` |  `array` |  contentSecurityPolicy is a list of Content-Security-Policy (CSP) directives for the plugin. Each directive specifies a list of values, appropriate for the given directive type, for example a list of remote endpoints for fetch directives such as ScriptSrc. Console web application uses CSP to detect and mitigate certain types of attacks, such as cross-site scripting (XSS) and data injection attacks. Dynamic plugins should specify this field if need to load assets from outside the cluster or if violation reports are observed. Dynamic plugins should always prefer loading their assets from within the cluster, either by vendoring them, or fetching from a cluster service. CSP violation reports can be viewed in the browser’s console logs during development and testing of the plugin in the OpenShift web console. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. Each of the available directives may be defined only once in the list. The value 'self' is automatically included in all fetch directives by the OpenShift web console’s backend. For more information about the CSP directives, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy> The OpenShift web console server aggregates the CSP directives and values across its own default values and all enabled ConsolePlugin CRs, merging them into a single policy string that is sent to the browser via `Content-Security-Policy` HTTP response header.  Example: ConsolePlugin A directives: script-src: <https://script1.com/>, <https://script2.com/> font-src: <https://font1.com/> ConsolePlugin B directives: script-src: <https://script2.com/>, <https://script3.com/> font-src: <https://font2.com/> img-src: <https://img1.com/> Unified set of CSP directives, passed to the OpenShift web console server: script-src: <https://script1.com/>, <https://script2.com/>, <https://script3.com/> font-src: <https://font1.com/>, <https://font2.com/> img-src: <https://img1.com/> OpenShift web console server CSP response header: Content-Security-Policy: default-src 'self'; base-uri 'self'; script-src 'self' <https://script1.com/> <https://script2.com/> <https://script3.com/>; font-src 'self' <https://font1.com/> <https://font2.com/>; img-src 'self' <https://img1.com/>; style-src 'self'; frame-src 'none'; object-src 'none'   
`contentSecurityPolicy[]` |  `object` |  ConsolePluginCSP holds configuration for a specific CSP directive   
`displayName` |  `string` |  displayName is the display name of the plugin. The dispalyName should be between 1 and 128 characters.   
`i18n` |  `object` |  i18n is the configuration of plugin’s localization resources.   
`proxy` |  `array` |  proxy is a list of proxies that describe various service type to which the plugin needs to connect to.   
`proxy[]` |  `object` |  ConsolePluginProxy holds information on various service types to which console’s backend will proxy the plugin’s requests.   
Show more

## 6.1.2. .spec.backend

Description
     backend holds the configuration of backend which is serving console’s plugin . 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`service` |  `object` |  service is a Kubernetes Service that exposes the plugin using a deployment with an HTTP server. The Service must use HTTPS and Service serving certificate. The console backend will proxy the plugins assets from the Service using the service CA bundle.   
`type` |  `string` |  type is the backend type which servers the console’s plugin. Currently only "Service" is supported.   
Show more

## 6.1.3. .spec.backend.service

Description
     service is a Kubernetes Service that exposes the plugin using a deployment with an HTTP server. The Service must use HTTPS and Service serving certificate. The console backend will proxy the plugins assets from the Service using the service CA bundle. 
Type
     `object`
Required
    

  * `name`
  * `namespace`
  * `port`



Property| Type| Description  
---|---|---  
`basePath` |  `string` |  basePath is the path to the plugin’s assets. The primary asset it the manifest file called `plugin-manifest.json`, which is a JSON document that contains metadata about the plugin and the extensions.   
`name` |  `string` |  name of Service that is serving the plugin assets.   
`namespace` |  `string` |  namespace of Service that is serving the plugin assets.   
`port` |  `integer` |  port on which the Service that is serving the plugin is listening to.   
Show more

## 6.1.4. .spec.contentSecurityPolicy

Description
    

contentSecurityPolicy is a list of Content-Security-Policy (CSP) directives for the plugin. Each directive specifies a list of values, appropriate for the given directive type, for example a list of remote endpoints for fetch directives such as ScriptSrc. Console web application uses CSP to detect and mitigate certain types of attacks, such as cross-site scripting (XSS) and data injection attacks. Dynamic plugins should specify this field if need to load assets from outside the cluster or if violation reports are observed. Dynamic plugins should always prefer loading their assets from within the cluster, either by vendoring them, or fetching from a cluster service. CSP violation reports can be viewed in the browser’s console logs during development and testing of the plugin in the OpenShift web console. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. Each of the available directives may be defined only once in the list. The value 'self' is automatically included in all fetch directives by the OpenShift web console’s backend. For more information about the CSP directives, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>

The OpenShift web console server aggregates the CSP directives and values across its own default values and all enabled ConsolePlugin CRs, merging them into a single policy string that is sent to the browser via `Content-Security-Policy` HTTP response header. 

Example: ConsolePlugin A directives: script-src: <https://script1.com/>, <https://script2.com/> font-src: <https://font1.com/>

```plaintext
ConsolePlugin B directives:
  script-src: https://script2.com/, https://script3.com/
  font-src: https://font2.com/
  img-src: https://img1.com/
```


```plaintext
Unified set of CSP directives, passed to the OpenShift web console server:
  script-src: https://script1.com/, https://script2.com/, https://script3.com/
  font-src: https://font1.com/, https://font2.com/
  img-src: https://img1.com/
```


```plaintext
OpenShift web console server CSP response header:
  Content-Security-Policy: default-src 'self'; base-uri 'self'; script-src 'self' https://script1.com/ https://script2.com/ https://script3.com/; font-src 'self' https://font1.com/ https://font2.com/; img-src 'self' https://img1.com/; style-src 'self'; frame-src 'none'; object-src 'none'
```


Type
     `array`

## 6.1.5. .spec.contentSecurityPolicy[]

Description
     ConsolePluginCSP holds configuration for a specific CSP directive 
Type
     `object`
Required
    

  * `directive`
  * `values`



Property| Type| Description  
---|---|---  
`directive` |  `string` |  directive specifies which Content-Security-Policy directive to configure. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. DefaultSrc directive serves as a fallback for the other CSP fetch directives. For more information about the DefaultSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/default-src> ScriptSrc directive specifies valid sources for JavaScript. For more information about the ScriptSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src> StyleSrc directive specifies valid sources for stylesheets. For more information about the StyleSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/style-src> ImgSrc directive specifies a valid sources of images and favicons. For more information about the ImgSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/img-src> FontSrc directive specifies valid sources for fonts loaded using @font-face. For more information about the FontSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/font-src> ConnectSrc directive restricts the URLs which can be loaded using script interfaces. For more information about the ConnectSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src>  
`values` |  `array (string)` |  values defines an array of values to append to the console defaults for this directive. Each ConsolePlugin may define their own directives with their values. These will be set by the OpenShift web console’s backend, as part of its Content-Security-Policy header. The array can contain at most 16 values. Each directive value must have a maximum length of 1024 characters and must not contain whitespace, commas (,), semicolons (;) or single quotes ('). The value '*' is not permitted. Each value in the array must be unique.   
Show more

## 6.1.6. .spec.i18n

Description
     i18n is the configuration of plugin’s localization resources. 
Type
     `object`
Required
    

  * `loadType`



Property| Type| Description  
---|---|---  
`loadType` |  `string` |  loadType indicates how the plugin’s localization resource should be loaded. Valid values are Preload, Lazy and the empty string. When set to Preload, all localization resources are fetched when the plugin is loaded. When set to Lazy, localization resources are lazily loaded as and when they are required by the console. When omitted or set to the empty string, the behaviour is equivalent to Lazy type.   
Show more

## 6.1.7. .spec.proxy

Description
     proxy is a list of proxies that describe various service type to which the plugin needs to connect to. 
Type
     `array`

## 6.1.8. .spec.proxy[]

Description
     ConsolePluginProxy holds information on various service types to which console’s backend will proxy the plugin’s requests. 
Type
     `object`
Required
    

  * `alias`
  * `endpoint`



Property| Type| Description  
---|---|---  
`alias` |  `string` |  alias is a proxy name that identifies the plugin’s proxy. An alias name should be unique per plugin. The console backend exposes following proxy endpoint:  /api/proxy/plugin/<plugin-name>/<proxy-alias>/<request-path>?<optional-query-parameters> Request example path:  /api/proxy/plugin/acm/search/pods?namespace=openshift-apiserver   
`authorization` |  `string` |  authorization provides information about authorization type, which the proxied request should contain   
`caCertificate` |  `string` |  caCertificate provides the cert authority certificate contents, in case the proxied Service is using custom service CA. By default, the service CA bundle provided by the service-ca operator is used.   
`endpoint` |  `object` |  endpoint provides information about endpoint to which the request is proxied to.   
Show more

## 6.1.9. .spec.proxy[].endpoint

Description
     endpoint provides information about endpoint to which the request is proxied to. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`service` |  `object` |  service is an in-cluster Service that the plugin will connect to. The Service must use HTTPS. The console backend exposes an endpoint in order to proxy communication between the plugin and the Service. Note: service field is required for now, since currently only "Service" type is supported.   
`type` |  `string` |  type is the type of the console plugin’s proxy. Currently only "Service" is supported.   
Show more

## 6.1.10. .spec.proxy[].endpoint.service

Description
     service is an in-cluster Service that the plugin will connect to. The Service must use HTTPS. The console backend exposes an endpoint in order to proxy communication between the plugin and the Service. Note: service field is required for now, since currently only "Service" type is supported. 
Type
     `object`
Required
    

  * `name`
  * `namespace`
  * `port`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of Service that the plugin needs to connect to.   
`namespace` |  `string` |  namespace of Service that the plugin needs to connect to   
`port` |  `integer` |  port on which the Service that the plugin needs to connect to is listening on.   
Show more
