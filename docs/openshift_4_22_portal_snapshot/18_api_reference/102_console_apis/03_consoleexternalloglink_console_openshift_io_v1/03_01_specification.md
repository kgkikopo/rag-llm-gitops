# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ConsoleExternalLogLinkSpec is the desired log link configuration. The log link will appear on the logs tab of the pod details page.   
Show more

## 3.1.1. .spec

Description
     ConsoleExternalLogLinkSpec is the desired log link configuration. The log link will appear on the logs tab of the pod details page. 
Type
     `object`
Required
    

  * `hrefTemplate`
  * `text`



Property| Type| Description  
---|---|---  
`hrefTemplate` |  `string` |  hrefTemplate is an absolute secure URL (must use https) for the log link including variables to be replaced. Variables are specified in the URL with the format ${variableName}, for instance, ${containerName} and will be replaced with the corresponding values from the resource. Resource is a pod. Supported variables are: - ${resourceName} - name of the resource which containes the logs - ${resourceUID} - UID of the resource which contains the logs - e.g. `11111111-2222-3333-4444-555555555555` \- ${containerName} - name of the resource’s container that contains the logs - ${resourceNamespace} - namespace of the resource that contains the logs - ${resourceNamespaceUID} - namespace UID of the resource that contains the logs - ${podLabels} - JSON representation of labels matching the pod with the logs - e.g. `{"key1":"value1","key2":"value2"}` e.g., [https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels}](https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels})  
`namespaceFilter` |  `string` |  namespaceFilter is a regular expression used to restrict a log link to a matching set of namespaces (e.g., `^openshift-`). The string is converted into a regular expression using the JavaScript RegExp constructor. If not specified, links will be displayed for all the namespaces.   
`text` |  `string` |  text is the display text for the link   
Show more
