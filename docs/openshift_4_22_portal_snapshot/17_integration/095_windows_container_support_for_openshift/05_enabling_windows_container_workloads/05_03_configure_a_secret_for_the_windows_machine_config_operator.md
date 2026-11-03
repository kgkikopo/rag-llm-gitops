# 5.3. Configure a secret for the Windows Machine Config Operator

Before you can use the Windows Machine Config Operator (WMCO), you must create a secret in the same WMCO namespace as your private key. 

This secret is required to allow the WMCO to communicate with the Windows virtual machine (VM). Use a different private key than the one used when installing the cluster. 

**Prerequisites**

  * You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM). 
  * You created a PEM-encoded file containing a private key by using a strong algorithm, such as ECDSA. 

If you created the key pair on a Red Hat Enterprise Linux (RHEL) system, before you can use the public key on a Windows system, make sure the public key is saved using ASCII encoding. For example, the following PowerShell command copies a public key, encoding it for the ASCII character set: 

```shell-session
C:\> echo "ssh-rsa <ssh_pub_key>" | Out-File <ssh_key_path> -Encoding ascii
```


where: 

`<ssh_pub_key>`
     Specifies the SSH public key used to access the cluster. 
`<ssh_key_path>`
     Specifies the path to the SSH public key. 




**Procedure**

  * Define the secret required to access the Windows VMs: 

```shell-session
$ oc create secret generic cloud-private-key --from-file=private-key.pem=${HOME}/.ssh/<key> \
    -n openshift-windows-machine-config-operator
```


You must create the private key in the WMCO namespace, such as `openshift-windows-machine-config-operator`.
