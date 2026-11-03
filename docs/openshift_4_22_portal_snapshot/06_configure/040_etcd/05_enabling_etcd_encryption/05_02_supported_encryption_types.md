# 5.2. Supported encryption types

OpenShift Container Platform supports AES-CBC and AES-GCM encryption types to protect etcd data at rest. 

The following encryption types are supported for encrypting etcd data in OpenShift Container Platform: 

AES-CBC
     Uses AES-CBC with PKCS#7 padding and a 32-byte key to perform the encryption. 
AES-GCM
     Uses AES-GCM with a random nonce and a 32-byte key to perform the encryption. 

The etcd encryption keys are rotated every 7 days. Up to 10 historical encryption keys are preserved after rotation to help decrypt older backups and provide an extra layer of data recovery safety.
