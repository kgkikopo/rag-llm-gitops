# 25.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  OperatorPKISpec is the PKI configuration.   
`status` |  `object` |  OperatorPKIStatus is not implemented.   
Show more

## 25.1.1. .spec

Description
     OperatorPKISpec is the PKI configuration. 
Type
     `object`
Required
    

  * `targetCert`



Property| Type| Description  
---|---|---  
`targetCert` |  `object` |  targetCert configures the certificate signed by the CA. It will have both ClientAuth and ServerAuth enabled   
Show more

## 25.1.2. .spec.targetCert

Description
     targetCert configures the certificate signed by the CA. It will have both ClientAuth and ServerAuth enabled 
Type
     `object`
Required
    

  * `commonName`



Property| Type| Description  
---|---|---  
`commonName` |  `string` |  commonName is the value in the certificate’s CN   
Show more

## 25.1.3. .status

Description
     OperatorPKIStatus is not implemented. 
Type
     `object`
