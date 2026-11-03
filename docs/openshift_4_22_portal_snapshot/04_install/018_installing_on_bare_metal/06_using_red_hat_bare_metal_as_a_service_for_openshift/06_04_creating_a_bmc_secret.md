# 6.4. Creating a BMC secret

To deploy a bare-metal host, you must create a secret to access the baseboard management controller (BMC). This means you can remotely provision or manage the physical hardware. 

**Procedure**

  1. Create a BMC secret file by running the following command: 

```shell-session
$ vim bmaas-<name>-bmc-secret.yaml
```


Replace `<name>` with the name of the bare-metal host. 

  2. Edit the secret: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: bmaas-<name>-bmc-secret
  namespace: bmaas
type: Opaque
data:
  username: <base64_of_uid>
  password: <base64_of_pwd>
```


<base64_of_uid>
     Replace `<base64_of_uid>` with the BMC user name as a Base64-encoded string. 
<base64_of_pwd>
     Replace `<base64_of_pwd>` with the BMC password as a Base64-encoded string. 

  3. Apply the BMC secret by running the following command: 

```shell-session
$ oc apply -f bmaas-<name>-bmc-secret.yaml
```


**Additional resources**

  * [About BMC addressing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_bare_metal/installer-provisioned-infrastructure#bmc-addressing_ipi-install-installation-workflow "3.3.15.2. BMC addressing")
