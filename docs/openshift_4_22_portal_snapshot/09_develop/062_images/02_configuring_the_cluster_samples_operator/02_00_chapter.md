# Chapter 2. Configuring the Cluster Samples Operator

You can configure the Cluster Samples Operator to manage the installation and updates of Red Hat Enterprise Linux (RHEL)-based OpenShift Container Platform image streams and templates in the `openshift` namespace. 

Important

  * The Cluster Samples Operator is deprecated. No new templates, samples, or non-Source-to-Image (Non-S2I) image streams are added to the Cluster Samples Operator. However, the existing S2I builder image streams and templates will continue to receive updates until the Cluster Samples Operator is removed in a future release. S2I image streams and templates include: 

    * Ruby 
    * Python 
    * Node.js 
    * Perl 
    * PHP 
    * HTTPD 
    * Nginx 
    * EAP 
    * Java 
    * Webserver 
    * .NET 
    * Go 

  * The Cluster Samples Operator will stop managing and providing support to the non-S2I samples (image streams and templates). You can contact the image stream or template owner for any requirements and future plans. In addition, refer to the following link: 

    * [List of the repositories hosting the image stream or templates](https://github.com/openshift/library/blob/master/official.yaml)

- [2.1. Understand the Cluster Samples Operator](02_01_understand_the_cluster_samples_operator.md)
- [2.2. Cluster Samples Operator use of management state](02_02_cluster_samples_operator_use_of_management_state.md)
- [2.3. Cluster Samples Operator tracking and error recovery of image stream imports](02_03_cluster_samples_operator_tracking_and_error_recovery_of_image_stream_imports.md)
- [2.4. Cluster Samples Operator configuration parameters](02_04_cluster_samples_operator_configuration_parameters.md)
- [2.5. Access the Cluster Samples Operator configuration](02_05_access_the_cluster_samples_operator_configuration.md)
- [2.6. Remove deprecated image stream tags from the Cluster Samples Operator](02_06_remove_deprecated_image_stream_tags_from_the_cluster_samples_operator.md)
