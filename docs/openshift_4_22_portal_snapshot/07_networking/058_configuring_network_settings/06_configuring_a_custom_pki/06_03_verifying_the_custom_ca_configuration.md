# 6.3. Verifying the custom CA configuration

To verify that your custom CA certificate has been successfully added to the OpenShift Container Platform cluster-wide trust bundle, you can view the contents of the trusted-ca-bundle `ConfigMap` object and check that your certificate is included. 

**Prerequisites**

  * You have permissions to view `ConfigMap` objects in the openshift-config namespace. 
  * You have the OpenShift CLI (`oc`) installed. 



**Procedure**

  1. Run the following command to view the contents of the cluster-wide CA trust bundle: 

```shell-session
$ oc get configmap trusted-ca-bundle -n openshift-config -o yaml
```


  2. In the YAML output, inspect the `data.ca-bundle.crt` field. This field contains all the trusted certificates for the cluster. 
  3. Verify that the PEM-encoded certificate you added is included in the list of certificates. The output will resemble the following structure: 

```yaml
kind: ConfigMap
metadata:
  name: trusted-ca-bundle
  namespace: openshift-config
data:
  ca-bundle.crt: |
    -----BEGIN CERTIFICATE-----
    <A_SYSTEM_CA_CERTIFICATE>
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    <ANOTHER_SYSTEM_CA_CERTIFICATE>
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    <YOUR_CUSTOM_CA_CERTIFICATE_SHOULD_BE_HERE>
    -----END CERTIFICATE-----
```


If your certificate is present in the output, the cluster now trusts your custom PKI.
