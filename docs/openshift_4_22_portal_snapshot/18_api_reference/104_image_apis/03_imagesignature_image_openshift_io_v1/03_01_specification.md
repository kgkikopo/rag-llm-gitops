# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`conditions` |  `array` |  conditions represent the latest available observations of a signature’s current state.   
`conditions[]` |  `object` |  SignatureCondition describes an image signature condition of particular kind at particular probe time.   
`content` |  `string` |  Required: An opaque binary string which is an image’s signature.   
`created` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  If specified, it is the time of signature’s creation.   
`imageIdentity` |  `string` |  A human readable string representing image’s identity. It could be a product name and version, or an image pull spec (e.g. "registry.access.redhat.com/rhel7/rhel:7.2").   
`issuedBy` |  `object` |  SignatureIssuer holds information about an issuer of signing certificate or key.   
`issuedTo` |  `object` |  SignatureSubject holds information about a person or entity who created the signature.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signedClaims` |  `object (string)` |  Contains claims from the signature.   
`type` |  `string` |  Required: Describes a type of stored blob.   
Show more

## 3.1.1. .conditions

Description
     conditions represent the latest available observations of a signature’s current state. 
Type
     `array`

## 3.1.2. .conditions[]

Description
     SignatureCondition describes an image signature condition of particular kind at particular probe time. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastProbeTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition was checked.   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transit from one status to another.   
`message` |  `string` |  Human readable message indicating details about last transition.   
`reason` |  `string` |  (brief) reason for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of signature condition, Complete or Failed.   
Show more

## 3.1.3. .issuedBy

Description
     SignatureIssuer holds information about an issuer of signing certificate or key. 
Type
     `object`

Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
Show more

## 3.1.4. .issuedTo

Description
     SignatureSubject holds information about a person or entity who created the signature. 
Type
     `object`
Required
    

  * `publicKeyID`



Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
`publicKeyID` |  `string` |  If present, it is a human readable key id of public key belonging to the subject used to verify image signature. It should contain at least 64 lowest bits of public key’s fingerprint (e.g. 0x685ebe62bf278440).   
Show more
