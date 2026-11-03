# 3.2. About installations in restricted networks

You can install OpenShift Container Platform 4.22 in a restricted network that lacks an active internet connection. These restricted installations use installer-provisioned or user-provisioned infrastructure, depending on your cloud platform. 

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and contains the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions. 

Important

Because of the complexity of the configuration for user-provisioned installations, consider completing a standard user-provisioned infrastructure installation before you try a restricted network installation using user-provisioned infrastructure. Completing this test installation might make it easier to isolate and troubleshoot any issues that might arise during your installation in a restricted network. 

## 3.2.1. Additional limits

Clusters in restricted networks have the following additional limitations and restrictions: 

  * The `ClusterVersion` status includes an `Unable to retrieve available updates` error. 
  * By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.
