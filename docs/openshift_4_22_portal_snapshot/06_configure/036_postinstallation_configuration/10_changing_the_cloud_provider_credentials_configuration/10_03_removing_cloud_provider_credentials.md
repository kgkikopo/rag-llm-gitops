# 10.3. Removing cloud provider credentials

After installing OpenShift Container Platform, some organizations require the removal of the cloud provider credentials that were used during the initial installation. 

To allow the cluster to use the new credentials, you must update the secrets that the Cloud Credential Operator (CCO) uses to manage cloud provider credentials. 

## 10.3.1. Removing cloud provider credentials

You can remove administrator-level cloud provider credentials from a cluster that uses the Cloud Credential Operator in mint mode to reduce the risk of credential exposure after installation. 

For clusters that use the Cloud Credential Operator (CCO) in mint mode, the administrator-level credential is stored in the `kube-system` namespace. The CCO uses the `admin` credential to process the `CredentialsRequest` objects in the cluster and create users for components with limited permissions. 

After installing an OpenShift Container Platform cluster with the CCO in mint mode, you can remove the administrator-level credential secret from the `kube-system` namespace in the cluster. The CCO only requires the administrator-level credential during changes that require reconciling new or modified `CredentialsRequest` custom resources, such as minor cluster version updates. 

Note

Before performing a minor version cluster update (for example, updating from OpenShift Container Platform 4.21 to 4.22), you must reinstate the credential secret with the administrator-level credential. If the credential is not present, the update might be blocked. 

**Prerequisites**

  * Your cluster is installed on a platform that supports removing cloud credentials from the CCO. Supported platforms are AWS and Google Cloud. 



**Procedure**

  1. In the **Administrator** perspective of the web console, navigate to **Workloads** **Secrets**. 
  2. In the table on the **Secrets** page, find the root secret for your cloud provider. 

Platform| Secret name  
---|---  
AWS  |  `aws-creds`  
Google Cloud  |  `gcp-credentials`  
Show more

  3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Postinstallation_configuration-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) in the same row as the secret and select **Delete Secret**. 



**Additional resources**

  * [The Cloud Credential Operator in mint mode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-mode-mint)
  * [Cloud Credential Operator (CCO)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#cloud-credential-operator_cluster-operators-ref)
