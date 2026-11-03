# 9.4. Populating the software catalog from mirrored Operator catalogs

If you mirrored Operator catalogs for use with disconnected clusters, you can populate the software catalog with the Operators from your mirrored catalogs. You can use the generated manifests from the mirroring process to create the required `ImageContentSourcePolicy` and `CatalogSource` objects. 

**Prerequisites**

  * You mirrored Operator catalogs for use with disconnected clusters. 



**Additional resources**

  * [Mirroring Operator catalogs for use with disconnected clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-mirror-catalog_installing-mirroring-installation-images)



## 9.4.1. Creating the ImageContentSourcePolicy object

To make mirrored Operator images available to a disconnected cluster, you can create an `ImageContentSourcePolicy` object that redirects image references to your mirror registry. 

After mirroring Operator catalog content to your mirror registry, create the required `ImageContentSourcePolicy` (ICSP) object. The ICSP object configures nodes to translate between the image references stored in Operator manifests and the mirrored registry. 

**Procedure**

  * On a host with access to the disconnected cluster, create the ICSP by running the following command to specify the `imageContentSourcePolicy.yaml` file in your manifests directory: 

```shell-session
$ oc create -f <path/to/manifests/dir>/imageContentSourcePolicy.yaml
```


where `<path/to/manifests/dir>` is the path to the manifests directory for your mirrored content. 

You can now create a `CatalogSource` object to reference your mirrored index image and Operator content. 




## 9.4.2. Add a catalog source to a cluster

To make Operators from a custom index image available for installation, create a catalog source that adds the catalog content to your cluster. 

Cluster administrators can create a `CatalogSource` object that references an index image. The software catalog uses catalog sources to populate the user interface. 

Tip

Alternatively, you can use the web console to manage catalog sources. From the **Administration** **Cluster Settings** **Configuration** **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources. 

**Prerequisites**

  * You built and pushed an index image to a registry. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Create a `CatalogSource` object that references your index image. If you used the `oc adm catalog mirror` command to mirror your catalog to a target registry, you can use the generated `catalogSource.yaml` file in your manifests directory as a starting point. 

     1. Modify the following to your specifications and save it as a `catalogSource.yaml` file: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: my-operator-catalog
  namespace: openshift-marketplace
spec:
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode>
  image: <registry>/<namespace>/redhat-operator-index:v4.22
  displayName: My Operator Catalog
  publisher: <publisher_name>
  updateStrategy:
    registryPoll:
      interval: 30m
```


where: 

`metadata.name`
     Specifies the value for the `metadata.name` parameter. If you mirrored content to local files before uploading to a registry, remove any backslash (`/`) characters from the `metadata.name` field to avoid an "invalid resource name" error when you create the object. 
`metadata.namespace`
     Specifies the value for the `metadata.namespace` parameter. If you want the catalog source to be available globally to users in all namespaces, specify the `openshift-marketplace` namespace. Otherwise, you can specify a different namespace for the catalog to be scoped and available only for that namespace. 
`spec.grpcPodConfig.securityContextConfig`
    

Specifies the value of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future OpenShift Container Platform release, it is planned that the default value will be `restricted`. 

Note

If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`. 

`spec.image`
     Specifies your index image. If you specify a tag after the image name, for example `:v4.22`, the catalog source pod uses an image pull policy of `Always`, meaning the pod always pulls the image before starting the container. If you specify a digest, for example `@sha256:<id>`, the image pull policy is `IfNotPresent`, meaning the pod pulls the image only if it does not already exist on the node. 
`spec.publisher`
     Specifies your name or an organization name publishing the catalog. 
`spec.updateStrategy.registryPoll`
     Specifies the value for the `spec.updateStrategy.registryPoll` parameter. The catalog sources can automatically check for new versions to keep up to date. 

     2. Use the file to create the `CatalogSource` object: 

```shell-session
$ oc apply -f catalogSource.yaml
```


  2. Verify the following resources are created successfully. 

     1. Check the pods: 

```shell-session
$ oc get pods -n openshift-marketplace
```


The following is example output: 

```shell-session
NAME                                    READY   STATUS    RESTARTS  AGE
my-operator-catalog-6njx6               1/1     Running   0         28s
marketplace-operator-d9f549946-96sgr    1/1     Running   0         26h
```


     2. Check the catalog source: 

```shell-session
$ oc get catalogsource -n openshift-marketplace
```


The following is example output: 

```shell-session
NAME                  DISPLAY               TYPE PUBLISHER  AGE
my-operator-catalog   My Operator Catalog   grpc            5s
```


     3. Check the package manifest: 

```shell-session
$ oc get packagemanifest -n openshift-marketplace
```


The following is example output: 

```shell-session
NAME                          CATALOG               AGE
jaeger-product                My Operator Catalog   93s
```


You can now install the Operators from the **Software Catalog** page on your OpenShift Container Platform web console. 




**Additional resources**

  * [Accessing images for Operators from private registries](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-accessing-images-private-registries_olm-managing-custom-catalogs)
  * [Image template for custom catalog sources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-catalogsource-image-template_olm-understanding-olm)
  * [Image pull policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#image-pull-policy)



## 9.4.3. Install from the software catalog by using the web console

To install and subscribe to an Operator from the software catalog, you can use the OpenShift Container Platform web console. The console guides you through selecting an install mode, namespace, and approval strategy. 

Warning

Failed Operator installations do not automatically remove created permissions. Audit and remove remaining permissions to secure the namespace. 

For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

**Prerequisites**

  * Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 



**Procedure**

  1. Navigate in the web console to the **Ecosystem** **Software Catalog** page. 
  2. Scroll or type a keyword into the **Filter by keyword** box to find the Operator you want. For example, type `jaeger` to find the Jaeger Operator. 

You can also filter options by **Infrastructure Features**. For example, select **Disconnected** if you want to see Operators that work in disconnected environments, also known as restricted network environments. 

  3. Select the Operator to display additional information. 

Note

Choosing a Community Operator warns that Red Hat does not certify Community Operators; you must acknowledge the warning before continuing. 

  4. Read the information about the Operator and click **Install**. 
  5. On the **Install Operator** page, configure your Operator installation: 

     1. If you want to install a specific version of an Operator, select an **Update channel** and **Version** from the lists. You can browse the various versions of an Operator across any channels it might have, view the metadata for that channel and version, and select the exact version you want to install. 

Note

The version selection defaults to the latest version for the channel selected. If the latest version for the channel is selected, the **Automatic** approval strategy is enabled by default. Otherwise, **Manual** approval is required when not installing the latest version for the selected channel. 

Installing an Operator with **Manual** approval causes all Operators installed within the namespace to function with the **Manual** approval strategy and all Operators are updated together. If you want to update Operators independently, install Operators into separate namespaces. 

     2. Confirm the installation mode for the Operator: 

        * **All namespaces on the cluster (default)** installs the Operator in the default `openshift-operators` namespace to watch and be made available to all namespaces in the cluster. This option is not always available. 
        * **A specific namespace on the cluster** allows you to choose a specific, single namespace in which to install the Operator. The Operator will only watch and be made available for use in this single namespace. 

     3. For clusters on cloud providers with token authentication enabled: 

        * If the cluster uses AWS Security Token Service (**STS Mode** in the web console), enter the Amazon Resource Name (ARN) of the AWS IAM role of your service account in the **role ARN** field. To create the role’s ARN, follow the procedure described in [Preparing AWS account](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/tutorials/cloud-experts-deploy-api-data-protection#prepare-aws-account_cloud-experts-deploy-api-data-protection). 
        * If the cluster uses Microsoft Entra Workload ID (**Workload Identity / Federated Identity Mode** in the web console), add the client ID, tenant ID, and subscription ID in the appropriate fields. 
        * If the cluster uses Google Cloud Platform Workload Identity (**GCP Workload Identity / Federated Identity Mode** in the web console), add the project number, pool ID, provider ID, and service account email in the appropriate fields. 

     4. For **Update approval** , select either the **Automatic** or **Manual** approval strategy. 

Important

If the web console shows that the cluster uses AWS STS, Microsoft Entra Workload ID, or GCP Workload Identity, you must set **Update approval** to **Manual**. 

Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update. 

  6. Click **Install** to make the Operator available to the selected namespaces on this OpenShift Container Platform cluster: 

     1. If you selected a **Manual** approval strategy, the upgrade status of the subscription remains **Upgrading** until you review and approve the install plan. 

After approving on the **Install Plan** page, the subscription upgrade status moves to **Up to date**. 

     2. If you selected an **Automatic** approval strategy, the upgrade status should resolve to **Up to date** without intervention. 




**Verification**

  * After the upgrade status of the subscription is **Up to date** , select **Ecosystem** **Installed Operators** to verify that the cluster service version (CSV) of the installed Operator eventually shows up. The **Status** should eventually resolve to **Succeeded** in the relevant namespace. 

Note

For the **All namespaces…​** installation mode, the status resolves to **Succeeded** in the `openshift-operators` namespace, but the status is **Copied** if you check in other namespaces. 

If it does not: 

    * Check the logs in any pods in the `openshift-operators` project (or other relevant namespace if **A specific namespace…​** installation mode was selected) on the **Workloads** **Pods** page that are reporting issues to troubleshoot further. 

  * When the Operator is installed, the metadata indicates which channel and version are installed. 

Note

The **Channel** and **Version** dropdown menus are still available for viewing other version metadata in this catalog context. 




## 9.4.4. Install from the software catalog by using the CLI

To install an Operator from the software catalog without using the web console, you can create or update a `Subscription` object by using the `oc` command in OpenShift Container Platform. 

For `SingleNamespace` install mode, you must also ensure an appropriate Operator group exists in the related namespace. An Operator group, defined by an `OperatorGroup` object, selects target namespaces in which to generate required RBAC access for all Operators in the same namespace as the Operator group. 

In most cases, the web console method of this procedure is preferred because it automates tasks in the background, such as handling the creation of `OperatorGroup` and `Subscription` objects automatically when choosing `SingleNamespace` mode. 

Warning

Failed Operator installations do not automatically remove created permissions. Audit and remove remaining permissions to secure the namespace. 

For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

**Prerequisites**

  * Access to your OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. View the list of Operators available to the cluster from the software catalog: 

```shell-session
$ oc get packagemanifests -n openshift-marketplace
```


**Example output**

```shell-session
NAME                               CATALOG               AGE
3scale-operator                    Red Hat Operators     91m
advanced-cluster-management        Red Hat Operators     91m
amq7-cert-manager                  Red Hat Operators     91m
# ...
couchbase-enterprise-certified     Certified Operators   91m
crunchy-postgres-operator          Certified Operators   91m
mongodb-enterprise                 Certified Operators   91m
# ...
etcd                               Community Operators   91m
jaeger                             Community Operators   91m
kubefed                            Community Operators   91m
# ...
```


Note the catalog for your desired Operator. 

  2. Inspect your desired Operator to verify its supported install modes and available channels: 

```shell-session
$ oc describe packagemanifests <operator_name> -n openshift-marketplace
```


**Example output**

```shell-session
# ...
Kind:         PackageManifest
# ...
      Install Modes:
        Supported:  true
        Type:       OwnNamespace
        Supported:  true
        Type:       SingleNamespace
        Supported:  false
        Type:       MultiNamespace
        Supported:  true
        Type:       AllNamespaces
# ...
    Entries:
      Name:       example-operator.v3.7.11
      Version:    3.7.11
      Name:       example-operator.v3.7.10
      Version:    3.7.10
    Name:         stable-3.7
# ...
   Entries:
      Name:         example-operator.v3.8.5
      Version:      3.8.5
      Name:         example-operator.v3.8.4
      Version:      3.8.4
    Name:           stable-3.8
  Default Channel:  stable-3.8
```


In the example output, `Install Modes` indicates which install modes are supported; `Name` shows example channel names; and `Default Channel` is the channel selected by default if one is not specified. 

Tip

You can print an Operator’s version and channel information in YAML format by running the following command: 

```shell-session
$ oc get packagemanifests <operator_name> -n <catalog_namespace> -o yaml
```


  3. If more than one catalog is installed in a namespace, run the following command to look up the available versions and channels of an Operator from a specific catalog: 

```shell-session
$ oc get packagemanifest \
   --selector=catalog=<catalogsource_name> \
   --field-selector metadata.name=<operator_name> \
   -n <catalog_namespace> -o yaml
```


Important

If you do not specify the Operator’s catalog, running the `oc get packagemanifest` and `oc describe packagemanifest` commands might return a package from an unexpected catalog if the following conditions are met: 

     * Multiple catalogs are installed in the same namespace. 
     * The catalogs contain the same Operators or Operators with the same name. 

  4. If the Operator you intend to install supports the `AllNamespaces` install mode, and you choose to use this mode, skip this step, because the `openshift-operators` namespace already has an appropriate Operator group in place by default, called `global-operators`. 

If the Operator you intend to install supports the `SingleNamespace` install mode, and you choose to use this mode, you must ensure an appropriate Operator group exists in the related namespace. If one does not exist, you can create create one by following these steps: 

Important

You can only have one Operator group per namespace. For more information, see "Operator groups". 

     1. Create an `OperatorGroup` object YAML file, for example `operatorgroup.yaml`, for `SingleNamespace` install mode: 

**Example`OperatorGroup` object for `SingleNamespace` install mode**

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: <operatorgroup_name>
  namespace: <namespace>
spec:
  targetNamespaces:
  - <namespace>
```


For `SingleNamespace` install mode, use the same `<namespace>` value for both the `metadata.namespace` and `spec.targetNamespaces` fields. 

     2. Create the `OperatorGroup` object: 

```shell-session
$ oc apply -f operatorgroup.yaml
```


  5. Create a `Subscription` object to subscribe a namespace to an Operator: 

     1. Create a YAML file for the `Subscription` object, for example `subscription.yaml`: 

Note

If you want to subscribe to a specific version of an Operator, set the `startingCSV` field to the desired version and set the `installPlanApproval` field to `Manual` to prevent the Operator from automatically upgrading if a later version exists in the catalog. For details, see the following "Example `Subscription` object with a specific starting Operator version". 

**Example`Subscription` object**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: <subscription_name>
  namespace: <namespace_per_install_mode>
spec:
  channel: <channel_name>
  name: <operator_name>
  source: <catalog_name>
  sourceNamespace: <catalog_source_namespace>
  config:
    env:
    - name: ARGS
      value: "-v=10"
    envFrom:
    - secretRef:
        name: license-secret
    volumes:
    - name: <volume_name>
      configMap:
        name: <configmap_name>
    volumeMounts:
    - mountPath: <directory_name>
      name: <volume_name>
    tolerations:
    - operator: "Exists"
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    nodeSelector:
      foo: bar
```


where: 

`<namespace_per_install_mode>`
     Specifies the namespace for your chosen install mode. For default `AllNamespaces` install mode usage, specify the `openshift-operators` namespace. Alternatively, you can specify a custom global namespace, if you have created one. For `SingleNamespace` install mode usage, specify the relevant single namespace. 
`<channel_name>`
     Specifies the name of the channel to subscribe to. 
`<operator_name>`
     Specifies the name of the Operator to subscribe to. 
`<catalog_name>`
     Specifies the name of the catalog source that provides the Operator. 
`<catalog_source_namespace>`
     Specifies the namespace of the catalog source. Use `openshift-marketplace` for the default software catalog sources. 
`config.env`
     Specifies a list of environment variables that must exist in all containers in the pod created by OLM. 
`config.envFrom`
     Specifies a list of sources to populate environment variables in the container. 
`config.volumes`
     Specifies a list of volumes that must exist on the pod created by OLM. 
`config.volumeMounts`
     Specifies a list of volume mounts that must exist in all containers in the pod created by OLM. If a `volumeMount` references a `volume` that does not exist, OLM fails to deploy the Operator. 
`config.tolerations`
     Specifies a list of tolerations for the pod created by OLM. 
`config.resources`
     Specifies resource constraints for all the containers in the pod created by OLM. 
`config.nodeSelector`
    

Specifies a `NodeSelector` for the pod created by OLM. 

**Example`Subscription` object with a specific starting Operator version**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: example-operator
  namespace: example-operator
spec:
  channel: stable-3.7
  installPlanApproval: Manual
  name: example-operator
  source: custom-operators
  sourceNamespace: openshift-marketplace
  startingCSV: example-operator.v3.7.10
```


where: 

`installPlanApproval`
     Specifies the approval strategy. Set to `Manual` in case your specified version is superseded by a later version in the catalog. This plan prevents an automatic upgrade to a later version and requires manual approval before the starting CSV can complete the installation. 
`startingCSV`
     Specifies a specific version of an Operator CSV. 

     2. For clusters on cloud providers with token authentication enabled, such as Amazon Web Services (AWS) Security Token Service (STS), Microsoft Entra Workload ID, or Google Cloud Platform Workload Identity, configure your `Subscription` object by following these steps: 

        1. Ensure the `Subscription` object is set to manual update approvals: 

**Example`Subscription` object with manual update approvals**

```yaml
kind: Subscription
# ...
spec:
  installPlanApproval: Manual
```


Set the `spec.installPlanApproval` parameter to `Manual`. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update. Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. 

        2. Include the relevant cloud provider-specific fields in the `Subscription` object’s `config` section: 

If the cluster is in AWS STS mode, include the following fields: 

**Example`Subscription` object with AWS STS variables**

```yaml
kind: Subscription
# ...
spec:
  config:
    env:
    - name: ROLEARN
      value: "<role_arn>"
```


           * `ROLEARN` is the Amazon Resource Name (ARN) of the role that the Operator assumes. 

If the cluster is in Workload ID mode, include the following fields: 

**Example`Subscription` object with Workload ID variables**

```yaml
kind: Subscription
# ...
spec:
 config:
   env:
   - name: CLIENTID
     value: "<client_id>"
   - name: TENANTID
     value: "<tenant_id>"
   - name: SUBSCRIPTIONID
     value: "<subscription_id>"
```


where: 

`<client_id>`
     Specifies the client ID. 
`<tenant_id>`
     Specifies the tenant ID. 
`<subscription_id>`
    

Specifies the subscription ID. 

If the cluster is in GCP Workload Identity mode, include the following fields: 

**Example`Subscription` object with GCP Workload Identity variables**

```yaml
kind: Subscription
# ...
spec:
 config:
   env:
   - name: AUDIENCE
     value: "<audience_url>"
   - name: SERVICE_ACCOUNT_EMAIL
     value: "<service_account_email>"
```


where: 

`<audience_url>`
    

Created in Google Cloud by the administrator when they set up GCP Workload Identity, the `AUDIENCE` value must be a preformatted URL in the following format: 

```plaintext
//iam.googleapis.com/projects/<project_number>/locations/global/workloadIdentityPools/<pool_id>/providers/<provider_id>
```


`<service_account_email>`
    

Specifies a Google Cloud service account email that is impersonated during Operator operation, for example: 

```plaintext
<service_account_name>@<project_id>.iam.gserviceaccount.com
```


     3. Create the `Subscription` object by running the following command: 

```shell-session
$ oc apply -f subscription.yaml
```


  6. If you set the `installPlanApproval` field to `Manual`, manually approve the pending install plan to complete the Operator installation. For more information, see "Manually approving a pending Operator update". 



**Verification**

At this point, OLM is now aware of the selected Operator. A cluster service version (CSV) for the Operator should appear in the target namespace, and APIs provided by the Operator should be available for creation. 

  1. Check the status of the `Subscription` object for your installed Operator by running the following command: 

```shell-session
$ oc describe subscription <subscription_name> -n <namespace>
```


  2. If you created an Operator group for `SingleNamespace` install mode, check the status of the `OperatorGroup` object by running the following command: 

```shell-session
$ oc describe operatorgroup <operatorgroup_name> -n <namespace>
```


**Additional resources**

  * [About OperatorGroups](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-operatorgroups-about_olm-understanding-operatorgroups)
