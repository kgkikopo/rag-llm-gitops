# 5.1. Token authentication

## 5.1.1. Token authentication for Operators on cloud providers

Many cloud providers can enable authentication by using account tokens that provide short-term, limited-privilege security credentials. 

OpenShift Container Platform includes the Cloud Credential Operator (CCO) to manage cloud provider credentials as custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with any specific permissions required. 

Previously, on clusters where the CCO is in _manual mode_ , Operators managed by Operator Lifecycle Manager (OLM) often provided detailed instructions in the OperatorHub for how users could manually provision any required cloud credentials. 

Starting in OpenShift Container Platform 4.14, the CCO can detect when it is running on clusters enabled to use short-term credentials on certain cloud providers. It can then semi-automate provisioning certain credentials, provided that the Operator author has enabled their Operator to support the updated CCO. 

**Additional resources**

  * [About the Cloud Credential Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#about-cloud-credential-operator)
  * [CCO-based workflow for OLM-managed Operators with AWS STS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/developing-operators#osdk-cco-aws-sts "5.1.2. CCO-based workflow for OLM-managed Operators with AWS STS")
  * [CCO-based workflow for OLM-managed Operators with Microsoft Entra Workload ID](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/developing-operators#osdk-cco-azure "5.1.3. CCO-based workflow for OLM-managed Operators with Microsoft Entra Workload ID")
  * [CCO-based workflow for OLM-managed Operators with GCP Workload Identity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/developing-operators#osdk-cco-gcp "5.1.4. CCO-based workflow for OLM-managed Operators with GCP Workload Identity")



## 5.1.2. CCO-based workflow for OLM-managed Operators with AWS STS

When an OpenShift Container Platform cluster running on AWS is in Security Token Service (STS) mode, it means the cluster is utilizing features of AWS and OpenShift Container Platform to use IAM roles at an application level. STS enables applications to provide a JSON Web Token (JWT) that can assume an IAM role. 

The JWT includes an Amazon Resource Name (ARN) for the `sts:AssumeRoleWithWebIdentity` IAM action to allow temporarily-granted permission for the service account. The JWT contains the signing keys for the `ProjectedServiceAccountToken` that AWS IAM can validate. The service account token itself, which is signed, is used as the JWT required for assuming the AWS role. 

The Cloud Credential Operator (CCO) is a cluster Operator installed by default in OpenShift Container Platform clusters running on cloud providers. For the purposes of STS, the CCO provides the following functions: 

  * Detects when it is running on an STS-enabled cluster 
  * Checks the `CredentialsRequest` object for the presence of fields that provide the required information for granting Operators access to AWS resources 



The CCO performs this detection even when in manual mode. When properly configured, the CCO projects a `Secret` object with the required access information into the Operator namespace. 

Starting in OpenShift Container Platform 4.14, the CCO can semi-automate this task through an expanded use of `CredentialsRequest` objects, which can request the creation of `Secrets` that contain the information required for STS workflows. Users can provide a role ARN when installing the Operator from either the web console or CLI. 

Note

Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update. 

As an Operator author preparing an Operator for use alongside the updated CCO in OpenShift Container Platform 4.14 or later, you should instruct users and add code to handle the divergence from earlier CCO versions, in addition to handling STS token authentication (if your Operator is not already STS-enabled). The recommended method is to provide a `CredentialsRequest` object with the correctly filled STS fields and let the CCO create the `Secret` for you. 

Important

If you plan to support OpenShift Container Platform clusters earlier than version 4.14, consider providing users with instructions on how to manually create a secret with the STS-enabling information by using the CCO utility (`ccoctl`). Earlier CCO versions are unaware of STS mode on the cluster and cannot create secrets for you. 

Your code should check for secrets that never appear and warn users to follow the fallback instructions you have provided. For more information, see the "Alternative method" subsection. 

**Additional resources**

  * [OLM-managed Operator support for authentication with AWS STS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-short-term-creds-aws-olm_cco-short-term-creds)
  * [Installing from OperatorHub using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-installing-from-software-catalog-using-web-console_olm-adding-operators-to-a-cluster "4.1.2. Install from the software catalog by using the web console")
  * [Installing from OperatorHub using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-installing-operator-from-software-catalog-using-cli_olm-adding-operators-to-a-cluster "4.1.3. Install from the software catalog by using the CLI")



### 5.1.2.1. Enable Operators to support CCO-based workflows with AWS STS

As an Operator author designing your project to run on Operator Lifecycle Manager (OLM), you can enable your Operator to authenticate against AWS on STS-enabled OpenShift Container Platform clusters by customizing your project to support the Cloud Credential Operator (CCO). 

With this method, the Operator is responsible for and requires RBAC permissions for creating the `CredentialsRequest` object and reading the resulting `Secret` object. 

Note

By default, pods related to the Operator deployment mount a `serviceAccountToken` volume so that the service account token can be referenced in the resulting `Secret` object. 

**Prerequisites**

  * OpenShift Container Platform 4.14 or later 
  * Cluster in STS mode 
  * OLM-based Operator project 



**Procedure**

  1. Update your Operator project’s `ClusterServiceVersion` (CSV) object: 

     1. Ensure your Operator has RBAC permission to create `CredentialsRequests` objects: 

**Example`clusterPermissions` list**

```yaml
# ...
install:
  spec:
    clusterPermissions:
    - rules:
      - apiGroups:
        - "cloudcredential.openshift.io"
        resources:
        - credentialsrequests
        verbs:
        - create
        - delete
        - get
        - list
        - patch
        - update
        - watch
```


     2. Add the following annotation to claim support for this method of CCO-based workflow with AWS STS: 

```yaml
# ...
metadata:
 annotations:
   features.operators.openshift.io/token-auth-aws: "true"
```


  2. Update your Operator project code: 

     1. Get the role ARN from the environment variable set on the pod by the `Subscription` object. For example: 

```plaintext
// Get ENV var
roleARN := os.Getenv("ROLEARN")
setupLog.Info("getting role ARN", "role ARN = ", roleARN)
webIdentityTokenPath := "/var/run/secrets/openshift/serviceaccount/token"
```


     2. Ensure you have a `CredentialsRequest` object ready to be patched and applied. For example: 

**Example`CredentialsRequest` object creation**

```plaintext
import (
   minterv1 "github.com/openshift/cloud-credential-operator/pkg/apis/cloudcredential/v1"
   corev1 "k8s.io/api/core/v1"
   metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

var in = minterv1.AWSProviderSpec{
   StatementEntries: []minterv1.StatementEntry{
      {
         Action: []string{
            "s3:*",
         },
         Effect:   "Allow",
         Resource: "arn:aws:s3:*:*:*",
      },
   },
	STSIAMRoleARN: "<role_arn>",
}

var codec = minterv1.Codec
var ProviderSpec, _ = codec.EncodeProviderSpec(in.DeepCopyObject())

const (
   name      = "<credential_request_name>"
   namespace = "<namespace_name>"
)

var CredentialsRequestTemplate = &minterv1.CredentialsRequest{
   ObjectMeta: metav1.ObjectMeta{
       Name:      name,
       Namespace: "openshift-cloud-credential-operator",
   },
   Spec: minterv1.CredentialsRequestSpec{
      ProviderSpec: ProviderSpec,
      SecretRef: corev1.ObjectReference{
         Name:      "<secret_name>",
         Namespace: namespace,
      },
      ServiceAccountNames: []string{
         "<service_account_name>",
      },
      CloudTokenPath:   "",
   },
}
```


Alternatively, if you are starting from a `CredentialsRequest` object in YAML form (for example, as part of your Operator project code), you can handle it differently: 

**Example`CredentialsRequest` object creation in YAML form**

```plaintext
// CredentialsRequest is a struct that represents a request for credentials
type CredentialsRequest struct {
  APIVersion string `yaml:"apiVersion"`
  Kind       string `yaml:"kind"`
  Metadata   struct {
     Name      string `yaml:"name"`
     Namespace string `yaml:"namespace"`
  } `yaml:"metadata"`
  Spec struct {
     SecretRef struct {
        Name      string `yaml:"name"`
        Namespace string `yaml:"namespace"`
     } `yaml:"secretRef"`
     ProviderSpec struct {
        APIVersion     string `yaml:"apiVersion"`
        Kind           string `yaml:"kind"`
        StatementEntries []struct {
           Effect   string   `yaml:"effect"`
           Action   []string `yaml:"action"`
           Resource string   `yaml:"resource"`
        } `yaml:"statementEntries"`
        STSIAMRoleARN   string `yaml:"stsIAMRoleARN"`
     } `yaml:"providerSpec"`

     // added new field
      CloudTokenPath   string `yaml:"cloudTokenPath"`
  } `yaml:"spec"`
}

// ConsumeCredsRequestAddingTokenInfo is a function that takes a YAML filename and two strings as arguments
// It unmarshals the YAML file to a CredentialsRequest object and adds the token information.
func ConsumeCredsRequestAddingTokenInfo(fileName, tokenString, tokenPath string) (*CredentialsRequest, error) {
  // open a file containing YAML form of a CredentialsRequest
  file, err := os.Open(fileName)
  if err != nil {
     return nil, err
  }
  defer file.Close()

  // create a new CredentialsRequest object
  cr := &CredentialsRequest{}

  // decode the yaml file to the object
  decoder := yaml.NewDecoder(file)
  err = decoder.Decode(cr)
  if err != nil {
     return nil, err
  }

  // assign the string to the existing field in the object
  cr.Spec.CloudTokenPath = tokenPath

  // return the modified object
  return cr, nil
}
```


Note

Adding a `CredentialsRequest` object to the Operator bundle is not currently supported. 

     3. Add the role ARN and web identity token path to the credentials request and apply it during Operator initialization: 

**Example applying`CredentialsRequest` object during Operator initialization**

```plaintext
// apply CredentialsRequest on install
credReq := credreq.CredentialsRequestTemplate
credReq.Spec.CloudTokenPath = webIdentityTokenPath

c := mgr.GetClient()
if err := c.Create(context.TODO(), credReq); err != nil {
   if !errors.IsAlreadyExists(err) {
      setupLog.Error(err, "unable to create CredRequest")
      os.Exit(1)
   }
}
```


     4. Ensure your Operator can wait for a `Secret` object to show up from the CCO, as shown in the following example, which is called along with the other items you are reconciling in your Operator: 

**Example wait for`Secret` object**

```plaintext
// WaitForSecret is a function that takes a Kubernetes client, a namespace, and a v1 "k8s.io/api/core/v1" name as arguments
// It waits until the secret object with the given name exists in the given namespace
// It returns the secret object or an error if the timeout is exceeded
func WaitForSecret(client kubernetes.Interface, namespace, name string) (*v1.Secret, error) {
  // set a timeout of 10 minutes
  timeout := time.After(10 * time.Minute)

  // set a polling interval of 10 seconds
  ticker := time.NewTicker(10 * time.Second)

  // loop until the timeout or the secret is found
  for {
     select {
     case <-timeout:
        // timeout is exceeded, return an error
        return nil, fmt.Errorf("timed out waiting for secret %s in namespace %s", name, namespace)
           // add to this error with a pointer to instructions for following a manual path to a Secret that will work on STS
     case <-ticker.C:
        // polling interval is reached, try to get the secret
        secret, err := client.CoreV1().Secrets(namespace).Get(context.Background(), name, metav1.GetOptions{})
        if err != nil {
           if errors.IsNotFound(err) {
              // secret does not exist yet, continue waiting
              continue
           } else {
              // some other error occurred, return it
              return nil, err
           }
        } else {
           // secret is found, return it
           return secret, nil
        }
     }
  }
}
```


The `timeout` value is based on an estimate of how fast the CCO might detect an added `CredentialsRequest` object and generate a `Secret` object. You might consider lowering the time or creating custom feedback for cluster administrators that could be wondering why the Operator is not yet accessing the cloud resources. 

     5. Set up the AWS configuration by reading the secret created by the CCO from the credentials request and creating the AWS config file containing the data from that secret: 

**Example AWS configuration creation**

```plaintext
func SharedCredentialsFileFromSecret(secret *corev1.Secret) (string, error) {
   var data []byte
   switch {
   case len(secret.Data["credentials"]) > 0:
       data = secret.Data["credentials"]
   default:
       return "", errors.New("invalid secret for aws credentials")
   }


   f, err := ioutil.TempFile("", "aws-shared-credentials")
   if err != nil {
       return "", errors.Wrap(err, "failed to create file for shared credentials")
   }
   defer f.Close()
   if _, err := f.Write(data); err != nil {
       return "", errors.Wrapf(err, "failed to write credentials to %s", f.Name())
   }
   return f.Name(), nil
}
```


Important

The secret is assumed to exist, but your Operator code should wait and retry when using this secret to give time to the CCO to create the secret. 

Additionally, the wait period should eventually time out and warn users that the OpenShift Container Platform cluster version, and therefore the CCO, might be an earlier version that does not support the `CredentialsRequest` object workflow with STS detection. In such cases, instruct users that they must add a secret by using another method. 

     6. Configure the AWS SDK session, for example: 

**Example AWS SDK session configuration**

```plaintext
sharedCredentialsFile, err := SharedCredentialsFileFromSecret(secret)
if err != nil {
   // handle error
}
options := session.Options{
   SharedConfigState: session.SharedConfigEnable,
   SharedConfigFiles: []string{sharedCredentialsFile},
}
```


### 5.1.2.2. Role specification

To install an Operator that uses AWS Security Token Service (STS), you must specify the IAM role that the Operator requires, ideally as a script that an administrator can run. 

The following example shows a script that creates the required AWS IAM role and attaches the trust policy: 

**Example role creation script**

```bash
#!/bin/bash
set -x

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
OIDC_PROVIDER=$(oc get authentication cluster -ojson | jq -r .spec.serviceAccountIssuer | sed -e "s/^https:\/\///")
NAMESPACE=my-namespace
SERVICE_ACCOUNT_NAME="my-service-account"
POLICY_ARN_STRINGS="arn:aws:iam::aws:policy/AmazonS3FullAccess"


read -r -d '' TRUST_RELATIONSHIP <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Effect": "Allow",
     "Principal": {
       "Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_PROVIDER}"
     },
     "Action": "sts:AssumeRoleWithWebIdentity",
     "Condition": {
       "StringEquals": {
         "${OIDC_PROVIDER}:sub": "system:serviceaccount:${NAMESPACE}:${SERVICE_ACCOUNT_NAME}"
       }
     }
   }
 ]
}
EOF

echo "${TRUST_RELATIONSHIP}" > trust.json

aws iam create-role --role-name "$SERVICE_ACCOUNT_NAME" --assume-role-policy-document file://trust.json --description "role for demo"

while IFS= read -r POLICY_ARN; do
   echo -n "Attaching $POLICY_ARN ... "
   aws iam attach-role-policy \
       --role-name "$SERVICE_ACCOUNT_NAME" \
       --policy-arn "${POLICY_ARN}"
   echo "ok."
done <<< "$POLICY_ARN_STRINGS"
```


### 5.1.2.3. Troubleshoot authentication failures

If authentication was not successful, ensure you can assume the role with web identity by using the token provided to the Operator. 

**Procedure**

  1. Extract the token from the pod: 

```shell-session
$ oc exec operator-pod -n <namespace_name> \
    -- cat /var/run/secrets/openshift/serviceaccount/token
```


  2. Extract the role ARN from the pod: 

```shell-session
$ oc exec operator-pod -n <namespace_name> \
    -- cat /<path>/<to>/<secret_name>
```


Do not use root for the path. 

  3. Try assuming the role with the web identity token: 

```shell-session
$ aws sts assume-role-with-web-identity \
    --role-arn $ROLEARN \
    --role-session-name <session_name> \
    --web-identity-token $TOKEN
```


### 5.1.2.4. Troubleshoot secrets not mounting correctly

To avoid credentials file mount failures on non-root pods, mount the secret to a writable location and enable the shared credentials file option in the AWS SDK. 

### 5.1.2.5. Alternative method

As an alternative method for Operator authors, you can indicate that the user is responsible for creating the `CredentialsRequest` object for the Cloud Credential Operator (CCO) before installing the Operator. 

The Operator instructions must indicate the following to users: 

  * Provide a YAML version of a `CredentialsRequest` object, either by providing the YAML inline in the instructions or pointing users to a download location 
  * Instruct the user to create the `CredentialsRequest` object 



In OpenShift Container Platform 4.14 and later, after the `CredentialsRequest` object appears on the cluster with the appropriate STS information added, the Operator can then read the CCO-generated `Secret` or mount it, having defined the mount in the cluster service version (CSV). 

For earlier versions of OpenShift Container Platform, the Operator instructions must also indicate the following to users: 

  * Use the CCO utility (`ccoctl`) to generate the `Secret` YAML object from the `CredentialsRequest` object 
  * Apply the `Secret` object to the cluster in the appropriate namespace 



The Operator still must be able to consume the resulting secret to communicate with cloud APIs. Because in this case the secret is created by the user before the Operator is installed, the Operator can do either of the following: 

  * Define an explicit mount in the `Deployment` object within the CSV 
  * Programmatically read the `Secret` object from the API server, as shown in the recommended "Enabling Operators to support CCO-based workflows with AWS STS" method 



## 5.1.3. CCO-based workflow for OLM-managed Operators with Microsoft Entra Workload ID

When an OpenShift Container Platform cluster running on Azure is in **Workload Identity / Federated Identity** mode, it means the cluster is utilizing features of Azure and OpenShift Container Platform to apply _user-assigned managed identities_ or _app registrations_ in Microsoft Entra Workload ID at an application level. 

The Cloud Credential Operator (CCO) is a cluster Operator installed by default in OpenShift Container Platform clusters running on cloud providers. Starting in OpenShift Container Platform 4.14.8, the CCO supports workflows for OLM-managed Operators with Workload ID. 

For the purposes of Workload ID, the CCO provides the following functions: 

  * Detects when it is running on an Workload ID-enabled cluster 
  * Checks the `CredentialsRequest` object for the presence of fields that provide the required information for granting Operators access to Azure resources 



The CCO can semi-automate this process through an expanded use of `CredentialsRequest` objects, which can request the creation of `Secrets` that contain the information required for Workload ID workflows. 

Note

Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update. 

As an Operator author preparing an Operator for use alongside the updated CCO in OpenShift Container Platform 4.14 and later, you should instruct users and add code to handle the divergence from earlier CCO versions, in addition to handling Workload ID token authentication (if your Operator is not already enabled). The recommended method is to provide a `CredentialsRequest` object with the correctly filled Workload ID fields and let the CCO create the `Secret` object for you. 

Important

If you plan to support OpenShift Container Platform clusters earlier than version 4.14, consider providing users with instructions on how to manually create a secret with the Workload ID-enabling information by using the CCO utility (`ccoctl`). Earlier CCO versions are unaware of Workload ID mode on the cluster and cannot create secrets for you. 

Your code should check for secrets that never appear and warn users to follow the fallback instructions you have provided. 

Authentication with Workload ID requires the following information: 

  * `azure_client_id`
  * `azure_tenant_id`
  * `azure_region`
  * `azure_subscription_id`
  * `azure_federated_token_file`



The **Install Operator** page in the web console allows cluster administrators to provide this information at installation time. This information is then propagated to the `Subscription` object as environment variables on the Operator pod. 

**Additional resources**

  * [OLM-managed Operator support for authentication with Microsoft Entra Workload ID](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-short-term-creds-azure-olm_cco-short-term-creds)
  * [Installing from OperatorHub using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-installing-from-software-catalog-using-web-console_olm-adding-operators-to-a-cluster "4.1.2. Install from the software catalog by using the web console")
  * [Installing from OperatorHub using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-installing-operator-from-software-catalog-using-cli_olm-adding-operators-to-a-cluster "4.1.3. Install from the software catalog by using the CLI")



### 5.1.3.1. Enabling Operators to support CCO-based workflows with Microsoft Entra Workload ID

As an Operator author designing your project to run on Operator Lifecycle Manager (OLM), you can enable your Operator to authenticate against Microsoft Entra Workload ID-enabled OpenShift Container Platform clusters by customizing your project to support the Cloud Credential Operator (CCO). 

With this method, the Operator is responsible for and requires RBAC permissions for creating the `CredentialsRequest` object and reading the resulting `Secret` object. 

Note

By default, pods related to the Operator deployment mount a `serviceAccountToken` volume so that the service account token can be referenced in the resulting `Secret` object. 

**Prerequisites**

  * OpenShift Container Platform 4.14 or later 
  * Cluster in Workload ID mode 
  * OLM-based Operator project 



**Procedure**

  1. Update your Operator project’s `ClusterServiceVersion` (CSV) object: 

     1. Ensure your Operator has RBAC permission to create `CredentialsRequests` objects: 

**Example`clusterPermissions` list**

```yaml
# ...
install:
  spec:
    clusterPermissions:
    - rules:
      - apiGroups:
        - "cloudcredential.openshift.io"
        resources:
        - credentialsrequests
        verbs:
        - create
        - delete
        - get
        - list
        - patch
        - update
        - watch
```


     2. Add the following annotation to claim support for this method of CCO-based workflow with Workload ID: 

```yaml
# ...
metadata:
 annotations:
   features.operators.openshift.io/token-auth-azure: "true"
```


  2. Update your Operator project code: 

     1. Get the client ID, tenant ID, and subscription ID from the environment variables set on the pod by the `Subscription` object. For example: 

```plaintext
// Get ENV var
clientID := os.Getenv("CLIENTID")
tenantID := os.Getenv("TENANTID")
subscriptionID := os.Getenv("SUBSCRIPTIONID")
azureFederatedTokenFile := "/var/run/secrets/openshift/serviceaccount/token"
```


     2. Ensure you have a `CredentialsRequest` object ready to be patched and applied. 

Note

Adding a `CredentialsRequest` object to the Operator bundle is not currently supported. 

     3. Add the Azure credentials information and web identity token path to the credentials request and apply it during Operator initialization: 

**Example applying`CredentialsRequest` object during Operator initialization**

```plaintext
// apply CredentialsRequest on install
credReqTemplate.Spec.AzureProviderSpec.AzureClientID = clientID
credReqTemplate.Spec.AzureProviderSpec.AzureTenantID = tenantID
credReqTemplate.Spec.AzureProviderSpec.AzureRegion = "centralus"
credReqTemplate.Spec.AzureProviderSpec.AzureSubscriptionID = subscriptionID
credReqTemplate.CloudTokenPath = azureFederatedTokenFile

c := mgr.GetClient()
if err := c.Create(context.TODO(), credReq); err != nil {
    if !errors.IsAlreadyExists(err) {
        setupLog.Error(err, "unable to create CredRequest")
        os.Exit(1)
    }
}
```


     4. Ensure your Operator can wait for a `Secret` object to show up from the CCO, as shown in the following example, which is called along with the other items you are reconciling in your Operator: 

**Example wait for`Secret` object**

```plaintext
// WaitForSecret is a function that takes a Kubernetes client, a namespace, and a v1 "k8s.io/api/core/v1" name as arguments
// It waits until the secret object with the given name exists in the given namespace
// It returns the secret object or an error if the timeout is exceeded
func WaitForSecret(client kubernetes.Interface, namespace, name string) (*v1.Secret, error) {
  // set a timeout of 10 minutes
  timeout := time.After(10 * time.Minute)

  // set a polling interval of 10 seconds
  ticker := time.NewTicker(10 * time.Second)

  // loop until the timeout or the secret is found
  for {
     select {
     case <-timeout:
        // timeout is exceeded, return an error
        return nil, fmt.Errorf("timed out waiting for secret %s in namespace %s", name, namespace)
           // add to this error with a pointer to instructions for following a manual path to a Secret that will work on STS
     case <-ticker.C:
        // polling interval is reached, try to get the secret
        secret, err := client.CoreV1().Secrets(namespace).Get(context.Background(), name, metav1.GetOptions{})
        if err != nil {
           if errors.IsNotFound(err) {
              // secret does not exist yet, continue waiting
              continue
           } else {
              // some other error occurred, return it
              return nil, err
           }
        } else {
           // secret is found, return it
           return secret, nil
        }
     }
  }
}
```


The `timeout` value is based on an estimate of how fast the CCO might detect an added `CredentialsRequest` object and generate a `Secret` object. You might consider lowering the time or creating custom feedback for cluster administrators that could be wondering why the Operator is not yet accessing the cloud resources. 

     5. Read the secret created by the CCO from the `CredentialsRequest` object to authenticate with Azure and receive the necessary credentials. 




## 5.1.4. CCO-based workflow for OLM-managed Operators with GCP Workload Identity

When an OpenShift Container Platform cluster running on Google Cloud is in **GCP Workload Identity / Federated Identity** mode, it means the cluster is utilizing features of Google Cloud and OpenShift Container Platform to apply permissions in GCP Workload Identity at an application level. 

The Cloud Credential Operator (CCO) is a cluster Operator installed by default in OpenShift Container Platform clusters running on cloud providers. Starting in OpenShift Container Platform 4.17, the CCO supports workflows for OLM-managed Operators with GCP Workload Identity. 

For the purposes of GCP Workload Identity, the CCO provides the following functions: 

  * Detects when it is running on an GCP Workload Identity-enabled cluster 
  * Checks the `CredentialsRequest` object for the presence of fields that provide the required information for granting Operators access to Google Cloud resources 



The CCO can semi-automate this process through an expanded use of `CredentialsRequest` objects, which can request the creation of `Secrets` that contain the information required for GCP Workload Identity workflows. 

Note

Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update. 

As an Operator author preparing an Operator for use alongside the updated CCO in OpenShift Container Platform 4.17 and later, you should instruct users and add code to handle the divergence from earlier CCO versions, in addition to handling GCP Workload Identity token authentication (if your Operator is not already enabled). The recommended method is to provide a `CredentialsRequest` object with the correctly filled GCP Workload Identity fields and let the CCO create the `Secret` object for you. 

Important

If you plan to support OpenShift Container Platform clusters earlier than version 4.17, consider providing users with instructions on how to manually create a secret with the GCP Workload Identity-enabling information by using the CCO utility (`ccoctl`). Earlier CCO versions are unaware of GCP Workload Identity mode on the cluster and cannot create secrets for you. 

Your code should check for secrets that never appear and warn users to follow the fallback instructions you have provided. 

To authenticate with Google Cloud using short-lived tokens via Google Cloud Platform Workload Identity, Operators must provide the following information: 

`AUDIENCE`
    

Created in Google Cloud by the administrator when they set up GCP Workload Identity, the `AUDIENCE` value must be a preformatted URL in the following format: 

```plaintext
//iam.googleapis.com/projects/<project_number>/locations/global/workloadIdentityPools/<pool_id>/providers/<provider_id>
```


`SERVICE_ACCOUNT_EMAIL`
    

The `SERVICE_ACCOUNT_EMAIL` value is a Google Cloud service account email that is impersonated during Operator operation, for example: 

```plaintext
<service_account_name>@<project_id>.iam.gserviceaccount.com
```


The **Install Operator** page in the web console allows cluster administrators to provide this information at installation time. This information is then propagated to the `Subscription` object as environment variables on the Operator pod. 

**Additional resources**

  * [OLM-managed Operator support for authentication with GCP Workload Identity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-short-term-creds-gcp-olm_cco-short-term-creds)
  * [Installing from OperatorHub using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-installing-from-software-catalog-using-web-console_olm-adding-operators-to-a-cluster "4.1.2. Install from the software catalog by using the web console")
  * [Installing from OperatorHub using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-installing-operator-from-software-catalog-using-cli_olm-adding-operators-to-a-cluster "4.1.3. Install from the software catalog by using the CLI")



### 5.1.4.1. Enabling Operators to support CCO-based workflows with GCP Workload Identity

As an Operator author designing your project to run on Operator Lifecycle Manager (OLM), you can enable your Operator to authenticate against Google Cloud Platform Workload Identity on OpenShift Container Platform clusters by customizing your project to support the Cloud Credential Operator (CCO). 

With this method, the Operator is responsible for and requires RBAC permissions for creating the `CredentialsRequest` object and reading the resulting `Secret` object. 

Note

By default, pods related to the Operator deployment mount a `serviceAccountToken` volume so that the service account token can be referenced in the resulting `Secret` object. 

**Prerequisites**

  * OpenShift Container Platform 4.17 or later 
  * Cluster in **GCP Workload Identity / Federated Identity** mode 
  * OLM-based Operator project 



**Procedure**

  1. Update your Operator project’s `ClusterServiceVersion` (CSV) object: 

     1. Ensure Operator deployment in the CSV has the following `volumeMounts` and `volumes` fields so that the Operator can assume the role with web identity: 

**Example`volumeMounts` and `volumes` fields**

```yaml
# ...
      volumeMounts:

      - name: bound-sa-token
        mountPath: /var/run/secrets/openshift/serviceaccount
        readOnly: true
      volumes:
         # This service account token can be used to provide identity outside the cluster.
         - name: bound-sa-token
           projected:
             sources:
             - serviceAccountToken:
               path: token
               audience: openshift
```


     2. Ensure your Operator has RBAC permission to create `CredentialsRequests` objects: 

**Example`clusterPermissions` list**

```yaml
# ...
install:
  spec:
    clusterPermissions:
    - rules:
      - apiGroups:
        - "cloudcredential.openshift.io"
        resources:
        - credentialsrequests
        verbs:
        - create
        - delete
        - get
        - list
        - patch
        - update
        - watch
```


     3. Add the following annotation to claim support for this method of CCO-based workflow with GCP Workload Identity: 

```yaml
# ...
metadata:
 annotations:
   features.operators.openshift.io/token-auth-gcp: "true"
```


  2. Update your Operator project code: 

     1. Get the `audience` and the `serviceAccountEmail` values from the environment variables set on the pod by the subscription config: 

```plaintext
 // Get ENV var
   audience := os.Getenv("AUDIENCE")
   serviceAccountEmail := os.Getenv("SERVICE_ACCOUNT_EMAIL")
   gcpIdentityTokenFile := "/var/run/secrets/openshift/serviceaccount/token"
```


     2. Ensure you have a `CredentialsRequest` object ready to be patched and applied. 

Note

Adding a `CredentialsRequest` object to the Operator bundle is not currently supported. 

     3. Add the GCP Workload Identity variables to the credentials request and apply it during Operator initialization: 

**Example applying`CredentialsRequest` object during Operator initialization**

```plaintext
// apply CredentialsRequest on install
   credReqTemplate.Spec.GCPProviderSpec.Audience = audience
   credReqTemplate.Spec.GCPProviderSpec.ServiceAccountEmail = serviceAccountEmail
   credReqTemplate.CloudTokenPath = gcpIdentityTokenFile


   c := mgr.GetClient()
   if err := c.Create(context.TODO(), credReq); err != nil {
       if !errors.IsAlreadyExists(err) {
           setupLog.Error(err, "unable to create CredRequest")
           os.Exit(1)
       }
   }
```


     4. Ensure your Operator can wait for a `Secret` object to show up from the CCO, as shown in the following example, which is called along with the other items you are reconciling in your Operator: 

**Example wait for`Secret` object**

```plaintext
// WaitForSecret is a function that takes a Kubernetes client, a namespace, and a v1 "k8s.io/api/core/v1" name as arguments
// It waits until the secret object with the given name exists in the given namespace
// It returns the secret object or an error if the timeout is exceeded
func WaitForSecret(client kubernetes.Interface, namespace, name string) (*v1.Secret, error) {
  // set a timeout of 10 minutes
  timeout := time.After(10 * time.Minute)

  // set a polling interval of 10 seconds
  ticker := time.NewTicker(10 * time.Second)

  // loop until the timeout or the secret is found
  for {
     select {
     case <-timeout:
        // timeout is exceeded, return an error
        return nil, fmt.Errorf("timed out waiting for secret %s in namespace %s", name, namespace)
// add to this error with a pointer to instructions for following a manual path to a Secret that will work
     case <-ticker.C:
        // polling interval is reached, try to get the secret
        secret, err := client.CoreV1().Secrets(namespace).Get(context.Background(), name, metav1.GetOptions{})
        if err != nil {
           if errors.IsNotFound(err) {
              // secret does not exist yet, continue waiting
              continue
           } else {
              // some other error occurred, return it
              return nil, err
           }
        } else {
           // secret is found, return it
           return secret, nil
        }
     }
  }
}
```


The `timeout` value is based on an estimate of how fast the CCO might detect an added `CredentialsRequest` object and generate a `Secret` object. You might consider lowering the time or creating custom feedback for cluster administrators that could be wondering why the Operator is not yet accessing the cloud resources. 

     5. Read the `service_account.json` field from the secret and use it to authenticate your Google Cloud client: 

```plaintext
service_account_json := secret.StringData["service_account.json"]
```
