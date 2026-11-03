# 2.2. Prepare your cluster for users after installation

Configure a production cluster for users before they access it. 

Some configuration is not required to install the cluster but recommended before your users access the cluster. You can customize the cluster itself by [customizing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations) the Operators that make up your cluster and integrate you cluster with other required systems, such as an identity provider. 

For a production cluster, you must configure the following integrations: 

  * [Persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#understanding-persistent-storage)
  * [An identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-identity-provider)
  * [Monitoring core OpenShift Container Platform components](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/getting_started/core-platform-monitoring-first-steps)
