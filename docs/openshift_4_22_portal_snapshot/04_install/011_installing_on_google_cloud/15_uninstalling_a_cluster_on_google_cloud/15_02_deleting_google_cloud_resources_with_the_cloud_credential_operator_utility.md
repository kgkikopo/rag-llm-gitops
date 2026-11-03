# 15.2. Deleting Google Cloud resources with the Cloud Credential Operator utility

After uninstalling an OpenShift Container Platform cluster that uses short-term credentials managed outside the cluster, you can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to remove the Google Cloud resources that `ccoctl` created during installation. 

**Prerequisites**

  * Extract and prepare the `ccoctl` binary. 
  * Uninstall an OpenShift Container Platform cluster on Google Cloud that uses short-term credentials. 



**Procedure**

  1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  2. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --to=<path_to_directory_for_credentials_requests>
```


where: 

`--included`
     The parameter includes only the manifests that your specific cluster configuration requires. 
`<path_to_directory_for_credentials_requests>`
     Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it. 

  3. Delete the Google Cloud resources that `ccoctl` created by running the following command: 

```shell-session
$ ccoctl gcp delete \
  --name=<name> \
  --project=<gcp_project_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --force-delete-custom-roles
```


where: 

`<name>`
     Matches the name that was originally used to create and tag the cloud resources. 
`<gcp_project_id>`
     The Google Cloud project ID in which to delete cloud resources. 
`force-delete-custom-roles`
     Optional: This parameter deletes the custom roles that the `ccoctl` utility creates during installation. Google Cloud does not permanently delete custom roles immediately. For more information, see Google Cloud documentation about [deleting a custom role](https://cloud.google.com/iam/docs/creating-custom-roles#deleting-custom-role). 




**Verification**

  * To verify that the resources are deleted, query Google Cloud. For more information, refer to Google Cloud documentation.
