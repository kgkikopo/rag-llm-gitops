# 4.12. Add the keys for secureboot

To sign kernel modules with Kernel Module Management (KMM) on OpenShift Container Platform, you can add Secure Boot certificate and private key files as Kubernetes secrets. 

For details on how to create these, see [Generating a public and private key pair](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot_managing-monitoring-and-updating-the-kernel#generating-a-public-and-private-key-pair_signing-a-kernel-and-modules-for-secure-boot). 

For details on how to extract the public and private key pair, see [Signing kernel modules with the private key](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot_managing-monitoring-and-updating-the-kernel#signing-kernel-modules-with-the-private-key_signing-a-kernel-and-modules-for-secure-boot). Use steps 1 through 4 to extract the keys into files. 

**Procedure**

  1. Create the `sb_cert.cer` file that contains the certificate and the `sb_cert.priv` file that contains the private key: 

```shell-session
$ openssl req -x509 -new -nodes -utf8 -sha256 -days 36500 -batch -config configuration_file.config -outform DER -out my_signing_key_pub.der -keyout my_signing_key.priv
```


  2. Add the files by using one of the following methods: 

     * Add the files as [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) directly: 

```shell-session
$ oc create secret generic my-signing-key --from-file=key=<my_signing_key.priv>
```


```shell-session
$ oc create secret generic my-signing-key-pub --from-file=cert=<my_signing_key_pub.der>
```


     * Add the files by base64 encoding them: 

```shell-session
$ cat sb_cert.priv | base64 -w 0 > my_signing_key2.base64
```


```shell-session
$ cat sb_cert.cer | base64 -w 0 > my_signing_key_pub.base64
```


  3. Add the encoded text to a YAML file: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-signing-key-pub
  namespace: default
type: Opaque
data:
  cert: <base64_encoded_secureboot_public_key>

---
apiVersion: v1
kind: Secret
metadata:
  name: my-signing-key
  namespace: default
type: Opaque
data:
  key: <base64_encoded_secureboot_private_key>
```


Replace `default` with a valid namespace. 

  4. Apply the YAML file: 

```shell-session
$ oc apply -f <yaml_filename>
```


## 4.12.1. Check the keys

To verify that your secure boot signing keys are configured correctly in OpenShift Container Platform, you can inspect the public certificate and private key secrets with the OpenShift CLI. 

**Procedure**

  1. Check to ensure the public key secret is set correctly: 

```shell-session
$ oc get secret -o yaml <certificate secret name> | awk '/cert/{print $2; exit}' | base64 -d  | openssl x509 -inform der -text
```


This should display a certificate with a Serial Number, Issuer, Subject, and more. 

  2. Check to ensure the private key secret is set correctly: 

```shell-session
$ oc get secret -o yaml <private key secret name> | awk '/key/{print $2; exit}' | base64 -d
```


This should display the key enclosed in the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.
