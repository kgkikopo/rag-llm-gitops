# 3.11. Configuring IAM for Nutanix

Installing the cluster requires that the Cloud Credential Operator (CCO) operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets. 

**Prerequisites**

  * You have configured the `ccoctl` binary. 
  * You have an `install-config.yaml` file. 



**Procedure**

  1. Create a YAML file that contains the credentials data in the following format: 

**Credentials data format**

```yaml
credentials:
- type: basic_auth
  data:
    prismCentral:
      username: <username_for_prism_central>
      password: <password_for_prism_central>
    prismElements:
    - name: <name_of_prism_element>
      username: <username_for_prism_element>
      password: <password_for_prism_element>
```


where: 

`type`
     Specifies the authentication type. Only basic authentication is supported. 
`prismCentral`
     Specifies the Prism Central credentials. 
`prismElements`
     Optional: Specifies the Prism Element credentials. 

  2. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  3. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command: 

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
     Includes only the manifests that your specific cluster configuration requires. 
`<path_to_directory_with_installation_configuration>`
     Specifies the location of the `install-config.yaml` file. 
`<path_to_directory_for_credentials_requests>`
    

Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it. 

**Sample`CredentialsRequest` object**

```yaml
  apiVersion: cloudcredential.openshift.io/v1
  kind: CredentialsRequest
  metadata:
    annotations:
      include.release.openshift.io/self-managed-high-availability: "true"
    labels:
      controller-tools.k8s.io: "1.0"
    name: openshift-machine-api-nutanix
    namespace: openshift-cloud-credential-operator
  spec:
    providerSpec:
      apiVersion: cloudcredential.openshift.io/v1
      kind: NutanixProviderSpec
    secretRef:
      name: nutanix-credentials
      namespace: openshift-machine-api
```


  4. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command: 

```shell-session
$ ccoctl nutanix create-shared-secrets \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --output-dir=<ccoctl_output_dir> \
  --credentials-source-filepath=<path_to_credentials_file>
```


where: 

`<path_to_credentials_requests_directory>`
     Specifies the path to the directory that contains the files for the component `CredentialsRequests` objects. 
`<ccoctl_output_dir>`
     Optional: Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run. 
`<path_to_credentials_file>`
     Optional: Specifies the directory that contains the credentials data YAML file. By default, `ccoctl` expects this file to be in `<home_directory>/.nutanix/credentials`. 

  5. Edit the `install-config.yaml` configuration file so that the `credentialsMode` parameter is set to `Manual`. 

**Example`install-config.yaml` configuration file**

```yaml
apiVersion: v1
baseDomain: cluster1.example.com
credentialsMode: Manual
...
```


Add the `credentialsMode` line to set the parameter to `Manual`. 

  6. Create the installation manifests by running the following command: 

```shell-session
$ openshift-install create manifests --dir <installation_directory>
```


For `<installation_directory>`, specify the path to the directory that contains the `install-config.yaml` file for your cluster. 

  7. Copy the generated credential files to the target manifests directory by running the following command: 

```shell-session
$ cp <ccoctl_output_dir>/manifests/*credentials.yaml ./<installation_directory>/manifests
```


**Verification**

  * Ensure that the appropriate secrets exist in the `manifests` directory. 

```shell-session
$ ls ./<installation_directory>/manifests
```


**Example output**

```plaintext
cluster-config.yaml
cluster-dns-02-config.yml
cluster-infrastructure-02-config.yml
cluster-ingress-02-config.yml
cluster-network-01-crd.yml
cluster-network-02-config.yml
cluster-proxy-01-config.yaml
cluster-scheduler-02-config.yml
cvo-overrides.yaml
kube-cloud-config.yaml
kube-system-configmap-root-ca.yaml
machine-config-server-tls-secret.yaml
openshift-config-secret-pull-secret.yaml
openshift-cloud-controller-manager-nutanix-credentials-credentials.yaml
openshift-machine-api-nutanix-credentials-credentials.yaml
```
