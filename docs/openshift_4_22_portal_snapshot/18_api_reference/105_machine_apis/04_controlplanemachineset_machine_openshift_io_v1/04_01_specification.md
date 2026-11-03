# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ControlPlaneMachineSet represents the configuration of the ControlPlaneMachineSet.   
`status` |  `object` |  ControlPlaneMachineSetStatus represents the status of the ControlPlaneMachineSet CRD.   
Show more

## 4.1.1. .spec

Description
     ControlPlaneMachineSet represents the configuration of the ControlPlaneMachineSet. 
Type
     `object`
Required
    

  * `replicas`
  * `selector`
  * `template`



Property| Type| Description  
---|---|---  
`machineNamePrefix` |  `string` |  machineNamePrefix is the prefix used when creating machine names. Each machine name will consist of this prefix, followed by a randomly generated string of 5 characters, and the index of the machine. It must be a lowercase RFC 1123 subdomain, consisting of lowercase alphanumeric characters, hyphens ('-'), and periods ('.'). Each block, separated by periods, must start and end with an alphanumeric character. Hyphens are not allowed at the start or end of a block, and consecutive periods are not permitted. The prefix must be between 1 and 245 characters in length. For example, if machineNamePrefix is set to 'control-plane', and three machines are created, their names might be: control-plane-abcde-0, control-plane-fghij-1, control-plane-klmno-2   
`replicas` |  `integer` |  replicas defines how many Control Plane Machines should be created by this ControlPlaneMachineSet. This field is immutable and cannot be changed after cluster installation. The ControlPlaneMachineSet only operates with 3 or 5 node control planes, 3 and 5 are the only valid values for this field.   
`selector` |  `object` |  Label selector for Machines. Existing Machines selected by this selector will be the ones affected by this ControlPlaneMachineSet. It must match the template’s labels. This field is considered immutable after creation of the resource.   
`state` |  `string` |  state defines whether the ControlPlaneMachineSet is Active or Inactive. When Inactive, the ControlPlaneMachineSet will not take any action on the state of the Machines within the cluster. When Active, the ControlPlaneMachineSet will reconcile the Machines and will update the Machines as necessary. Once Active, a ControlPlaneMachineSet cannot be made Inactive. To prevent further action please remove the ControlPlaneMachineSet.   
`strategy` |  `object` |  strategy defines how the ControlPlaneMachineSet will update Machines when it detects a change to the ProviderSpec.   
`template` |  `object` |  template describes the Control Plane Machines that will be created by this ControlPlaneMachineSet.   
Show more

## 4.1.2. .spec.selector

Description
     Label selector for Machines. Existing Machines selected by this selector will be the ones affected by this ControlPlaneMachineSet. It must match the template’s labels. This field is considered immutable after creation of the resource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 4.1.3. .spec.selector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 4.1.4. .spec.selector.matchExpressions[]

Description
     A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the label key that the selector applies to.   
`operator` |  `string` |  operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`values` |  `array (string)` |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
Show more

## 4.1.5. .spec.strategy

Description
     strategy defines how the ControlPlaneMachineSet will update Machines when it detects a change to the ProviderSpec. 
Type
     `object`

Property| Type| Description  
---|---|---  
`type` |  `string` |  type defines the type of update strategy that should be used when updating Machines owned by the ControlPlaneMachineSet. Valid values are "RollingUpdate" and "OnDelete". The current default value is "RollingUpdate".   
Show more

## 4.1.6. .spec.template

Description
     template describes the Control Plane Machines that will be created by this ControlPlaneMachineSet. 
Type
     `object`
Required
    

  * `machineType`



Property| Type| Description  
---|---|---  
`machineType` |  `string` |  machineType determines the type of Machines that should be managed by the ControlPlaneMachineSet. Currently, the only valid value is machines_v1beta1_machine_openshift_io.   
`machines_v1beta1_machine_openshift_io` |  `object` |  OpenShiftMachineV1Beta1Machine defines the template for creating Machines from the v1beta1.machine.openshift.io API group.   
Show more

## 4.1.7. .spec.template.machines_v1beta1_machine_openshift_io

Description
     OpenShiftMachineV1Beta1Machine defines the template for creating Machines from the v1beta1.machine.openshift.io API group. 
Type
     `object`
Required
    

  * `metadata`
  * `spec`



Property| Type| Description  
---|---|---  
`failureDomains` |  `object` |  failureDomains is the list of failure domains (sometimes called availability zones) in which the ControlPlaneMachineSet should balance the Control Plane Machines. This will be merged into the ProviderSpec given in the template. This field is optional on platforms that do not require placement information.   
`metadata` |  `object` |  ObjectMeta is the standard object metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> Labels are required to match the ControlPlaneMachineSet selector.   
`spec` |  `object` |  spec contains the desired configuration of the Control Plane Machines. The ProviderSpec within contains platform specific details for creating the Control Plane Machines. The ProviderSe should be complete apart from the platform specific failure domain field. This will be overridden when the Machines are created based on the FailureDomains field.   
Show more

## 4.1.8. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains

Description
     failureDomains is the list of failure domains (sometimes called availability zones) in which the ControlPlaneMachineSet should balance the Control Plane Machines. This will be merged into the ProviderSpec given in the template. This field is optional on platforms that do not require placement information. 
Type
     `object`
Required
    

  * `platform`



Property| Type| Description  
---|---|---  
`aws` |  `array` |  aws configures failure domain information for the AWS platform.   
`aws[]` |  `object` |  AWSFailureDomain configures failure domain information for the AWS platform.   
`azure` |  `array` |  azure configures failure domain information for the Azure platform.   
`azure[]` |  `object` |  AzureFailureDomain configures failure domain information for the Azure platform.   
`gcp` |  `array` |  gcp configures failure domain information for the GCP platform.   
`gcp[]` |  `object` |  GCPFailureDomain configures failure domain information for the GCP platform   
`nutanix` |  `array` |  nutanix configures failure domain information for the Nutanix platform.   
`nutanix[]` |  `object` |  NutanixFailureDomainReference refers to the failure domain of the Nutanix platform.   
`openstack` |  `array` |  openstack configures failure domain information for the OpenStack platform.   
`openstack[]` |  `object` |  OpenStackFailureDomain configures failure domain information for the OpenStack platform.   
`platform` |  `string` |  platform identifies the platform for which the FailureDomain represents. Currently supported values are AWS, Azure, GCP, OpenStack, VSphere and Nutanix.   
`vsphere` |  `array` |  vsphere configures failure domain information for the VSphere platform.   
`vsphere[]` |  `object` |  VSphereFailureDomain configures failure domain information for the vSphere platform   
Show more

## 4.1.9. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws

Description
     aws configures failure domain information for the AWS platform. 
Type
     `array`

## 4.1.10. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws[]

Description
     AWSFailureDomain configures failure domain information for the AWS platform. 
Type
     `object`

Property| Type| Description  
---|---|---  
`placement` |  `object` |  placement configures the placement information for this instance.   
`subnet` |  `object` |  subnet is a reference to the subnet to use for this instance.   
Show more

## 4.1.11. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws[].placement

Description
     placement configures the placement information for this instance. 
Type
     `object`
Required
    

  * `availabilityZone`



Property| Type| Description  
---|---|---  
`availabilityZone` |  `string` |  availabilityZone is the availability zone of the instance.   
Show more

## 4.1.12. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws[].subnet

Description
     subnet is a reference to the subnet to use for this instance. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`arn` |  `string` |  arn of resource.   
`filters` |  `array` |  filters is a set of filters used to identify a resource.   
`filters[]` |  `object` |  AWSResourceFilter is a filter used to identify an AWS resource   
`id` |  `string` |  id of resource.   
`type` |  `string` |  type determines how the reference will fetch the AWS resource.   
Show more

## 4.1.13. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws[].subnet.filters

Description
     filters is a set of filters used to identify a resource. 
Type
     `array`

## 4.1.14. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws[].subnet.filters[]

Description
     AWSResourceFilter is a filter used to identify an AWS resource 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the filter. Filter names are case-sensitive.   
`values` |  `array (string)` |  values includes one or more filter values. Filter values are case-sensitive.   
Show more

## 4.1.15. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.azure

Description
     azure configures failure domain information for the Azure platform. 
Type
     `array`

## 4.1.16. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.azure[]

Description
     AzureFailureDomain configures failure domain information for the Azure platform. 
Type
     `object`
Required
    

  * `zone`



Property| Type| Description  
---|---|---  
`subnet` |  `string` |  subnet is the name of the network subnet in which the VM will be created. When omitted, the subnet value from the machine providerSpec template will be used.   
`zone` |  `string` |  Availability Zone for the virtual machine. If nil, the virtual machine should be deployed to no zone.   
Show more

## 4.1.17. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.gcp

Description
     gcp configures failure domain information for the GCP platform. 
Type
     `array`

## 4.1.18. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.gcp[]

Description
     GCPFailureDomain configures failure domain information for the GCP platform 
Type
     `object`
Required
    

  * `zone`



Property| Type| Description  
---|---|---  
`zone` |  `string` |  zone is the zone in which the GCP machine provider will create the VM.   
Show more

## 4.1.19. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.nutanix

Description
     nutanix configures failure domain information for the Nutanix platform. 
Type
     `array`

## 4.1.20. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.nutanix[]

Description
     NutanixFailureDomainReference refers to the failure domain of the Nutanix platform. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the failure domain in which the nutanix machine provider will create the VM. Failure domains are defined in a cluster’s config.openshift.io/Infrastructure resource.   
Show more

## 4.1.21. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.openstack

Description
     openstack configures failure domain information for the OpenStack platform. 
Type
     `array`

## 4.1.22. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.openstack[]

Description
     OpenStackFailureDomain configures failure domain information for the OpenStack platform. 
Type
     `object`

Property| Type| Description  
---|---|---  
`availabilityZone` |  `string` |  availabilityZone is the nova availability zone in which the OpenStack machine provider will create the VM. If not specified, the VM will be created in the default availability zone specified in the nova configuration. Availability zone names must NOT contain : since it is used by admin users to specify hosts where instances are launched in server creation. Also, it must not contain spaces otherwise it will lead to node that belongs to this availability zone register failure, see kubernetes/cloud-provider-openstack#1379 for further information. The maximum length of availability zone name is 63 as per labels limits.   
`rootVolume` |  `object` |  rootVolume contains settings that will be used by the OpenStack machine provider to create the root volume attached to the VM. If not specified, no root volume will be created.   
Show more

## 4.1.23. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.openstack[].rootVolume

Description
     rootVolume contains settings that will be used by the OpenStack machine provider to create the root volume attached to the VM. If not specified, no root volume will be created. 
Type
     `object`
Required
    

  * `volumeType`



Property| Type| Description  
---|---|---  
`availabilityZone` |  `string` |  availabilityZone specifies the Cinder availability zone where the root volume will be created. If not specifified, the root volume will be created in the availability zone specified by the volume type in the cinder configuration. If the volume type (configured in the OpenStack cluster) does not specify an availability zone, the root volume will be created in the default availability zone specified in the cinder configuration. See <https://docs.openstack.org/cinder/latest/admin/availability-zone-type.html> for more details. If the OpenStack cluster is deployed with the cross_az_attach configuration option set to false, the root volume will have to be in the same availability zone as the VM (defined by OpenStackFailureDomain.AvailabilityZone). Availability zone names must NOT contain spaces otherwise it will lead to volume that belongs to this availability zone register failure, see kubernetes/cloud-provider-openstack#1379 for further information. The maximum length of availability zone name is 63 as per labels limits.   
`volumeType` |  `string` |  volumeType specifies the type of the root volume that will be provisioned. The maximum length of a volume type name is 255 characters, as per the OpenStack limit.   
Show more

## 4.1.24. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.vsphere

Description
     vsphere configures failure domain information for the VSphere platform. 
Type
     `array`

## 4.1.25. .spec.template.machines_v1beta1_machine_openshift_io.failureDomains.vsphere[]

Description
     VSphereFailureDomain configures failure domain information for the vSphere platform 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the failure domain in which the vSphere machine provider will create the VM. Failure domains are defined in a cluster’s config.openshift.io/Infrastructure resource. When balancing machines across failure domains, the control plane machine set will inject configuration from the Infrastructure resource into the machine providerSpec to allocate the machine to a failure domain.   
Show more

## 4.1.26. .spec.template.machines_v1beta1_machine_openshift_io.metadata

Description
     ObjectMeta is the standard object metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> Labels are required to match the ControlPlaneMachineSet selector. 
Type
     `object`
Required
    

  * `labels`



Property| Type| Description  
---|---|---  
`annotations` |  `object (string)` |  annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <http://kubernetes.io/docs/user-guide/annotations>  
`labels` |  `object (string)` |  Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <http://kubernetes.io/docs/user-guide/labels>. This field must contain both the 'machine.openshift.io/cluster-api-machine-role' and 'machine.openshift.io/cluster-api-machine-type' labels, both with a value of 'master'. It must also contain a label with the key 'machine.openshift.io/cluster-api-cluster'.   
Show more

## 4.1.27. .spec.template.machines_v1beta1_machine_openshift_io.spec

Description
     spec contains the desired configuration of the Control Plane Machines. The ProviderSpec within contains platform specific details for creating the Control Plane Machines. The ProviderSe should be complete apart from the platform specific failure domain field. This will be overridden when the Machines are created based on the FailureDomains field. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lifecycleHooks` |  `object` |  lifecycleHooks allow users to pause operations on the machine at certain predefined points within the machine lifecycle.   
`metadata` |  `object` |  ObjectMeta will autopopulate the Node created. Use this to indicate what labels, annotations, name prefix, etc., should be used when creating the Node.   
`providerID` |  `string` |  providerID is the identification ID of the machine provided by the provider. This field must match the provider ID as seen on the node object corresponding to this machine. This field is required by higher level consumers of cluster-api. Example use case is cluster autoscaler with cluster-api as provider. Clean-up logic in the autoscaler compares machines to nodes to find out machines at provider which could not get registered as Kubernetes nodes. With cluster-api as a generic out-of-tree provider for autoscaler, this field is required by autoscaler to be able to have a provider view of the list of machines. Another list of nodes is queried from the k8s apiserver and then a comparison is done to find out unregistered machines and are marked for delete. This field will be set by the actuators and consumed by higher level entities like autoscaler that will be interfacing with cluster-api as generic provider.   
`providerSpec` |  `object` |  providerSpec details Provider-specific configuration to use during node creation.   
`taints` |  `array` |  The list of the taints to be applied to the corresponding Node in additive manner. This list will not overwrite any other taints added to the Node on an ongoing basis by other entities. These taints should be actively reconciled e.g. if you ask the machine controller to apply a taint and then manually remove the taint the machine controller will put it back) but not have the machine controller remove any taints   
`taints[]` |  `object` |  The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.   
Show more

## 4.1.28. .spec.template.machines_v1beta1_machine_openshift_io.spec.lifecycleHooks

Description
     lifecycleHooks allow users to pause operations on the machine at certain predefined points within the machine lifecycle. 
Type
     `object`

Property| Type| Description  
---|---|---  
`preDrain` |  `array` |  preDrain hooks prevent the machine from being drained. This also blocks further lifecycle events, such as termination.   
`preDrain[]` |  `object` |  LifecycleHook represents a single instance of a lifecycle hook   
`preTerminate` |  `array` |  preTerminate hooks prevent the machine from being terminated. PreTerminate hooks be actioned after the Machine has been drained.   
`preTerminate[]` |  `object` |  LifecycleHook represents a single instance of a lifecycle hook   
Show more

## 4.1.29. .spec.template.machines_v1beta1_machine_openshift_io.spec.lifecycleHooks.preDrain

Description
     preDrain hooks prevent the machine from being drained. This also blocks further lifecycle events, such as termination. 
Type
     `array`

## 4.1.30. .spec.template.machines_v1beta1_machine_openshift_io.spec.lifecycleHooks.preDrain[]

Description
     LifecycleHook represents a single instance of a lifecycle hook 
Type
     `object`
Required
    

  * `name`
  * `owner`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name defines a unique name for the lifcycle hook. The name should be unique and descriptive, ideally 1-3 words, in CamelCase or it may be namespaced, eg. foo.example.com/CamelCase. Names must be unique and should only be managed by a single entity.   
`owner` |  `string` |  owner defines the owner of the lifecycle hook. This should be descriptive enough so that users can identify who/what is responsible for blocking the lifecycle. This could be the name of a controller (e.g. clusteroperator/etcd) or an administrator managing the hook.   
Show more

## 4.1.31. .spec.template.machines_v1beta1_machine_openshift_io.spec.lifecycleHooks.preTerminate

Description
     preTerminate hooks prevent the machine from being terminated. PreTerminate hooks be actioned after the Machine has been drained. 
Type
     `array`

## 4.1.32. .spec.template.machines_v1beta1_machine_openshift_io.spec.lifecycleHooks.preTerminate[]

Description
     LifecycleHook represents a single instance of a lifecycle hook 
Type
     `object`
Required
    

  * `name`
  * `owner`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name defines a unique name for the lifcycle hook. The name should be unique and descriptive, ideally 1-3 words, in CamelCase or it may be namespaced, eg. foo.example.com/CamelCase. Names must be unique and should only be managed by a single entity.   
`owner` |  `string` |  owner defines the owner of the lifecycle hook. This should be descriptive enough so that users can identify who/what is responsible for blocking the lifecycle. This could be the name of a controller (e.g. clusteroperator/etcd) or an administrator managing the hook.   
Show more

## 4.1.33. .spec.template.machines_v1beta1_machine_openshift_io.spec.metadata

Description
     ObjectMeta will autopopulate the Node created. Use this to indicate what labels, annotations, name prefix, etc., should be used when creating the Node. 
Type
     `object`

Property| Type| Description  
---|---|---  
`annotations` |  `object (string)` |  annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <http://kubernetes.io/docs/user-guide/annotations>  
`generateName` |  `string` |  generateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency>  
`labels` |  `object (string)` |  Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <http://kubernetes.io/docs/user-guide/labels>  
`name` |  `string` |  name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <http://kubernetes.io/docs/user-guide/identifiers#names>  
`namespace` |  `string` |  namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: <http://kubernetes.io/docs/user-guide/namespaces>  
`ownerReferences` |  `array` |  List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.   
`ownerReferences[]` |  `object` |  OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.   
Show more

## 4.1.34. .spec.template.machines_v1beta1_machine_openshift_io.spec.metadata.ownerReferences

Description
     List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller. 
Type
     `array`

## 4.1.35. .spec.template.machines_v1beta1_machine_openshift_io.spec.metadata.ownerReferences[]

Description
     OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field. 
Type
     `object`
Required
    

  * `apiVersion`
  * `kind`
  * `name`
  * `uid`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`blockOwnerDeletion` |  `boolean` |  If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See <https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion> for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.   
`controller` |  `boolean` |  If true, this reference points to the managing controller.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids>  
Show more

## 4.1.36. .spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec

Description
     providerSpec details Provider-specific configuration to use during node creation. 
Type
     `object`

Property| Type| Description  
---|---|---  
`value` |  ``  |  value is an inlined, serialized representation of the resource configuration. It is recommended that providers maintain their own versioned API types that should be serialized/deserialized from this field, akin to component config.   
Show more

## 4.1.37. .spec.template.machines_v1beta1_machine_openshift_io.spec.taints

Description
     The list of the taints to be applied to the corresponding Node in additive manner. This list will not overwrite any other taints added to the Node on an ongoing basis by other entities. These taints should be actively reconciled e.g. if you ask the machine controller to apply a taint and then manually remove the taint the machine controller will put it back) but not have the machine controller remove any taints 
Type
     `array`

## 4.1.38. .spec.template.machines_v1beta1_machine_openshift_io.spec.taints[]

Description
     The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint. 
Type
     `object`
Required
    

  * `effect`
  * `key`



Property| Type| Description  
---|---|---  
`effect` |  `string` |  Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.   
`key` |  `string` |  Required. The taint key to be applied to a node.   
`timeAdded` |  `string` |  TimeAdded represents the time at which the taint was added.   
`value` |  `string` |  The taint value corresponding to the taint key.   
Show more

## 4.1.39. .status

Description
     ControlPlaneMachineSetStatus represents the status of the ControlPlaneMachineSet CRD. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represents the observations of the ControlPlaneMachineSet’s current state. Known .status.conditions.type are: Available, Degraded and Progressing.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`observedGeneration` |  `integer` |  observedGeneration is the most recent generation observed for this ControlPlaneMachineSet. It corresponds to the ControlPlaneMachineSets’s generation, which is updated on mutation by the API Server.   
`readyReplicas` |  `integer` |  readyReplicas is the number of Control Plane Machines created by the ControlPlaneMachineSet controller which are ready. Note that this value may be higher than the desired number of replicas while rolling updates are in-progress.   
`replicas` |  `integer` |  replicas is the number of Control Plane Machines created by the ControlPlaneMachineSet controller. Note that during update operations this value may differ from the desired replica count.   
`unavailableReplicas` |  `integer` |  unavailableReplicas is the number of Control Plane Machines that are still required before the ControlPlaneMachineSet reaches the desired available capacity. When this value is non-zero, the number of ReadyReplicas is less than the desired Replicas.   
`updatedReplicas` |  `integer` |  updatedReplicas is the number of non-terminated Control Plane Machines created by the ControlPlaneMachineSet controller that have the desired provider spec and are ready. This value is set to 0 when a change is detected to the desired spec. When the update strategy is RollingUpdate, this will also coincide with starting the process of updating the Machines. When the update strategy is OnDelete, this value will remain at 0 until a user deletes an existing replica and its replacement has become ready.   
Show more

## 4.1.40. .status.conditions

Description
     conditions represents the observations of the ControlPlaneMachineSet’s current state. Known .status.conditions.type are: Available, Degraded and Progressing. 
Type
     `array`

## 4.1.41. .status.conditions[]

Description
     Condition contains details for one aspect of the current state of this API Resource. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `message`
  * `reason`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This may be an empty string.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more
