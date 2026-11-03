# 7.8. Manually creating IAM

To install OpenShift Container Platform, the Cloud Credential Operator (CCO) must operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for your cloud provider. 

You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to create the required IBM Cloud® resources. 

**Prerequisites**

  * You have configured the `ccoctl` binary. 
  * You have an existing `install-config.yaml` file. 



**Procedure**

  1. Edit the `install-config.yaml` configuration file so that the file includes the `credentialsMode` parameter set to `Manual`. 

```yaml
apiVersion: v1
baseDomain: cluster1.example.com
credentialsMode: Manual
compute:
- architecture: ppc64le
  hyperthreading: Enabled
```


where: 

`credentialsMode`
     Specifies the CCO credentials mode. Set the value to `Manual`. 

  2. To generate the manifests, run the following command from the directory that includes the installation program: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


  3. From the directory that includes the installation program, set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  4. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command: 

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
     Specifies that only the manifests that your specific cluster configuration requires are included. 
`--install-config`
     Specifies the location of the `install-config.yaml` file. 
`--to`
    

Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it. 

This command creates a YAML file for each `CredentialsRequest` object. 

**Sample`CredentialsRequest` object**

```yaml
  apiVersion: cloudcredential.openshift.io/v1
  kind: CredentialsRequest
  metadata:
    labels:
      controller-tools.k8s.io: "1.0"
    name: openshift-image-registry-ibmcos
    namespace: openshift-cloud-credential-operator
  spec:
    secretRef:
      name: installer-cloud-credentials
      namespace: openshift-image-registry
    providerSpec:
      apiVersion: cloudcredential.openshift.io/v1
      kind: IBMCloudProviderSpec
      policies:
      - attributes:
        - name: serviceName
          value: cloud-object-storage
        roles:
        - crn:v1:bluemix:public:iam::::role:Viewer
        - crn:v1:bluemix:public:iam::::role:Operator
        - crn:v1:bluemix:public:iam::::role:Editor
        - crn:v1:bluemix:public:iam::::serviceRole:Reader
        - crn:v1:bluemix:public:iam::::serviceRole:Writer
      - attributes:
        - name: resourceType
          value: resource-group
        roles:
        - crn:v1:bluemix:public:iam::::role:Viewer
```


  5. Create the service ID for each credential request, assign the policies defined, create an API key, and generate the secret: 

```shell-session
$ ccoctl ibmcloud create-service-id \
  --credentials-requests-dir=<path_to_credential_requests_directory> \
  --name=<cluster_name> \
  --output-dir=<installation_directory> \
  --resource-group-name=<resource_group_name>
```


where: 

`<path_to_credential_requests_directory>`
     Specifies the directory that has the files for the `CredentialsRequest` objects. 
`<cluster_name>`
     Specifies the name of the OpenShift Container Platform cluster. 
`<installation_directory>`
     Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands. This parameter is optional. 
`<resource_group_name>`
    

Specifies the name of the resource group used for scoping the access policies. This parameter is optional. 

Note

If you enabled Technology Preview features by using the `TechPreviewNoUpgrade` feature set for your cluster, you must include the `--enable-tech-preview` parameter in the configuration for the `CredentialsRequest` object. 

If you provided a wrong resource group name, the installation fails during the bootstrap phase. To find the correct resource group name, run the following command: 

```shell-session
$ grep resourceGroup <installation_directory>/manifests/cluster-infrastructure-02-config.yml
```


**Verification**

  * Check that the appropriate secrets exist in the `manifests` directory of your cluster.
