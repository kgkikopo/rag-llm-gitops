# 3.3. Migration considerations

Review the changes and other considerations that might affect your transition from OpenShift Container Platform 3.11 to OpenShift Container Platform 4. 

## 3.3.1. Storage considerations

Review the following storage changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22. 

### 3.3.1.1. Local volume persistent storage

Local storage is only supported by using the Local Storage Operator in OpenShift Container Platform 4.22. It is not supported to use the local provisioner method from OpenShift Container Platform 3.11. 

For more information, see [Persistent storage using local volumes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-local-volume). 

### 3.3.1.2. FlexVolume persistent storage

The FlexVolume plugin location changed from OpenShift Container Platform 3.11. The new location in OpenShift Container Platform 4.22 is `/etc/kubernetes/kubelet-plugins/volume/exec`. Attachable FlexVolume plugins are no longer supported. 

For more information, see [Persistent storage using FlexVolume](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-flexvolume). 

### 3.3.1.3. Container Storage Interface (CSI) persistent storage

Persistent storage using the Container Storage Interface (CSI) was [Technology Preview](https://access.redhat.com/support/offerings/techpreview) in OpenShift Container Platform 3.11. OpenShift Container Platform 4.22 includes with [several CSI drivers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-drivers-supported_persistent-storage-csi). You can also install your own driver. 

For more information, see [Persistent storage using the Container Storage Interface (CSI)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-csi). 

### 3.3.1.4. Red Hat OpenShift Data Foundation

OpenShift Container Storage 3, which is available for use with OpenShift Container Platform 3.11, uses Red Hat Gluster Storage as the backing storage. 

Red Hat OpenShift Data Foundation 4, which is available for use with OpenShift Container Platform 4, uses Red Hat Ceph Storage as the backing storage. 

For more information, see [Persistent storage using Red Hat OpenShift Data Foundation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#red-hat-openshift-data-foundation) and the [interoperability matrix](https://access.redhat.com/articles/4731161) article. 

### 3.3.1.5. Unsupported persistent storage options

Support for the following persistent storage options from OpenShift Container Platform 3.11 has changed in OpenShift Container Platform 4.22: 

  * GlusterFS is no longer supported. 
  * CephFS as a standalone product is no longer supported. 
  * Ceph RBD as a standalone product is no longer supported. 



If you used one of these in OpenShift Container Platform 3.11, you must choose a different persistent storage option for full support in OpenShift Container Platform 4.22. 

For more information, see [Understanding persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#understanding-persistent-storage). 

### 3.3.1.6. Migration of in-tree volumes to CSI drivers

OpenShift Container Platform 4 is migrating in-tree volume plugins to their Container Storage Interface (CSI) counterparts. In OpenShift Container Platform 4.22, CSI drivers are the new default for the following in-tree volume types: 

  * Amazon Web Services (AWS) Elastic Block Storage (EBS) 
  * Azure Disk 
  * Azure File 
  * Google Cloud Persistent Disk (GCP PD) 
  * OpenStack Cinder 
  * VMware vSphere 

Note

As of OpenShift Container Platform 4.13, VMware vSphere is not available by default. However, you can opt into VMware vSphere. 




All aspects of volume lifecycle, such as creation, deletion, mounting, and unmounting, is handled by the CSI driver. 

For more information, see [CSI automatic migration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-migration). 

## 3.3.2. Networking considerations

Review the following networking changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22. 

### 3.3.2.1. Network isolation mode

The default network isolation mode for OpenShift Container Platform 3.11 was `ovs-subnet`, though users frequently switched to use `ovn-multitenant`. The default network isolation mode for OpenShift Container Platform 4.22 is controlled by a network policy. 

If your OpenShift Container Platform 3.11 cluster used the `ovs-subnet` or `ovs-multitenant` mode, it is recommended to switch to a network policy for your OpenShift Container Platform 4.22 cluster. Network policies are supported upstream, are more flexible, and they provide the functionality that `ovs-multitenant` does. If you want to maintain the `ovs-multitenant` behavior while using a network policy in OpenShift Container Platform 4.22, follow the steps to [configure multitenant isolation using network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#multitenant-network-policy). 

For more information, see [About network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#about-network-policy). 

### 3.3.2.2. OVN-Kubernetes as the default networking plugin in Red Hat OpenShift Networking

In OpenShift Container Platform 3.11, OpenShift SDN was the default networking plugin in Red Hat OpenShift Networking. In OpenShift Container Platform 4.22, OVN-Kubernetes is now the default networking plugin. 

For more information on the removal of the OpenShift SDN network plugin and why it has been removed see [OpenShiftSDN CNI removal in OCP 4.17](https://access.redhat.com/articles/7065170). 

For information on OVN-Kubernetes features that are similar to features in the OpenShift SDN plugin see: 

  * [Configuring an egress IP address](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#configuring-egress-ips)
  * [Configuring an egress firewall for a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-egress-firewall-ovn)
  * [Enabling multicast for a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#enabling-multicast)
  * [Deploying an egress router pod in redirect mode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#deploying-egress-router-ovn-redirection)
  * [Configuring multitenant isolation with network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#multitenant-network-policy)



Warning

You should install OpenShift Container Platform 4 with the OVN-Kubernetes network plugin because it is not possible to upgrade a cluster to OpenShift Container Platform 4.17 or later if it is using the OpenShift SDN network plugin. 

## 3.3.3. Logging considerations

Review the following logging changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22. 

### 3.3.3.1. Deploying OpenShift Logging

OpenShift Container Platform 4 provides a simple deployment mechanism for OpenShift Logging, by using a Cluster Logging custom resource. 

### 3.3.3.2. Aggregated logging data

You cannot transition your aggregate logging data from OpenShift Container Platform 3.11 into your new OpenShift Container Platform 4 cluster. 

### 3.3.3.3. Unsupported logging configurations

Some logging configurations that were available in OpenShift Container Platform 3.11 are no longer supported in OpenShift Container Platform 4.22. 

## 3.3.4. Security considerations

Review the following security changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22. 

### 3.3.4.1. Unauthenticated access to discovery endpoints

In OpenShift Container Platform 3.11, an unauthenticated user could access the discovery endpoints (for example, `/api/*` and `/apis/*`). For security reasons, unauthenticated access to the discovery endpoints is no longer allowed in OpenShift Container Platform 4.22. If you do need to allow unauthenticated access, you can configure the RBAC settings as necessary; however, be sure to consider the security implications as this can expose internal cluster components to the external network. 

### 3.3.4.2. Identity providers

Configuration for identity providers has changed for OpenShift Container Platform 4, including the following notable changes: 

  * The request header identity provider in OpenShift Container Platform 4.22 requires mutual TLS, where in OpenShift Container Platform 3.11 it did not. 
  * The configuration of the OpenID Connect identity provider was simplified in OpenShift Container Platform 4.22. It now obtains data, which previously had to specified in OpenShift Container Platform 3.11, from the provider’s `/.well-known/openid-configuration` endpoint. 



For more information, see [Understanding identity provider configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-identity-provider). 

### 3.3.4.3. OAuth token storage format

Newly created OAuth HTTP bearer tokens no longer match the names of their OAuth access token objects. The object names are now a hash of the bearer token and are no longer sensitive. This reduces the risk of leaking sensitive information. 

### 3.3.4.4. Default security context constraints

The `restricted` security context constraints (SCC) in OpenShift Container Platform 4 can no longer be accessed by any authenticated user as the `restricted` SCC in OpenShift Container Platform 3.11. The broad authenticated access is now granted to the `restricted-v2` SCC, which is more restrictive than the old `restricted` SCC. The `restricted` SCC still exists; users that want to use it must be specifically given permissions to do it. 

For more information, see [Managing security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#managing-pod-security-policies). 

## 3.3.5. Monitoring considerations

Review the following monitoring changes when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22. You cannot migrate Hawkular configurations and metrics to Prometheus. 

### 3.3.5.1. Alert for monitoring infrastructure availability

The default alert that triggers to ensure the availability of the monitoring structure was called `DeadMansSwitch` in OpenShift Container Platform 3.11. This was renamed to `Watchdog` in OpenShift Container Platform 4. If you had PagerDuty integration set up with this alert in OpenShift Container Platform 3.11, you must set up the PagerDuty integration for the `Watchdog` alert in OpenShift Container Platform 4. 

For more information, see [Configuring alert routing for default platform alerts](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_core_platform_monitoring/configuring-alerts-and-notifications#configuring-alert-routing-default-platform-alerts_configuring-alerts-and-notifications).
