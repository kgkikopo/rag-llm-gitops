# 2.3. Cluster Samples Operator tracking and error recovery of image stream imports

After creation or update of a samples image stream, the Cluster Samples Operator monitors the progress of each image stream tag’s image import. 

If an import fails, the Cluster Samples Operator retries the import through the image stream image import API at a rate of about every 15 minutes until either one of the following occurs: 

  * The import succeeds. 
  * The Cluster Samples Operator configuration is changed such that either the image stream is added to the `skippedImagestreams` list, or the management state is changed to `Removed`. 



## 2.3.1. Cluster Samples Operator assistance for mirroring

During installation, OpenShift Container Platform creates a config map named `imagestreamtag-to-image` in the `openshift-cluster-samples-operator` namespace. 

The `imagestreamtag-to-image` config map contains an entry, the populating image, for each image stream tag. 

The format of the key for each entry in the data field in the config map is `<image_stream_name>_<image_stream_tag_name>`. 

During a disconnected installation of OpenShift Container Platform, the status of the Cluster Samples Operator is set to `Removed`. If you choose to change it to `Managed`, it installs samples. 

Note

The use of samples in a network-restricted or discontinued environment might require access to services external to your network. Some example services include: Github, Maven Central, npm, RubyGems, PyPi and others. There might be additional steps to take that allow the Cluster Samples Operators objects to reach the services they require. 

Use the following principles to determine which images you need to mirror for your image streams to import: 

  * While the Cluster Samples Operator is set to `Removed`, you can create your mirrored registry, or determine which existing mirrored registry you want to use. 
  * Mirror the samples you want to the mirrored registry using the new config map as your guide. 
  * Add any of the image streams you did not mirror to the `skippedImagestreams` list of the Cluster Samples Operator configuration object. 
  * Set `samplesRegistry` of the Cluster Samples Operator configuration object to the mirrored registry. 
  * Then set the Cluster Samples Operator to `Managed` to install the image streams you have mirrored.
