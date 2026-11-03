# 10.2. Rotating cloud provider credentials

Some organizations require the rotation of the cloud provider credentials. To allow the cluster to use the new credentials, you must update the secrets that the Cloud Credential Operator (CCO) uses to manage cloud provider credentials. 

## 10.2.1. Rotate cloud provider credentials manually

If your cloud provider credentials are changed for any reason, you must manually update the secret that the Cloud Credential Operator (CCO) uses to manage cloud provider credentials. 

The process for rotating cloud credentials depends on the mode that the CCO is configured to use. After you rotate credentials for a cluster that is using mint mode, you must manually remove the component credentials that were created by the removed credential. 

**Prerequisites**

  * Your cluster is installed on a platform that supports rotating cloud credentials manually with the CCO mode that you are using: 

    * For mint mode, Amazon Web Services (AWS) and Google Cloud are supported. 
    * For passthrough mode, Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Red Hat OpenStack Platform (RHOSP), and VMware vSphere are supported. 

  * You have changed the credentials that are used to interface with your cloud provider. 
  * The new credentials have sufficient permissions for the mode CCO is configured to use in your cluster. 



**Procedure**

  1. In the **Administrator** perspective of the web console, navigate to **Workloads** **Secrets**. 
  2. In the table on the **Secrets** page, find the root secret for your cloud provider. 

Platform| Secret name  
---|---  
AWS  |  `aws-creds`  
Azure  |  `azure-credentials`  
Google Cloud  |  `gcp-credentials`  
RHOSP  |  `openstack-credentials`  
VMware vSphere  |  `vsphere-creds`  
Show more

  3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Postinstallation_configuration-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) in the same row as the secret and select **Edit Secret**. 
  4. Record the contents of the **Value** field or fields. You can use this information to verify that the value is different after updating the credentials. 
  5. Update the text in the **Value** field or fields with the new authentication information for your cloud provider, and then click **Save**. 
  6. If you are updating the credentials for a vSphere cluster that does not have the vSphere CSI Driver Operator enabled, you must force a rollout of the Kubernetes controller manager to apply the updated credentials. 

Note

If the vSphere CSI Driver Operator is enabled, this step is not required. 

To apply the updated vSphere credentials, log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role and run the following command: 

```shell-session
$ oc patch kubecontrollermanager cluster \
  -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date )"'"}}' \
  --type=merge
```


While the credentials are rolling out, the status of the Kubernetes Controller Manager Operator reports `Progressing=true`. To view the status, run the following command: 

```shell-session
$ oc get co kube-controller-manager
```


  7. If the CCO for your cluster is configured to use mint mode, delete each component secret that is referenced by the individual `CredentialsRequest` objects. 

     1. Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. 
     2. Get the names and namespaces of all referenced component secrets: 

```shell-session
$ oc -n openshift-cloud-credential-operator get CredentialsRequest \
  -o json | jq -r '.items[] | select (.spec.providerSpec.kind=="<provider_spec>") | .spec.secretRef'
```


where `<provider_spec>` is the corresponding value for your cloud provider: 

        * AWS: `AWSProviderSpec`
        * Google Cloud: `GCPProviderSpec`

The following example is partial output for the command on an AWS cluster: 

```plaintext
{
  "name": "ebs-cloud-credentials",
  "namespace": "openshift-cluster-csi-drivers"
}
{
  "name": "cloud-credential-operator-iam-ro-creds",
  "namespace": "openshift-cloud-credential-operator"
}
```


     3. Delete each of the referenced component secrets: 

```shell-session
$ oc delete secret <secret_name> \
```


1

```shell-session
  -n <secret_namespace> 
```


2

```shell-session

```


where: 

`<secret_name>`
     Specifies the name of a secret. 
`<secret_namespace>`
     Specifies the namespace that contains the secret. 

The following example is a command to delete an AWS secret: 

```shell-session
$ oc delete secret ebs-cloud-credentials -n openshift-cluster-csi-drivers
```


You do not need to manually delete the credentials from your provider console. Deleting the referenced component secrets will cause the CCO to delete the existing credentials from the platform and create new ones. 




**Verification**

  1. In the **Administrator** perspective of the web console, navigate to **Workloads** **Secrets**. 
  2. Verify that the contents of the **Value** field or fields have changed. 



**Additional resources**

  * [The Cloud Credential Operator in mint mode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-mode-mint)
  * [The Cloud Credential Operator in passthrough mode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-mode-passthrough)
  * [vSphere CSI Driver Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-vsphere)
  * [Cloud Credential Operator (CCO)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#cloud-credential-operator_cluster-operators-ref)
