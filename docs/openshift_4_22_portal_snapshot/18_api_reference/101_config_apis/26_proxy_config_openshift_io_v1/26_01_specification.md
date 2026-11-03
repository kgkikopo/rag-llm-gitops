# 26.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user-settable values for the proxy configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 26.1.1. .spec

Description
     spec holds user-settable values for the proxy configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`httpProxy` |  `string` |  httpProxy is the URL of the proxy for HTTP requests. Empty means unset and will not result in an env var.   
`httpsProxy` |  `string` |  httpsProxy is the URL of the proxy for HTTPS requests. Empty means unset and will not result in an env var.   
`noProxy` |  `string` |  noProxy is a comma-separated list of hostnames and/or CIDRs and/or IPs for which the proxy should not be used. Empty means unset and will not result in an env var.   
`readinessEndpoints` |  `array (string)` |  readinessEndpoints is a list of endpoints used to verify readiness of the proxy.   
`trustedCA` |  `object` |  trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well.  The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml):  apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: | -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE-----   
Show more

## 26.1.2. .spec.trustedCA

Description
    

trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well. 

The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml): 

apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: \| -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE----- 

Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 26.1.3. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`

Property| Type| Description  
---|---|---  
`httpProxy` |  `string` |  httpProxy is the URL of the proxy for HTTP requests.   
`httpsProxy` |  `string` |  httpsProxy is the URL of the proxy for HTTPS requests.   
`noProxy` |  `string` |  noProxy is a comma-separated list of hostnames and/or CIDRs for which the proxy should not be used.   
Show more
