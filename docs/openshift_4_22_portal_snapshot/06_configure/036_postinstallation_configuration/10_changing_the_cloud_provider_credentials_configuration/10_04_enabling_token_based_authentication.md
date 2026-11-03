# 10.4. Enabling token-based authentication

After installing an OpenShift Container Platform cluster on Microsoft Azure or Amazon Web Services (AWS), you can enable Microsoft Entra Workload ID or Security Token Service (STS) to use short-term credentials. 

## 10.4.1. Configuring the Cloud Credential Operator utility

To configure an existing cluster to create and manage cloud credentials from outside of the cluster, extract and prepare the Cloud Credential Operator utility (`ccoctl`) binary. 

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment. 

**Prerequisites**

  * You have access to an OpenShift Container Platform account with cluster administrator access. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Set a variable for the OpenShift Container Platform release image by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(oc get clusterversion -o jsonpath={..desired.image})
```


  2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
```


Note

Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool. 

  3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
```


For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid: 

     * `rhel8`: Specify this value for hosts that use RHEL 8. 
     * `rhel9`: Specify this value for hosts that use RHEL 9. 

Note

The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`. 

  4. Change the permissions to make `ccoctl` executable by running the following command: 

```shell-session
$ chmod 775 ccoctl
```


**Verification**

  * To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example: 

```shell-session
$ ./ccoctl
```


**Example output**

```shell-session
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
```


## 10.4.2. Enabling Microsoft Entra Workload ID on an existing cluster

Enable Microsoft Entra Workload ID on an existing Microsoft Azure OpenShift Container Platform cluster. If you did not configure your cluster to use Microsoft Entra Workload ID during installation, you can enable this authentication method post-installation. 

Important

The process to enable Workload ID on an existing cluster is disruptive and takes a significant amount of time. Before proceeding, observe the following considerations: 

  * Read the following steps and ensure that you understand and accept the time requirement. The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour. 
  * During this process, you must refresh all service accounts and restart all pods on the cluster. These actions are disruptive to workloads. To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready. 
  * After starting this process, do not attempt to update the cluster until it is complete. If an update is triggered, the process to enable Workload ID on an existing cluster fails. 



**Prerequisites**

  * You have installed an OpenShift Container Platform cluster on Microsoft Azure. 
  * You have access to the cluster using an account with `cluster-admin` permissions. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have extracted and prepared the Cloud Credential Operator utility (`ccoctl`) binary. 
  * You have access to your Azure account by using the Azure CLI (`az`). 



**Procedure**

  1. Create an output directory for the manifests that the `ccoctl` utility generates. This procedure uses `./output_dir` as an example. 
  2. Extract the service account public signing key for the cluster to the output directory by running the following command: 

```shell-session
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 -d \
  > output_dir/serviceaccount-signer.public
```


This procedure uses a file named `serviceaccount-signer.public` as an example. 

  3. Use the extracted service account public signing key to create an OpenID Connect (OIDC) issuer and Azure blob storage container with OIDC configuration files by running the following command: 

```shell-session
$ ./ccoctl azure create-oidc-issuer \
  --name <azure_infra_name> \
  --output-dir ./output_dir \
  --region <azure_region> \
  --subscription-id <azure_subscription_id> \
  --tenant-id <azure_tenant_id> \
  --public-key-file ./output_dir/serviceaccount-signer.public
```


where: 

`<azure_infra_name>`
     The value of the `name` parameter is used to create an Azure resource group. To use an existing Azure resource group instead of creating a new one, specify the `--oidc-resource-group-name` argument with the existing group name as its value. 
`<azure_region>`
     Specify the region of the existing cluster. 
`<azure_subscription_id>`
     Specify the subscription ID of the existing cluster. 
`--public-key-file`
     Specify the file that contains the service account public signing key for the cluster. 

  4. Verify that the configuration file for the Azure pod identity webhook was created by running the following command: 

```shell-session
$ ll ./output_dir/manifests
```


**Example output**

```plaintext
total 8
-rw-------. 1 cloud-user cloud-user 193 May 22 02:29 azure-ad-pod-identity-webhook-config.yaml
-rw-------. 1 cloud-user cloud-user 165 May 22 02:29 cluster-authentication-02-config.yaml
```


The file `azure-ad-pod-identity-webhook-config.yaml` contains the Azure pod identity webhook configuration. 

  5. Set an `OIDC_ISSUER_URL` variable with the OIDC issuer URL from the generated manifests in the output directory by running the following command: 

```shell-session
$ OIDC_ISSUER_URL=`awk '/serviceAccountIssuer/ { print $2 }' ./output_dir/manifests/cluster-authentication-02-config.yaml`
```


  6. Update the `spec.serviceAccountIssuer` parameter of the cluster `authentication` configuration by running the following command: 

```shell-session
$ oc patch authentication cluster \
  --type=merge \
  -p "{\"spec\":{\"serviceAccountIssuer\":\"${OIDC_ISSUER_URL}\"}}"
```


  7. Monitor the configuration update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  8. Restart all of the pods in the cluster by running the following command: 

```shell-session
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
```


Restarting a pod updates the `serviceAccountIssuer` field and refreshes the service account public signing key. 

  9. Monitor the restart and update process by running the following command: 

```shell-session
$ oc adm wait-for-node-reboot nodes --all
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All nodes rebooted
```


  10. Update the Cloud Credential Operator `spec.credentialsMode` parameter to `Manual` by running the following command: 

```shell-session
$ oc patch cloudcredential cluster \
  --type=merge \
  --patch '{"spec":{"credentialsMode":"Manual"}}'
```


  11. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc adm release extract \
  --credentials-requests \
  --included \
  --to <path_to_directory_for_credentials_requests> \
  --registry-config ~/.pull-secret
```


Note

This command might take a few moments to run. 

  12. Set an `AZURE_INSTALL_RG` variable with the Azure resource group name by running the following command: 

```shell-session
$ AZURE_INSTALL_RG=`oc get infrastructure cluster -o jsonpath --template '{ .status.platformStatus.azure.resourceGroupName }'`
```


  13. Use the `ccoctl` utility to create managed identities for all `CredentialsRequest` objects by running the following command: 

Note

The following command does not show all available options. For a complete list of options, including those that might be necessary for your specific use case, run `$ ccoctl azure create-managed-identities --help`. 

```shell-session
$ ccoctl azure create-managed-identities \
  --name <azure_infra_name> \
  --output-dir ./output_dir \
  --region <azure_region> \
  --subscription-id <azure_subscription_id> \
  --credentials-requests-dir <path_to_directory_for_credentials_requests> \
  --issuer-url "${OIDC_ISSUER_URL}" \
  --dnszone-resource-group-name <azure_dns_zone_resourcegroup_name> \
  --installation-resource-group-name "${AZURE_INSTALL_RG}" \
  --network-resource-group-name <azure_resource_group> \
  --preserve-existing-roles
```


where: 

`<azure_dns_zone_resourcegroup_name>`
     Specify the name of the resource group that contains the DNS zone. 
`<azure_resource_group>`
     Optional: Specify the virtual network resource group if it is different from the cluster resource group. 
`--preserve-existing-roles`
     Optional: Specify this flag to ensure that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates. 

  14. Apply the Azure pod identity webhook configuration for Workload ID by running the following command: 

```shell-session
$ oc apply -f ./output_dir/manifests/azure-ad-pod-identity-webhook-config.yaml
```


  15. Apply the secrets generated by the `ccoctl` utility by running the following command: 

```shell-session
$ find ./output_dir/manifests -iname "openshift*yaml" -print0 | xargs -I {} -0 -t oc replace -f {}
```


This process might take several minutes. 

  16. Restart all of the pods in the cluster by running the following command: 

```shell-session
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
```


Restarting a pod updates the `serviceAccountIssuer` field and refreshes the service account public signing key. 

  17. Monitor the restart and update process by running the following command: 

```shell-session
$ oc adm wait-for-node-reboot nodes --all
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All nodes rebooted
```


  18. Monitor the configuration update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  19. Optional: Remove the Azure root credentials secret by running the following command: 

```shell-session
$ oc delete secret -n kube-system azure-credentials
```


## 10.4.3. Enabling AWS Security Token Service (STS) on an existing cluster

Enable AWS Security Token Service (STS) on an existing OpenShift Container Platform cluster if you did not configure this authentication method during installation. 

Important

The process to enable STS on an existing cluster is disruptive and takes a significant amount of time. Before proceeding, observe the following considerations: 

  * Read the following steps and ensure that you understand and accept the time requirement. The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour. 
  * During this process, you must refresh all service accounts and restart all pods on the cluster. These actions are disruptive to workloads. To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready. 
  * Do not update the cluster until this process is complete. 



**Prerequisites**

  * You have installed an OpenShift Container Platform cluster on AWS. 
  * You have access to the cluster using an account with `cluster-admin` permissions. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have extracted and prepared the Cloud Credential Operator utility (`ccoctl`) binary. 
  * You have access to your AWS account by using the AWS CLI (aws). 



**Procedure**

  1. Create an output directory for `ccoctl` generated manifests. 

```shell-session
$ mkdir ./output_dir
```


  2. Create the AWS Identity and Access Management (IAM) OpenID Connect (OIDC) provider. 

     1. Extract the service account public signing key for the cluster by running the following command: 

```shell-session
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 -d \
  > output_dir/serviceaccount-signer.public
```


This procedure uses a file named `serviceaccount-signer.public` as an example. 

     2. Create the AWS IAM identity provider and S3 bucket by running the following command: 

```shell-session
$ ./ccoctl aws create-identity-provider \
  --output-dir output_dir \
  --name <name_you_choose> \
  --region us-east-2 \
  --public-key-file output_dir/serviceaccount-signer.public
```


where: 

`--output-dir`
     Specify the output directory you created earlier. 
`--name`
     Specify a globally unique name. This name functions as a prefix for AWS resources created by this command. 
`--region`
     Specify the AWS region of the cluster. 
`--public-key-file`
     Specify the relative path to the `serviceaccount-signer.public` file you created earlier. 

     3. Save or note the Amazon Resource Name (ARN) for the IAM identity provider. You can find this information in the final line of the output of the previous command. 

  3. Update the cluster authentication configuration. 

     1. Extract the OIDC issuer URL and update the authentication configuration of the cluster by running the following commands: 

```shell-session
$ OIDC_ISSUER_URL=`awk '/serviceAccountIssuer/ { print $2 }' output_dir/manifests/cluster-authentication-02-config.yaml`
$ oc patch authentication cluster --type=merge -p "{\"spec\":{\"serviceAccountIssuer\":\"${OIDC_ISSUER_URL}\"}}"
```


     2. Monitor the configuration update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  4. Restart pods to apply the issuer update. 

     1. Restart all of the pods in the cluster by running the following command: 

```shell-session
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
```


Restarting a pod updates the `serviceAccountIssuer` field and refreshes the service account public signing key. 

     2. Monitor the restart and update process by running the following command: 

```shell-session
$ oc adm wait-for-node-reboot nodes --all
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All nodes rebooted
```


  5. Update the Cloud Credential Operator `spec.credentialsMode` parameter to `Manual` by running the following command: 

```shell-session
$ oc patch cloudcredential cluster \
  --type=merge \
  --patch '{"spec":{"credentialsMode":"Manual"}}'
```


  6. Extract `CredentialsRequests` objects. 

     1. Create a `CLUSTER_VERSION` environment variable by running the following command: 

```shell-session
$ CLUSTER_VERSION=$(oc get clusterversion version -o json | jq -r '.status.desired.version')
```


     2. Create a `CLUSTER_IMAGE` environment variable by running the following command: 

```shell-session
$ CLUSTER_IMAGE=$(oc get clusterversion version -o json | jq -r ".status.history[] | select(.version == \"${CLUSTER_VERSION}\") | .image")
```


     3. Extract `CredentialsRequests` objects from the release image by running the following command: 

```shell-session
$ oc adm release extract \
  --credentials-requests \
  --cloud=aws \
  --from ${CLUSTER_IMAGE} \
  --to output_dir/cred-reqs
```


  7. Create AWS IAM roles and apply secrets. 

     1. Create an IAM role for each `CredentialsRequests` object by running the following command: 

```shell-session
$ ./ccoctl aws create-iam-roles \
  --output-dir ./output_dir/ \
  --name <name_you_choose> \
  --identity-provider-arn <identity_provider_arn> \
  --region us-east-2 \
  --credentials-requests-dir ./output_dir/cred-reqs/ \
  --permissions-boundary-arn=<policy_arn>
```


where: 

`--output-dir`
     Specify the output directory you created earlier. 
`--name`
     Specify a globally unique name. This name functions as a prefix for AWS resources created by this command. 
`--identity-provider-arn`
     Specify the ARN for the IAM identity provider. 
`--region`
     Specify the AWS region of the cluster. 
`--credentials-requests-dir`
     Specify the relative path to the folder where you extracted the `CredentialsRequest` files with the `oc adm release extract` command. 
`--permissions-boundary-arn`
     Optional: Specify the Amazon Resource Name (ARN) of the AWS IAM policy to use as the permissions boundary for the IAM roles created by the `ccoctl` utility. 

     2. Apply the generated secrets by running the following command: 

```shell-session
$ find ./output_dir/manifests -iname "openshift*yaml" -print0 | xargs -I {} -0 -t oc replace -f {}
```


  8. Finish the configuration process by restarting the cluster. 

     1. Restart all of the pods in the cluster by running the following command: 

```shell-session
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
```


     2. Monitor the restart and update process by running the following command: 

```shell-session
$ oc adm wait-for-node-reboot nodes --all
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All nodes rebooted
```


     3. Monitor the configuration update progress by running the following command: 

```shell-session
$ oc adm wait-for-stable-cluster
```


This process might take 15 minutes or longer. The following output indicates that the process is complete: 

```plaintext
All clusteroperators are stable
```


  9. Optional: Remove the AWS root credentials secret by running the following command: 

```shell-session
$ oc delete secret -n kube-system aws-creds
```


**Additional resources**

  * [Microsoft Entra Workload ID](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-short-term-creds-azure_cco-short-term-creds)
  * [Configuring an Azure cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-with-short-term-creds_installing-azure-customizations)
  * [AWS Security Token Service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#cco-short-term-creds-aws_cco-short-term-creds)
  * [Configuring an AWS cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-with-short-term-creds_installing-aws-customizations)



## 10.4.4. Verifying that a cluster uses short-term credentials

You can verify that a cluster uses short-term security credentials for individual components by checking the Cloud Credential Operator (CCO) configuration and other values in the cluster. 

**Prerequisites**

  * You deployed an OpenShift Container Platform cluster using the Cloud Credential Operator utility (`ccoctl`) to implement short-term credentials. 
  * You installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  * Verify that the CCO is configured to operate in manual mode by running the following command: 

```shell-session
$ oc get cloudcredentials cluster \
  -o=jsonpath={.spec.credentialsMode}
```


The following output confirms that the CCO is operating in manual mode: 

**Example output**

```plaintext
Manual
```


  * Verify that the cluster does not have `root` credentials by running the following command: 

```shell-session
$ oc get secrets \
  -n kube-system <secret_name>
```


where `<secret_name>` is the name of the root secret for your cloud provider. 

Platform| Secret name  
---|---  
Amazon Web Services (AWS)  |  `aws-creds`  
Microsoft Azure  |  `azure-credentials`  
Google Cloud  |  `gcp-credentials`  
Show more

An error confirms that the root secret is not present on the cluster. 

**Example output for an AWS cluster**

```plaintext
Error from server (NotFound): secrets "aws-creds" not found
```


  * Verify that the components are using short-term security credentials for individual components by running the following command: 

```shell-session
$ oc get authentication cluster \
  -o jsonpath \
  --template='{ .spec.serviceAccountIssuer }'
```


This command displays the value of the `.spec.serviceAccountIssuer` parameter in the cluster `Authentication` object. An output of a URL that is associated with your cloud provider indicates that the cluster is using manual mode with short-term credentials that are created and managed from outside of the cluster. 

  * Azure clusters: Verify that the components are assuming the Azure client ID that is specified in the secret manifests by running the following command: 

```shell-session
$ oc get secrets \
  -n openshift-image-registry installer-cloud-credentials \
  -o jsonpath='{.data}'
```


An output that contains the `azure_client_id` and `azure_federated_token_file` fields confirms that the components are assuming the Azure client ID. 

  * Azure clusters: Verify that the pod identity webhook is running by running the following command: 

```shell-session
$ oc get pods \
  -n openshift-cloud-credential-operator
```


**Example output**

```plaintext
NAME                                         READY   STATUS    RESTARTS   AGE
cloud-credential-operator-59cf744f78-r8pbq   2/2     Running   2          71m
pod-identity-webhook-548f977b4c-859lz        1/1     Running   1          70m
```
