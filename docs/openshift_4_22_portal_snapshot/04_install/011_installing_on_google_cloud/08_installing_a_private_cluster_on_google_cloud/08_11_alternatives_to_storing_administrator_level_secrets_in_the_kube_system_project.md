# 8.11. Alternatives to storing administrator-level secrets in the kube-system project

By default, OpenShift Container Platform stores administrator secrets in the `kube-system` project. 

If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must configure an alternative credential management strategy by using either long-term manual credentials or short-term credentials that are managed outside the cluster. 

  * To manage long-term cloud credentials manually, follow the procedure in "Manually creating long-term credentials". 
  * To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in "Short-term credential configuration for a Google Cloud cluster". 



## 8.11.1. Manually creating long-term credentials

You can put the Cloud Credential Operator (CCO) into manual mode before OpenShift Container Platform installation if the cloud identity and access management (IAM) APIs are not reachable, or if you prefer not to store an administrator-level credential secret in the cluster `kube-system` namespace. 

**Procedure**

  1. Add the following granular permissions to the Google Cloud account that the installation program uses: 

     * compute.machineTypes.list 
     * compute.regions.list 
     * compute.zones.list 
     * dns.changes.create 
     * dns.changes.get 
     * dns.managedZones.create 
     * dns.managedZones.delete 
     * dns.managedZones.get 
     * dns.managedZones.list 
     * dns.networks.bindPrivateDNSZone 
     * dns.resourceRecordSets.create 
     * dns.resourceRecordSets.delete 
     * dns.resourceRecordSets.list 

  2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown: 

**Sample configuration file snippet**

```yaml
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
```


  3. If you have not previously created installation manifest files, do so by running the following command: 

```shell-session
$ openshift-install create manifests --dir <installation_directory>
```


where `<installation_directory>` is the directory in which the installation program creates files. 

  4. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  5. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
```


where: 

`--included`
     Specifies only the manifests that your specific cluster configuration requires. 
`<path_to_directory_with_installation_configuration>`
     Specifies the location of the `install-config.yaml` file. 
`<path_to_directory_for_credentials_requests>`
    

Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it. 

This command creates a YAML file for each `CredentialsRequest` object. 

**Sample`CredentialsRequest` object**

```yaml
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: GCPProviderSpec
    predefinedRoles:
    - roles/storage.admin
    - roles/iam.serviceAccountUser
    skipServiceCheck: true
  ...
```


  6. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object. 

**Sample`CredentialsRequest` object with secrets**

```yaml
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
      ...
  secretRef:
    name: <component_secret>
    namespace: <component_namespace>
  ...
```


**Sample`Secret` object**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: <component_secret>
  namespace: <component_namespace>
data:
  service_account.json: <base64_encoded_gcp_service_account_file>
```


Important

Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state. 




## 8.11.2. Short-term credential configuration for a Google Cloud cluster

To install an OpenShift Container Platform cluster that is configured to use Google Cloud Workload Identity, you must configure the Cloud Credential Operator (CCO) utility and create the required Google Cloud resources for your cluster. 

Cluster Operators use the credentials created by the CCO. The installation program does not use these credentials. 

### 8.11.2.1. Configuring the Cloud Credential Operator utility

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary. 

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment. 

**Prerequisites**

  * You have access to an OpenShift Container Platform account with cluster administrator access. 
  * You have installed the OpenShift CLI (`oc`). 



  * You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses: 

    * The **IAM Workload Identity Pool Admin** role 
    * The following granular permissions: 

      * `compute.projects.get`
      * `iam.googleapis.com/workloadIdentityPoolProviders.create`
      * `iam.googleapis.com/workloadIdentityPoolProviders.get`
      * `iam.googleapis.com/workloadIdentityPools.create`
      * `iam.googleapis.com/workloadIdentityPools.delete`
      * `iam.googleapis.com/workloadIdentityPools.get`
      * `iam.googleapis.com/workloadIdentityPools.undelete`
      * `iam.roles.create`
      * `iam.roles.delete`
      * `iam.roles.list`
      * `iam.roles.undelete`
      * `iam.roles.update`
      * `iam.serviceAccounts.create`
      * `iam.serviceAccounts.delete`
      * `iam.serviceAccounts.getIamPolicy`
      * `iam.serviceAccounts.list`
      * `iam.serviceAccounts.setIamPolicy`
      * `iam.workloadIdentityPoolProviders.get`
      * `iam.workloadIdentityPools.delete`
      * `resourcemanager.projects.get`
      * `resourcemanager.projects.getIamPolicy`
      * `resourcemanager.projects.setIamPolicy`
      * `storage.buckets.create`
      * `storage.buckets.delete`
      * `storage.buckets.get`
      * `storage.buckets.getIamPolicy`
      * `storage.buckets.setIamPolicy`
      * `storage.objects.create`
      * `storage.objects.delete`
      * `storage.objects.list`




**Procedure**

  1. Set a variable for the OpenShift Container Platform release image by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
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


### 8.11.2.2. Creating Google Cloud resources with the Cloud Credential Operator utility

You can use the `ccoctl gcp create-all` command to automate the creation of Google Cloud resources. 

Note

By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory. 

**Prerequisites**

You must have: 

  * Extracted and prepared the `ccoctl` binary. 



**Procedure**

  1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  2. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
```


where: 

`--included`
     Specifies to include only the manifests that your specific cluster configuration requires. 
`<path_to_directory_with_installation_configuration>`
     Specifies the location of the `install-config.yaml` file. 
`<path_to_directory_for_credentials_requests>`
    

Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it. 

Note

This command might take a few moments to run. 

  3. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command: 

```shell-session
$ ccoctl gcp create-all \
  --name=<name> \
  --region=<gcp_region> \
  --project=<gcp_project_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --key-storage-method=<key_storage_method>
```


where: 

`<name>`
     Specifies the user-defined name for all created Google Cloud resources used for tracking. If you plan to install the Google Cloud Filestore Container Storage Interface (CSI) Driver Operator, retain this value. 
`<gcp_region>`
     Specifies the Google Cloud region in which cloud resources will be created. 
`<gcp_project_id>`
     Specifies the Google Cloud project ID in which cloud resources will be created. 
`<path_to_credentials_requests_directory>`
     Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts. 
`<key_storage_method>`
    

Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional. 

Note

If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter. 




**Verification**

  * To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory: 

```shell-session
$ ls <path_to_ccoctl_output_dir>/manifests
```


**Example output**

```plaintext
cluster-authentication-02-config.yaml
openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-gcp-cloud-credentials-credentials.yaml
```


You can verify that the IAM service accounts are created by querying Google Cloud. For more information, refer to Google Cloud documentation on listing IAM service accounts. 




### 8.11.2.3. Restricting service account impersonation to the compute nodes service account

After the Cloud Credential Operator utility (`ccoctl`) creates the resources for the cluster, you can restrict the Google Cloud `iam.serviceAccounts.actAs` permission that the `ccoctl` utility granted to the Machine API controller service account to the compute nodes service account. 

Note

Restricting service account impersonation to the compute nodes service account is optional. If your organization does not require this change, you can continue to "Incorporating the Cloud Credential Operator utility manifests". 

When the `ccoctl` utility assigns custom and Google Cloud predefined roles to OpenShift Container Platform components service accounts, it grants the `iam.serviceAccounts.actAs` permission to the Machine API controller service account at the Google Cloud project level. To reduce the scope of the `iam.serviceAccounts.actAs` permission, you identify the custom role of the Machine API controller service account and replace it with a role that has a more restricted set of permissions. To allow this component to work, you then grant the Machine API controller service account the Service Account User role on the service account of the compute nodes instead. 

**Prerequisites**

  * You have configured an account with the cloud platform that hosts your cluster. 
  * You have used the `ccoctl` utility to create the cloud provider resources for your cluster. 
  * You have access to your `install-config.yaml` file. 
  * You have logged in to the Google Cloud CLI (`gcloud`) as a user with permissions to manage service accounts and roles. 



**Procedure**

  1. Obtain the following values from your `install-config.yaml` file: 

     * The Google Cloud project name. In the YAML file, this is the value of the `platform.gcp.projectID` parameter. 
     * The cluster name. In the YAML file, this is the value of the `metadata.name` parameter. 
     * The service account for the compute nodes. In the YAML file, this is the value of the `compute[0].platform.gcp.serviceAccount` parameter. 

  2. Obtain the service account for the Machine API controller that the `ccoctl` utility created by running the following command: 

```shell-session
$ gcloud iam service-accounts list \
  --filter="displayName=<cluster_name>-openshift-machine-api-gcp" \
  --format='value(email)'
```


where `<cluster_name>` is the value specified for the `metadata.name` parameter in your `install-config.yaml` file. 

  3. Obtain the role ID of the custom role for the Machine API controller service account by running the following command: 

```shell-session
$ gcloud projects get-iam-policy <project_name> \
  --flatten='bindings[].members' \
  --format='table(bindings.role)' \
  --filter="bindings.members:<machine_api_controller_service_account>"
```


where `<machine_api_controller_service_account>` is the Machine API controller service account. 

  4. List the custom role permissions for the Machine API controller service account by running the following command: 

```shell-session
$ gcloud iam roles describe <machine_api_role> \
  --project <project_name>
```


where `<machine_api_role>` is the role ID of the custom role for the Machine API controller service account. 

**Example output**

```plaintext
etag: <etag_value>
includedPermissions:
- compute.acceleratorTypes.get
- compute.acceleratorTypes.list
- compute.disks.create
- compute.disks.createTagBinding
...
- compute.zones.get
- compute.zones.list
- iam.serviceAccounts.actAs
- iam.serviceAccounts.get
- iam.serviceAccounts.list
- resourcemanager.tagValues.get
- resourcemanager.tagValues.list
- serviceusage.quotas.get
- serviceusage.services.get
- serviceusage.services.list
name: projects/<project_name>/roles/<machine_api_role>
stage: GA
title: <project_name>-openshift-machine-api-gcp
```


where `<project_name>` is the Google Cloud project name specified in the `install-config.yaml` file. 

Note

This truncated example output might not match the permissions list for your cluster. 

  5. Create a custom role that includes all of the permissions from your output except for the `iam.serviceAccounts.actAs` permission by running a command similar to the following: 

```shell-session
$ gcloud iam roles create <machine_api_role>_without_actas \
--project=<project_name> \
--title=<machine_api_role>_without_actas \
--description="Required permissions for the Machine API controller without the iam.serviceAccounts.actAs permission" \
--permissions=compute.acceleratorTypes.get,\
compute.acceleratorTypes.list,\
compute.disks.create,\
compute.disks.createTagBinding,\
...
compute.zones.get,\
compute.zones.list,\
iam.serviceAccounts.get,\
iam.serviceAccounts.list,\
resourcemanager.tagValues.get,\
resourcemanager.tagValues.list,\
serviceusage.quotas.get,\
serviceusage.services.get,\
serviceusage.services.list
```


In this example, the new role name is the original custom role name, `<machine_api_role>`, with a `_without_actas` string added to the end. 

Important

This truncated example command might not match the permissions list for your cluster. You must use the list of permissions from the output of the `gcloud iam roles describe <machine_api_role> --project <project_name>` command on your cluster. 

  6. Remove the custom role that includes the `iam.serviceAccounts.actAs` permission from the Machine API controller service account by running the following command: 

```shell-session
$ gcloud projects remove-iam-policy-binding <project_name> \
  --member "serviceAccount:<machine_api_controller_service_account>" \
  --role "projects/<project_name>/roles/<machine_api_role>"
```


where `<machine_api_role>` is the original custom role. 

  7. Grant the custom role that excludes the `iam.serviceAccounts.actAs` permission to the Machine API controller service account by running the following command: 

```shell-session
$ gcloud projects add-iam-policy-binding <project_name> \
  --member "serviceAccount:<machine_api_controller_service_account>" \
  --role "projects/<project_name>/roles/<machine_api_role>_without_actas
```


where `<machine_api_role>_without_actas` is the new custom role. 

  8. Optional: To verify that the Machine API controller service account has the correct role, check the attached role ID by running the following command: 

```shell-session
$ gcloud projects get-iam-policy <project_name> \
  --flatten='bindings[].members' \
  --format='table(bindings.role)' \
  --filter="bindings.members:<machine_api_controller_service_account>"
```


**Example output**

```plaintext
ROLE
projects/<project_name>/roles/<machine_api_role>_without_actas
```


  9. Grant the Machine API controller service account the Service Account User role on the service account of the compute nodes by running the following command: 

```shell-session
$ gcloud iam service-accounts add-iam-policy-binding <compute_nodes_service_account> \
  --member="serviceAccount:<machine_api_controller_service_account>" \
  --role=roles/iam.serviceAccountUser
```


where `<compute_nodes_service_account>` is the service account for your compute nodes. This value is the `compute[0].platform.gcp.serviceAccount` parameter in your `install-config.yaml` file. 




### 8.11.2.4. Incorporating the Cloud Credential Operator utility manifests

To implement short-term security credentials managed outside the cluster for individual OpenShift Container Platform components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program. 

**Prerequisites**

  * You have configured an account with the cloud platform that hosts your cluster. 
  * You have configured the Cloud Credential Operator utility (`ccoctl`). 
  * You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility. 



**Procedure**

  1. Add the following granular permissions to the Google Cloud account that the installation program uses: 

     * compute.machineTypes.list 
     * compute.regions.list 
     * compute.zones.list 
     * dns.changes.create 
     * dns.changes.get 
     * dns.managedZones.create 
     * dns.managedZones.delete 
     * dns.managedZones.get 
     * dns.managedZones.list 
     * dns.networks.bindPrivateDNSZone 
     * dns.resourceRecordSets.create 
     * dns.resourceRecordSets.delete 
     * dns.resourceRecordSets.list 

  2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown: 

**Sample configuration file snippet**

```yaml
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
```


  3. If you have not previously created installation manifest files, do so by running the following command: 

```shell-session
$ openshift-install create manifests --dir <installation_directory>
```


where `<installation_directory>` is the directory in which the installation program creates files. 

  4. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command: 

```shell-session
$ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
```


  5. Copy the `tls` directory that contains the private key to the installation directory: 

```shell-session
$ cp -a /<path_to_ccoctl_output_dir>/tls .
```
