# 6.13. Cluster Samples Operator

The Cluster Samples Operator is an optional cluster capability that can be disabled by cluster administrators during installation. 

For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_. 

The Cluster Samples Operator manages the sample image streams and templates stored in the `openshift` namespace. 

On initial start up, the Operator creates the default samples configuration resource to initiate the creation of the image streams and templates. The configuration object is a cluster scoped object with the key `cluster` and type `configs.samples`. 

The image streams are the Red Hat Enterprise Linux CoreOS (RHCOS)-based OpenShift Container Platform image streams pointing to images on `registry.redhat.io`. Similarly, the templates are those categorized as OpenShift Container Platform templates. 

The Cluster Samples Operator deployment is contained within the `openshift-cluster-samples-operator` namespace. On start up, the install pull secret is used by the image stream import logic in the OpenShift image registry and API server to authenticate with `registry.redhat.io`. An administrator can create any additional secrets in the `openshift` namespace if they change the registry used for the sample image streams. If created, those secrets contain the content of a `config.json` for `docker` needed to facilitate image import. 

The image for the Cluster Samples Operator contains image stream and template definitions for the associated OpenShift Container Platform release. After the Cluster Samples Operator creates a sample, it adds an annotation that denotes the OpenShift Container Platform version that it is compatible with. The Operator uses this annotation to ensure that each sample matches the compatible release version. Samples outside of its inventory are ignored, as are skipped samples. 

Modifications to any samples that are managed by the Operator are allowed as long as the version annotation is not modified or deleted. However, on an upgrade, as the version annotation will change, those modifications can get replaced as the sample will be updated with the newer version. The Jenkins images are part of the image payload from the installation and are tagged into the image streams directly. 

The samples resource includes a finalizer, which cleans up the following upon its deletion: 

  * Operator-managed image streams 
  * Operator-managed templates 
  * Operator-generated configuration resources 
  * Cluster status resources 



Upon deletion of the samples resource, the Cluster Samples Operator recreates the resource using the default configuration. 

**Additional resources**

  * [OpenShift samples capability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-samples-operator_cluster-capabilities)
  * [cluster-samples-operator](https://github.com/openshift/cluster-samples-operator)
