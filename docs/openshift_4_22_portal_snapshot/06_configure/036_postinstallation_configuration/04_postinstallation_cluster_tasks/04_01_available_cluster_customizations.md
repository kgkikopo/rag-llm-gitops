# 4.1. Available cluster customizations

You complete most of the cluster configuration and customization after you deploy your OpenShift Container Platform cluster. Several _configuration resources_ are available. 

Note

If you install your cluster on IBM Z®, not all features and functions are available. 

You modify the configuration resources to configure the major features of the cluster, such as the image registry, networking configuration, image build behavior, and the identity provider. 

For current documentation of the settings that you control by using these resources, use the `oc explain` command, for example `oc explain builds --api-version=config.openshift.io/v1`

## 4.1.1. Cluster configuration resources

Review the globally scoped cluster configuration resources that control major features of an OpenShift Container Platform cluster. 

All cluster configuration resources are globally scoped (not namespaced) and named `cluster`. 

Resource name| Description  
---|---  
`apiserver.config.openshift.io` |  Provides API server configuration such as [certificates and certificate authorities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#api-server-certificates).   
`authentication.config.openshift.io` |  Controls the [identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-identity-provider) and authentication configuration for the cluster.   
`build.config.openshift.io` |  Controls default and enforced [configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_buildconfig/#build-configuration) for all builds on the cluster.   
`console.config.openshift.io` |  Configures the behavior of the web console interface, including the [logout behavior](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#configuring-web-console).   
`featuregate.config.openshift.io` |  Enables [FeatureGates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cluster-enabling-features) so that you can use Tech Preview features.   
`image.config.openshift.io` |  Configures how specific [image registries](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#image-configuration) should be treated (allowed, disallowed, insecure, CA details).   
`ingress.config.openshift.io` |  Configuration details related to [routing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-installation-ingress-config-asset_ingress-operator) such as the default domain for routes.   
`oauth.config.openshift.io` |  Configures identity providers and other behavior related to [internal OAuth server](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-internal-oauth) flows.   
`project.config.openshift.io` |  Configures [how projects are created](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#configuring-project-creation) including the project template.   
`proxy.config.openshift.io` |  Defines proxies to be used by components needing external network access. Note: not all components currently consume this value.   
`scheduler.config.openshift.io` |  Configures [scheduler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-profiles) behavior such as profiles and default node selectors.   
Show more

## 4.1.2. Operator configuration resources

Review the cluster-scoped Operator configuration resources that control the behavior of specific OpenShift Container Platform components. 

These configuration resources are cluster-scoped instances, named `cluster`, which control the behavior of a specific component as owned by a particular Operator. 

Resource name| Description  
---|---  
`consoles.operator.openshift.io` |  Controls console appearance such as branding customizations   
`config.imageregistry.operator.openshift.io` |  Configures [OpenShift image registry settings](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/registry/#registry-operator-configuration-resource-overview_configuring-registry-operator) such as public routing, log levels, proxy settings, resource constraints, replica counts, and storage type.   
`config.samples.operator.openshift.io` |  Configures the [Samples Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#configuring-samples-operator) to control which example image streams and templates are installed on the cluster.   
Show more

## 4.1.3. Additional configuration resources

Review the additional configuration resources that represent a single instance of a particular OpenShift Container Platform component. 

These configuration resources represent a single instance of a particular component. In some cases, you can request multiple instances by creating multiple instances of the resource. In other cases, the Operator can use only a specific resource instance name in a specific namespace. Reference the component-specific documentation for details on how and when you can create additional resource instances. 

Resource name| Instance name| Namespace| Description  
---|---|---|---  
`alertmanager.monitoring.coreos.com` |  `main` |  `openshift-monitoring` |  Controls the [Alertmanager](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_core_platform_monitoring/configuring-alerts-and-notifications) deployment parameters.   
`ingresscontroller.operator.openshift.io` |  `default` |  `openshift-ingress-operator` |  Configures [Ingress Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#configuring-ingress-controller) behavior such as domain, number of replicas, certificates, and controller placement.   
Show more

## 4.1.4. Informational resources

Review the informational resources that you can use to retrieve information about an OpenShift Container Platform cluster. 

You use these resources to retrieve information about the cluster. Some configurations might require you to edit these resources directly. 

Resource name| Instance name| Description  
---|---|---  
`clusterversion.config.openshift.io` |  `version` |  In OpenShift Container Platform 4.22, you must not customize the `ClusterVersion` resource for production clusters. Instead, follow the process to [update a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-web-console).   
`dns.config.openshift.io` |  `cluster` |  You cannot modify the DNS settings for your cluster. You can [check the DNS Operator status](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-dns-operator-status_dns-operator).   
`infrastructure.config.openshift.io` |  `cluster` |  Configuration details allowing the cluster to interact with its cloud provider.   
`network.config.openshift.io` |  `cluster` |  You cannot modify your cluster networking after installation. To customize your network, follow the process to [customize networking during installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations).   
Show more
