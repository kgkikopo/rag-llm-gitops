# 4.6. Managing user-defined labels and tags for Google Cloud

You can use Google Cloud labels and tags to identify and organize the resources created for a specific OpenShift Container Platform cluster. 

You can define labels and tags for each Google Cloud resource only during OpenShift Container Platform cluster installation. 

Important

User-defined labels and tags are not supported for OpenShift Container Platform clusters upgraded to OpenShift Container Platform 4.22. 

Note

You cannot update the tags that are already added. Also, a new tag-supported resource creation fails if the configured tag keys or tag values are deleted. 

User-defined labels and OpenShift Container Platform specific labels are applied only to resources created by the OpenShift Container Platform installation program and its core components, such as the following: 

  * Google Cloud FileStore CSI Driver Operator 
  * Google Cloud PD CSI Driver Operator 
  * Image Registry Operator 
  * Machine API provider for Google Cloud 



User-defined labels are not attached to the resources created by any other Operators or the Kubernetes in-tree components. 

User-defined labels and OpenShift Container Platform labels are available on the following Google Cloud resources: 

  * Compute disk 
  * Compute forwarding rule 
  * Compute image 
  * Compute instance 
  * DNS managed zone 
  * Filestore backup 
  * Filestore instance 
  * Storage bucket 



User-defined labels have the following limitations: 

  * Labels for `ComputeAddress` are supported in the Google Cloud beta version. OpenShift Container Platform does not add labels to the resource. 



User-defined tags are applied only to resources created by the OpenShift Container Platform installation program and its core components, such as the following: 

  * Google Cloud FileStore CSI Driver Operator 
  * Google Cloud PD CSI Driver Operator 
  * Image Registry Operator 
  * Machine API provider for Google Cloud 



User-defined tags are not attached to the resources created by any other Operators or the Kubernetes in-tree components. 

User-defined tags are available on the following Google Cloud resources: 

  * Compute disk 
  * Compute instance 
  * Filestore backup 
  * Filestore instance 
  * Storage bucket 



User-defined tags have the following limitations: 

  * Tags must not be restricted to particular service accounts, because Operators create and use service accounts with minimal roles. 
  * OpenShift Container Platform does not create any key and value resources of the tag. 
  * OpenShift Container Platform specific tags are not added to any resource. 



**Additional resources**

  * [Retrieving your organization ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id)
  * [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * [Labels overview](https://cloud.google.com/resource-manager/docs/labels-overview)
  * [Tags overview](https://cloud.google.com/resource-manager/docs/tags/tags-overview)



## 4.6.1. Criteria for user-defined labels and tags

User-defined labels and tags for Google Cloud in OpenShift Container Platform must meet specific formatting and quantity requirements for proper resource governance. 

The following list details the requirements for user-defined labels: 

  * A label key and value must have a minimum of 1 character and can have a maximum of 63 characters. 
  * A label key and value must contain only lowercase letters, numeric characters, an underscore (`_`), and a dash (`-`). 
  * A label key must start with a lowercase letter. 
  * You can configure a maximum of 32 labels per resource. 

    * Each resource has a maximum of 64 labels, where OpenShift Container Platform reserves 32 labels for internal use. 




The following list details the requirements for user-defined tags: 

  * Tag key and tag value must already exist. OpenShift Container Platform does not create the key and the value. 
  * A tag `parentID` can be either `OrganizationID` or `ProjectID`: 

    * `OrganizationID` must consist of decimal numbers without leading zeros. 
    * `ProjectID` must be 6 to 30 characters in length, that includes only lowercase letters, numbers, and hyphens. 
    * `ProjectID` must start with a letter, and cannot end with a hyphen. 

  * A tag key must contain only uppercase and lowercase alphanumeric characters, a hyphen (`-`), an underscore (`_`), and a period (`.`). 
  * A tag value must contain only uppercase and lowercase alphanumeric characters and any of the following characters: 

    * A colon (`:`) 
    * A comma (`,`) 
    * A curly braces (`{}`) 
    * A hyphen (`-`) 
    * A parentheses (`()`) 
    * A percent sign (`%`) 
    * A plus (`+`) 
    * A pound sign (`$`) 
    * A space. 
    * A square braces (`[]`) 
    * An ampersand (`&`) 
    * An asterisk (`*`) 
    * An at sign (`@`) 
    * An equals sign (`=`) 
    * An underscore (`_`) 
    * A period (`.`) 

  * A tag key and value must begin and end with an alphanumeric character. 
  * Tag value must be one of the predefined values for the key. 
  * You can configure a maximum of 50 tags. 
  * Do not define a tag key with the same value as any of the existing tag keys that get inherited from the parent resource. 



## 4.6.2. Configuring user-defined labels and tags for Google Cloud

You can apply key-value pairs as labels and tags to your Google Cloud resources to organize, manage, and automate your OpenShift Container Platform infrastructure. 

**Prerequisites**

  * The installation program requires that a service account includes a `TagUser` role, so that the program can create the OpenShift Container Platform cluster with defined tags at both organization and project levels. 



**Procedure**

  * Update the `install-config.yaml` file to define the list of required labels and tags. 

Note

If you set labels and tags during creation of the `install-config.yaml` configuration file, you cannot create new or update existing labels and tags after creation of the cluster. 

The following sample `install-config.yaml` file defines user labels and tags: 

```yaml
apiVersion: v1
credentialsMode: Passthrough
platform:
 gcp:
   userLabels:
   - key: <label_key>
     value: <label_value>
   userTags:
   - parentID: <OrganizationID/ProjectID>
     key: <tag_key_short_name>
     value: <tag_value_short_name>
# ...
```


where: 

  * `credentialsMode`: In passthrough mode, the Cloud Credential Operator (CCO) passes the provided cloud credential to the components that request cloud credentials. 
  * `userLabels`: Adds keys and values as labels to the resources created on Google Cloud. 
  * `<label_key>`: Specifies the label name. 
  * `<label_value>`: Specifies the label content. 
  * `userTags`: Adds keys and values as tags to the resources created on Google Cloud. 
  * `<OrganizationID/ProjectID>`: Specifies the ID of the hierarchical resource where you defined the tags at the organization or the project level. 



## 4.6.3. Querying user-defined labels and tags for Google Cloud

After creating the OpenShift Container Platform cluster, you can query the labels and tags defined for Google Cloud resources in the `infrastructures.config.openshift.io/cluster` object to verify your labeling configuration or reference tag values during troubleshooting. 

**Sample`infrastructure.yaml` file**

```yaml
apiVersion: config.openshift.io/v1
kind: Infrastructure
metadata:
 name: cluster
spec:
 platformSpec:
   type: GCP
status:
 infrastructureName: <cluster_id>
 platform: GCP
 platformStatus:
   gcp:
     resourceLabels:
     - key: <label_key>
       value: <label_value>
     resourceTags:
     - key: <tag_key_short_name>
       parentID: <OrganizationID/ProjectID>
       value: <tag_value_short_name>
   type: GCP
```


Where `<cluster_id>` is the cluster ID that is generated during cluster installation. 

Along with the user-defined labels, resources have a label defined by the OpenShift Container Platform. The format of the OpenShift Container Platform labels is `kubernetes-io-cluster-<cluster_id>:owned`.
