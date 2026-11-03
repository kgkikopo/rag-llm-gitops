# 6.1. Adding a custom CA during cluster installation

To add a custom Certificate Authority (CA) to your OpenShift Container Platform cluster during initial cluster installation, you can add the CA certificate to your `install-config.yaml` file. Adding the CA certificate during installation ensures that your cluster trusts the CA after installation. 

The following procedure uses the `additionalTrustBundle` parameter. If you are also configuring an egress proxy, you can add this parameter to your `install-config.yaml` file along with your proxy configuration. For more information on the available proxy settings, see the "Configuring the cluster-wide proxy" chapter. 

**Prerequisites**

  * You have access to the `install-config.yaml` file for your cluster installation. 
  * You have your custom CA certificate avalable in PEM-encoded format. 



**Procedure**

  1. Open your `install-config.yaml` file. 
  2. Add the `additionalTrustBundle` parameter with your PEM-encoded CA certificate: 

```yaml
apiVersion: v1
baseDomain: my.domain.com
metadata:
  name: my-cluster
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  <MY_PEM_ENCODED_CA_CERT>
  -----END CERTIFICATE-----
```


where: 

`additionalTrustBundle`
     Specifies the custom CA certificate that you want the cluster to trust. The installation program uses the certificate to generate a `user-ca-bundle` `ConfigMap` object in the `openshift-config` namespace. 

  3. Save the `install-config.yaml` file and continue with your cluster installation.
