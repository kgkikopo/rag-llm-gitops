# Chapter 14. Setting up additional trusted certificate authorities for builds

Use the following sections to set up additional certificate authorities (CA) to be trusted by builds when pulling images from an image registry. 

The procedure requires a cluster administrator to create a `ConfigMap` and add additional CAs as keys in the `ConfigMap`. 

  * The `ConfigMap` must be created in the `openshift-config` namespace. 
  * `domain` is the key in the `ConfigMap` and `value` is the PEM-encoded certificate. 

    * Each CA must be associated with a domain. The domain format is `hostname[..port]`. 

  * The `ConfigMap` name must be set in the `image.config.openshift.io/cluster` cluster scoped configuration resource’s `spec.additionalTrustedCA` field.

- [14.1. Add certificate authorities to the cluster](14_01_add_certificate_authorities_to_the_cluster.md)
- [14.2. Additional resources](14_02_additional_resources.md)
