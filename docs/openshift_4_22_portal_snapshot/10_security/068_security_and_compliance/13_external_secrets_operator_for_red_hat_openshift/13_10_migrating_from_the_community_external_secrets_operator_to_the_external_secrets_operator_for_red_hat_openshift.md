# 13.10. Migrating from the community External Secrets Operator to the External Secrets Operator for Red Hat OpenShift

You can migrate from the community version of the External Secrets Operator. Migrating to External Secrets Operator for Red Hat OpenShift provides you with an officially supported product giving you access to enterprise-grade support. It also provides you with seamless integration from installation to upgrades. 

The following migration versions have been fully tested. 

Upstream version| Installation method| Downstream version  
---|---|---  
0.11.0  |  OLM  |  v1.0.0 GA   
0.19.0  |  Helm  |  v1.0.0 GA   
Show more

Note

The migration does not support rollbacks. 

Note

External Secrets Operator for Red Hat OpenShift is based on the upstream version 0.19.0. Do not try to migrate from a higher version of the External Secrets Operator. 

## 13.10.1. Deleting the community External Secrets Operator

Delete the configuration resource for the community Operator so that the legacy application is fully removed. This action prevents conflicts before installing the External Secrets Operator for Red Hat OpenShift. 

**Prerequisites**

  * You must be logged in as a user with the `cluster-admin` role. 
  * You must have the `oc` command-line tool installed and configured. 



**Procedure**

  1. Find your community Operator’s `namespace` by running the following command: 

```shell-session
$ oc get operatorconfigs.operator.external-secrets.io -A
```


The following is an example of finding the `namespace`: 

```shell-session
NAMESPACE             NAME        AGE
external-secrets      cluster     9m18s
```


  2. Delete the `operatorconfig` custom resrouce (CR) by running the following command: 

```shell-session
$ oc delete operatorconfig <config_name> -n <operator_namespace>
```


**Verification**

  1. To verify that the `operatorconfig` CR is deleted, run the following command: 

```shell-session
$ oc get operatorconfig -n <operator_namespace>
```


The command must return `no resource found`. 

  2. To verify that the old webhooks are deleted, run the following commands: 

```shell-session
$ oc get validatingwebhookconfigurations | grep external-secrets
```


```shell-session
$ oc get mutatingwebhookconfigurations | grep external-secrets
```


The commands must return no results. 




## 13.10.2. Uninstalling the community External Secrets Operator

Uninstall the community External Secrets Operator to prevent conflicts or accidental recreation after you migrate to External Secrets Operator for Red Hat OpenShift. 

You must uninstall the community External Secrets Operator to prevent it from being recreated or conflicting with the new one. The steps to uninstall are different based on how the community External Secrets Operator was installed but the prerequisites are the same for each. 

### 13.10.2.1. Uninstalling a helm installed community External Secrets Operator

Remove the community External Secrets Operator that was installed using Helm. This helps you free up resources and maintain a clean environment for your cluster. 

**Prerequisites**

  * You must be logged in as a user with the `cluster-admin` role. 
  * You must have deleted the `operatorconfig` custom resource (CR). 



**Procedure**

  1. Install the External Secrets Operator for Red Hat OpenShift. The `external-secrets-operator` namespace must be null. 
  2. Delete the External Secrets Operator by running the following command: 

```shell-session
$ oc helm delete <release_name> -n <operator_namespace>
```


Note

Using `helm delete` might delete all Custom Resource Definitions (CRDs) and CRs. It is recommended to install the downstream Operator first if the namespace `external-secrets-operator` is empty. 




### 13.10.2.2. Uninstalling an Operator Lifecycle Manager installed community External Secrets Operator

Remove the community External Secrets Operator that was installed by an Operator Lifecycle Manager (OLM) subscription. This helps you free up resources and maintain a clean environment for your cluster. 

**Prerequisites**

  * You must be logged in as a user with the `cluster-admin` role. 
  * You must have deleted the `operatorconfig` custom resource (CR). 



**Procedure**

  1. Find the subscription name by running the following command: 

```shell-session
$ oc get subscription -n <operator_namespace> | grep external-secrets
```


  2. Delete the subscription by running the following command: 

```shell-session
$ oc delete subscription <subscription_name> -n <operator_namespace>
```


  3. Delete the `ClusterServiceVersion` by running the following command: 

```shell-session
$ oc delete csv <csv_name> -n <operator_namespace>
```


### 13.10.2.3. Uninstalling a raw manifest installed community External Secrets Operator

Remove the community External Secrets Operator that was installed by raw manifests. This helps you free up resources and maintain a clean environment for your cluster. 

**Prerequisites**

  * You must be logged in as a user with the `cluster-admin` role. 
  * You must have deleted the `operatorconfig` CR. 



**Procedure**

  * To remove the communiity External Secrets Operator that was installed by raw manifests, run the following command: 

```shell-session
$ oc delete -f /path/to/your/old/manifests.yaml -n <operator_namespace>
```


## 13.10.3. Installing the External Secrets Operator for Red Hat OpenShift

Install the External Secrets Operator for Red Hat OpenShift after cleaning up the community version. This establishes the officially supported service for managing secrets in your cluster. 

## 13.10.4. Creating the ExternalSecretsConfig Operator

Create the `ExternalSecretsConfig` resource to install and configure the core `external-secrets` component. This setup helps ensure that features like Bitwarden and cert-manager support are correctly enabled. 

**Prerequisites**

  * External Secrets Operator for Red Hat OpenShift is installed. 
  * cert-manager Operator for Red Hat OpenShift is installed. 
  * You have access to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Create an `externalsecretsconfig` file by defining a YAML file with the following content: 

```plaintext
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
metadata:
  labels:
    app.kubernetes.io/name: cluster
  name: cluster
spec:
  appConfig:
    logLevel: 1
  controllerConfig:
    networkPolicies:
      - componentName: ExternalSecretsCoreController
        egress:
          - {}
        name: allow-external-secrets-egress
  plugins: {}
```


  2. Create the `ExternalSecretsConfig` object by running the following command: 

```shell-session
$ oc create -f externalsecretsconfig.yaml
```


**Verification**

Verify that all custom resources (CRs) are present and that the APIs are using `v1` instead of `v1beta1`. There CRs are retained and automatically converted by the new Operator. 

  1. To verify that the `external-secrets` pods are in a `running` state, run the following command: 

```shell-session
$ oc get pods -n external-secret
```


The following is example output that the `external-secrets` pods are in a `running` state. 

```shell-session
NAME                                          READY        STATUS        RESTARTS     AGE
bitwarden-sdk-server-5b4cf48766-w7zp7         1/1          Running       0            5m
external-secrets-5854b85dd5-m6zf9             1/1          Running       0            5m
external-secrets-webhook-5cb85b8fdb-6jtqb     1/1          Running       0            5m
```


  2. To verify that the `SecretStore` CR is present, run the following command: 

```shell-session
$ oc get secretstores.external-secrets.io -A
```


The following is example output from validating that the `SecretStore` is present: 

```shell-session
NAMESPACE               NAME                         AGE         STATUS      CAPABILITIES    READY
external-secrets-1      gcp-store                    18min       Valid       ReadWrite       True
external-secrets-2      aws-secretstore              11min       Valid       ReadWrite       True
external-secrets        bitwarden-secretsmanager     20min       Valid       Readwrite       True
```


  3. To verify that the `ExternalSecret` CR is present, run the following command: 

```shell-session
$ oc get externalsecrets.external-secrets.io -A
```


The following is example output from validating that the `SecretStore` is present: 

```shell-session
NAMESPACE             NAME                    STORE                      REFRESH INTERVAL    STATUS          READY
external-secrets-1    gcp-externalsecret      gcp-store                  1hr                 SecretSynced    True
external-secrets-2    aws-external-secret     aws-secret-store           1hr                 SecretSynced    True
external-secrets      bitwarden               bitwarden-secretsmanager   1hr                 SecretSynced    True
```


  4. To verify that the `SecretStore` is `apiVersion: external-secrets.io/v1`, run the following command: 

```shell-session
$ oc get secretstores.external-secrets.io -n external-secrets-1 gcp-store -o yaml
```


The following is example output that the `SecretStore` is `apiVersion: external-secrets.io/v1`. 

```plaintext
apiVersion: external-secrets.io/v1
kind: SecretStore
metadata:
  creationTimestamp: "2025-10-27T11:38:19Z"
  generation: 1
  name: gcp-store
  namespace: external-secrets-1
  resourceVersion: "104519"
  uid: 7bccb0cc-2557-4f4a-9caa-1577f0108f4b
spec:
.
.
.
status:
  capabilities: ReadWrite
  conditions:
  - lastTransitionTime: "2025-10-27T11:38:19Z"
    message: store validated
    reason: Valid
    status: "True"
    type: Ready
```


  5. To verify that the `ExternalSecret` is `apiVersion: external-secrets.io/v1`, run the following command: 

```shell-session
$ oc get externalsecrets.external-secrets.io -n external-secrets-1 gcp-externalsecret -o yaml
```


The following is example output that the `ExternalSecret` is `apiVersion: external-secrets.io/v1`. 

```plaintext
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  creationTimestamp: "2025-10-27T11:39:03Z"
  generation: 1
  name: gcp-externalsecret
  namespace: external-secrets-1
  resourceVersion: "104532"
  uid: 93a3295a-a3ad-4304-90e1-1328d951e5fb
spec:
.
.
.
status:
  binding:
    name: k8s-secret-gcp
  conditions:
  - lastTransitionTime: "2025-10-27T11:39:03Z"
    message: secret synced
    reason: SecretSynced
    status: "True"
    type: Ready
  refreshTime: "2025-10-27T12:13:15Z"
  syncedResourceVersion: 1-f47fe3c0b255b6dd8047cdffa772587bb829efe7a1cb70febeda2eb2
```
