# 24.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 24.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`projectRequestMessage` |  `string` |  projectRequestMessage is the string presented to a user if they are unable to request a project via the projectrequest api endpoint   
`projectRequestTemplate` |  `object` |  projectRequestTemplate is the template to use for creating projects in response to projectrequest. This must point to a template in 'openshift-config' namespace. It is optional. If it is not specified, a default template is used.   
Show more

## 24.1.2. .spec.projectRequestTemplate

Description
     projectRequestTemplate is the template to use for creating projects in response to projectrequest. This must point to a template in 'openshift-config' namespace. It is optional. If it is not specified, a default template is used. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced project request template   
Show more

## 24.1.3. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`
