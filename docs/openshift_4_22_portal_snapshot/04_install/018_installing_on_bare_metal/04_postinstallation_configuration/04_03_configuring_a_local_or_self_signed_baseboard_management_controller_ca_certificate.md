# 4.3. Configuring a local or self-signed Baseboard Management Controller CA certificate

You can configure a local or self-signed Baseboard Management Controller (BMC) CA certificate on a cluster that already has a CA certificate, or add one to a cluster that was installed without a CA certificate. 

Providing a local or self-signed CA certificate gives you more control over secure communication with bare metal BMC’s. 

## 4.3.1. Replacing an existing BMC CA certificate

You can replace the BMC CA certificate with your own local or self-signed CA certificate by editing the `bmc-verify-ca` ConfigMap in the `openshift-machine-api` namespace. Providing your own CA certificate gives you control over the secure communications between your cluster and BMC’s. 

**Prerequisites**

  * You have installed a cluster on bare metal. 
  * You configured a CA certificate for BMC communication when you installed the cluster. 
  * You have a local or self-signed CA certificate. 



**Procedure**

  1. Edit the `bmc-verify-ca` ConfigMap by running the following command: 

```shell-session
$ oc edit configmap bmc-verify-ca -n openshift-machine-api
```


  2. Replace the contents of the `verify_ca.crt` stanza with your local or self-signed CA certificate, as in the following example: 

```yaml
apiVersion: v1
data:
  verify_ca.crt: |
    -----BEGIN CERTIFICATE-----
    <self_signed_certificate_contents>
    -----END CERTIFICATE-----
kind: ConfigMap
```


where: 

`<self_signed_certificate_contents>`
     Specifies the contents of your local or self-signed CA certificate. 




## 4.3.2. Installing a new BMC CA certificate

You can install a local or self-signed BMC CA certificate on a cluster which was installed without a BMC CA certificate. Providing your own BMC CA certificate secures the communication between your cluster and BMC’s. 

**Prerequisites**

  * You installed a cluster on bare metal without a BMC CA certificate. 
  * You have a local or self-signed CA certificate. 



**Procedure**

  1. Create a file called `bmc-verify-ca.yaml` using a text editor, with the following contents: 

```yaml
apiVersion: v1
data:
  verify_ca.crt: |
    -----BEGIN CERTIFICATE-----
    <self_signed_certificate_contents>
    -----END CERTIFICATE-----
kind: ConfigMap
metadata:
  name: bmc-verify-ca
  namespace: openshift-machine-api
```


where: 

`<self_signed_certificate_contents>`
     Specifies the contents of your local or self-signed CA certificate. 

  2. Apply the ConfigMap by running the following command: 

```shell-session
$ oc apply -f bmc-verify-ca.yaml
```


  3. Verify that the ConfigMap has been mounted in the Ironic container by running the following command: 

```shell-session
$ oc exec -n openshift-machine-api \
  $(oc get pods -n openshift-machine-api -l app=metal3 -o jsonpath='{.items[0].metadata.name}') \
  -c metal3-ironic -- ls -l /certs/ca/bmc
```


If successful, the command should display the certificate file. 

  4. For each bare metal host in your cluster that you want to secure BMC communications with, follow the procedure titled _Editing a BareMetalHost resource_ and ensure that the `disableCertificateVerification` parameter is set to `false`. 



**Additional resources**

  * [Editing a `BareMetalHost` resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_bare_metal/bare-metal-post-installation-configuration#bmo-editing-a-baremetalhost-resource_bare-metal-postinstallation-configuration "4.10.4. Editing a BareMetalHost resource")
