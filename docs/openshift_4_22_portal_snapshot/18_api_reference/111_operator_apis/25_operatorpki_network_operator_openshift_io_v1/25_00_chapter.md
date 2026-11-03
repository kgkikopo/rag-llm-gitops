# Chapter 25. OperatorPKI [network.operator.openshift.io/v1]

Description
    

OperatorPKI is a simple certificate authority. It is not intended for external use - rather, it is internal to the network operator. The CNO creates a CA and a certificate signed by that CA. The certificate has both ClientAuth and ServerAuth extended usages enabled. 

```plaintext
More specifically, given an OperatorPKI with <name>, the CNO will manage:
```


  * A Secret called <name>-ca with two data keys: 
  * tls.key - the private key 
  * tls.crt - the CA certificate 
  * A ConfigMap called <name>-ca with a single data key: 
  * cabundle.crt - the CA certificate(s) 
  * A Secret called <name>-cert with two data keys: 
  * tls.key - the private key 
  * tls.crt - the certificate, signed by the CA 



The CA certificate will have a validity of 10 years, rotated after 9. The target certificate will have a validity of 6 months, rotated after 3 

The CA certificate will have a CommonName of "<namespace>_<name>-ca@<timestamp>", where <timestamp> is the last rotation time. 

Type
     `object`
Required
    

  * `spec`

- [25.1. Specification](25_01_specification.md)
- [25.2. API endpoints](25_02_api_endpoints.md)
