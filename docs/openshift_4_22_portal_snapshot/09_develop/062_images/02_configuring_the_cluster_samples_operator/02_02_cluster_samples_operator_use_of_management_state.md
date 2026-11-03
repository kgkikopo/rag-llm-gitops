# 2.2. Cluster Samples Operator use of management state

The Cluster Samples Operator is bootstrapped as `Managed` by default or if global proxy is configured. 

In the `Managed` state, the Cluster Samples Operator is actively managing its resources and keeping the component active to pull sample image streams and images from the registry and ensure that the requisite sample templates are installed. 

Certain circumstances result in the Cluster Samples Operator bootstrapping itself as `Removed` including: 

  * If the Cluster Samples Operator cannot reach the registry after three minutes on initial startup after a clean installation. 
  * If the Cluster Samples Operator detects that it is on an IPv6 network. 
  * If the image controller configuration parameters prevent the creation of image streams by using the default image registry, or by using the image registry specified by `samplesRegistry` setting. For more information, see "Image controller configuration parameters" and "Cluster Samples Operator configuration parameters". 



Note

For OpenShift Container Platform, the default image registry is `registry.redhat.io`. 

However, if the Cluster Samples Operator detects that it is on an IPv6 network and an OpenShift Container Platform global proxy is configured, then the IPv6 check supersedes all the checks. As a result, the Cluster Samples Operator bootstraps itself as `Removed`. 

Important

IPv6 installations are not currently supported by the registry. The Cluster Samples Operator pulls most of the sample image streams and images from the registry. 

**Additional resources**

  * [Image controller configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/image-configuration-classic#images-configuration-parameters_image-configuration)
  * [Cluster Samples Operator configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/configuring-samples-operator#samples-operator-configuration_configuring-samples-operator)



## 2.2.1. Restricted network installation

The Cluster Samples Operator bootstrapping itself as `Removed` when unable to access `registry.redhat.io` facilitates restricted network installations when the network restriction is already in place. 

As a cluster administrator, you have more time to decide if samples are needed when the Operator is bootstrapped `Removed`. This is because the Cluster Samples Operator does not submit alerts that sample image stream imports are failing when the management state is `Removed`. When the Cluster Samples Operator management state is `Managed`, and the Operator attempts to install sample image streams, failing-import alerts start two hours after initial installation. 

## 2.2.2. Restricted network installation with initial network access

If a cluster that eventually runs on a restricted network is first installed while network access exists, the Cluster Samples Operator installs content from `registry.redhat.io`. 

In this case, you can defer samples installation until you have decided which samples are needed by overriding the default configuration of `Managed` for a connected installation. 

If you want the Cluster Samples Operator to bootstrap with the management state as `Removed` during an installation that has initial network access, override the Cluster Samples Operator default configuration by using the following instructions: 

  * [Customizing nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installation_configuration/installing-customizing)



To host samples in your restricted environment, use the following instructions: 

  * [Using the Cluster Samples Operator with an alternate registry](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/samples-operator-alt-registry)



You must also put the following additional YAML file in the `openshift` directory created by the `openshift-install create manifest` process: 

**Example Cluster Samples Operator YAML file with`managementState: Removed`**

```yaml
apiVersion: samples.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  architectures:
  - x86_64
  managementState: Removed
```
