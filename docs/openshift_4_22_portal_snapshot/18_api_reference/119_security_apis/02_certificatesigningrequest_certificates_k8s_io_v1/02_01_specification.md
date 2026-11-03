# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |   
`spec` |  `object` |  CertificateSigningRequestSpec contains the certificate request.   
`status` |  `object` |  CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate.   
Show more

## 2.1.1. .spec

Description
     CertificateSigningRequestSpec contains the certificate request. 
Type
     `object`
Required
    

  * `request`
  * `signerName`



Property| Type| Description  
---|---|---  
`expirationSeconds` |  `integer` |  expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.  The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.  Certificate signers may not honor this field for various reasons:  1\. Old signer that is unaware of the field (such as the in-tree implementations prior to v1.22) 2. Signer whose configured maximum is shorter than the requested duration 3. Signer whose configured minimum is longer than the requested duration  The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.   
`extra` |  `object` |  extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.   
`extra{}` |  `array (string)` |   
`groups` |  `array (string)` |  groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.   
`request` |  `string` |  request contains an x509 certificate signing request encoded in a "CERTIFICATE REQUEST" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded.   
`signerName` |  `string` |  signerName indicates the requested signer, and is a qualified name.  List/watch requests for CertificateSigningRequests can filter on this field using a "spec.signerName=NAME" fieldSelector.  Well-known Kubernetes signers are: 1. "kubernetes.io/kube-apiserver-client": issues client certificates that can be used to authenticate to kube-apiserver. Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the "csrsigning" controller in kube-controller-manager. 2. "kubernetes.io/kube-apiserver-client-kubelet": issues client certificates that kubelets use to authenticate to kube-apiserver. Requests for this signer can be auto-approved by the "csrapproving" controller in kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager. 3. "kubernetes.io/kubelet-serving" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely. Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.  More details are available at <https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers> Custom signerNames can also be specified. The signer defines: 1. Trust distribution: how trust (CA bundles) are distributed. 2. Permitted subjects: and behavior when a disallowed subject is requested. 3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested. 4. Required, permitted, or forbidden key usages / extended key usages. 5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin. 6. Whether or not requests for CA certificates are allowed.   
`uid` |  `string` |  uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.   
`usages` |  `array (string)` |  usages specifies a set of key usages requested in the issued certificate.  Requests for TLS client certificates typically request: "digital signature", "key encipherment", "client auth".  Requests for TLS serving certificates typically request: "key encipherment", "digital signature", "server auth".  Valid values are: "signing", "digital signature", "content commitment", "key encipherment", "key agreement", "data encipherment", "cert sign", "crl sign", "encipher only", "decipher only", "any", "server auth", "client auth", "code signing", "email protection", "s/mime", "ipsec end system", "ipsec tunnel", "ipsec user", "timestamping", "ocsp signing", "microsoft sgc", "netscape sgc"   
`username` |  `string` |  username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.   
Show more

## 2.1.2. .spec.extra

Description
     extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. 
Type
     `object`

## 2.1.3. .status

Description
     CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate. 
Type
     `object`

Property| Type| Description  
---|---|---  
`certificate` |  `string` |  certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.  If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.  Validation requirements: 1. certificate must contain one or more PEM blocks. 2. All PEM blocks must have the "CERTIFICATE" label, contain no headers, and the encoded data must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280. 3. Non-PEM content may appear before or after the "CERTIFICATE" PEM blocks and is unvalidated, to allow for explanatory text as described in section 5.2 of RFC7468.  If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.  The certificate is encoded in PEM format.  When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:  base64( -----BEGIN CERTIFICATE----- …​ -----END CERTIFICATE----- )   
`conditions` |  `array` |  conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed".   
`conditions[]` |  `object` |  CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object   
Show more

## 2.1.4. .status.conditions

Description
     conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed". 
Type
     `array`

## 2.1.5. .status.conditions[]

Description
     CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition’s status is changed, the server defaults this to the current time.   
`lastUpdateTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastUpdateTime is the time of the last update to this condition   
`message` |  `string` |  message contains a human readable message with details about the request state   
`reason` |  `string` |  reason indicates a brief reason for the request state   
`status` |  `string` |  status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown".   
`type` |  `string` |  type of the condition. Known conditions are "Approved", "Denied", and "Failed".  An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.  A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.  A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.  Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.  Only one condition of a given type is allowed.   
Show more
