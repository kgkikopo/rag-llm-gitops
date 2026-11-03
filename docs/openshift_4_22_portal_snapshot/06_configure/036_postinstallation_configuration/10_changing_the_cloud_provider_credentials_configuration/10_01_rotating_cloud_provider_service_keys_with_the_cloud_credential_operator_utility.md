# 10.1. Rotating cloud provider service keys with the Cloud Credential Operator utility

Some organizations require the rotation of the service keys that authenticate the cluster. You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to update keys for clusters installed on the following cloud providers: 

  * Amazon Web Services (AWS) with Security Token Service (STS) 
  * Google Cloud with GCP Workload Identity 
  * Microsoft Azure with Workload ID 
  * IBM Cloud 



## 10.1.1. Rotating AWS OIDC bound service account signer keys

You can rotate the bound service account signer key for an OpenShift Container Platform cluster on Amazon Web Services (AWS) that uses the Cloud Credential Operator (CCO) in manual mode with STS. 

To rotate the key, you delete the existing key on your cluster, which causes the Kubernetes API server to create a new key. To reduce authentication failures during this process, you must immediately add the new public key to the existing issuer file. After the cluster is using the new key for authentication, you can remove any remaining keys. 

Important

The process to rotate OIDC bound service account signer keys is disruptive and takes a significant amount of time. Some steps are time-sensitive. Before proceeding, observe the following considerations: 

  * Read the following steps and ensure that you understand and accept the time requirement. The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour. 
  * To reduce the risk of authentication failures, ensure that you understand and prepare for the time-sensitive steps. 
  * During this process, you must refresh all service accounts and restart all pods on the cluster. These actions are disruptive to workloads. To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready. 



**Prerequisites**

  * You have access to the OpenShift CLI (`oc`) as a user with the `cluster-admin` role. 



  * You have created an AWS account for the `ccoctl` utility to use with the following permissions: 

    * `s3:GetObject`
    * `s3:PutObject`
    * `s3:PutObjectTagging`
    * For clusters that store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL, the AWS account that runs the `ccoctl` utility requires the `cloudfront:ListDistributions` permission. 




  * You have configured the `ccoctl` utility. 
  * Your cluster is in a stable state. You can confirm that the cluster is stable by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster --minimum-stable-period=5s
```


**Procedure**

  1. Configure the following environment variables: 

```plaintext
INFRA_ID=$(oc get infrastructures cluster -o jsonpath='{.status.infrastructureName}')
CLUSTER_NAME=${INFRA_ID%-*}
```


where: 

`CLUSTER_NAME`
    

This value should match the name of the cluster that was specified in the `metadata.name` field of the `install-config.yaml` file during installation. 

Note

Your cluster might differ from this example, and the resource names might not be derived identically from the cluster name. Ensure that you specify the correct corresponding resource names for your cluster. 

     * For AWS clusters that store the OIDC configuration in a public S3 bucket, configure the following environment variable: 

```plaintext
AWS_BUCKET=$(oc get authentication cluster -o jsonpath={'.spec.serviceAccountIssuer'} | awk -F'://' '{print$2}' |awk -F'.' '{print$1}')
```


     * For AWS clusters that store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL, complete the following steps: 

       1. Extract the public CloudFront distribution URL by running the following command: 

```shell-session
$ basename $(oc get authentication cluster -o jsonpath={'.spec.serviceAccountIssuer'} )
```


**Example output**

```plaintext
<subdomain>.cloudfront.net
```


where `<subdomain>` is an alphanumeric string. 

       2. Determine the private S3 bucket name by running the following command: 

```shell-session
$ aws cloudfront list-distributions --query "DistributionList.Items[].{DomainName: DomainName, OriginDomainName: Origins.Items[0].DomainName}[?contains(DomainName, '<subdomain>.cloudfront.net')]"
```


**Example output**

```plaintext
[
    {
        "DomainName": "<subdomain>.cloudfront.net",
        "OriginDomainName": "<s3_bucket>.s3.us-east-2.amazonaws.com"
    }
]
```


where `<s3_bucket>` is the private S3 bucket name for your cluster. 

       3. Configure the following environment variable: 

```plaintext
AWS_BUCKET=$<s3_bucket>
```


where `<s3_bucket>` is the private S3 bucket name for your cluster. 

  2. Create a temporary directory to use and assign it an environment variable by running the following command: 

```shell-session
$ TEMPDIR=$(mktemp -d)
```


  3. To cause the Kubernetes API server to create a new bound service account signing key, you delete the next bound service account signing key. 

Important

After you complete this step, the Kubernetes API server starts to roll out a new key. To reduce the risk of authentication failures, complete the remaining steps as quickly as possible. The remaining steps might be disruptive to workloads. 

When you are ready, delete the next bound service account signing key by running the following command: 

```shell-session
$ oc delete secrets/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator
```


  4. Download the public key from the service account signing key secret that the Kubernetes API server created by running the following command: 

```shell-session
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 \
  -d > ${TEMPDIR}/serviceaccount-signer.public
```


  5. Use the public key to create a `keys.json` file by running the following command: 

```shell-session
$ ccoctl aws create-identity-provider \
  --dry-run \
  --output-dir ${TEMPDIR} \
  --public-key-file=${TEMPDIR}/serviceaccount-signer.public \
  --name fake \
  --region us-east-1
```


where: 

`--dry-run`
     The dry run mode outputs files, including the new `keys.json` file, to the disk without making API calls. 
`--public-key-file`
     The path to the public key that you downloaded in the previous step. 
`--name`
     Some parameters do not require real values because the `--dry-run` option does not make any API calls. 
`--region`
     Any valid AWS region, such as `us-east-1`. This value does not need to match the region the cluster is in. 

  6. Rename the `keys.json` file by running the following command: 

```shell-session
$ cp ${TEMPDIR}/<number>-keys.json ${TEMPDIR}/jwks.new.json
```


where `<number>` is a two-digit numerical value that varies depending on your environment. 

  7. Download the existing `keys.json` file from the cloud provider by running the following command: 

```shell-session
$ aws s3api get-object \
  --bucket ${AWS_BUCKET} \
  --key keys.json ${TEMPDIR}/jwks.current.json
```


  8. Combine the two `keys.json` files by running the following command: 

```shell-session
$ jq -s '{ keys: map(.keys[])}' ${TEMPDIR}/jwks.current.json ${TEMPDIR}/jwks.new.json > ${TEMPDIR}/jwks.combined.json
```


  9. To enable authentication for the old and new keys during the rotation, upload the combined `keys.json` file to the cloud provider by running the following command: 

```shell-session
$ aws s3api put-object \
  --bucket ${AWS_BUCKET} \
  --tagging "openshift.io/cloud-credential-operator/${CLUSTER_NAME}=owned" \
  --key keys.json \
  --body ${TEMPDIR}/jwks.combined.json
```


  10. Wait for the Kubernetes API server to update and use the new key. You can monitor the update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  11. To ensure that all pods on the cluster use the new key, you must restart them. 

Important

This step maintains uptime for services that are configured for high availability across multiple nodes, but might cause downtime for any services that are not. 

Restart all of the pods in the cluster by running the following command: 

```shell-session
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
```


  12. Monitor the restart and update process by running the following command: 

```shell-session
$ oc adm wait-for-node-reboot nodes --all
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All nodes rebooted
```


  13. Monitor the update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  14. Replace the combined `keys.json` file with the updated `keys.json` file on the cloud provider by running the following command: 

```shell-session
$ aws s3api put-object \
  --bucket ${AWS_BUCKET} \
  --tagging "openshift.io/cloud-credential-operator/${CLUSTER_NAME}=owned" \
  --key keys.json \
  --body ${TEMPDIR}/jwks.new.json
```


## 10.1.2. Rotating Google Cloud OIDC bound service account signer keys

You can rotate the bound service account signer key for an OpenShift Container Platform cluster on Google Cloud that uses the Cloud Credential Operator (CCO) in manual mode with GCP Workload Identity. 

To rotate the key, you delete the existing key on your cluster, which causes the Kubernetes API server to create a new key. To reduce authentication failures during this process, you must immediately add the new public key to the existing issuer file. After the cluster is using the new key for authentication, you can remove any remaining keys. 

Important

The process to rotate OIDC bound service account signer keys is disruptive and takes a significant amount of time. Some steps are time-sensitive. Before proceeding, observe the following considerations: 

  * Read the following steps and ensure that you understand and accept the time requirement. The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour. 
  * To reduce the risk of authentication failures, ensure that you understand and prepare for the time-sensitive steps. 
  * During this process, you must refresh all service accounts and restart all pods on the cluster. These actions are disruptive to workloads. To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready. 



**Prerequisites**

  * You have access to the OpenShift CLI (`oc`) as a user with the `cluster-admin` role. 



  * You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses: 

    * The **IAM Workload Identity Pool Admin** role 
    * The following granular permissions: 

      * `storage.objects.create`
      * `storage.objects.delete`

  * You have configured the `ccoctl` utility. 
  * Your cluster is in a stable state. You can confirm that the cluster is stable by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster --minimum-stable-period=5s
```


**Procedure**

  1. Configure the following environment variables: 

```plaintext
CURRENT_ISSUER=$(oc get authentication cluster -o jsonpath='{.spec.serviceAccountIssuer}')
GCP_BUCKET=$(echo ${CURRENT_ISSUER} | cut -d "/" -f4)
CLUSTER_NAME=${GCP_BUCKET%-*}
```


Note

Your cluster might differ from this example, and the resource names might not be derived identically from the cluster name. Ensure that you specify the correct corresponding resource names for your cluster. 

  2. Create a temporary directory to use and assign it an environment variable by running the following command: 

```shell-session
$ TEMPDIR=$(mktemp -d)
```


  3. To cause the Kubernetes API server to create a new bound service account signing key, you delete the next bound service account signing key. 

Important

After you complete this step, the Kubernetes API server starts to roll out a new key. To reduce the risk of authentication failures, complete the remaining steps as quickly as possible. The remaining steps might be disruptive to workloads. 

When you are ready, delete the next bound service account signing key by running the following command: 

```shell-session
$ oc delete secrets/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator
```


  4. Download the public key from the service account signing key secret that the Kubernetes API server created by running the following command: 

```shell-session
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 \
  -d > ${TEMPDIR}/serviceaccount-signer.public
```


  5. Use the public key to create a `keys.json` file by running the following command: 

```shell-session
$ ccoctl gcp create-workload-identity-provider \
  --dry-run \
  --output-dir=${TEMPDIR} \
  --public-key-file=${TEMPDIR}/serviceaccount-signer.public \
  --name fake \
  --project fake \
  --workload-identity-pool fake
```


where: 

`--dry-run`
     The dry run mode outputs files, including the new `keys.json` file, to the disk without making API calls. 
`--public-key-file`
     The path to the public key that you downloaded in the previous step. 
`--name`
     Some parameters do not require real values because the `--dry-run` option does not make any API calls. 

  6. Rename the `keys.json` file by running the following command: 

```shell-session
$ cp ${TEMPDIR}/<number>-keys.json ${TEMPDIR}/jwks.new.json
```


where `<number>` is a two-digit numerical value that varies depending on your environment. 

  7. Download the existing `keys.json` file from the cloud provider by running the following command: 

     * For Google Cloud clusters that store OIDC keys in a public bucket, run the following command: 

```shell-session
$ gcloud storage cp gs://${GCP_BUCKET}/keys.json ${TEMPDIR}/jwks.current.json
```


     * For Google Cloud clusters that attach OIDC keys directly to the workload identity pool, run the following command: 

```shell-session
$ gcloud iam workload-identity-pools providers describe \
  --format json \
  --location global \
  --workload-identity-pool ${CLUSTER_NAME} ${CLUSTER_NAME} \
  | jq -r ".oidc.jwksJson" > ${TEMPDIR}/jwks.current.json
```


  8. Combine the two `keys.json` files by running the following command: 

```shell-session
$ jq -s '{ keys: map(.keys[])}' ${TEMPDIR}/jwks.current.json ${TEMPDIR}/jwks.new.json > ${TEMPDIR}/jwks.combined.json
```


  9. To enable authentication for the old and new keys during the rotation, upload the combined `keys.json` file to the cloud provider by running the following command: 

     * For Google Cloud clusters that store OIDC keys in a public bucket, run the following command: 

```shell-session
$ gcloud storage cp ${TEMPDIR}/jwks.combined.json gs://${GCP_BUCKET}/keys.json
```


     * For Google Cloud clusters that attach OIDC keys directly to the workload identity pool, run the following command: 

```shell-session
$ gcloud iam workload-identity-pools providers update-oidc ${CLUSTER_NAME} \
  --location=global \
  --workload-identity-pool=${CLUSTER_NAME} \
  --jwk-json-path=${TEMPDIR}/jwks.combined.json
```


  10. Wait for the Kubernetes API server to update and use the new key. You can monitor the update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  11. To ensure that all pods on the cluster use the new key, you must restart them. 

Important

This step maintains uptime for services that are configured for high availability across multiple nodes, but might cause downtime for any services that are not. 

Restart all of the pods in the cluster by running the following command: 

```shell-session
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
```


  12. Monitor the restart and update process by running the following command: 

```shell-session
$ oc adm wait-for-node-reboot nodes --all
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All nodes rebooted
```


  13. Monitor the update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  14. Replace the combined `keys.json` file with the updated `keys.json` file on the cloud provider by running the following command: 

     * For Google Cloud clusters that store OIDC keys in a public bucket, run the following command: 

```shell-session
$ gcloud storage cp ${TEMPDIR}/jwks.new.json gs://${GCP_BUCKET}/keys.json
```


     * For Google Cloud clusters that attach OIDC keys directly to the workload identity pool, run the following command: 

```shell-session
$ gcloud iam workload-identity-pools providers update-oidc ${CLUSTER_NAME} \
  --location=global \
  --workload-identity-pool=${CLUSTER_NAME} \
  --jwk-json-path=${TEMPDIR}/jwks.new.json
```


## 10.1.3. Rotating Azure OIDC bound service account signer keys

You can rotate the bound service account signer key for an OpenShift Container Platform cluster on Microsoft Azure that uses the Cloud Credential Operator (CCO) in manual mode with Microsoft Entra Workload ID. 

To rotate the key, you delete the existing key on your cluster, which causes the Kubernetes API server to create a new key. To reduce authentication failures during this process, you must immediately add the new public key to the existing issuer file. After the cluster is using the new key for authentication, you can remove any remaining keys. 

Important

The process to rotate OIDC bound service account signer keys is disruptive and takes a significant amount of time. Some steps are time-sensitive. Before proceeding, observe the following considerations: 

  * Read the following steps and ensure that you understand and accept the time requirement. The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour. 
  * To reduce the risk of authentication failures, ensure that you understand and prepare for the time-sensitive steps. 
  * During this process, you must refresh all service accounts and restart all pods on the cluster. These actions are disruptive to workloads. To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready. 



**Prerequisites**

  * You have access to the OpenShift CLI (`oc`) as a user with the `cluster-admin` role. 



  * You have created a global Azure account for the `ccoctl` utility to use with the following permissions: 

    * `Microsoft.Storage/storageAccounts/listkeys/action`
    * `Microsoft.Storage/storageAccounts/read`
    * `Microsoft.Storage/storageAccounts/write`
    * `Microsoft.Storage/storageAccounts/blobServices/containers/read`
    * `Microsoft.Storage/storageAccounts/blobServices/containers/write`




  * You have configured the `ccoctl` utility. 
  * Your cluster is in a stable state. You can confirm that the cluster is stable by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster --minimum-stable-period=5s
```


**Procedure**

  1. Configure the following environment variables: 

```plaintext
CURRENT_ISSUER=$(oc get authentication cluster -o jsonpath='{.spec.serviceAccountIssuer}')
AZURE_STORAGE_ACCOUNT=$(echo ${CURRENT_ISSUER} | cut -d "/" -f3 | cut -d "." -f1)
AZURE_STORAGE_CONTAINER=$(echo ${CURRENT_ISSUER} | cut -d "/" -f4)
```


Note

Your cluster might differ from this example, and the resource names might not be derived identically from the cluster name. Ensure that you specify the correct corresponding resource names for your cluster. 

  2. Create a temporary directory to use and assign it an environment variable by running the following command: 

```shell-session
$ TEMPDIR=$(mktemp -d)
```


  3. To cause the Kubernetes API server to create a new bound service account signing key, you delete the next bound service account signing key. 

Important

After you complete this step, the Kubernetes API server starts to roll out a new key. To reduce the risk of authentication failures, complete the remaining steps as quickly as possible. The remaining steps might be disruptive to workloads. 

When you are ready, delete the next bound service account signing key by running the following command: 

```shell-session
$ oc delete secrets/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator
```


  4. Download the public key from the service account signing key secret that the Kubernetes API server created by running the following command: 

```shell-session
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 \
  -d > ${TEMPDIR}/serviceaccount-signer.public
```


  5. Use the public key to create a `keys.json` file by running the following command: 

```shell-session
$ ccoctl aws create-identity-provider \
  --dry-run \
  --output-dir ${TEMPDIR} \
  --public-key-file=${TEMPDIR}/serviceaccount-signer.public \
  --name fake \
  --region us-east-1
```


where: 

`ccoctl aws`
     The command does not include a `--dry-run` option. To use the `--dry-run` option, you must specify `aws` for an Azure cluster. 
`--dry-run`
     The dry run mode outputs files, including the new `keys.json` file, to the disk without making API calls. 
`--public-key-file`
     The path to the public key that you downloaded in the previous step. 
`--name`
     Some parameters do not require real values because the `--dry-run` option does not make any API calls. 
`--region`
     Any valid AWS region, such as `us-east-1`. This value does not need to match the region the cluster is in. 

  6. Rename the `keys.json` file by running the following command: 

```shell-session
$ cp ${TEMPDIR}/<number>-keys.json ${TEMPDIR}/jwks.new.json
```


where `<number>` is a two-digit numerical value that varies depending on your environment. 

  7. Download the existing `keys.json` file from the cloud provider by running the following command: 

```shell-session
$ az storage blob download \
  --container-name ${AZURE_STORAGE_CONTAINER} \
  --account-name ${AZURE_STORAGE_ACCOUNT} \
  --name 'openid/v1/jwks' \
  -f ${TEMPDIR}/jwks.current.json
```


  8. Combine the two `keys.json` files by running the following command: 

```shell-session
$ jq -s '{ keys: map(.keys[])}' ${TEMPDIR}/jwks.current.json ${TEMPDIR}/jwks.new.json > ${TEMPDIR}/jwks.combined.json
```


  9. To enable authentication for the old and new keys during the rotation, upload the combined `keys.json` file to the cloud provider by running the following command: 

```shell-session
$ az storage blob upload \
  --overwrite \
  --account-name ${AZURE_STORAGE_ACCOUNT} \
  --container-name ${AZURE_STORAGE_CONTAINER} \
  --name 'openid/v1/jwks' \
  -f ${TEMPDIR}/jwks.combined.json
```


  10. Wait for the Kubernetes API server to update and use the new key. You can monitor the update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  11. To ensure that all pods on the cluster use the new key, you must restart them. 

Important

This step maintains uptime for services that are configured for high availability across multiple nodes, but might cause downtime for any services that are not. 

Restart all of the pods in the cluster by running the following command: 

```shell-session
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
```


  12. Monitor the restart and update process by running the following command: 

```shell-session
$ oc adm wait-for-node-reboot nodes --all
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All nodes rebooted
```


  13. Monitor the update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  14. Replace the combined `keys.json` file with the updated `keys.json` file on the cloud provider by running the following command: 

```shell-session
$ az storage blob upload \
  --overwrite \
  --account-name ${AZURE_STORAGE_ACCOUNT} \
  --container-name ${AZURE_STORAGE_CONTAINER} \
  --name 'openid/v1/jwks' \
  -f ${TEMPDIR}/jwks.new.json
```


## 10.1.4. Rotating IBM Cloud credentials

You can rotate API keys for existing IBM Cloud service IDs and update the corresponding cluster secrets to maintain valid cloud provider credentials. 

You can rotate API keys for your existing service IDs and update the corresponding secrets. 

**Prerequisites**

  * You have configured the `ccoctl` utility. 
  * You have existing service IDs in a live OpenShift Container Platform cluster installed. 



**Procedure**

  * Use the `ccoctl` utility to rotate your API keys for the service IDs and update the secrets by running the following command: 

```shell-session
$ ccoctl <provider_name> refresh-keys \
    --kubeconfig <openshift_kubeconfig_file> \
    --credentials-requests-dir <path_to_credential_requests_directory> \
    --name <name>
```


where: 

`<provider_name>`
     The name of the provider. For example: `ibmcloud` or `powervs`. 
`<openshift_kubeconfig_file>`
     The `kubeconfig` file associated with the cluster. For example, `<installation_directory>/auth/kubeconfig`. 
`<path_to_credential_requests_directory>`
     The directory where the credential requests are stored. 
`<name>`
    

The name of the OpenShift Container Platform cluster. 

Note

If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter. 




**Additional resources**

  * [Amazon Web Services (AWS) with Security Token Service (STS)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/changing-cloud-credentials-configuration#rotating-bound-service-keys_key-rotation-aws "10.1.1. Rotating AWS OIDC bound service account signer keys")
  * [Google Cloud with GCP Workload Identity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/changing-cloud-credentials-configuration#rotating-bound-service-keys_key-rotation-gcp "10.1.2. Rotating Google Cloud OIDC bound service account signer keys")
  * [Microsoft Azure with Workload ID](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/changing-cloud-credentials-configuration#rotating-bound-service-keys_key-rotation-azure "10.1.3. Rotating Azure OIDC bound service account signer keys")
  * [IBM Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/changing-cloud-credentials-configuration#refreshing-service-ids-ibm-cloud_changing-cloud-credentials-configuration "10.1.4. Rotating IBM Cloud credentials")
