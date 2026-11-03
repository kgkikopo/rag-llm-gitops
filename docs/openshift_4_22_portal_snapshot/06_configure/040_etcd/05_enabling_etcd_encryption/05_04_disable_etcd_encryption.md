# 5.4. Disable etcd encryption

Disable etcd encryption when you no longer need to encrypt sensitive cluster resources at rest. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Modify the `APIServer` object: 

```shell-session
$ oc edit apiserver
```


  2. Set the `encryption` field type to `identity`: 

```yaml
spec:
  encryption:
    type: identity
```


The `identity` value specifies that no encryption is performed. This is the default value. 

  3. Save the file to apply the changes. 

The decryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of your cluster. 




**Verification**

  * Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully decrypted: 

```shell-session
$ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `DecryptionCompleted` upon successful decryption: 

```shell-session
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
```


If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again. 

  * Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully decrypted: 

```shell-session
$ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `DecryptionCompleted` upon successful decryption: 

```shell-session
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
```


If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again. 

  * Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully decrypted: 

```shell-session
$ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```


The output shows `DecryptionCompleted` upon successful decryption: 

```shell-session
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
```


If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.
