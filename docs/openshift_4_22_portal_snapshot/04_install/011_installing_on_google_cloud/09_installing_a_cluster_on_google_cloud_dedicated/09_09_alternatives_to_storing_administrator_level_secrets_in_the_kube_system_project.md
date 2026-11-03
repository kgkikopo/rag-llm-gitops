# 9.9. Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must manage long-term cloud credentials manually. 

## 9.9.1. Manually creating long-term credentials

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
