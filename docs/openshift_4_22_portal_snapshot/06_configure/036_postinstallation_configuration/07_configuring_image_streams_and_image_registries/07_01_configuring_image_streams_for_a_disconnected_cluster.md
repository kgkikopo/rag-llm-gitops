# 7.1. Configuring image streams for a disconnected cluster

After installing OpenShift Container Platform in a disconnected environment, configure the image streams for the Cluster Samples Operator and the `must-gather` image stream. 

## 7.1.1. Cluster Samples Operator assistance for mirroring

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



## 7.1.2. Use Cluster Samples Operator image streams with alternate or mirrored registries

You can use an alternate or mirror registry to host your images streams instead of using the Red Hat registry. 

Most image streams in the `openshift` namespace managed by the Cluster Samples Operator point to images located in the Red Hat registry at [registry.redhat.io](https://registry.redhat.io). 

Note

The `cli`, `installer`, `must-gather`, and `tests` image streams, while part of the install payload, are not managed by the Cluster Samples Operator. These are not addressed in this procedure. 

Important

The Cluster Samples Operator must be set to `Managed` in a disconnected environment. To install the image streams, you must have a mirrored registry. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * Create a pull secret for your mirror registry. 



**Procedure**

  1. Access the images of a specific image stream to mirror, for example: 

```shell-session
$ oc get is <imagestream> -n openshift -o json | jq .spec.tags[].from.name | grep registry.redhat.io
```


  2. Mirror images from [registry.redhat.io](https://registry.redhat.io) associated with any image streams you need 

```shell-session
$ oc image mirror registry.redhat.io/rhscl/ruby-25-rhel7:latest ${MIRROR_ADDR}/rhscl/ruby-25-rhel7:latest
```


  3. Create the image configuration object for the cluster by running the following command: 

```shell-session
$ oc create configmap registry-config --from-file=${MIRROR_ADDR_HOSTNAME}..5000=$path/ca.crt -n openshift-config
```


  4. Add the required trusted CAs for the mirror in the image configuration object: 

```shell-session
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
```


  5. Update the `samplesRegistry` field in the Cluster Samples Operator configuration object to contain the `hostname` portion of the mirror location defined in the mirror configuration: 

```shell-session
$ oc edit configs.samples.operator.openshift.io -n openshift-cluster-samples-operator
```


Important

This step is required because the image stream import process does not use the mirror or search mechanism at this time. 

  6. Add any image streams that are not mirrored into the `skippedImagestreams` field of the Cluster Samples Operator configuration object. Or if you do not want to support any of the sample image streams, set the Cluster Samples Operator to `Removed` in the Cluster Samples Operator configuration object. 

Note

The Cluster Samples Operator issues alerts if image stream imports are failing but the Cluster Samples Operator is either periodically retrying or does not appear to be retrying them. 

Many of the templates in the `openshift` namespace reference the image streams. You can use `Removed` to purge both the image streams and templates. This eliminates the possibility of attempts to use the templates if they are not functional because of any missing image streams. 




## 7.1.3. Preparing your cluster to gather support data

You can prepare a cluster on a restricted network to gather support data by importing the default must-gather image and configuring access to the mirror registry. 

Clusters using a restricted network must import the default must-gather image to gather debugging data for Red Hat support. The must-gather image is not imported by default, and clusters on a restricted network do not have access to the internet to pull the latest image from a remote repository. 

**Procedure**

  1. If you have not added your mirror registry’s trusted CA to your cluster’s image configuration object as part of the Cluster Samples Operator configuration, perform the following steps: 

     1. Create the cluster’s image configuration object: 

```shell-session
$ oc create configmap registry-config --from-file=${MIRROR_ADDR_HOSTNAME}..5000=$path/ca.crt -n openshift-config
```


     2. Add the required trusted CAs for the mirror in the cluster’s image configuration object: 

```shell-session
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
```


  2. Import the default must-gather image from your installation payload: 

```shell-session
$ oc import-image is/must-gather -n openshift
```


When running the `oc adm must-gather` command, use the `--image` flag and point to the payload image, as in the following example: 

```shell-session
$ oc adm must-gather --image=$(oc adm release info --image-for must-gather)
```
